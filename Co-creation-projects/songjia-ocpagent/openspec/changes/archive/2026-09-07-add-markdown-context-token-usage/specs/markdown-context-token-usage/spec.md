## ADDED Requirements

### Requirement: Report provider token usage for a Markdown-context answer
After a successful Markdown-context local LLM invocation, the script SHALL report the provider-reported input, output, and total token counts. It SHALL read normalized LangChain `usage_metadata` when available and otherwise support OpenAI-compatible response metadata token usage. It SHALL not estimate or fabricate missing counts.

#### Scenario: Normalized LangChain usage is returned
- **WHEN** the LLM response has `usage_metadata` with input, output, and total token counts
- **THEN** the script reports those three values as `input_tokens`, `output_tokens`, and `total_tokens`

#### Scenario: OpenAI-compatible provider usage is returned
- **WHEN** normalized usage is absent and response metadata contains prompt, completion, and total token counts
- **THEN** the script reports prompt as input, completion as output, and total as total tokens

#### Scenario: Usage is omitted by the provider
- **WHEN** the successful LLM response contains no supported token usage metadata
- **THEN** the script reports all three token fields as `unavailable` and does not estimate values

### Requirement: Preserve answer-only standard output while printing token diagnostics
The script SHALL preserve the unmodified LLM answer as the only standard output. It SHALL write exactly one token-usage diagnostic line to standard error after a successful answer, using `Token usage: input_tokens=<value> output_tokens=<value> total_tokens=<value>`.

#### Scenario: A formatted answer and usage are returned
- **WHEN** the LLM returns a multiline Markdown answer and token usage
- **THEN** standard output contains exactly the answer and standard error contains the token-usage line
