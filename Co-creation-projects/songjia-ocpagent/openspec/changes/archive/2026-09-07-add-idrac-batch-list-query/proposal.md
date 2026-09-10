## Why

The iDRAC MCP list tool currently returns only the full inventory, so callers that know several server serial numbers must make separate single-record requests. A serial-number array on the list tool makes selective multi-server lookup one local MCP call while preserving full-list behavior.

## What Changes

- Extend `list_idrac_nodes` with an optional `sn` array parameter.
- Return all mock iDRAC records when `sn` is omitted or empty; return only matching serial-number records when it is supplied.
- Preserve caller serial-number order, omit unknown serial numbers, and avoid duplicate returned iDRAC records for duplicate serials.
- Move iDRAC selector filtering, batch SN lookup, IP lookup fallback, ordering, and deduplication into the service layer so Query Agent uses the same resource-operation pattern as node and pod queries.

## Capabilities

### New Capabilities

None.

### Modified Capabilities

- `idrac-inventory-query`: Extend the iDRAC MCP list contract with optional serial-number batch selection and define the Query Agent's use of it.
- `mock-cluster-mcp`: Extend the mock-only iDRAC list tool input contract.

## Impact

- Affected code: iDRAC store lookup, MCP tool signature, MCP/service adapters, Query Agent resource-operation mapping, and tests.
- Existing `list_idrac_nodes()` calls without arguments remain compatible and return all ten records.
- No real iDRAC, Redfish, Kubernetes, OpenShift, or external infrastructure connection is introduced.
