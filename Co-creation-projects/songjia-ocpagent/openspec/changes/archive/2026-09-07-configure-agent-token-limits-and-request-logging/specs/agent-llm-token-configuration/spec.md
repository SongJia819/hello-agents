## ADDED Requirements

### Requirement: Runtime LLM output budgets are independently configurable
The system SHALL expose validated positive-integer environment configuration for the maximum output tokens of Router classification, Query answer generation, Plan generation, general Knowledge chat, and RAG-grounded Knowledge answer generation. The local `.env` defaults SHALL define Router `1024`, Query `2048`, Plan `2048`, general Knowledge chat `2048`, and RAG Knowledge answer `4096`.

#### Scenario: No token environment overrides are supplied
- **WHEN** runtime settings are loaded without token-limit environment overrides
- **THEN** each Agent uses its documented default and RAG Knowledge answer generation has a larger budget than Router and general Knowledge chat

#### Scenario: A deployment overrides one budget
- **WHEN** a valid environment value overrides the Router output-token budget
- **THEN** Router structured classification uses that value while the other Agent budgets retain their independently configured values

#### Scenario: An invalid budget is supplied
- **WHEN** a token-limit environment value is zero, negative, or not an integer
- **THEN** configuration loading fails with a validation error before an LLM client is used

### Requirement: Each runtime LLM consumer uses its purpose-specific budget
The Router, Query answer, Plan, general Knowledge chat, and RAG Knowledge answer consumers SHALL create or select their LLM client with their own configured maximum output tokens. Temporary hard-coded token limits SHALL not remain in those consumers.

#### Scenario: Query and RAG requests run in the same process
- **WHEN** a Query answer and a RAG Knowledge answer are generated in one runtime process
- **THEN** Query uses the Query budget and RAG uses the RAG Knowledge answer budget rather than a shared global limit
