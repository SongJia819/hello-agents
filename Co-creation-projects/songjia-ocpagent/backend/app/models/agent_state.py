from typing import TypedDict, List, Annotated, Any, NotRequired
from app.models.cluster import Cluster
from app.models.plan import Plan
from app.models.knowledge import KnowledgeResult
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    plans: List[str]
    tasks: List[str]
    current_task: str
    clusters: List[Cluster]
    current_cluster: Cluster
    current_work_cluster: NotRequired[str]
    current_work_node: NotRequired[str]
    cluster_count: NotRequired[int]
    agent: str
    user_query: str
    user_message: NotRequired[str]
    trace_id: NotRequired[str]
    resource: str
    resources: List[str]
    idrac_selectors: NotRequired[List[str]]
    supported: bool
    tool_result: Any
    answer: str
    action: str
    plan: NotRequired[Plan | None]
    knowledge_result: NotRequired[KnowledgeResult | None]


