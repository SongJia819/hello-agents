class RouterAgent:

    def __init__(self, graph):
        self.graph = graph

    async def invoke(self, state):
        return await self.graph.ainvoke(state)

    async def stream(self, state, stream_mode="updates"):
        async for event in self.graph.astream(
            state,
            stream_mode=stream_mode
        ):
            yield event