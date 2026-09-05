"""Ingest one versioned OCP Markdown corpus as BGE-M3 hybrid Qdrant points."""

from __future__ import annotations

import argparse
import hashlib
import math
import re
import sys
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Sequence

from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_text_splitters import MarkdownHeaderTextSplitter, RecursiveCharacterTextSplitter
from qdrant_client import QdrantClient, models


QDRANT_URL = "http://localhost:6333"
COLLECTION_NAME = "ocp-documents"
DENSE_VECTOR_NAME = "dense"
SPARSE_VECTOR_NAME = "sparse"
DEFAULT_MODEL_NAME = "BAAI/bge-m3"
DEFAULT_DOCUMENTS_ROOT = Path(__file__).resolve().parent / "docs"
HEADER_METADATA_KEYS = tuple(f"h{level}" for level in range(1, 7))


class IngestionError(RuntimeError):
    """A user-actionable ingestion failure."""


@dataclass(frozen=True)
class IngestionSummary:
    document_version: str
    documents: int
    chunks: int
    upserted: int
    collection_name: str


def corpus_path(documents_root: Path, document_version: str) -> Path:
    """Return the bounded corpus directory for one OCP version."""

    if not document_version or "/" in document_version or "\\" in document_version:
        raise IngestionError("Document version must be a simple value such as 4.22")
    root = documents_root.resolve()
    corpus = (root / f"ocp-{document_version}").resolve()
    if corpus.parent != root:
        raise IngestionError("Document version escaped the documents root")
    if not corpus.is_dir():
        raise IngestionError(f"No Markdown corpus found for OCP {document_version}: {corpus}")
    return corpus


def markdown_files(corpus: Path) -> list[Path]:
    files = sorted(path for path in corpus.rglob("*.md") if path.is_file())
    if not files:
        raise IngestionError(f"No Markdown files found in {corpus}")
    return files


def _front_matter_source_url(markdown: str) -> str | None:
    if not markdown.startswith("---\n"):
        return None
    for line in markdown.split("---\n", 2)[1].splitlines():
        key, separator, value = line.partition(":")
        if separator and key.strip() == "source_url":
            return value.strip().strip('"') or None
    return None


def _heading_path(metadata: dict[str, Any]) -> list[str]:
    return [str(metadata[key]) for key in HEADER_METADATA_KEYS if metadata.get(key)]


def _document_title(markdown: str) -> str | None:
    match = re.search(r"^#\s+(.+?)\s*$", markdown, flags=re.MULTILINE)
    return match.group(1).strip() if match else None


def split_markdown_file(path: Path, corpus: Path, document_version: str, chunk_size: int, chunk_overlap: int) -> list[Document]:
    """Header-split a Markdown file and bound oversized sections."""

    markdown = path.read_text(encoding="utf-8")
    header_splitter = MarkdownHeaderTextSplitter(
        headers_to_split_on=[(f"#{'#' * (level - 1)}", f"h{level}") for level in range(1, 7)],
        strip_headers=False,
    )
    section_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", " ", ""],
    )
    source_path = path.relative_to(corpus).as_posix()
    common_metadata: dict[str, Any] = {
        "source_path": source_path,
        "document_version": document_version,
    }
    title = _document_title(markdown)
    if title:
        common_metadata["document_title"] = title
    source_url = _front_matter_source_url(markdown)
    if source_url:
        common_metadata["source_url"] = source_url

    chunks: list[Document] = []
    for section in header_splitter.split_text(markdown):
        metadata = {**common_metadata, **section.metadata}
        heading_path = _heading_path(metadata)
        metadata["heading_path"] = " > ".join(heading_path)
        children = section_splitter.create_documents([section.page_content], metadatas=[metadata])
        chunks.extend(child for child in children if child.page_content.strip())

    for ordinal, chunk in enumerate(chunks):
        chunk.metadata["chunk_ordinal"] = ordinal
    return chunks


