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
            # "deployment": "list_deployments",
            # "namespace": "list_namespaces",
            # "service": "list_services",
        },
    },

    AgentType.PLAN: {
        # "create_cluster": "create_cluster_plan",
        # "delete_node": "delete_node_plan",
    },

    AgentType.EXECUTION: {
        # "drain_node": "drain_node",
        # "delete_node": "delete_node",
    }
}
