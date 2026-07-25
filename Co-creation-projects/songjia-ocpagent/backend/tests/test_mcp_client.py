import asyncio
import json

from langchain_mcp_adapters.client import MultiServerMCPClient
from app.models.node import Node
from app.models.cluster import ClusterSummary



async def main():
    client = MultiServerMCPClient(
        {
            "ocp": {
                "transport": "streamable_http",
                "url": "http://127.0.0.1:8001/mcp",
            }
        }
    )

    tools = await client.get_tools()

    print("Available tools:")
    for tool in tools:
        print(f" - {tool.name}")

    #
    # list_clusters
    #
    cluster_tool = next(t for t in tools if t.name == "list_clusters")

    result = await cluster_tool.ainvoke({})

    clusters = [
        ClusterSummary.model_validate(item)
        for item in json.loads(result[0]["text"])
    ]

    print("\nClusters:")
    for cluster in clusters:
        print(cluster)

    #
    # list_nodes
    #
    node_tool = next(t for t in tools if t.name == "list_nodes")

    nodes_result = await node_tool.ainvoke(
        {
            "cluster_id": clusters[0].cluster_id
        }
    )

    nodes = [
        Node.model_validate(item)
        for item in json.loads(nodes_result[0]["text"])
    ]

    print("\nNodes:")
    for node in nodes:
        print(node)


if __name__ == "__main__":
    asyncio.run(main())