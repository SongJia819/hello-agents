import asyncio
import json
import unittest
from uuid import uuid4
from unittest.mock import call, patch

from app.agents.plan.nodes import PlanNodes
from app.agents.plan.skill_llm_diagnostic import build_messages
from app.agents.plan.skills import NODE_ADD_SKILL, OCP_NODE_DELETE_SKILL
from app.agents.router.graph import RouterGraph
from app.agents.router.nodes import RouterNodes
from app.models.plan import Plan, PlanStep
from app.models.router import RouterResult


class FakeStructuredLLM:
    def __init__(self, result):
        self.result = result
        self.calls = []

    async def ainvoke(self, messages):
        self.calls.append(messages)
        return self.result


class FakeTextLLM(FakeStructuredLLM):
    def __init__(self, result):
        super().__init__(type("LLMResponse", (), {"content": result})())


class FakeDeleteRouterLLM:
    async def ainvoke(self, _messages):
        return RouterResult(
            agent="plan", action="delete", resources=["node"],
            current_work_cluster="cluster-001", current_work_node="worker-001",
        )


def valid_node_add_plan():
    steps = []
    previous_step = None
    for step_id in NODE_ADD_SKILL.procedure_step_ids:
        steps.append(
            PlanStep(
                id=step_id,
                skill=NODE_ADD_SKILL.name,
                description=f"Run {step_id}.",
                inputs=[] if previous_step is None else [f"{previous_step}.result"],
                outputs=[f"{step_id}.result"],
                depends_on=[] if previous_step is None else [previous_step],
            )
        )
        previous_step = step_id

    return Plan(
        skill=NODE_ADD_SKILL.name,
        action=NODE_ADD_SKILL.action,
        resources=list(NODE_ADD_SKILL.resources),
        required_inputs=list(NODE_ADD_SKILL.required_inputs),
        write_only_inputs=list(NODE_ADD_SKILL.write_only_inputs),
        final_outputs=list(NODE_ADD_SKILL.final_outputs),
        steps=steps,
    )


def valid_node_delete_plan():
    steps = [
        PlanStep(
            id=step.id,
            skill=OCP_NODE_DELETE_SKILL.name,
            description=f"Plan {step.id} without executing it.",
            inputs=list(step.inputs), outputs=list(step.outputs), depends_on=list(step.depends_on),
            method={"type": "mcp", "name": step.id},
            input_bindings={name: f"$.input.{name}" for name in step.inputs},
            output_mappings={name: f"$.output.{name}" for name in step.outputs},
        )
        for step in OCP_NODE_DELETE_SKILL.step_interfaces
    ]
    return Plan(
        skill=OCP_NODE_DELETE_SKILL.name,
        plan_id=str(uuid4()), status="planned",
        action=OCP_NODE_DELETE_SKILL.action,
        resources=list(OCP_NODE_DELETE_SKILL.resources),
        required_inputs=list(OCP_NODE_DELETE_SKILL.required_inputs),
        write_only_inputs=list(OCP_NODE_DELETE_SKILL.write_only_inputs),
        final_outputs=list(OCP_NODE_DELETE_SKILL.final_outputs),
        target={"cluster_id": "cluster-001", "node_name": "worker-002"},
        parameters={"drain": {"force": True}},
        final_output_mappings={"node_deleted": "$.steps.delete_node.outputs.node_deleted"},
        steps=steps,
    )


def valid_node_delete_response():
    return {
        "operation": "node.delete",
        "cluster_id": "cluster-001",
        "node_name": "cluster-001-worker-001",
        "steps": [
            {
                "id": "cordon_node",
                "intent": "oc adm cordon <node_name>",
                "inputs": ["cluster_id", "node_name"],
                "outputs": ["node_unschedulable"],
                "depends_on": [],
            },
            {
                "id": "drain_node",
                "intent": "oc adm drain <node_name> --force=true",
                "inputs": ["cluster_id", "node_name", "node_unschedulable"],
                "outputs": ["pods_drained"],
                "depends_on": ["cordon_node"],
            },
            {
                "id": "delete_node",
                "intent": "oc delete node <node_name>",
                "inputs": ["cluster_id", "node_name", "pods_drained"],
                "outputs": ["node_deleted"],
                "depends_on": ["drain_node"],
            },
        ],
    }


class FakeDriftedDeleteRouterLLM:
    async def ainvoke(self, _messages):
        return RouterResult(
            agent="plan", action="delete", resources=["cluster-001-worker-001"],
            current_work_cluster="cluster-001", current_work_node="worker-001",
        )


