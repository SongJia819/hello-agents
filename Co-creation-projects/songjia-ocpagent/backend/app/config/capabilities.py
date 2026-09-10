from enum import Enum

class AgentType(str, Enum):
    QUERY = "query"
    PLAN = "plan"
    EXECUTION = "execution"
    KNOWLEDGE = "knowledge"
    MEMORY = "memory"

CAPABILITIES = {
    AgentType.QUERY: {
        "list": {
            "node": "list_nodes",
            "pod": "list_pods",
            "idrac": "list_idrac_nodes",
            # "deployment": "list_deployments",
            # "namespace": "list_namespaces",
            # "service": "list_services",
        },
    },

    AgentType.PLAN: {
        "add": {
            "node": "node-add",
        },
        "delete": {
            "node": "ocp-node-delete",
        },
    },

    AgentType.EXECUTION: {
        # "drain_node": "drain_node",
        # "delete_node": "delete_node",
    },
    AgentType.KNOWLEDGE: {
        "answer": {
            "documentation": "knowledge_answer",
        },
        "chat": {
            "conversation": "knowledge_chat",
        },
    },
}
