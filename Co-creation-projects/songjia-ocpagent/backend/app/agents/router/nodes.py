from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from app.config.llm import routing_llm
from app.config.capabilities import CAPABILITIES, AgentType
from app.mcp.cluster_store import MockClusterStore
from app.models.router import RouterResult
from app.observability import await_llm, emit_progress

from .prompts import ROUTER_PROMPT


class RouterNodes:
    def __init__(self, router_llm=None, cluster_store=None):
        self.router_llm = router_llm or routing_llm.with_structured_output(RouterResult)
        self.cluster_store = cluster_store or MockClusterStore()

    async def route(self, state):
        emit_progress("router", "route", "route_classification", "started", "正在识别请求。", state=state)
        result: RouterResult = await await_llm(lambda: self.router_llm.ainvoke(
            [
                SystemMessage(content=ROUTER_PROMPT),
                HumanMessage(content=state["user_query"]),
            ]
        ), agent="router", node="route", state=state)
        emit_progress("router", "route", "route_classification", "completed", "请求已识别。", state=state)

        route = result.model_dump()
        route["resource"] = route["resources"][0]
        # Preserve selectors emitted through the older compatibility fields while
        # making the normalized work-target fields available to downstream state.
        route["current_work_cluster"] = (
            route["current_work_cluster"] or route.get("cluster_name", "")
        )
        route["current_work_node"] = (
            route["current_work_node"] or route.get("resource_name", "")
        )
        self._validate_delete_target(state["user_query"], route)

        return {
        **route,

        "messages": [
            AIMessage(
                content=result.model_dump_json(indent=2),
                name="router"
            )
        ]
    }

    def capability_check(self, state):
        if error := state.get("routing_error"):
            return {"supported": False, "messages": error}
        try:
            agent = AgentType(state["agent"])
        except ValueError:
            agent = None

        action = state.get("action")
        resources = state.get("resources") or ([state["resource"]] if state.get("resource") else [])
        supported_resources = CAPABILITIES.get(agent, {}).get(action, {})
        unsupported_resources = [
            resource for resource in resources if resource not in supported_resources
        ]
        supported = bool(resources) and not unsupported_resources

        if not supported:
            if agent is None:
                message = f"当前版本暂不支持 '{state.get('agent', '')}' Agent。"
            elif action not in CAPABILITIES.get(agent, {}):
                message = f"当前版本暂不支持 '{action}' 操作。"
            else:
                message = f"当前版本暂不支持 '{', '.join(unsupported_resources)}' 功能。"

        result = {"supported": supported}
        if not supported:
            result["messages"] = message
        return result

    def _validate_delete_target(self, user_query: str, route: dict) -> None:
        """Resolve delete targets from the user text, never a shortened LLM selector."""
        if not (route.get("agent") == "plan" and route.get("action") == "delete"):
            return

        query = user_query.casefold()
        matches = [
            node
            for cluster in self.cluster_store.list_clusters()
            for node in self.cluster_store.list_nodes(cluster.cluster_id)
            if node.name.casefold() in query
        ]
        if len(matches) != 1:
            route["routing_error"] = (
                "Node deletion requires exactly one full node name from the selected cluster."
            )
            return

        node = matches[0]
        route["resources"] = ["node"]
        route["resource"] = "node"
        route["current_work_cluster"] = node.cluster_id
        route["cluster_name"] = node.cluster_id
        route["current_work_node"] = node.name
        route["resource_name"] = node.name

    def unsupported(slef, state):
        return {
            "answer": state["messages"]
        }
