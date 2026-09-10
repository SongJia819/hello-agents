## Purpose

Configure Ollama-compatible runtime LLM think mode at deployment time and provide a safe local console launcher.

## Requirements

### Requirement: Configure LLM think mode at deployment time
The system SHALL configure all runtime Ollama-compatible LLM clients from `OCP_AGENT_LLM_THINK`. The setting SHALL be a boolean, SHALL default to enabled when unset, and SHALL be passed as the provider `think` request option for Router, Query, Plan, and Knowledge LLM calls.

#### Scenario: No think-mode override is provided
- **WHEN** the application starts without `OCP_AGENT_LLM_THINK`
- **THEN** every runtime LLM client requests think mode enabled

#### Scenario: Think mode is disabled
- **WHEN** `OCP_AGENT_LLM_THINK=false`
- **THEN** every runtime LLM client requests think mode disabled

#### Scenario: Think mode setting is invalid
- **WHEN** `OCP_AGENT_LLM_THINK` is not a supported boolean value
- **THEN** configuration validation fails before a runtime LLM request is made

### Requirement: Launch the console with the local environment file
The system SHALL provide an executable project-local launcher for `console_agent_test.py` that loads and exports `backend/.env` before starting the console process. Before accepting console input, it SHALL display the effective operational configuration including the resolved think-mode setting. It SHALL NOT display credential, token, password, API key, or secret values.

#### Scenario: Local launcher starts the console
- **WHEN** a developer runs the provided launcher from any working directory
- **THEN** it resolves the project `backend/.env`, exports its variables, and starts the existing console Agent entrypoint with `OCP_AGENT_LLM_THINK` available to the process

#### Scenario: Launcher displays configuration safely
- **WHEN** the launcher has loaded the local environment file
- **THEN** it displays the effective think-mode and non-sensitive operational settings while redacting sensitive values

### Requirement: Render streamed console answers without added line breaks
The console SHALL write each streamed LLM answer fragment immediately without appending a line break. It SHALL preserve line breaks included in the fragment and add one line break only after the streamed answer has completed.

#### Scenario: Answer is received in multiple fragments
- **WHEN** an LLM answer is received as two or more streamed fragments
- **THEN** the rendered answer is the exact concatenation of those fragments, followed by one console line break
