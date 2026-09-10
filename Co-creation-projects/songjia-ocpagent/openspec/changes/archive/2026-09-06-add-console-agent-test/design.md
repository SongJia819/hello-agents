## Context

The current mock MCP server is executable through `app.mcp.server` on streamable HTTP port `8001`. `Container.initialize()` connects the MCP client and constructs the Router Agent, whose graph already performs intent classification, capability validation, and dispatch to query, plan, or knowledge subagents. Existing scripts either test the MCP client directly or invoke the container assuming an MCP server is already running.

The requested script is a developer-facing integration harness, not a replacement for the FastAPI chat endpoint or a new agent implementation.

## Goals / Non-Goals

**Goals:**

- Start the project-local mock MCP server before initializing the existing Agent container.
- Provide an interactive console loop that forwards each request only to `router_agent.invoke({"user_query": ...})`.
- Render final agent state safely and provide clear lifecycle/error messages.
- Replace an already-running local `app.mcp.server` instance before creating the fresh MCP child process, then shut down the new managed instance on exit.

**Non-Goals:**

- Reimplementing router intent recognition, capability checks, or any subagent dispatch policy.
- Starting FastAPI, connecting to real OpenShift infrastructure, or accepting remote network clients.
- Making Qdrant/Ollama dependencies mandatory for non-knowledge requests.

## Decisions

### Launch MCP as a managed subprocess

The console script will first inspect local process command lines for an existing `python -m app.mcp.server` instance. It will stop and wait for every matching instance before starting a fresh `python -m app.mcp.server` child process, poll its local connection readiness with a bounded timeout, then initialize `Container`. Its `finally` path terminates and waits for the exact fresh child process, escalating to kill only when it does not exit in time. If port `8001` remains occupied by a non-matching process, the script fails rather than killing an unknown process.

Running the server in-process would complicate FastMCP's blocking server lifecycle and cleanup. Requiring the user to start it separately would not satisfy the requested one-command test harness.

### Keep the Router Agent as the sole request entrypoint

For each non-empty line, the script calls the already-configured `router_agent` with `user_query`, then prints a JSON-safe version of the returned final state. It does not inspect the text to choose a subagent or invoke MCP tools directly.

This preserves production-equivalent routing behavior and ensures query, plan, and knowledge requests all exercise their existing paths.

### Separate orchestration from console I/O

The implementation will expose small async helpers for MCP process startup, request execution, and state formatting. `main()` owns `input()`/printing and translates EOF, `exit`/`quit`, and Ctrl+C into normal shutdown. Process and container dependencies will be injectable or patchable for unit tests.

This avoids tests that bind ports, launch a real MCP process, or invoke local LLM/Qdrant services.

### Use an explicit developer command

The script will document a `PYTHONPATH=backend python -m app.console_agent_test` invocation. It runs in the current terminal and uses the existing fixed local MCP endpoint expected by `MCPClient`.

## Risks / Trade-offs

- [A prior project MCP server owns port `8001`] → identify it by its `app.mcp.server` command line, stop it, wait for release, and start a fresh instance.
- [Port `8001` is occupied by an unknown process] → fail with a clear startup message and never terminate the unknown process.
- [MCP server fails before becoming ready] → surface child output/exit status, clean up the child, and do not initialize the container.
- [A knowledge question needs unavailable Qdrant/Ollama] → display the existing Knowledge Agent fallback; the console harness does not mask dependency failures.
- [Final state contains non-JSON-native objects] → apply the existing JSON encoder/sanitizer pattern or a bounded `default=str` fallback for display only.
- [Interactive input blocks automated tests] → test helpers with fake input, container, and subprocess interfaces instead of `main()` against live services.

## Migration Plan

1. Add the script and isolated lifecycle/dispatch tests.
2. Run the focused tests and static checks.
3. Optionally perform a local `list node` smoke test when port `8001` and the configured LLM are available.
4. Rollback consists of removing the standalone script; agent, MCP, and API runtime behavior remain unchanged.

## Open Questions

- None. The default exit commands will be `exit` and `quit`, matching the existing knowledge console tool.
