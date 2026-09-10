## ADDED Requirements

### Requirement: Maintain deterministic mock iDRAC inventory
The system SHALL maintain exactly ten standalone mock iDRAC inventory records identified by serial numbers `DELLSN01` through `DELLSN10` and iDRAC IP addresses `168.0.0.1` through `168.0.0.10`. Each record SHALL include system information whose default operating system is `Red Hat Enterprise Linux 8.0`, at least one network-interface record with a speed of 20,000 Mbps, and exactly ten storage-device records with serial numbers `<SN>storage01` through `<SN>storage10` for that record's serial number. The inventory SHALL be backed solely by the local SQLite mock store.

#### Scenario: A complete seeded iDRAC inventory is read
- **WHEN** the local fixture is initialized and all iDRAC inventory records are requested
- **THEN** it returns exactly ten complete records covering `DELLSN01`–`DELLSN10` and `168.0.0.1`–`168.0.0.10`, with 20,000 Mbps network interfaces, `Red Hat Enterprise Linux 8.0`, and ten correctly prefixed storage serials per record

### Requirement: List iDRAC inventory through MCP
The MCP server SHALL expose a `list_idrac_nodes` tool that returns every complete mock iDRAC inventory record without requiring a cluster identifier or connecting to external infrastructure.

#### Scenario: MCP client lists all iDRAC records
- **WHEN** a client invokes `list_idrac_nodes`
- **THEN** the server returns the complete ten-record local mock iDRAC inventory

### Requirement: Retrieve one iDRAC inventory record through MCP
The MCP server SHALL expose a `get_idrac_node` tool that accepts exactly one selector: `sn` or `idrac_ip`. It SHALL return the complete matching mock iDRAC inventory record when either selector identifies one record, and SHALL return no record when a valid selector has no match. It SHALL reject calls that provide neither selector or both selectors.

#### Scenario: MCP client retrieves inventory by serial number
- **WHEN** a client invokes `get_idrac_node` with `sn` set to `DELLSN01`
- **THEN** the server returns the complete record whose iDRAC IP is `168.0.0.1`

#### Scenario: MCP client retrieves inventory by iDRAC IP
- **WHEN** a client invokes `get_idrac_node` with `idrac_ip` set to `168.0.0.10`
- **THEN** the server returns the complete record whose serial number is `DELLSN10`

#### Scenario: MCP client supplies ambiguous or missing selectors
- **WHEN** a client invokes `get_idrac_node` with both selectors or with neither selector
- **THEN** the server rejects the request with a selector-validation error

### Requirement: List iDRAC inventory through the Query Agent
The Query Agent SHALL support `idrac` as a general `list` resource. A list request containing only `idrac` SHALL return iDRAC records under the `idrac` key in `tool_result`; a request containing `idrac` with `node` and/or `pod` SHALL retain one ordered, resource-keyed result entry per requested resource. The Query Agent SHALL accept zero or more ordered iDRAC selectors, each an SN or iDRAC IP: zero selectors SHALL list all iDRAC records, while one or more selectors SHALL return the matching iDRAC records in selector order without duplicates.

#### Scenario: Query Agent lists all iDRAC inventory
- **WHEN** the Router resolves a general list request whose only resource is `idrac` and no iDRAC selectors are supplied
- **THEN** the Query Agent returns all ten iDRAC records as the `idrac` entry in `tool_result`

#### Scenario: Query Agent lists selected iDRAC nodes
- **WHEN** the Router resolves an iDRAC list request with one or more SN and/or iDRAC-IP selectors
- **THEN** the Query Agent returns only matching complete inventory records under the `idrac` key in the original selector order without duplicate records

#### Scenario: Query Agent lists iDRAC with other resources
- **WHEN** the Router resolves one general list request for `node`, `pod`, and `idrac`
- **THEN** the Query Agent returns `node`, `pod`, and `idrac` entries in `tool_result` and does not change the result shape of the existing resources
