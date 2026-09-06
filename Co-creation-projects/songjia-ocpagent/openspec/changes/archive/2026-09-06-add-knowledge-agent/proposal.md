## Why

The repository has a standalone, locally validated hybrid RAG evaluation script, but its retrieval and answer-generation logic is not available from the LangGraph agent runtime. Users therefore cannot ask documentation questions through the normal chat route.

## What Changes

- Add a Knowledge Agent that answers OpenShift documentation questions through the agent runtime.
- Move runtime hybrid retrieval responsibilities into service-layer components: Qdrant dense/sparse recall, reciprocal-rank fusion (RRF), and reranking.
- Define typed knowledge request, retrieved-chunk, and answer-result contracts in `backend/app/models/`.
- Add database/vector-store configuration to `backend/app/config/` and keep runtime defaults aligned with the existing versioned OCP corpus.
- Extend Router structured intent recognition, capability validation, and graph dispatch so knowledge questions are delegated to the Knowledge Agent.
- Require context-grounded LLM answers with chunk provenance and a clear fallback when supporting documentation is unavailable.

## Capabilities

### New Capabilities
- `knowledge-question-answering`: Answer version-scoped OCP documentation questions through hybrid retrieval, RRF, reranking, and a grounded LLM response.

### Modified Capabilities
- `agent-routing`: Recognize, validate, and dispatch supported knowledge intents to the Knowledge Agent.

## Impact

- Affected runtime areas: `backend/app/agents/`, `backend/app/services/`, `backend/app/models/`, `backend/app/config/`, and router tests.
- The implementation reuses the existing local Qdrant corpus and BGE-M3/reranker approach; it does not introduce real-cluster access or change MCP mock-data behavior.
