import asyncio
import io
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from app.agents.plan.skill_llm_diagnostic import (
    MAX_TOKENS,
    TIMEOUT_SECONDS,
    PlanSkillDiagnosticError,
    build_messages,
    create_chat_model,
    format_input,
    invoke_once,
    run,
)


class FakeChatModel:
    def __init__(self, content='{"skill": "ocp-node-delete"}'):
        self.content = content
        self.calls = []

    async def ainvoke(self, messages):
        self.calls.append(messages)
        return SimpleNamespace(content=self.content)


class PlanSkillLLMDiagnosticTests(unittest.TestCase):
    def test_prompt_uses_complete_node_delete_skill_contract_and_targets(self):
        messages = build_messages("cluster-a", "node-a")
        rendered = format_input(messages)

        self.assertIn("OCP Plan Agent", messages[0].content)
        self.assertIn("Skill: ocp-node-delete", rendered)
        self.assertIn("Bound input values: {'cluster_id': 'cluster-a', 'node_name': 'node-a'}", rendered)
        self.assertIn("## Procedure", rendered)
        self.assertIn("cordon_node", rendered)
        self.assertIn("drain_node", rendered)
        self.assertIn("delete_node", rendered)

    def test_client_uses_fixed_non_thinking_4096_token_settings(self):
        with patch("app.agents.plan.skill_llm_diagnostic.create_llm") as create:
            create_chat_model()

        max_tokens, settings = create.call_args.args
        self.assertEqual(max_tokens, MAX_TOKENS)
        self.assertEqual(MAX_TOKENS, 4096)
        self.assertFalse(settings.think)

    def test_run_prints_complete_input_and_unvalidated_output(self):
        stdout, stderr = io.StringIO(), io.StringIO()
        result = run(chat_model=FakeChatModel('{"steps": ["cordon_node"]}'), stdout=stdout, stderr=stderr)

        self.assertEqual(result, 0)
        self.assertIn("=== INPUT ===", stdout.getvalue())
        self.assertIn("Local skill contract:", stdout.getvalue())
        self.assertIn("=== OUTPUT ===", stdout.getvalue())
        self.assertIn('{"steps": ["cordon_node"]}', stdout.getvalue())
        self.assertEqual(stderr.getvalue(), "")

    def test_timeout_is_reported_without_output_block(self):
        class NeverReturns:
            async def ainvoke(self, _messages):
                await asyncio.sleep(1)

        stdout, stderr = io.StringIO(), io.StringIO()
        result = run(chat_model=NeverReturns(), stdout=stdout, stderr=stderr, timeout_seconds=0.001)

        self.assertEqual(result, 1)
        self.assertIn("=== INPUT ===", stdout.getvalue())
        self.assertNotIn("=== OUTPUT ===", stdout.getvalue())
        self.assertIn("timed out after 0.001 seconds", stderr.getvalue())

    def test_invocation_is_single_call_with_the_fixed_ten_minute_default(self):
        async def check():
            model = FakeChatModel()
            await invoke_once(build_messages(), chat_model=model)
            self.assertEqual(len(model.calls), 1)

        asyncio.run(check())
        self.assertEqual(TIMEOUT_SECONDS, 600)

    def test_non_text_response_is_reported(self):
        class NonTextModel:
            async def ainvoke(self, _messages):
                return SimpleNamespace(content={"plan": "not text"})

        with self.assertRaisesRegex(PlanSkillDiagnosticError, "non-text"):
            asyncio.run(invoke_once(build_messages(), chat_model=NonTextModel()))
