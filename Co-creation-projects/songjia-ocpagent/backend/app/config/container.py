# app/config/container.py

from app.mcp.client import MCPClient
from app.services.cluster_service import ClusterService

from app.agents.query.nodes import QueryNodes
from app.agents.query.graph import QueryGraph
from app.agents.query.agent import QueryAgent
from app.agents.plan.nodes import PlanNodes
from app.agents.plan.graph import PlanGraph
from app.agents.plan.agent import PlanAgent
from app.agents.router.graph import RouterGraph
from app.agents.router.nodes import RouterNodes
from app.agents.router.agent import RouterAgent



class Container:

    def __init__(self):

        # MCP
        self.mcp_client = MCPClient()

        # Services
        self.cluster_service = ClusterService(self.mcp_client)

        # Query Agent
        self.query_nodes = QueryNodes(self.cluster_service)
        self.query_graph = QueryGraph(self.query_nodes)
        self.query_agent = QueryAgent(self.query_graph.graph)

        # Plan Agent (mock-only planning; it never executes a skill)
        self.plan_nodes = PlanNodes()
        self.plan_graph = PlanGraph(self.plan_nodes)
        self.plan_agent = PlanAgent(self.plan_graph.graph)

        # Router Agent
        self.router_nodes = RouterNodes()
        self.router_graph = RouterGraph(
            self.router_nodes, self.query_agent, self.plan_agent
        )
        self.router_agent = RouterAgent(self.router_graph.graph)

    async def initialize(self):
        await self.mcp_client.initialize()
