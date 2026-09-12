"""Dependency-aware execution for the registered mock delete-node skill."""
from __future__ import annotations

import time
from typing import Any, cast

from app.models.agent_state import ExecutionStepState, PlanExecutionResult, ValidatedDeleteNodePlan
from app.models.node import NodeOperationResult
from app.observability import emit_progress


class ExecutorNodes:
    """Execute only static MCP bindings approved for `ocp-node-delete`."""

    _TOOL_BY_STEP = {
        "cordon_node": "cordon_node",
        "drain_node": "drain_node",
        "delete_node": "delete_node",
    }

    def __init__(self, mcp_client):
        self.mcp_client = mcp_client

    async def execute_plan(self, state: dict[str, Any]) -> dict[str, Any]:
        plan = state.get("validated_plan")
        if not self._is_delete_node_plan(plan):
            return self._failure(
                state, [], "The validated plan is not eligible for mock execution."
            )

        plan = cast(ValidatedDeleteNodePlan, plan)
        cluster_id, node_name = plan["cluster_id"], plan["node_name"]
        if error := self._registered_steps_error(plan["steps"]):
            return self._failure(state, [], error)
        execution_steps: list[ExecutionStepState] = []
        completed_ids: set[str] = set()

        for raw_step in plan["steps"]:
            started = time.perf_counter()
            step_id = raw_step.get("id") if isinstance(raw_step, dict) else None
            dependencies = raw_step.get("depends_on") if isinstance(raw_step, dict) else None
            if not isinstance(step_id, str) or not isinstance(dependencies, list) or not all(
                isinstance(dependency, str) for dependency in dependencies
            ):
                return self._failure(
                    state,
                    execution_steps,
                    "The validated plan contains a malformed execution step.",
                    failed_step_id=step_id if isinstance(step_id, str) else None,
                )

            unmet_dependencies = [
                dependency
                for dependency in dependencies
                if dependency == step_id or dependency not in completed_ids
            ]
            if unmet_dependencies:
                duration_ms = self._duration_ms(started)
                message = f"步骤执行被依赖阻塞：{step_id}。"
                emit_progress("executor", "execute_plan", "plan_execution", "started", f"正在执行步骤：{step_id}。", state=state)
                emit_progress("executor", "execute_plan", "plan_execution", "failed", message, state=state)
                execution_steps.append(cast(ExecutionStepState, {
                    "id": step_id,
                    "depends_on": list(dependencies),
                    "status": "blocked",
                    "error": f"Unmet dependencies: {', '.join(unmet_dependencies)}.",
                    "duration_ms": duration_ms,
                }))
                return self._failure(state, execution_steps, message, failed_step_id=step_id)

            emit_progress("executor", "execute_plan", "plan_execution", "started", f"正在执行步骤：{step_id}。", state=state)
            try:
                result = await self.mcp_client.call(
                    self._TOOL_BY_STEP[step_id], NodeOperationResult,
                    cluster_id=cluster_id, node_name=node_name,
                )
            except Exception as error:
                return self._step_failure(
                    state, execution_steps, step_id, dependencies,
                    f"Mock MCP execution failed: {type(error).__name__}.", started,
                )

            if not result.success:
                return self._step_failure(
                    state, execution_steps, step_id, dependencies,
                    result.message or "Mock MCP operation reported failure.", started,
                    result=result,
                )

            duration_ms = self._duration_ms(started)
            execution_steps.append(cast(ExecutionStepState, {
                "id": step_id,
                "depends_on": list(dependencies),
                "status": "succeeded",
                "result": result.model_dump(mode="json"),
                "duration_ms": duration_ms,
            }))
            completed_ids.add(step_id)
            emit_progress("executor", "execute_plan", "plan_execution", "completed", f"步骤执行成功：{step_id}。", state=state)

        message = "整个计划执行成功。"
        emit_progress("executor", "execute_plan", "plan_execution", "completed", message, state=state)
        execution_result = cast(PlanExecutionResult, {
            "success": True,
            "status": "completed",
            "operation": plan["operation"],
            "cluster_id": cluster_id,
            "node_name": node_name,
            "completed_step_ids": [step["id"] for step in execution_steps],
            "message": message,
        })
        return {
            "execution_steps": execution_steps,
            "execution_result": execution_result,
            "tool_result": execution_result,
            "answer": message,
        }

    @staticmethod
    def _is_delete_node_plan(plan: Any) -> bool:
        return (
            isinstance(plan, dict)
            and plan.get("operation") == "node.delete"
            and isinstance(plan.get("cluster_id"), str)
            and isinstance(plan.get("node_name"), str)
            and isinstance(plan.get("steps"), list)
        )

    def _registered_steps_error(self, steps: list[Any]) -> str | None:
        """Reject unknown/duplicate/missing step IDs before any mock mutation."""
        step_ids = [step.get("id") if isinstance(step, dict) else None for step in steps]
        expected_ids = set(self._TOOL_BY_STEP)
        if (
            len(step_ids) != len(expected_ids)
            or not all(isinstance(step_id, str) for step_id in step_ids)
            or set(step_ids) != expected_ids
        ):
            return "The validated plan does not contain exactly the registered execution steps."
        return None

    def _step_failure(
        self,
        state: dict[str, Any],
        execution_steps: list[ExecutionStepState],
        step_id: str,
        dependencies: list[str],
        error: str,
        started: float,
        *,
        result: NodeOperationResult | None = None,
    ) -> dict[str, Any]:
        message = f"步骤执行失败：{step_id}。"
        step: ExecutionStepState = {
            "id": step_id,
            "depends_on": list(dependencies),
            "status": "failed",
            "error": error,
            "duration_ms": self._duration_ms(started),
        }
        if result is not None:
            step["result"] = result.model_dump(mode="json")
        execution_steps.append(step)
        emit_progress("executor", "execute_plan", "plan_execution", "failed", message, state=state)
        return self._failure(state, execution_steps, message, failed_step_id=step_id)

    def _failure(
        self,
        state: dict[str, Any],
        execution_steps: list[ExecutionStepState],
        message: str,
        *,
        failed_step_id: str | None = None,
    ) -> dict[str, Any]:
        plan = state.get("validated_plan") if isinstance(state.get("validated_plan"), dict) else {}
        execution_result: PlanExecutionResult = {
            "success": False,
            "status": "failed",
            "operation": str(plan.get("operation", "node.delete")),
            "cluster_id": str(plan.get("cluster_id", "")),
            "node_name": str(plan.get("node_name", "")),
            "completed_step_ids": [step["id"] for step in execution_steps if step["status"] == "succeeded"],
            "message": f"计划执行失败。{message}",
        }
        if failed_step_id is not None:
            execution_result["failed_step_id"] = failed_step_id
        emit_progress("executor", "execute_plan", "plan_execution", "failed", execution_result["message"], state=state)
        return {
            "execution_steps": execution_steps,
            "execution_result": execution_result,
            "tool_result": execution_result,
            "answer": execution_result["message"],
        }

    @staticmethod
    def _duration_ms(started: float) -> float:
        return max(0.0, round((time.perf_counter() - started) * 1000, 3))
