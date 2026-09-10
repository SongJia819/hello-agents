## ADDED Requirements

### Requirement: Structured request routing
The system SHALL classify each user query into an agent, action, resource, optional resource name, and optional cluster name before dispatching work.

#### Scenario: Node-list query is classified
- **WHEN** a user asks to list nodes
- **THEN** the system returns a route with agent `query`, action `list`, and resource `node`

### Requirement: Capability validation before dispatch
The system SHALL validate the routed resource against the configured capabilities for the selected agent before dispatching to an agent graph.

#### Scenario: Supported query is dispatched
- **WHEN** a route selects the query agent and the resource is `node`
- **THEN** the system marks the request as supported and dispatches it to the query graph

#### Scenario: Unsupported resource is stopped
- **WHEN** a route selects a resource that is not enabled for its agent
- **THEN** the system stops normal agent dispatch and returns an unsupported-feature response

