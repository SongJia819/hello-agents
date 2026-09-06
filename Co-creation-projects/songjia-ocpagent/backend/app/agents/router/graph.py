from langgraph.graph import StateGraph
from langgraph.graph import START
from langgraph.graph import END

from app.models.agent_state import AgentState


class RouterGraph:

    def __init__(self, router_nodes, query_agent, plan_agent, knowledge_agent):

        builder = StateGraph(AgentState)

        builder.add_node("route", router_nodes.route)
        builder.add_node("query", query_agent.invoke)
        builder.add_node("plan_agent", plan_agent.invoke)
        builder.add_node("knowledge", knowledge_agent.invoke)
        builder.add_node("capability_check", router_nodes.capability_check)
        builder.add_node("unsupported", router_nodes.unsupported)

        builder.add_edge(START,"route")
        builder.add_edge("route", "capability_check")

        builder.add_conditional_edges(
            "capability_check",
            self.route_next,
            {
                "query": "query",
                "plan": "plan_agent",
                "knowledge": "knowledge",
                "unsupported": "unsupported",
            },
        )

        builder.add_edge("query", END)
        builder.add_edge("plan_agent", END)
        builder.add_edge("knowledge", END)
        builder.add_edge("unsupported", END)

        self.graph = builder.compile()

    def route_next(self, state: AgentState) -> str:
        if not state["supported"]:
            return "unsupported"

        return state["agent"]
