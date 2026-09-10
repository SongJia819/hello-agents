## 1. Local SQLite mock data store

- [x] 1.1 Define typed Node lifecycle, iDRAC, network-interface, and storage-device models under `backend/app/models/`.
- [x] 1.2 Add MCP SQLite path configuration and a repository module that creates the relational schema, status/cluster constraint, and foreign-key enforcement.
- [x] 1.3 Seed exactly two simulated clusters with added nodes plus standalone `new`, `reimage`, and `removed` nodes, related namespaces, pods, interfaces, and storage devices idempotently.
- [x] 1.4 Implement parameterized repository queries that map cluster, node, and pod rows to the typed MCP models.

## 2. MCP integration

- [x] 2.1 Replace `list_clusters`, `list_nodes`, and `list_pods` in-memory literals with SQLite repository queries while preserving their public contracts.
- [x] 2.2 Make the MCP `health` tool verify availability of the local SQLite store without exposing implementation details.

## 3. Verification

- [x] 3.1 Add focused tests for typed Node states, schema initialization, status/cluster constraints, idempotent two-cluster seeding, foreign-key relationships, unknown-cluster results, and model mapping.
- [x] 3.2 Add MCP tool tests confirming SQLite-backed cluster, node, pod, and health responses.
- [x] 3.3 Run focused tests, static compilation, and `openspec validate add-sqlite-mcp-data --strict`.
