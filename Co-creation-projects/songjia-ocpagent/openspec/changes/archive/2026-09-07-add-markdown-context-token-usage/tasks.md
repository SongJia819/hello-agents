## 1. Token Usage Diagnostics

- [x] 1.1 Add a response token-usage extractor supporting LangChain normalized and OpenAI-compatible metadata.
- [x] 1.2 Write one stable input/output/total token diagnostic line to standard error after a successful answer without changing standard output.
- [x] 1.3 Render missing provider usage values as `unavailable` without estimating them.

## 2. Verification

- [x] 2.1 Add focused tests for normalized usage, provider metadata fallback, unavailable usage, and stdout/stderr separation.
- [x] 2.2 Run focused tests and `openspec validate add-markdown-context-token-usage --strict`.
