## Context

The Router currently dispatches `knowledge/answer/documentation` only to a Knowledge Agent graph with one retrieval-backed answer node. Requests that are neither an OCP documentation question nor a registered Query or Plan capability end at the Router's unsupported response. The configured local LLM and streaming helper already provide retry and progress behavior, but the Knowledge Agent has no direct conversation path.

## Goals / Non-Goals

**Goals:**

- Route OCP documentation questions through the existing grounded retrieval pipeline unchanged.
- Let the Router send ordinary conversation to a new `knowledge/chat/conversation` capability only after it excludes registered Query, Plan, and other Agent work.
- Generate plain-chat answers directly from the configured LLM with streaming/retry behavior and a clear failure fallback.
- Keep documentation evidence and diagnostics isolated from direct-chat responses.

**Non-Goals:**

- Adding general-purpose tools, external APIs, web search, or real-cluster access.
- Using plain chat to answer OCP-documentation questions when retrieval has no evidence or fails.
- Reclassifying requests that a supported Query, Plan, Execution, or future registered Agent owns.
- Changing the existing documentation retrieval, citation, or mock-MCP contracts.

## Decisions

### Add an explicit routed chat capability

The Router will classify eligible ordinary interaction as `agent=knowledge`, `action=chat`, and `resources=["conversation"]`. Capabilities will register that exact tuple and RouterGraph will retain the existing Knowledge Agent dispatch point. This makes direct chat explicit and testable rather than treating every unsupported route as chat.

Alternative considered: route all unsupported requests to the LLM. Rejected because unsupported infrastructure actions and unregistered Agent responsibilities would silently receive an answer instead of a capability response.

### Branch within the Knowledge Agent by action

The Knowledge graph will branch after entry: `answer` invokes the current retrieval-backed `KnowledgeAnswerService`, while `chat` invokes a direct-chat service/node. Both write the user-facing `answer`; only documentation answers write the existing `knowledge_result` evidence object.

Alternative considered: add a top-level generic-chat Agent. Rejected because this request scopes the capability to Knowledge Agent and the existing graph/container wiring already owns its LLM-backed answer flows.

### Keep direct chat prompt and failure semantics separate

The direct-chat path will submit the user's message and a concise conversational system instruction to the configured LLM without retrieved chunks. It will use the shared streaming/retry helper and return a clearly identified unavailable-response fallback if all attempts fail. It will not cite document chunks or claim grounded OCP evidence.

Alternative considered: reuse the documentation prompt with empty context. Rejected because it would instruct the model to refuse ordinary interaction and blur the evidence boundary.

## Risks / Trade-offs

- [Router misclassification can route an OCP question to direct chat] → Router prompt examples and structured-route tests will prioritize `knowledge/answer/documentation` for OCP documentation questions.
- [A new Agent becomes registered later] → Capability-first routing tests will require registered Agent work to stay out of the conversation fallback.
- [LLM availability failure] → reuse bounded retries and provide a transparent fallback; no synthetic answer is returned.
- [Conversation history is not yet modeled] → initial scope uses the current user message only; multi-turn memory is intentionally outside this change.

## Migration Plan

1. Add the conversation capability, route schema/prompt examples, and Knowledge graph branch.
2. Add direct-chat service/node tests alongside regression tests for documentation routes and unsupported Agent operations.
3. Deploy with the existing configured local LLM endpoint; rollback removes the conversation capability and branch, restoring unsupported responses for ordinary chat.
