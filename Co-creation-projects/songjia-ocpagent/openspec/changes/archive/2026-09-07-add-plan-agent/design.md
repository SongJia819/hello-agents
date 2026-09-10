## Context

The implemented router graph performs structured LLM classification, capability
validation, and dispatches only the query agent. `AgentState` has a legacy
`plans: List[str]` field but no typed completed-plan value. The repository has
one local skill, `backend/app/skills/node-add/SKILL.md`, that documents a
mock-only node-add procedure, required inputs, ordered steps, outputs, and
failure behavior.

The new Plan Agent must turn a supported routed request into an inspectable plan
before any execution exists. The project remains a demo: skills and their plans
must never contact a cluster or perform an infrastructure mutation.

## Goals / Non-Goals

**Goals:**
- Route configured planning requests to a Plan Agent.
- Resolve the corresponding approved repository-local skill and derive a
  typed, execution-ready plan from its contract.
- Preserve request inputs, outputs, dependency relationships, and the complete
  plan result in LangGraph state.
- Provide deterministic tests without a live LLM, MCP server, or OpenShift
  cluster.

**Non-Goals:**
- Execute a plan, modify mock cluster state, or implement an execution agent.
- Load arbitrary paths, remote skills, or user-provided skill documents.
- Infer secrets or synthesize missing operational values.
- Change the public chat-response schema in this change.

## Decisions

### Define a typed, single completed plan in state

Add Pydantic models for `Plan`, `PlanStep`, and any typed input/output and
dependency references needed by their contract. `PlanStep` SHALL include a
stable id, skill name, description, declared input names, declared output
names, and `depends_on` step ids. `Plan` SHALL include the routed action and
resources, request input contract, final outputs, and an ordered step list.

`AgentState` will gain `plan: Plan | None`, while retaining `plans` during this
change for compatibility with any caller that supplies it. The Plan Agent
returns `plan` in its node update; it does not place serialized plans in
messages or `tool_result`. A structured object prevents the fragile free-text
plan alternative and makes later execution validation possible.

### Use a controlled skill registry keyed by planning capability

Extend `CAPABILITIES[AgentType.PLAN]` to map supported action/resource pairs to
a named skill, initially `add` + `node` to `node-add`. Plan Agent code resolves
only registry entries and maps each entry to an expected file beneath
`backend/app/skills/`. It reads the selected `SKILL.md` as planning context and
never accepts a path from user input or router output. Missing, malformed, or
unregistered skills produce an unsupported planning response rather than a
plan.

This deliberately avoids directory scanning as the authorization mechanism:
discovering every file would allow an unreviewed document to become executable
planning input.

### Preserve skill contracts in a dependency-aware plan

The Plan Agent invokes the configured structured-output LLM with the routed
request and selected skill contract. The response schema constrains the LLM to
the known skill name, supplied action/resources, named contract inputs/outputs,
and valid dependency ids. The node validates that dependency ids reference
earlier steps, that the graph is acyclic, and that no sensitive input values are
copied into plan output or messages.

The first supported skill, `node-add`, produces the ordered procedure described
by its skill document, with each step declaring consumed and produced values.
Missing required values stay as required input placeholders; the planner does
not invent credentials or artifact paths. Generating unrestricted prose was
rejected because it cannot reliably establish execution order or data flow.

### Dispatch the normalized `plan` agent target

Update the routing prompt/model examples to classify planning requests as
`plan`, matching `AgentType.PLAN`, rather than `planner`. Router capability
validation remains the gate for both query and plan routes. `RouterGraph`
receives a Plan Agent dependency, registers a `plan` node, and adds it to its
conditional dispatch map. The container constructs and injects the Plan Agent
alongside the Query Agent.

Aliasing `planner` in the graph was rejected: one canonical state value avoids
an unvalidated second routing target and keeps capability keys, state, tests,
and graph-node names aligned.

## Risks / Trade-offs

- [Skill instructions are incomplete or inconsistent] → Treat the skill as a
  contract source, validate structured output against the typed plan schema,
  and return a clear planning failure rather than an executable-looking plan.
- [An LLM introduces an invalid dependency] → Validate references, ordering,
  and cycles after structured-output parsing; reject invalid plans.
- [Sensitive node-add fields leak into state or messages] → Keep values as
  write-only caller inputs; expose only field names/requirements and redact
  known sensitive fields in planner logs and returned plan metadata.
- [Future skills have different document layouts] → Keep registry metadata
  explicit and add parser/adapter support per approved skill rather than
  assuming all Markdown is machine-readable.

## Migration Plan

1. Add typed planning models, state field, local skill resolver, and Plan Agent
   graph/node implementation.
2. Register `node-add` as the initial supported mock-only planning capability
   and normalize router classification to `plan`.
3. Inject the Plan Agent into the router graph and add isolated tests for plan
   routing and plan validation.
4. Validate the OpenSpec change and automated tests. Roll back by removing the
   plan route and registration; query routing remains independent.

## Open Questions

- The initial plan result is internal graph state. A later API change can decide
  which redacted plan fields to expose in `POST /v1/chat`.
