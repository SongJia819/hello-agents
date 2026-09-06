from langchain_core.messages import HumanMessage, SystemMessage

from app.config.llm import llm
from app.models.plan import Plan
from app.observability import emit_progress

from .prompts import PLAN_PROMPT
from .skills import SkillDefinition, SkillRegistry, SkillResolutionError


class InvalidPlanError(ValueError):
    pass


class PlanNodes:
    def __init__(self, planner_llm=None, skill_registry: SkillRegistry | None = None):
        self.planner_llm = planner_llm or llm.with_structured_output(Plan)
        self.skill_registry = skill_registry or SkillRegistry()

    async def create_plan(self, state):
        emit_progress("plan", "create_plan", "plan_generation", "started", "正在生成计划。", state=state)
        resources = state.get("resources") or ([state["resource"]] if state.get("resource") else [])
        try:
            definition, skill_contract = self.skill_registry.resolve(
                state.get("action", ""), resources
            )
            result = await self.planner_llm.ainvoke(
                [
                    SystemMessage(content=PLAN_PROMPT),
                    HumanMessage(
                        content=self._planning_request(state, definition, skill_contract)
                    ),
                ]
            )
            plan = result if isinstance(result, Plan) else Plan.model_validate(result)
            self._validate(plan, definition, resources, state.get("action", ""))
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
        return {"plan": plan}

    @staticmethod
    def _planning_request(state, definition: SkillDefinition, skill_contract: str) -> str:
        return "\n".join(
            (
                f"Action: {state.get('action', '')}",
                f"Resources: {state.get('resources') or [state.get('resource', '')]}",
                f"Skill: {definition.name}",
                f"Required inputs: {list(definition.required_inputs)}",
                f"Write-only inputs: {list(definition.write_only_inputs)}",
                f"Final outputs: {list(definition.final_outputs)}",
                f"Procedure step ids: {list(definition.procedure_step_ids)}",
                "Local skill contract:\n" + skill_contract,
            )
        )

    @staticmethod
    def _validate(
        plan: Plan,
        definition: SkillDefinition,
        resources: list[str],
        action: str,
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
        for step in plan.steps:
            if step.skill != definition.name:
                raise InvalidPlanError("A plan step references an unexpected skill.")
            if any(dependency not in known_ids for dependency in step.depends_on):
                raise InvalidPlanError("Plan dependencies must reference earlier steps.")
            known_ids.add(step.id)
