## ADDED Requirements

### Requirement: Mock cluster resolution
The system SHALL obtain the available clusters through the cluster service and use the first returned cluster as the current cluster for the node-query workflow.

#### Scenario: Cluster is available
- **WHEN** the node-query workflow begins and the mock cluster service returns clusters
- **THEN** the system stores the first returned cluster as `current_cluster`

### Requirement: Node listing through the service layer
The system SHALL request nodes for the current cluster through the cluster service and store the validated node models as the tool result.

#### Scenario: Nodes are returned for current cluster
- **WHEN** a current cluster has been resolved
- **THEN** the system calls `list_nodes` with that cluster identifier and stores the returned nodes in `tool_result`

