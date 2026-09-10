## 1. Streaming event transport

- [x] 1.1 Extend the observability stream contract with request-scoped queue-backed semantic `progress` and `answer_chunk` publishers that yield immediately during graph-node execution and preserve redaction.
- [x] 1.2 Update Router subagent dispatch and all runtime Agent stream paths so nested Query, Plan, and Knowledge events reach the outer Router stream in order before its one terminal result.
- [x] 1.3 Add stable, user-safe progress messages for Router routing/capability handling, Query resolution/listing/answer generation, Plan generation, and Knowledge answering without exposing state or prompts.

## 2. Knowledge retrieval and LLM resilience

- [x] 2.1 Emit real-time Knowledge service progress around dense/sparse recall, RRF fusion, reranking, and answer generation, including safe success/failure metadata.
- [x] 2.2 Add validated configuration for `OCP_AGENT_LLM_EMPTY_RESPONSE_RETRY_LIMIT` with default `3`, and share it across answer-generating Agent services.
- [x] 2.3 Implement a shared async LLM stream collector that emits answer chunks, preserves assembled whitespace, normalizes text content safely, retries whitespace-only results up to the configured total attempt limit, and reports an explicit exhausted-retry fallback.
- [x] 2.4 Migrate Knowledge and Query answer generation to the stream collector; preserve their diagnostic/tool-result contracts and safe exception fallbacks.
- [x] 2.5 Migrate Plan user-facing LLM generation where applicable, while retaining complete structured Router classification before dispatch.

## 3. Console rendering and verification

- [x] 3.1 Render semantic progress and answer chunks in `console_agent_test.py` as readable real-time chat feedback without JSON envelopes, raw results, duplicated final answers, or leaked secrets.
- [x] 3.2 Add focused observability tests for immediate nested progress ordering and one terminal event, plus Knowledge phase progress tests.
- [x] 3.3 Add fake streamable-LLM tests for incremental answer assembly, whitespace-only retries, configured attempt limits, exhausted fallback, and stream exceptions.
- [x] 3.4 Update console tests for progress/chunk rendering, formatting preservation, final-answer de-duplication, and existing cleanup/failure behavior.
- [x] 3.5 Run focused backend tests, static compilation, and `openspec validate add-agent-progress-streaming-retries --strict`.
- [ ] 3.6 If local MCP, Qdrant, and Ollama are available, run console query and knowledge-request smoke tests and verify visible recall/RRF/rerank progress plus streamed non-empty answers.
