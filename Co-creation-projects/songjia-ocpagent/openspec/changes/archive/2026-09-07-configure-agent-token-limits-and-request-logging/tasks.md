## 1. Configuration

- [x] 1.1 Extend typed LLM settings with validated Router, Query, Plan, Knowledge chat, and RAG answer output-token fields and environment parsing.
- [x] 1.2 Add the documented per-purpose default token values to the local `.env` configuration while preserving existing model and think settings.
- [x] 1.3 Add focused configuration tests for defaults, per-field overrides, and invalid values.

## 2. Agent LLM Consumers

- [x] 2.1 Replace Router's temporary token constant with a Router-specific configured client.
- [x] 2.2 Configure Query answer generation and Plan generation with their respective output-token budgets.
- [x] 2.3 Configure direct Knowledge chat and RAG Knowledge answer generation with their respective budgets, with the RAG default larger for chunk-grounded responses.
- [x] 2.4 Update focused agent and service tests to assert each consumer receives the intended configured limit.

## 3. Request State and Observability

- [x] 3.1 Add `user_message` to `AgentState` and normalize direct and Router workflow inputs so it retains the original message alongside `user_query`.
- [x] 3.2 Enrich centralized lifecycle log records with the redacted original user message without adding it to user-visible stream events.
- [x] 3.3 Add tests for request-state preservation, successful and failed lifecycle logs, and sensitive-value redaction.

## 4. Verification

- [x] 4.1 Run the focused configuration, Router, Query, Plan, Knowledge, and observability test suites.
- [x] 4.2 Run `openspec validate configure-agent-token-limits-and-request-logging --strict`.
