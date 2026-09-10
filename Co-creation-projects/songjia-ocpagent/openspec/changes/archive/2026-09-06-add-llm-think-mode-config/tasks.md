## 1. Think-mode configuration

- [x] 1.1 Add validated `OCP_AGENT_LLM_THINK` configuration with default `true` and a shared Ollama-compatible client-options helper.
- [x] 1.2 Apply the shared think option to global Router/Query/Plan clients and Knowledge client construction.
- [x] 1.3 Set `OCP_AGENT_LLM_THINK=false` in the current `backend/.env` environment configuration.
- [x] 1.4 Add an executable project-relative console launcher that exports `backend/.env`, shows an allowlisted/redacted effective configuration summary, and starts the existing console entrypoint.

## 2. Verification

- [x] 2.1 Add tests for default, disabled, and invalid boolean values plus global/Knowledge client options.
- [x] 2.2 Run focused tests, static compilation, and `openspec validate add-llm-think-mode-config --strict`.
- [x] 2.3 Add launcher tests for `.env` loading, think-mode forwarding, path independence, and sensitive-value redaction; rerun focused validation.

## 3. Console streaming rendering

- [x] 3.1 Render `answer_chunk` events without a per-fragment line terminator, flush immediately, and separate completed answers with one line break.
- [x] 3.2 Add a fragmented-answer console test and run focused tests plus strict OpenSpec validation.
