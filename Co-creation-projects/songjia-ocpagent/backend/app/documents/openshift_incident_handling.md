# OpenShift Incident Handling

This runbook provides a simple, repeatable way to handle simulated OpenShift
incidents. It supports investigation and communication; it does not authorize
changes to a real cluster.

## Triage

Capture the affected cluster, namespace, workload, start time, and visible
symptoms. Classify the severity according to user impact:

- **Low:** no user-facing impact or a single noncritical workload.
- **Medium:** a degraded application or a limited group of users affected.
- **High:** a broad outage, data-risk signal, or control-plane concern.

## Investigate

Begin with read-only information. Check node readiness, pod phase and restart
counts, deployment replica availability, and recent simulated events. Form a
clear hypothesis before proposing a remediation.

Typical correlations include a pending pod on an unavailable node, repeated
container restarts after a configuration change, or a deployment with fewer
available replicas than requested.

## Respond and communicate

State what is known, what is being checked, and the next safe action. Keep
observations separate from assumptions. For high-severity incidents, provide
short updates that include scope, current status, and the next update point.

## Recover and verify

Choose the smallest safe simulated remediation, such as rolling back a
deployment, scaling a healthy workload, or investigating a node condition.
Verify recovery through the relevant status: nodes are `Ready`, pods are
`Running`, and deployments have their intended available replicas.

## Close the incident

Summarize the impact, timeline, suspected cause, action taken, and verification
evidence. Record follow-up work such as adding a readiness check or improving
deployment validation.
