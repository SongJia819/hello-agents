## MODIFIED Requirements

### Requirement: Structured request routing
The system SHALL classify each user query into an agent, action, an ordered list of one or more resources, optional resource name, and optional cluster name before dispatching work. The query capability SHALL use `list` as its only supported action.

#### Scenario: Single-resource list query is classified
- **WHEN** a user asks to list nodes
- **THEN** the system returns a route with agent `query`, action `list`, and resources `["node"]`

#### Scenario: Multi-resource list query is classified
- **WHEN** a user asks to list node and pod resources
- **THEN** the system returns a route with agent `query`, action `list`, and resources `["node", "pod"]`

### Requirement: Capability validation before dispatch
The system SHALL validate the `list` action and every routed resource against the configured capabilities for the selected agent before dispatching to an agent graph.

#### Scenario: Supported list query is dispatched
- **WHEN** a route selects the query agent, action `list`, and one or more enabled resources
- **THEN** the system marks the request as supported and dispatches it to the general list workflow with all requested resources

#### Scenario: Unsupported resource is stopped
- **WHEN** a route selects a resource that is not enabled for its agent
- **THEN** the system stops normal agent dispatch and returns an unsupported-feature response
