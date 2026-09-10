## Why

The agent runtime can return a final state and some graphs already expose raw LangGraph events, but neither node progress nor consistent streaming output is available across every Agent. Developers using the console harness cannot see work in progress or inspect a durable execution trace after a request completes or fails.

## What Changes

- Add a unified stream contract to Router, Query, Plan, and Knowledge Agents, with normalized node lifecycle and result events.
- Add structured node logging for every runtime graph node and write request-correlated records to a configurable local log file.
- Replace ad-hoc `print` diagnostics in agent nodes with the shared logger.
- Update `console_agent_test.py` to consume Router Agent streaming events, display them as they arrive, and then display the final frontend-facing result summary.
- Add isolated tests for stream ordering, node log records, error logging, sensitive-field redaction, and console streaming display.

## Capabilities

### New Capabilities
- `agent-streaming-observability`: Provide consistent streaming execution events and durable structured node logs across the agent runtime.

### Modified Capabilities
- `console-agent-test`: Display Router Agent execution events progressively and present the final agent result to the console user.

## Impact

- Affected areas: `backend/app/agents/`, shared logging/configuration, `backend/app/console_agent_test.py`, and backend tests.
- Existing mock MCP data and routing/subagent selection remain unchanged; the change only exposes execution progress and diagnostics.
