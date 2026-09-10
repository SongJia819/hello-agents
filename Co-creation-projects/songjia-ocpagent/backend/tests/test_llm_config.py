import os
import unittest
from unittest.mock import patch

from app.config.llm import (
    LLMSettings,
    client_options,
    create_llm,
    plan_llm,
    query_llm,
    routing_llm,
)


class LLMThinkConfigurationTests(unittest.TestCase):
    def test_default_think_mode_is_enabled(self):
        with patch.dict(os.environ, {}, clear=True):
            settings = LLMSettings.from_env()
        self.assertTrue(settings.think)
        self.assertEqual(client_options(settings), {"extra_body": {"think": True}})

    def test_false_disables_think_mode(self):
        with patch.dict(os.environ, {"OCP_AGENT_LLM_THINK": "false"}, clear=True):
            settings = LLMSettings.from_env()
        self.assertFalse(settings.think)
        self.assertEqual(client_options(settings), {"extra_body": {"think": False}})

    def test_invalid_think_mode_is_rejected(self):
        with patch.dict(os.environ, {"OCP_AGENT_LLM_THINK": "sometimes"}, clear=True):
            with self.assertRaisesRegex(ValueError, "must be true or false"):
                LLMSettings.from_env()

    def test_token_budget_defaults_are_per_runtime_purpose(self):
        settings = LLMSettings()

        self.assertEqual(settings.router_max_tokens, 1024)
        self.assertEqual(settings.query_max_tokens, 2048)
        self.assertEqual(settings.plan_max_tokens, 2048)
        self.assertEqual(settings.knowledge_chat_max_tokens, 2048)
        self.assertEqual(settings.knowledge_rag_max_tokens, 4096)
        self.assertGreater(settings.knowledge_rag_max_tokens, settings.knowledge_chat_max_tokens)

    def test_temperature_defaults_are_per_runtime_purpose(self):
        settings = LLMSettings()

        self.assertEqual(settings.router_temperature, 0.0)
        self.assertEqual(settings.query_temperature, 0.2)
        self.assertEqual(settings.plan_temperature, 0.0)
        self.assertEqual(settings.knowledge_chat_temperature, 0.3)
        self.assertEqual(settings.knowledge_rag_temperature, 0.1)

    def test_token_budget_environment_override_is_independent(self):
        with patch.dict(os.environ, {"OCP_AGENT_LLM_ROUTER_MAX_TOKENS": "777"}, clear=True):
            settings = LLMSettings.from_env()

        self.assertEqual(settings.router_max_tokens, 777)
        self.assertEqual(settings.query_max_tokens, 2048)

    def test_temperature_environment_override_is_independent(self):
        with patch.dict(os.environ, {"OCP_AGENT_LLM_QUERY_TEMPERATURE": "0.7"}, clear=True):
            settings = LLMSettings.from_env()

        self.assertEqual(settings.query_temperature, 0.7)
        self.assertEqual(settings.router_temperature, 0.0)

    def test_invalid_token_budget_is_rejected(self):
        with patch.dict(os.environ, {"OCP_AGENT_LLM_PLAN_MAX_TOKENS": "0"}, clear=True):
            with self.assertRaisesRegex(ValueError, "greater than 0"):
                LLMSettings.from_env()

    def test_invalid_temperature_is_rejected(self):
        for value in ("not-a-number", "-0.1", "1.1"):
            with self.subTest(value=value), patch.dict(
                os.environ, {"OCP_AGENT_LLM_PLAN_TEMPERATURE": value}, clear=True
            ):
                with self.assertRaises(ValueError):
                    LLMSettings.from_env()

    def test_runtime_clients_use_purpose_specific_budgets(self):
        self.assertEqual(routing_llm.max_tokens, LLMSettings().router_max_tokens)
        self.assertEqual(query_llm.max_tokens, LLMSettings().query_max_tokens)
        self.assertEqual(plan_llm.max_tokens, LLMSettings().plan_max_tokens)
        self.assertEqual(create_llm(321, LLMSettings(think=False)).max_tokens, 321)

    def test_plan_client_disables_think_mode(self):
        self.assertEqual(plan_llm.extra_body, {"think": False})

    def test_runtime_clients_use_purpose_specific_temperatures(self):
        self.assertEqual(routing_llm.temperature, LLMSettings().router_temperature)
        self.assertEqual(query_llm.temperature, LLMSettings().query_temperature)
        self.assertEqual(plan_llm.temperature, LLMSettings().plan_temperature)
        self.assertEqual(
            create_llm(321, LLMSettings(think=False), temperature=0.6).temperature, 0.6
        )
