"""Local deployment configuration for hybrid OCP knowledge answering."""

from __future__ import annotations

import os

from pydantic import BaseModel, Field


class KnowledgeSettings(BaseModel):
    qdrant_url: str = "http://localhost:6333"
    collection_name: str = "ocp-documents"
    document_version: str = "4.22"
    embedding_model: str = "BAAI/bge-m3"
    reranker_model: str = "BAAI/bge-reranker-v2-m3"
    llm_model: str = "qwen3.5:4b"
    llm_base_url: str = "http://localhost:11434/v1"
    retrieval_limit: int = Field(default=30, gt=0)
    rerank_input_limit: int = Field(default=20, gt=0)
    context_limit: int = Field(default=10, gt=0)
    rrf_constant: int = Field(default=60, ge=0)

    @classmethod
    def from_env(cls) -> "KnowledgeSettings":
        values: dict[str, object] = {}
        mapping = {
            "qdrant_url": "OCP_KNOWLEDGE_QDRANT_URL",
            "collection_name": "OCP_KNOWLEDGE_COLLECTION_NAME",
            "document_version": "OCP_KNOWLEDGE_DOCUMENT_VERSION",
            "embedding_model": "OCP_KNOWLEDGE_EMBEDDING_MODEL",
            "reranker_model": "OCP_KNOWLEDGE_RERANKER_MODEL",
            "llm_model": "OCP_KNOWLEDGE_LLM_MODEL",
            "llm_base_url": "OCP_KNOWLEDGE_LLM_BASE_URL",
        }
        for field, env_name in mapping.items():
            if value := os.getenv(env_name):
                values[field] = value
        for field in ("retrieval_limit", "rerank_input_limit", "context_limit", "rrf_constant"):
            if value := os.getenv(f"OCP_KNOWLEDGE_{field.upper()}"):
                values[field] = int(value)
        return cls.model_validate(values)


knowledge_settings = KnowledgeSettings.from_env()
