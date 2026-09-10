## Context

The runtime stream currently exposes node-started and node-completed envelopes only after a LangGraph update is available. Knowledge retrieval performs recall, RRF, rerank, and one non-streaming LLM request inside a single `answer` node, so its long-running stages are invisible to callers. A successful transport response with empty `content` is also accepted as an answer and the answer-only console prints a blank line.

## Goals / Non-Goals

**Goals:**

- Deliver user-safe semantic progress from long-running agent work as it happens, including knowledge recall, RRF, rerank, LLM generation, and retry transitions.
- Stream LLM output chunks through the normalized Agent stream while still assembling the final `answer` state.
- Retry an empty or whitespace-only assembled LLM answer using a configurable limit whose default is three attempts.
- Preserve request correlation, secret redaction, the mock-only MCP boundary, and existing `invoke` final-state behavior.

**Non-Goals:**

- Changing retrieval algorithms, RRF/rerank limits, model selection, the MCP protocol, or adding a frontend transport.
- Retrying non-empty but low-quality answers, providing token-level cancellation, or streaming Router structured-output JSON before it validates.

## Decisions

### Use semantic progress envelopes, not raw node payloads

The normalized stream will add `progress` events with a stable `phase`, `status` (`started`, `completed`, `retrying`, or `failed`), and a concise user-facing message. Events retain request ID, agent, and node and omit prompts, chunks, model metadata, and tool results. The Knowledge service emits `recall`, `rrf`, and `rerank` around its service calls; LLM callers emit `llm_generation` and retry transitions. Router, Query, Plan, and Knowledge graph nodes retain their lifecycle events.

This adds useful feedback without rendering internal state. Generic node events alone cannot distinguish, for example, starting retrieval from RRF fusion.

### Make the stream transport concurrent with graph execution

`stream_graph` will run graph updates in a producer task and expose a request-scoped async event queue to nodes/services. It will yield queue items immediately while a graph node is still running, then emit exactly one terminal final-result event after the graph completes. Nested Router subagent execution will use the same request-scoped publisher, so child progress reaches the outer Router stream in execution order instead of being buffered until the Router node returns.

An `asyncio.Queue` is selected over the current list sink because a list is drained only after a LangGraph update, which is too late for real-time feedback. The queue has bounded, local lifecycle cleanup to prevent a completed request from leaking events into a subsequent request.

### Collect LLM output with `astream` and validate the assembled answer

Answer-generating calls use the model's async streaming interface. Each non-empty text chunk is appended to an attempt-local buffer and emits an `answer_chunk` stream event. The final answer is the joined buffer, preserving model whitespace. Structured Router intent classification remains an awaited structured invocation because it is not user answer text and requires a complete valid schema before dispatch.

Consumers that only want a final answer can ignore `answer_chunk`; the console will render chunks as they arrive and avoid printing the same completed answer a second time.

### Centralize empty-answer retry configuration

Add an LLM response setting in the config layer, sourced from `OCP_AGENT_LLM_EMPTY_RESPONSE_RETRY_LIMIT`, with validation for a positive integer and default `3`. Query, Knowledge, and Plan answer-generation paths consume this setting through a shared streaming-answer helper. An attempt is empty when the assembled content is whitespace-only. Each empty attempt emits `progress` with `status=retrying`; after the configured number of attempts, the caller returns a clear non-empty fallback and logs the exhausted condition. Existing exception fallbacks remain safe and explicit.

A shared helper avoids divergent retry behavior and lets fake streamable models test chunking, whitespace-only outputs, and attempt counts consistently.

## Risks / Trade-offs

- [High-frequency token chunks overwhelm a slow terminal] → use concise chunk events, preserve ordering, and allow non-console consumers to ignore them.
- [A producer task fails after emitting partial events] → emit a safe node-failed event, stop the queue cleanly, and keep the existing final/failure semantics.
- [Retry repeats tokens in the console] → console identifies retry boundaries and renders only the successful attempt's text as final output; partial failed-attempt text is not treated as a final answer.
- [Model returns non-text content blocks] → normalize only textual blocks; no extracted text means an empty attempt and triggers configured retry.

## Migration Plan

1. Add event types, queue-backed stream transport, config, and unit tests with a fake publisher/model.
2. Instrument Knowledge internal phases and migrate Query/Plan answer generation to the shared streamable helper.
3. Update Router nested forwarding and console rendering, then run a local MCP/Ollama smoke test.
4. Roll back by retaining the terminal final-result interface and replacing the helper with awaited invocation; no data migration is needed.

## Open Questions

- None. The default retry limit counts the initial empty result as attempt one, so a value of three permits at most three model calls.
