## Context

The current router and query graph expose node and pod retrieval as separate resource-specific paths. The revised contract has one query action, `list`, which selects one or more supported resources. The general list workflow resolves the first mock cluster once, gathers data for every selected resource, and returns a consistent resource-keyed result.

The project is a demo. Every new pod response must be generated from local mock data and must not contact Kubernetes, OpenShift, or other external infrastructure.

## Goals / Non-Goals

**Goals:**

- Route `list` requests for one or more supported resources to the query agent after validating every requested resource.
- Resolve the current mock cluster once, then fetch selected node and/or pod data as one list operation.
- Return a resource-keyed result for both single- and multi-resource list requests.
- Consolidate deterministic general-list coverage in `backend/tests/test_query_agent.py`.

**Non-Goals:**

- Support actions other than `list`, such as create, delete, logs, namespace filtering, or pod detail queries.
- Add resources beyond node and pod, or change cluster-selection behavior.
- Access real cluster APIs, credentials, or infrastructure.

## Decisions

### Represent every list selection as an ordered resource list

The routed state will carry an ordered `resources` list for every `list` request, including a single-resource request such as `["node"]`. Router capability validation must confirm every requested resource is enabled for the query agent before dispatch. Inferring resources from raw user text in the query graph was rejected because routing, not execution, owns request interpretation.

### Use one general list workflow

After resolving the first mock cluster, the query graph will execute one general list workflow for all selected resources. It will invoke the required resource providers concurrently where independent and return a result mapping keyed by resource, for example `{ "node": [...], "pod": [...] }`; a single-resource request returns the same shape with one key. Separate node-list and pod-list workflow branches were rejected because the public capability is one `list` action.

### Keep resource-specific providers behind the general list capability

The MCP client will continue to validate mock node and pod responses with their existing domain models. The general list workflow may delegate to resource-specific provider calls such as `list_nodes(cluster_id)` and `list_pods(cluster_id)` internally; those calls are not separate user-facing query capabilities. This avoids introducing duplicate data models while keeping mock data stable and cluster-associated.

### Keep general list support capability-driven

`node` and `pod` remain enabled resources for the query agent. The router classifies requests through its structured LLM output, accepts only the `list` action for this capability, validates all requested resources before dispatch, and preserves the unsupported response if any requested resource is not enabled by the capability map.

### Keep mock data local to the MCP provider

The `list_pods` tool remains next to the current mock cluster tools and returns deterministic, realistic pod summaries without calling a Kubernetes/OpenShift API. Tests will use fake service seams rather than external endpoints.

## Risks / Trade-offs

- [LLM classification returns an incomplete resource list] → Require the structured router output to preserve every recognized requested resource and validate the list before dispatch.
- [Concurrent results have an unstable shape] → Return a resource-keyed mapping for every general-list response, including a single-resource response.
- [Mock data becomes mistaken for live cluster state] → Keep mock-only wording in the MCP contract and use clearly synthetic identifiers/IPs.
- [The existing `Pod` model is too small for future UI needs] → Limit this change to name and IP; evolve the model in a separate capability change when additional fields are needed.

## Migration Plan

1. Normalize router state/output and capability validation around the `list` action and resource lists.
2. Replace resource-specific query branches with the general list workflow and concurrent node/pod provider calls.
3. Consolidate query-agent tests around single- and multi-resource list cases.
4. Run the relevant backend tests with only mock dependencies.
5. Roll back by restoring resource-specific workflow branches and their existing result shapes.

## Open Questions

- None for the initial cluster-wide, mock-only pod list operation.
