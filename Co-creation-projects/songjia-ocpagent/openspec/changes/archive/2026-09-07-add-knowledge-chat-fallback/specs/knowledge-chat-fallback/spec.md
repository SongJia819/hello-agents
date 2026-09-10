## ADDED Requirements

### Requirement: Provide direct LLM chat for eligible ordinary interaction
The Knowledge Agent SHALL provide a direct-chat capability for requests routed as `knowledge`, action `chat`, and resource `conversation`. It SHALL send the user's current message directly to the configured LLM without document retrieval, RRF, reranking, document chunks, or citations, and SHALL return the LLM answer as the user-facing answer.

#### Scenario: Ordinary conversation receives a direct answer
- **WHEN** the Knowledge Agent receives an eligible `knowledge/chat/conversation` route
- **THEN** it invokes the configured LLM with the current user message and returns its direct conversational response

#### Scenario: Direct chat does not produce documentation evidence
- **WHEN** the Knowledge Agent completes an eligible direct-chat request
- **THEN** it does not create document citations or report retrieved-document diagnostics as support for that response

### Requirement: Fail direct chat transparently
The direct-chat capability SHALL use the configured bounded LLM retry behavior and SHALL return a clear unavailable-response fallback when the LLM cannot produce a response. It MUST NOT substitute a documentation-grounded or fabricated success response.

#### Scenario: Direct chat LLM invocation fails
- **WHEN** all configured direct-chat LLM attempts fail or return no usable content
- **THEN** the Knowledge Agent returns a clear direct-chat unavailable-response fallback
