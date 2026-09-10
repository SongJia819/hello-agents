## ADDED Requirements

### Requirement: Mock-only iDRAC inventory tools
The MCP server SHALL provide `list_idrac_nodes` and `get_idrac_node` tools backed exclusively by the local SQLite mock iDRAC inventory. These tools MUST NOT connect to a real Dell iDRAC/Redfish endpoint, Kubernetes, OpenShift, or other external infrastructure.

#### Scenario: An iDRAC MCP tool is invoked
- **WHEN** a client invokes either iDRAC inventory tool
- **THEN** the server obtains its response only from the local SQLite mock store
