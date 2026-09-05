from langgraph.graph import END, START, StateGraph

from app.models.agent_state import AgentState


class PlanGraph:
    def __init__(self, plan_nodes):
        builder = StateGraph(AgentState)
        builder.add_node("create_plan", plan_nodes.create_plan)
        builder.add_edge(START, "create_plan")
        builder.add_edge("create_plan", END)
        self.graph = builder.compile()
