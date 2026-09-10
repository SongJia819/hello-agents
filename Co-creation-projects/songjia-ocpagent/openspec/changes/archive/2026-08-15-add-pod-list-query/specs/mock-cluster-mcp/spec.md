## ADDED Requirements

### Requirement: Mock resource providers for general listing
The MCP server SHALL provide mock node and pod data providers that accept a cluster identifier and return data associated with that identifier without connecting to a real Kubernetes or OpenShift cluster. The query agent SHALL use these providers only behind its general `list` capability.

#### Scenario: A node resource is listed for a requested cluster
- **WHEN** the general list workflow requests node data for a cluster identifier
- **THEN** the server returns one or more mock nodes whose names include that identifier

#### Scenario: A pod resource is listed for a requested cluster
- **WHEN** the general list workflow requests pod data for a cluster identifier
- **THEN** the server returns one or more mock pods whose names include that identifier
