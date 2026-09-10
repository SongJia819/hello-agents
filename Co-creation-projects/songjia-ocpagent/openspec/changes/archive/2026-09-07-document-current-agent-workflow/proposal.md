## Why

The repository has an implemented but undocumented router, query, and mock MCP workflow. A baseline contract is needed so future work can distinguish current behavior from planned agent-platform capabilities.

## What Changes

- Document the current intent-routing and capability-validation behavior.
- Document the current node-query workflow and its mock-cluster selection behavior.
- Document the mock MCP contract for cluster discovery, node listing, and health checks.
- Add no production cluster integration, API, frontend, memory, or additional agent capabilities.

## Capabilities

### New Capabilities

- `agent-routing`: Classify a user request and dispatch supported requests to the available agent graph.
- `cluster-node-query`: Resolve the available mock cluster and retrieve its nodes through the service layer.
- `mock-cluster-mcp`: Provide the mock MCP tools consumed by the agent workflows.

### Modified Capabilities

- None.

## Impact

- Documents the behavior in `backend/app/agents/router`, `backend/app/agents/query`, `backend/app/services`, and `backend/app/mcp`.
- Establishes main specifications in `openspec/specs`.
- Does not modify application code, public HTTP APIs, or external dependencies.
