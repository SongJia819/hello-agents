import os

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class LLMSettings(BaseModel):
    empty_response_retry_limit: int = Field(default=3, ge=1)

    @classmethod
    def from_env(cls) -> "LLMSettings":
        value = os.getenv("OCP_AGENT_LLM_EMPTY_RESPONSE_RETRY_LIMIT")
        return cls(empty_response_retry_limit=int(value)) if value else cls()


llm_settings = LLMSettings.from_env()

llm = ChatOpenAI(
    model="qwen3.5:4b",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    temperature=0,
    max_tokens=11434,
)
