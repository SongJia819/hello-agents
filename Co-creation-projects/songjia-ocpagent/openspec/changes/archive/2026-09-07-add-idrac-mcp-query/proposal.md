## Why

The mock cluster fixture currently stores iDRAC IP as a node attribute, but it cannot represent or retrieve a complete standalone iDRAC hardware inventory. A deterministic ten-node iDRAC fixture and MCP queries are needed for demos to inspect server management information without accessing real hardware.

## What Changes

- Add a local SQLite iDRAC inventory table and seed exactly ten simulated iDRAC records.
- Model each inventory record with serial number `DELLSN01` through `DELLSN10`, iDRAC IP `168.0.0.1` through `168.0.0.10`, Red Hat Enterprise Linux 8.0 system information, 20 Gb network interfaces, and ten storage devices whose serial numbers follow `<SN>storage01` through `<SN>storage10`.
- Add mock MCP tools to list all iDRAC inventories and retrieve one inventory by either serial number or iDRAC IP.
- Extend the Query Agent's general `list` action with the `idrac` resource so users can list the entire inventory, one or more selected iDRAC nodes, or iDRAC alongside node and pod resources.
- Preserve the mock-only boundary: no real Dell iDRAC, Kubernetes, OpenShift, or external infrastructure connection is introduced.

## Capabilities

### New Capabilities

- `idrac-inventory-query`: Define the standalone mock iDRAC inventory schema, deterministic fixture, and MCP list/get query contracts.

### Modified Capabilities

- `sqlite-mock-cluster-store`: Extend the local mock SQLite fixture schema to retain the iDRAC inventory data and its hardware children.
- `mock-cluster-mcp`: Extend the mock-only MCP surface with iDRAC inventory list and single-record lookup tools.

## Impact

- Affected code: `backend/app/mcp/cluster_store.py`, `backend/app/mcp/cluster_tools.py`, `backend/app/agents/query/`, router/capability models and prompts, service-layer adapters, new/updated Pydantic inventory models, and targeted tests.
- Affected specifications: `sqlite-mock-cluster-store`, `mock-cluster-mcp`, plus the new `idrac-inventory-query` capability.
- No external dependencies or real infrastructure operations are added.
