import asyncio

from app.mcp.client import MCPClient
from app.models.cluster import ClusterSummary, Pod
from app.models.idrac import IdracNode
from app.models.node import Node

class ClusterService:
    def __init__(self, mcp_client: MCPClient):
        self.mcp_client = mcp_client

    async def list_nodes(self, cluster_id: str):
        return await self.mcp_client.call("list_nodes", Node, cluster_id=cluster_id)

    async def list_pods(self, cluster_id: str):
        return await self.mcp_client.call("list_pods", Pod, cluster_id=cluster_id)

    async def list_idrac_nodes(self, selectors: list[str] | None = None) -> list[IdracNode]:
        if not selectors:
            return await self.mcp_client.call("list_idrac_nodes", IdracNode)

        if all(not self._is_ip_address(selector) for selector in selectors):
            return await self.mcp_client.call("list_idrac_nodes", IdracNode, sn=selectors)

        selected = await asyncio.gather(*(self.get_idrac_node(selector) for selector in selectors))
        seen: set[str] = set()
        result = []
        for node in selected:
            if node is None or node.sn in seen:
                continue
            seen.add(node.sn)
            result.append(node)
        return result

    async def get_idrac_node(self, selector: str) -> IdracNode | None:
        argument = "idrac_ip" if self._is_ip_address(selector) else "sn"
        return await self.mcp_client.call_optional("get_idrac_node", IdracNode, **{argument: selector})

    async def list_clusters(self):
        return await self.mcp_client.call("list_clusters", ClusterSummary)

    @staticmethod
    def _is_ip_address(value: str) -> bool:
        parts = value.split(".")
        return len(parts) == 4 and all(part.isdigit() and 0 <= int(part) <= 255 for part in parts)
