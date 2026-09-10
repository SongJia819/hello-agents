## Why

The project has isolated MCP and agent test scripts, but there is no single executable that brings up the mock MCP dependency and lets a developer exercise the complete Router-to-subagent workflow interactively. A console entrypoint makes the demo flow inspectable without starting the HTTP API separately.

## What Changes

- Add a main console test script under `backend/app/` that starts the local mock MCP Server and the configured Agent container.
- Accept repeated user requests from standard input and send each non-empty request to the Router Agent.
- Display the routed final state in a JSON-safe, readable form while leaving all intent recognition and subagent dispatch to the existing Router graph.
- Before startup, detect and stop an already-running local `app.mcp.server` instance, then start a fresh MCP child process; handle startup failures, Ctrl+C/end-of-input, and shutdown cleanly.
- Add automated tests for console request handling and MCP process lifecycle seams without requiring a live LLM, Qdrant, or network port.

## Capabilities

### New Capabilities
- `console-agent-test`: Interactively exercise the complete mock-MCP and Router Agent workflow from a local terminal.

### Modified Capabilities

- None.

## Impact

- Affected areas: a new executable in `backend/app/`, local process orchestration, and focused tests under `backend/tests/`.
- The script uses the existing mock-only MCP server at port `8001` and existing Router Agent/subagent graph; it adds no real cluster connectivity or new routing policy.