class FakeNodeStore:
    def list_clusters(self):
        return [type("Cluster", (), {"cluster_id": "cluster-001"})()]

    def list_nodes(self, _cluster_id):
        return [type("Node", (), {
            "name": "cluster-001-worker-001", "cluster_id": "cluster-001",
        })()]


class PlanNodeTests(unittest.IsolatedAsyncioTestCase):
    def test_delete_node_skill_uses_the_compact_contract(self):
        self.assertEqual(
            OCP_NODE_DELETE_SKILL.final_outputs,
            ("operation", "cluster_id", "node_name", "steps"),
        )
        self.assertEqual(
            OCP_NODE_DELETE_SKILL.step_interfaces[1].inputs,
            ("cluster_id", "node_name", "node_unschedulable"),
        )

    async def test_default_plan_client_does_not_enable_provider_structured_output(self):
        with patch("app.agents.plan.nodes.plan_llm") as plain_llm:
            nodes = PlanNodes()

        self.assertIs(nodes.planner_llm, plain_llm)
        plain_llm.with_structured_output.assert_not_called()

    def test_plan_invocation_metadata_is_compact_and_does_not_include_prompt_text(self):
        fake_llm = type("LLM", (), {"model_name": "local", "max_tokens": 4096, "extra_body": {"think": False}})()
        metadata = PlanNodes(planner_llm=fake_llm)._invocation_metadata(build_messages := [
            type("Message", (), {"content": "system prompt"})(),
            type("Message", (), {"content": "user prompt"})(),
        ])

        self.assertEqual(metadata["request_format"], "plain_json")
        self.assertEqual(metadata["model"], "local")
        self.assertEqual(metadata["max_tokens"], 4096)
        self.assertFalse(metadata["think"])
        self.assertNotIn("system prompt", str(metadata))
        self.assertEqual(len(metadata["prompt_sha256"]), 64)

    async def test_node_add_plan_is_structured_and_does_not_expose_password(self):
        fake_llm = FakeStructuredLLM(valid_node_add_plan())
        result = await PlanNodes(planner_llm=fake_llm, validate_plan_schema=True).create_plan(
            {
                "action": "add",
                "resources": ["node"],
                "password": "do-not-expose-this",
            }
        )

        plan = result["plan"]
        self.assertEqual(plan.skill, "node-add")
        self.assertEqual(plan.steps[-1].id, "mark_ready")
        self.assertEqual(plan.steps[1].depends_on, ["validate_input"])
        self.assertIn("node.password", plan.write_only_inputs)
        self.assertNotIn("do-not-expose-this", str(plan.model_dump()))
        self.assertEqual(len(fake_llm.calls), 1)

    async def test_node_delete_plan_uses_llm_without_execution(self):
        response = valid_node_delete_response()
        fake_llm = FakeTextLLM(json.dumps(response))
        state = {
            "action": "delete", "resources": ["node"],
            "current_work_cluster": "cluster-001", "current_work_node": "cluster-001-worker-002",
        }
        with patch("app.agents.plan.nodes.emit_progress") as emit_progress:
            result = await PlanNodes(planner_llm=fake_llm).create_plan(state)

        self.assertIsNone(result["plan"])
        self.assertEqual(result["plan_llm_output"], json.dumps(response))
        self.assertEqual(result["answer"], json.dumps(response))
        self.assertEqual(result["validated_plan"], response)
        self.assertEqual(result["plan_input_values"], {"cluster_id": "cluster-001", "node_name": "cluster-001-worker-002"})
        self.assertIn(
            call(
                "plan", "create_plan", "schema_validation", "completed",
                "Schema validation succeeded.", state=state,
            ),
            emit_progress.call_args_list,
        )
        self.assertEqual(len(fake_llm.calls), 1)
        self.assertEqual(
            [message.content for message in fake_llm.calls[0]],
            [message.content for message in build_messages("cluster-001", "cluster-001-worker-002")],
        )

    async def test_skill_shaped_json_with_extra_keys_and_noncanonical_values_is_accepted(self):
        response = valid_node_delete_response()
        response["extra"] = {"any": "value"}
        response["success"] = "extra non-schema value"
        response["steps"] = list(reversed(response["steps"]))
        raw_json = "```json\n" + json.dumps(response) + "\n```"
        fake_llm = FakeTextLLM(raw_json)
        result = await PlanNodes(planner_llm=fake_llm).create_plan(
            {"action": "delete", "resources": ["node"], "current_work_cluster": "cluster-001", "current_work_node": "cluster-001-worker-002"}
        )

        self.assertIsNone(result["plan"])
        self.assertEqual(result["answer"], raw_json)
        self.assertEqual(len(fake_llm.calls), 1)

    async def test_schema_validation_is_disabled_and_raw_llm_output_is_returned(self):
        state = {
            "action": "delete", "resources": ["node"], "current_work_cluster": "cluster-001",
            "current_work_node": "cluster-001-worker-002", "trace_id": "test-raw-plan-output",
        }
        with patch("app.agents.plan.nodes.emit_answer_chunk") as emit_chunk:
            result = await PlanNodes(
                planner_llm=FakeTextLLM("not JSON"), validate_plan_schema=False
            ).create_plan(state)

        self.assertIsNone(result["plan"])
        self.assertEqual(result["plan_llm_output"], "not JSON")
        self.assertEqual(result["answer"], "not JSON")
        emit_chunk.assert_called_once_with("plan", "create_plan", "not JSON", state=state)

    async def test_schema_validation_rejects_invalid_llm_json_when_enabled(self):
        result = await PlanNodes(
            planner_llm=FakeTextLLM("not JSON"), validate_plan_schema=True
        ).create_plan(
            {"action": "delete", "resources": ["node"], "current_work_cluster": "cluster-001", "current_work_node": "cluster-001-worker-002"}
        )

        self.assertFalse(result["supported"])
        self.assertIsNone(result["plan"])
        self.assertIn("not valid JSON", result["answer"])

    async def test_node_delete_without_routed_targets_does_not_invoke_llm(self):
        fake_llm = FakeStructuredLLM(valid_node_delete_plan())
        result = await PlanNodes(planner_llm=fake_llm).create_plan(
            {"action": "delete", "resources": ["node"]}
        )

        self.assertFalse(result["supported"])
        self.assertIsNone(result["plan"])
        self.assertIn("cluster_id", result["answer"])
        self.assertEqual(fake_llm.calls, [])

    async def test_schema_validation_rejects_missing_root_key(self):
        response = valid_node_delete_response()
        response.pop("operation")
        with patch("app.agents.plan.nodes.emit_progress") as emit_progress:
            result = await PlanNodes(planner_llm=FakeTextLLM(json.dumps(response))).create_plan(
                {"action": "delete", "resources": ["node"], "current_work_cluster": "cluster-001", "current_work_node": "cluster-001-worker-002"}
            )
        self.assertFalse(result["supported"])
        self.assertIn("operation", result["answer"])
        self.assertFalse(any(
            progress.args[2] == "schema_validation" and progress.args[3] == "completed"
            for progress in emit_progress.call_args_list
        ))

    async def test_schema_validation_rejects_missing_step_key(self):
        response = valid_node_delete_response()
        response["steps"][1].pop("intent")
        result = await PlanNodes(planner_llm=FakeTextLLM(json.dumps(response))).create_plan(
            {"action": "delete", "resources": ["node"], "current_work_cluster": "cluster-001", "current_work_node": "cluster-001-worker-002"}
        )
        self.assertFalse(result["supported"])
        self.assertIsNone(result["plan"])
        self.assertIn("drain_node", result["answer"])
        self.assertIn("intent", result["answer"])

    def test_plan_schema_rejects_unknown_fields_and_wrong_types(self):
        payload = valid_node_delete_plan().model_dump()
        with self.assertRaises(Exception):
            Plan.model_validate({**payload, "unexpected": True}, strict=True)
        with self.assertRaises(Exception):
            Plan.model_validate({**payload, "target": {"cluster_id": 1, "node_name": "worker-002"}}, strict=True)

    async def test_schema_validation_rejects_missing_declared_step(self):
        response = valid_node_delete_response()
        response["steps"] = response["steps"][:2]
        result = await PlanNodes(planner_llm=FakeTextLLM(json.dumps(response))).create_plan(
            {"action": "delete", "resources": ["node"], "current_work_cluster": "cluster-001", "current_work_node": "cluster-001-worker-001"}
        )

        self.assertFalse(result["supported"])
        self.assertIsNone(result["plan"])
        self.assertIn("delete_node", result["answer"])

    async def test_multiple_node_delete_resources_do_not_invoke_llm(self):
        fake_llm = FakeStructuredLLM(valid_node_add_plan())
        result = await PlanNodes(planner_llm=fake_llm).create_plan(
            {"action": "delete", "resources": ["node", "node"]}
        )

        self.assertFalse(result["supported"])
        self.assertIsNone(result["plan"])
        self.assertEqual(fake_llm.calls, [])

    async def test_later_step_dependency_is_rejected(self):
        invalid = valid_node_add_plan()
        invalid.steps[0] = invalid.steps[0].model_copy(
            update={"depends_on": ["check_cluster"]}
        )

        result = await PlanNodes(planner_llm=FakeStructuredLLM(invalid), validate_plan_schema=True).create_plan(
            {"action": "add", "resources": ["node"]}
        )

        self.assertFalse(result["supported"])
        self.assertIsNone(result["plan"])
        self.assertIn("earlier steps", result["answer"])


