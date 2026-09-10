## 1. Plan Contracts And Skill Resolution

- [x] 1.1 Add typed plan and plan-step models with action, resources, required
  input names, output names, stable step ids, and dependency ids.
- [x] 1.2 Add an optional structured `plan` result to `AgentState`, retaining
  the legacy `plans` field for compatibility.
- [x] 1.3 Implement a registry-backed resolver for approved local planning
  skills, initially mapping `add` + `node` to `node-add`, with safe missing or
  malformed-skill handling.
- [x] 1.4 Implement validation for skill-matched plans, including step ordering,
  input/output declarations, dependency references, cycle rejection, and
  sensitive-value redaction.

## 2. Plan Agent

- [x] 2.1 Add Plan Agent graph/node modules that read the selected local skill
  contract and use typed LLM output to generate a non-executing plan.
- [x] 2.2 Convert valid plan output into the typed `AgentState.plan` result
  without invoking MCP tools or changing mock cluster state.
- [x] 2.3 Return a clear unsupported or invalid-plan result when no registered
  skill exists or plan validation fails.

## 3. Router Integration

- [x] 3.1 Normalize planning classifications and examples to the canonical
  `plan` agent target in the router prompt/model boundary.
- [x] 3.2 Extend planning capability validation to require a registered local
  skill for every routed planning action/resource combination.
- [x] 3.3 Register the Plan Agent in the router graph, dispatch supported
  `plan` routes to it, and inject it through the application container.

## 4. Test And Verify

- [x] 4.1 Add unit tests for planning capability checks and router dispatch to
  the Plan Agent without live LLM, MCP, or cluster dependencies.
- [x] 4.2 Add Plan Agent tests using a fake structured LLM and fixture skill
  contract to verify node-add step inputs, outputs, dependencies, state result,
  unsupported skills, invalid dependency graphs, and secret redaction.
- [x] 4.3 Run the relevant backend test suite and `openspec validate
  add-plan-agent --strict`; record any unavailable live-service verification
  separately from automated results.
