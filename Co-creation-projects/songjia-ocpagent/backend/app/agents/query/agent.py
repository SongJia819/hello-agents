from collections.abc import AsyncGenerator

class QueryAgent:

    def __init__(self, graph):
        self.graph = graph

    async def invoke(self, state):

        return await self.graph.ainvoke(state)

    async def stream(
            self,
            state: dict,
            stream_mode: str = "updates"
    ) -> AsyncGenerator[dict, None]:
        async for event in self.graph.astream(
                state,
                stream_mode=stream_mode
        ):
            yield event