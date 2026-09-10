## ADDED Requirements

### Requirement: Mock-only cluster tools
The MCP server SHALL provide mock cluster-management responses and MUST NOT connect to a real Kubernetes or OpenShift cluster.

#### Scenario: Cluster discovery uses mock data
- **WHEN** a client invokes `list_clusters`
- **THEN** the server returns one or more mock cluster summaries

### Requirement: Mock node listing
The MCP server SHALL provide a `list_nodes` tool that accepts a cluster identifier and returns mock node data associated with that identifier.

#### Scenario: Nodes are listed for a requested cluster
- **WHEN** a client invokes `list_nodes` with a cluster identifier
- **THEN** the server returns at least one mock node whose name includes that identifier

### Requirement: MCP health check
The MCP server SHALL expose a `health` tool that reports the availability of the mock server.

#### Scenario: Health check succeeds
- **WHEN** a client invokes `health`
- **THEN** the server returns `OK`

