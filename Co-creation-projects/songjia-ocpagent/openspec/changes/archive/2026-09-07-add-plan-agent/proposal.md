## Why

The router can classify mutating requests as planning work, but the backend has
no Plan Agent, skill-aware task decomposition, or durable state contract for a
generated plan. Users therefore cannot inspect an executable, dependency-aware
plan before any future mock operation is handed to an execution workflow.

## What Changes

- Add a Plan Agent that resolves an approved local skill from the routed action
  and resource, reads its input/output/procedure contract, and produces a
  structured executable plan without performing the operation.
- Add structured plan models and an `AgentState.plan` result that preserves the
  plan inputs, ordered steps, each step's outputs, and inter-step dependencies.
- Register supported planning capabilities and connect a supported `plan` route
  from the router graph to the Plan Agent.
- Normalize the router's planning target name to `plan` and reject planning
  routes that have no configured skill-backed capability.
- Add isolated tests for routing, skill resolution, plan structure, and
  unsupported planning requests.

## Capabilities

### New Capabilities
- `skill-aware-plan-generation`: Generate a non-executing, structured plan
  from a routed request and an approved local skill contract.

### Modified Capabilities
- `agent-routing`: Dispatch supported skill-backed planning routes to the Plan
  Agent and reject unsupported planning routes before dispatch.

## Impact

- Affects router prompts, routing capability validation, the router graph and
  container wiring under `backend/app/`.
- Adds plan-agent modules, typed plan/state models, and tests under
  `backend/tests/`.
- Reads only repository-local skill definitions under `backend/app/skills/`;
  it does not invoke external infrastructure, tools, or real OpenShift APIs.
