## MODIFIED Requirements

### Requirement: Mock-only iDRAC inventory tools
The MCP server SHALL provide `list_idrac_nodes` with an optional `sn` array and `get_idrac_node` backed exclusively by the local SQLite mock iDRAC inventory. These tools MUST NOT connect to a real Dell iDRAC/Redfish endpoint, Kubernetes, OpenShift, or other external infrastructure.

#### Scenario: An iDRAC MCP tool is invoked
- **WHEN** a client invokes either iDRAC inventory tool
- **THEN** the server obtains its response only from the local SQLite mock store

#### Scenario: A batch iDRAC list is invoked
- **WHEN** a client supplies one or more serial numbers to `list_idrac_nodes`
- **THEN** the server returns only matching mock iDRAC records without external requests
