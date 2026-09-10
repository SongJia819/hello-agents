## Why

Developers need a lightweight way to check how the local LLM answers from one specific OCP Markdown document without involving Qdrant retrieval, RRF, or reranking. The existing hybrid RAG test cannot isolate document-context behavior this way.

## What Changes

- Add a command-line test script under `backend/app/knowledge/` that accepts a Markdown file path and a user question.
- Read the complete named Markdown document, provide it as the only answer context, and call the local LLM.
- Configure this script's LLM client with `max_tokens=4096` and `think=false`, independently of deployment defaults.
- Write only the LLM answer to standard output, preserving its text formatting such as line breaks and Markdown; errors go to standard error with a non-zero exit status.

## Capabilities

### New Capabilities

- `markdown-context-llm-test`: Run a local LLM answer check against the complete contents of one specified Markdown document.

### Modified Capabilities

<!-- None. -->

## Impact

- New script and focused unit tests in `backend/app/knowledge/` and `backend/tests/`.
- Reuses the existing local Ollama-compatible LangChain client dependency; does not access Qdrant, embedding, reranking, MCP, or real cluster infrastructure.
