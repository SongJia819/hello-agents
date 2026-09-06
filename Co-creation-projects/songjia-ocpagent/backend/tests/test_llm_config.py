import os
import unittest
from unittest.mock import patch

from app.config.llm import LLMSettings, client_options


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
