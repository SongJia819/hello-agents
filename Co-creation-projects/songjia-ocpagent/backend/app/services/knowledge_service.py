"""Service-layer hybrid retrieval and grounded answer generation."""

from __future__ import annotations

import re
from collections.abc import Sequence
from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage
from qdrant_client import QdrantClient, models

from app.config.knowledge import KnowledgeSettings, knowledge_settings
from app.models.knowledge import KnowledgeChunk, KnowledgeRequest, KnowledgeResult, RetrievalDiagnostics
from app.config.llm import llm_settings
from app.observability import emit_progress
from app.services.llm_streaming import collect_streamed_answer

DENSE_VECTOR_NAME = "dense"
SPARSE_VECTOR_NAME = "sparse"
_CITATION = re.compile(r"\[chunk:([^\]]+)\]")


class KnowledgeServiceError(RuntimeError):
    pass


class QdrantRecallService:
    def __init__(self, settings: KnowledgeSettings, client: Any, embeddings: Any):
        self.settings, self.client, self.embeddings = settings, client, embeddings

    def recall(self, request: KnowledgeRequest) -> tuple[list[KnowledgeChunk], list[KnowledgeChunk]]:
        vectors = self.embeddings.embed_hybrid([request.question])
        if not vectors or not vectors[0][0]:
            raise KnowledgeServiceError("Embedding model returned no query vector")
        dense, sparse = vectors[0]
        version = request.document_version or self.settings.document_version
        return (
            self._search(DENSE_VECTOR_NAME, dense, version),
            self._search(SPARSE_VECTOR_NAME, self._sparse_vector(sparse), version),
        )

    @staticmethod
    def _sparse_vector(weights: dict[int, float]) -> models.SparseVector:
        return models.SparseVector(indices=list(weights), values=list(weights.values()))

    def _search(self, mode: str, vector: Any, version: str) -> list[KnowledgeChunk]:
        response = self.client.query_points(
            collection_name=self.settings.collection_name,
            query=vector,
            using=mode,
            query_filter=models.Filter(must=[models.FieldCondition(
                key="document_version", match=models.MatchValue(value=version)
            )]),
            limit=self.settings.retrieval_limit,
            with_payload=True,
            with_vectors=False,
        )
        chunks = []
        for rank, point in enumerate(response.points, 1):
            payload = dict(point.payload or {})
            content = payload.get("content")
            if isinstance(content, str) and content.strip():
                chunks.append(KnowledgeChunk(
                    point_id=str(point.id), content=content,
                    source_path=str(payload.get("source_path", "")),
                    heading_path=str(payload.get("heading_path", "")),
                    document_version=str(payload.get("document_version", version)),
                    retrieval_mode=mode, retrieval_rank=rank, retrieval_score=float(point.score),
                ))
        return chunks


class RRFFusionService:
    def __init__(self, rrf_constant: int):
        self.rrf_constant = rrf_constant

    def fuse(self, *rankings: Sequence[KnowledgeChunk]) -> list[KnowledgeChunk]:
        by_id: dict[str, tuple[KnowledgeChunk, float]] = {}
        for ranking in rankings:
            for rank, chunk in enumerate(ranking, 1):
                existing, score = by_id.get(chunk.point_id, (chunk, 0.0))
                by_id[chunk.point_id] = (existing, score + 1 / (self.rrf_constant + rank))
        ordered = sorted(by_id.values(), key=lambda item: item[1], reverse=True)
        return [chunk.model_copy(update={"rrf_rank": rank, "rrf_score": score})
                for rank, (chunk, score) in enumerate(ordered, 1)]


class RerankService:
    def __init__(self, settings: KnowledgeSettings, reranker: Any):
        self.settings, self.reranker = settings, reranker

    def rerank(self, question: str, chunks: Sequence[KnowledgeChunk]) -> list[KnowledgeChunk]:
        candidates = list(chunks[: self.settings.rerank_input_limit])
        if not candidates:
            return []
        scores = self.reranker.compute_score([[question, chunk.content] for chunk in candidates], normalize=True)
        if not isinstance(scores, list):
            scores = [scores]
        ordered = sorted(zip(candidates, scores, strict=True), key=lambda pair: pair[1], reverse=True)
        return [chunk.model_copy(update={"rerank_rank": rank, "rerank_score": float(score)})
                for rank, (chunk, score) in enumerate(ordered[: self.settings.context_limit], 1)]


