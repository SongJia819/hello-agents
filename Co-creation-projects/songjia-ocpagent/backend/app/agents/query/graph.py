from langgraph.graph import START
from langgraph.graph import END
from langgraph.graph import StateGraph

from app.models.agent_state import AgentState
from app.observability import observed


class QueryGraph:

    def __init__(self, query_nodes):

        builder = StateGraph(AgentState)

        builder.add_node(
            "resolve_cluster",
            observed("query", "resolve_cluster", query_nodes.resolve_cluster)
        )

        builder.add_node("list", observed("query", "list", query_nodes.list))
        builder.add_node(
            "summarize_answer",
            observed("query", "summarize_answer", query_nodes.summarize_answer),
        )

        builder.add_edge(START, "resolve_cluster")

        builder.add_edge("resolve_cluster", "list")
        builder.add_edge("list", "summarize_answer")
        builder.add_edge("summarize_answer", END)

        self.graph = builder.compile()
