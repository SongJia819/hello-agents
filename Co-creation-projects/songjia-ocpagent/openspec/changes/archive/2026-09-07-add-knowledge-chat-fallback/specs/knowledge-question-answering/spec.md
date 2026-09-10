## MODIFIED Requirements

### Requirement: Generate a grounded knowledge answer
The Knowledge Agent SHALL invoke recall, RRF, reranking, and LLM generation in that order for requests routed as `knowledge`, action `answer`, and resource `documentation`. It SHALL send the original user question and only retained reranked chunks to the LLM, label every context chunk with its stable point ID, and instruct the LLM to ground factual claims in that context. It SHALL write the answer and typed knowledge result into agent state. It SHALL NOT substitute direct chat when supporting OCP documentation is absent or a knowledge dependency fails.

#### Scenario: Documentation evidence supports a question
- **WHEN** recall and reranking retain one or more chunks and the configured LLM succeeds
- **THEN** the agent returns the LLM answer with the retained evidence available in its knowledge result

#### Scenario: No supporting documentation is found
- **WHEN** both recall modes produce no version-matching chunks or reranking retains no chunks
- **THEN** the agent returns a clear no-evidence response and SHALL NOT call the LLM

#### Scenario: A knowledge dependency fails
- **WHEN** Qdrant, embedding, reranking, or LLM invocation fails
- **THEN** the agent returns a clear non-fabricated fallback with a typed failure reason and no successful answer claim
