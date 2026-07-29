# OpenShift Deployment Management

Deployments describe the desired number of application pod replicas and the
container image they run. This document is guidance for interpreting and
simulating deployment-management requests in the demo environment.

## Inspect a deployment

Start by identifying the namespace and deployment name. Review its desired,
available, and ready replica counts, along with the current image and recent
events. A healthy deployment normally has matching desired and available
replicas.

## Roll out an update

When updating an application, state the intended image or configuration change
and monitor rollout progress. The usual sequence is:

1. Update the deployment template.
2. Create replacement pods gradually.
3. Wait for replacement pods to become ready.
4. Scale down the prior replica set.

For this project, report those stages as simulated actions. Never imply that a
real registry, OpenShift API, or workload was changed.

## Scale safely

Confirm the requested replica count and the namespace before scaling. Explain
the expected capacity impact, then report the resulting desired replica count.
If pods cannot become ready, retain the useful status details for pod
troubleshooting.

## Roll back

Roll back when a new version causes readiness failures, elevated errors, or an
unexpected reduction in available replicas. Identify the prior known-good
revision, restore it in the mock response, and verify that the simulated pods
return to `Running` and `Ready`.

## Troubleshooting checklist

- Compare desired, updated, and available replicas.
- Check whether a pod is pending, restarting, or failing readiness checks.
- Review the image and configuration referenced by the deployment.
- Use a rollback rather than continuing a failed rollout without a clear cause.
