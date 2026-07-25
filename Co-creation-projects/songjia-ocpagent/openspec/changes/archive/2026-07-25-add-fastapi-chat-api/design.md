## Context

The current backend exposes the router agent only through Python demonstration scripts. `Container` owns the MCP client and router graph, and its asynchronous `initialize` method discovers tools from the local mock MCP server. `backend/app/api/` and `backend/app/run.py` are empty. The project is a demo and its cluster data must remain mock-only.

## Goals / Non-Goals

**Goals:**

- Expose the existing router workflow through a small FastAPI `POST /v1/chat` interface.
- Initialize one shared application container during FastAPI lifespan startup.
- Return a stable, JSON-safe response without credential-shaped fields from mock nodes.
- Make the endpoint testable without requiring local Ollama or MCP processes.

**Non-Goals:**

- Add authentication, streaming, persistence, session memory, or frontend work.
- Add agent capabilities, modify routing behavior, or access a real OpenShift/Kubernetes cluster.
- Expose raw LangGraph state or internal MCP data directly to clients.

## Decisions

### Use an application-owned container initialized by FastAPI lifespan

The FastAPI app will create one `Container`, await `initialize()` during startup, and retain it on application state for endpoint access. This avoids recreating MCP tool discovery for every chat request and keeps resource lifecycle explicit. Creating a container per request was considered but adds repeated external initialization and makes testing less representative.

### Define explicit chat request and response schemas

`POST /v1/chat` will accept a non-empty `message` field. The handler will invoke `router_agent.invoke` with `{"user_query": message}` and translate the returned graph state into a response containing the original message, routing metadata when available, the supported flag, answer when available, and safe result data. Returning the raw graph state was rejected because it contains non-JSON-safe LangChain objects and leaks internal workflow details.

### Sanitize HTTP-facing tool results

The response mapper will serialize Pydantic models and remove `username`, `password`, and other credential-shaped fields before rendering node results. This protects consumers from mock secrets and establishes a safe boundary even though all data is simulated. Reusing `Node.model_dump()` without filtering was rejected because its current schema includes `username` and `password`.

### Keep server launch separate from application construction

The API module will expose the ASGI application for import and testing; `backend/app/run.py` will contain the executable Uvicorn launch path. This supports test clients without starting a network listener and gives operators a direct backend start command.

### Test with an injected or overridden router dependency

API tests will replace the application router/container with an async fake and assert the HTTP request forwarding and response mapping. The test suite must not call the local LLM or MCP endpoints. End-to-end live dependency testing was rejected because it would make the requested API unit tests environment-dependent.

## Risks / Trade-offs

- [MCP initialization fails when the mock server is unavailable] → Fail application startup with a clear error; tests bypass the real container through the API’s test seam.
- [The router produces incomplete or unsupported state] → Map optional fields defensively and return the router’s supported status and answer rather than assuming node data exists.
- [Future tool results contain additional sensitive fields] → Centralize response sanitization and extend its denylist as models evolve.
- [A static response model constrains later agent features] → Use a generic safe `result` payload while keeping core chat metadata stable.

## Migration Plan

1. Add FastAPI and Uvicorn dependencies if they are not already available to the backend runtime.
2. Add the API module, lifespan initialization, response mapping, and Uvicorn entrypoint.
3. Add isolated endpoint tests and run the backend test suite.
4. Start the mock MCP server, then start the FastAPI application to verify the existing node-query demonstration flow.
5. Roll back by removing the new API entrypoint and dependency additions; existing router and MCP workflows remain independent of the HTTP layer.

## Open Questions

- None for the initial non-streaming demo endpoint.
