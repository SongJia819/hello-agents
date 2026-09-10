## Why

All non-RAG runtime LLM calls currently inherit a broad shared generation limit, while the recent Router and general-chat limits are temporary code constants. This allows lightweight structured routing to consume excessive tokens and makes per-Agent tuning impossible without source edits; the runtime logs also do not explicitly record the original user message.

## What Changes

- Define editable, per-purpose LLM `max_tokens` settings with defaults in `.env`, rather than using one shared limit or hard-coded temporary limits.
- Apply distinct limits to Router, Query answer generation, Plan generation, general Knowledge chat, and RAG-grounded Knowledge answers; retain a larger default budget for RAG answers so they can synthesize cited chunks.
- Preserve the incoming user message in `AgentState` for every workflow entrypoint.
- Add the user message to request-correlated structured lifecycle logs after the existing sensitive-value redaction.
- Replace the current temporary Router and general-chat token constants with the configured settings.

## Capabilities

### New Capabilities

- `agent-llm-token-configuration`: Configure and apply purpose-specific LLM output-token budgets for runtime Agents.

### Modified Capabilities

- `agent-streaming-observability`: Persist and safely log the original user message with runtime node lifecycle records.

## Impact

- Affected configuration: `backend/app/config/llm.py`, `backend/app/config/knowledge.py`, and the local `.env` template/defaults.
- Affected runtime consumers: Router, Query, Plan, direct Knowledge chat, and RAG Knowledge answer services.
- Affected contracts and tests: `AgentState`, graph entrypoints, observability records, configuration parsing, and agent/service tests.
