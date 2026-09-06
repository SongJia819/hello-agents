from langgraph.graph import END, START, StateGraph

from app.models.agent_state import AgentState


class KnowledgeGraph:
    def __init__(self, nodes):
        builder = StateGraph(AgentState)
        builder.add_node("answer", nodes.answer)
        builder.add_edge(START, "answer")
        builder.add_edge("answer", END)
        self.graph = builder.compile()
