## ADDED Requirements

### Requirement: Persist iDRAC inventory in local relational tables
The local SQLite mock fixture SHALL create and retain `idrac_nodes`, `idrac_network_interfaces`, and `idrac_storage_devices` tables with enforced foreign-key relationships. An iDRAC node SHALL retain a unique serial number, a unique iDRAC IP, and system information; its network interfaces and storage devices SHALL belong to that iDRAC node. Initialization SHALL seed the prescribed ten-record iDRAC fixture exactly once and SHALL not duplicate it when the database is reopened.

#### Scenario: iDRAC tables are initialized or reopened
- **WHEN** the mock data store is opened before or after iDRAC inventory tables exist
- **THEN** the tables are available with foreign keys enabled and the prescribed ten-record inventory exists without duplicated parent or child rows

### Requirement: Query iDRAC inventory safely from the local fixture
The data store SHALL retrieve full iDRAC inventory records and an individual record selected by serial number or iDRAC IP with parameterized SQLite statements. It SHALL map parent, system, network-interface, and storage-device data into typed response models and SHALL not connect to external infrastructure.

#### Scenario: A matching iDRAC selector is queried
- **WHEN** the store receives a serial number or iDRAC IP that matches a seeded record
- **THEN** it returns that complete typed record with its related network and storage inventory

#### Scenario: A nonmatching iDRAC selector is queried
- **WHEN** the store receives a valid serial number or iDRAC IP that matches no seeded record
- **THEN** it returns no record without issuing an external request
