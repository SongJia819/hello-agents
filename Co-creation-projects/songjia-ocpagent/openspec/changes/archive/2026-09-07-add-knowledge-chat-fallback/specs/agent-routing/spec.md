## MODIFIED Requirements

### Requirement: Structured request routing
The system SHALL classify each user query into an agent, action, an ordered list of one or more resources, optional resource name, and optional cluster name before dispatching work. The query capability SHALL use `list` as its only supported action. The routing contract SHALL recognize OCP documentation questions as agent `knowledge`, action `answer`, and resource `documentation`. It SHALL classify ordinary interaction that does not require OCP documentation and does not belong to a registered capability of another Agent as agent `knowledge`, action `chat`, and resource `conversation`.

#### Scenario: Single-resource list query is classified
- **WHEN** a user asks to list nodes
- **THEN** the system returns a route with agent `query`, action `list`, and resources `["node"]`

#### Scenario: Multi-resource list query is classified
- **WHEN** a user asks to list node and pod resources
- **THEN** the system returns a route with agent `query`, action `list`, and resources `["node", "pod"]`

#### Scenario: Documentation question is classified
- **WHEN** a user asks an OCP how-to, architecture, troubleshooting, or explanatory question that requires documentation knowledge
- **THEN** the system returns a route with agent `knowledge`, action `answer`, and resources `["documentation"]`

#### Scenario: Ordinary conversation is classified
- **WHEN** a user sends an ordinary conversational request that does not require OCP documentation and is not handled by another registered Agent capability
- **THEN** the system returns a route with agent `knowledge`, action `chat`, and resources `["conversation"]`

### Requirement: Capability validation before dispatch
The system SHALL validate the routed action and every routed resource against the configured capabilities for the selected agent before dispatching to an agent graph. A supported knowledge documentation route SHALL require the `knowledge` agent's `answer` action and `documentation` resource to be registered. A supported direct-chat route SHALL require the `knowledge` agent's `chat` action and `conversation` resource to be registered.

#### Scenario: Supported list query is dispatched
- **WHEN** a route selects the query agent, action `list`, and one or more enabled resources
- **THEN** the system marks the request as supported and dispatches it to the general list workflow with all requested resources

#### Scenario: Supported knowledge question is dispatched
- **WHEN** a route selects agent `knowledge`, action `answer`, and resource `documentation`
- **THEN** the system marks the request as supported and dispatches it to the Knowledge Agent

#### Scenario: Supported direct chat is dispatched
- **WHEN** a route selects agent `knowledge`, action `chat`, and resource `conversation`
- **THEN** the system marks the request as supported and dispatches it to the Knowledge Agent direct-chat workflow

#### Scenario: Unsupported resource is stopped
- **WHEN** a route selects a resource that is not enabled for its agent
- **THEN** the system stops normal agent dispatch and returns an unsupported-feature response
