from app.observability import stream_graph


class RouterAgent:

    def __init__(self, graph):
        self.graph = graph

    async def invoke(self, state):
        return await self.graph.ainvoke(state)

    async def stream(self, state, stream_mode="updates"):
        del stream_mode
        async for event in stream_graph(self.graph, "router", state):
            yield event
