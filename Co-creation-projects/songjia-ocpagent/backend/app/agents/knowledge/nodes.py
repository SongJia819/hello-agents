from app.models.knowledge import KnowledgeRequest


class KnowledgeNodes:
    def __init__(self, service):
        self.service = service

    async def answer(self, state):
        result = await self.service.answer(KnowledgeRequest(question=state["user_query"]))
        return {"answer": result.answer, "knowledge_result": result}