class RouterPlanDispatchTests(unittest.TestCase):
    def test_delete_node_route_preserves_target_selectors(self):
        route = asyncio.run(
            RouterNodes(FakeDeleteRouterLLM(), cluster_store=FakeNodeStore()).route(
                {"user_query": "delete cluster-001-worker-001 in cluster-001"}
            )
        )

        self.assertEqual(route["agent"], "plan")
        self.assertEqual(route["action"], "delete")
        self.assertEqual(route["resources"], ["node"])
        self.assertEqual(route["current_work_cluster"], "cluster-001")
        self.assertEqual(route["current_work_node"], "cluster-001-worker-001")

    def test_delete_node_route_normalizes_drifted_resource_field(self):
        route = asyncio.run(
            RouterNodes(FakeDriftedDeleteRouterLLM(), cluster_store=FakeNodeStore()).route(
                {"user_query": "delete cluster-001-worker-001 in cluster-001"}
            )
        )
        self.assertEqual(route["resources"], ["node"])
        self.assertEqual(route["resource"], "node")
        self.assertEqual(route["current_work_cluster"], "cluster-001")
        self.assertEqual(route["current_work_node"], "cluster-001-worker-001")

    def test_delete_node_route_rejects_unmatched_target(self):
        store = type("Store", (), {
            "list_clusters": lambda _self: [type("Cluster", (), {"cluster_id": "cluster-001"})()],
            "list_nodes": lambda _self, _cluster: [],
        })()
        route = asyncio.run(
            RouterNodes(FakeDeleteRouterLLM(), cluster_store=store).route(
                {"user_query": "delete unknown in cluster-1"}
            )
        )
        result = RouterNodes.capability_check(None, route)
        self.assertFalse(result["supported"])
        self.assertIn("exactly one full node name", result["messages"])

    def test_supported_plan_route_selects_plan_agent_node(self):
        graph = RouterGraph.__new__(RouterGraph)

        self.assertEqual(
            graph.route_next({"supported": True, "agent": "plan"}), "plan"
        )

    def test_supported_knowledge_route_selects_knowledge_node(self):
        graph = RouterGraph.__new__(RouterGraph)
        self.assertEqual(
            graph.route_next({"supported": True, "agent": "knowledge"}), "knowledge"
        )


