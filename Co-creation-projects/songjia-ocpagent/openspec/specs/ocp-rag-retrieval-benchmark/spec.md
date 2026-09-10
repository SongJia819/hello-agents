## Purpose

Provide a local, version-aware benchmark for measuring hybrid OCP documentation
retrieval quality against corpus-grounded Qdrant chunk labels.

## Requirements

### Requirement: Execute a version-filtered retrieval benchmark
The system SHALL provide a standalone knowledge benchmark command that loads a
configured set of RAG query cases and evaluates every selected case against the
configured Qdrant collection. It SHALL default to document version `4.22`,
Qdrant URL `http://localhost:6333`, collection `ocp-documents`, dense and sparse
candidate depth 30, RRF rerank input depth 30, and final reranked depth 30. It
SHALL provide command-line overrides for the fixture path, document version,
collection, Qdrant URL, model names, output directory, candidate limits, and an
optional case selection.

#### Scenario: Run all default OCP 4.22 cases
- **WHEN** the benchmark is run without case-selection overrides and Qdrant is
  available
- **THEN** it evaluates every fixture case tagged with document version `4.22`
  using only points with that document version

#### Scenario: Run selected cases
- **WHEN** the user supplies a document-version override and explicit case
  selection
- **THEN** the benchmark evaluates only matching selected cases and reports the
  effective configuration

### Requirement: Maintain a corpus-grounded OCP 4.22 benchmark fixture
The system SHALL include a JSON benchmark fixture with exactly 250 initial OCP
4.22 cases. Each case SHALL contain a unique case id, a non-empty question,
document version, and one or more expected stable Qdrant chunk point IDs. The
initial cases SHALL cover multiple OCP documentation areas and every expected
ID SHALL be verified to exist in the OCP 4.22 corpus with matching document
version before a benchmark run begins.

#### Scenario: Load the initial benchmark fixture
- **WHEN** the default fixture is loaded for document version `4.22`
- **THEN** it contains exactly 250 uniquely identified, version-matching cases
  with non-empty expected chunk ID lists

#### Scenario: Fixture contains an invalid expected chunk
- **WHEN** an expected point ID is absent from Qdrant or has a different
  document version
- **THEN** the benchmark reports fixture validation failure and does not score
  that invalid label as a retrieval miss

### Requirement: Score hybrid retrieval stages using expected chunks
For every valid case, the system SHALL run BGE-M3 dense retrieval and sparse
retrieval independently, fuse the ranked results through RRF, and rerank the
configured RRF prefix with the configured BGE reranker. It SHALL calculate
precision and recall at top-10, top-20, and top-30 for dense, sparse, RRF, and
reranked results using deduplicated stable point IDs. At each cutoff, precision
SHALL equal matching retrieved IDs divided by returned unique IDs, and recall
SHALL equal matching retrieved IDs divided by expected IDs.

#### Scenario: A retrieved list contains expected IDs
- **WHEN** a scored stage returns one or more IDs present in the case's expected
  ID set
- **THEN** the case result records retrieved, matched, and missing IDs and
  calculates precision and recall for top-10, top-20, and top-30

#### Scenario: A retrieval stage returns no chunks
- **WHEN** dense, sparse, RRF, or reranking produces an empty result for a valid
  case
- **THEN** that stage records precision and recall of `0.0` at every required
  cutoff without preventing independent stages or later cases from evaluation

### Requirement: Generate auditable benchmark reports
The system SHALL write one JSON report and one Markdown report for each
benchmark execution. Both reports SHALL identify the fixture, effective
configuration, document version, selected and completed case counts, failures,
per-case stage results, and macro and micro precision/recall at top-10, top-20,
and top-30 for every scored stage. The reports SHALL be written to a configurable
output directory and the command SHALL print their paths.

#### Scenario: All selected cases complete
- **WHEN** every selected case is evaluated successfully
- **THEN** both reports include aggregate metrics across all selected cases and
  case-level retrieval diagnostics

#### Scenario: Some cases fail at runtime
- **WHEN** a Qdrant query or reranker operation fails for one case
- **THEN** the benchmark continues independent cases, records the failed case
  and error in both reports, and excludes that failed stage from aggregates
