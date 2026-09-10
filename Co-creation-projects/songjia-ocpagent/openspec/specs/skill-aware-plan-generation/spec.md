## Purpose

Define mock-only, skill-aware structured plan generation.

## Requirements

### Requirement: Generate a structured plan from an approved local skill
The system SHALL generate a typed, non-executing plan when it receives a supported planning route. It SHALL resolve the route's action and every target resource through the configured planning capability registry, read only the registered repository-local skill contract, and return a plan whose skill, action, and resources match that route.

#### Scenario: Supported node-add route creates a node-add plan
- **WHEN** the Plan Agent receives a supported `plan` route with action `add` and resource `node`
- **THEN** it uses the registered `node-add` local skill and returns a typed plan without invoking an MCP tool or changing mock cluster state

#### Scenario: Unregistered planning capability is not planned
- **WHEN** the Plan Agent receives an action or resource without a registered planning skill
- **THEN** it returns an unsupported planning result and does not read an arbitrary skill path

### Requirement: Plan records step interfaces and dependencies
The generated plan SHALL be stored as `plan` in the agent state. It SHALL contain the selected skill, routed action and resources, required request input names, final output names, and ordered steps. Every step SHALL contain a stable id, description, input names, output names, and dependency step ids; every dependency SHALL identify an earlier step and the complete dependency graph SHALL be acyclic.

#### Scenario: Node-add procedure has explicit data flow
- **WHEN** a valid node-add plan is generated
- **THEN** its steps represent the skill procedure in order and explicitly declare the inputs, outputs, and dependencies required to execute them

#### Scenario: Invalid dependency graph is rejected
- **WHEN** generated plan steps reference a nonexistent, later, or cyclic dependency
- **THEN** the system does not store that plan as a successful result

### Requirement: Planning keeps sensitive values write-only
The Plan Agent SHALL preserve required input field names and validation requirements without placing credential values, certificate contents, or other sensitive caller values in the generated plan, graph messages, or logs.

#### Scenario: Node-add credentials are represented safely
- **WHEN** a node-add request includes a password
- **THEN** the plan identifies the password as a required write-only input and does not include its value
