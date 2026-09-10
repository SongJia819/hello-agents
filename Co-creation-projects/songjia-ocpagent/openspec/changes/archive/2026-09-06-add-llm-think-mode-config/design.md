## Context

Runtime LLM clients are constructed in the common LLM configuration and in the Knowledge service. Ollama-compatible models accept a `think` request option, but the application does not currently configure it consistently.

## Goals / Non-Goals

**Goals:**

- Provide one boolean environment setting, defaulting to enabled, for all runtime LLM requests.
- Disable think mode in the current local `backend/.env` configuration.
- Provide one repeatable console launcher that exports `backend/.env` before importing runtime configuration.
- Preserve LLM-provided answer formatting while rendering streamed answer fragments in the console.
- Preserve model, prompt, retry, and structured-output behavior.

**Non-Goals:**

- Parsing, showing, or persisting model reasoning text.
- Changing a remote model provider or its authentication.

## Decisions

Use `OCP_AGENT_LLM_THINK` with strict boolean parsing (`true`/`false`) and default `true`. Build a common client-options helper that passes the setting as the Ollama-compatible request `think` option for both global and Knowledge clients. This is preferable to separate per-agent flags because a deployment should not silently use different reasoning modes for routing and answering.

The checked-in local environment override will set `OCP_AGENT_LLM_THINK=false`; deployments omitting it retain the enabled default. A `backend/scripts/start_console_agent_test.sh` launcher will resolve the project-relative `.env`, export its variables for the child console process, and print an allowlisted effective configuration summary before startup. Secret-bearing keys are redacted rather than echoed.

The console loop will write each `answer_chunk` without a renderer-added line terminator and flush immediately. It will emit one separating newline after a streamed answer completes. This keeps progress messages line-oriented while ensuring the model controls the answer's spaces and line breaks.

## Risks / Trade-offs

- [Provider ignores the option] → retain client-construction tests and document the option as Ollama-compatible.
- [Invalid environment value] → fail configuration validation early rather than silently changing behavior.
- [Launcher prints a credential] → render only an allowlist of operational values and redact recognized secret field names.
- [Tiny model fragments render as separate lines] → write fragments without `print`'s default newline and assert their combined console output is unchanged.

## Migration Plan

1. Add settings parsing and shared client options.
2. Apply to global and Knowledge clients, then add local override, launcher, and tests.
3. Roll back by removing the launcher or environment override; default behavior remains enabled.
