## MODIFIED Requirements

### Requirement: Mock-only cluster tools
The MCP server SHALL provide mock cluster-management responses from the project-local SQLite mock data store and MUST NOT connect to a real Kubernetes or OpenShift cluster.

#### Scenario: Cluster discovery uses SQLite mock data
- **WHEN** a client invokes `list_clusters`
- **THEN** the server returns one or more simulated cluster summaries queried from the local SQLite store

### Requirement: Mock resource providers for general listing
The MCP server SHALL provide mock node and pod data providers that accept a cluster identifier and return SQLite-backed data associated with that identifier without connecting to a real Kubernetes or OpenShift cluster. Node responses SHALL include their typed lifecycle status, iDRAC IP, network interfaces, and storage devices. The query agent SHALL use these providers only behind its general `list` capability.

#### Scenario: A node resource is listed for a requested cluster
- **WHEN** the general list workflow requests node data for a cluster identifier
- **THEN** the server returns one or more SQLite-backed nodes belonging to that cluster

#### Scenario: A standalone node is stored but not listed for a cluster
- **WHEN** a node has no cluster ID because its status is `new`, `reimage`, or `removed`
- **THEN** a cluster-scoped node listing does not return that node

#### Scenario: A pod resource is listed for a requested cluster
- **WHEN** the general list workflow requests pod data for a cluster identifier
- **THEN** the server returns one or more SQLite-backed pods belonging to that cluster

### Requirement: MCP health check
The MCP server SHALL expose a `health` tool that reports the availability of the local SQLite-backed mock server.

#### Scenario: Health check succeeds
- **WHEN** a client invokes `health` while the local SQLite mock data store can be opened
- **THEN** the server returns `OK`
