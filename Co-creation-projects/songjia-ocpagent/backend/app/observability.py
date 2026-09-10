"""Local trace, timing, streaming, and JSON Lines observability helpers."""
from __future__ import annotations
import asyncio, contextvars, inspect, json, logging, os, time, uuid
from collections.abc import AsyncGenerator, Awaitable, Callable
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

_request_id = contextvars.ContextVar("agent_request_id", default=None)
_trace_id = contextvars.ContextVar("agent_trace_id", default=None)
_event_sink = contextvars.ContextVar("agent_event_sink", default=None)
_event_count = contextvars.ContextVar("agent_event_count", default=0)
_starts = contextvars.ContextVar("agent_step_starts", default={})
_SENSITIVE = {"username", "password", "token", "api_key", "apikey", "secret"}
_DEFAULT_LOG = Path(__file__).resolve().parents[1] / "logs" / "agent-runtime.log"
LLM_TIMEOUT_SECONDS, LLM_HEARTBEAT_SECONDS = 300, 60
_LIFECYCLE_EVENTS = {"node_started", "node_completed", "node_failed"}

def redact(value: Any) -> Any:
    if hasattr(value, "model_dump"): value = value.model_dump()
    if isinstance(value, dict): return {k: "***" if k.lower() in _SENSITIVE else redact(v) for k, v in value.items()}
    if isinstance(value, (list, tuple)): return [redact(v) for v in value]
    return value

def _time() -> str: return datetime.now(timezone.utc).isoformat()
def request_id(state=None) -> str:
    value = (state or {}).get("request_id") or _request_id.get() or str(uuid.uuid4()); _request_id.set(value); return value
def trace_id(state=None) -> str:
    value = (state or {}).get("trace_id") or _trace_id.get() or str(uuid.uuid4()); _trace_id.set(value); return value
def normalize_request_state(state: dict[str, Any]) -> dict[str, Any]:
    result = dict(state); message = result.get("user_message", result.get("user_query"))
    if isinstance(message, str): result["user_message"] = message; result.setdefault("user_query", message)
    result.setdefault("trace_id", trace_id(result)); result.setdefault("request_id", request_id(result)); return result
def log_path() -> Path: return Path(os.getenv("OCP_AGENT_LOG_FILE", str(_DEFAULT_LOG)))
def _write(path: Path, record: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True); logger = logging.getLogger(f"ocp-agent:{path}")
    if not logger.handlers:
        logger.setLevel(logging.INFO); handler = logging.FileHandler(path, encoding="utf-8"); handler.setFormatter(logging.Formatter("%(message)s")); logger.addHandler(handler); logger.propagate = False
    logger.info(json.dumps(record, ensure_ascii=False, default=str))


def _aggregate_payload(event: str, payload: Any) -> Any:
    """Keep aggregate lifecycle records useful without copying Agent diagnostics."""
    if event not in _LIFECYCLE_EVENTS or not isinstance(payload, dict):
        return payload

    summary: dict[str, Any] = {
        "result_type": "object",
        "result_keys": sorted(str(key) for key in payload),
    }
    answer = payload.get("answer")
    if isinstance(answer, str):
        summary["answer_length"] = len(answer)

    knowledge_result = payload.get("knowledge_result")
    if isinstance(knowledge_result, dict):
        knowledge_summary: dict[str, Any] = {}
        citations = knowledge_result.get("citations")
        if isinstance(citations, list):
            knowledge_summary["citation_count"] = len(citations)
        diagnostics = knowledge_result.get("diagnostics")
        if isinstance(diagnostics, dict):
            counts = {
                stage: len(chunks)
                for stage, chunks in diagnostics.items()
                if isinstance(chunks, list)
            }
            if counts:
                knowledge_summary["diagnostic_counts"] = counts
        if knowledge_summary:
            summary["knowledge_result"] = knowledge_summary
    return summary


def node_log(agent, node, event, *, state=None, payload=None, error=None, step=None, duration_ms=None) -> None:
    record = {"timestamp": _time(), "request_id": request_id(state), "trace_id": trace_id(state), "agent": agent, "node": node, "step": step or node, "event": event}
    message = (state or {}).get("user_message", (state or {}).get("user_query"))
    if message is not None: record["user_message"] = redact(message)
    if payload is not None: record["payload"] = redact(payload)
    if error is not None: record.update(error_type=type(error).__name__, error=str(error))
    if duration_ms is not None: record["duration_ms"] = max(0.0, round(duration_ms, 3))
    aggregate = log_path(); agent_path = aggregate.parent / f"{agent}.log"
    if event not in {"retrieval_chunks", "llm_output"}:
        aggregate_record = dict(record)
        if payload is not None:
            aggregate_record["payload"] = _aggregate_payload(event, record["payload"])
        _write(aggregate, aggregate_record)
    if agent_path != aggregate: _write(agent_path, record)
