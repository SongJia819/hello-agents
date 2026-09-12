import asyncio
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from app.agents.executor.agent import ExecutorAgent
from app.agents.executor.graph import ExecutorGraph
from app.agents.executor.nodes import ExecutorNodes
from app.agents.router.graph import RouterGraph
from app.models.node import NodeOperationResult, NodeStatus


def delete_plan(*, steps=None):
    return {
        "operation": "node.delete",
        "cluster_id": "cluster-001",
        "node_name": "cluster-001-worker-001",
        "steps": steps or [
            {"id": "cordon_node", "intent": "ignored", "inputs": [], "outputs": [], "depends_on": []},
            {"id": "drain_node", "intent": "ignored", "inputs": [], "outputs": [], "depends_on": ["cordon_node"]},
            {"id": "delete_node", "intent": "ignored", "inputs": [], "outputs": [], "depends_on": ["drain_node"]},
        ],
    }


class FakeMCPClient:
    def __init__(self, *, failures=None, exception_for=None):
        self.calls = []
        self.failures = failures or set()
        self.exception_for = exception_for

    async def call(self, tool_name, _model, **kwargs):
        self.calls.append((tool_name, kwargs))
        if tool_name == self.exception_for:
            raise RuntimeError("mock transport error")
        success = tool_name not in self.failures
        return NodeOperationResult(
            success=success,
            operation=f"node.{tool_name.removesuffix('_node')}",
            cluster_id=kwargs["cluster_id"],
            node_name=kwargs["node_name"],
            status=NodeStatus.CORDONED if tool_name == "cordon_node" and success else None,
            error_code=None if success else "MOCK_FAILURE",
            message="ok" if success else "mock failure",
        )


class ExecutorNodesTests(unittest.IsolatedAsyncioTestCase):
    async def test_executes_registered_steps_with_root_target_arguments(self):
        client = FakeMCPClient()
        result = await ExecutorNodes(client).execute_plan({"validated_plan": delete_plan()})

        self.assertTrue(result["execution_result"]["success"])
        self.assertEqual(result["execution_result"]["completed_step_ids"], ["cordon_node", "drain_node", "delete_node"])
        self.assertEqual([step["status"] for step in result["execution_steps"]], ["succeeded"] * 3)
        self.assertEqual(
            client.calls,
            [
                ("cordon_node", {"cluster_id": "cluster-001", "node_name": "cluster-001-worker-001"}),
                ("drain_node", {"cluster_id": "cluster-001", "node_name": "cluster-001-worker-001"}),
                ("delete_node", {"cluster_id": "cluster-001", "node_name": "cluster-001-worker-001"}),
            ],
        )

    async def test_unmet_dependency_blocks_without_calling_mcp(self):
        plan = delete_plan(steps=[
            {"id": "cordon_node", "intent": "ignored", "inputs": [], "outputs": [], "depends_on": ["missing"]},
            {"id": "drain_node", "intent": "ignored", "inputs": [], "outputs": [], "depends_on": ["cordon_node"]},
            {"id": "delete_node", "intent": "ignored", "inputs": [], "outputs": [], "depends_on": ["drain_node"]},
        ])
        client = FakeMCPClient()
        result = await ExecutorNodes(client).execute_plan({"validated_plan": plan})

        self.assertFalse(result["execution_result"]["success"])
        self.assertEqual(result["execution_steps"][0]["status"], "blocked")
        self.assertEqual(client.calls, [])

    async def test_mcp_failure_preserves_prior_success_and_stops_later_calls(self):
        client = FakeMCPClient(failures={"drain_node"})
        result = await ExecutorNodes(client).execute_plan({"validated_plan": delete_plan()})

        self.assertFalse(result["execution_result"]["success"])
        self.assertEqual([step["status"] for step in result["execution_steps"]], ["succeeded", "failed"])
        self.assertEqual([call[0] for call in client.calls], ["cordon_node", "drain_node"])

    async def test_mcp_exception_stops_later_calls(self):
        client = FakeMCPClient(exception_for="drain_node")
        result = await ExecutorNodes(client).execute_plan({"validated_plan": delete_plan()})

        self.assertFalse(result["execution_result"]["success"])
        self.assertEqual(result["execution_steps"][-1]["status"], "failed")
        self.assertEqual([call[0] for call in client.calls], ["cordon_node", "drain_node"])

    async def test_unregistered_step_never_invokes_mcp(self):
        client = FakeMCPClient()
        result = await ExecutorNodes(client).execute_plan({"validated_plan": delete_plan(steps=[
            {"id": "cordon_node", "intent": "ignored", "inputs": [], "outputs": [], "depends_on": []},
            {"id": "arbitrary_tool", "intent": "unsafe", "inputs": [], "outputs": [], "depends_on": ["cordon_node"]},
            {"id": "delete_node", "intent": "ignored", "inputs": [], "outputs": [], "depends_on": ["arbitrary_tool"]},
        ])})

        self.assertFalse(result["execution_result"]["success"])
        self.assertEqual(client.calls, [])

    async def test_executor_stream_and_logs_are_trace_correlated(self):
        client = FakeMCPClient()
        agent = ExecutorAgent(ExecutorGraph(ExecutorNodes(client)).graph)
        with tempfile.TemporaryDirectory() as directory, patch.dict(
            "os.environ", {"OCP_AGENT_LOG_FILE": str(Path(directory) / "agent-runtime.log")}, clear=False
        ):
            events = [event async for event in agent.stream({"trace_id": "executor-trace", "user_query": "delete", "validated_plan": delete_plan()})]
            records = [json.loads(line) for line in (Path(directory) / "executor.log").read_text().splitlines()]

        self.assertTrue(any(event.get("agent") == "executor" and event.get("phase") == "plan_execution" for event in events))
        self.assertTrue(all(record["trace_id"] == "executor-trace" for record in records))
        self.assertTrue(any(record["event"] == "node_completed" for record in records))


class RouterExecutorTransitionTests(unittest.TestCase):
    def test_router_registers_executor_and_selects_it_for_validated_delete_plan(self):
        class Nodes:
            async def route(self, _state):
                return {"agent": "plan", "action": "delete", "resources": ["node"]}

            def capability_check(self, _state):
                return {"supported": True}

            def unsupported(self, _state):
                raise AssertionError("must not be unsupported")

        class Agent:
            async def invoke(self, state):
                return state

        graph = RouterGraph(Nodes(), Agent(), Agent(), Agent(), Agent()).graph

        self.assertIn("executor_agent", graph.get_graph().nodes)
        self.assertEqual(RouterGraph.plan_next({"validated_plan": delete_plan()}), "execute")

    def test_router_does_not_dispatch_absent_or_non_delete_plan(self):
        self.assertEqual(RouterGraph.plan_next({}), "end")
        self.assertEqual(RouterGraph.plan_next({"validated_plan": {"operation": "node.add"}}), "end")
