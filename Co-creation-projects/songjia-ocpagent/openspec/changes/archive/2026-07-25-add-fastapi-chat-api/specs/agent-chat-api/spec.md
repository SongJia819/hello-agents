## ADDED Requirements

### Requirement: Chat endpoint invokes the router workflow
The system SHALL expose `POST /v1/chat`, accept a JSON object with a non-empty `message` string, and invoke the configured router agent with that value as `user_query`.

#### Scenario: A chat message is routed
- **WHEN** a client posts `{ "message": "list nodes" }` to `/v1/chat`
- **THEN** the endpoint invokes the router agent with `user_query` equal to `list nodes` and returns an HTTP success response

#### Scenario: A chat message is missing
- **WHEN** a client posts a request without a valid non-empty `message` string to `/v1/chat`
- **THEN** the endpoint returns a validation error and does not invoke the router agent

### Requirement: Chat response presents safe agent results
The system SHALL return a JSON-safe chat response containing the submitted message, available routing metadata, the supported status, optional answer, and sanitized result data from the completed router workflow.

#### Scenario: A supported node query completes
- **WHEN** the router workflow returns a supported node-query result
- **THEN** the chat response includes the route metadata and node result data without `username` or `password` fields

#### Scenario: An unsupported request completes
- **WHEN** the router workflow returns an unsupported-feature result
- **THEN** the chat response includes `supported` as false and the returned unsupported answer without requiring a tool result

### Requirement: Application startup initializes shared dependencies
The FastAPI application SHALL initialize its shared agent container before accepting chat requests, and the executable backend entrypoint SHALL start the application through an ASGI server.

#### Scenario: Server starts successfully
- **WHEN** the mock MCP service is available and the backend start command is run
- **THEN** the application initializes the container and serves the `/v1/chat` endpoint

#### Scenario: Endpoint test isolates external services
- **WHEN** the automated chat API test runs
- **THEN** it substitutes the router dependency and completes without connecting to a local LLM or MCP server
