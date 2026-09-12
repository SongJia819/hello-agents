---
name: ocp-node-delete
description: Create a mock-only, non-executing three-step plan to cordon, drain, and delete one OpenShift node. Use for Plan Agent node deletion requests; do not use to execute cluster operations.
---

# OCP Node Delete

Create a plan for deleting one demo OpenShift node. This skill is a planning
contract only: it MUST NOT run `oc`, call Kubernetes or OpenShift APIs, use an
MCP execution tool, alter mock state, or request cluster credentials.

## Input Schema

```json
{
  "type": "object",
  "required": ["cluster_id", "node_name"],
  "properties": {
    "cluster_id": {"type": "string", "minLength": 1},
    "node_name": {"type": "string", "minLength": 1}
  }
}
```

The drain command's `--force=true` option is fixed operational intent, not a
plan input and does not allow callers to execute a command.

## Procedure

The generated plan MUST contain exactly these three steps in order.

1. `cordon_node`

   ```json
   {
     "id": "cordon_node",
     "intent": "oc adm cordon <node_name>",
     "inputs": ["cluster_id", "node_name"],
     "outputs": ["node_unschedulable"],
     "depends_on": []
   }
   ```

2. `drain_node`

   ```json
   {
     "id": "drain_node",
     "intent": "oc adm drain <node_name> --force=true",
     "inputs": ["cluster_id", "node_name", "node_unschedulable"],
     "outputs": ["pods_drained"],
     "depends_on": ["cordon_node"]
   }
   ```

3. `delete_node`

   ```json
   {
     "id": "delete_node",
     "intent": "oc delete node <node_name>",
     "inputs": ["cluster_id", "node_name", "pods_drained"],
     "outputs": ["node_deleted"],
     "depends_on": ["drain_node"]
   }
   ```

## Output Schema

```json
{
  "type": "object",
  "required": ["operation", "cluster_id", "node_name", "steps"],
  "properties": {
    "operation": {"const": "node.delete"},
    "cluster_id": {"type": "string"},
    "node_name": {"type": "string"},
    "steps": {
      "type": "array",
      "items": {
        "type": "object",
        "required": ["id", "intent", "inputs", "outputs", "depends_on"],
        "properties": {
          "id": {"type": "string"},
          "intent": {"type": "string"},
          "inputs": {"type": "array"},
          "outputs": {"type": "array"},
          "depends_on": {"type": "array"}
        }
      }
    }
  }
}
```

The output describes the planned result only. It MUST NOT claim the node was
actually cordoned, drained, or deleted.
