## 1. Trace context and log destinations

- [x] 1.1 Add optional `trace_id` to typed Agent state and create/normalize it at Router request entry while retaining direct-Agent supplied traces.
- [x] 1.2 Extend observability records and streamed envelopes with ISO-8601 timestamps, trace IDs, named steps, and terminal `duration_ms` values measured with a monotonic clock.
- [x] 1.3 Preserve aggregate `agent-runtime.log` compatibility and dual-write each safe JSON Lines record to default Router, Query, Plan, or Knowledge log files in the configured local log directory.

## 2. Detailed runtime instrumentation

- [x] 2.1 Instrument Router classification, Query cluster/list operations, and Plan generation with trace-correlated named-step timing records.
- [x] 2.2 Instrument Knowledge dense/sparse recall, RRF fusion, and reranking with stage timing and detailed retained chunk payloads.
- [x] 2.3 Record every available streamed LLM output chunk and fallback non-stream output, including available provider reasoning/output metadata, with generation-attempt timing and existing sensitive-field redaction.
- [x] 2.4 Add one shared 300-second timeout and 60-second trace-correlated thinking heartbeat around every Router, Plan, Query, and Knowledge LLM invocation; cancel calls and suppress late output on timeout.
- [x] 2.5 Filter Console progress to frontend-relevant timestamped milestones, preserve incremental answer rendering, and keep detailed step/chunk data out of the frontend display.

## 3. Verification

- [x] 3.1 Add focused tests that parse aggregate and Agent-specific JSON Lines logs and verify trace propagation, destinations, timestamp format, terminal durations, and redaction.
- [x] 3.2 Add focused Knowledge/LLM tests for retrieval-stage chunk detail and ordered output-chunk logging without a live LLM, Qdrant, or reranker.
- [x] 3.3 Add focused async tests for 60-second heartbeat cadence, five-minute cancellation, timeout logging, late-output suppression, and concise timestamped Console output.
- [x] 3.4 Run relevant backend tests, static compilation, `git diff --check`, and `openspec validate add-agent-trace-logs --strict`.

## 4. Runtime log compaction

- [x] 4.1 Keep retrieval chunks and LLM output payloads out of `agent-runtime.log`, while retaining them in `knowledge.log`; add focused coverage and rerun validation.
- [ ] 4.2 Summarize generic aggregate lifecycle payloads so nested `knowledge_result.diagnostics`, retrieval chunks, LLM output text, and provider metadata cannot enter `agent-runtime.log` through `node_completed` or delegated results; retain the complete diagnostic payload only in the originating Agent log, add focused regression coverage, and rerun validation.
