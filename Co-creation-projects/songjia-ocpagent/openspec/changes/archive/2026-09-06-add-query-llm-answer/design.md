## Context

The Query graph resolves a mock cluster and lists one or more resources through MCP-backed services, leaving the resource-keyed data in `tool_result`. The Router streams execution events, and the console currently renders those events followed by an object containing route metadata and raw result data. The configured local `llm` is already used for Router structured intent classification and Plan generation.

## Goals / Non-Goals

**Goals:**

- Add one Query graph answer-generation node after MCP listing.
- Give the LLM the unmodified original question and a JSON-safe representation of all selected resource results.
- Set `AgentState.answer` to a readable, grounded response while retaining `tool_result` internally.
- Make the console display only the terminal answer text, with no JSON serialization or formatting normalization.

**Non-Goals:**

- Token-level LLM streaming, citations, knowledge-RAG behavior, or a new chat API protocol.
- Changing mock MCP tools, list resource selection, Router policy, or the stored `tool_result` contract.
- Exposing internal stream events or routing/tool payloads in the user-facing terminal.

## Decisions

### Add a dedicated Query answer node after listing

The Query graph will run `resolve_cluster -> list -> summarize_answer`. The answer node receives `user_query` and the completed resource-keyed `tool_result`, invokes the configured LLM with a natural-language summarization prompt, and returns only `answer` into state.

This keeps MCP retrieval deterministic and separately observable while locating presentation logic at the end of the Query workflow. Summarizing in Router would couple different subagent result types; making the console call the LLM would duplicate business logic and make non-console clients receive raw data.

### Ground the LLM strictly in query data

The prompt will say that the supplied query result is the only factual source, identify the user question, and request a concise answer in the user's language. It will preserve the model's message content as returned, without JSON reserialization or whitespace cleanup. The node is testable through an injected chat model.

### Use an honest fallback for LLM failure

If answer generation fails, the node will set a concise user-visible failure answer and log the error through existing observability. It will retain `tool_result` for diagnostics but will not claim that the LLM summarized it. The console shows this fallback text only.

### Keep streaming internal to the console session

The Router streaming interface remains intact for observability, but the console consumes it silently. It reads only the terminal final-result payload and prints `answer` directly with `print(answer)` semantics, allowing meaningful newlines and spacing to reach the terminal exactly as emitted by the LLM. It does not render route metadata, state JSON, tool results, or lifecycle events.

## Risks / Trade-offs

- [Local LLM is unavailable] → display a clear fallback answer and retain node failure logs; test the failure path with a fake model.
- [MCP result is large] → serialize the selected result once for the prompt; response-size budgeting is deferred for this demo.
- [Model invents facts] → constrain it to supplied result data and retain raw internal `tool_result` for verification.
- [Console users lose debug events] → retain file logs and `stream()` for diagnostics; console is intentionally chat-focused.

## Migration Plan

1. Add the Query prompt/node/graph edge and injected-model tests.
2. Change console terminal rendering to answer-only and update console tests.
3. Run focused tests and a local mock-MCP/LLM console smoke test when available.
4. Rollback removes the summary node/edge; existing MCP list results remain available in state.

## Open Questions

- None. The initial answer is one complete LLM response rather than token streaming.
