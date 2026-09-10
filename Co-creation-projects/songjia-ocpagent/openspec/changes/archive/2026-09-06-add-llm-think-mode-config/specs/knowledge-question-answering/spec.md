## MODIFIED Requirements

### Requirement: Provide a typed, configurable knowledge-answering contract
The system SHALL define typed models for a knowledge question, retrieved document chunk, retrieval-stage diagnostics, and knowledge answer result under `backend/app/models/`. It SHALL define vector-store and pipeline settings under `backend/app/config/`, including Qdrant endpoint, collection, document version, embedding model, reranker model, generation model/endpoint, LLM think mode, and stage limits. The configuration SHALL default to the existing local OCP 4.22 corpus settings and support deployment-time overrides without code changes.

#### Scenario: Default knowledge request uses the managed corpus
- **WHEN** the Knowledge Agent receives a question with no configuration override
- **THEN** it uses the configured local Qdrant collection and document version `4.22`

#### Scenario: Retained evidence is exposed through models
- **WHEN** the retrieval pipeline retains a chunk for answer generation
- **THEN** the knowledge result includes its stable point ID, content, source path, heading path, document version, ranks, and available retrieval/RRF/rerank scores
