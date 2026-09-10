## MODIFIED Requirements

### Requirement: Forward every console request to the Router Agent
The console script SHALL repeatedly accept standard-input requests, ignore blank input, and send each non-empty non-exit request to the configured Router Agent as `{"user_query": <request>}`. It SHALL render user-safe progress and answer chunks from the Router Agent stream as they arrive, then render the completed natural-language answer once. It SHALL not select or invoke query, plan, knowledge, MCP, or other subagents directly, and SHALL NOT display raw event envelopes, route metadata, state JSON, or raw tool results.

#### Scenario: User enters a supported query
- **WHEN** a user enters `list node`
- **THEN** the script displays readable real-time progress, streams answer text as available, and completes with one final natural-language answer

#### Scenario: User enters a knowledge question
- **WHEN** a user enters an OCP documentation question
- **THEN** the script displays readable progress for recall, RRF, rerank, and answer generation before the final answer

#### Scenario: User enters blank input
- **WHEN** a user enters an empty or whitespace-only line
- **THEN** the script does not invoke the Router Agent and continues prompting

### Requirement: Render results and clean up predictably
The console script SHALL preserve answer text's line breaks and spaces and SHALL render a final answer only once, even when answer chunks were displayed during generation. On `exit`, `quit`, EOF, Ctrl+C, or an unhandled request failure, it SHALL stop accepting requests and terminate the fresh MCP child process it started. It SHALL not terminate non-project processes.

#### Scenario: Streamed answer completes
- **WHEN** the Router Agent emits answer chunks followed by its final-result event
- **THEN** the console preserves the streamed text formatting and does not duplicate the completed answer

#### Scenario: Router invocation fails
- **WHEN** the Router Agent stream raises an exception while processing a request
- **THEN** the script displays a clear error and continues the session when safe, without leaking the managed MCP child process

#### Scenario: Automated test supplies fake dependencies
- **WHEN** lifecycle and console request tests run
- **THEN** they can substitute subprocess, readiness, input, and Router Agent stream dependencies without starting a network listener, local LLM, Qdrant, or real MCP server
