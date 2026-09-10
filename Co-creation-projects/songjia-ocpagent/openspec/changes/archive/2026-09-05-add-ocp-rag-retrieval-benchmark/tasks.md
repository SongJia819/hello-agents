## 1. Benchmark Fixture

- [x] 1.1 Define and implement strict loading and validation for the versioned
  JSON benchmark fixture schema.
- [x] 1.2 Inspect the OCP 4.22 Qdrant corpus and curate exactly 250 questions
  across installation, nodes, workloads, networking, storage, security,
  operators, observability, backup, and upgrades.
- [x] 1.3 Assign non-empty expected stable point-ID sets to every case and
  validate that each ID exists with document version `4.22`.

## 2. Retrieval Evaluation

- [x] 2.1 Add a standalone benchmark module under `backend/app/knowledge` with
  CLI configuration for fixture, version, Qdrant endpoint, collection, models,
  limits, case selection, and output directory.
- [x] 2.2 Reuse the version-filtered BGE-M3 dense and sparse retrieval path and
  implement deterministic RRF and BGE reranking without invoking an LLM.
- [x] 2.3 Implement per-case deduplication, expected-ID matching, and
  precision/recall calculation for dense, sparse, RRF, and reranked stages.
- [x] 2.4 Continue independent cases after runtime failures and distinguish
  fixture validation failures from scored retrieval results.

## 3. Reporting

- [x] 3.1 Generate timestamped JSON reports containing configuration,
  completion/failure counts, aggregate stage metrics, and per-case diagnostics.
- [x] 3.2 Generate equivalent Markdown reports and print both report paths at
  the end of a benchmark run.

## 4. Verification

- [x] 4.1 Add offline tests with fake retrievers and rerankers for fixture
  validation, set-based precision/recall, aggregate metrics, and report
  rendering.
- [x] 4.2 Run focused unit tests and static checks without Qdrant, BGE models,
  or Ollama.
- [x] 4.3 Run all 250 OCP 4.22 cases against the local Qdrant corpus and verify
  that the generated reports include every case and all retrieval stages.
