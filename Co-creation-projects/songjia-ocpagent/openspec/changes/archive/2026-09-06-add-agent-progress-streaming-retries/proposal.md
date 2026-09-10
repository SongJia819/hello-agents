## Why

The runtime currently exposes only generic node lifecycle events, so users cannot see meaningful retrieval milestones while a knowledge request is running. In addition, an LLM may return an empty response without raising an exception, which becomes a blank console answer instead of a recoverable failure.

## What Changes

- Emit request-correlated, user-safe progress events for meaningful agent work, including knowledge recall, RRF fusion, reranking, LLM generation, retries, and completion.
- Forward progress events as they occur through nested Agent streams and render readable progress feedback in the console while preserving the final answer-only result.
- Use streamable LLM invocation for answer generation where supported, forwarding generated answer chunks through the runtime stream without exposing internal prompts or tool data.
- Add configurable LLM empty-answer retry limits, defaulting to three attempts, and return an explicit fallback when all attempts are empty or fail.

## Capabilities

### New Capabilities

- `llm-response-streaming-retry`: Configurable streaming LLM response collection, empty-result validation, retries, and safe exhausted-retry fallback.

### Modified Capabilities

- `agent-streaming-observability`: Add semantic progress and answer-chunk events to the normalized, request-correlated agent stream.
- `console-agent-test`: Render real-time readable progress and streamed answer text without exposing raw event envelopes or internal state.

## Impact

- Affected areas: observability event transport, Router and nested Agent streams, Knowledge/Query/Plan LLM callers, LLM configuration, console output, and focused tests.
- Existing mock MCP-only scope is unchanged; no real cluster integration is introduced.
