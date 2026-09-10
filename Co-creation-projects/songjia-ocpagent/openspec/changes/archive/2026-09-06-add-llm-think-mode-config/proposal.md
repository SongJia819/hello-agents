## Why

LLM thinking output changes latency and streaming behavior, but the current runtime has no deployment-time control for it. The default should retain thinking support while the current local environment needs it disabled for faster, direct responses.

## What Changes

- Add one environment-configurable boolean that controls whether configured Ollama-compatible LLM clients request think mode.
- Default think mode to enabled when no override is present.
- Set the current local `backend/.env` override to disabled.
- Apply the setting consistently to Router, Query, Plan, and Knowledge LLM client construction without changing prompts or answer contracts.
- Add a console startup script that loads `backend/.env`, displays the effective safe configuration, and then launches the existing console Agent entrypoint.
- Render streamed console answer fragments continuously, preserving only line breaks supplied by the LLM.

## Capabilities

### New Capabilities

- `llm-think-mode-configuration`: Deployment-time think-mode control for all runtime LLM clients.

### Modified Capabilities

- `knowledge-question-answering`: Honor the common LLM think-mode setting for Knowledge answer generation.

## Impact

- Affected areas: LLM config, Knowledge client construction, local environment sample/configuration, console startup/rendering, and LLM construction tests.
