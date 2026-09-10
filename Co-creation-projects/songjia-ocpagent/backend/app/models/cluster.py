from pydantic import BaseModel
from app.models.node import Node


class ClusterSummary(BaseModel):
    cluster_id: str
    cluster_name: str
    cluster_ip: str = ""
    cluster_port: int = 0

class Cluster(BaseModel):
    cluster_id: int
    cluster_name: str
    cluster_ip: str
    cluster_port: int
    nodes: list[Node]
    namespaces: list[Namespace]
    deployments: list[Deployment]
    pods: list[Pod]
    secrets: list[Secret]

class Namespace(BaseModel):
    namespace_id: int
    namespace_name: str
    deployments: list[Deployment]

class Deployment(BaseModel):
    name: str

class Pod(BaseModel):
    pod_name: str
    pod_ip: str

class Secret(BaseModel):
    secret_name: str
