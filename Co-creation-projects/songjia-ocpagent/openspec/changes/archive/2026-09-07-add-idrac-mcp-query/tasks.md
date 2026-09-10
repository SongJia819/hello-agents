## 1. iDRAC inventory model and fixture

- [x] 1.1 Add typed iDRAC inventory, system-information, network-interface, and storage-device response models.
- [x] 1.2 Add the three relational iDRAC tables with foreign keys to the SQLite mock-store initialization.
- [x] 1.3 Implement idempotent seed data for exactly ten `DELLSN01`–`DELLSN10` records, their requested iDRAC IPs, Red Hat Enterprise Linux 8.0 system data, 20,000 Mbps network interfaces, and ten correctly numbered disks per record.
- [x] 1.4 Implement parameterized store accessors that return complete typed iDRAC records for all records or one record selected by serial number or iDRAC IP.

## 2. MCP interface

- [x] 2.1 Register `list_idrac_nodes` to return all local mock iDRAC inventory records.
- [x] 2.2 Register `get_idrac_node(sn, idrac_ip)` with exactly-one-selector validation, complete matching responses, and an explicit no-match result.

## 3. Verification

- [x] 3.1 Add isolated tests for first-time and repeat initialization, fixture cardinality, prescribed serial/IP/OS/NIC/disk values, and complete typed mapping.
- [x] 3.2 Add MCP-tool tests for full listing, serial lookup, iDRAC-IP lookup, unknown lookup, and missing/ambiguous selector validation.
- [x] 3.3 Run targeted automated tests and `openspec validate add-idrac-mcp-query --strict`; record any unavailable live MCP verification separately.

## Verification Record

- `PYTHONPATH=backend python -m unittest backend.tests.test_mcp_sqlite_store -v`: passed (7 tests).
- `python -m py_compile backend/app/models/idrac.py backend/app/mcp/cluster_store.py backend/app/mcp/cluster_tools.py`: passed.
- `openspec validate add-idrac-mcp-query --strict`: passed.
- Live network MCP verification was not run: no `app.mcp.server` process was active, and sandbox restrictions prevented socket-listener inspection. The MCP function registrations are covered by isolated tool tests using a temporary SQLite store.

## 4. Query Agent iDRAC listing

- [x] 4.1 Extend Router structured output, prompt examples, capability configuration, and state to recognize `idrac` and ordered iDRAC SN/IP selectors.
- [x] 4.2 Add the service-layer iDRAC list and selected-record lookup adapters with typed result handling.
- [x] 4.3 Extend the Query Agent general `list` orchestration to list all iDRAC nodes when unfiltered, resolve one or more selected iDRAC nodes in order without duplicates, and compose `idrac` with node and pod results.
- [x] 4.4 Add Router and Query Agent tests for all-iDRAC, one-iDRAC, multiple selected iDRAC, mixed-resource list requests, unsupported resources, and selector ordering/deduplication.
- [x] 4.5 Run the affected automated tests and `openspec validate add-idrac-mcp-query --strict`; record live MCP/LLM integration availability separately.

## Query Agent Verification Record

- `PYTHONPATH=backend python -m unittest backend.tests.test_query_agent backend.tests.test_mcp_sqlite_store -v`: passed (15 tests).
- Python compilation passed for changed Router, state, capability, MCP client, service, and Query Agent modules.
- `openspec validate add-idrac-mcp-query --strict`: passed.
- Live MCP/LLM integration was not run because no local MCP server or LLM endpoint was started for this verification; mock-only store/tool and Router/Query Agent boundaries are covered by automated tests.
