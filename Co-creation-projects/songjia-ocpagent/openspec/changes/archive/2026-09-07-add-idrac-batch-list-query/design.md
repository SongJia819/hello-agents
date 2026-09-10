## Context

`list_idrac_nodes()` currently returns all ten local mock records and the Query Agent resolves every selected serial number through individual `get_idrac_node` calls. The existing MCP list interface is the natural batch boundary because a serial-number selection is one database query, not ten unrelated infrastructure operations.

## Goals / Non-Goals

**Goals:**

- Keep no-argument iDRAC listing backward compatible.
- Allow callers to pass one or more serial numbers in one `sn` array.
- Preserve requested serial order, omit unknown serials, and return any iDRAC record at most once.
- Keep Query Agent resource orchestration uniform for node, pod, and iDRAC.

**Non-Goals:**

- Add a new MCP tool or change the existing `get_idrac_node` SN/IP contract.
- Add iDRAC-IP array selection to `list_idrac_nodes`; IP selection continues through `get_idrac_node`.
- Connect to external systems or change inventory seed data.

## Decisions

### Optional serial-number array on the existing list tool

`list_idrac_nodes(sn: list[str] | None = None)` is extended in place. `None` and an empty array both mean list all. A non-empty array selects serials. This preserves existing callers and avoids a redundant batch-only tool.

### Parameterized batch query plus deterministic response ordering

The store uses a parameterized SQLite `IN` query for non-empty input, maps results by serial number, and constructs the response by iterating the requested array. This preserves input order, skips unknown serials, and deduplicates repeated serials. SQL result order is not relied upon.

### Service layer owns iDRAC selector resolution

The service exposes one iDRAC list method that accepts optional ordered selectors. It calls `list_idrac_nodes(sn=...)` once for serial-number-only input. For input containing an iDRAC IP, it uses the existing single-record MCP lookup, then filters `None`, preserves selector order, and deduplicates by serial number. This keeps MCP-specific lookup choices outside Query Agent.

### Query Agent uses the common resource-operation mapping

Query Agent builds one callable operation per selected resource—node and pod receive `cluster_id`; iDRAC receives the ordered selectors—and awaits them together. It does not define iDRAC-specific nested coroutines, classify selectors, or filter iDRAC records. This is preferred over keeping a resource-specific branch in the agent because orchestration stays consistent as resources are added.

## Risks / Trade-offs

- [Large or duplicate caller input] → The local fixture is bounded; deduplication limits output to known records and SQL values remain bound parameters.
- [Mixed serial/IP selectors cannot use one batch request] → Keep the existing single-record path for mixed selectors rather than changing the documented list input contract.
- [Empty-array interpretation differs between callers] → Specify and test that empty equals unfiltered list-all.

## Migration Plan

1. Extend store, MCP tool, and service signatures while retaining no-argument behavior.
2. Centralize selector resolution in the service layer and simplify Query Agent to the common resource-operation mapping.
3. Add store, MCP, service, and Query Agent tests for all, one, multiple, duplicate, and unknown serials.
4. Run targeted tests and strict OpenSpec validation.

## Open Questions

None. The requested `sn` array is treated as an optional serial-number selector; it does not replace iDRAC-IP lookup.
