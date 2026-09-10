## Context

The mock MCP server currently creates one cluster, one node, and two pods in tool functions. That keeps the demo self-contained but hides the relationships needed to demonstrate multi-cluster OCP data. The project must remain mock-only and must not connect to a Kubernetes or OpenShift API.

## Goals / Non-Goals

**Goals:**

- Store simulated OCP resources in one local SQLite database file with two seeded clusters and standalone nodes.
- Represent optional cluster-to-node, node-to-network-interface, node-to-storage-device, cluster-to-namespace, and namespace-to-pod relationships with foreign keys.
- Preserve existing MCP tool names and parameters while extending the typed Node response model.
- Make initialization and seed data repeatable across MCP server restarts.

**Non-Goals:**

- Connecting to a real cluster, accepting real credentials, or performing mutating cluster operations.
- Adding new Router resources or a public namespace-listing tool in this change.
- Providing a general database administration interface or production migrations.

## Decisions

Use Python's standard-library `sqlite3` module, avoiding a new dependency. A small MCP-local repository module will resolve a configurable project-local database path, open short-lived connections with `PRAGMA foreign_keys = ON`, create the schema when absent, and seed only when the fixture is empty. This makes the database file durable and restart-safe while keeping the MCP tool layer thin.

The schema will use `clusters(cluster_id, cluster_name, cluster_ip, cluster_port)`, `nodes` with nullable `cluster_id`, `status`, and `idrac_ip`, `node_network_interfaces`, `node_storage_devices`, `namespaces` with a foreign key to `clusters`, and `pods` with foreign keys to both `clusters` and `namespaces`. A database CHECK constraint will require `cluster_id` exactly when `status` is `added`; `new`, `reimage`, and `removed` nodes have no cluster association. `NodeStatus` will be defined in `backend/app/models/` and used by the Node model, so database values are validated at the MCP boundary. Seed data will contain two clusters with added nodes plus standalone nodes in every other lifecycle status, each with network and storage records. SQLite queries will use bound parameters and map rows into typed Pydantic models; no caller-provided value will be interpolated into SQL.

Existing `list_clusters`, `list_nodes(cluster_id)`, and `list_pods(cluster_id)` tools will query the repository. `health` will verify the local SQLite store can be opened and queried. The Query Agent will keep its current node/pod-only public capability, so no Router prompt or agent contract changes are required.

## Risks / Trade-offs

- [A checked-in or runtime database becomes stale] → schema creation and seeding are idempotent, and tests create a temporary database to verify the fixture contract.
- [Foreign-key relationships are silently ignored by SQLite] → enable foreign keys on every connection and test cross-cluster isolation.
- [Node model fields are lost during row mapping] → seed and validate lifecycle, iDRAC, interface, and storage fields through typed Node models.
- [Standalone nodes gain invalid cluster membership] → enforce nullable cluster association and the status/cluster CHECK constraint in SQLite tests.
- [Database errors expose implementation details] → MCP tools return safe failures and do not expose SQL statements or local paths to callers.

## Migration Plan

1. Add the database path configuration and repository schema/seed lifecycle.
2. Replace tool literals with repository queries without changing public tool contracts.
3. Add focused repository and MCP-tool tests, then verify the server can return both simulated clusters.
4. Roll back by removing the local database file and restoring the prior mock-only tool implementation; no external state is affected.

## Open Questions

None. Namespace records are included as relational fixture data but are not exposed through a new public MCP tool in this scoped change.
