## ADDED Requirements

### Requirement: Streamable LLM answers have configurable empty-result retries
The system SHALL collect user-facing LLM answers through an asynchronous stream, assemble its text chunks without whitespace normalization, and validate that the assembled answer contains non-whitespace content. The maximum number of attempts SHALL be configured by `OCP_AGENT_LLM_EMPTY_RESPONSE_RETRY_LIMIT` and default to `3`; the initial attempt SHALL count toward this limit.

#### Scenario: First LLM stream contains text
- **WHEN** an answer-generating LLM stream produces non-whitespace text on its first attempt
- **THEN** the system stores the joined text as the answer and does not make another LLM attempt

#### Scenario: LLM stream is empty before the retry limit
- **WHEN** an answer-generating LLM stream completes with only empty or whitespace text and attempts remain
- **THEN** the system emits a retrying progress event and starts another stream attempt

#### Scenario: All configured attempts are empty
- **WHEN** every configured LLM attempt completes with empty or whitespace-only content
- **THEN** the system returns a clear non-empty fallback answer, logs the exhausted retry condition safely, and does not report an empty final answer

#### Scenario: Retry limit is configured
- **WHEN** `OCP_AGENT_LLM_EMPTY_RESPONSE_RETRY_LIMIT` is set to a positive integer
- **THEN** the system uses that integer as the maximum total number of answer-generation attempts

### Requirement: Streaming failures remain safe
The system SHALL retain existing safe failure behavior when a streamable LLM invocation raises an exception and SHALL not expose prompts, secrets, or raw model metadata in progress or fallback output.

#### Scenario: LLM stream raises an exception
- **WHEN** an answer-generating LLM stream raises an exception
- **THEN** the system logs a request-correlated safe error and returns the caller's clear fallback answer
