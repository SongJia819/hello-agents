## Why

The current hybrid RAG test script supports inspecting one question at a time,
but it cannot measure whether retrieval quality changes across the OCP 4.22
corpus. A repeatable benchmark with corpus-grounded expected chunks is needed
to report retrieval precision and recall before changing retrieval settings.

## What Changes

- Add a standalone knowledge benchmark script that executes configured OCP RAG
  queries in batch against a selected document version.
- Add a version-aware JSON benchmark configuration containing 250 curated OCP
  4.22 questions and their verified expected Qdrant chunk identifiers.
- Measure precision and recall at top-10, top-20, and top-30 for dense
  retrieval, sparse retrieval, RRF fusion, and BGE reranking, with per-case and
  aggregate results.
- Generate machine-readable JSON and human-readable Markdown reports, including
  configuration, stage metrics, missing expected chunks, and execution errors.
- Add focused tests using fakes so metric computation and report generation do
  not require Qdrant or local embedding models.

## Capabilities

### New Capabilities
- `ocp-rag-retrieval-benchmark`: Runs a version-filtered hybrid retrieval
  benchmark against expected OCP documentation chunks and reports quality
  metrics.

### Modified Capabilities
- None.

## Impact

- Adds a benchmark script, benchmark configuration, generated-report output
  location, and unit tests under `backend/app/knowledge` and `backend/tests`.
- Reuses the existing versioned Qdrant `ocp-documents` collection and BGE-M3 /
  BGE reranker query path without changing corpus ingestion or Qdrant data.
- Requires a locally available Qdrant collection when running the real 250-case
  benchmark; unit tests remain offline.
