## Why

Query Agent currently returns raw mock MCP models in `tool_result`, leaving users to interpret internal data structures. The console also exposes runtime progress and result envelopes rather than behaving like a natural chat response.

## What Changes

- After Query Agent completes MCP resource listing, send the original user question and resource-keyed tool result to the configured LLM.
- Store the LLM's grounded, natural-language summary in `AgentState.answer` while preserving `tool_result` for internal/API consumers.
- Handle LLM failures with a clear answer fallback that does not claim a generated summary succeeded.
- Change `console_agent_test.py` to display only the final LLM answer text; preserve its formatting exactly, including line breaks and spaces, and suppress internal stream events, routing metadata, and raw tool data from the user-facing console.
- Add isolated tests for prompt input, answer propagation, failure handling, and chat-style console rendering.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `cluster-node-query`: Generate an LLM natural-language answer from a completed MCP-backed query result.
- `console-agent-test`: Render only the final natural-language answer as a chat response.

## Impact

- Affected areas: Query graph/nodes/prompts, Agent state behavior, console rendering, and tests.
- Query resource discovery still uses existing mock MCP services; no real OpenShift connection is introduced.
