from app.services.cluster_service import ClusterService
from app.models.cluster import ClusterSummary


class QueryNodes:

    def __init__(self, cluster_service: ClusterService):
        self.cluster_service = cluster_service

    async def resolve_cluster(self, state):

        query = state["user_query"]

        clusters = await self.cluster_service.list_clusters()
        print(f"=======clusters: {clusters}")

        cluster: ClusterSummary = clusters[0]


        return {
            "current_cluster": cluster
        }

    async def list_nodes(self, state):

        nodes = await self.cluster_service.list_nodes(state["current_cluster"].cluster_id)

        return {
            "tool_result": nodes
        }