## MODIFIED Requirements

### Requirement: All runtime Agents expose normalized execution streaming
The Router, Query, Plan, and Knowledge Agents SHALL expose an async streaming interface for a request. The interface SHALL emit JSON-safe, request-correlated event envelopes for node lifecycle progress, semantic work progress, streamed answer chunks, and one terminal final-result event. Each event SHALL identify the originating agent and node, and the terminal event SHALL contain the completed agent state or a safe failure payload. Semantic progress events SHALL identify a stable phase and status and SHALL NOT expose prompts, raw MCP results, retrieval chunks, or secrets.

#### Scenario: Router delegates to a query subagent
- **WHEN** a Router request is classified and dispatched to the Query Agent
- **THEN** the stream emits Router progress and Query node, semantic progress, and answer-chunk events in execution order before one Router final-result event

#### Scenario: Knowledge Agent reports retrieval phases
- **WHEN** a caller streams a Knowledge Agent documentation request with supporting documents
- **THEN** it receives real-time `progress` events for recall started/completed, RRF started/completed, rerank started/completed, and LLM generation started/completed before the terminal final-result event

#### Scenario: A node fails
- **WHEN** a runtime graph node raises an exception
- **THEN** the stream emits a safe node-failed event with request, agent, and node identifiers and does not expose sensitive state

#### Scenario: Answer text is generated incrementally
- **WHEN** an answer-generating LLM returns text through its async stream
- **THEN** the Agent stream emits ordered answer-chunk events as chunks arrive and stores the complete joined text in the terminal `answer`

### Requirement: Log every runtime node lifecycle to a file
The system SHALL write structured JSON Lines records for start, successful completion, and failure of every Router, Query, Plan, and Knowledge runtime node. Records SHALL include timestamp, request ID, agent, node, event, and safe metadata, and SHALL be written to a configurable local file path whose default is `backend/logs/agent-runtime.log`.

#### Scenario: A query workflow completes
- **WHEN** Router, Query cluster resolution, and Query list nodes complete successfully
- **THEN** the configured log file contains correlated start and completion records for each executed node

#### Scenario: A plan node fails validation
- **WHEN** Plan Agent plan creation catches or raises a validation failure
- **THEN** the log file contains a request-correlated failure record with a safe error summary

#### Scenario: State includes a secret
- **WHEN** a node state or result includes a field named password, token, secret, username, or API key
- **THEN** that value is redacted from both stream event payloads and file log records

### Requirement: Preserve existing non-stream invocation behavior
The existing `invoke` interface for every Agent SHALL continue to return the completed graph state. Streaming and logging SHALL not change router intent classification, supported capability outcomes, MCP mock responses, or final answer/result semantics.

#### Scenario: Existing query invocation is used
- **WHEN** a caller invokes the Router Agent through its existing `invoke` method for `list node`
- **THEN** it returns the same completed query result shape while also writing node logs
