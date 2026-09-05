"""Interactively test versioned OCP hybrid RAG against local Qdrant and Ollama."""

from __future__ import annotations

import argparse
import json
import logging
import re
import sys
from dataclasses import asdict, dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Sequence

from langchain_classic.retrievers import EnsembleRetriever
from langchain_core.documents import Document
from langchain_core.documents.compressor import BaseDocumentCompressor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.retrievers import BaseRetriever
from pydantic import ConfigDict, Field
from qdrant_client import QdrantClient, models

from app.knowledge.ingest_ocp_docs import (
    COLLECTION_NAME,
    DENSE_VECTOR_NAME,
    DEFAULT_MODEL_NAME,
    QDRANT_URL,
    SPARSE_VECTOR_NAME,
    BgeM3HybridEmbeddings,
    IngestionError,
    ensure_collection,
)


DEFAULT_DOCUMENT_VERSION = "4.22"
DEFAULT_RERANKER_MODEL = "BAAI/bge-reranker-v2-m3"
DEFAULT_OLLAMA_MODEL = "qwen3.5:4b"
DEFAULT_OLLAMA_URL = "http://localhost:11434"
RETRIEVAL_LIMIT = 30
RERANK_INPUT_LIMIT = 20
CONTEXT_LIMIT = 10
RRF_CONSTANT = 60
LOG_PATH = Path(__file__).with_name("hybrid_rag_test.log")
CITATION_PATTERN = re.compile(r"\[chunk:([0-9a-fA-F-]+)\]")
PARENTHESIZED_CITATION_PATTERN = re.compile(r"\(chunk:([0-9a-fA-F-]+)\)")


class RetrievalError(RuntimeError):
    """A recoverable failure in the local RAG evaluation pipeline."""


@dataclass(frozen=True)
class PipelineConfig:
    document_version: str = DEFAULT_DOCUMENT_VERSION
    qdrant_url: str = QDRANT_URL
    collection_name: str = COLLECTION_NAME
    embedding_model: str = DEFAULT_MODEL_NAME
    reranker_model: str = DEFAULT_RERANKER_MODEL
    ollama_url: str = DEFAULT_OLLAMA_URL
    ollama_model: str = DEFAULT_OLLAMA_MODEL
    retrieval_limit: int = RETRIEVAL_LIMIT
    rerank_input_limit: int = RERANK_INPUT_LIMIT
    context_limit: int = CONTEXT_LIMIT
    rrf_constant: int = RRF_CONSTANT


@dataclass(frozen=True)
class PipelineResult:
    answer: str
    dense_documents: list[Document]
    sparse_documents: list[Document]
    fused_documents: list[Document]
    reranked_documents: list[Document]
    citations: list[str]


class StaticRetriever(BaseRetriever):
    """Expose already-fetched documents to LangChain EnsembleRetriever."""

    documents: list[Document] = Field(default_factory=list)

    def _get_relevant_documents(self, _query: str, *, run_manager: Any) -> list[Document]:
        return self.documents


