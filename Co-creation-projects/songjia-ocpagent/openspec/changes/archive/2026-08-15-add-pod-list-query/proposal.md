## Why

The current query workflow exposes node and pod retrieval as resource-specific paths. A single, general `list` capability that accepts one or more resources makes the mock-only query interface easier to use and demonstrates multi-resource orchestration without connecting to a real cluster.

## What Changes

- Define `list` as the only query action for supported mock resources.
- Allow one `list` request to select one or more resources; the initial supported resources are `node` and `pod`.
- Route and validate every requested resource before running the general list workflow.
- Return results keyed by resource name so callers receive a consistent result for one or more selected resources.
- Retain resource-specific mock MCP data providers behind the general list capability and preserve the mock-only safety boundary.

## Capabilities

### New Capabilities

- None.

### Modified Capabilities

- `agent-routing`: Support and dispatch the general `list` action with one or more supported resources through the query agent.
- `cluster-node-query`: Replace resource-specific query behavior with a general mock-cluster list workflow for node and pod resources.
- `mock-cluster-mcp`: Provide the mock node and pod data sources used by the general list capability.

## Impact

- Updates query and router agent graph/nodes, capabilities, cluster service, and MCP tool/client integration under `backend/app/`.
- Adds or extends assertion-based backend tests under `backend/tests/` for single- and multi-resource list requests.
- Preserves the mock-only safety boundary: no Kubernetes/OpenShift APIs, credentials, or external infrastructure are introduced.
