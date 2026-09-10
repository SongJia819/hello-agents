## Why

The Knowledge Agent currently only answers through the OCP documentation retrieval pipeline, while ordinary conversational requests can be rejected as unsupported. Users need a direct LLM response for general interaction without weakening the grounded OCP documentation-answering contract or bypassing another Agent's supported work.

## What Changes

- Add a Knowledge Agent plain-chat path that sends eligible non-OCP conversational requests directly to the configured LLM and returns its answer.
- Preserve the existing OCP documentation route, including retrieval, grounding, citations, and no-evidence behavior.
- Extend structured routing and capability validation to distinguish OCP documentation questions, supported work for other Agents, and eligible plain-chat requests.
- Return a clear LLM-failure fallback for plain chat without claiming documentation support or producing retrieval diagnostics.

## Capabilities

### New Capabilities

- `knowledge-chat-fallback`: Direct configured-LLM responses for ordinary conversation that does not belong to another supported Agent.

### Modified Capabilities

- `knowledge-question-answering`: Preserve grounded OCP documentation behavior while adding a distinct non-retrieval chat path.
- `agent-routing`: Classify and dispatch eligible plain-chat requests without diverting OCP documentation or supported Agent requests.

## Impact

- Affects Router prompt/model/capabilities/graph dispatch, Knowledge Agent nodes and service/model contracts, streaming progress, and focused router/Knowledge Agent tests.
- Uses the already configured local LLM endpoint; it does not add external infrastructure access or change mock-cluster-only MCP behavior.
