## 1. Query answer generation

- [x] 1.1 Add a Query Agent answer-generation prompt that supplies the original user question and JSON-safe resource-keyed MCP result, and requires a grounded natural-language answer.
- [x] 1.2 Add a `summarize_answer` Query graph node after general listing; invoke the configured LLM and store its response content in `AgentState.answer` without changing `tool_result`.
- [x] 1.3 Add a safe Query LLM failure result and request-correlated node logging that retains the internal MCP result without claiming a successful summary.

## 2. Chat-style console rendering

- [x] 2.1 Change console stream consumption to ignore internal lifecycle events and extract the terminal final-result state only.
- [x] 2.2 Print only the final `answer` text once, preserving LLM line breaks and spaces without JSON serialization, metadata, routing fields, or raw MCP results.
- [x] 2.3 Preserve blank input, exit, stream-failure, and MCP cleanup behavior.

## 3. Verification

- [x] 3.1 Add isolated Query tests with a fake LLM for question/result prompt content, one-resource and multi-resource answer propagation, and LLM failure handling.
- [x] 3.2 Update console tests for answer-only rendering, whitespace preservation, and no internal event/result rendering.
- [x] 3.3 Run focused backend tests, static checks, and `openspec validate add-query-llm-answer --strict`.
- [x] 3.4 If local MCP and Ollama are available, run a console `list node` smoke test and verify a natural-language answer is displayed without structured payloads.