class KnowledgeAnswerService:
    def __init__(self, settings: KnowledgeSettings | None = None, *, recall_service: QdrantRecallService | None = None,
                 fusion_service: RRFFusionService | None = None, rerank_service: RerankService | None = None,
                 chat_model: Any | None = None):
        self.settings = settings or knowledge_settings
        self.recall_service = recall_service
        self.fusion_service = fusion_service or RRFFusionService(self.settings.rrf_constant)
        self.rerank_service = rerank_service
        self.chat_model = chat_model

    def _recall_dependencies(self) -> None:
        if self.recall_service is None:
            from app.knowledge.ingest_ocp_docs import BgeM3HybridEmbeddings
            self.recall_service = QdrantRecallService(
                self.settings, QdrantClient(url=self.settings.qdrant_url),
                BgeM3HybridEmbeddings(self.settings.embedding_model),
            )
    def _rerank_dependencies(self) -> None:
        if self.rerank_service is None:
            from FlagEmbedding import FlagReranker
            self.rerank_service = RerankService(self.settings, FlagReranker(self.settings.reranker_model, use_fp16=False))
    def _chat_dependencies(self) -> None:
        if self.chat_model is None:
            from langchain_openai import ChatOpenAI
            self.chat_model = ChatOpenAI(model=self.settings.llm_model, base_url=self.settings.llm_base_url,
                                         api_key="ollama", temperature=0)

    async def answer(self, request: KnowledgeRequest, state: dict[str, Any] | None = None) -> KnowledgeResult:
        diagnostics = RetrievalDiagnostics()
        state = state or {"user_query": request.question}
        try:
            self._recall_dependencies()
            emit_progress("knowledge", "answer", "recall", "started", "正在召回文档。", state=state)
            diagnostics.dense, diagnostics.sparse = self.recall_service.recall(request)
            emit_progress("knowledge", "answer", "recall", "completed", "文档召回完成。", state=state)
            emit_progress("knowledge", "answer", "rrf", "started", "正在进行 RRF 融合。", state=state)
            diagnostics.fused = self.fusion_service.fuse(diagnostics.dense, diagnostics.sparse)
            emit_progress("knowledge", "answer", "rrf", "completed", "RRF 融合完成。", state=state)
            if not diagnostics.fused:
                return KnowledgeResult(answer="No supporting OCP documentation was found for this question.", diagnostics=diagnostics,
                                       failure_reason="no_supporting_documentation")
            self._rerank_dependencies()
            emit_progress("knowledge", "answer", "rerank", "started", "正在重排序文档。", state=state)
            diagnostics.reranked = self.rerank_service.rerank(request.question, diagnostics.fused)
            emit_progress("knowledge", "answer", "rerank", "completed", "文档重排序完成。", state=state)
            if not diagnostics.reranked:
                return KnowledgeResult(answer="No supporting OCP documentation was found for this question.", diagnostics=diagnostics,
                                       failure_reason="no_reranked_documentation")
            self._chat_dependencies()
            answer = await collect_streamed_answer(
                self.chat_model, self._messages(request.question, diagnostics.reranked),
                agent="knowledge", node="answer", state=state,
                attempts=llm_settings.empty_response_retry_limit,
                fallback="I cannot generate a supporting OCP documentation answer right now.",
            )
            return KnowledgeResult(answer=answer, citations=_CITATION.findall(answer), diagnostics=diagnostics)
        except Exception as error:
            return KnowledgeResult(answer="I cannot retrieve supporting OCP documentation right now.", diagnostics=diagnostics,
                                   failure_reason=str(error))

    @staticmethod
    def _messages(question: str, chunks: Sequence[KnowledgeChunk]) -> list[Any]:
        context = "\n\n".join(f"[chunk:{chunk.point_id}]\n{chunk.content}" for chunk in chunks)
        return [
            SystemMessage(content="Answer only from the supplied OCP documentation context. Cite factual claims with [chunk:<point-id>]. If the context is insufficient, say so."),
            HumanMessage(content=f"Question:\n{question}\n\nContext:\n{context}"),
        ]
