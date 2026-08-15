from langgraph.graph import START
from langgraph.graph import END
from langgraph.graph import StateGraph

from app.models.agent_state import AgentState


class QueryGraph:

    def __init__(self, query_nodes):

        builder = StateGraph(AgentState)

        builder.add_node(
            "resolve_cluster",
            query_nodes.resolve_cluster
        )

        builder.add_node("list", query_nodes.list)

        builder.add_edge(START, "resolve_cluster")

        builder.add_edge("resolve_cluster", "list")
        builder.add_edge("list", END)

        self.graph = builder.compile()
