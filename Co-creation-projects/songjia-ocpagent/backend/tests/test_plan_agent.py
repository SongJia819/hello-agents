import unittest

from app.agents.plan.nodes import PlanNodes
from app.agents.plan.skills import NODE_ADD_SKILL, OCP_NODE_DELETE_SKILL
from app.agents.router.graph import RouterGraph
from app.agents.router.nodes import RouterNodes
from app.models.plan import Plan, PlanStep


class FakeStructuredLLM:
    def __init__(self, result):
        self.result = result
        self.calls = []

    async def ainvoke(self, messages):
        self.calls.append(messages)
        return self.result


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
            inputs=list(step.inputs),
            outputs=list(step.outputs),
            depends_on=list(step.depends_on),
        )
        for step in OCP_NODE_DELETE_SKILL.step_interfaces
    ]
    return Plan(
        skill=OCP_NODE_DELETE_SKILL.name,
        action=OCP_NODE_DELETE_SKILL.action,
        resources=list(OCP_NODE_DELETE_SKILL.resources),
        required_inputs=list(OCP_NODE_DELETE_SKILL.required_inputs),
        write_only_inputs=list(OCP_NODE_DELETE_SKILL.write_only_inputs),
        final_outputs=list(OCP_NODE_DELETE_SKILL.final_outputs),
        steps=steps,
    )


class PlanNodeTests(unittest.IsolatedAsyncioTestCase):
    async def test_node_add_plan_is_structured_and_does_not_expose_password(self):
        fake_llm = FakeStructuredLLM(valid_node_add_plan())
        result = await PlanNodes(planner_llm=fake_llm).create_plan(
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

    async def test_node_delete_plan_preserves_schema_interfaces_without_execution(self):
        fake_llm = FakeStructuredLLM(valid_node_delete_plan())
        result = await PlanNodes(planner_llm=fake_llm).create_plan(
            {"action": "delete", "resources": ["node"], "cluster_id": "cluster-001", "node_name": "worker-002"}
        )

        plan = result["plan"]
        self.assertEqual(plan.skill, "ocp-node-delete")
        self.assertEqual([step.id for step in plan.steps], ["cordon_node", "drain_node", "delete_node"])
        self.assertEqual(plan.steps[0].inputs, ["cluster_id", "node_name"])
        self.assertEqual(plan.steps[1].depends_on, ["cordon_node"])
        self.assertEqual(plan.steps[1].inputs[-1], "drain.force")
        self.assertEqual(plan.steps[2].outputs, ["node_deleted"])
        self.assertEqual(len(fake_llm.calls), 1)

    async def test_node_delete_step_interface_change_is_rejected(self):
        invalid = valid_node_delete_plan()
        invalid.steps[1] = invalid.steps[1].model_copy(update={"depends_on": []})

        result = await PlanNodes(planner_llm=FakeStructuredLLM(invalid)).create_plan(
            {"action": "delete", "resources": ["node"]}
        )

        self.assertFalse(result["supported"])
        self.assertIsNone(result["plan"])
        self.assertIn("step interfaces", result["answer"])

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

        result = await PlanNodes(planner_llm=FakeStructuredLLM(invalid)).create_plan(
            {"action": "add", "resources": ["node"]}
        )

        self.assertFalse(result["supported"])
        self.assertIsNone(result["plan"])
        self.assertIn("earlier steps", result["answer"])


class RouterPlanDispatchTests(unittest.TestCase):
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
