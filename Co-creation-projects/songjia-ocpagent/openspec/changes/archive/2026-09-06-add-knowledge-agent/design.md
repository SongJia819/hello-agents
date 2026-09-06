## Context

`backend/app/knowledge/hybrid_rag_test.py` already proves a local version-scoped OCP pipeline: BGE-M3 dense and sparse Qdrant retrieval, RRF fusion, BGE reranking, then a context-only Ollama answer. It is a standalone diagnostic script, however, and mixes configuration, data contracts, retrieval mechanics, logging, and generation. The Router graph currently supports `query` and `plan` dispatch and validates each route with `CAPABILITIES`; `AgentType.KNOWLEDGE` exists but has no capability or graph node.

The project remains a demo/reference implementation. Knowledge retrieval uses its local OCP documentation collection and must not contact a real OpenShift cluster.

## Goals / Non-Goals

**Goals:**

- Expose grounded, version-scoped OCP documentation answers through a `knowledge` LangGraph agent.
- Keep vector-store settings and pipeline limits in `app.config`, request/result schemas in `app.models`, and recall/RRF/rerank mechanics in `app.services`.
- Preserve the proven hybrid sequence: dense and sparse recall, RRF, bounded reranking, and LLM generation from retained chunks.
- Route a supported documentation question through the existing structured Router and capability gate.

**Non-Goals:**

- Replacing the ingestion command, corpus layout, vector schema, or standalone RAG evaluation/benchmark tools.
- Real cluster APIs, MCP tools, credential management, streaming answers, or long-term memory.
- Changing the behavior of existing query and plan routes.

## Decisions

### Add a composition-oriented Knowledge Agent

Create `app/agents/knowledge/` with an agent/graph entrypoint that reads `user_query`, invokes a knowledge orchestration service, and writes the final answer and typed retrieval outcome into `AgentState`. The Router graph receives this agent as a dependency and adds a `knowledge` terminal node, mirroring existing query/plan integration.

This keeps routing orchestration separate from RAG mechanics. Embedding the pipeline in Router would couple intent classification to data access and make failure testing difficult; exposing the standalone test script itself as an agent would retain command-line concerns in runtime code.

### Centralize runtime settings in `app.config`

Introduce a typed knowledge/vector-store configuration object with Qdrant URL, collection, document version, BGE-M3 embedding model, reranker model, LLM model/base URL, recall limits, RRF constant, reranker-input limit, and answer-context limit. Defaults retain the current OCP 4.22 local-Qdrant behavior, with environment-based overrides suitable for local demo deployment.

The configuration is injected into services and agent construction instead of using module-local constants. This separates deployment configuration from models while retaining a deterministic test seam. Environment configuration is preferred over hard-coded values because the existing corpus/endpoint can differ across developer machines.

### Use typed models at service boundaries

Define Pydantic models for a knowledge request, a retrieved chunk, per-stage retrieval diagnostics, and the final knowledge result. A chunk retains stable point ID, text, document provenance, retrieval/RRF/rerank ranks and scores where available. The final result holds answer text, retained source chunks, and an optional safe failure reason.

Services exchange these models rather than LangChain `Document` objects. LangChain/Qdrant adapters remain internal implementation details, while agent state carries only serializable contracts suitable for tests and API presentation.

### Split the RAG pipeline into service-layer stages

Implement recall, fusion, and reranking in separately testable services under `app/services/`, with a thin knowledge-answer orchestration service calling them in order. Recall performs dense and sparse named-vector searches filtered by document version. Fusion deduplicates by stable point ID using RRF. Reranking accepts only the configured prefix of the fused order and returns only the configured answer context. The orchestration service formats labeled context and calls the configured LLM only if retained evidence exists.

This explicitly meets the requested service-layer placement and lets tests replace clients/embedders/rerankers/LLMs. A single monolithic service was rejected because it would obscure the mandated stages and make RRF behavior less testable.

### Model knowledge routing explicitly

Extend `RouterResult`/prompt policy to classify documentation and explanatory OCP questions as agent `knowledge`, with a canonical action such as `answer` and resource `documentation`. Add the corresponding `AgentType.KNOWLEDGE` capability. The capability check remains the one gate before dispatch, so arbitrary router output cannot invoke the Knowledge Agent.

Existing routes retain their current resource semantics. Reusing query `list` would conflate live/mock resource inventory with documentation questions and would not represent the knowledge pipeline's input/output contract.

### Ground responses and represent recoverable failures

The generation prompt only supplies reranked chunks, labels every block with its stable point ID, and requires citations. If recall, reranking, Qdrant, or LLM calls fail, the agent returns a non-fabricated user-facing fallback and structured diagnostics; it does not silently answer from model knowledge. The plan preserves diagnostic provenance in the typed result but does not require script-style file logging in the runtime path.

## Risks / Trade-offs

- [Local Qdrant, embedding model, reranker, or Ollama is unavailable] → Catch stage failures, return a clear fallback, and cover injected-dependency failure paths in unit tests.
- [RAG model loading is expensive] → Construct/load dependencies lazily and allow tests to inject fakes; optimization/caching beyond that is out of scope.
- [The router misclassifies a cluster-operation question as documentation] → Use explicit prompt examples and structured RouterResult tests for query, plan, and knowledge routes.
- [Current `AgentState` is not fully typed for optional RAG payloads] → Add an optional typed knowledge-result field without changing established query/plan fields.
- [Existing standalone tool and runtime pipeline drift] → Reuse its accepted defaults and document the shared pipeline contract; refactoring the standalone tool itself is not required by this change.

## Migration Plan

1. Add models, config, services, and focused unit tests with fake dependencies.
2. Add Knowledge Agent and Router capability/graph integration; preserve existing route tests.
3. Run unit tests and strict OpenSpec validation; where local Qdrant/Ollama is absent, report live integration as unverified rather than passing it implicitly.
4. Roll back by removing the new capability and graph node; existing query and plan paths remain independent.

## Open Questions

- None for the planning phase. The initial implementation uses document version `4.22` as the configuration default, matching the currently ingested corpus.
