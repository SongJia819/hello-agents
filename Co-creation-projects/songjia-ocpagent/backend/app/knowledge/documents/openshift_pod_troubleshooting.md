# OpenShift Pod Troubleshooting

Pods are the smallest deployable workload unit in OpenShift. Use this guide to
interpret common pod states and to structure a simulated troubleshooting
response.

## Start with pod status

Identify the namespace and pod name, then inspect phase, container state,
restart count, assigned node, and recent events. These facts usually narrow
the problem quickly.

| Symptom | Likely area to inspect |
| --- | --- |
| `Pending` | Scheduling, node capacity, resource requests, or missing claims |
| `ImagePullBackOff` | Image name, registry access, or image pull credentials |
| `CrashLoopBackOff` | Container logs, command, configuration, or dependencies |
| Not ready | Readiness probe, service dependency, or application startup |
| Frequent restarts | Resource limits, application failures, or health checks |

## Follow a safe investigation order

1. Read the pod status and recent events.
2. Compare the pod's resource requests with available node capacity.
3. Check the owning deployment and its replica status.
4. Review simulated logs or failure details when provided.
5. Propose the smallest change that addresses the observed cause.

## Common resolutions

A pending pod may need a ready node with enough capacity. An image-pull failure
needs a corrected image reference or simulated credential configuration. A
crash loop usually requires fixing the application configuration or reverting a
recent deployment change. Do not recommend deleting a pod as a substitute for
understanding a persistent failure.

## Verify recovery

After a simulated remediation, confirm that the replacement pod is `Running`,
passes readiness checks, has a stable restart count, and restores the owning
deployment's available replicas.
