import json

from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

from app.config.llm import llm
from app.config.capabilities import CAPABILITIES, AgentType
from app.models.router import RouterResult

from .prompts import ROUTER_PROMPT


class RouterNodes:
    def __init__(self):
        self.router_llm = llm.with_structured_output(RouterResult)

    async def route(self, state):
        result: RouterResult = await self.router_llm.ainvoke(
            [
                SystemMessage(content=ROUTER_PROMPT),
                HumanMessage(content=state["user_query"]),
            ]
        )

        print("======= Router Result =======")
        print(result)

        return {
        **result.model_dump(),

        "messages": [
            AIMessage(
                content=result.model_dump_json(indent=2),
                name="router"
            )
        ]
    }

    def capability_check(self, state):
        agent = AgentType(state["agent"])
        resource = state["resource"]

        supported = resource in CAPABILITIES.get(agent, {})

        return {
            "supported": supported,
            "messages": (
                ""
                if supported
                else f"当前版本暂不支持 '{resource}' 功能。"
            )
        }

    def unsupported(slef, state):
        return {
            "answer": state["messages"]
        }