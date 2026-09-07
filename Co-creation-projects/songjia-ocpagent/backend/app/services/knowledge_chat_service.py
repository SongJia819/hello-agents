"""Direct configured-LLM chat for ordinary Knowledge Agent conversation."""

from __future__ import annotations

from typing import Any

from langchain_core.messages import HumanMessage, SystemMessage

from app.config.knowledge import KnowledgeSettings, knowledge_settings
from app.config.llm import client_options, llm_settings
from app.services.llm_streaming import collect_streamed_answer


class KnowledgeChatService:
    def __init__(self, settings: KnowledgeSettings | None = None, *, chat_model: Any | None = None):
        self.settings = settings or knowledge_settings
        self.chat_model = chat_model

    def _chat_dependencies(self) -> None:
        if self.chat_model is None:
            from langchain_openai import ChatOpenAI

            self.chat_model = ChatOpenAI(
                model=self.settings.llm_model,
                base_url=self.settings.llm_base_url,
                api_key="ollama",
                temperature=0,
                **client_options(),
            )

    async def chat(self, question: str, state: dict[str, Any] | None = None) -> str:
        self._chat_dependencies()
        return await collect_streamed_answer(
            self.chat_model,
            [
                SystemMessage(content="Respond helpfully to the user. Do not claim to use OCP documentation or citations."),
                HumanMessage(content=question),
            ],
            agent="knowledge",
            node="chat",
            state=state or {"user_query": question},
            attempts=llm_settings.empty_response_retry_limit,
            fallback="I cannot provide a general chat response right now.",
        )