def load_chunks(documents_root: Path, document_version: str, chunk_size: int, chunk_overlap: int) -> tuple[Path, list[Document]]:
    corpus = corpus_path(documents_root, document_version)
    chunks: list[Document] = []
    for path in markdown_files(corpus):
        chunks.extend(split_markdown_file(path, corpus, document_version, chunk_size, chunk_overlap))
    if not chunks:
        raise IngestionError(f"No non-empty Markdown chunks found in {corpus}")
    return corpus, chunks


def point_id(chunk: Document) -> str:
    """Create a stable UUID from all content that identifies a versioned chunk."""

    metadata = chunk.metadata
    material = "\x1f".join(
        [
            str(metadata["document_version"]),
            str(metadata["source_path"]),
            str(metadata.get("heading_path", "")),
            str(metadata["chunk_ordinal"]),
            hashlib.sha256(chunk.page_content.encode("utf-8")).hexdigest(),
        ]
    )
    return str(uuid.uuid5(uuid.NAMESPACE_URL, f"ocp-knowledge/{material}"))


class BgeM3HybridEmbeddings(Embeddings):
    """LangChain embeddings adapter exposing BGE-M3 dense and sparse outputs."""

    def __init__(self, model_name: str = DEFAULT_MODEL_NAME, model: Any | None = None) -> None:
        if model is None:
            try:
                from FlagEmbedding import BGEM3FlagModel
            except ImportError as error:
                raise IngestionError(
                    "FlagEmbedding is required for BGE-M3 ingestion; install backend requirements"
                ) from error
            model = BGEM3FlagModel(model_name, use_fp16=False)
        self.model = model

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        return [dense for dense, _sparse in self.embed_hybrid(texts)]

    def embed_query(self, text: str) -> list[float]:
        return self.embed_documents([text])[0]

    def embed_hybrid(self, texts: Sequence[str]) -> list[tuple[list[float], dict[int, float]]]:
        if not texts:
            return []
        result = self.model.encode(
            list(texts),
            return_dense=True,
            return_sparse=True,
            return_colbert_vecs=False,
        )
        dense_vectors = result.get("dense_vecs")
        sparse_vectors = result.get("lexical_weights")
        if dense_vectors is None or sparse_vectors is None or len(dense_vectors) != len(texts):
            raise IngestionError("BGE-M3 did not return dense and sparse vectors for every chunk")
        vectors: list[tuple[list[float], dict[int, float]]] = []
        for dense, sparse in zip(dense_vectors, sparse_vectors, strict=True):
            values = dense.tolist() if hasattr(dense, "tolist") else dense
            dense_values = [float(value) for value in values]
            magnitude = math.sqrt(sum(value * value for value in dense_values))
            if magnitude == 0:
                raise IngestionError("BGE-M3 returned a zero dense embedding")
            lexical = {int(index): float(weight) for index, weight in sparse.items() if float(weight) != 0}
            vectors.append(([value / magnitude for value in dense_values], lexical))
        return vectors


def _collection_vectors(collection: Any) -> tuple[Any, Any]:
    params = collection.config.params
    return params.vectors, params.sparse_vectors


def ensure_collection(client: Any, collection_name: str, dense_size: int) -> None:
    """Create or verify the required named dense/sparse Qdrant schema."""

    if not client.collection_exists(collection_name):
        client.create_collection(
            collection_name=collection_name,
            vectors_config={
                DENSE_VECTOR_NAME: models.VectorParams(size=dense_size, distance=models.Distance.COSINE)
            },
            sparse_vectors_config={SPARSE_VECTOR_NAME: models.SparseVectorParams()},
        )

    collection = client.get_collection(collection_name)
    dense_vectors, sparse_vectors = _collection_vectors(collection)
    dense = dense_vectors.get(DENSE_VECTOR_NAME) if isinstance(dense_vectors, dict) else None
    sparse = sparse_vectors.get(SPARSE_VECTOR_NAME) if isinstance(sparse_vectors, dict) else None
    if dense is None or sparse is None:
        raise IngestionError(
            f"Collection {collection_name!r} must define named vectors "
            f"{DENSE_VECTOR_NAME!r} and {SPARSE_VECTOR_NAME!r}"
        )
    if dense.size != dense_size or dense.distance != models.Distance.COSINE:
        raise IngestionError(
            f"Collection {collection_name!r} dense vector must use size {dense_size} and cosine distance"
        )


