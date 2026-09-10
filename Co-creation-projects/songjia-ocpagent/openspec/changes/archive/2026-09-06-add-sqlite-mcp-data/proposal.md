## Why

The MCP server currently constructs mock cluster, node, and pod responses in Python code, so relationships between simulated OCP resources cannot be queried or evolved consistently. A local SQLite-backed fixture will keep the demo mock-only while providing durable, relational sample data.

## What Changes

- Add a project-local SQLite database with relational `clusters`, `nodes`, `node_network_interfaces`, `node_storage_devices`, `namespaces`, and `pods` tables and two seeded simulated OCP clusters.
- Model standalone and cluster-added nodes, including typed lifecycle state, optional Cluster association, iDRAC IP, multiple network-interface records, and storage-device records.
- Add a small MCP-local data access layer that creates and seeds the database idempotently, enables foreign keys, and maps SQL rows to existing response models.
- Replace embedded Python fixtures behind existing `list_clusters`, `list_nodes`, and `list_pods` MCP tools with parameterized SQLite queries; retain their public input/output contracts and the `health` tool.
- Keep all MCP data strictly local and simulated; do not add a Kubernetes/OpenShift connection.
- Add database and MCP-tool tests that verify node lifecycle states, standalone versus cluster-associated nodes, per-cluster isolation, relationships, and repeatable initialization.

## Capabilities

### New Capabilities

- `sqlite-mock-cluster-store`: Local relational fixture schema, seed lifecycle, and query behavior for simulated OCP resource data.

### Modified Capabilities

- `mock-cluster-mcp`: Existing MCP cluster, node, and pod listings read their mock-only responses from the local SQLite fixture instead of in-memory literals.

## Impact

- Affected areas: Node models, MCP server tools, new local database/service module and SQLite file, seed data, and MCP-focused tests.
- Public MCP tool names remain unchanged; node response models gain lifecycle, hardware-management, network-interface, and storage-device fields.
