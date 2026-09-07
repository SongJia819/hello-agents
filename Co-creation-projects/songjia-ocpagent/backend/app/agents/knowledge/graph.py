from langgraph.graph import END, START, StateGraph

from app.models.agent_state import AgentState
from app.observability import observed


class KnowledgeGraph:
    def __init__(self, nodes):
        builder = StateGraph(AgentState)
        builder.add_node("select", self.select)
        builder.add_node("answer", observed("knowledge", "answer", nodes.answer))
        builder.add_node("chat", observed("knowledge", "chat", nodes.chat))
        builder.add_edge(START, "select")
        builder.add_conditional_edges("select", self.entry_node, {"answer": "answer", "chat": "chat"})
        builder.add_edge("answer", END)
        builder.add_edge("chat", END)
        self.graph = builder.compile()

    @staticmethod
    def entry_node(state: AgentState) -> str:
        return "chat" if state.get("action") == "chat" else "answer"

    @staticmethod
    def select(_state: AgentState) -> dict:
        return {}
