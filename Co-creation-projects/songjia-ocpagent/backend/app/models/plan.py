from pydantic import BaseModel, Field


class PlanStep(BaseModel):
    """One ordered, non-executing step derived from an approved skill."""

    id: str = Field(min_length=1)
    skill: str = Field(min_length=1)
    description: str = Field(min_length=1)
    inputs: list[str] = Field(default_factory=list)
    outputs: list[str] = Field(default_factory=list)
    depends_on: list[str] = Field(default_factory=list)


class Plan(BaseModel):
    """A validated plan that can be consumed by a future execution agent."""

    skill: str = Field(min_length=1)
    action: str = Field(min_length=1)
    resources: list[str] = Field(min_length=1)
    required_inputs: list[str] = Field(default_factory=list)
    write_only_inputs: list[str] = Field(default_factory=list)
    final_outputs: list[str] = Field(default_factory=list)
    steps: list[PlanStep] = Field(min_length=1)
