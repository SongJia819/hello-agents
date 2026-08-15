from app.models.node import Node
from app.mcp.server_app import mcp
from app.models.cluster import ClusterSummary, Pod


@mcp.tool
def list_nodes(cluster_id: str) -> list[Node]:
    result = []
    node = Node(
        name=f"{cluster_id}-node-001",
        username="admin",
        password="Admin@123456",
        domain="agent.local",
        network={
            "port": 8080,
            "ip": "192.168.1.100",
            "netmask": "255.255.255.0",
            "gateway": "192.168.1.1"
        },
        image={
            "image_name": "ollama-qwen3-4b",
            "image_path": "/opt/docker/images/qwen3-4b.tar"
        },
        firmware={
            "firmware_name": "device-fw-v2.3.1",
            "firmware_path": "/data/firmware/v2.3.1.bin"
        },
        certificate={
            "certificate_file_name": "agent-cert.pem",
            "certificate_file_path": "/etc/ssl/certs/agent-cert.pem"
        }
    )
    result.append(node)
    return result

@mcp.tool
def list_clusters() -> list[ClusterSummary]:
    clusters = []
    clusters.append(ClusterSummary(
        cluster_id="cluster-001",
        cluster_name="Cluster 1"
    ))
    return clusters


@mcp.tool
def list_pods(cluster_id: str) -> list[Pod]:
    return [
        Pod(
            pod_name=f"{cluster_id}-api-7d8f9c6b5d-xk2lm",
            pod_ip="10.128.0.21",
        ),
        Pod(
            pod_name=f"{cluster_id}-worker-6b7c8d9e4f-pq3rs",
            pod_ip="10.128.0.22",
        ),
    ]

@mcp.tool
def health() -> str:
    return "OK"