def delete_version(client: Any, collection_name: str, document_version: str) -> None:
    client.delete(
        collection_name=collection_name,
        points_selector=models.FilterSelector(
            filter=models.Filter(
                must=[
                    models.FieldCondition(
                        key="document_version",
                        match=models.MatchValue(value=document_version),
                    )
                ]
            )
        ),
        wait=True,
    )


def hybrid_points(chunks: Sequence[Document], vectors: Sequence[tuple[list[float], dict[int, float]]]) -> list[Any]:
    if len(chunks) != len(vectors):
        raise IngestionError("Embedding count does not match chunk count")
    points = []
    for chunk, (dense, sparse) in zip(chunks, vectors, strict=True):
        points.append(
            models.PointStruct(
                id=point_id(chunk),
                vector={
                    DENSE_VECTOR_NAME: dense,
                    SPARSE_VECTOR_NAME: models.SparseVector(
                        indices=list(sparse), values=list(sparse.values())
                    ),
                },
                payload={**chunk.metadata, "content": chunk.page_content},
            )
        )
    return points


def batches(items: Sequence[Any], batch_size: int) -> Iterable[Sequence[Any]]:
    if batch_size < 1:
        raise IngestionError("Batch size must be at least 1")
    for start in range(0, len(items), batch_size):
        yield items[start : start + batch_size]


def ingest(
    *,
    documents_root: Path = DEFAULT_DOCUMENTS_ROOT,
    document_version: str,
    qdrant_url: str = QDRANT_URL,
    collection_name: str = COLLECTION_NAME,
    model_name: str = DEFAULT_MODEL_NAME,
    batch_size: int = 32,
    replace_version: bool = False,
    chunk_size: int = 1200,
    chunk_overlap: int = 160,
    embeddings: BgeM3HybridEmbeddings | None = None,
    client: Any | None = None,
) -> IngestionSummary:
    corpus, chunks = load_chunks(documents_root, document_version, chunk_size, chunk_overlap)
    document_count = len(markdown_files(corpus))
    embeddings = embeddings or BgeM3HybridEmbeddings(model_name)
    vectors = embeddings.embed_hybrid([chunk.page_content for chunk in chunks])
    if not vectors or not vectors[0][0]:
        raise IngestionError("BGE-M3 returned no dense embedding values")
    client = client or QdrantClient(url=qdrant_url)
    ensure_collection(client, collection_name, len(vectors[0][0]))
    if replace_version:
        delete_version(client, collection_name, document_version)

    points = hybrid_points(chunks, vectors)
    upserted = 0
    for batch in batches(points, batch_size):
        client.upsert(collection_name=collection_name, points=batch, wait=True)
        upserted += len(batch)
    return IngestionSummary(
        document_version=document_version,
        documents=document_count,
        chunks=len(chunks),
        upserted=upserted,
        collection_name=collection_name,
    )


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--document-version", required=True, help="OCP version, for example 4.22")
    parser.add_argument("--documents-root", type=Path, default=DEFAULT_DOCUMENTS_ROOT)
    parser.add_argument("--qdrant-url", default=QDRANT_URL)
    parser.add_argument("--collection-name", default=COLLECTION_NAME)
    parser.add_argument("--model-name", default=DEFAULT_MODEL_NAME)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--chunk-size", type=int, default=1200)
    parser.add_argument("--chunk-overlap", type=int, default=160)
    parser.add_argument("--replace-version", action="store_true")
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        summary = ingest(**vars(args))
    except Exception as error:
        print(f"Ingestion failed: {error}", file=sys.stderr)
        return 1
    print(
        f"Ingested OCP {summary.document_version}: documents={summary.documents}, "
        f"chunks={summary.chunks}, upserted={summary.upserted}, "
        f"collection={summary.collection_name}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
