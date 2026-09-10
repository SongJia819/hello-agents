## Context

The shared runtime `llm` has a single broad `max_tokens` value. Router and direct Knowledge chat currently override it through temporary code constants after a Router structured-output call exhausted the model's context budget. Query answer generation, Plan generation, and grounded RAG answer generation still do not have independent output budgets. The current `AgentState` only carries `user_query`, and lifecycle logging records node events and results without an explicit original message field.

## Goals / Non-Goals

**Goals:**

- Make each runtime LLM generation budget explicit, validated, and editable through environment configuration.
- Give RAG answer generation a larger default than lightweight routing and ordinary chat so cited chunk synthesis has adequate output space.
- Preserve the original incoming message in state without breaking existing callers that use `user_query`.
- Include the redacted original message in request-correlated file logs for debugging.

**Non-Goals:**

- Changing models, providers, temperature, or the existing `think` setting.
- Introducing real cluster access, persistent conversation history, or request-content retention outside the configured runtime log.
- Defining a hard timeout, token usage telemetry, or a generic LLM retry policy beyond the existing empty-response retry behavior.

## Decisions

### One typed configuration source with purpose-specific budgets

Extend `LLMSettings` with validated positive integer fields and environment variables for Router, Query, Plan, general Knowledge chat, and RAG Knowledge answer generation. Defaults will be placed in `.env`; proposed defaults are Router `1024`, Query `2048`, Plan `2048`, Knowledge chat `2048`, and RAG answer `4096`.

The shared base client remains available for compatibility, but each consumer constructs or selects a client using its dedicated setting. This replaces temporary literals and prevents a lightweight structured call from inheriting a RAG-sized budget. A separate `KnowledgeSettings` token field was considered, but rejected because all model client behavior belongs in the existing shared LLM configuration and one environment prefix is easier to operate.

### Preserve a raw message field while retaining `user_query`

Add an optional `user_message` field to `AgentState`. Router and direct Agent entrypoints normalize the submitted request so both `user_query` and `user_message` contain the original text. Existing callers that provide only `user_query` remain valid, and downstream prompt construction continues to use `user_query`.

Replacing `user_query` was rejected because public API and existing graph callers depend on it; relying only on `messages` was rejected because LangGraph message reducers can contain derived agent messages rather than one stable original input field.

### Log messages centrally in lifecycle records

`node_log` adds a top-level `user_message` value sourced from state, falling back to `user_query`, and passes it through the existing redaction function. Every observed node therefore has the message without each Agent hand-writing logging calls. The message is recorded in the local configurable runtime log only; it is not added to progress events or user-visible responses.

## Risks / Trade-offs

- [A budget too small truncates a valid response] → Defaults separate concise structured tasks from RAG synthesis; values remain editable in `.env` without code changes.
- [A very large RAG answer can still be slow] → RAG has a deliberately bounded larger default rather than the prior broad shared limit.
- [Runtime logs contain user-provided content] → Keep existing local log-path configuration and sensitive-key redaction; do not add messages to streaming events.
- [Some direct callers bypass Router] → Normalize state at each public Agent invocation path and cover it with focused tests.

## Migration Plan

1. Add the configuration fields and `.env` defaults, keeping a compatibility default for callers that instantiate settings without environment values.
2. Replace temporary and shared-client token assignments with purpose-specific clients.
3. Add state normalization and central log enrichment.
4. Run configuration, agent, service, and observability tests; rollback by restoring prior environment values and client selection if needed.

## Open Questions

None. The specified defaults are intentionally conservative and remain deployment-configurable.
