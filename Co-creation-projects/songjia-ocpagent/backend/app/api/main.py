from __future__ import annotations

from collections.abc import Callable, Mapping
from contextlib import asynccontextmanager
from typing import Any

from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field

_SENSITIVE_FIELDS = {"username", "password", "token", "api_key", "apikey", "secret"}


class ChatRequest(BaseModel):
    message: str = Field(min_length=1)


class RouteMetadata(BaseModel):
    agent: str | None = None
    action: str | None = None
    resource: str | None = None
    resource_name: str | None = None
    cluster_name: str | None = None


class ChatResponse(BaseModel):
    message: str
    route: RouteMetadata | None = None
    supported: bool | None = None
    answer: Any = None
    result: Any = None


def _sanitize(value: Any) -> Any:
    encoded = jsonable_encoder(value)

    if isinstance(encoded, list):
        return [_sanitize(item) for item in encoded]

    if isinstance(encoded, dict):
        return {
            key: _sanitize(item)
            for key, item in encoded.items()
            if key.lower() not in _SENSITIVE_FIELDS
        }

    return encoded


def _chat_response(message: str, state: Mapping[str, Any]) -> ChatResponse:
    route_keys = ("agent", "action", "resource", "resource_name", "cluster_name")
    route_values = {key: state[key] for key in route_keys if key in state}

    return ChatResponse(
        message=message,
        route=RouteMetadata(**route_values) if route_values else None,
        supported=state.get("supported"),
        answer=_sanitize(state.get("answer")),
        result=_sanitize(state.get("tool_result")),
    )


def _default_container_factory() -> Any:
    from app.config.container import Container

    return Container()


def create_app(container_factory: Callable[[], Any] | None = None) -> FastAPI:
    factory = container_factory or _default_container_factory

    @asynccontextmanager
    async def lifespan(app: FastAPI):
        container = factory()
        await container.initialize()
        app.state.container = container
        yield

    app = FastAPI(title="OCP Agent API", lifespan=lifespan)

    @app.post("/v1/chat", response_model=ChatResponse)
    async def chat(payload: ChatRequest, request: Request) -> ChatResponse:
        state = await request.app.state.container.router_agent.invoke(
            {"user_query": payload.message, "user_message": payload.message}
        )
        return _chat_response(payload.message, state)

    return app


app = create_app()
