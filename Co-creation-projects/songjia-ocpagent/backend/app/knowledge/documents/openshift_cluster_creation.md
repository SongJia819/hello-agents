# OpenShift Cluster Creation

This guide describes the standard cluster-creation workflow used by the demo
agent. The platform returns simulated results only; it does not create or
connect to a real OpenShift cluster.

## Gather requirements

Before creating a cluster, confirm the requested name, environment, OpenShift
version, control-plane size, worker count, and network range. A useful request
also identifies the workload type and any availability requirements.

Example request:

```text
Create a development cluster named demo-dev with three workers.
```

## Plan the topology

For a typical demo cluster, use three control-plane nodes and three worker
nodes. Assign clear, stable names such as `master-01` and `worker-01`. Record
the selected version and the intended machine capacity so that later node and
pod queries have meaningful context.

## Simulated creation flow

1. Validate that the cluster name is present and unique in the mock inventory.
2. Create the mock control-plane and worker records.
3. Mark nodes as `Ready` after the simulated bootstrap completes.
4. Return the cluster identifier, node summary, and a success or failure
   message.

If validation fails, explain the reason and suggest a corrected request. Do
not claim that infrastructure was provisioned outside the demo environment.

## Verify the result

After a successful response, query the cluster nodes and confirm that the
expected nodes report `Ready`. Then query namespaces or pods to verify that
the simulated platform workloads are available.

## Common issues

- **Duplicate name:** choose a different cluster name or remove the existing
  mock cluster record.
- **Invalid worker count:** request a positive whole number.
- **Nodes not ready:** inspect the simulated bootstrap or node status returned
  by the agent before retrying.
