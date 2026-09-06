import os

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class LLMSettings(BaseModel):
    empty_response_retry_limit: int = Field(default=3, ge=1)
    think: bool = True

    @classmethod
    def from_env(cls) -> "LLMSettings":
        values: dict[str, object] = {}
        if value := os.getenv("OCP_AGENT_LLM_EMPTY_RESPONSE_RETRY_LIMIT"):
            values["empty_response_retry_limit"] = int(value)
        if value := os.getenv("OCP_AGENT_LLM_THINK"):
            normalized = value.strip().lower()
            if normalized not in {"true", "false"}:
                raise ValueError("OCP_AGENT_LLM_THINK must be true or false")
            values["think"] = normalized == "true"
        return cls.model_validate(values)


def client_options(settings: LLMSettings | None = None) -> dict[str, object]:
    """Options shared by every Ollama-compatible runtime LLM client."""
    return {"extra_body": {"think": (settings or llm_settings).think}}


llm_settings = LLMSettings.from_env()

llm = ChatOpenAI(
    model="qwen3.5:4b",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    temperature=0,
    max_tokens=11434,
    **client_options(),
)
