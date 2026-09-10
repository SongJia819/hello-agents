## Context

The Markdown-context diagnostic invokes a local Ollama-compatible LLM and writes only the returned answer to standard output. LangChain responses can expose usage either through normalized `usage_metadata` (`input_tokens`, `output_tokens`, `total_tokens`) or provider response metadata such as `token_usage` (`prompt_tokens`, `completion_tokens`, `total_tokens`).

## Goals / Non-Goals

**Goals:**

- Display provider-reported input, output, and total tokens after a successful invocation.
- Preserve stdout as an answer-only stream so piping answer text remains reliable.
- Tolerate both normalized and provider-specific LangChain usage shapes.

**Non-Goals:**

- Locally estimating tokens when the provider does not report them.
- Changing prompt content, document handling, LLM model settings, or answer formatting.
- Adding token telemetry to Agent runtime workflows.

## Decisions

### Extract normalized usage first, then provider metadata

Use `response.usage_metadata` when it contains the three normalized counts. Otherwise inspect the `response.response_metadata["token_usage"]` mapping and translate `prompt_tokens` to input and `completion_tokens` to output. This accommodates normal LangChain chat results and the local OpenAI-compatible response shape without provider-specific dependencies.

### Emit diagnostics to standard error

After writing the unchanged answer to stdout, write one stable stderr line:

`Token usage: input_tokens=<value> output_tokens=<value> total_tokens=<value>`

This preserves the existing answer-only stdout contract. Missing fields are rendered as `unavailable`; counts are never invented.

## Risks / Trade-offs

- [Ollama/version adapter omits usage] → Print explicit unavailable values rather than misleading estimates.
- [Provider changes usage field names] → Cover the normalized and OpenAI-compatible shapes; preserve answer output even when metrics cannot be found.
- [Mixed stdout/stderr terminal display] → The stable stderr prefix makes diagnostics easy to identify or redirect.

## Migration Plan

1. Add an isolated usage-extraction helper and tests for both metadata shapes and missing values.
2. Print the diagnostics after successful answer output.
3. Roll back by removing the stderr diagnostic only; no data migration is involved.

## Open Questions

None.
