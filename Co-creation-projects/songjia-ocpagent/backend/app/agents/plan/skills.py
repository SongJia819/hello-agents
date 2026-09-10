from dataclasses import dataclass
from pathlib import Path

from app.config.capabilities import CAPABILITIES, AgentType


@dataclass(frozen=True)
class SkillStepDefinition:
    id: str
    inputs: tuple[str, ...]
    outputs: tuple[str, ...]
    depends_on: tuple[str, ...]


@dataclass(frozen=True)
class SkillDefinition:
    name: str
    relative_path: str
    action: str
    resources: tuple[str, ...]
    required_inputs: tuple[str, ...]
    write_only_inputs: tuple[str, ...]
    final_outputs: tuple[str, ...]
    procedure_step_ids: tuple[str, ...]
    step_interfaces: tuple[SkillStepDefinition, ...] = ()


NODE_ADD_SKILL = SkillDefinition(
    name="node-add",
    relative_path="node-add/SKILL.md",
    action="add",
    resources=("node",),
    required_inputs=(
        "cluster_id",
        "node.name",
        "node.username",
        "node.password",
        "node.domain",
        "node.network.port",
        "node.network.ip",
        "node.network.netmask",
        "node.network.gateway",
        "node.image.image_name",
        "node.image.image_path",
        "node.firmware.firmware_name",
        "node.firmware.firmware_path",
        "node.certificate.certificate_file_name",
        "node.certificate.certificate_file_path",
    ),
    write_only_inputs=("node.password",),
    final_outputs=("success", "operation", "cluster_id", "node", "steps", "message"),
    procedure_step_ids=(
        "validate_input",
        "check_cluster",
        "check_duplicates",
        "prepare_artifacts",
        "register_node",
        "configure_network",
        "install_firmware",
        "install_certificate",
        "mark_ready",
    ),
)


OCP_NODE_DELETE_SKILL = SkillDefinition(
    name="ocp-node-delete",
    relative_path="ocp-node-delete/SKILL.md",
    action="delete",
    resources=("node",),
    required_inputs=("cluster_id", "node_name"),
    write_only_inputs=(),
    final_outputs=("success", "operation", "cluster_id", "node_name", "steps", "message"),
    procedure_step_ids=("cordon_node", "drain_node", "delete_node"),
    step_interfaces=(
        SkillStepDefinition(
            id="cordon_node",
            inputs=("cluster_id", "node_name"),
            outputs=("node_unschedulable",),
            depends_on=(),
        ),
        SkillStepDefinition(
            id="drain_node",
            inputs=("cluster_id", "node_name", "node_unschedulable", "drain.force"),
            outputs=("pods_drained",),
            depends_on=("cordon_node",),
        ),
        SkillStepDefinition(
            id="delete_node",
            inputs=("cluster_id", "node_name", "pods_drained"),
            outputs=("node_deleted",),
            depends_on=("drain_node",),
        ),
    ),
)


class SkillResolutionError(ValueError):
    pass


class SkillRegistry:
    """Resolves only explicitly registered skills below the application root."""

    def __init__(self, skills_root: Path | None = None):
        self.skills_root = skills_root or Path(__file__).resolve().parents[2] / "skills"
        self._definitions = {
            NODE_ADD_SKILL.name: NODE_ADD_SKILL,
            OCP_NODE_DELETE_SKILL.name: OCP_NODE_DELETE_SKILL,
        }

    def resolve(self, action: str, resources: list[str]) -> tuple[SkillDefinition, str]:
        capability = CAPABILITIES[AgentType.PLAN].get(action, {})
        if len(resources) != 1:
            raise SkillResolutionError("A planning request must select exactly one resource.")

        skill_name = capability.get(resources[0])
        definition = self._definitions.get(skill_name)
        if definition is None:
            raise SkillResolutionError("No approved local skill supports this planning request.")

        path = (self.skills_root / definition.relative_path).resolve()
        root = self.skills_root.resolve()
        if root not in path.parents or not path.is_file():
            raise SkillResolutionError("The registered local skill is unavailable.")

        content = path.read_text(encoding="utf-8")
        if f"name: {definition.name}" not in content or "## Procedure" not in content:
            raise SkillResolutionError("The registered local skill is malformed.")

        return definition, content