class PlanCapabilityTests(unittest.TestCase):
    def test_registered_plan_capability_is_supported(self):
        result = RouterNodes.capability_check(
            None, {"agent": "plan", "action": "add", "resources": ["node"]}
        )
        self.assertTrue(result["supported"])

    def test_node_delete_plan_capability_is_supported(self):
        result = RouterNodes.capability_check(
            None, {"agent": "plan", "action": "delete", "resources": ["node"]}
        )
        self.assertTrue(result["supported"])


class KnowledgeCapabilityTests(unittest.TestCase):
    def test_registered_knowledge_capability_is_supported(self):
        result = RouterNodes.capability_check(
            None, {"agent": "knowledge", "action": "answer", "resources": ["documentation"]}
        )
        self.assertTrue(result["supported"])

    def test_unknown_knowledge_action_is_rejected(self):
        result = RouterNodes.capability_check(
            None, {"agent": "knowledge", "action": "list", "resources": ["documentation"]}
        )
        self.assertFalse(result["supported"])

    def test_registered_direct_chat_capability_is_supported(self):
        result = RouterNodes.capability_check(
            None, {"agent": "knowledge", "action": "chat", "resources": ["conversation"]}
        )
        self.assertTrue(result["supported"])

    def test_unsupported_direct_chat_resource_is_rejected(self):
        result = RouterNodes.capability_check(
            None, {"agent": "knowledge", "action": "chat", "resources": ["node"]}
        )
        self.assertFalse(result["supported"])
