from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from app.config.llm import routing_llm
from app.config.capabilities import CAPABILITIES, AgentType
from app.models.router import RouterResult
from app.observability import await_llm, emit_progress

from .prompts import ROUTER_PROMPT


class RouterNodes:
    def __init__(self, router_llm=None):
        self.router_llm = router_llm or routing_llm.with_structured_output(RouterResult)

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

    def unsupported(slef, state):
        return {
            "answer": state["messages"]
        }
