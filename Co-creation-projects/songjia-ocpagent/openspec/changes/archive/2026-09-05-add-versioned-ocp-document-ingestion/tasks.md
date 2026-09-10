## 1. Legacy Script Isolation And Command Setup

- [x] 1.1 Move legacy `ingest.py`, `re-rank.py`, and `test_retrieval.py` to
  `backend/app/knowledge/test/` without modifying their implementation.
- [x] 1.2 Add the LangChain, Qdrant, and BGE-M3-compatible dependencies needed
  for hybrid ingestion.
- [x] 1.3 Create a new separately named configurable knowledge ingestion
  command; do not modify the relocated legacy `ingest.py`.
- [x] 1.4 Resolve and validate the selected `ocp-<version>` Markdown corpus
  without loading other versions.

## 2. Chunking And Metadata

- [x] 2.1 Implement Markdown H1-H6 header splitting followed by bounded
  recursive splitting for oversized sections.
- [x] 2.2 Preserve source path, optional front-matter source URL, heading path,
  chunk ordinal, and `document_version` metadata on every chunk.
- [x] 2.3 Generate deterministic point identifiers for versioned chunks.

## 3. Hybrid Qdrant Ingestion

- [x] 3.1 Implement a LangChain-compatible BGE-M3 adapter that produces dense
  embeddings and sparse lexical vectors.
- [x] 3.2 Create or validate the `ocp-documents` named dense/sparse vector
  schema at the configured Qdrant endpoint.
- [x] 3.3 Batch upsert hybrid points and implement version-filtered replacement
  without deleting another document version.
- [x] 3.4 Report selected version, document/chunk/upsert counts, target
  collection, and failures with non-zero failure status.

## 4. Verification

- [x] 4.1 Add offline tests for version selection, heading-aware chunk metadata,
  deterministic identifiers, sparse/dense payloads, schema validation, and
  version-filtered replacement using fakes.
- [x] 4.2 Run focused automated tests and
  `openspec validate add-versioned-ocp-document-ingestion --strict`.
- [x] 4.3 When Qdrant and BGE-M3 are locally available, ingest OCP 4.22 and
  inspect stored hybrid vectors and document-version metadata.
