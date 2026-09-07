import io
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from app.knowledge.markdown_context_llm_test import (
    MAX_TOKENS,
    MarkdownContextTestError,
    answer_markdown,
    build_messages,
    create_chat_model,
    extract_token_usage,
    format_token_usage,
    read_markdown,
    run,
)


class FakeChatModel:
    def __init__(self, answer="## Answer\n\n- formatted", *, usage_metadata=None, response_metadata=None):
        self.answer = answer
        self.usage_metadata = usage_metadata
        self.response_metadata = response_metadata
        self.messages = []

    def invoke(self, messages):
        self.messages = messages
        return SimpleNamespace(
            content=self.answer,
            usage_metadata=self.usage_metadata,
            response_metadata=self.response_metadata,
        )


class MarkdownContextLLMTestTests(unittest.TestCase):
    def test_reads_complete_utf8_markdown_and_places_it_unmodified_in_prompt(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.md"
            document = "# Images\n\n创建 image 的完整说明。\n"
            path.write_text(document, encoding="utf-8")
            model = FakeChatModel()

            answer = answer_markdown(path, "怎么创建 image？", chat_model=model)

        self.assertEqual(answer, "## Answer\n\n- formatted")
        self.assertEqual(model.messages[1].content, "Question:\n怎么创建 image？\n\nMarkdown document:\n" + document)
        self.assertIn("only the supplied Markdown document", model.messages[0].content)

    def test_rejects_missing_or_non_markdown_file(self):
        with self.assertRaisesRegex(MarkdownContextTestError, "does not exist"):
            read_markdown("missing.md")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.txt"
            path.write_text("not Markdown", encoding="utf-8")
            with self.assertRaisesRegex(MarkdownContextTestError, "must name a .md file"):
                read_markdown(path)

    def test_local_client_has_fixed_non_thinking_4096_token_settings(self):
        with patch("app.knowledge.markdown_context_llm_test.create_llm") as create:
            create_chat_model()

        max_tokens, settings = create.call_args.args
        self.assertEqual(max_tokens, MAX_TOKENS)
        self.assertEqual(MAX_TOKENS, 4096)
        self.assertFalse(settings.think)

    def test_build_messages_keeps_document_content_unchanged(self):
        document = "line one\n\n```yaml\nkey: value\n```\n"
        messages = build_messages("question", document)
        self.assertTrue(messages[1].content.endswith(document))

    def test_run_writes_only_exact_formatted_answer(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "document.md"
            path.write_text("source", encoding="utf-8")
            result = run([str(path), "question"], stdout=stdout, stderr=stderr,
                         chat_model=FakeChatModel(
                             "# Heading\n\ntext\n",
                             usage_metadata={"input_tokens": 12, "output_tokens": 5, "total_tokens": 17},
                         ))

        self.assertEqual(result, 0)
        self.assertEqual(stdout.getvalue(), "# Heading\n\ntext\n")
        self.assertEqual(stderr.getvalue(), "Token usage: input_tokens=12 output_tokens=5 total_tokens=17\n")

    def test_extracts_openai_compatible_usage_metadata(self):
        response = SimpleNamespace(
            usage_metadata=None,
            response_metadata={"token_usage": {"prompt_tokens": 10, "completion_tokens": 4, "total_tokens": 14}},
        )

        self.assertEqual(extract_token_usage(response), (10, 4, 14))
        self.assertEqual(format_token_usage(response), "Token usage: input_tokens=10 output_tokens=4 total_tokens=14")

    def test_missing_usage_is_rendered_as_unavailable_without_estimation(self):
        response = SimpleNamespace(usage_metadata=None, response_metadata={})

        self.assertEqual(extract_token_usage(response), (None, None, None))
        self.assertEqual(
            format_token_usage(response),
            "Token usage: input_tokens=unavailable output_tokens=unavailable total_tokens=unavailable",
        )

    def test_run_reports_input_error_on_stderr_without_invoking_model(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        result = run(["missing.md", "question"], stdout=stdout, stderr=stderr)

        self.assertEqual(result, 1)
        self.assertEqual(stdout.getvalue(), "")
        self.assertIn("markdown-context-llm-test:", stderr.getvalue())
