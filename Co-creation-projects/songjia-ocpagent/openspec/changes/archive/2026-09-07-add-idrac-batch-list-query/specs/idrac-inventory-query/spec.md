## MODIFIED Requirements

### Requirement: List iDRAC inventory through MCP
The MCP server SHALL expose a `list_idrac_nodes` tool that accepts an optional `sn` array. When `sn` is omitted or empty, it SHALL return every complete mock iDRAC inventory record without requiring a cluster identifier or connecting to external infrastructure. When `sn` contains one or more serial numbers, it SHALL return matching complete records in the input serial order, omit unknown serial numbers, and return each matching iDRAC record at most once.

#### Scenario: MCP client lists all iDRAC records
- **WHEN** a client invokes `list_idrac_nodes` without `sn` or with an empty `sn` array
- **THEN** the server returns the complete ten-record local mock iDRAC inventory

#### Scenario: MCP client lists selected iDRAC records by serial number
- **WHEN** a client invokes `list_idrac_nodes` with `sn` set to `DELLSN02`, `DELLSN01`, `DELLSN02`, and an unknown serial number
- **THEN** the server returns only `DELLSN02` followed by `DELLSN01`, each once

### Requirement: List iDRAC inventory through the Query Agent
The Query Agent SHALL support `idrac` as a general `list` resource. A list request containing only `idrac` SHALL return iDRAC records under the `idrac` key in `tool_result`; a request containing `idrac` with `node` and/or `pod` SHALL retain one ordered, resource-keyed result entry per requested resource. The Query Agent SHALL invoke one service-layer iDRAC list operation as part of its common resource-operation mapping. The service layer SHALL accept zero or more ordered iDRAC selectors, each an SN or iDRAC IP: zero selectors SHALL list all iDRAC records, serial-number-only selectors SHALL use one batch iDRAC list request, and selectors containing an iDRAC IP SHALL return matching records in selector order without duplicates through the single-record lookup contract.

#### Scenario: Query Agent lists all iDRAC inventory
- **WHEN** the Router resolves a general list request whose only resource is `idrac` and no iDRAC selectors are supplied
- **THEN** the Query Agent returns all ten iDRAC records as the `idrac` entry in `tool_result`

#### Scenario: Query Agent lists selected iDRAC serial numbers
- **WHEN** the Router resolves an iDRAC list request with one or more serial-number selectors
- **THEN** the Query Agent invokes one service-layer iDRAC list operation, which uses one batch iDRAC list request and returns only matching complete inventory records under the `idrac` key in serial-selector order without duplicates

#### Scenario: Query Agent lists selected iDRAC IP addresses
- **WHEN** the Router resolves an iDRAC list request containing an iDRAC-IP selector
- **THEN** the Query Agent invokes one service-layer iDRAC list operation, which uses the single-record lookup contract and returns matching records in original selector order without duplicates

#### Scenario: Query Agent lists iDRAC with other resources
- **WHEN** the Router resolves one general list request for `node`, `pod`, and `idrac`
- **THEN** the Query Agent returns `node`, `pod`, and `idrac` entries in `tool_result` and does not change the result shape of the existing resources
