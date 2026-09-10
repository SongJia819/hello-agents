## ADDED Requirements

### Requirement: Answer a question from one complete Markdown document
The system SHALL provide a standalone script under `backend/app/knowledge/` that accepts exactly a Markdown file path and a non-empty user question as positional arguments. It SHALL read the complete UTF-8 Markdown file and provide its unmodified contents as the only document context to the local LLM. The script SHALL not access Qdrant, embeddings, reranking, MCP, or external cluster infrastructure.

#### Scenario: A valid document and question are supplied
- **WHEN** the script receives `backend/app/knowledge/docs/ocp-4.22/images.md` and a question about creating an image
- **THEN** it invokes the local LLM with the complete contents of `images.md` and the supplied question

#### Scenario: The document path is invalid
- **WHEN** the supplied path does not exist, is not a regular `.md` file, cannot be read, or is not valid UTF-8
- **THEN** the script writes a clear diagnostic to standard error, exits non-zero, and does not invoke the LLM

### Requirement: Use fixed local LLM output and thinking settings
The script SHALL create its local LLM client with `max_tokens=4096` and `think=false`, while reusing the configured local model and base URL.

#### Scenario: The script creates its LLM client
- **WHEN** a valid Markdown document and question reach LLM invocation
- **THEN** the client receives `max_tokens` equal to `4096` and an Ollama-compatible request option that disables thinking

### Requirement: Preserve the LLM answer as the only standard output
The script SHALL write only the LLM response answer to standard output without labels, JSON envelopes, citation normalization, or text reformatting. It SHALL preserve response content such as line breaks and Markdown syntax. LLM invocation failures SHALL be reported on standard error with a non-zero exit code.

#### Scenario: The LLM returns formatted content
- **WHEN** the local LLM returns an answer containing Markdown and multiple lines
- **THEN** standard output contains exactly that answer content and no additional output
