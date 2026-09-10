## ADDED Requirements

### Requirement: General mock resource listing through the service layer
The system SHALL process each `list` request through one general list workflow, request every selected supported resource for the current cluster through the cluster service, and store a resource-keyed mapping of validated models as the tool result.

#### Scenario: One resource is listed for the current cluster
- **WHEN** a `list` request for `node` has resolved a current cluster
- **THEN** the system requests nodes for that cluster and stores them as the `node` entry in `tool_result`

#### Scenario: Multiple resources are listed for the current cluster
- **WHEN** a `list` request for `node` and `pod` has resolved a current cluster
- **THEN** the system requests both resources and stores node and pod results keyed by their resource names in `tool_result`
