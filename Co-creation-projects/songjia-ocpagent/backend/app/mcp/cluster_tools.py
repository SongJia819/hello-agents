from app.mcp.cluster_store import MockClusterStore
from app.mcp.server_app import mcp
from app.models.cluster import ClusterSummary, Pod
from app.models.node import Node


store = MockClusterStore()


@mcp.tool
def list_nodes(cluster_id: str) -> list[Node]:
    return store.list_nodes(cluster_id)

@mcp.tool
def list_clusters() -> list[ClusterSummary]:
    return store.list_clusters()


@mcp.tool
def list_pods(cluster_id: str) -> list[Pod]:
    return store.list_pods(cluster_id)

@mcp.tool
def health() -> str:
    return "OK" if store.health_check() else "UNAVAILABLE"

