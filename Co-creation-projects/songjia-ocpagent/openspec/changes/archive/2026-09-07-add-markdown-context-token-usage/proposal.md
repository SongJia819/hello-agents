## Why

The Markdown-context LLM diagnostic currently returns the answer but gives no visibility into the context and generation size. Operators need the provider-reported input, output, and total token counts to evaluate the cost and context impact of supplying a complete document.

## What Changes

- Extract token usage from the local LLM response and report `input_tokens`, `output_tokens`, and `total_tokens` after a successful answer.
- Preserve answer-only standard output by writing token diagnostics to standard error.
- Support both LangChain `usage_metadata` and Ollama/OpenAI-style response metadata field names.
- Report unavailable counts explicitly when the local provider omits usage data; do not estimate tokens.

## Capabilities

### New Capabilities

- `markdown-context-token-usage`: Report local-provider input, output, and total token usage for Markdown-context LLM diagnostics.

### Modified Capabilities

<!-- None. -->

## Impact

- Update the Markdown-context test script and its focused tests.
- No change to the local model invocation, document contents, answer text, or external services.
