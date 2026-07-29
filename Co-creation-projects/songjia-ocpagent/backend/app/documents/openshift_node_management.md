# OpenShift Node Management

Nodes provide the compute capacity for OpenShift workloads. In this demo,
node-management operations inspect and change mock node data only.

## Review node health

List nodes before taking action. Pay attention to name, role, readiness,
capacity, allocatable resources, and scheduling state. A node in `Ready` state
can accept workloads unless it is cordoned; a `NotReady` node needs
investigation before workloads are moved.

## Cordon a node

Cordoning prevents new pods from being scheduled on a node while leaving
existing pods in place. Use it before maintenance or when isolating a node
with a suspected issue. Clearly report the node name and its resulting
scheduling state.

## Drain a node

Draining evicts eligible workloads so maintenance can proceed. Check for
capacity on other ready nodes and for workloads that may not be safely
evicted. In a real environment this requires additional safeguards; here it is
only represented as a simulated operation.

## Return a node to service

After confirming that the node is healthy, uncordon it so new pods may be
scheduled. Verify that it is `Ready` and that its scheduling state allows
placement before declaring the maintenance complete.

## Investigation checklist

- Confirm the readiness condition and any reported reason.
- Compare CPU and memory capacity with current workload demand.
- Identify pods assigned to the node.
- Cordon first when an unsafe node might receive more workloads.
- Verify cluster capacity before proposing a drain.
