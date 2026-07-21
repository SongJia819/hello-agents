import json

from langchain_mcp_adapters.client import MultiServerMCPClient
from typing import Type, TypeVar
T = TypeVar("T")

class MCPClient:

    def __init__(self):
        self.client = MultiServerMCPClient(
            {
                "ocp": {
                    "transport": "streamable_http",
                    "url": "http://127.0.0.1:8001/mcp",
                }
            }
        )
        self.tools = {}

    async def initialize(self):
        tools = await self.client.get_tools()
        self.tools = {tool.name: tool for tool in tools}

    async def call(self, tool_name: str, model: Type[T], **kwargs):
        tool = self.tools[tool_name]
        result = await tool.ainvoke(kwargs)
        data = json.loads(result[0]["text"])

        if isinstance(data, list):
            return [model.model_validate(x) for x in data]

        return model.model_validate(data)