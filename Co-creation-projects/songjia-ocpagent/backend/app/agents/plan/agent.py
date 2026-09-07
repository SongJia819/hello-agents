from collections.abc import AsyncGenerator
from app.observability import normalize_request_state, stream_graph


class PlanAgent:
    def __init__(self, graph):
        self.graph = graph

    async def invoke(self, state):
        return await self.graph.ainvoke(normalize_request_state(state))

    async def stream(
        self, state: dict, stream_mode: str = "updates"
    ) -> AsyncGenerator[dict, None]:
        del stream_mode
        async for event in stream_graph(self.graph, "plan", normalize_request_state(state)):
            yield event
