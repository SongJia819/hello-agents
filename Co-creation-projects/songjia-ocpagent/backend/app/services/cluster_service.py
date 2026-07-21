from app.mcp.client import MCPClient
from app.models.cluster import ClusterSummary
from app.models.node import Node

class ClusterService:
    def __init__(self, mcp_client: MCPClient):
        self.mcp_client = mcp_client

    async def list_nodes(self, cluster_id: str):
        return await self.mcp_client.call("list_nodes", Node, cluster_id=cluster_id)

    async def list_clusters(self):
        return await self.mcp_client.call("list_clusters", ClusterSummary)
