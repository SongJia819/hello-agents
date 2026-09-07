import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.observability import observed, redact, stream_graph
from app.agents.knowledge.agent import KnowledgeAgent
from app.agents.plan.agent import PlanAgent
from app.agents.query.agent import QueryAgent
from app.agents.router.agent import RouterAgent


class FakeGraph:
    async def astream(self, _state, stream_mode):
        self.mode = stream_mode
        yield {"route": {"agent": "query", "password": "nope"}}
        yield {"query": {"tool_result": {"node": [{"name": "worker"}]}}}


class ObservabilityTests(unittest.IsolatedAsyncioTestCase):
    async def test_stream_normalizes_updates_and_has_one_final_event(self):
        events = [event async for event in stream_graph(FakeGraph(), "router", {"user_query": "list node"})]
        self.assertEqual([event["event"] for event in events], ["node_completed", "node_completed", "final_result"])
        self.assertEqual(events[0]["node"], "route")
        self.assertEqual(events[1]["node"], "query")
        self.assertEqual(events[-1]["payload"]["tool_result"]["node"][0]["name"], "worker")
        self.assertEqual(events[0]["payload"]["password"], "***")

    async def test_observed_logs_lifecycle_and_redacts_secret(self):
        async def node(_state):
            return {"password": "hidden", "answer": "ok"}

        with tempfile.TemporaryDirectory() as directory, patch.dict("os.environ", {"OCP_AGENT_LOG_FILE": str(Path(directory) / "agent.log")}, clear=False):
            result = await observed("query", "list", node)(
                {"request_id": "request-1", "user_query": "list nodes"}
            )
            records = [json.loads(line.split(" ", 2)[2]) for line in (Path(directory) / "agent.log").read_text().splitlines()]
        self.assertEqual(result["answer"], "ok")
        self.assertEqual([record["event"] for record in records], ["node_started", "node_completed"])
        self.assertEqual(records[-1]["payload"]["password"], "***")
        self.assertEqual(records[-1]["request_id"], "request-1")
        self.assertEqual(records[-1]["user_message"], "list nodes")

    async def test_observed_logs_failure_and_reraises(self):
        async def node(_state):
            raise ValueError("bad node")

        with tempfile.TemporaryDirectory() as directory, patch.dict("os.environ", {"OCP_AGENT_LOG_FILE": str(Path(directory) / "agent.log")}, clear=False):
            with self.assertRaisesRegex(ValueError, "bad node"):
                await observed("plan", "create_plan", node)(
                    {"request_id": "request-2", "user_query": "add node"}
                )
            records = [json.loads(line.split(" ", 2)[2]) for line in (Path(directory) / "agent.log").read_text().splitlines()]
        self.assertEqual(records[-1]["event"], "node_failed")
        self.assertEqual(records[-1]["error_type"], "ValueError")
        self.assertEqual(records[-1]["user_message"], "add node")

    async def test_redact_recurses_models_and_lists(self):
        self.assertEqual(redact({"token": "x", "items": [{"api_key": "y"}]}), {"token": "***", "items": [{"api_key": "***"}]})

    async def test_agent_entrypoints_preserve_user_message(self):
        class CapturingGraph:
            async def ainvoke(self, state):
                return state

        for agent_type in (RouterAgent, QueryAgent, PlanAgent, KnowledgeAgent):
            with self.subTest(agent=agent_type.__name__):
                state = await agent_type(CapturingGraph()).invoke({"user_query": "original request"})
                self.assertEqual(state["user_query"], "original request")
                self.assertEqual(state["user_message"], "original request")
