import os

from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field


class LLMSettings(BaseModel):
    empty_response_retry_limit: int = Field(default=3, ge=1)
    think: bool = True
    router_max_tokens: int = Field(default=1024, gt=0)
    query_max_tokens: int = Field(default=2048, gt=0)
    plan_max_tokens: int = Field(default=4096, gt=0)
    knowledge_chat_max_tokens: int = Field(default=2048, gt=0)
    knowledge_rag_max_tokens: int = Field(default=4096, gt=0)
    router_temperature: float = Field(default=0.0, ge=0.0, le=1.0)
    query_temperature: float = Field(default=0.2, ge=0.0, le=1.0)
    plan_temperature: float = Field(default=0.0, ge=0.0, le=1.0)
    knowledge_chat_temperature: float = Field(default=0.3, ge=0.0, le=1.0)
    knowledge_rag_temperature: float = Field(default=0.1, ge=0.0, le=1.0)

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
        for field in (
            "router_max_tokens",
            "query_max_tokens",
            "plan_max_tokens",
            "knowledge_chat_max_tokens",
            "knowledge_rag_max_tokens",
        ):
            if value := os.getenv(f"OCP_AGENT_LLM_{field.upper()}"):
                values[field] = int(value)
        for field in (
            "router_temperature",
            "query_temperature",
            "plan_temperature",
            "knowledge_chat_temperature",
            "knowledge_rag_temperature",
        ):
            if value := os.getenv(f"OCP_AGENT_LLM_{field.upper()}"):
                values[field] = float(value)
        return cls.model_validate(values)


def client_options(settings: LLMSettings | None = None) -> dict[str, object]:
    """Options shared by every Ollama-compatible runtime LLM client."""
    return {"extra_body": {"think": (settings or llm_settings).think}}


llm_settings = LLMSettings.from_env()

def create_llm(
    max_tokens: int, settings: LLMSettings | None = None, *, temperature: float = 0.0
) -> ChatOpenAI:
    """Create a local runtime LLM client with purpose-specific output and sampling settings."""
    return ChatOpenAI(
        model="qwen3.5:4b",
        base_url="http://localhost:11434/v1",
        api_key="ollama",
        temperature=temperature,
        max_tokens=max_tokens,
        **client_options(settings),
    )

query_llm = create_llm(llm_settings.query_max_tokens, temperature=llm_settings.query_temperature)


def create_plan_llm(settings: LLMSettings | None = None) -> ChatOpenAI:
    """Create the deterministic, non-thinking client shared by Plan tooling."""
    plan_settings = (settings or llm_settings).model_copy(update={"think": False})
    return create_llm(
        plan_settings.plan_max_tokens,
        plan_settings,
        temperature=plan_settings.plan_temperature,
    )


plan_llm = create_plan_llm()
routing_llm = create_llm(llm_settings.router_max_tokens, temperature=llm_settings.router_temperature)

# Compatibility alias for callers that have not yet selected a dedicated client.
llm = query_llm
