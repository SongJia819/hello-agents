## ADDED Requirements

### Requirement: Maintain a local relational mock OCP fixture
The system SHALL maintain a project-local SQLite database file for MCP mock data. It SHALL create and retain `clusters`, `nodes`, `node_network_interfaces`, `node_storage_devices`, `namespaces`, and `pods` tables with enforced foreign-key relationships. Nodes SHALL have a nullable cluster association, a lifecycle status, and an iDRAC IP; network interfaces and storage devices SHALL belong to a node. Namespaces SHALL belong to clusters, and pods SHALL belong to both their cluster and namespace. The fixture SHALL contain exactly two simulated OCP clusters on first initialization, with each cluster having associated nodes, namespaces, and pods.

#### Scenario: Database is initialized for the first time
- **WHEN** the MCP data store is opened and its database file or tables do not exist
- **THEN** it creates the schema, enables foreign-key enforcement, and seeds two related simulated cluster data sets plus standalone node data

#### Scenario: Database is opened after a prior initialization
- **WHEN** the MCP data store is opened after its schema and seed rows already exist
- **THEN** it preserves existing fixture data and does not duplicate seed rows

#### Scenario: Resources belong to their seeded cluster
- **WHEN** the fixture is queried for resources of either simulated cluster
- **THEN** returned nodes and pods belong only to that cluster and each pod references a namespace belonging to the same cluster

### Requirement: Query the local fixture safely
The system SHALL retrieve mock resource data through parameterized SQLite statements and map rows into the MCP response models. It SHALL not connect to Kubernetes, OpenShift, or other external infrastructure.

#### Scenario: Unknown cluster is queried
- **WHEN** a query requests nodes or pods for an unknown cluster identifier
- **THEN** it returns an empty validated resource collection without issuing an external request

### Requirement: Model node ownership, lifecycle, and hardware inventory
The system SHALL define `NodeStatus` in `backend/app/models/` with exactly `new`, `added`, `reimage`, and `removed` values, and the typed Node model SHALL expose that status, `idrac_ip`, network-interface records, and storage-device records. The database SHALL require an `added` node to have a cluster ID and SHALL require `new`, `reimage`, and `removed` nodes to have no cluster ID.

#### Scenario: A node has been added to a cluster
- **WHEN** a seeded node has status `added`
- **THEN** it has a valid cluster ID and its MCP model includes iDRAC, network-interface, and storage-device information

#### Scenario: A node is not associated with a cluster
- **WHEN** a seeded node has status `new`, `reimage`, or `removed`
- **THEN** it has no cluster ID and its typed MCP model retains its lifecycle and hardware inventory information
