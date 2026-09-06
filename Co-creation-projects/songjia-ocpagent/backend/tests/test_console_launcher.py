import os
import subprocess
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "backend" / "scripts" / "start_console_agent_test.sh"


class ConsoleLauncherTests(unittest.TestCase):
    def test_launcher_loads_env_from_any_directory_without_printing_secrets(self):
        think_value = next(
            line.partition("=")[2]
            for line in (ROOT / "backend" / ".env").read_text().splitlines()
            if line.startswith("OCP_AGENT_LLM_THINK=")
        )
        result = subprocess.run(
            [str(SCRIPT)],
            cwd="/tmp",
            env={**os.environ, "CONSOLE_AGENT_TEST_DRY_RUN": "true"},
            text=True,
            capture_output=True,
            check=True,
        )
        self.assertIn(f"OCP_AGENT_LLM_THINK={think_value}", result.stdout)
        self.assertIn("Effective non-sensitive configuration", result.stdout)
        self.assertIn("Sensitive configuration values are redacted", result.stdout)
        self.assertNotIn("LLM_API_KEY=", result.stdout)
        self.assertNotIn("UNSPLASH_SECRET_KEY=", result.stdout)
