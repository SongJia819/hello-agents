import asyncio
import unittest

from app.console_agent_test import MCPStartupError, console_loop, format_state, run_console, start_fresh_mcp_server


class FakeProcess:
    def __init__(self):
        self.returncode = None
        self.terminated = False
        self.killed = False

    def terminate(self):
        self.terminated = True
        self.returncode = 0

    def kill(self):
        self.killed = True
        self.returncode = -9

    async def wait(self):
        return self.returncode


class FakeRouter:
    def __init__(self):
        self.calls = []

    async def invoke(self, state):
        self.calls.append(state)
        if state["user_query"] == "broken":
            raise RuntimeError("router unavailable")
        return {"answer": "ok", "password": "hidden"}


class ConsoleAgentTests(unittest.IsolatedAsyncioTestCase):
    async def test_prior_project_server_is_stopped_before_fresh_server_starts(self):
        order = []
        process = FakeProcess()

        async def stop(pid):
            order.append(("stop", pid))

        async def closed_port():
            order.append(("port", None))
            return False

        async def spawn():
            order.append(("spawn", None))
            return process

        async def ready():
            order.append(("ready", None))

        result = await start_fresh_mcp_server(
            find_pids=lambda: [101, 102], stop_pid=stop, is_port_open=closed_port,
            spawn=spawn, wait_ready=ready,
        )
        self.assertIs(result, process)
        self.assertEqual(order, [("stop", 101), ("stop", 102), ("port", None), ("spawn", None), ("ready", None)])

    async def test_unknown_port_owner_is_not_replaced(self):
        async def occupied():
            return True

        with self.assertRaises(MCPStartupError):
            await start_fresh_mcp_server(find_pids=lambda: [], is_port_open=occupied)

    async def test_console_forwards_only_nonblank_nonexit_requests(self):
        router, output = FakeRouter(), []
        lines = iter(["  ", "list node", "broken", "quit"])
        await console_loop(router, input_fn=lambda _prompt: next(lines), output=output.append)
        self.assertEqual(router.calls, [{"user_query": "list node"}, {"user_query": "broken"}])
        self.assertIn("router unavailable", output[1])
        self.assertNotIn("hidden", output[0])

    async def test_run_console_stops_only_fresh_managed_process(self):
        events, process = [], FakeProcess()

        async def start():
            events.append("start")
            return process

        async def stop(value):
            events.append(("stop", value))

        class Container:
            router_agent = FakeRouter()

            async def initialize(self):
                events.append("initialize")

        await run_console(
            container_factory=Container, start_server=start, stop_server=stop,
            input_fn=lambda _prompt: "exit", output=lambda _line: None,
        )
        self.assertEqual(events, ["start", "initialize", ("stop", process)])

    def test_format_state_is_json_safe_and_redacts_credentials(self):
        rendered = format_state({"answer": "ok", "password": "secret"})
        self.assertIn('"answer": "ok"', rendered)
        self.assertNotIn("secret", rendered)
