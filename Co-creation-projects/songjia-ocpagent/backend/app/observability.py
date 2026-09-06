"""Small, local observability primitives for agent graph execution."""

from __future__ import annotations

import contextvars
import inspect
import json
import logging
import os
import uuid
from collections.abc import AsyncGenerator, Callable
from pathlib import Path
from typing import Any

_request_id: contextvars.ContextVar[str | None] = contextvars.ContextVar("agent_request_id", default=None)
_event_sink: contextvars.ContextVar[list[dict[str, Any]] | None] = contextvars.ContextVar("agent_event_sink", default=None)
_SENSITIVE = {"username", "password", "token", "api_key", "apikey", "secret"}
_DEFAULT_LOG = Path(__file__).resolve().parents[1] / "logs" / "agent-runtime.log"


def redact(value: Any) -> Any:
    if hasattr(value, "model_dump"):
        value = value.model_dump()
    if isinstance(value, dict):
        return {key: "***" if key.lower() in _SENSITIVE else redact(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [redact(item) for item in value]
    return value


def request_id(state: dict[str, Any] | None = None) -> str:
    value = (state or {}).get("request_id") or _request_id.get() or str(uuid.uuid4())
    _request_id.set(value)
    return value


def log_path() -> Path:
    return Path(os.getenv("OCP_AGENT_LOG_FILE", str(_DEFAULT_LOG)))


def node_log(agent: str, node: str, event: str, *, state: dict[str, Any] | None = None,
             payload: Any = None, error: Exception | None = None) -> None:
    path = log_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    record: dict[str, Any] = {
        "request_id": request_id(state), "agent": agent, "node": node, "event": event,
    }
    if payload is not None:
        record["payload"] = redact(payload)
    if error is not None:
        record["error_type"] = type(error).__name__
        record["error"] = str(error)
    logger = logging.getLogger(f"ocp-agent:{path}")
    if not logger.handlers:
        logger.setLevel(logging.INFO)
        handler = logging.FileHandler(path, encoding="utf-8")
        handler.setFormatter(logging.Formatter("%(asctime)s %(message)s"))
        logger.addHandler(handler)
        logger.propagate = False
    logger.info(json.dumps(record, ensure_ascii=False, default=str))


def _stream_event(agent: str, node: str, event: str, state: dict[str, Any], payload: Any = None,
                  error: Exception | None = None) -> None:
    sink = _event_sink.get()
    if sink is None:
        return
    value: dict[str, Any] = {"event": event, "request_id": request_id(state), "agent": agent, "node": node}
    if payload is not None:
        value["payload"] = redact(payload)
    if error is not None:
        value["error_type"] = type(error).__name__
        value["error"] = str(error)
    sink.append(value)


def observed(agent: str, node: str, function: Callable[..., Any]) -> Callable[..., Any]:
    async def wrapper(state: dict[str, Any]) -> dict[str, Any]:
        request_id(state)
        node_log(agent, node, "node_started", state=state)
        _stream_event(agent, node, "node_started", state)
        try:
            result = function(state)
            if inspect.isawaitable(result):
                result = await result
        except Exception as error:
            node_log(agent, node, "node_failed", state=state, error=error)
            _stream_event(agent, node, "node_failed", state, error=error)
            raise
        node_log(agent, node, "node_completed", state=state, payload=result)
        _stream_event(agent, node, "node_completed", state, payload=result)
        return result
    return wrapper


async def stream_graph(graph: Any, agent: str, state: dict[str, Any]) -> AsyncGenerator[dict[str, Any], None]:
    initial = dict(state)
    rid = request_id(initial)
    accumulated = dict(initial)
    sink: list[dict[str, Any]] = []
    token = _event_sink.set(sink)
    try:
        async for raw_event in graph.astream(initial, stream_mode="updates"):
            emitted = bool(sink)
            for update in raw_event.values():
                if isinstance(update, dict):
                    accumulated.update(update)
            while sink:
                yield sink.pop(0)
            if not emitted:
                for node, update in raw_event.items():
                    yield {"event": "node_completed", "request_id": rid, "agent": agent,
                           "node": node, "payload": redact(update)}
        while sink:
            yield sink.pop(0)
    finally:
        _event_sink.reset(token)
    yield {"event": "final_result", "request_id": rid, "agent": agent,
           "node": None, "payload": redact(accumulated)}
