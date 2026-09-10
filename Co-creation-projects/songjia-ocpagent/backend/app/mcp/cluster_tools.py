from app.mcp.cluster_store import MockClusterStore
from app.mcp.server_app import mcp
from app.models.cluster import ClusterSummary, Pod
from app.models.idrac import IdracNode
from app.models.node import Node, NodeOperationResult


store = MockClusterStore()


@mcp.tool
def list_nodes(cluster_id: str) -> list[Node]:
    return store.list_nodes(cluster_id)


@mcp.tool
def cordon_node(cluster_id: str, node_name: str) -> NodeOperationResult:
    return store.cordon_node(cluster_id, node_name)


@mcp.tool
def drain_node(cluster_id: str, node_name: str) -> NodeOperationResult:
    return store.drain_node(cluster_id, node_name)


@mcp.tool
def delete_node(cluster_id: str, node_name: str) -> NodeOperationResult:
    return store.delete_node(cluster_id, node_name)


@mcp.tool
def list_idrac_nodes(sn: list[str] | None = None) -> list[IdracNode]:
    return store.list_idrac_nodes(sn=sn)


@mcp.tool
def get_idrac_node(sn: str | None = None, idrac_ip: str | None = None) -> IdracNode | None:
    return store.get_idrac_node(sn=sn, idrac_ip=idrac_ip)

@mcp.tool
def list_clusters() -> list[ClusterSummary]:
    return store.list_clusters()


@mcp.tool
def list_pods(cluster_id: str) -> list[Pod]:
    return store.list_pods(cluster_id)

@mcp.tool
def health() -> str:
    return "OK" if store.health_check() else "UNAVAILABLE"

