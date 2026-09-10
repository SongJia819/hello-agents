## ADDED Requirements

### Requirement: Start the mock MCP server for a console agent session
The system SHALL provide an executable local console test script that starts a fresh project mock MCP server as a managed child process before initializing the configured Agent container. Before starting it, the script SHALL detect any local process launched as `app.mcp.server`, stop it, and wait for it to exit. It SHALL wait for bounded MCP readiness at the existing local endpoint and SHALL report startup failure without accepting a request when readiness is not reached.

#### Scenario: MCP server becomes ready
- **WHEN** the console test script is started and port `8001` is available
- **THEN** it starts the local mock MCP server, initializes the Agent container, and displays a prompt for user requests

#### Scenario: Prior project MCP server is running
- **WHEN** a local `app.mcp.server` process is already running when the console test script starts
- **THEN** the script stops and waits for the prior process before starting a fresh MCP server instance and initializing the Agent container

#### Scenario: Unknown process owns the MCP port
- **WHEN** port `8001` remains occupied after prior `app.mcp.server` instances have stopped
- **THEN** the script reports that the port is occupied and does not terminate the unknown process or start the Agent container

#### Scenario: MCP server cannot start
- **WHEN** the child MCP server exits or does not become ready before the configured timeout
- **THEN** the script reports the startup failure, cleans up its child process, and does not initialize a console request session

### Requirement: Forward every console request to the Router Agent
The console script SHALL repeatedly accept standard-input requests, ignore blank input, and send each non-empty non-exit request to the configured Router Agent as `{"user_query": <request>}`. It SHALL not select or invoke query, plan, knowledge, MCP, or other subagents directly.

#### Scenario: User enters a supported query
- **WHEN** a user enters `list node`
- **THEN** the script invokes the Router Agent once with that exact request and displays the final routed result

#### Scenario: User enters a knowledge question
- **WHEN** a user enters an OCP documentation question
- **THEN** the script sends it unchanged to the Router Agent and displays the final result returned by the Router-selected Knowledge Agent

#### Scenario: User enters blank input
- **WHEN** a user enters an empty or whitespace-only line
- **THEN** the script does not invoke the Router Agent and continues prompting

### Requirement: Render results and clean up predictably
The console script SHALL render completed Router Agent state in JSON-safe, human-readable output. On `exit`, `quit`, EOF, Ctrl+C, or an unhandled request failure, it SHALL stop accepting requests and terminate the fresh MCP child process it started. It SHALL not terminate non-project processes.

#### Scenario: User exits normally
- **WHEN** a user enters `exit` or `quit`
- **THEN** the script ends the console loop and terminates its managed MCP child process

#### Scenario: Router invocation fails
- **WHEN** the Router Agent raises an exception while processing a request
- **THEN** the script displays a clear error and continues the session when safe, without leaking the managed MCP child process

#### Scenario: Automated test supplies fake dependencies
- **WHEN** lifecycle and console request tests run
- **THEN** they can substitute subprocess, readiness, input, and Router Agent dependencies without starting a network listener, local LLM, Qdrant, or real MCP server
