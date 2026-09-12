import hashlib
import json
import os
import subprocess
from functools import lru_cache
from pathlib import Path
from typing import cast

from langchain_core.messages import HumanMessage, SystemMessage

from app.config.llm import plan_llm
from app.models.agent_state import ValidatedDeleteNodePlan, ValidatedDeleteNodePlanStep
from app.models.plan import ExecutionMethod, Plan
from app.observability import await_llm, emit_answer_chunk, emit_progress

from .prompts import PLAN_PROMPT
from .skill_llm_diagnostic import build_messages as build_delete_node_messages
from .skills import SkillDefinition, SkillRegistry, SkillResolutionError


class InvalidPlanError(ValueError):
    pass


class PlanNodes:
    def __init__(
        self,
        planner_llm=None,
        skill_registry: SkillRegistry | None = None,
        *,
        validate_plan_schema: bool = True,
        validate_raw_llm_schema: bool = False,
    ):
        self.planner_llm = planner_llm or plan_llm
        self.skill_registry = skill_registry or SkillRegistry()
        self.validate_plan_schema = validate_plan_schema
        self.validate_raw_llm_schema = validate_raw_llm_schema

    async def create_plan(self, state):
        emit_progress("plan", "create_plan", "plan_generation", "started", "正在生成计划。", state=state)
        resources = state.get("resources") or ([state["resource"]] if state.get("resource") else [])
        try:
            definition, skill_contract = self.skill_registry.resolve(
                state.get("action", ""), resources
            )
            plan_input_values = self._plan_input_values(state, definition)
            messages = (
                build_delete_node_messages(
                    plan_input_values["cluster_id"],
                    plan_input_values["node_name"],
                    skill_registry=self.skill_registry,
                )
                if definition.name == "ocp-node-delete"
                else [
                    SystemMessage(content=PLAN_PROMPT),
                    HumanMessage(
                        content=self._planning_request(
                            state, definition, skill_contract, plan_input_values
                        )
                    ),
                ]
            )
            result = await await_llm(
                lambda: self.planner_llm.ainvoke(messages),
                agent="plan",
                node="create_plan",
                state=state,
                invocation_metadata=self._invocation_metadata(messages),
            )
            if definition.name == "ocp-node-delete" and self.validate_plan_schema:
                output = self._raw_llm_output(result)
                response = self._json_object(output)
                self._validate_skill_response_keys(response, definition, skill_contract)
                validated_plan = self._validated_plan_projection(response, definition)
                emit_progress(
                    "plan", "create_plan", "schema_validation", "completed",
                    "Schema validation succeeded.", state=state,
                )
                emit_answer_chunk("plan", "create_plan", output, state=state)
                emit_progress("plan", "create_plan", "plan_generation", "completed", "计划生成完成。", state=state)
                return {
                    "plan": None,
                    "plan_input_values": plan_input_values,
                    "plan_llm_output": output,
                    "validated_plan": validated_plan,
                    "answer": output,
                }
            if not self.validate_plan_schema:
                output = self._raw_llm_output(result)
                emit_answer_chunk("plan", "create_plan", output, state=state)
                emit_progress("plan", "create_plan", "plan_generation", "completed", "计划生成完成。", state=state)
                return {
                    "plan": None,
                    "plan_input_values": plan_input_values,
                    "plan_llm_output": output,
                    "answer": output,
                }
            plan = self._parse_plan(result)
            if self.validate_raw_llm_schema:
                self._validate_raw_plan(plan, definition)
            plan = self._complete_plan(plan, definition, plan_input_values)
            self._validate(plan, definition, resources, state.get("action", ""), plan_input_values)
        except (SkillResolutionError, InvalidPlanError, ValueError) as error:
            emit_progress("plan", "create_plan", "plan_generation", "failed", "计划生成失败。", state=state)
            return {"supported": False, "plan": None, "answer": str(error)}
        except Exception:
            emit_progress("plan", "create_plan", "plan_generation", "failed", "计划生成失败。", state=state)
            return {
                "supported": False,
                "plan": None,
                "answer": "Unable to generate a valid plan for this request.",
            }

        emit_progress("plan", "create_plan", "plan_generation", "completed", "计划生成完成。", state=state)
        return {"plan": plan, "plan_input_values": plan_input_values}

    @staticmethod
    def _raw_llm_output(result) -> str:
        content = getattr(result, "content", result)
        if not isinstance(content, str):
            raise InvalidPlanError("The LLM returned non-text plan content.")
        return content

    @staticmethod
    def _parse_plan(raw_plan) -> Plan:
        if isinstance(raw_plan, Plan):
            return raw_plan

        content = PlanNodes._raw_llm_output(raw_plan)
        payload = PlanNodes._json_object(content)
        try:
            return Plan.model_validate(payload)
        except ValueError as error:
            raise InvalidPlanError(f"The LLM returned an invalid plan JSON object: {error}") from error

    def _validate_skill_response_keys(
        self, response: dict, definition: SkillDefinition, skill_contract: str
    ) -> None:
        output_schema = self.skill_registry.output_schema(skill_contract)
        required_root_keys = output_schema.get("required", [])
        if not isinstance(required_root_keys, list) or not all(
            isinstance(key, str) for key in required_root_keys
        ):
            raise InvalidPlanError("The registered skill output schema has invalid required keys.")
        missing_root_keys = [key for key in required_root_keys if key not in response]
        if missing_root_keys:
            raise InvalidPlanError(
                f"The LLM response is missing required skill keys: {', '.join(missing_root_keys)}."
            )

        step_schema = (
            output_schema.get("properties", {})
            .get("steps", {})
            .get("items", {})
        )
        required_step_keys = step_schema.get("required", []) if isinstance(step_schema, dict) else []
        if not isinstance(required_step_keys, list) or not all(
            isinstance(key, str) for key in required_step_keys
        ):
            raise InvalidPlanError("The registered skill output schema has invalid step required keys.")

        response_steps = response.get("steps")
        if not isinstance(response_steps, list):
            raise InvalidPlanError("The LLM response is missing declared procedure steps.")
        for step_id in definition.procedure_step_ids:
            matched_step = next(
                (
                    step for step in response_steps
                    if isinstance(step, dict) and step.get("id") == step_id
                ),
                None,
            )
            if matched_step is None:
                raise InvalidPlanError(f"The LLM response is missing declared procedure step: {step_id}.")
            missing_step_keys = [key for key in required_step_keys if key not in matched_step]
            if missing_step_keys:
                raise InvalidPlanError(
                    f"The LLM response step {step_id} is missing required skill keys: "
                    f"{', '.join(missing_step_keys)}."
                )

    @staticmethod
    def _validated_plan_projection(
        response: dict, definition: SkillDefinition
    ) -> ValidatedDeleteNodePlan:
        steps_by_id = {
            step["id"]: step
            for step in response["steps"]
            if isinstance(step, dict) and step.get("id") in definition.procedure_step_ids
        }
        steps = [
            cast(ValidatedDeleteNodePlanStep, {
                "id": steps_by_id[step_id]["id"],
                "intent": steps_by_id[step_id]["intent"],
                "inputs": steps_by_id[step_id]["inputs"],
                "outputs": steps_by_id[step_id]["outputs"],
                "depends_on": steps_by_id[step_id]["depends_on"],
            })
            for step_id in definition.procedure_step_ids
        ]
        return cast(ValidatedDeleteNodePlan, {
            "operation": response["operation"],
            "cluster_id": response["cluster_id"],
            "node_name": response["node_name"],
            "steps": steps,
        })

    @staticmethod
    def _json_object(content: str) -> dict:
        text = content.strip()
        if text.startswith("```") and text.endswith("```"):
            parts = text.split("\n", 1)
            if len(parts) != 2:
                raise InvalidPlanError("The LLM response is not valid JSON.")
            text = parts[1].rsplit("\n", 1)[0].strip()
        try:
            payload = json.loads(text)
        except json.JSONDecodeError as error:
            raise InvalidPlanError("The LLM response is not valid JSON.") from error
        if not isinstance(payload, dict):
            raise InvalidPlanError("The LLM response JSON must be an object.")
        return payload

    def _invocation_metadata(self, messages) -> dict[str, object]:
        prompt = "\n".join(str(message.content) for message in messages)
        extra_body = getattr(self.planner_llm, "extra_body", {})
        return {
            "request_format": "plain_json",
            "prompt_sha256": hashlib.sha256(prompt.encode("utf-8")).hexdigest(),
            "model": getattr(self.planner_llm, "model_name", None),
            "max_tokens": getattr(self.planner_llm, "max_tokens", None),
            "think": extra_body.get("think") if isinstance(extra_body, dict) else None,
            "code_revision": _code_revision(),
        }

    @staticmethod
    def _validate_raw_plan(plan: Plan, definition: SkillDefinition) -> None:
        if definition.name != "ocp-node-delete":
            return
        required_plan_fields = {
            "plan_id", "status", "skill", "action", "resources", "required_inputs",
            "write_only_inputs", "final_outputs", "target", "parameters",
            "final_output_mappings", "steps",
        }
        missing = required_plan_fields - plan.model_fields_set
        if missing:
            raise InvalidPlanError(f"LLM plan is missing required schema fields: {', '.join(sorted(missing))}.")
        required_step_fields = {
            "id", "skill", "description", "inputs", "outputs", "depends_on",
            "method", "input_bindings", "output_mappings",
        }
        for step in plan.steps:
            missing = required_step_fields - step.model_fields_set
            if missing:
                raise InvalidPlanError(f"LLM plan step {step.id} is missing required schema fields: {', '.join(sorted(missing))}.")

    @staticmethod
    def _complete_plan(plan: Plan, definition: SkillDefinition, values: dict[str, str]) -> Plan:
        if definition.name != "ocp-node-delete":
            return plan
        steps = []
        for step, contract in zip(plan.steps, definition.step_interfaces, strict=True):
            bindings = {
                name: (
                    f"$.target.{name}" if name in values else "$.parameters.drain.force"
                    if name == "drain.force" else f"$.steps.{contract.depends_on[-1]}.outputs.{name}"
                )
                for name in contract.inputs
            }
            steps.append(step.model_copy(update={
                "method": ExecutionMethod(type="mcp", name=contract.id),
                "input_bindings": bindings,
                "output_mappings": {name: f"$.steps.{contract.id}.outputs.{name}" for name in contract.outputs},
            }))
        return plan.model_copy(update={
            "target": values,
            "parameters": {"drain": {"force": True}},
            "steps": steps,
            "final_output_mappings": {"node_deleted": "$.steps.delete_node.outputs.node_deleted"},
        })

    @staticmethod
    def _plan_input_values(state, definition: SkillDefinition) -> dict[str, str]:
        if definition.name != "ocp-node-delete":
            return {}
        values = {
            "cluster_id": state.get("current_work_cluster") or state.get("cluster_id", ""),
            "node_name": state.get("current_work_node") or state.get("node_name", ""),
        }
        missing = [name for name, value in values.items() if not value]
        if missing:
            raise InvalidPlanError(
                f"Node deletion planning requires routed values for: {', '.join(missing)}."
            )
        return values

    @staticmethod
    def _planning_request(
        state, definition: SkillDefinition, skill_contract: str, plan_input_values: dict[str, str]
    ) -> str:
        return "\n".join(
            (
                f"Action: {state.get('action', '')}",
                f"Resources: {state.get('resources') or [state.get('resource', '')]}",
                f"Skill: {definition.name}",
                f"Required inputs: {list(definition.required_inputs)}",
                f"Write-only inputs: {list(definition.write_only_inputs)}",
                f"Final outputs: {list(definition.final_outputs)}",
                f"Procedure step ids: {list(definition.procedure_step_ids)}",
                f"Bound input values: {plan_input_values}",
                "Local skill contract:\n" + skill_contract,
            )
        )

    @staticmethod
    def _validate(
        plan: Plan,
        definition: SkillDefinition,
        resources: list[str],
        action: str, values: dict[str, str],
    ) -> None:
        if plan.skill != definition.name or plan.action != action or plan.resources != resources:
            raise InvalidPlanError("The generated plan does not match the routed skill request.")
        if tuple(plan.required_inputs) != definition.required_inputs:
            raise InvalidPlanError("The generated plan does not preserve required skill inputs.")
        if tuple(plan.write_only_inputs) != definition.write_only_inputs:
            raise InvalidPlanError("The generated plan does not preserve write-only inputs.")
        if tuple(plan.final_outputs) != definition.final_outputs:
            raise InvalidPlanError("The generated plan does not preserve skill outputs.")

        ids = [step.id for step in plan.steps]
        if tuple(ids) != definition.procedure_step_ids or len(ids) != len(set(ids)):
            raise InvalidPlanError("The generated plan does not preserve the skill procedure.")

        known_ids = set()
        for index, step in enumerate(plan.steps):
            if step.skill != definition.name:
                raise InvalidPlanError("A plan step references an unexpected skill.")
            if any(dependency not in known_ids for dependency in step.depends_on):
                raise InvalidPlanError("Plan dependencies must reference earlier steps.")
            if definition.step_interfaces:
                expected = definition.step_interfaces[index]
                if (
                    tuple(step.inputs) != expected.inputs
                    or tuple(step.outputs) != expected.outputs
                    or tuple(step.depends_on) != expected.depends_on
                ):
                    raise InvalidPlanError("The generated plan does not preserve skill step interfaces.")
            known_ids.add(step.id)
        if definition.name == "ocp-node-delete":
            if plan.target != values or plan.parameters != {"drain": {"force": True}}:
                raise InvalidPlanError("The generated plan does not preserve delete target parameters.")
            if any(step.method != ExecutionMethod(type="mcp", name=step.id) for step in plan.steps):
                raise InvalidPlanError("The generated plan does not preserve execution methods.")


@lru_cache(maxsize=1)
def _code_revision() -> str:
    configured = os.getenv("OCP_AGENT_CODE_REVISION")
    if configured:
        return configured
    try:
        result = subprocess.run(
            ["git", "rev-parse", "HEAD"],
            cwd=Path(__file__).resolve().parents[4],
            capture_output=True,
            check=True,
            text=True,
            timeout=0.25,
        )
        return result.stdout.strip()
    except (OSError, subprocess.SubprocessError):
        return "unavailable"
