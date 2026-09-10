## MODIFIED Requirements

### Requirement: General mock resource listing through the service layer
The system SHALL process each `list` request through one general list workflow, request every selected supported resource for the current cluster through the cluster service, and store a resource-keyed mapping of validated models as the tool result. After all selected MCP resource results are available, it SHALL send the original user query and the complete resource-keyed tool result to the configured LLM and store its grounded natural-language response in `answer`.

#### Scenario: One resource is listed for the current cluster
- **WHEN** a `list` request for `node` has resolved a current cluster
- **THEN** the system requests nodes for that cluster, stores them as the `node` entry in `tool_result`, and produces an LLM answer based on the original question and node result

#### Scenario: Multiple resources are listed for the current cluster
- **WHEN** a `list` request for `node` and `pod` has resolved a current cluster
- **THEN** the system requests both resources, stores node and pod results keyed by their resource names in `tool_result`, and produces one LLM answer using both result sets

#### Scenario: Query answer LLM is unavailable
- **WHEN** resource listing succeeds but LLM answer generation fails
- **THEN** the system retains `tool_result`, returns a clear answer-generation failure message in `answer`, and does not claim a generated resource summary succeeded
