## 1. Console harness and lifecycle

- [x] 1.1 Add an executable `backend/app/` console test module with a documented `python -m` invocation.
- [x] 1.2 Detect, stop, and wait for an existing local `app.mcp.server` process before launching a fresh managed child; reject an unknown process that still owns port `8001`.
- [x] 1.3 Initialize the existing Agent `Container` only after MCP readiness succeeds and report actionable startup failures.

## 2. Router-driven console interaction

- [x] 2.1 Implement an async console loop that ignores blank input, exits on `exit`/`quit`/EOF/Ctrl+C, and forwards every other request unchanged as `user_query` to `router_agent.invoke`.
- [x] 2.2 Render the completed Router Agent state in JSON-safe readable output and handle individual Router invocation failures without leaking the MCP child process.
- [x] 2.3 Preserve Router ownership of intent classification and subagent dispatch; do not add console-side query, plan, knowledge, or MCP-tool selection.

## 3. Verification

- [x] 3.1 Add isolated tests using fake process discovery, subprocess, readiness, input, and Router Agent dependencies for prior-server replacement, startup ordering, request forwarding, blank/exit behavior, cleanup, and failure handling.
- [x] 3.2 Run focused tests, static checks, and `openspec validate add-console-agent-test --strict`.
- [x] 3.3 If local dependencies are available, run one `list node` console smoke test and report the result separately from automated verification.
