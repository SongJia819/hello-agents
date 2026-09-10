## 1. Routing and capability contracts

- [x] 1.1 Register the Knowledge Agent `chat/conversation` capability and extend Router structured output, prompt guidance, and tests to distinguish OCP documentation, other supported Agent work, and eligible ordinary conversation.
- [x] 1.2 Preserve existing unsupported responses for routes outside all registered capabilities rather than treating every unsupported request as chat.

## 2. Knowledge Agent direct chat

- [x] 2.1 Add a direct-chat service/node that invokes the configured LLM with only the current user message, shared streaming/retry behavior, and a transparent fallback.
- [x] 2.2 Add a Knowledge graph branch for `answer` versus `chat`, preserving the existing retrieval-backed answer path and evidence state only for documentation questions.

## 3. Verification

- [x] 3.1 Add focused unit tests for direct-chat success, direct-chat LLM failure, no retrieval/citation use, routing precedence, and documentation-path regression.
- [x] 3.2 Run focused automated tests, Python compilation, and `openspec validate add-knowledge-chat-fallback --strict`; record whether live LLM integration is available.

## Verification Record

- Focused automated tests passed: 42 tests covering direct chat, routing/capabilities, Knowledge retrieval regression (except the existing stream lifecycle test), Query Agent, and shared LLM streaming.
- The existing `test_knowledge_stream_emits_retrieval_phase_progress` assertion passed when run alone, but its process did not exit within the command waiting window in this environment; it was not counted in the 42-test completed process.
- Python compilation passed for every changed runtime module.
- `openspec validate add-knowledge-chat-fallback --strict`: passed.
- Live LLM integration was not run because no local LLM endpoint was started; direct-chat behavior is covered with injected test models.
