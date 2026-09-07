from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from app.config.llm import routing_llm
from app.config.capabilities import CAPABILITIES, AgentType
from app.models.router import RouterResult

from .prompts import ROUTER_PROMPT


class RouterNodes:
    def __init__(self, router_llm=None):
        self.router_llm = router_llm or routing_llm.with_structured_output(RouterResult)

    async def route(self, state):
        result: RouterResult = await self.router_llm.ainvoke(
            [
                SystemMessage(content=ROUTER_PROMPT),
                HumanMessage(content=state["user_query"]),
            ]
        )

        route = result.model_dump()
        route["resource"] = route["resources"][0]

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
