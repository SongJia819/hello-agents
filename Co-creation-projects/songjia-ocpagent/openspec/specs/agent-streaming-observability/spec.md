## Purpose

Define consistent execution streaming and local node lifecycle logging for all runtime Agents.

## Requirements

### Requirement: All runtime Agents expose normalized execution streaming
The Router, Query, Plan, and Knowledge Agents SHALL expose an async streaming interface for a request. The interface SHALL emit JSON-safe, request-correlated event envelopes for node lifecycle progress and one terminal final-result event. Each event SHALL identify the originating agent and node, and the terminal event SHALL contain the completed agent state or a safe failure payload.

#### Scenario: Router delegates to a query subagent
- **WHEN** a Router request is classified and dispatched to the Query Agent
- **THEN** the stream emits Router progress and Query node events in execution order before one Router final-result event

#### Scenario: Knowledge Agent is streamed directly
- **WHEN** a caller streams a Knowledge Agent documentation request
- **THEN** the agent emits its answer-node progress and one final-result event using the same event envelope as the other agents

#### Scenario: A node fails
- **WHEN** a runtime graph node raises an exception
- **THEN** the stream emits a safe node-failed event with request, agent, and node identifiers and does not expose sensitive state

### Requirement: Log every runtime node lifecycle to a file
The system SHALL write structured JSON Lines records for start, successful completion, and failure of every Router, Query, Plan, and Knowledge runtime node. Records SHALL include timestamp, request ID, agent, node, event, the original user message, and safe metadata, and SHALL be written to a configurable local file path whose default is `backend/logs/agent-runtime.log`. The original message SHALL be redacted using the same sensitive-value rules as other logged state and payloads.

#### Scenario: A query workflow completes
- **WHEN** Router, Query cluster resolution, and Query list nodes complete successfully
- **THEN** the configured log file contains correlated start and completion records for each executed node, each including the submitted user message

#### Scenario: A plan node fails validation
- **WHEN** Plan Agent plan creation catches or raises a validation failure
- **THEN** the log file contains a request-correlated failure record with the submitted user message and a safe error summary

#### Scenario: State includes a secret
- **WHEN** a node state or result includes a field named password, token, secret, username, or API key
- **THEN** that value is redacted from both stream event payloads and file log records, including the logged user message when represented in structured state

### Requirement: Preserve the original user message in agent state
The system SHALL preserve the submitted message as `user_message` in `AgentState` for Router, Query, Plan, and Knowledge workflows, while retaining `user_query` for existing prompt and API compatibility.

#### Scenario: A chat endpoint invokes Router
- **WHEN** a client submits a non-empty chat message to the Router workflow
- **THEN** the resulting workflow state contains that text in both `user_message` and `user_query`

#### Scenario: A direct Agent caller provides only user_query
- **WHEN** a direct Query, Plan, or Knowledge Agent invocation supplies `user_query` without `user_message`
- **THEN** the workflow normalizes and preserves the same text as `user_message` before node lifecycle logging

### Requirement: Preserve existing non-stream invocation behavior
The existing `invoke` interface for every Agent SHALL continue to return the completed graph state. Streaming and logging SHALL not change router intent classification, supported capability outcomes, MCP mock responses, or final answer/result semantics.

#### Scenario: Existing query invocation is used
- **WHEN** a caller invokes the Router Agent through its existing `invoke` method for `list node`
- **THEN** it returns the same completed query result shape while also writing node logs
