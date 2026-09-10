## Context

`backend/app/knowledge/hybrid_rag_test.py` exercises the full retrieval pipeline, so its LLM context is a bounded set of reranked chunks rather than a single source document. A document-level diagnostic needs to test the local LLM directly against the complete contents of a supplied Markdown file.

## Goals / Non-Goals

**Goals:**

- Provide one deterministic CLI invocation taking a Markdown path and a question.
- Send the whole UTF-8 document as the sole supplied document context and instruct the LLM to answer from it.
- Produce answer-only standard output without reformatting LLM content.
- Fix the script's LLM behavior to `max_tokens=4096` and `think=false`.

**Non-Goals:**

- Retrieval, chunking, citations, Qdrant access, reranking, or agent routing.
- Editing source documents, accepting non-Markdown input, or serving an API.
- Truncating or summarizing the document to fit a context window; model/provider limits remain visible as an invocation failure.

## Decisions

### Positional CLI contract

The new script will accept two positional arguments: `markdown_path` and `question`. `markdown_path` is resolved and checked as a readable `.md` file before invoking the model. Positional arguments make a one-off diagnostic concise and avoid confusing it with the interactive RAG tool.

### Full document is the only grounding context

The script reads the full file unchanged using UTF-8 and forms a system/human message pair that states the answer must use only that document. It does not add chunk labels or retrieval metadata. This intentionally exposes context-window failures rather than silently dropping text.

### Dedicated non-thinking local client

The script reuses the local model/base URL settings, but builds a client with `max_tokens=4096` and a local `LLMSettings(think=False)` passed to the shared client-options helper. It must not depend on the deployment's generic `OCP_AGENT_LLM_THINK` value, because this diagnostic's contract requires thought mode disabled.

### Answer-only output

The script writes the response content directly with `sys.stdout.write`, adding no label, JSON wrapper, trailing transformation, or Markdown rendering. Diagnostic errors are written only to standard error and cause a non-zero exit code.

## Risks / Trade-offs

- [A large Markdown file exceeds the model context window] → Do not truncate; surface the model error so the diagnostic remains faithful to the supplied document.
- [The model answers beyond the document] → Explicitly constrain the prompt to the supplied Markdown; this remains an LLM behavior test, not a factual guarantee.
- [A user passes a non-document path] → Validate existence, file type, `.md` suffix, and UTF-8 decoding before client invocation.

## Migration Plan

1. Add the standalone script and its unit tests with an injected fake chat model.
2. Run the script against a local Markdown fixture and verify exact stdout preservation.
3. No migration or runtime integration is required; remove the script to roll back.

## Open Questions

None.