class QdrantNamedVectorRetriever(BaseRetriever):
    """LangChain retriever backed by one Qdrant named vector."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    client: Any = Field(exclude=True)
    collection_name: str
    vector_name: str
    query_vector: list[float] | models.SparseVector
    document_version: str
    limit: int = RETRIEVAL_LIMIT

    def _get_relevant_documents(self, _query: str, *, run_manager: Any) -> list[Document]:
        response = self.client.query_points(
            collection_name=self.collection_name,
            query=self.query_vector,
            using=self.vector_name,
            query_filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="document_version",
                        match=models.MatchValue(value=self.document_version),
                    )
                ]
            ),
            limit=self.limit,
            with_payload=True,
            with_vectors=False,
        )
        documents: list[Document] = []
        for rank, point in enumerate(response.points, start=1):
            payload = dict(point.payload or {})
            content = payload.pop("content", None)
            if not isinstance(content, str) or not content.strip():
                continue
            payload.update(
                {
                    "point_id": str(point.id),
                    "retrieval_rank": rank,
                    "retrieval_score": float(point.score),
                    "retrieval_mode": self.vector_name,
                }
            )
            documents.append(Document(page_content=content, metadata=payload))
        return documents


class BgeRerankerCompressor(BaseDocumentCompressor):
    """LangChain document compressor using BGE reranking scores."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    reranker: Any = Field(exclude=True)

    def compress_documents(
        self, documents: Sequence[Document], query: str, callbacks: Any = None
    ) -> Sequence[Document]:
        del callbacks
        pairs = [[query, document.page_content] for document in documents]
        if not pairs:
            return []
        scores = self.reranker.compute_score(pairs, normalize=True)
        if not isinstance(scores, list):
            scores = [scores]
        ranked = []
        for document, score in zip(documents, scores, strict=True):
            metadata = {**document.metadata, "rerank_score": float(score)}
            ranked.append(Document(page_content=document.page_content, metadata=metadata))
        return sorted(ranked, key=lambda document: document.metadata["rerank_score"], reverse=True)


def configure_logger(path: Path = LOG_PATH) -> logging.Logger:
    logger = logging.getLogger(f"hybrid-rag-test:{path}")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(path, encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(handler)
        logger.propagate = False
    return logger


def _chunk_record(document: Document, rank: int) -> dict[str, Any]:
    metadata = document.metadata
    return {
        "rank": rank,
        "point_id": metadata.get("point_id"),
        "source_path": metadata.get("source_path"),
        "heading_path": metadata.get("heading_path"),
        "document_version": metadata.get("document_version"),
        "retrieval_mode": metadata.get("retrieval_mode"),
        "retrieval_rank": metadata.get("retrieval_rank"),
        "retrieval_score": metadata.get("retrieval_score"),
        "rerank_score": metadata.get("rerank_score"),
        "content": document.page_content,
    }


def log_run(
    logger: logging.Logger,
    question: str,
    config: PipelineConfig,
    stages: dict[str, Sequence[Document]],
    *,
    answer: str | None = None,
    citations: Sequence[str] = (),
    error: str | None = None,
) -> None:
    logger.info(
        json.dumps(
            {
                "timestamp": datetime.now(UTC).isoformat(),
                "question": question,
                "config": asdict(config),
                "stages": {
                    name: [_chunk_record(document, rank) for rank, document in enumerate(documents, 1)]
                    for name, documents in stages.items()
                },
                "answer": answer,
                "citations": list(citations),
                "error": error,
            },
            ensure_ascii=False,
        )
    )


def create_reranker(model_name: str) -> Any:
    try:
        from FlagEmbedding import FlagReranker
    except ImportError as error:
        raise RetrievalError("FlagEmbedding is required; install backend requirements") from error
    return FlagReranker(model_name, use_fp16=False)


def create_chat_model(model_name: str, base_url: str) -> Any:
    try:
        from langchain_ollama import ChatOllama
    except ImportError as error:
        raise RetrievalError("langchain-ollama is required; install backend requirements") from error
    return ChatOllama(model=model_name, base_url=base_url, temperature=0)


def _sparse_vector(weights: dict[int, float]) -> models.SparseVector:
    return models.SparseVector(indices=list(weights), values=list(weights.values()))


def _validate_collection(client: Any, config: PipelineConfig, dense_size: int) -> None:
    try:
        ensure_collection(client, config.collection_name, dense_size)
    except IngestionError as error:
        raise RetrievalError(str(error)) from error


def retrieve_documents(
    question: str,
    config: PipelineConfig,
    embeddings: BgeM3HybridEmbeddings,
    client: Any,
) -> tuple[list[Document], list[Document]]:
    vectors = embeddings.embed_hybrid([question])
    if not vectors or not vectors[0][0]:
        raise RetrievalError("BGE-M3 returned no query embedding")
    dense, sparse = vectors[0]
    _validate_collection(client, config, len(dense))
    dense_retriever = QdrantNamedVectorRetriever(
        client=client,
        collection_name=config.collection_name,
        vector_name=DENSE_VECTOR_NAME,
        query_vector=dense,
        document_version=config.document_version,
        limit=config.retrieval_limit,
    )
    sparse_retriever = QdrantNamedVectorRetriever(
        client=client,
        collection_name=config.collection_name,
        vector_name=SPARSE_VECTOR_NAME,
        query_vector=_sparse_vector(sparse),
        document_version=config.document_version,
        limit=config.retrieval_limit,
    )
    return dense_retriever.invoke(question), sparse_retriever.invoke(question)


def fuse_documents(dense: Sequence[Document], sparse: Sequence[Document], config: PipelineConfig) -> list[Document]:
    """Use LangChain's RRF ensemble over the already-observed ranked lists."""

    ensemble = EnsembleRetriever(
        retrievers=[StaticRetriever(documents=list(dense)), StaticRetriever(documents=list(sparse))],
        weights=[0.5, 0.5],
        c=config.rrf_constant,
        id_key="point_id",
    )
    fused = ensemble.invoke("fixed hybrid fusion")
    for rank, document in enumerate(fused, start=1):
        document.metadata["rrf_rank"] = rank
    return fused


def rerank_documents(
    question: str, documents: Sequence[Document], reranker: Any, config: PipelineConfig
) -> tuple[list[Document], list[Document]]:
    reranker_input = list(documents[: config.rerank_input_limit])
    compressor = BgeRerankerCompressor(reranker=reranker)
    reranked = list(compressor.compress_documents(reranker_input, question))[: config.context_limit]
    for rank, document in enumerate(reranked, start=1):
        document.metadata["rerank_rank"] = rank
    return reranker_input, reranked


def build_prompt(question: str, documents: Sequence[Document]) -> list[Any]:
    context = "\n\n".join(
        f"[chunk:{document.metadata['point_id']}]\n{document.page_content}" for document in documents
    )
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "Answer only from the supplied OCP documentation context. "
                "Every factual answer must cite one or more [chunk:<point-id>] labels from the context. "
                "Use square brackets exactly, for example [chunk:123e4567-e89b-12d3-a456-426614174000]; "
                "do not use parentheses or any other citation syntax. "
                "If the context is insufficient, say so and cite the closest relevant chunk.",
            ),
            ("human", "Question:\n{question}\n\nContext:\n{context}"),
        ]
    )
    return prompt.format_messages(question=question, context=context)


