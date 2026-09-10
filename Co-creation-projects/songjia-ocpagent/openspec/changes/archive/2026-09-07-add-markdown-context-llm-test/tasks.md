## 1. Markdown Context Test Script

- [x] 1.1 Add a standalone `backend/app/knowledge/` CLI script with positional Markdown-path and question arguments.
- [x] 1.2 Validate the supplied Markdown file and read its complete UTF-8 contents without chunking or truncation.
- [x] 1.3 Build the local LLM request from the question and full document context, using `max_tokens=4096` and `think=false`.
- [x] 1.4 Emit only the unmodified LLM answer to standard output and handle input/LLM failures through standard error and non-zero exit status.

## 2. Verification

- [x] 2.1 Add focused tests for argument/file validation, complete-context prompt construction, fixed LLM options, and exact formatted-answer output.
- [x] 2.2 Run the focused test suite and `openspec validate add-markdown-context-llm-test --strict`.
