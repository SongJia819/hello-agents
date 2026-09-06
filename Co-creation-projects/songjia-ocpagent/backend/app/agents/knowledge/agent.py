class KnowledgeAgent:
    def __init__(self, graph):
        self.graph = graph

    async def invoke(self, state):
        return await self.graph.ainvoke(state)
