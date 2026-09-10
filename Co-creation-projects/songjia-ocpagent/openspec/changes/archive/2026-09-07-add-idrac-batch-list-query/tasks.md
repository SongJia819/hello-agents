## 1. Batch iDRAC MCP listing

- [x] 1.1 Extend the iDRAC store list accessor with an optional serial-number array using parameterized SQLite queries and deterministic order/deduplication.
- [x] 1.2 Extend `list_idrac_nodes` with the optional `sn` array while preserving no-argument and empty-array full-inventory behavior.
- [x] 1.3 Add a typed service-layer serial-array list adapter and use it from Query Agent for serial-only iDRAC selectors; preserve the existing SN/IP single-lookup path for selectors containing an IP.

## 2. Verification

- [x] 2.1 Add store and MCP tests for all, empty, one, multiple ordered, duplicate, and unknown serial-number inputs.
- [x] 2.2 Add Query Agent/service tests proving serial-only selections issue one batch list request and IP/mixed selections retain single-record lookup behavior.
- [x] 2.3 Run targeted automated tests and `openspec validate add-idrac-batch-list-query --strict`; record live MCP/LLM integration availability separately.

## Verification Record

- `PYTHONPATH=backend python -m unittest backend.tests.test_mcp_sqlite_store backend.tests.test_query_agent -v`: passed (17 tests).
- Python compilation passed for the changed store, MCP tool, service, and Query Agent modules.
- `openspec validate add-idrac-batch-list-query --strict`: passed.
- Live MCP/LLM integration was not run because no local MCP server or LLM endpoint was started; mock-only store/tool and Query Agent boundaries are covered by automated tests.

## 3. Service-layer selector orchestration

- [x] 3.1 Move iDRAC selector classification, batch SN lookup, IP lookup fallback, ordering, and deduplication into one service-layer list method.
- [x] 3.2 Simplify Query Agent to use one common resource-operation mapping for node, pod, and iDRAC without an iDRAC-specific nested coroutine.
- [x] 3.3 Add service and Query Agent regression tests for all, serial-only, IP-only, mixed-selector, ordering, and deduplication behavior; run targeted validation.

## Verification Record: Service-layer selector orchestration

- `PYTHONPATH=backend python -m unittest backend.tests.test_mcp_sqlite_store backend.tests.test_query_agent -v`: passed (19 tests).
- Python compilation passed for `ClusterService` and Query Agent nodes.
- `openspec validate add-idrac-batch-list-query --strict`: passed.
- Live MCP/LLM integration was not run because no local MCP server or LLM endpoint was started; automated tests cover the mock MCP, service, and Query Agent boundaries.
