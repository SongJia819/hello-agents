## 1. General List Contract

- [x] 1.1 Normalize routed query state and structured routing output around the single `list` action and an ordered resource list.
- [x] 1.2 Validate the `list` action and every requested resource against the query-agent capability map.
- [x] 1.3 Define a stable resource-keyed `tool_result` contract for both one- and multi-resource list responses.

## 2. General List Workflow

- [x] 2.1 Replace resource-specific query branches with one general list workflow after mock-cluster resolution.
- [x] 2.2 Delegate each selected resource to its mock node or pod provider and aggregate the results by resource name.
- [x] 2.3 Run independent node and pod provider calls concurrently for multi-resource list requests.
- [x] 2.4 Preserve the unsupported-feature response for actions other than `list` and resources outside configured capabilities.

## 3. Verification

- [x] 3.1 Add assertion-based tests for a single-resource `list` request for node and for pod.
- [x] 3.2 Add query-agent tests that verify a multi-resource `list` request returns node and pod results keyed by resource name.
- [x] 3.3 Add router tests for supported `list` requests and unsupported actions or resources.
- [x] 3.4 Run the relevant backend tests with only mock dependencies and record the results.

Verification result (2026-08-15): `python -m unittest discover -v` passed (7 tests), including 4 general-list assertion tests.

## 4. Manual Integration Verification

- [x] 4.1 Update the manual LLM/MCP query-agent test to cover `list node`, `list pod`, and `list node and pod`.
- [ ] 4.2 Run the manual query-agent integration test against the configured LLM and mock MCP server, then record the result.

Verification pending: the manual query-agent integration test requires the configured local LLM and mock MCP server.
