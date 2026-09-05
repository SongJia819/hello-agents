---
name: node-add
description: Add a node to the demo OpenShift cluster through the mock node-management workflow, including input validation, ordered provisioning steps, and a structured result. Use for requests to add, register, or provision a cluster node; do not use for listing or removing nodes.
---

# Node Add

Add one node to the demo cluster using mock data only. This skill describes the
workflow contract for an agent or tool implementation; it does not authorize
connections to a real Kubernetes/OpenShift cluster and must not request cluster
credentials.

## Input

Accept a structured object with these fields:

```json
{
  "cluster_id": "cluster-001",
  "node": {
    "name": "worker-002",
    "username": "admin",
    "password": "Admin@123456",
    "domain": "agent.local",
    "network": {
      "port": 8080,
      "ip": "192.168.1.101",
      "netmask": "255.255.255.0",
      "gateway": "192.168.1.1"
    },
    "image": {
      "image_name": "ollama-qwen3-4b",
      "image_path": "/opt/docker/images/qwen3-4b.tar"
    },
    "firmware": {
      "firmware_name": "device-fw-v2.3.1",
      "firmware_path": "/data/firmware/v2.3.1.bin"
    },
    "certificate": {
      "certificate_file_name": "agent-cert.pem",
      "certificate_file_path": "/etc/ssl/certs/agent-cert.pem"
    }
  }
}
```

Required fields are `cluster_id`, `node.name`, `node.username`, `node.password`,
`node.domain`, and all fields under `network`, `image`, `firmware`, and
`certificate`. Validate that `network.port` is an integer, IP-related values
are non-empty, and all artifact paths are non-empty strings. Never echo the
password in logs or the output.

## Procedure

Execute the following steps in order:

1. Validate the input shape and required values. Return a validation failure
   without changing mock cluster state when validation fails.
2. Confirm that `cluster_id` identifies an available mock cluster.
3. List existing mock nodes for the cluster.
4. Reject the request if another node already has the requested `node.name` or
   if the requested IP is already assigned.
5. Validate the requested image, firmware, and certificate metadata as mock
   artifacts. Do not download files, inspect the host, or contact external
   services.
6. Create/register the node in the mock provider with an initial status of
   `Provisioning`.
7. Simulate artifact preparation, network setup, firmware validation, and
   certificate installation in that order.
8. Mark the node `Ready` only when every simulated step succeeds. If a step
   fails, mark the mock operation `Failed`, preserve the failed step and reason,
   and do not claim that the node is ready.
9. Return the structured result below. Include only a redacted node summary;
   credentials are write-only inputs for this workflow.

## Output

Return an object with this shape:

```json
{
  "success": true,
  "operation": "node.add",
  "cluster_id": "cluster-001",
  "node": {
    "name": "worker-002",
    "status": "Ready",
    "ip": "192.168.1.101",
    "domain": "agent.local"
  },
  "steps": [
    {"name": "validate_input", "status": "Succeeded"},
    {"name": "check_cluster", "status": "Succeeded"},
    {"name": "check_duplicates", "status": "Succeeded"},
    {"name": "prepare_artifacts", "status": "Succeeded"},
    {"name": "register_node", "status": "Succeeded"},
    {"name": "configure_network", "status": "Succeeded"},
    {"name": "install_firmware", "status": "Succeeded"},
    {"name": "install_certificate", "status": "Succeeded"},
    {"name": "mark_ready", "status": "Succeeded"}
  ],
  "message": "Node worker-002 was added successfully to cluster-001."
}
```

For failure, set `success` to `false`, set the node status to `Failed` when a
node record was created, and add `failed_step` and `error`:

```json
{
  "success": false,
  "operation": "node.add",
  "cluster_id": "cluster-001",
  "node": {"name": "worker-002", "status": "Failed", "ip": "192.168.1.101"},
  "failed_step": "check_duplicates",
  "error": {"code": "NODE_ALREADY_EXISTS", "message": "A node named worker-002 already exists."},
  "steps": []
}
```

Use stable error codes such as `INVALID_INPUT`, `CLUSTER_NOT_FOUND`,
`NODE_ALREADY_EXISTS`, `IP_ALREADY_ASSIGNED`, `ARTIFACT_INVALID`, and
`PROVISIONING_FAILED`. Keep the output safe for conversation display: omit
passwords, private keys, certificate contents, and other secrets.
