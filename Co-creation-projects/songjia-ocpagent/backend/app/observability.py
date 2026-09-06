"""Small, local observability primitives for agent graph execution."""

from __future__ import annotations

import contextvars
import asyncio
import inspect
import json
import logging
import os
import uuid
from collections.abc import AsyncGenerator, Callable
from pathlib import Path
from typing import Any

_request_id: contextvars.ContextVar[str | None] = contextvars.ContextVar("agent_request_id", default=None)
_event_sink: contextvars.ContextVar[asyncio.Queue[Any] | None] = contextvars.ContextVar("agent_event_sink", default=None)
_event_count: contextvars.ContextVar[int] = contextvars.ContextVar("agent_event_count", default=0)
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
    sink.put_nowait(value)
    _event_count.set(_event_count.get() + 1)


def emit_progress(agent: str, node: str, phase: str, status: str, message: str,
                  *, state: dict[str, Any] | None = None) -> None:
    """Publish a safe semantic progress event immediately, if a request is streaming."""
    sink = _event_sink.get()
    if sink is None:
        return
    sink.put_nowait({"event": "progress", "request_id": request_id(state), "agent": agent,
                     "node": node, "phase": phase, "status": status, "message": message})
    _event_count.set(_event_count.get() + 1)


def emit_answer_chunk(agent: str, node: str, text: str, *, state: dict[str, Any] | None = None,
                      attempt: int = 1) -> None:
    sink = _event_sink.get()
    if sink is not None and text:
        sink.put_nowait({"event": "answer_chunk", "request_id": request_id(state), "agent": agent,
                         "node": node, "attempt": attempt, "text": text})
        _event_count.set(_event_count.get() + 1)


def observed(agent: str, node: str, function: Callable[..., Any]) -> Callable[..., Any]:
    async def wrapper(state: dict[str, Any]) -> dict[str, Any]:
        request_id(state)
        node_log(agent, node, "node_started", state=state)
        _stream_event(agent, node, "node_started", state)
        emit_progress(agent, node, node, "started", f"正在执行 {node}。", state=state)
        try:
            result = function(state)
            if inspect.isawaitable(result):
                result = await result
        except Exception as error:
            node_log(agent, node, "node_failed", state=state, error=error)
            _stream_event(agent, node, "node_failed", state, error=error)
            emit_progress(agent, node, node, "failed", f"{node} 执行失败。", state=state)
            raise
        node_log(agent, node, "node_completed", state=state, payload=result)
        _stream_event(agent, node, "node_completed", state, payload=result)
        emit_progress(agent, node, node, "completed", f"{node} 已完成。", state=state)
        return result
    return wrapper


async def stream_graph(graph: Any, agent: str, state: dict[str, Any]) -> AsyncGenerator[dict[str, Any], None]:
    initial = dict(state)
    rid = request_id(initial)
    accumulated = dict(initial)
    sink: asyncio.Queue[Any] = asyncio.Queue()
    token = _event_sink.set(sink)
    count_token = _event_count.set(0)
    finished = object()
    failure: list[BaseException] = []

    async def produce() -> None:
        try:
            async for raw_event in graph.astream(initial, stream_mode="updates"):
                emitted = _event_count.get()
                for update in raw_event.values():
                    if isinstance(update, dict):
                        accumulated.update(update)
                if _event_count.get() == emitted:
                    for node, update in raw_event.items():
                        sink.put_nowait({"event": "node_completed", "request_id": rid, "agent": agent,
                                         "node": node, "payload": redact(update)})
        except BaseException as error:
            failure.append(error)
        finally:
            sink.put_nowait(finished)

    producer = asyncio.create_task(produce())
    try:
        while True:
            event = await sink.get()
            if event is finished:
                break
            yield event
        await producer
        if failure:
            raise failure[0]
    finally:
        _event_sink.reset(token)
        _event_count.reset(count_token)
        if not producer.done():
            producer.cancel()
    yield {"event": "final_result", "request_id": rid, "agent": agent,
           "node": None, "payload": redact(accumulated)}
