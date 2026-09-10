## MODIFIED Requirements

### Requirement: Forward every console request to the Router Agent
The console script SHALL repeatedly accept standard-input requests, ignore blank input, and send each non-empty non-exit request to the configured Router Agent as `{"user_query": <request>}`. It SHALL consume the Router Agent's normalized execution stream without displaying internal lifecycle events. It SHALL not select or invoke query, plan, knowledge, MCP, or other subagents directly.

#### Scenario: User enters a supported query
- **WHEN** a user enters `list node`
- **THEN** the script sends the request once to the Router Agent and displays only the terminal natural-language answer

#### Scenario: User enters a knowledge question
- **WHEN** a user enters an OCP documentation question
- **THEN** the script sends it unchanged to the Router Agent and displays only the terminal natural-language answer

#### Scenario: User enters blank input
- **WHEN** a user enters an empty or whitespace-only line
- **THEN** the script does not invoke the Router Agent and continues prompting

### Requirement: Render results and clean up predictably
The console script SHALL render only the terminal `answer` text as a chat response. It SHALL preserve the answer text's line breaks and spaces and SHALL NOT render route metadata, support status, raw tool results, state JSON, or stream events. On `exit`, `quit`, EOF, Ctrl+C, or an unhandled request failure, it SHALL stop accepting requests and terminate the fresh MCP child process it started. It SHALL not terminate non-project processes.

#### Scenario: Terminal answer is received
- **WHEN** the Router Agent stream emits its final-result event with an answer
- **THEN** the console prints that answer once without JSON serialization or whitespace normalization

#### Scenario: Router invocation fails
- **WHEN** the Router Agent stream raises an exception while processing a request
- **THEN** the script displays a clear error and continues the session when safe, without leaking the managed MCP child process

#### Scenario: Automated test supplies fake dependencies
- **WHEN** lifecycle and console request tests run
- **THEN** they can substitute subprocess, readiness, input, and Router Agent stream dependencies without starting a network listener, local LLM, Qdrant, or real MCP server
