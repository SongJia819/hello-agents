from typing import TypedDict, List, Annotated, Any
from app.models.cluster import Cluster
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    plans: List[str]
    tasks: List[str]
    current_task: str
    clusters: List[Cluster]
    current_cluster: Cluster
    agent: str
    user_query: str
    resource: str
    resources: List[str]
    supported: bool
    tool_result: Any
    answer: str
    action: str


