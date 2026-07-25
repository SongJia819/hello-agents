
• ## 1. Project overview

  ocp-agent is an OpenShift-management AI-agent demo. It is explicitly scoped to simulated cluster operations: MCP tools return mock data and must not connect to a real cluster.

  The repository currently contains an early backend prototype. The intended frontend, REST API, memory layer, planner/execution/knowledge agents, and OpenSpec specifications are not implemented yet.

  ## 2. Current architecture

  Current executable flow:

  User query
    → Router LangGraph
    → capability check
    → Query LangGraph
    → ClusterService
    → MCP HTTP client
    → FastMCP mock server
    → mock clusters/nodes

  - The dependency container wires MCP, service, query agent, and router agent together in backend/app/config/container.py.
  - Router uses an Ollama-compatible local LLM (qwen3.5:4b) to return a structured route decision in backend/app/config/llm.py.
  - Only query → node → list_nodes is currently enabled by the capability map in backend/app/config/capabilities.py.
  - MCP is an HTTP service at 127.0.0.1:8001/mcp; it exposes mock list_clusters, list_nodes, and health tools in backend/app/mcp/cluster_tools.py.

  openspec/specs is empty, as is frontend. backend/app/api and run.py are also empty, so there is no backend API entrypoint or UI yet.

  ## 3. Important modules

  - Router agent — classifies intent, checks supported capabilities, then dispatches to the query graph: backend/app/agents/router.
  - Query agent — resolves the first mock cluster, then lists its nodes: backend/app/agents/query.
  - MCP client/server — adapter boundary between agent workflows and mock cluster tools: backend/app/mcp.
  - Service layer — keeps MCP calls out of agent nodes: backend/app/services/cluster_service.py.
  - Models/state — Pydantic domain models and LangGraph state schema: backend/app/models.
  - Tests — currently manual async demonstration scripts with printed output rather than assertion-based tests: backend/tests.