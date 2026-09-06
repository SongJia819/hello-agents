"""Shared streaming answer collection with empty-response retries."""

from __future__ import annotations

from typing import Any

from app.observability import emit_answer_chunk, emit_progress, node_log


def _text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "".join(item.get("text", "") if isinstance(item, dict) else str(item) for item in content)
    return "" if content is None else str(content)


async def collect_streamed_answer(model: Any, messages: list[Any], *, agent: str, node: str,
                                  state: dict[str, Any], attempts: int, fallback: str) -> str:
    for attempt in range(1, attempts + 1):
        emit_progress(agent, node, "llm_generation", "started", "正在生成回答。", state=state)
        parts: list[str] = []
        try:
            if hasattr(model, "astream"):
                async for chunk in model.astream(messages):
                    text = _text(getattr(chunk, "content", chunk))
                    if text:
                        parts.append(text)
                        emit_answer_chunk(agent, node, text, state=state, attempt=attempt)
            else:  # compatibility for injected test doubles; configured models stream.
                response = await model.ainvoke(messages)
                text = _text(getattr(response, "content", response))
                if text:
                    parts.append(text)
                    emit_answer_chunk(agent, node, text, state=state, attempt=attempt)
        except Exception as error:
            node_log(agent, node, "llm_stream_failed", state=state, error=error)
            emit_progress(agent, node, "llm_generation", "failed", "回答生成失败。", state=state)
            return fallback
        answer = "".join(parts)
        if answer.strip():
            emit_progress(agent, node, "llm_generation", "completed", "回答生成完成。", state=state)
            return answer
        if attempt < attempts:
            emit_progress(agent, node, "llm_generation", "retrying", "回答为空，正在重试。", state=state)
    node_log(agent, node, "llm_empty_response_exhausted", state=state)
    emit_progress(agent, node, "llm_generation", "failed", "回答为空，已达到重试次数。", state=state)
    return fallback
