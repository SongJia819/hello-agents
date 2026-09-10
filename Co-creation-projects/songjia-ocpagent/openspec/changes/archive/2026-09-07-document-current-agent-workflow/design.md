## Context

The implemented backend uses two LangGraph workflows: a router graph and a node-query graph. The router calls a structured-output LLM, validates the resulting route against a capability map, and dispatches supported node queries to the query graph. The query graph obtains mock cluster data through a service and MCP client. The FastMCP server is a local mock provider.

This change establishes specifications for that existing behavior. It deliberately does not describe the planner, execution, knowledge, memory, REST API, or frontend capabilities mentioned in the project overview because they are not implemented in the repository.

## Goals / Non-Goals

**Goals:**

- Capture the observable behavior and boundaries of the router, query, and MCP layers.
- Provide scenario-based contracts that can guide future automated tests and implementation changes.
- Establish main OpenSpec capability documents without changing runtime behavior.

**Non-Goals:**

- Change agent routing, cluster selection, tool schemas, or mock data.
- Add production infrastructure integrations or credentials.
- Implement missing agent types, APIs, frontend, or persistence.

## Decisions

### Use one capability per runtime boundary

The baseline separates `agent-routing`, `cluster-node-query`, and `mock-cluster-mcp`. This matches the existing control-flow and service boundaries, so changes can evolve independently. A single end-to-end capability was considered but would obscure whether a change affects LLM routing, LangGraph orchestration, or the MCP contract.

### Specify current behavior rather than intended architecture

The specifications preserve the current first-cluster resolution and node-only query capability. The broader architecture in `AGENTS.md` is a roadmap, not a current contract; specifying it now would create requirements unsupported by the code.

### Keep the MCP provider explicitly mock-only

The mock-only constraint is captured as a normative requirement because it is a project safety boundary. This prevents future work from interpreting the MCP interfaces as permission to access real cluster infrastructure.

## Risks / Trade-offs

- [The first-cluster rule is simplistic] → Document it accurately now; replace it with explicit cluster selection in a later change.
- [LLM classification can produce invalid values] → The current baseline records capability validation only; add schema/error-handling requirements when routing hardening is implemented.
- [Mock node data includes credential-shaped fields] → Treat those as demo data and create a dedicated safety change before exposing results through an API or UI.

## Migration Plan

1. Add the change artifacts and validate their structure.
2. Sync the new capability specifications into `openspec/specs`.
3. Leave the documentation change active as traceability for the initial baseline; archive it only when the project’s workflow calls for archival.

## Open Questions

- Should a future query interface require users to select a cluster rather than defaulting to the first mock cluster?
- What final answer schema should successful agent workflows return to API and UI consumers?
