## MODIFIED Requirements

### Requirement: Structured request routing
The system SHALL classify each user query into an agent, action, an ordered
list of one or more resources, optional resource name, and optional cluster
name before dispatching work. The query capability SHALL use `list` as its only
supported action. The planning capability SHALL use the canonical agent name
`plan`.

#### Scenario: Single-resource list query is classified
- **WHEN** a user asks to list nodes
- **THEN** the system returns a route with agent `query`, action `list`, and
  resources `["node"]`

#### Scenario: Multi-resource list query is classified
- **WHEN** a user asks to list node and pod resources
- **THEN** the system returns a route with agent `query`, action `list`, and
  resources `["node", "pod"]`

#### Scenario: Skill-backed planning request is classified
- **WHEN** a user asks to add a node
- **THEN** the system returns a route with agent `plan`, action `add`, and
  resources `["node"]`

### Requirement: Capability validation before dispatch
The system SHALL validate the routed action and every routed resource against
the configured capabilities for the selected agent before dispatching to an
agent graph. A planning route SHALL be supported only when its selected
action/resource combination resolves to a registered local planning skill.

#### Scenario: Supported list query is dispatched
- **WHEN** a route selects the query agent, action `list`, and one or more
  enabled resources
- **THEN** the system marks the request as supported and dispatches it to the
  general list workflow with all requested resources

#### Scenario: Supported planning query is dispatched
- **WHEN** a route selects agent `plan`, action `add`, and resource `node`
- **THEN** the system marks the request as supported and dispatches it to the
  Plan Agent

#### Scenario: Unsupported resource is stopped
- **WHEN** a route selects a resource that is not enabled for its agent
- **THEN** the system stops normal agent dispatch and returns an
  unsupported-feature response

#### Scenario: Planning route without a skill is stopped
- **WHEN** a route selects a planning action/resource combination that has no
  registered local skill
- **THEN** the system returns an unsupported-feature response without invoking
  the Plan Agent
