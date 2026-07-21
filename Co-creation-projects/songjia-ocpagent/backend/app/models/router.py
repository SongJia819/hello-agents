from pydantic import BaseModel, Field


class RouterResult(BaseModel):
    agent: str = Field(
        description="Target agent. One of: query, planner, execution"
    )

    action: str = Field(
        description="Operation such as list, create, delete, add"
    )

    resource: str = Field(
        description="Target resource such as cluster, node, pod, deployment"
    )

    resource_name: str = Field(
        default="",
        description="Specific resource name if provided"
    )

    cluster_name: str = Field(
        default="",
        description="Cluster name if provided"
    )