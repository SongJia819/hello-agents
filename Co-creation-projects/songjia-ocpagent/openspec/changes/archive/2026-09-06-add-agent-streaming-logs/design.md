## Context

Router, Query, and Plan Agents expose thin `graph.astream(..., stream_mode="updates")` wrappers, while Knowledge Agent exposes only `invoke`. The console harness calls `router_agent.invoke`, so it displays only one final state. Node diagnostics use direct `print` calls in Router and Query, and no shared request-correlated file logger exists.

The runtime is LangGraph based: Router invokes Query/Plan/Knowledge agent graphs as nodes. Streaming must therefore preserve nested graph events while remaining understandable to a terminal consumer.

## Goals / Non-Goals

**Goals:**

- Give Router, Query, Plan, and Knowledge Agents a consistent `stream()` async-generator interface.
- Emit a stable frontend event envelope for node progress, node output/error, and final result.
- Write redacted structured node lifecycle records to a configurable local log file.
- Make `console_agent_test.py` render progress events immediately and print one final, frontend-facing result payload.

**Non-Goals:**

- Token-by-token LLM generation or SSE/WebSocket API delivery.
- Changing routing decisions, MCP mock data, knowledge RAG behavior, or AgentState business fields.
- Centralized observability services, log rotation, distributed tracing, or production credential storage.

## Decisions

### Normalize LangGraph updates at the Agent boundary

Each Agent will implement `stream(state)` using its compiled graph's async stream. A shared event adapter will convert raw LangGraph updates into a JSON-safe envelope containing `event` (`node_started`, `node_completed`, `node_failed`, or `final_result`), `agent`, `node`, `request_id`, and a redacted payload. Router nested agent updates must retain the originating subagent/node name rather than being collapsed into one opaque Router update.

LangGraph `updates` is selected because it exposes completed node state changes without forcing token-stream support from structured-output models. Passing raw LangGraph events to the console was rejected because their shape is framework-specific and can expose non-serializable or sensitive state.

### Correlate request-scoped logs and sanitize before output

Create a shared observability helper under `app/` that generates or propagates a request ID, logs JSON Lines to a configurable path (default `backend/logs/agent-runtime.log`), and redacts sensitive keys recursively before writing logs or stream payloads. Node lifecycle records include timestamp, level, request ID, agent, node, event, and safe metadata; errors include a safe message and type.

The logger replaces existing `print` diagnostics in agent nodes. Per-node log files were rejected because a single request trace would be harder to follow; a shared JSONL file supports chronological request correlation and remains appropriate for this demo.

### Instrument node entry, success, and failure consistently

Router route/capability/unsupported, Query cluster resolution/list, Plan plan creation, and Knowledge answer nodes will emit start/completion/error logs through a reusable wrapper or explicit lifecycle calls. Node instrumentation SHALL re-raise the original exception after logging so LangGraph retains existing failure semantics.

Logging only graph-level events was rejected because it would omit node inputs/outputs and make failed-node diagnosis ambiguous. Business payloads are summarized/redacted rather than duplicated in full to avoid logging credentials and oversized retrieval context.

### Console consumes Router streaming plus final result

The console loop calls `router_agent.stream` instead of `invoke`. It prints each normalized progress event as it arrives and obtains the final state from the terminal `final_result` event, then renders a compact frontend result containing route metadata, support status, answer, and tool result. It will not call a subagent itself.

The console should not re-run `invoke` after streaming, because that would duplicate MCP/LLM side effects. A final event is the single source of the displayed result.

## Risks / Trade-offs

- [Nested graph updates have version-dependent shapes] → isolate parsing in one adapter and test Router-to-subagent event normalization with fake graphs.
- [Log files grow indefinitely] → document this as a local demo log; support a configurable path but defer rotation.
- [State/output contains credentials or large document chunks] → recursively redact sensitive fields and log bounded summaries instead of raw state.
- [A consumer stops reading a stream] → console owns the async iteration and the MCP process cleanup `finally`; future API streaming is out of scope.
- [Structured LLM calls do not emit token chunks] → expose node lifecycle/result streaming, not misleading token-level events.

## Migration Plan

1. Add observability models/configuration and shared stream/log adapters with tests.
2. Instrument all existing runtime nodes and add missing Knowledge Agent streaming.
3. Migrate console rendering to Router streaming and validate final result rendering.
4. Run isolated tests and one local console `list node` smoke test, explicitly distinguishing it from knowledge-service integration.
5. Rollback by retaining the existing `invoke` paths and removing stream/log integration; no persisted business data migration is required.

## Open Questions

- None. The initial event schema is JSON Lines-friendly and stable for the console; a future HTTP streaming API can reuse it.
