"""Typed contracts for the runtime OCP documentation-answering pipeline."""

from __future__ import annotations

from pydantic import BaseModel, Field


class KnowledgeRequest(BaseModel):
    question: str = Field(min_length=1)
    document_version: str | None = None


class KnowledgeChunk(BaseModel):
    point_id: str
    content: str
    source_path: str = ""
    heading_path: str = ""
    document_version: str = ""
    retrieval_mode: str | None = None
    retrieval_rank: int | None = None
    retrieval_score: float | None = None
    rrf_rank: int | None = None
    rrf_score: float | None = None
    rerank_rank: int | None = None
    rerank_score: float | None = None


class RetrievalDiagnostics(BaseModel):
    dense: list[KnowledgeChunk] = Field(default_factory=list)
    sparse: list[KnowledgeChunk] = Field(default_factory=list)
    fused: list[KnowledgeChunk] = Field(default_factory=list)
    reranked: list[KnowledgeChunk] = Field(default_factory=list)


class KnowledgeResult(BaseModel):
    answer: str = ""
    citations: list[str] = Field(default_factory=list)
    diagnostics: RetrievalDiagnostics = Field(default_factory=RetrievalDiagnostics)
    failure_reason: str | None = None

    @property
    def successful(self) -> bool:
        return self.failure_reason is None and bool(self.answer)
