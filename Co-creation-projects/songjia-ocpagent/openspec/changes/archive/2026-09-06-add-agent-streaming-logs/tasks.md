## 1. Shared streaming and logging foundation

- [x] 1.1 Define JSON-safe, request-correlated stream event and log-record contracts, including recursive sensitive-field redaction.
- [x] 1.2 Add configurable local JSONL logging with default path `backend/logs/agent-runtime.log` and request ID propagation.
- [x] 1.3 Add a LangGraph update adapter that emits normalized node lifecycle, node output/error, and final-result events without changing `invoke` return behavior.

## 2. Agent and node instrumentation

- [x] 2.1 Add or standardize `stream()` on Router, Query, Plan, and Knowledge Agents using the shared event adapter.
- [x] 2.2 Instrument Router route/capability/unsupported nodes with request-correlated start, completion, and failure file logs; replace direct prints.
- [x] 2.3 Instrument Query resolve-cluster/list nodes with request-correlated lifecycle file logs; replace direct prints.
- [x] 2.4 Instrument Plan create-plan and Knowledge answer nodes with request-correlated lifecycle file logs and safe error summaries.
- [x] 2.5 Verify nested Router-to-subagent events preserve the subagent and node identifiers in the public stream.

## 3. Console streaming presentation

- [x] 3.1 Change `console_agent_test.py` to consume `router_agent.stream` and render normalized events immediately rather than calling `invoke`.
- [x] 3.2 Render exactly one frontend-facing final result from the terminal event, including route metadata, supported status, answer, and tool result.
- [x] 3.3 Preserve console blank/exit behavior and MCP subprocess cleanup while handling a stream error without a duplicate Agent invocation.

## 4. Verification

- [x] 4.1 Add isolated tests for every Agent stream contract, nested event ordering, final result, node logs, request correlation, and secret redaction.
- [x] 4.2 Add console tests for progressive event display, final-result rendering, and stream failure handling using a fake streaming Router Agent.
- [x] 4.3 Run focused backend tests, static checks, and `openspec validate add-agent-streaming-logs --strict`.
- [x] 4.4 If local MCP and LLM dependencies are available, run a console `list node` smoke test and confirm both progressive events and node log records.
