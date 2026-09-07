from app.observability import normalize_request_state, stream_graph


class RouterAgent:

    def __init__(self, graph):
        self.graph = graph

    async def invoke(self, state):
        return await self.graph.ainvoke(normalize_request_state(state))

    async def stream(self, state, stream_mode="updates"):
        del stream_mode
        async for event in stream_graph(self.graph, "router", normalize_request_state(state)):
            yield event
