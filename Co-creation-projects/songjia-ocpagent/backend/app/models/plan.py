from typing import Any, Literal
from uuid import uuid4

from pydantic import BaseModel, ConfigDict, Field


class StrictPlanModel(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)


class ExecutionMethod(StrictPlanModel):
    type: Literal["mcp"]
    name: str = Field(min_length=1)


class PlanStep(StrictPlanModel):
    """One ordered, non-executing step derived from an approved skill."""

    id: str = Field(min_length=1)
    skill: str = Field(min_length=1)
    description: str = Field(min_length=1)
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    depends_on: list[str] = Field(default_factory=list)
    method: ExecutionMethod | None = None
    input_bindings: dict[str, str] = Field(default_factory=dict)
    output_mappings: dict[str, str] = Field(default_factory=dict)


class Plan(StrictPlanModel):
    """A validated plan that can be consumed by a future execution agent."""

    skill: str = Field(min_length=1)
    plan_id: str = Field(default_factory=lambda: str(uuid4()))
    status: Literal["planned"] = "planned"
    action: str = Field(min_length=1)
    resources: list[str] = Field(min_length=1)
    required_inputs: list[str] = Field(default_factory=list)
    write_only_inputs: list[str] = Field(default_factory=list)
    final_outputs: list[str] = Field(default_factory=list)
    target: dict[str, str] = Field(default_factory=dict)
    parameters: dict[str, Any] = Field(default_factory=dict)
    final_output_mappings: dict[str, str] = Field(default_factory=dict)
    steps: list[PlanStep] = Field(min_length=1)