def _event(agent, node, event, state, payload=None, error=None, **extra) -> None:
    sink = _event_sink.get()
    if sink is None: return
    value = {"event": event, "timestamp": _time(), "request_id": request_id(state), "trace_id": trace_id(state), "agent": agent, "node": node, **extra}
    if payload is not None: value["payload"] = redact(payload)
    if error is not None: value.update(error_type=type(error).__name__, error=str(error))
    sink.put_nowait(value)
    _event_count.set(_event_count.get() + 1)
def emit_progress(agent, node, phase, status, message, *, state=None) -> None:
    state = state or {}; key = (agent, node, phase); starts = dict(_starts.get()); duration = None
    if status == "started": starts[key] = time.perf_counter(); _starts.set(starts)
    elif key in starts: duration = (time.perf_counter() - starts.pop(key)) * 1000; _starts.set(starts)
    node_log(agent, node, "llm_thinking" if phase == "llm_thinking" else f"step_{status}", state=state, step=phase, duration_ms=duration, payload={"message": message})
    _event(agent, node, "progress", state, phase=phase, status=status, message=message, duration_ms=duration)
def emit_answer_chunk(agent, node, text, *, state=None, attempt=1, metadata=None) -> None:
    if text:
        node_log(agent, node, "llm_output", state=state, step="llm_generation", payload={"attempt": attempt, "text": text, "metadata": metadata})
        _event(agent, node, "answer_chunk", state or {}, attempt=attempt, text=text)
async def await_llm(call: Callable[[], Awaitable[Any]], *, agent: str, node: str, state: dict[str, Any]) -> Any:
    for attempt in range(1, 4):
        task, started = asyncio.create_task(call()), time.perf_counter()
        try:
            node_log(agent, node, "llm_attempt_started", state=state, step="llm_generation", payload={"attempt": attempt})
            while True:
                remaining = LLM_TIMEOUT_SECONDS - (time.perf_counter() - started)
                if remaining <= 0: raise TimeoutError("LLM call exceeded 300 seconds")
                done, _ = await asyncio.wait({task}, timeout=min(LLM_HEARTBEAT_SECONDS, remaining))
                if done: return task.result()
                emit_progress(agent, node, "llm_thinking", "active", "LLM 正在思考。", state=state)
        except TimeoutError as error:
            task.cancel()
            try: await task
            except asyncio.CancelledError: pass
            duration = (time.perf_counter() - started) * 1000; node_log(agent, node, "llm_timeout", state=state, error=error, step="llm_generation", duration_ms=duration, payload={"attempt": attempt}); _event(agent, node, "llm_timeout", state, error=error, duration_ms=duration, attempt=attempt)
            if attempt < 3:
                node_log(agent, node, "llm_retry_started", state=state, step="llm_generation", payload={"attempt": attempt + 1})
                continue
            node_log(agent, node, "llm_retry_exhausted", state=state, step="llm_generation", payload={"attempt": attempt})
            raise
    raise RuntimeError("unreachable")
def observed(agent, node, function):
    async def wrapper(state):
        state = normalize_request_state(state); started = time.perf_counter(); node_log(agent, node, "node_started", state=state); _event(agent, node, "node_started", state); emit_progress(agent, node, node, "started", f"正在执行 {node}。", state=state)
        try:
            result = function(state); result = await result if inspect.isawaitable(result) else result
        except Exception as error:
            duration = (time.perf_counter() - started) * 1000; node_log(agent, node, "node_failed", state=state, error=error, duration_ms=duration); _event(agent, node, "node_failed", state, error=error, duration_ms=duration); emit_progress(agent, node, node, "failed", f"{node} 执行失败。", state=state); raise
        duration = (time.perf_counter() - started) * 1000; node_log(agent, node, "node_completed", state=state, payload=result, duration_ms=duration); _event(agent, node, "node_completed", state, payload=result, duration_ms=duration); emit_progress(agent, node, node, "completed", f"{node} 已完成。", state=state); return result
    return wrapper
async def stream_graph(graph: Any, agent: str, state: dict[str, Any]) -> AsyncGenerator[dict[str, Any], None]:
    initial, accumulated, sink, finished, failure = normalize_request_state(state), None, asyncio.Queue(), object(), []
    accumulated = dict(initial); token = _event_sink.set(sink); count_token = _event_count.set(0)
    async def produce():
        try:
            async for raw in graph.astream(initial, stream_mode="updates"):
                emitted = _event_count.get()
                for update in raw.values():
                    if isinstance(update, dict): accumulated.update(update)
                if _event_count.get() == emitted:
                    for name, update in raw.items(): _event(agent, name, "node_completed", initial, payload=update)
        except BaseException as error: failure.append(error)
        finally: sink.put_nowait(finished)
    producer = asyncio.create_task(produce())
    try:
        while (item := await sink.get()) is not finished: yield item
        await producer
        if failure: raise failure[0]
    finally:
        _event_sink.reset(token)
        _event_count.reset(count_token)
        if not producer.done(): producer.cancel()
    yield {"event": "final_result", "timestamp": _time(), "request_id": request_id(initial), "trace_id": trace_id(initial), "agent": agent, "node": None, "payload": redact(accumulated)}
