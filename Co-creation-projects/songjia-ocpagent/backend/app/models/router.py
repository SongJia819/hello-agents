from pydantic import BaseModel, Field


class RouterResult(BaseModel):
    agent: str = Field(
        description="Target agent. One of: query, plan, execution"
    )

    action: str = Field(
        description="Operation such as list, create, delete, add"
    )

    resources: list[str] = Field(
        min_length=1,
        description="Ordered target resources, such as node or node and pod",
    )

    resource: str = Field(
        default="",
        description="Deprecated primary resource retained for state compatibility",
    )

    resource_name: str = Field(
        default="",
        description="Specific resource name if provided"
    )

    cluster_name: str = Field(
        default="",
        description="Cluster name if provided"
    )
