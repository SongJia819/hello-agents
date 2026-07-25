## 1. API Runtime Setup

- [x] 1.1 Add the FastAPI and ASGI server runtime dependencies using the repository’s dependency-management convention.
- [x] 1.2 Create the importable FastAPI application and lifespan startup that initializes and stores one shared `Container`.
- [x] 1.3 Add the `backend/app/run.py` Uvicorn launch path for the application.

## 2. Chat Endpoint

- [x] 2.1 Define validated request and response models for `POST /v1/chat`.
- [x] 2.2 Implement the chat route to forward `message` as `user_query` to `router_agent.invoke`.
- [x] 2.3 Map final router state into a JSON-safe response, including route metadata, supported status, answer, and sanitized result data.
- [x] 2.4 Ensure HTTP response mapping removes mock node `username` and `password` fields.

## 3. Verification

- [x] 3.1 Add API tests under `backend/tests/` with an injected or overridden async router/container fake.
- [x] 3.2 Test successful message forwarding and sanitized supported-query output.
- [x] 3.3 Test invalid chat input and unsupported-route output without local LLM or MCP connections.
- [x] 3.4 Run the relevant backend test suite and record the result.

Verification result (2026-07-25): `python -m unittest -v tests.test_chat_api` and
`python -m unittest discover -v` both passed (3 tests each).
