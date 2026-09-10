## MODIFIED Requirements

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
