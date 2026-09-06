## 1. Knowledge contracts and configuration

- [x] 1.1 Add typed knowledge request, chunk provenance, stage diagnostics, and answer-result models under `backend/app/models/`, and add the optional knowledge result to `AgentState`.
- [x] 1.2 Add typed database/vector-store and knowledge-pipeline settings under `backend/app/config/`, with environment overrides and defaults aligned to the local OCP 4.22 Qdrant corpus.
- [x] 1.3 Add unit tests covering model serialization/defaults and configuration overrides without requiring a live service.

## 2. Hybrid retrieval services

- [x] 2.1 Implement service-layer dense and sparse Qdrant recall using BGE-M3 query vectors, named-vector searches, and document-version filtering.
- [x] 2.2 Implement a service-layer RRF fusion component that deduplicates stable point IDs and records fused rank/provenance.
- [x] 2.3 Implement a service-layer BGE reranker component that enforces configured input/context limits and records rerank scores/ranks.
- [x] 2.4 Implement a knowledge-answer orchestration service that composes recall, RRF, reranking, context formatting, and grounded LLM generation, including no-evidence and dependency-failure results.
- [x] 2.5 Add isolated unit tests with fake Qdrant/embedding/reranker/LLM dependencies for dual-mode recall, one-empty-mode fusion, duplicate deduplication, limits, grounded context, and failure paths.

## 3. Knowledge Agent and Router integration

- [x] 3.1 Add the `backend/app/agents/knowledge/` agent/graph entrypoint that invokes the knowledge-answer service and maps its typed result to agent state.
- [x] 3.2 Extend `RouterResult`, router policy/examples, and capability configuration to support `knowledge` / `answer` / `documentation` intent recognition and validation.
- [x] 3.3 Add the Knowledge Agent dependency, node, conditional route, and terminal edge to the Router graph without altering query or plan route behavior.
- [x] 3.4 Add Router and graph tests proving a supported documentation question dispatches to the Knowledge Agent and unsupported knowledge resource/action is stopped before invocation.

## 4. Verification and handoff

- [x] 4.1 Run the affected backend unit tests, static checks, and `openspec validate add-knowledge-agent --strict`.
- [x] 4.2 If local Qdrant and Ollama are available, perform one end-to-end documentation-question smoke test; otherwise document the live integration as unverified and retain automated evidence.
