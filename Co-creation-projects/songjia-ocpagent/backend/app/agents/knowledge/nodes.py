from app.models.knowledge import KnowledgeRequest
from app.services.knowledge_chat_service import KnowledgeChatService


class KnowledgeNodes:
    def __init__(self, service, chat_service=None):
        self.service = service
        self.chat_service = chat_service or KnowledgeChatService()

    async def answer(self, state):
        result = await self.service.answer(KnowledgeRequest(question=state["user_query"]), state=state)
        return {"answer": result.answer, "knowledge_result": result}

    async def chat(self, state):
        return {"answer": await self.chat_service.chat(state["user_query"], state=state)}
