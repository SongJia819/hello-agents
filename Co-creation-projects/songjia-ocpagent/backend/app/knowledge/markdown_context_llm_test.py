"""Answer one question from the complete contents of a local Markdown document."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any, Sequence, TextIO

from langchain_core.messages import HumanMessage, SystemMessage

from app.config.llm import LLMSettings, create_llm

MAX_TOKENS = 4096


class MarkdownContextTestError(RuntimeError):
    """Raised when the document or local LLM cannot complete the diagnostic."""


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("markdown_path", help="UTF-8 Markdown file to use as complete LLM context")
    parser.add_argument("question", help="Non-empty question to answer from the Markdown document")
    args = parser.parse_args(argv)
    if not args.question.strip():
        parser.error("question must not be empty")
    return args


def read_markdown(markdown_path: str | Path) -> str:
    path = Path(markdown_path)
    if path.suffix.lower() != ".md":
        raise MarkdownContextTestError("markdown_path must name a .md file")
    if not path.is_file():
        raise MarkdownContextTestError(f"Markdown file does not exist or is not a regular file: {path}")
    try:
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError) as error:
        raise MarkdownContextTestError(f"Cannot read UTF-8 Markdown file: {path}") from error


def build_messages(question: str, document: str) -> list[Any]:
    return [
        SystemMessage(
            content=(
                "Answer the user's question using only the supplied Markdown document. "
                "If the document does not contain enough information, say so."
            )
        ),
        HumanMessage(content=f"Question:\n{question}\n\nMarkdown document:\n{document}"),
    ]


def create_chat_model() -> Any:
    return create_llm(MAX_TOKENS, LLMSettings(think=False))


def answer_markdown(markdown_path: str | Path, question: str, *, chat_model: Any | None = None) -> str:
    document = read_markdown(markdown_path)
    try:
        response = (chat_model or create_chat_model()).invoke(build_messages(question, document))
    except Exception as error:
        raise MarkdownContextTestError(f"Local LLM invocation failed: {error}") from error
    content = getattr(response, "content", response)
    if not isinstance(content, str):
        raise MarkdownContextTestError("Local LLM returned non-text answer content")
    return content


def run(
    argv: Sequence[str] | None = None,
    *,
    stdout: TextIO = sys.stdout,
    stderr: TextIO = sys.stderr,
    chat_model: Any | None = None,
) -> int:
    try:
        args = parse_args(argv)
        answer = answer_markdown(args.markdown_path, args.question, chat_model=chat_model)
    except MarkdownContextTestError as error:
        print(f"markdown-context-llm-test: {error}", file=stderr)
        return 1
    stdout.write(answer)
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    return run(argv)


if __name__ == "__main__":
    raise SystemExit(main())
