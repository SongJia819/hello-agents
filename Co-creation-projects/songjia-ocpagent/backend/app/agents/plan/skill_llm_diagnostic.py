"""Direct, non-executing local LLM diagnostic for the node-delete plan skill."""

from __future__ import annotations

import argparse
import asyncio
import sys
from collections.abc import Sequence
from typing import Any, TextIO

from langchain_core.messages import HumanMessage, SystemMessage

from app.config.llm import create_plan_llm

from .prompts import PLAN_PROMPT
from .skills import SkillRegistry

TIMEOUT_SECONDS = 600
DEFAULT_CLUSTER_ID = "cluster-001"
DEFAULT_NODE_NAME = "cluster-001-worker-001"


class PlanSkillDiagnosticError(RuntimeError):
    """Raised when the direct LLM diagnostic cannot complete."""


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cluster-id", default=DEFAULT_CLUSTER_ID)
    parser.add_argument("--node-name", default=DEFAULT_NODE_NAME)
    return parser.parse_args(argv)


def build_messages(
    cluster_id: str = DEFAULT_CLUSTER_ID,
    node_name: str = DEFAULT_NODE_NAME,
    *,
    skill_registry: SkillRegistry | None = None,
) -> list[Any]:
    definition, skill_contract = (skill_registry or SkillRegistry()).resolve("delete", ["node"])
    input_values = {"cluster_id": cluster_id, "node_name": node_name}
    request = "\n".join(
        (
            f"Action: {definition.action}",
            f"Resources: {list(definition.resources)}",
            f"Skill: {definition.name}",
            f"Required inputs: {list(definition.required_inputs)}",
            f"Write-only inputs: {list(definition.write_only_inputs)}",
            f"Final outputs: {list(definition.final_outputs)}",
            f"Procedure step ids: {list(definition.procedure_step_ids)}",
            f"Bound input values: {input_values}",
            "Local skill contract:\n" + skill_contract,
        )
    )
    return [SystemMessage(content=PLAN_PROMPT), HumanMessage(content=request)]


def create_chat_model() -> Any:
    return create_plan_llm()


async def invoke_once(
    messages: list[Any], *, chat_model: Any, timeout_seconds: float = TIMEOUT_SECONDS
) -> str:
    try:
        response = await asyncio.wait_for(chat_model.ainvoke(messages), timeout=timeout_seconds)
    except TimeoutError as error:
        raise PlanSkillDiagnosticError(
            f"LLM invocation timed out after {timeout_seconds:g} seconds"
        ) from error
    except Exception as error:
        raise PlanSkillDiagnosticError(f"LLM invocation failed: {error}") from error

    content = getattr(response, "content", response)
    if not isinstance(content, str):
        raise PlanSkillDiagnosticError("LLM returned non-text content")
    return content


def format_input(messages: list[Any]) -> str:
    return "\n\n".join(
        f"--- {message.type.upper()} PROMPT ---\n{message.content}" for message in messages
    )


def run(
    argv: Sequence[str] | None = None,
    *,
    stdout: TextIO = sys.stdout,
    stderr: TextIO = sys.stderr,
    chat_model: Any | None = None,
    timeout_seconds: float = TIMEOUT_SECONDS,
) -> int:
    args = parse_args([] if argv is None else argv)
    messages = build_messages(args.cluster_id, args.node_name)
    print("=== INPUT ===", file=stdout)
    print(format_input(messages), file=stdout)
    try:
        content = asyncio.run(
            invoke_once(messages, chat_model=chat_model or create_chat_model(), timeout_seconds=timeout_seconds)
        )
    except PlanSkillDiagnosticError as error:
        print(f"plan-skill-llm-diagnostic: {error}", file=stderr)
        return 1

    print("=== OUTPUT ===", file=stdout)
    print(content, file=stdout)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    return run(sys.argv[1:] if argv is None else argv)


if __name__ == "__main__":
    raise SystemExit(main())
