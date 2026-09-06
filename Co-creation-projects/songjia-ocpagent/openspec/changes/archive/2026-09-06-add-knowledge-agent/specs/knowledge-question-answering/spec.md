## ADDED Requirements

### Requirement: Provide a typed, configurable knowledge-answering contract
The system SHALL define typed models for a knowledge question, retrieved document chunk, retrieval-stage diagnostics, and knowledge answer result under `backend/app/models/`. It SHALL define vector-store and pipeline settings under `backend/app/config/`, including Qdrant endpoint, collection, document version, embedding model, reranker model, generation model/endpoint, and stage limits. The configuration SHALL default to the existing local OCP 4.22 corpus settings and support deployment-time overrides without code changes.

#### Scenario: Default knowledge request uses the managed corpus
- **WHEN** the Knowledge Agent receives a question with no configuration override
- **THEN** it uses the configured local Qdrant collection and document version `4.22`

#### Scenario: Retained evidence is exposed through models
- **WHEN** the retrieval pipeline retains a chunk for answer generation
- **THEN** the knowledge result includes its stable point ID, content, source path, heading path, document version, ranks, and available retrieval/RRF/rerank scores

### Requirement: Recall version-filtered dense and sparse candidates
The system SHALL implement database recall in `backend/app/services/`. For each knowledge question, it SHALL create BGE-M3 dense and sparse query vectors, search the corresponding Qdrant named vectors, and filter both searches by the configured document version. It SHALL retain stage-specific candidate provenance in typed models.

#### Scenario: Both recall modes yield candidates
- **WHEN** dense and sparse vector searches return version-matching points
- **THEN** the service returns ordered dense and sparse candidate lists with stable point identifiers and retrieval metadata

#### Scenario: One recall mode is empty
- **WHEN** one vector search returns no version-matching points and the other returns candidates
- **THEN** the service returns both stage results and allows subsequent fusion to use the non-empty list

### Requirement: Fuse recalled candidates with reciprocal rank fusion
The system SHALL implement RRF in `backend/app/services/` using the configured RRF constant. It SHALL fuse dense and sparse rankings, deduplicate a chunk by stable point ID, and record the fused rank for every retained chunk.

#### Scenario: A chunk appears in both recall rankings
- **WHEN** dense and sparse recall contain the same stable point ID
- **THEN** RRF returns that chunk once at its fused rank

#### Scenario: Only one recall ranking has candidates
- **WHEN** exactly one recall ranking is non-empty
- **THEN** RRF returns the available candidates in a valid fused result

### Requirement: Rerank bounded fused evidence in the service layer
The system SHALL implement reranking in `backend/app/services/`. It SHALL send no more than the configured fused-candidate limit and original question to the configured BGE reranker, retain no more than the configured answer-context limit, and preserve rerank score and rank on each result.

#### Scenario: Fused candidates exceed the reranker input limit
- **WHEN** fusion yields more candidates than the configured reranker-input limit
- **THEN** only the highest RRF-ranked configured prefix is passed to the reranker

#### Scenario: Reranking produces answer context
- **WHEN** the reranker returns scored candidates
- **THEN** the result retains the configured top context chunks in descending rerank order

### Requirement: Generate a grounded knowledge answer
The Knowledge Agent SHALL invoke recall, RRF, reranking, and LLM generation in that order. It SHALL send the original user question and only retained reranked chunks to the LLM, label every context chunk with its stable point ID, and instruct the LLM to ground factual claims in that context. It SHALL write the answer and typed knowledge result into agent state.

#### Scenario: Documentation evidence supports a question
- **WHEN** recall and reranking retain one or more chunks and the configured LLM succeeds
- **THEN** the agent returns the LLM answer with the retained evidence available in its knowledge result

#### Scenario: No supporting documentation is found
- **WHEN** both recall modes produce no version-matching chunks or reranking retains no chunks
- **THEN** the agent returns a clear no-evidence response and SHALL NOT call the LLM

#### Scenario: A knowledge dependency fails
- **WHEN** Qdrant, embedding, reranking, or LLM invocation fails
- **THEN** the agent returns a clear non-fabricated fallback with a typed failure reason and no successful answer claim
