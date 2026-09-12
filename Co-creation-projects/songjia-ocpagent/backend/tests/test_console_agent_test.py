import asyncio
import unittest

from app.console_agent_test import MCPStartupError, console_loop, format_progress, format_state, run_console, start_fresh_mcp_server
from app.models.plan import Plan, PlanStep


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

    async def stream(self, state):
        self.calls.append(state)
        if state["user_query"] == "broken":
            raise RuntimeError("router unavailable")
        yield {"event": "node_completed", "agent": "router", "node": "route", "payload": {"password": "hidden"}}
        yield {"event": "progress", "timestamp": "2026-09-10T12:00:00+00:00", "agent": "knowledge", "node": "answer", "phase": "recall", "message": "正在召回文档。"}
        yield {"event": "answer_chunk", "agent": "knowledge", "node": "answer", "text": "first line\n\nsecond line"}
        yield {"event": "final_result", "agent": "router", "payload": {"answer": "first line\n\nsecond line", "password": "hidden", "supported": True}}


class FragmentedAnswerRouter:
    async def stream(self, _state):
        yield {"event": "answer_chunk", "text": "Answer"}
        yield {"event": "answer_chunk", "text": " with"}
        yield {"event": "answer_chunk", "text": " spacing"}
        yield {"event": "final_result", "payload": {"answer": "Answer with spacing"}}


class PlanRouter:
    async def stream(self, _state):
        yield {
            "event": "final_result",
            "payload": {
                "plan": Plan(
                    skill="ocp-node-delete", action="delete", resources=["node"],
                    target={"cluster_id": "cluster-1", "node_name": "node-1"},
                    parameters={"drain": {"force": True}},
                    required_inputs=["cluster_id", "node_name"], final_outputs=["node_deleted"],
                    steps=[PlanStep(id="cordon_node", skill="ocp-node-delete", description="Plan only")],
                ),
            },
        }


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

        def reset():
            order.append(("reset", None))

        result = await start_fresh_mcp_server(
            find_pids=lambda: [101, 102], stop_pid=stop, is_port_open=closed_port,
            spawn=spawn, wait_ready=ready, reset_data=reset,
        )
        self.assertIs(result, process)
        self.assertEqual(order, [("stop", 101), ("stop", 102), ("port", None), ("reset", None), ("spawn", None), ("ready", None)])

    async def test_unknown_port_owner_is_not_replaced(self):
        reset_calls = []

        async def occupied():
            return True

        with self.assertRaises(MCPStartupError):
            await start_fresh_mcp_server(
                find_pids=lambda: [], is_port_open=occupied,
                reset_data=lambda: reset_calls.append(True),
            )
        self.assertEqual(reset_calls, [])

    async def test_reset_failure_prevents_mcp_spawn(self):
        spawned = []

        async def closed_port():
            return False

        async def spawn():
            spawned.append(True)
            return FakeProcess()

        with self.assertRaisesRegex(MCPStartupError, "Mock data reset failed"):
            await start_fresh_mcp_server(
                find_pids=lambda: [], is_port_open=closed_port, spawn=spawn,
                reset_data=lambda: (_ for _ in ()).throw(RuntimeError("database unavailable")),
            )
        self.assertEqual(spawned, [])

    async def test_console_forwards_only_nonblank_nonexit_requests(self):
        router, output = FakeRouter(), []
        lines = iter(["  ", "list node", "broken", "quit"])
        await console_loop(
            router, input_fn=lambda _prompt: next(lines), output=output.append,
            answer_output=output.append, answer_end=lambda: None,
        )
        self.assertEqual(router.calls, [{"user_query": "list node"}, {"user_query": "broken"}])
        self.assertIn("router unavailable", output[-1])
        self.assertNotIn("hidden", "\n".join(output))
        self.assertRegex(output[0], r"^\[.*\] 正在召回文档。$")
        self.assertEqual(output[1], "first line\n\nsecond line")
        self.assertEqual(len(output), 3)

    async def test_console_renders_fragmented_answer_continuously(self):
        rendered = []
        lines = iter(["question", "quit"])
        await console_loop(
            FragmentedAnswerRouter(), input_fn=lambda _prompt: next(lines), output=lambda _text: None,
            answer_output=rendered.append, answer_end=lambda: rendered.append("\n"),
        )
        self.assertEqual("".join(rendered), "Answer with spacing\n")

    async def test_console_renders_plan_json_without_execution_output(self):
        output = []
        lines = iter(["delete node-1 in cluster-1", "quit"])
        await console_loop(PlanRouter(), input_fn=lambda _prompt: next(lines), output=output.append)

        self.assertEqual(output[0], "Plan (planning only):")
        self.assertIn('"skill": "ocp-node-delete"', output[1])
        self.assertIn('"cluster_id": "cluster-1"', output[1])
        self.assertNotIn("executed", output[1].lower())

    async def test_run_console_stops_only_fresh_managed_process(self):
        events, process = [], FakeProcess()

        async def start(*, reset_data):
            events.append("start")
            reset_data()
            return process

        def reset():
            events.append("reset")

        async def stop(value):
            events.append(("stop", value))

        class Container:
            router_agent = FakeRouter()

            async def initialize(self):
                events.append("initialize")

        await run_console(
            container_factory=Container, start_server=start, stop_server=stop, reset_data=reset,
            input_fn=lambda _prompt: "exit", output=lambda _line: None,
        )
        self.assertEqual(events, ["start", "reset", "initialize", ("stop", process)])

    def test_format_state_is_json_safe_and_redacts_credentials(self):
        rendered = format_state({"answer": "ok", "password": "secret"})
        self.assertIn('"answer": "ok"', rendered)
        self.assertNotIn("secret", rendered)

    def test_console_renders_schema_validation_success_with_timestamp(self):
        rendered = format_progress({
            "event": "progress", "timestamp": "2026-09-12T12:00:00+00:00",
            "phase": "schema_validation", "message": "Schema validation succeeded.",
        })
        self.assertRegex(rendered, r"^\[.*\] Schema validation succeeded\.$")

    def test_console_renders_executor_execution_milestones_with_timestamp(self):
        rendered = format_progress({
            "event": "progress", "timestamp": "2026-09-12T12:00:00+00:00",
            "phase": "plan_execution", "message": "步骤执行成功：cordon_node。",
        })
        self.assertRegex(rendered, r"^\[.*\] 步骤执行成功：cordon_node。$")
