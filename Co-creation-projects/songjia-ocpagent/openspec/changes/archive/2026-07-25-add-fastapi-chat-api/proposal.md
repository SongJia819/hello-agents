## Why

The implemented router and query workflows cannot yet be called through an HTTP interface, preventing a frontend or API client from using the demo. A small FastAPI boundary is needed to expose the existing mock-only agent flow without adding cluster infrastructure operations.

## What Changes

- Add a FastAPI application with a `POST /v1/chat` endpoint that submits a user message to the router agent.
- Add application startup logic in `backend/app/run.py` to run the HTTP server and initialize the shared agent container.
- Define request and response contracts that return a JSON-safe, consumer-oriented representation of router and query results.
- Add automated API tests that isolate the router dependency and do not require a local LLM or MCP server.
- Redact credential-shaped mock node fields from HTTP responses.

## Capabilities

### New Capabilities

- `agent-chat-api`: Provide an HTTP chat endpoint that invokes the existing router workflow and returns safe agent results.

### Modified Capabilities

- None.

## Impact

- Adds FastAPI/Uvicorn runtime dependencies and code under `backend/app/api/` and `backend/app/run.py`.
- Adds API tests under `backend/tests/` because the repository currently has no root-level `tests/` directory.
- Makes the mock router/query workflow available to future frontend clients while preserving the project’s mock-only cluster boundary.
