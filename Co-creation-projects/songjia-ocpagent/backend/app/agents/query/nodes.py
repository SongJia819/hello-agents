import asyncio

from app.services.cluster_service import ClusterService
from app.models.cluster import ClusterSummary


class QueryNodes:

    def __init__(self, cluster_service: ClusterService):
        self.cluster_service = cluster_service

    async def resolve_cluster(self, state):

        query = state["user_query"]

        clusters = await self.cluster_service.list_clusters()
        cluster: ClusterSummary = clusters[0]


        return {
            "current_cluster": cluster
        }

    async def list(self, state):
        cluster_id = state["current_cluster"].cluster_id
        resources = state["resources"]
        operations = {
            "node": self.cluster_service.list_nodes,
            "pod": self.cluster_service.list_pods,
        }

        results = await asyncio.gather(
            *(operations[resource](cluster_id) for resource in resources)
        )

        return {
            "tool_result": dict(zip(resources, results, strict=True))
        }
