from collections.abc import AsyncGenerator
from app.observability import stream_graph


class PlanAgent:
    def __init__(self, graph):
        self.graph = graph

    async def invoke(self, state):
        return await self.graph.ainvoke(state)

    async def stream(
        self, state: dict, stream_mode: str = "updates"
    ) -> AsyncGenerator[dict, None]:
        del stream_mode
        async for event in stream_graph(self.graph, "plan", state):
            yield event
