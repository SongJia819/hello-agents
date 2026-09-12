from langgraph.graph import END, START, StateGraph

from app.models.agent_state import AgentState
from app.observability import observed


class ExecutorGraph:
    def __init__(self, executor_nodes):
        builder = StateGraph(AgentState)
        builder.add_node(
            "execute_plan",
            observed("executor", "execute_plan", executor_nodes.execute_plan),
        )
        builder.add_edge(START, "execute_plan")
        builder.add_edge("execute_plan", END)
        self.graph = builder.compile()
