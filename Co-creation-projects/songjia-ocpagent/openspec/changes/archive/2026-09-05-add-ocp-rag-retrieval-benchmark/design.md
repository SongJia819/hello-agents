## Context

The versioned OCP knowledge corpus is stored in Qdrant collection
`ocp-documents`. Each point has a stable identifier, `document_version` payload,
and named BGE-M3 `dense` and `sparse` vectors. The existing
`hybrid_rag_test.py` script retrieves the top 30 candidates from each vector,
fuses them with RRF, and reranks the leading candidates, but accepts only one
interactive question and has no expected-result dataset or aggregate metrics.

The benchmark must evaluate the same retrieval behavior without invoking the
local LLM. Expected results must identify actual stored chunk point IDs so the
test measures corpus retrieval rather than subjective generated answers.

## Goals / Non-Goals

**Goals:**
- Provide a repeatable command that evaluates all configured cases for one
  `document_version`.
- Curate 250 OCP 4.22 questions covering the available documentation and label
  each with one or more verified, version-matching Qdrant point IDs.
- Report precision and recall by retrieval stage and ranking cutoff, along with
  enough case-level provenance to diagnose a regression.
- Keep metric and report tests runnable without Qdrant, model downloads, or
  Ollama.

**Non-Goals:**
- Judge LLM answer correctness, citation correctness, latency, or generation
  quality.
- Change ingestion, stored vectors, document chunking, the collection schema,
  or the interactive hybrid RAG script.
- Contact an OpenShift cluster or external services other than the configured
  local Qdrant endpoint during an actual benchmark run.

## Decisions

### Use a JSON benchmark fixture with stable Qdrant point IDs

The implementation will add a versioned JSON fixture under
`backend/app/knowledge` with a schema containing a fixture version, default
document version, and ordered cases. Each case will contain a stable case id,
question, `document_version`, and a non-empty `expected_chunk_ids` list. The
250 initial cases will be selected from actual OCP 4.22 points and their IDs
will be verified before the fixture is accepted.

JSON is selected because it needs no additional runtime dependency and supports
strict schema validation. Free-text expected answers and source URLs were
rejected because they cannot unambiguously identify the chunk used for set-based
retrieval metrics.

### Reuse the deterministic hybrid retrieval path and score every stage

The benchmark will reuse the existing BGE-M3 query encoding, two named-vector
Qdrant searches, RRF logic, and BGE reranker configuration. It will retrieve
the configured dense and sparse depth (default 30), create the fused ranking,
then rerank its configured prefix (default 30) and keep the configured final
depth (default 30). It will not initialize ChatOllama or make an LLM request.

The report will score dense, sparse, RRF, and reranked lists independently at
top-10, top-20, and top-30. Evaluating all stages and cutoffs makes a change in
vector retrieval, fusion, reranking, or ranking depth distinguishable. Scoring
only the final list was rejected because it obscures where recall was lost.

### Define precision and recall with expected-ID set intersection

For each case, scored stage, and `k` in 10, 20, and 30, the implementation will
deduplicate returned point IDs while preserving rank. Let `R` be the first `k`
returned unique IDs and `E` be the non-empty expected ID set. It will calculate:

- `matched = R intersect E`
- `precision_at_k = len(matched) / len(R)`, or `0.0` if `R` is empty
- `recall_at_k = len(matched) / len(E)`

The report will include macro averages across successfully evaluated cases and
micro precision/recall calculated from summed matches, returned counts, and
expected counts. A case whose expected IDs cannot be found with its document
version is a fixture-validation failure, not a zero-score retrieval result.

Using a fixed denominator of `k` for precision was rejected because an empty or
short result set would be reported as lower quality without distinguishing the
absence of retrieved chunks from irrelevant chunks.

### Produce durable JSON and Markdown reports

The command will write timestamped JSON and Markdown reports to a configurable
output directory under `backend/app/knowledge` by default. Both formats will
record effective CLI settings, fixture identity, selected case count, elapsed
time, failures, stage-level macro/micro metrics, and per-case expected,
retrieved, matched, and missing IDs. JSON enables automation; Markdown enables
review in the repository workspace.

Printing only terminal totals was rejected because failures and individual
misses need to be inspected after a batch run completes.

### Treat fixture and service failures separately from scored cases

The script will validate case IDs, document versions, expected-ID presence, and
configuration before retrieval. It will continue independent cases after a
retrieval or reranking error, list failures in the final report, and compute
aggregate metrics only from cases that completed the affected stage. A malformed
fixture will terminate before issuing retrievals.

This prevents a single transient Qdrant or model failure from discarding useful
benchmark evidence while preventing invalid labels from being silently treated
as poor retrieval quality.

## Risks / Trade-offs

- [Qdrant point IDs change after a destructive re-ingestion] -> Validate every
  expected ID and document version at startup; regenerate labels deliberately
  when corpus chunking changes.
- [BGE model initialization makes the full suite slow] -> Initialize embedding
  and reranker models once per process; make limits and case selection
  configurable for focused runs.
- [One question has several semantically valid chunks] -> Permit multiple
  expected chunk IDs per case and curate labels from actual corpus content.
- [Metric totals conceal narrow-topic failures] -> Preserve per-case results,
  stage metrics, and missing expected IDs in both report formats.
- [Local Qdrant is unavailable] -> Fail the real run with a service error while
  keeping unit tests independent of local services.

## Migration Plan

1. Add the benchmark module, fixture, report writer, and offline unit tests.
2. Inspect OCP 4.22 Qdrant payloads and curate then validate all 250 fixture
   labels against the current corpus.
3. Run focused offline tests, then run the complete fixture against local
   Qdrant and save the initial reports.
4. Roll back by removing the standalone benchmark module, fixture, tests, and
   generated reports; no Qdrant data is written by this change.

## Open Questions

- None.
