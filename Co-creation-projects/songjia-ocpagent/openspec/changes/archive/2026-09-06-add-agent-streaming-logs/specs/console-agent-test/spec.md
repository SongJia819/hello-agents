## MODIFIED Requirements

### Requirement: Forward every console request to the Router Agent
The console script SHALL repeatedly accept standard-input requests, ignore blank input, and send each non-empty non-exit request to the configured Router Agent as `{"user_query": <request>}`. It SHALL consume and display the Router Agent's normalized execution stream as events arrive. It SHALL not select or invoke query, plan, knowledge, MCP, or other subagents directly.

#### Scenario: User enters a supported query
- **WHEN** a user enters `list node`
- **THEN** the script streams Router and routed Query progress events, displays them during execution, and displays the final routed result

#### Scenario: User enters a knowledge question
- **WHEN** a user enters an OCP documentation question
- **THEN** the script sends it unchanged to the Router Agent, displays the streamed Router-selected Knowledge Agent progress, and displays the final result

#### Scenario: User enters blank input
- **WHEN** a user enters an empty or whitespace-only line
- **THEN** the script does not invoke the Router Agent and continues prompting

### Requirement: Render results and clean up predictably
The console script SHALL render streamed execution events in JSON-safe, human-readable form and, after the terminal final-result event, SHALL render a frontend-facing final result containing available route metadata, supported status, answer, and result data. On `exit`, `quit`, EOF, Ctrl+C, or an unhandled request failure, it SHALL stop accepting requests and terminate the fresh MCP child process it started. It SHALL not terminate non-project processes.

#### Scenario: User exits normally
- **WHEN** a user enters `exit` or `quit`
- **THEN** the script ends the console loop and terminates its managed MCP child process

#### Scenario: Router invocation fails
- **WHEN** the Router Agent stream raises an exception while processing a request
- **THEN** the script displays a clear error and continues the session when safe, without leaking the managed MCP child process

#### Scenario: Terminal event is received
- **WHEN** the Router Agent stream emits its final-result event
- **THEN** the console renders one frontend-facing final result and does not invoke the Router Agent a second time

#### Scenario: Automated test supplies fake dependencies
- **WHEN** lifecycle and console request tests run
- **THEN** they can substitute subprocess, readiness, input, and Router Agent stream dependencies without starting a network listener, local LLM, Qdrant, or real MCP server
