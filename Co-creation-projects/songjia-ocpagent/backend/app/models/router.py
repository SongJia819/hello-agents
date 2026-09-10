from pydantic import BaseModel, Field


class RouterResult(BaseModel):
    agent: str = Field(
        description="Target agent. One of: query, plan, execution, knowledge"
    )

    action: str = Field(
        description="Operation such as list, create, delete, add, answer, chat"
    )

    resources: list[str] = Field(
        min_length=1,
        description="Ordered target resources, such as node, pod, idrac, documentation, or conversation",
    )

    idrac_selectors: list[str] = Field(
        default_factory=list,
        description="Ordered iDRAC serial-number or IP selectors; only used when resources includes idrac",
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

    current_work_cluster: str = ""
    current_work_node: str = ""