def normalize_citation_syntax(answer: str) -> str:
    """Normalize the local model's common parenthesized chunk citation form."""

    return PARENTHESIZED_CITATION_PATTERN.sub(r"[chunk:\1]", answer)


def validate_citations(answer: str, documents: Sequence[Document]) -> list[str]:
    """Extract model-supplied chunk labels without rejecting its answer."""

    del documents
    return CITATION_PATTERN.findall(answer)


def answer_question(
    question: str,
    config: PipelineConfig,
    *,
    client: Any | None = None,
    embeddings: BgeM3HybridEmbeddings | None = None,
    reranker: Any | None = None,
    chat_model: Any | None = None,
    logger: logging.Logger | None = None,
) -> PipelineResult:
    logger = logger or configure_logger()
    stages: dict[str, Sequence[Document]] = {"dense": [], "sparse": [], "rrf": [], "rerank_input": [], "reranked": [], "llm_context": []}
    answer: str | None = None
    citations: list[str] = []
    try:
        embeddings = embeddings or BgeM3HybridEmbeddings(config.embedding_model)
        client = client or QdrantClient(url=config.qdrant_url)
        dense, sparse = retrieve_documents(question, config, embeddings, client)
        stages["dense"], stages["sparse"] = dense, sparse
        fused = fuse_documents(dense, sparse, config)
        stages["rrf"] = fused
        if not fused:
            raise RetrievalError("No supporting documentation was found for this version")
        reranker = reranker or create_reranker(config.reranker_model)
        rerank_input, reranked = rerank_documents(question, fused, reranker, config)
        stages["rerank_input"], stages["reranked"], stages["llm_context"] = rerank_input, reranked, reranked
        if not reranked:
            raise RetrievalError("BGE reranker returned no supporting chunks")
        chat_model = chat_model or create_chat_model(config.ollama_model, config.ollama_url)
        response = chat_model.invoke(build_prompt(question, reranked))
        answer = normalize_citation_syntax(str(response.content))
        citations = validate_citations(answer, reranked)
    except Exception as error:
        log_run(logger, question, config, stages, answer=answer, citations=citations, error=str(error))
        if isinstance(error, RetrievalError):
            raise
        raise RetrievalError(str(error)) from error
    log_run(logger, question, config, stages, answer=answer, citations=citations)
    return PipelineResult(answer, list(dense), list(sparse), list(fused), list(reranked), citations)


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--document-version", default=DEFAULT_DOCUMENT_VERSION)
    parser.add_argument("--qdrant-url", default=QDRANT_URL)
    parser.add_argument("--collection-name", default=COLLECTION_NAME)
    parser.add_argument("--embedding-model", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--reranker-model", default=DEFAULT_RERANKER_MODEL)
    parser.add_argument("--ollama-url", default=DEFAULT_OLLAMA_URL)
    parser.add_argument("--ollama-model", default=DEFAULT_OLLAMA_MODEL)
    parser.add_argument("--retrieval-limit", type=int, default=RETRIEVAL_LIMIT)
    parser.add_argument("--rerank-input-limit", type=int, default=RERANK_INPUT_LIMIT)
    parser.add_argument("--context-limit", type=int, default=CONTEXT_LIMIT)
    parser.add_argument("--rrf-constant", type=int, default=RRF_CONSTANT)
    return parser.parse_args(argv)


def config_from_args(args: argparse.Namespace) -> PipelineConfig:
    config = PipelineConfig(**vars(args))
    if config.retrieval_limit != RETRIEVAL_LIMIT:
        raise RetrievalError(f"retrieval limit must be {RETRIEVAL_LIMIT} for each vector mode")
    if config.rerank_input_limit != RERANK_INPUT_LIMIT or config.context_limit != CONTEXT_LIMIT:
        raise RetrievalError(
            f"rerank input limit must be {RERANK_INPUT_LIMIT} and context limit must be {CONTEXT_LIMIT}"
        )
    return config


def print_result(result: PipelineResult) -> None:
    print("\nAnswer:\n" + result.answer)
    print("\nSupporting chunks:")
    for document in result.reranked_documents:
        print(
            f"[chunk:{document.metadata['point_id']}] "
            f"{document.metadata.get('source_path')} | {document.metadata.get('heading_path')} | "
            f"score={document.metadata.get('rerank_score'):.4f}"
        )


def main(argv: Sequence[str] | None = None, input_fn: Any = input) -> int:
    try:
        config = config_from_args(parse_args(argv))
    except RetrievalError as error:
        print(f"Configuration failed: {error}", file=sys.stderr)
        return 2
    logger = configure_logger()
    print("Ask an OCP documentation question. Type 'exit' to quit.")
    while True:
        try:
            question = input_fn("ocp> ").strip()
        except EOFError:
            return 0
        if question.lower() in {"exit", "quit"}:
            return 0
        if not question:
            continue
        try:
            print_result(answer_question(question, config, logger=logger))
        except RetrievalError as error:
            print(f"RAG evaluation failed: {error}", file=sys.stderr)


if __name__ == "__main__":
    raise SystemExit(main())
