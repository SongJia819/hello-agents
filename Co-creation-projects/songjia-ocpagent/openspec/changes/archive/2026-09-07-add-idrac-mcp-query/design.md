## Context

The SQLite mock store currently gives each generic node an iDRAC IP, but it has no independent iDRAC entity, service-tag lookup, operating-system data, or deterministic hardware inventory for ten management controllers. This demo must remain local and mock-only.

## Goals / Non-Goals

**Goals:**

- Persist and return a complete, deterministic iDRAC inventory for ten simulated servers.
- Make full-inventory and single-inventory lookup available through the MCP server.
- Make iDRAC inventory available through the Query Agent's general `list` workflow without changing existing node and pod result behavior.

**Non-Goals:**

- Connecting to Dell iDRAC/Redfish, Kubernetes, OpenShift, or a real database service.
- Adding create, update, delete, credential, power-management, or firmware-operation tools.

## Decisions

### Use dedicated relational iDRAC inventory tables

Add an `idrac_nodes` parent table with system metadata, an `idrac_network_interfaces` child table, and an `idrac_storage_devices` child table. Child tables preserve one-to-many NIC and disk data without serializing hardware records into JSON. This is preferred over extending `nodes`, because iDRAC inventory is queried by iDRAC IP/service tag independently of cluster membership and must always contain ten records.

### Seed an idempotent, prescribed fixture

First-time initialization seeds exactly ten iDRAC nodes: service tags `DELLSN01`–`DELLSN10`, management addresses `168.0.0.1`–`168.0.0.10`, system `Red Hat Enterprise Linux 8.0`, 20,000 Mbps network interfaces, and ten disks per node with serials `<SN>storage01`–`<SN>storage10`. Existing initialized databases retain their data; initialization must also ensure the new tables and fixture exist without duplicate rows.

### Expose explicit MCP inventory tools

Use `list_idrac_nodes()` for all records and `get_idrac_node(sn=None, idrac_ip=None)` for a single record. Exactly one selector is required; supplying neither or both is an input validation error. A valid but unmatched selector returns no inventory record. The explicit MCP tools remain the inventory boundary, while the Query Agent becomes the user-facing caller for general list requests.

### Add iDRAC as a general Query Agent list resource

Add `idrac` to the Query Agent's supported `list` resources and to Router structured output/prompt vocabulary. A request with only `idrac` returns the iDRAC result under `tool_result["idrac"]`; a mixed request such as `node`, `pod`, and `idrac` retains the existing resource-keyed result shape and executes independent resource providers concurrently.

For iDRAC only, Router output carries an ordered optional selector list. Each selector is either an SN or iDRAC IP. With no selectors, the service calls `list_idrac_nodes`; with one or more selectors, it resolves each via `get_idrac_node` and returns matching records in selector order. This is preferred over making iDRAC cluster-scoped or filtering client-side because it preserves the MCP lookup contract and avoids returning unrelated management records.

### Return typed, complete inventory records

Introduce typed models for the parent system data, network interfaces, and storage devices. Store queries use parameterized SQLite statements and a shared row mapper, ensuring that list and get return the same complete shape.

## Risks / Trade-offs

- [An existing SQLite file predates the new schema] → Initialization uses `CREATE TABLE IF NOT EXISTS` and an idempotent seed check for the iDRAC fixture.
- [The specified `168.0.0.0/24` range is unusual and differs from current fixture addresses] → Preserve the requested literal addresses exactly; do not infer a different private range.
- [MCP callers provide ambiguous lookup arguments] → Validate exclusivity and cover neither/both-selector cases in tests.
- [A router emits an unsupported or duplicate iDRAC selector] → Validate the `idrac` resource and selector collection at the Router/Query boundary; preserve selector order and return each matching record at most once.
- [Ten records each with ten disks increase response size] → The bounded fixture (100 disks total) is acceptable for a local demo and the list tool intentionally returns complete inventory.

## Migration Plan

1. Add models, tables, idempotent seed data, and store accessors.
2. Register the MCP tools and add isolated store/tool tests.
3. Extend Router, capability configuration, state, service adapter, and Query Agent list orchestration for iDRAC resources and ordered selectors.
4. Add Query Agent/Router tests, then run targeted automated tests and strict OpenSpec validation.
5. Existing local databases are upgraded in place when next initialized; rollback is code rollback, while the added tables are harmless unused local mock data.

## Open Questions

None. The requested IP range, serial formats, 20G NIC value, ten disks per server, and default OS are treated as fixed fixture requirements.
