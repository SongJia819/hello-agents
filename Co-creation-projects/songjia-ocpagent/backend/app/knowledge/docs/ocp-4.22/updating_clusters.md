---
title: "Updating clusters"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/index
retrieved_at: 2026-09-05T05:43:01.032896+00:00
---

# Updating clusters

---

OpenShift Container Platform 4.22

## Updating OpenShift Container Platform clusters

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139685294070656)

**Abstract**

This document provides instructions for updating, or upgrading, OpenShift Container Platform clusters. Updating your cluster is a simple process that does not require you to take your cluster offline.

---

## [Chapter 1. Understanding OpenShift updates](#understanding-openshift-updates-1) Copy linkLink copied to clipboard!

### [1.1. Introduction to OpenShift updates](#understanding-openshift-updates) Copy linkLink copied to clipboard!

With OpenShift Container Platform 4, you can update an OpenShift Container Platform cluster with a single operation by using the web console or the OpenShift CLI (`oc`).

Platform administrators can view new update options either by going to **Administration** → **Cluster Settings** in the web console or by looking at the output of the `oc adm upgrade` command.

#### [1.1.1. Cluster update overview](#about-updates_understanding-openshift-updates) Copy linkLink copied to clipboard!

OpenShift Container Platform updates involve several services, Operators, and processes working in tandem to change the cluster to the desired version.

Red Hat hosts a public OpenShift Update Service (OSUS), which serves a graph of update possibilities based on the OpenShift Container Platform release images in the official registry. The graph contains update information for any public release. OpenShift Container Platform clusters are configured to connect to the OSUS by default, and the OSUS responds to clusters with information about known update targets.

An update begins when either a cluster administrator or an automatic update controller edits the custom resource (CR) of the Cluster Version Operator (CVO) with a new version. To reconcile the cluster with the newly specified version, the CVO retrieves the target release image from an image registry and begins to apply changes to the cluster.

Note

Operators previously installed through Operator Lifecycle Manager (OLM) follow a different process for updates. See [Updating installed Operators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-upgrading-operators) for more information.

The target release image contains manifest files for all cluster components that form a specific OCP version. When updating the cluster to a new version, the CVO applies manifests in separate stages called Runlevels. Most, but not all, manifests support one of the cluster Operators. As the CVO applies a manifest to a cluster Operator, the Operator might perform update tasks to reconcile itself with its new specified version.

The CVO monitors the state of each applied resource and the states reported by all cluster Operators. The CVO only proceeds with the update when all manifests and cluster Operators in the active Runlevel reach a stable condition. After the CVO updates the entire control plane through this process, the Machine Config Operator (MCO) updates the operating system and configuration of every node in the cluster.

#### [1.1.2. Common questions about update availability](#update-availability_understanding-openshift-updates) Copy linkLink copied to clipboard!

There are several factors that affect if and when an update is made available to an OpenShift Container Platform cluster.

The following list provides common questions regarding the availability of an update:

**What are the differences between each of the update channels?**

* A new release is initially added to the `candidate` channel.
* After successful final testing, a release on the `candidate` channel is promoted to the `fast` channel, an errata is published, and the release is now fully supported.
* After a delay, a release on the `fast` channel is finally promoted to the `stable` channel. This delay represents the only difference between the `fast` and `stable` channels.

  Note

  For the latest z-stream releases, this delay may generally be a week or two. However, the delay for initial updates to the latest minor version may take much longer, generally 45-90 days.
* Releases promoted to the `stable` channel are simultaneously promoted to the `eus` channel. The primary purpose of the `eus` channel is to serve as a convenience for clusters performing a Control Plane Only update.

**Is a release on the `stable` channel safer or more supported than a release on the `fast` channel?**

* If a regression is identified for a release on a `fast` channel, it will be resolved and managed to the same extent as if that regression was identified for a release on the `stable` channel.
* The only difference between releases on the `fast` and `stable` channels is that a release only appears on the `stable` channel after it has been on the `fast` channel for some time, which provides more time for new update risks to be discovered.
* A release that is available on the `fast` channel always becomes available on the `stable` channel after this delay.

**What does it mean if an update has known issues?**

* Red Hat continuously evaluates data from multiple sources to determine whether updates from one version to another have any declared issues. Identified issues are typically documented in the version’s release notes. Even if the update path has known issues, customers are still supported if they perform the update.
* Red Hat does not block users from updating to a certain version. Red Hat may declare conditional update risks, which may or may not apply to a particular cluster.

  + Declared risks provide cluster administrators more context about a supported update. Cluster administrators can still accept the risk and update to that particular target version.

**What if I see that an update to a particular release is no longer recommended?**

* If Red Hat removes update recommendations from any supported release due to a regression, a superseding update recommendation will be provided to a future version that corrects the regression. There may be a delay while the defect is corrected, tested, and promoted to your selected channel.

**How long until the next z-stream release is made available on the fast and stable channels?**

* While the specific cadence can vary based on a number of factors, new z-stream releases for the latest minor version are typically made available about every week. Older minor versions, which have become more stable over time, may take much longer for new z-stream releases to be made available.

  Important

  These are only estimates based on past data about z-stream releases. Red Hat reserves the right to change the release frequency as needed. Any number of issues could cause irregularities and delays in this release cadence.
* Once a z-stream release is published, it also appears in the `fast` channel for that minor version. After a delay, the z-stream release may then appear in that minor version’s `stable` channel.

#### [1.1.3. About the OpenShift Update Service](#update-service-about_understanding-openshift-updates) Copy linkLink copied to clipboard!

The OpenShift Update Service (OSUS) provides update recommendations to OpenShift Container Platform, including Red Hat Enterprise Linux CoreOS (RHCOS). It provides a graph, or diagram, that contains the *vertices* of component Operators and the *edges* that connect them.

The edges in the graph show which versions you can safely update to. The vertices are update payloads that specify the intended state of the managed cluster components.

The Cluster Version Operator (CVO) in your cluster checks with the OpenShift Update Service to see the valid updates and update paths based on current component versions and information in the graph. When you request an update, the CVO uses the corresponding release image to update your cluster. The release artifacts are hosted in Quay as container images.

To allow the OpenShift Update Service to provide only compatible updates, a release verification pipeline drives automation. Each release artifact is verified for compatibility with supported cloud platforms and system architectures, as well as other component packages. After the pipeline confirms the suitability of a release, the OpenShift Update Service notifies you that it is available.

The OpenShift Update Service (OSUS) supports a single-stream release model, where only one release version is active and supported at any given time. When a new release is deployed, it fully replaces the previous release.

The updated release provides support for upgrades from all OpenShift Container Platform versions starting after 4.8 up to the new release version.

Important

The OpenShift Update Service displays all recommended updates for your current cluster. If an update path is not recommended by the OpenShift Update Service, it might be because of a known issue related to the update path, such as incompatibility or availability.

Two controllers run during continuous update mode. The first controller continuously updates the payload manifests, applies the manifests to the cluster, and outputs the controlled rollout status of the Operators to indicate whether they are available, upgrading, or failed. The second controller polls the OpenShift Update Service to determine if updates are available.

Important

Only updating to a newer version is supported. Reverting or rolling back your cluster to a previous version is not supported. If your update fails, contact Red Hat support.

During the update process, the Machine Config Operator (MCO) applies the new configuration to your cluster machines. The MCO cordons the number of nodes specified by the `maxUnavailable` field on the machine configuration pool and marks them unavailable. By default, this value is set to `1`. The MCO updates the affected nodes alphabetically by zone, based on the `topology.kubernetes.io/zone` label. If a zone has more than one node, the oldest nodes are updated first. For nodes that do not use zones, such as in bare metal deployments, the nodes are updated by age, with the oldest nodes updated first. The MCO updates the number of nodes as specified by the `maxUnavailable` field on the machine configuration pool at a time. The MCO then applies the new configuration and reboots the machine.

Warning

The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.

If you use Red Hat Enterprise Linux (RHEL) machines as workers, the MCO does not update the kubelet because you must update the OpenShift API on the machines first.

With the specification for the new version applied to the old kubelet, the RHEL machine cannot return to the `Ready` state. You cannot complete the update until the machines are available. However, the maximum number of unavailable nodes is set to ensure that normal cluster operations can continue with that number of machines out of service.

The OpenShift Update Service is composed of an Operator and one or more application instances.

#### [1.1.4. Understanding cluster Operator condition types](#understanding_clusteroperator_conditiontypes_understanding-openshift-updates) Copy linkLink copied to clipboard!

The status of cluster Operators includes their condition type, which informs you of the current state of your Operator’s health.

The following definitions cover a list of some common ClusterOperator condition types. Operators that have additional condition types and use Operator-specific language have been omitted.

The Cluster Version Operator (CVO) is responsible for collecting the status conditions from cluster Operators so that cluster administrators can better understand the state of the OpenShift Container Platform cluster.

* Available: The condition type `Available` indicates that an Operator is functional and available in the cluster. If the status is `False`, at least one part of the operand is non-functional and the condition requires an administrator to intervene.
* Progressing: The condition type `Progressing` indicates that an Operator is actively rolling out new code, propagating configuration changes, or otherwise moving from one steady state to another.

  Operators do not report the condition type `Progressing` as `True` when they are reconciling a previous known state. If the observed cluster state has changed and the Operator is reacting to it, then the status reports back as `True`, since it is moving from one steady state to another.
* Degraded: The condition type `Degraded` indicates that an Operator has a current state that does not match its required state over a period of time. The period of time can vary by component, but a `Degraded` status represents persistent observation of an Operator’s condition. As a result, an Operator does not fluctuate in and out of the `Degraded` state.

  There might be a different condition type if the transition from one state to another does not persist over a long enough period to report `Degraded`. An Operator does not report `Degraded` during the course of a normal update. An Operator may report `Degraded` in response to a persistent infrastructure failure that requires eventual administrator intervention.

  Note

  This condition type is only an indication that something may need investigation and adjustment. As long as the Operator is available, the `Degraded` condition does not cause user workload failure or application downtime.
* Upgradeable: The condition type `Upgradeable` indicates whether the Operator is safe to update based on the current cluster state. The message field contains a human-readable description of what the administrator needs to do for the cluster to successfully update. The CVO allows updates when this condition is `True`, `Unknown` or missing.

  When the `Upgradeable` status is `False`, only minor updates are impacted, and the CVO prevents the cluster from performing impacted updates unless forced.

#### [1.1.5. Understanding cluster version condition types](#understanding-clusterversion-conditiontypes_understanding-openshift-updates) Copy linkLink copied to clipboard!

The Cluster Version Operator (CVO) monitors cluster Operators and other components, and is responsible for collecting the status of both the cluster version and its Operators. This status includes the condition type, which informs you of the health and current state of the OpenShift Container Platform cluster.

In addition to `Available`, `Progressing`, and `Upgradeable`, there are condition types that affect cluster versions and Operators.

* Failing: The cluster version condition type `Failing` indicates that a cluster cannot reach its desired state, is unhealthy, and requires an administrator to intervene.
* Invalid: The cluster version condition type `Invalid` indicates that the cluster version has an error that prevents the server from taking action. The CVO only reconciles the current state as long as this condition is set.
* RetrievedUpdates: The cluster version condition type `RetrievedUpdates` indicates whether or not available updates have been retrieved from the upstream update server. The condition is `Unknown` before retrieval, `False` if the updates either recently failed or could not be retrieved, or `True` if the `availableUpdates` field is both recent and accurate.
* ReleaseAccepted: The cluster version condition type `ReleaseAccepted` with a `True` status indicates that the requested release payload was successfully loaded without failure during image verification and precondition checking.
* ImplicitlyEnabledCapabilities: The cluster version condition type `ImplicitlyEnabledCapabilities` with a `True` status indicates that there are enabled capabilities that the user is not currently requesting through `spec.capabilities`. The CVO does not support disabling capabilities if any associated resources were previously managed by the CVO.

#### [1.1.6. Common terms](#update-common-terms_understanding-openshift-updates) Copy linkLink copied to clipboard!

Some terms are commonly used in the context of OpenShift Container Platform updates, which might be useful to learn.

Control plane
:   The *control plane*, which is composed of control plane machines, manages the OpenShift Container Platform cluster. The control plane machines manage workloads on the compute machines, which are also known as worker machines.

Cluster Version Operator
:   The *Cluster Version Operator* (CVO) starts the update process for the cluster. It checks with OSUS based on the current cluster version and retrieves the graph which contains available or possible update paths.

Machine Config Operator
:   The *Machine Config Operator* (MCO) is a cluster-level Operator that manages the operating system and machine configurations. Through the MCO, platform administrators can configure and update systemd, CRI-O and Kubelet, the kernel, NetworkManager, and other system features on the worker nodes.

OpenShift Update Service
:   The *OpenShift Update Service* (OSUS) provides over-the-air updates to OpenShift Container Platform, including to Red Hat Enterprise Linux CoreOS (RHCOS). It provides a graph, or diagram, that contains the vertices of component Operators and the edges that connect them.

Channels
:   *Channels* declare an update strategy tied to minor versions of OpenShift Container Platform. The OSUS uses this configured strategy to recommend update edges consistent with that strategy.

Recommended update edge
:   A *recommended update edge* is a recommended update between OpenShift Container Platform releases. Whether a given update is recommended can depend on the cluster’s configured channel, current version, known bugs, and other information. OSUS communicates the recommended edges to the CVO, which runs in every cluster.

### [1.2. How cluster updates work](#how-updates-work) Copy linkLink copied to clipboard!

The Cluster Version Operator (CVO) is the primary component that orchestrates the OpenShift Container Platform update process. During standard cluster operation, the CVO compares manifests of cluster Operators to in-cluster resources and reconciles discrepancies between the actual state of these resources and their desired state.

The following sections describe each major aspect of the OpenShift Container Platform (OCP) update process in detail. For a general overview of how updates work, see the [Introduction to OpenShift updates](#understanding-openshift-updates "1.1. Introduction to OpenShift updates").

#### [1.2.1. The ClusterVersion object](#update-cluster-version-object_how-updates-work) Copy linkLink copied to clipboard!

One of the resources that the Cluster Version Operator (CVO) monitors is the `ClusterVersion` resource.

Administrators and OpenShift Container Platform components can communicate or interact with the CVO through the `ClusterVersion` object. The desired CVO state is declared through the `ClusterVersion` object and the current CVO state is reflected in the object’s status.

Note

Do not directly modify the `ClusterVersion` object. Instead, use interfaces such as the `oc` CLI or the web console to declare your update target.

The CVO continually reconciles the cluster with the target state declared in the `spec` property of the `ClusterVersion` resource. When the desired release differs from the actual release, that reconciliation updates the cluster.

##### [1.2.1.1. Update availability data](#update-availability-data_how-updates-work) Copy linkLink copied to clipboard!

The `ClusterVersion` resource also contains information about updates that are available to the cluster. This includes updates that are available, but not recommended due to a known risk that applies to the cluster. These updates are known as conditional updates. To learn how the CVO maintains this information about available updates in the `ClusterVersion` resource, see the "Evaluation of update availability" section.

You can inspect all available updates with the following command:

```
$ oc adm upgrade --include-not-recommended
```

Note

The additional `--include-not-recommended` parameter includes updates that are available with known issues that apply to the cluster.

**Example output**

```
Cluster version is 4.13.40

Upstream is unset, so the cluster will use an appropriate default.
Channel: stable-4.14 (available channels: candidate-4.13, candidate-4.14, eus-4.14, fast-4.13, fast-4.14, stable-4.13, stable-4.14)

Recommended updates:

  VERSION     IMAGE
  4.14.27     quay.io/openshift-release-dev/ocp-release@sha256:4d30b359aa6600a89ed49ce6a9a5fdab54092bcb821a25480fdfbc47e66af9ec
  4.14.26     quay.io/openshift-release-dev/ocp-release@sha256:4fe7d4ccf4d967a309f83118f1a380a656a733d7fcee1dbaf4d51752a6372890
  4.14.25     quay.io/openshift-release-dev/ocp-release@sha256:a0ef946ef8ae75aef726af1d9bbaad278559ad8cab2c1ed1088928a0087990b6
  4.14.24     quay.io/openshift-release-dev/ocp-release@sha256:0a34eac4b834e67f1bca94493c237e307be2c0eae7b8956d4d8ef1c0c462c7b0
  4.14.23     quay.io/openshift-release-dev/ocp-release@sha256:f8465817382128ec7c0bc676174bad0fb43204c353e49c146ddd83a5b3d58d92
  4.13.42     quay.io/openshift-release-dev/ocp-release@sha256:dcf5c3ad7384f8bee3c275da8f886b0bc9aea7611d166d695d0cf0fff40a0b55
  4.13.41     quay.io/openshift-release-dev/ocp-release@sha256:dbb8aa0cf53dc5ac663514e259ad2768d8c82fd1fe7181a4cfb484e3ffdbd3ba

Updates with known issues:

  Version: 4.14.22
  Image: quay.io/openshift-release-dev/ocp-release@sha256:7093fa606debe63820671cc92a1384e14d0b70058d4b4719d666571e1fc62190
  Reason: MultipleReasons
  Message: Exposure to AzureRegistryImageMigrationUserProvisioned is unknown due to an evaluation failure: client-side throttling: only 18.061µs has elapsed since the last match call completed for this cluster condition backend; this cached cluster condition request has been queued for later execution
  In Azure clusters with the user-provisioned registry storage, the in-cluster image registry component may struggle to complete the cluster update. https://issues.redhat.com/browse/IR-468

  Incoming HTTP requests to services exposed by Routes may fail while routers reload their configuration, especially when made with Apache HTTPClient versions before 5.0. The problem is more likely to occur in clusters with higher number of Routes and corresponding endpoints. https://issues.redhat.com/browse/NE-1689

  Version: 4.14.21
  Image: quay.io/openshift-release-dev/ocp-release@sha256:6e3fba19a1453e61f8846c6b0ad3abf41436a3550092cbfd364ad4ce194582b7
  Reason: MultipleReasons
  Message: Exposure to AzureRegistryImageMigrationUserProvisioned is unknown due to an evaluation failure: client-side throttling: only 33.991µs has elapsed since the last match call completed for this cluster condition backend; this cached cluster condition request has been queued for later execution
  In Azure clusters with the user-provisioned registry storage, the in-cluster image registry component may struggle to complete the cluster update. https://issues.redhat.com/browse/IR-468

  Incoming HTTP requests to services exposed by Routes may fail while routers reload their configuration, especially when made with Apache HTTPClient versions before 5.0. The problem is more likely to occur in clusters with higher number of Routes and corresponding endpoints. https://issues.redhat.com/browse/NE-1689
```

The `oc adm upgrade` command queries the `ClusterVersion` resource for information about available updates and presents it in a human-readable format.

One way to directly inspect the underlying availability data created by the CVO is by querying the `ClusterVersion` resource with the following command:

```
$ oc get clusterversion version -o json | jq '.status.availableUpdates'
```

**Example output**

```
[
  {
    "channels": [
      "candidate-4.11",
      "candidate-4.12",
      "fast-4.11",
      "fast-4.12"
    ],
    "image": "quay.io/openshift-release-dev/ocp-release@sha256:400267c7f4e61c6bfa0a59571467e8bd85c9188e442cbd820cc8263809be3775",
    "url": "https://access.redhat.com/errata/RHBA-2023:3213",
    "version": "4.11.41"
  },
  ...
]
```

A similar command can be used to check conditional updates:

```
$ oc get clusterversion version -o json | jq '.status.conditionalUpdates'
```

**Example output**

```
[
  {
    "conditions": [
      {
        "lastTransitionTime": "2023-05-30T16:28:59Z",
        "message": "The 4.11.36 release only resolves an installation issue https://issues.redhat.com//browse/OCPBUGS-11663 , which does not affect already running clusters. 4.11.36 does not include fixes delivered in recent 4.11.z releases and therefore upgrading from these versions would cause fixed bugs to reappear. Red Hat does not recommend upgrading clusters to 4.11.36 version for this reason. https://access.redhat.com/solutions/7007136",
        "reason": "PatchesOlderRelease",
        "status": "False",
        "type": "Recommended"
      }
    ],
    "release": {
      "channels": [...],
      "image": "quay.io/openshift-release-dev/ocp-release@sha256:8c04176b771a62abd801fcda3e952633566c8b5ff177b93592e8e8d2d1f8471d",
      "url": "https://access.redhat.com/errata/RHBA-2023:1733",
      "version": "4.11.36"
    },
    "risks": [...]
  },
  ...
]
```

#### [1.2.2. Evaluation of update availability](#update-evaluate-availability_how-updates-work) Copy linkLink copied to clipboard!

The Cluster Version Operator (CVO) periodically queries the OpenShift Update Service (OSUS) for the most recent data about update possibilities.

This data is based on the cluster’s subscribed channel. The CVO then saves information about update recommendations into either the `availableUpdates` or `conditionalUpdates` field of its `ClusterVersion` resource.

The CVO periodically checks the conditional updates for update risks. These risks are conveyed through the data served by the OSUS, which contains information for each version about known issues that might affect a cluster updated to that version. Most risks are limited to clusters with specific characteristics, such as clusters with a certain size or clusters that are deployed in a particular cloud platform.

The CVO continuously evaluates its cluster characteristics against the conditional risk information for each conditional update. If the CVO finds that the cluster matches the criteria, the CVO stores this information in the `conditionalUpdates` field of its `ClusterVersion` resource. If the CVO finds that the cluster does not match the risks of an update, or that there are no risks associated with the update, it stores the target version in the `availableUpdates` field of its `ClusterVersion` resource.

The user interface, either the web console or the OpenShift CLI (`oc`), presents this information in sectioned headings to the administrator. Each known issue associated with the update path contains a link to further resources about the risk so that the administrator can make an informed decision about the update.

#### [1.2.3. Release images](#update-release-images_how-updates-work) Copy linkLink copied to clipboard!

A release image is the delivery mechanism for a specific OpenShift Container Platform (OCP) version.

It contains the release metadata, a Cluster Version Operator (CVO) binary matching the release version, every manifest needed to deploy individual cluster Operators, and a list of SHA digest-versioned references to all container images that make up this version.

You can extract a specific release image by running the following command:

```
$ oc adm release extract <release image>
```

**Example command**

```
$ oc adm release extract quay.io/openshift-release-dev/ocp-release:4.12.6-x86_64
```

**Example output**

```
Extracted release payload from digest sha256:800d1e39d145664975a3bb7cbc6e674fbf78e3c45b5dde9ff2c5a11a8690c87b created at 2023-03-01T12:46:29Z
```

After the release image is extracted, you can inspect its contents by running the following command:

```
$ ls
```

**Example output**

```
0000_03_authorization-openshift_01_rolebindingrestriction.crd.yaml
0000_03_config-operator_01_proxy.crd.yaml
0000_03_marketplace-operator_01_operatorhub.crd.yaml
0000_03_marketplace-operator_02_operatorhub.cr.yaml
0000_03_quota-openshift_01_clusterresourcequota.crd.yaml
...
0000_90_service-ca-operator_02_prometheusrolebinding.yaml
0000_90_service-ca-operator_03_servicemonitor.yaml
0000_99_machine-api-operator_00_tombstones.yaml
image-references
release-metadata
```

In this example output, the following contents can be seen:

* `0000_03_quota-openshift_01_clusterresourcequota.crd.yaml` is the manifest for the `ClusterResourceQuota` CRD, to be applied on Runlevel 03.
* `0000_90_service-ca-operator_02_prometheusrolebinding.yaml` is the manifest for the `PrometheusRoleBinding` resource for the `service-ca-operator`, to be applied on Runlevel 90.
* `image-references` is the list of SHA digest-versioned references to all required images.

#### [1.2.4. Update process workflow](#update-process-workflow_how-updates-work) Copy linkLink copied to clipboard!

When you initiate a cluster update, the Cluster Version Operator (CVO) begins a specific sequence of events to orchestrate the update.

The following steps represent a detailed workflow of the OpenShift Container Platform update process:

1. The target version is stored in the `spec.desiredUpdate.version` field of the `ClusterVersion` resource, which may be managed through the web console or the CLI.
2. The CVO detects that the `desiredUpdate` field in the `ClusterVersion` resource differs from the current cluster version. Using graph data from the OpenShift Update Service, the CVO resolves the desired cluster version to a pull spec for the release image.
3. The CVO validates the integrity and authenticity of the release image. Red Hat publishes cryptographically-signed statements about published release images at predefined locations by using image SHA digests as unique and immutable release image identifiers. The CVO utilizes a list of built-in public keys to validate the presence and signatures of the statement matching the checked release image.
4. The CVO creates a job named `version-$version-$hash` in the `openshift-cluster-version` namespace. This job uses containers that are executing the release image, so the cluster downloads the image through the container runtime. The job then extracts the manifests and metadata from the release image to a shared volume that is accessible to the CVO.
5. The CVO validates the extracted manifests and metadata.
6. The CVO checks some preconditions to ensure that no problematic condition is detected in the cluster. Certain conditions can prevent updates from proceeding. These conditions are either determined by the CVO itself, or reported by individual cluster Operators that detect some details about the cluster that the Operator considers problematic for the update.
7. The CVO records the accepted release in `status.desired` and creates a `status.history` entry about the new update.
8. The CVO begins reconciling the manifests from the release image. Cluster Operators are updated in separate stages called Runlevels, and the CVO ensures that all Operators in a Runlevel finish updating before it proceeds to the next level.
9. Manifests for the CVO itself are applied early in the process. When the CVO deployment is applied, the current CVO pod stops, and a CVO pod that uses the new version starts. The new CVO proceeds to reconcile the remaining manifests.
10. The update proceeds until the entire control plane is updated to the new version. Individual cluster Operators might perform update tasks on their domain of the cluster, and while they do so, they report their state through the `Progressing=True` condition.
11. The Machine Config Operator (MCO) manifests are applied towards the end of the process. The updated MCO then begins updating the system configuration and operating system of every node. Each node might be drained, updated, and rebooted before it starts to accept workloads again.

The cluster reports as updated after the control plane update is finished, usually before all nodes are updated. After the update, the CVO maintains all cluster resources to match the state delivered in the release image.

#### [1.2.5. Understanding how manifests are applied during an update](#update-manifest-application_how-updates-work) Copy linkLink copied to clipboard!

Some manifests supplied in a release image must be applied in a certain order because of the dependencies between them.

For example, the `CustomResourceDefinition` resource must be created before the matching custom resources. Additionally, there is a logical order in which the individual cluster Operators must be updated to minimize disruption in the cluster. The Cluster Version Operator (CVO) implements this logical order through the concept of Runlevels.

These dependencies are encoded in the filenames of the manifests in the release image:

```
0000_<runlevel>_<component>_<manifest-name>.yaml
```

For example:

```
0000_03_config-operator_01_proxy.crd.yaml
```

The CVO internally builds a dependency graph for the manifests, where the CVO obeys the following rules:

* During an update, manifests at a lower Runlevel are applied before those at a higher Runlevel.
* Within one Runlevel, manifests for different components can be applied in parallel.
* Within one Runlevel, manifests for a single component are applied in lexicographic order.

The CVO then applies manifests following the generated dependency graph.

Note

For some resource types, the CVO monitors the resource after its manifest is applied, and considers it to be successfully updated only after the resource reaches a stable state. Achieving this state can take some time. This is especially true for `ClusterOperator` resources, while the CVO waits for a cluster Operator to update itself and then update its `ClusterOperator` status.

The CVO waits until all cluster Operators in the Runlevel meet the following conditions before it proceeds to the next Runlevel:

* The cluster Operators have an `Available=True` condition.
* The cluster Operators have a `Degraded=False` condition.
* The cluster Operators declare they have achieved the desired version in their ClusterOperator resource.

Some actions can take significant time to finish. The CVO waits for the actions to complete in order to ensure the subsequent Runlevels can proceed safely. Initially reconciling the new release’s manifests is expected to take 60 to 120 minutes in total; see **Understanding OpenShift Container Platform update duration** for more information about factors that influence update duration.

In the previous example diagram, the CVO is waiting until all work is completed at Runlevel 20. The CVO has applied all manifests to the Operators in the Runlevel, but the `kube-apiserver-operator ClusterOperator` performs some actions after its new version was deployed. The `kube-apiserver-operator ClusterOperator` declares this progress through the `Progressing=True` condition and by not declaring the new version as reconciled in its `status.versions`. The CVO waits until the ClusterOperator reports an acceptable status, and then it will start reconciling manifests at Runlevel 25.

#### [1.2.6. Understanding how the Machine Config Operator updates nodes](#mco-update-process_how-updates-work) Copy linkLink copied to clipboard!

The Machine Config Operator (MCO) applies a new machine configuration to each control plane node and compute node. During the machine configuration update, control plane nodes and compute nodes are organized into their own machine config pools, where the pools of machines are updated in parallel.

The `.spec.maxUnavailable` parameter, which has a default value of `1`, determines how many nodes in a machine config pool can simultaneously undergo the update process.

Warning

The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.

When the machine configuration update process begins, the MCO checks the amount of currently unavailable nodes in a pool. If there are fewer unavailable nodes than the value of `.spec.maxUnavailable`, the MCO initiates the following sequence of actions on available nodes in the pool:

1. Cordon and drain the node

   Note

   When a node is cordoned, workloads cannot be scheduled to it.
2. Update the system configuration and operating system (OS) of the node
3. Reboot the node
4. Uncordon the node

A node undergoing this process is unavailable until it is uncordoned and workloads can be scheduled to it again. The MCO begins updating nodes until the number of unavailable nodes is equal to the value of `.spec.maxUnavailable`.

As a node completes its update and becomes available, the number of unavailable nodes in the machine config pool is once again fewer than `.spec.maxUnavailable`. If there are remaining nodes that need to be updated, the MCO initiates the update process on a node until the `.spec.maxUnavailable` limit is once again reached. This process repeats until each control plane node and compute node has been updated.

The following example workflow describes how this process might occur in a machine config pool with 5 nodes, where `.spec.maxUnavailable` is 3 and all nodes are initially available:

1. The MCO cordons nodes 1, 2, and 3, and begins to drain them.
2. Node 2 finishes draining, reboots, and becomes available again. The MCO cordons node 4 and begins draining it.
3. Node 1 finishes draining, reboots, and becomes available again. The MCO cordons node 5 and begins draining it.
4. Node 3 finishes draining, reboots, and becomes available again.
5. Node 5 finishes draining, reboots, and becomes available again.
6. Node 4 finishes draining, reboots, and becomes available again.

Because the update process for each node is independent of other nodes, some nodes in the example above finish their update out of the order in which they were cordoned by the MCO.

You can check the status of the machine configuration update by running the following command:

```
$ oc get mcp
```

**Example output**

```
NAME         CONFIG                                                 UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master       rendered-master-acd1358917e9f98cbdb599aea622d78b       True      False      False      3              3                   3                     0                      22h
worker       rendered-worker-1d871ac76e1951d32b2fe92369879826       False     True       False      2              1                   1                     0                      22h
```

### [1.3. Understanding update channels and releases](#understanding-update-channels-releases) Copy linkLink copied to clipboard!

Update channels are the mechanism by which users declare the OpenShift Container Platform minor version they intend to update their clusters to. They also allow users to choose the timing and level of support their updates will have through the `fast`, `stable`, `candidate`, and `eus` channel options.

The Cluster Version Operator uses an update graph based on the channel declaration, along with other conditional information, to provide a list of recommended and conditional updates available to the cluster.

#### [1.3.1. Overview of update channels](#understanding-update-channels-overview_understanding-update-channels-releases) Copy linkLink copied to clipboard!

Update channels correspond to a minor version of OpenShift Container Platform. The version number in the channel represents the target minor version that the cluster will eventually be updated to, even if it is higher than the cluster’s current minor version.

For instance, OpenShift Container Platform 4.10 update channels provide the following recommendations:

* Updates within 4.10.
* Updates within 4.9.
* Updates from 4.9 to 4.10, allowing all 4.9 clusters to eventually update to 4.10, even if they do not immediately meet the minimum z-stream version requirements.
* `eus-4.10` only: updates within 4.8.
* `eus-4.10` only: updates from 4.8 to 4.9 to 4.10, allowing all 4.8 clusters to eventually update to 4.10.

4.10 update channels do not recommend updates to 4.11 or later releases. This strategy ensures that administrators must explicitly decide to update to the next minor version of OpenShift Container Platform.

Update channels control only release selection and do not impact the version of the cluster that you install. The `openshift-install` binary file for a specific version of OpenShift Container Platform always installs that version.

OpenShift Container Platform 4.22 offers the following update channels:

* `stable-4.22`
* `eus-4.y` (only offered for EUS versions and meant to facilitate updates between EUS versions)
* `fast-4.22`
* `candidate-4.22`

If you do not want the Cluster Version Operator to fetch available updates from the update recommendation service, you can use the `oc adm upgrade channel` command in the OpenShift CLI to configure an empty channel. This configuration can be helpful if, for example, a cluster has restricted network access and there is no local, reachable update recommendation service.

Warning

Red Hat recommends updating only to versions suggested by OpenShift Update Service. For a minor version update, versions must be contiguous. Red Hat does not test updates to noncontiguous versions and cannot guarantee compatibility with earlier versions.

#### [1.3.2. Update channels](#understanding-update-channels_understanding-update-channels-releases) Copy linkLink copied to clipboard!

OpenShift Container Platform offers several update channels for you to choose from, depending on your desired update strategy.

##### [1.3.2.1. fast-4.22 channel](#fast-version-channel_understanding-update-channels-releases) Copy linkLink copied to clipboard!

The `fast-4.22` channel is updated with new versions of OpenShift Container Platform 4.22 as soon as Red Hat declares the version as a general availability (GA) release. As such, these releases are fully supported and purposed to be used in production environments.

##### [1.3.2.2. stable-4.22 channel](#stable-version-channel_understanding-update-channels-releases) Copy linkLink copied to clipboard!

While the `fast-4.22` channel contains releases as soon as their errata are published, releases are added to the `stable-4.22` channel after a delay. During this delay, data is collected from multiple sources and analyzed for indications of product regressions. Once a significant number of data points have been collected, these releases are added to the stable channel.

Note

Since the time required to obtain a significant number of data points varies based on many factors, Service LeveL Objective (SLO) is not offered for the delay duration between fast and stable channels. For more information, please see "Choosing the correct channel for your cluster"

Newly installed clusters default to using stable channels.

##### [1.3.2.3. eus-4.y channel](#eus-4y-channel_understanding-update-channels-releases) Copy linkLink copied to clipboard!

In addition to the stable channel, all even-numbered minor versions of OpenShift Container Platform offer [Extended Update Support](https://access.redhat.com/support/policy/updates/openshift#ocp4_phases) (EUS). Releases promoted to the stable channel are also simultaneously promoted to the EUS channels. The primary purpose of the EUS channels is to serve as a convenience for clusters performing a Control Plane Only update.

Note

Both standard and non-EUS subscribers can access all EUS repositories and necessary RPMs (`rhel-*-eus-rpms`) to be able to support critical purposes such as debugging and building drivers.

##### [1.3.2.4. candidate-4.22 channel](#candidate-version-channel_understanding-update-channels-releases) Copy linkLink copied to clipboard!

The `candidate-4.22` channel offers unsupported early access to releases as soon as they are built. Releases present only in candidate channels may not contain the full feature set of eventual GA releases or features may be removed prior to GA. Additionally, these releases have not been subject to full Red Hat Quality Assurance and may not offer update paths to later GA releases. Given these caveats, the candidate channel is only suitable for testing purposes where destroying and recreating a cluster is acceptable.

#### [1.3.3. Restricted network clusters](#restricted-network-clusters_understanding-update-channels-releases) Copy linkLink copied to clipboard!

If you manage the container images for your OpenShift Container Platform clusters yourself, you must consult the Red Hat errata that is associated with product releases and note any comments that impact updates.

During an update, the user interface might warn you about switching between these versions, so you must ensure that you selected an appropriate version before you bypass those warnings.

#### [1.3.4. Update recommendations in the channel](#upgrade-version-paths_understanding-update-channels-releases) Copy linkLink copied to clipboard!

OpenShift Container Platform maintains an update recommendation service that knows your installed OpenShift Container Platform version and the path to take within the channel to get you to the next release.

Update paths are also limited to versions relevant to your currently selected channel and its promotion characteristics.

You can imagine seeing the following releases in your channel:

* 4.22.0
* 4.22.1
* 4.22.3
* 4.22.4

The service recommends only updates that have been tested and have no known serious regressions. For example, if your cluster is on 4.22.1 and OpenShift Container Platform suggests 4.22.4, then it is recommended to update from 4.22.1 to 4.22.4.

Important

Do not rely on consecutive patch numbers. In this example, 4.22.2 is not and never was available in the channel, therefore updates to 4.22.2 are not recommended or supported.

#### [1.3.5. Update recommendations and Conditional Updates](#conditional-updates-overview_understanding-update-channels-releases) Copy linkLink copied to clipboard!

Red Hat monitors newly released versions and update paths associated with those versions before and after they are added to supported channels.

If Red Hat removes update recommendations from any supported release, a superseding update recommendation will be provided to a future version that corrects the regression. There may however be a delay while the defect is corrected, tested, and promoted to your selected channel.

Beginning in OpenShift Container Platform 4.10, when update risks are confirmed, they are declared as Conditional Update risks for the relevant updates. Each known risk may apply to all clusters or only clusters matching certain conditions. Some examples include having the `Platform` set to `None` or the CNI provider set to `OpenShiftSDN`. The Cluster Version Operator (CVO) continually evaluates known risks against the current cluster state. If no risks match, the update is recommended. If the risk matches, those update paths are labeled as *updates with known issues*, and a reference link to the known issues is provided. The reference link helps the cluster admin decide if they want to accept the risk and continue to update their cluster.

When Red Hat chooses to declare Conditional Update risks, that action is taken in all relevant channels simultaneously. Declaration of a Conditional Update risk may happen either before or after the update has been promoted to supported channels.

#### [1.3.6. What to consider when choosing an update channel](#fast-stable-channel-strategies_understanding-update-channels-releases) Copy linkLink copied to clipboard!

Choosing the appropriate update channel for your cluster involves two decisions.

First, select the minor version you want for your cluster update. Selecting a channel which matches your current version ensures that you only apply z-stream updates and do not receive feature updates. Selecting an available channel which has a version greater than your current version will ensure that after one or more updates your cluster will have updated to that version. Your cluster will only be offered channels which match its current version, the next version, or the next EUS version.

Note

Due to the complexity involved in planning updates between versions many minors apart, channels that assist in planning updates beyond a single Control Plane Only update are not offered.

Second, you should choose your desired rollout strategy. You may choose to update as soon as Red Hat declares a release GA by selecting from fast channels or you may want to wait for Red Hat to promote releases to the stable channel. Update recommendations offered in the `fast-4.22` and `stable-4.22` are both fully supported and benefit equally from ongoing data analysis. The promotion delay before promoting a release to the stable channel represents the only difference between the two channels. Updates to the latest z-streams are generally promoted to the stable channel within a week or two, however the delay when initially rolling out updates to the latest minor is much longer, generally 45-90 days. Please consider the promotion delay when choosing your desired channel, as waiting for promotion to the stable channel may affect your scheduling plans.

Additionally, there are several factors which may lead an organization to move clusters to the fast channel either permanently or temporarily including the following:

* The desire to apply a specific fix known to affect your environment without delay.
* Application of CVE fixes without delay. CVE fixes may introduce regressions, so promotion delays still apply to z-streams with CVE fixes.
* Internal testing processes. If it takes your organization several weeks to qualify releases it is best test concurrently with our promotion process rather than waiting. This also assures that any telemetry signal provided to Red Hat is a factored into our rollout, so issues relevant to you can be fixed faster.

#### [1.3.7. Considerations for switching between channels](#switching-between-channels_understanding-update-channels-releases) Copy linkLink copied to clipboard!

You can switch your cluster’s update channel through the web console or the CLI, in order to access different update recommendations for your cluster.

You can switch the channel from the CLI by running the following command:

```
$ oc adm upgrade channel <channel>
```

The web console will display an alert if you switch to a channel that does not include the current release. The web console does not recommend any updates while on a channel without the current release. You can return to the original channel at any point, however.

Changing your channel might impact the supportability of your cluster. The following conditions might apply:

* Your cluster is still supported if you change from the `stable-4.22` channel to the `fast-4.22` channel.
* You can switch to the `candidate-4.22` channel at any time, but some releases for this channel might be unsupported.
* You can switch from the `candidate-4.22` channel to the `fast-4.22` channel if your current release is a general availability release.
* You can always switch from the `fast-4.22` channel to the `stable-4.22` channel. There is a possible delay of up to a day for the release to be promoted to `stable-4.22` if the current release was recently promoted.

### [1.4. Understanding OpenShift Container Platform update duration](#understanding-openshift-update-duration) Copy linkLink copied to clipboard!

OpenShift Container Platform update duration varies based on the deployment topology. You can understand the factors that affect update duration and use them to estimate how long the cluster update takes in your environment.

#### [1.4.1. Factors affecting update duration](#factors-affecting-update-duration_openshift-update-duration) Copy linkLink copied to clipboard!

The duration of OpenShift Container Platform updates vary for several reasons.

The following factors can affect your cluster update duration:

* The reboot of compute nodes to the new machine configuration by Machine Config Operator (MCO)

  + The value of `MaxUnavailable` in the machine config pool

    Warning

    The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.
  + The minimum number or percentages of replicas set in pod disruption budget (PDB)
* The number of nodes in the cluster
* The health of the cluster nodes

#### [1.4.2. Cluster update phases](#cluster-update-phases_openshift-update-duration) Copy linkLink copied to clipboard!

OpenShift Container Platform updates are done in multiple phases.

The cluster update happens in the following two phases:

* Cluster Version Operator (CVO) target update payload deployment
* Machine Config Operator (MCO) node updates

##### [1.4.2.1. Cluster Version Operator target update payload deployment](#cluster-version-operator_openshift-update-duration) Copy linkLink copied to clipboard!

In the first phase of the update, the Cluster Version Operator (CVO) retrieves the target update release image and applies to the cluster.

All components which run as pods are updated during this phase, whereas the host components are updated by the Machine Config Operator (MCO). This process might take 60 to 120 minutes.

Note

The CVO phase of the update does not restart the nodes.

##### [1.4.2.2. Machine Config Operator node updates](#machine-config-operator-node-updates_openshift-update-duration) Copy linkLink copied to clipboard!

In the second phase of the update, the Machine Config Operator (MCO) applies a new machine configuration to each control plane and compute node.

During this process, the MCO performs the following sequential actions on each node of the cluster:

1. Cordon and drain all the nodes
2. Update the operating system (OS)
3. Reboot the nodes
4. Uncordon all nodes and schedule workloads on the node

Note

When a node is cordoned, workloads cannot be scheduled to it.

The time to complete this process depends on several factors including the node and infrastructure configuration. This process might take 5 or more minutes to complete per node.

In addition to MCO, you should consider the impact of the following parameters:

* The control plane node update duration is predictable and oftentimes shorter than compute nodes, because the control plane workloads are tuned for graceful updates and quick drains.
* You can update the compute nodes in parallel by setting the `maxUnavailable` field to greater than `1` in the Machine Config Pool (MCP). The MCO cordons the number of nodes specified in `maxUnavailable` and marks them unavailable for update.
* When you increase `maxUnavailable` on the MCP, it can help the pool to update more quickly. However, if `maxUnavailable` is set too high, and several nodes are cordoned simultaneously, the pod disruption budget (PDB) guarded workloads could fail to drain because a schedulable node cannot be found to run the replicas. If you increase `maxUnavailable` for the MCP, ensure that you still have sufficient schedulable nodes to allow PDB guarded workloads to drain.
* Before you begin the update, you must ensure that all the nodes are available. Any unavailable nodes can significantly impact the update duration because the node unavailability affects the `maxUnavailable` and pod disruption budgets.

  To check the status of nodes from the terminal, run the following command:

  ```
  $ oc get node
  ```

  **Example Output**

  ```
  NAME                                        STATUS                      ROLES   AGE     VERSION
  ip-10-0-137-31.us-east-2.compute.internal   Ready,SchedulingDisabled    worker  12d     v1.23.5+3afdacb
  ip-10-0-151-208.us-east-2.compute.internal  Ready                       master  12d     v1.23.5+3afdacb
  ip-10-0-176-138.us-east-2.compute.internal  Ready                       master  12d     v1.23.5+3afdacb
  ip-10-0-183-194.us-east-2.compute.internal  Ready                       worker  12d     v1.23.5+3afdacb
  ip-10-0-204-102.us-east-2.compute.internal  Ready                       master  12d     v1.23.5+3afdacb
  ip-10-0-207-224.us-east-2.compute.internal  Ready                       worker  12d     v1.23.5+3afdacb
  ```

  If the status of the node is `NotReady` or `SchedulingDisabled`, then the node is not available and this impacts the update duration.

  You can also check the status of nodes from the **Administrator** perspective in the web console by expanding **Compute** → **Nodes**.

##### [1.4.2.3. Example update duration of cluster Operators](#update-duration-example_openshift-update-duration) Copy linkLink copied to clipboard!

You can review an example of the update duration for cluster Operators to better understand the factors that affect the duration of the update.

The previous diagram shows an example of the time that cluster Operators might take to update to their new versions. The example is based on a three-node AWS OVN cluster, which has a healthy compute `MachineConfigPool` and no workloads that take long to drain, updating from 4.13 to 4.14.

Note

* The specific update duration of a cluster and its Operators can vary based on several cluster characteristics, such as the target version, the amount of nodes, and the types of workloads scheduled to the nodes.
* Some Operators, such as the Cluster Version Operator, update themselves in a short amount of time. These Operators have either been omitted from the diagram or are included in the broader group of Operators labeled "Other Operators in parallel".

Each cluster Operator has characteristics that affect the time it takes to update itself. For instance, the Kube API Server Operator in this example took more than eleven minutes to update because `kube-apiserver` provides graceful termination support, meaning that existing, in-flight requests are allowed to complete gracefully. This might result in a longer shutdown of the `kube-apiserver`. In the case of this Operator, update speed is sacrificed to help prevent and limit disruptions to cluster functionality during an update.

Another characteristic that affects the update duration of an Operator is whether the Operator utilizes DaemonSets. The Network and DNS Operators utilize full-cluster DaemonSets, which can take time to roll out their version changes, and this is one of several reasons why these Operators might take longer to update themselves.

Additionally, the update duration for some Operators is heavily dependent on characteristics of the cluster itself. For example, the Machine Config Operator update applies machine configuration changes to each node in the cluster. A cluster with many nodes has a longer update duration for the Machine Config Operator compared to a cluster with fewer nodes.

Note

Each cluster Operator is assigned a stage during which it can be updated. Operators within the same stage can update simultaneously, and Operators in a given stage cannot begin updating until all previous stages have been completed. For more information, see "Understanding how manifests are applied during an update".

#### [1.4.3. How to estimate cluster update time](#estimating-cluster-update-time_openshift-update-duration) Copy linkLink copied to clipboard!

Historical update duration of similar clusters provides you the best estimate for the future cluster updates. If you do not have historical data, you can calculate an estimate of the update duration.

You can use the following convention to estimate your cluster update time:

```
Cluster update time = CVO target update payload deployment time + (# node update iterations x MCO node update time)
```

A node update iteration consists of one or more nodes updated in parallel. The control plane nodes are always updated in parallel with the compute nodes. In addition, one or more compute nodes can be updated in parallel based on the `maxUnavailable` value.

Warning

The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.

For example, to estimate the update time, consider an OpenShift Container Platform cluster with three control plane nodes and six compute nodes, where each host takes about 5 minutes to reboot.

Note

The time it takes to reboot a particular node varies significantly. In cloud instances, the reboot might take about 1 to 2 minutes, whereas in physical bare metal hosts the reboot might take more than 15 minutes.

In a scenario where you set `maxUnavailable` to `1` for both the control plane and compute nodes Machine Config Pool (MCP), then all the six compute nodes will update one after another in each iteration:

```
Cluster update time = 60 + (6 x 5) = 90 minutes
```

In a scenario where you set `maxUnavailable` to `2` for the compute node MCP, then two compute nodes will update in parallel in each iteration. Therefore it takes total three iterations to update all the nodes.

```
Cluster update time = 60 + (3 x 5) = 75 minutes
```

Important

The default setting for `maxUnavailable` is `1` for all the MCPs in OpenShift Container Platform. It is recommended that you do not change the `maxUnavailable` in the control plane MCP.

## [Chapter 2. Preparing to update a cluster](#preparing-to-update-a-cluster) Copy linkLink copied to clipboard!

### [2.1. Preparing to update to OpenShift Container Platform 4.22](#updating-cluster-prepare) Copy linkLink copied to clipboard!

Before you update your OpenShift Container Platform cluster, complete the required administrative tasks and review best practices to minimize disruption and avoid update failures.

#### [2.1.1. Kubernetes API removals](#kube-api-removals_updating-cluster-prepare) Copy linkLink copied to clipboard!

There are no Kubernetes API removals in this release.

#### [2.1.2. Providing an administrator acknowledgment for Microsoft Azure or VMware vSphere clusters](#update-preparing-azure-vsphere-ack_updating-cluster-prepare) Copy linkLink copied to clipboard!

If you are updating a Microsoft Azure or VMware vSphere cluster from OpenShift Container Platform 4.21 to 4.22, and you have not configured the `managedBootImages` parameter, the update is blocked with a "*This cluster is Azure or vSphere but lacks a boot image configuration.*" message.

The update is blocked intentionally on Azure or vSphere clusters in order to alert you that the default updated boot image behavior is changing between version 4.21 and 4.22 to enable updated boot images by default on those platforms.

To allow the update, you must perform one of the following tasks:

* If you want to allow the feature to be enabled, you must provide an administrator acknowledgment as described in the following procedure before you can update your cluster.
* If you do not want the updated boot image feature enabled, you must explicitly disable the feature for compute nodes and then update your cluster. For more information, see "Disabling boot image management".

**Prerequisite**

* You must have access to the cluster as a user with the `cluster-admin` role.

**Procedure**

* Acknowledge that you are aware of the change in the default behavior by running the following command:

  ```
  $ oc -n openshift-config patch cm admin-acks --patch '{"data":{"ack-4.21-boot-image-opt-out-in-4.22":"true"}}' --type=merge
  ```

#### [2.1.3. Self-service Technical Supportability Review](#about-self-service-tsr_updating-cluster-prepare) Copy linkLink copied to clipboard!

You can use the self-service Technical Supportability Review (TSR) on the Red Hat Customer Portal to validate your cluster configuration against Red Hat common practices.

Note

The `must-gather` tool collects diagnostic information about your cluster, including resource definitions, service logs, and configuration data. For more information, see "Gathering data about your cluster" in the OpenShift Container Platform documentation.

The self-service TSR uses AI to evaluate your cluster’s `must-gather` data and provides a prioritized executive summary of recommendations. This serves as a starting point to help you identify and resolve potential issues before they impact your environment.

The TSR performs hundreds of checks across the OpenShift Container Platform platform, including OpenShift Virtualization. Coverage is continually expanding.

##### [2.1.3.1. When to use the self-service TSR tool](#when-to-use-self-service-tsr_updating-cluster-prepare) Copy linkLink copied to clipboard!

Integrating the self-service TSR into your regular operational workflow can be helpful in the following scenarios:

Routine benchmarking
:   Use the TSR quarterly to benchmark cluster health and plan for routine maintenance activities.

Pre-flight checks
:   Validate your cluster configuration before major structural changes, including upgrades, migrations, and expansions.

Critical event preparation
:   Confirm cluster stability ahead of high-traffic business events, such as seasonal peaks, or operational milestones, such as year-end shutdowns, business continuity drills, and compliance audits.

##### [2.1.3.2. How to access the TSR](#how-to-access-tsr_updating-cluster-prepare) Copy linkLink copied to clipboard!

To run a self-service review, upload your cluster’s `must-gather` data to the **Analyze** tab in the **Support** section of the Red Hat Customer Portal. For a direct link, see "Technical Supportability Review with AI tool" in the Additional resources section. The **Analyze** feature generates a prioritized executive summary that identifies your cluster’s top risks and recommends corrective actions. Review the recommendations and implement the suggested corrective actions to address the identified risks.

The self-service TSR provides a solid baseline for cluster health. If you need additional guidance or a more comprehensive review, contact your Red Hat account team to arrange an assisted review through a Technical Account Manager (TAM) or Red Hat consultant. An assisted review includes human analysis, deeper coverage, and access to checks that are updated more frequently than the self-service version.

#### [2.1.4. The risk of conditional updates](#update-preparing-conditional_updating-cluster-prepare) Copy linkLink copied to clipboard!

Conditional updates are update targets flagged by the OpenShift Update Service (OSUS) as available but not recommended due to known risks that apply to your cluster.

The Cluster Version Operator (CVO) periodically queries the OSUS for the most recent data about update recommendations, and some potential update targets might have risks associated with them.

The CVO evaluates the conditional risks, and if the risks are not applicable to the cluster, then the target version is available as a recommended update path for the cluster. If the risk is determined to be applicable, or if for some reason CVO cannot evaluate the risk, then the update target is available to the cluster as a conditional update.

When you encounter a conditional update while you are trying to update to a target version, you must assess the risk of updating your cluster to that version. Generally, if you do not have a specific need to update to that target version, it is best to wait for a recommended update path from Red Hat.

However, if you have a strong reason to update to that version, for example, if you need to fix an important CVE, then the benefit of fixing the CVE might outweigh the risk of the update being problematic for your cluster. You can complete the following tasks to determine whether you agree with the Red Hat assessment of the update risk:

* Complete extensive testing in a non-production environment to the extent that you are comfortable completing the update in your production environment.
* Follow the links provided in the conditional update description, investigate the bug, and determine if it is likely to cause issues for your cluster. If you need help understanding the risk, contact Red Hat Support.

#### [2.1.5. etcd backups before cluster updates](#update-etcd-backup_updating-cluster-prepare) Copy linkLink copied to clipboard!

Create etcd backups before you update clusters to preserve your cluster state and to enable disaster recovery.

etcd backups record the state of your cluster and all of its resource objects. You can use backups to try to restore the state of a cluster when the cluster has become unrecoverable.

In the context of updates, you can attempt an etcd restoration of the cluster if an update introduced catastrophic conditions that cannot be fixed without reverting to the previous cluster version.

etcd restorations might be destructive and destabilizing to a running cluster, use them only as a last resort.

Warning

Due to their high consequences, etcd restorations are not intended to be used as a rollback solution. Rolling your cluster back to a previous version is not supported. If your update is failing to complete, contact Red Hat support.

There are several factors that affect the viability of an etcd restoration. For more information, see "Backing up etcd data" and "Restoring to an earlier cluster state".

#### [2.1.6. Using the oc adm upgrade recommend command to identify update risks](#oc-adm-upgrade-recommend_updating-cluster-prepare) Copy linkLink copied to clipboard!

To identify potential update risks before initiating a cluster update, you can use the `oc adm upgrade recommend` command.

When you run the `oc adm upgrade recommend` command, the output displays the following information:

* Any issues that cause the Cluster Version Operator to have a status of `Failing=True`
* Any firing alerts that might be a cause for concern about a cluster update
* Information about your current update channel and your cluster’s update service
* Recommended target versions and any relevant known issues associated with each version

You can use the information provided by the output to make informed decisions about the state of your cluster. Examples include whether any critical cluster issues should be addressed before attempting an update, or which specific target version would have less risk for your cluster.

Note

The `oc adm upgrade recommend` command is read-only and does not affect the state of the cluster. To request an update, use the `oc adm upgrade` command.

**Prerequisites**

* You installed the latest version of OpenShift CLI (`oc`).
* You are logged in with a token-based identity, such as `kubeadmin`, by using the `oc login` command.

  Note

  The `oc adm upgrade recommend` command requires a bearer token to query the cluster’s Thanos monitoring service for firing alerts. Certificate-based authentication, such as the `system:admin` identity provided in the default `kubeconfig` file from the installation program, does not satisfy this requirement. If you use certificate-based authentication, the command output displays the following message and skips all alert-based precondition checks:

  ```
  Failed to check for at least some preconditions: no token is currently in use for this session
  ```

**Procedure**

* Identify potential update risks and view recommended update versions by running the following command:

  ```
  $ oc adm upgrade recommend
  ```

  **Example output**

  ```
  The following conditions found no cause for concern in updating this cluster to later releases: recommended/CriticalAlerts (AsExpected), recommended/NodeAlerts (AsExpected), recommended/PodDisruptionBudgetAlerts (AsExpected), recommended/PodImagePullAlerts (AsExpected), recommended/UpdatePrecheckAlerts (AsExpected)

  Upstream update service is unset, so the cluster will use an appropriate default.
  Channel: stable-4.21 (available channels: candidate-4.20, candidate-4.21, candidate-4.22, eus-4.20, fast-4.20, fast-4.21, stable-4.20, stable-4.21)

  Updates to 4.21:
    VERSION     ISSUES
    4.21.14     no known issues relevant to this cluster
    4.21.13     no known issues relevant to this cluster
  And 2 older 4.21 updates you can see with '--show-outdated-releases' or '--version VERSION'.

  Updates to 4.20:
    VERSION     ISSUES
    4.20.20     no known issues relevant to this cluster
  ```

##### [2.1.6.1. Adding custom alerts to oc adm upgrade recommend command output](#oc-adm-upgrade-recommend-custom-alert_updating-cluster-prepare) Copy linkLink copied to clipboard!

You can configure specific alerts to be checked by the `oc adm upgrade recommend` command, so that if they are firing they appear in the output of the command. To do this, add the `openShiftUpdatePrecheck` label to an alert and set it to true.

**Procedure**

1. Edit a `PrometheusRule` custom resource (CR) by running the following command:

   ```
   $ oc edit prometheusrule <rule_name> -n <namespace>
   ```

   where:

   `<rule_name>`
   :   Specifies the name of the `PrometheusRule` CR.

   `<namespace>`
   :   Specifies the namespace that contains the CR.
2. Add the following snippet to the `labels` section of the alert you want to be checked by the `oc adm upgrade recommend` command:

   ```
   # ...
        labels:
          openShiftUpdatePrecheck: "true"
   # ...
   ```

   **Example `PrometheusRule` CR with precheck label**

   ```
   apiVersion: monitoring.coreos.com/v1
   kind: PrometheusRule
   metadata:
     name: storage-warning-alerts
     namespace: openshift-monitoring
   spec:
     groups:
     - name: disk-usage-warnings
       rules:
       - alert: VolumeNearingCapacity
         expr: (kubelet_volume_stats_used_bytes / kubelet_volume_stats_capacity_bytes) > 0.85
         for: 15m
         labels:
           severity: warning
           openShiftUpdatePrecheck: "true"
         annotations:
           summary: "Storage volume is over 85% full"
           description: "The volume {{ $labels.persistentvolumeclaim }} in namespace {{ $labels.namespace }} is currently {{ $value | humanizePercentage }} full. This may cause issues during pod restarts or cluster updates."
   ```

##### [2.1.6.2. Accepting risks with the oc adm upgrade recommend command](#oc-adm-upgrade-recommend-accept_updating-cluster-prepare) Copy linkLink copied to clipboard!

You can use a command flag to explicitly accept update risks that are shown in the output of the `oc adm upgrade recommend` command.

**Procedure**

1. Check for update risks by running the following command:

   ```
   $ oc adm upgrade recommend
   ```

   **Example output**

   ```
   The following conditions found no cause for concern in updating this cluster to later releases: recommended/CriticalAlerts (AsExpected), recommended/NodeAlerts (AsExpected), recommended/PodDisruptionBudgetAlerts (AsExpected), recommended/PodImagePullAlerts (AsExpected)

   The following conditions found cause for concern in updating this cluster to later releases: recommended/UpdatePrecheckAlerts/TestAlert/0

   recommended/UpdatePrecheckAlerts/TestAlert/0=False:

     Reason: Alert:firing
     Message: warning alert TestAlert firing, suggesting issues worth investigating before updating the cluster. Test alert for updates. The alert description is: Test alert for updates <alert does not have a runbook_url annotation>

   Upstream update service is unset, so the cluster will use an appropriate default.
   Channel: stable-4.21 (available channels: candidate-4.20, candidate-4.21, candidate-4.22, eus-4.20, fast-4.20, fast-4.21, stable-4.20, stable-4.21)

   Updates to 4.21:
     VERSION     ISSUES
     4.21.14     no known issues relevant to this cluster
     4.21.13     no known issues relevant to this cluster
   And 2 older 4.21 updates you can see with '--show-outdated-releases' or '--version VERSION'.

   Updates to 4.20:
     VERSION     ISSUES
     4.20.20     no known issues relevant to this cluster
   ```

   In this example, `TestAlert` is the name of the alert that is firing on the cluster and is considered a risk to a cluster update. Alerts that are identified as update risks might be changed over time.
2. Accept update risks by running the following command:

   ```
   $ oc adm upgrade recommend --accept <risk_name>
   ```

   Replace `<risk_name>` with the name of the risk you want to accept. You can accept multiple risks at once by separating each risk by a comma, for example `risk1,risk2,risk3`.

   **Example command**

   ```
   $ oc adm upgrade recommend --accept TestAlert
   ```

   **Example output**

   ```
   The following conditions found no cause for concern in updating this cluster to later releases: recommended/CriticalAlerts (AsExpected), recommended/NodeAlerts (AsExpected), recommended/PodDisruptionBudgetAlerts (AsExpected), recommended/PodImagePullAlerts (AsExpected)

   The following conditions found cause for concern in updating this cluster to later releases, but were explicitly accepted via --accept: recommended/UpdatePrecheckAlerts/TestAlert/0

   Upstream update service is unset, so the cluster will use an appropriate default.
   Channel: stable-4.21 (available channels: candidate-4.20, candidate-4.21, candidate-4.22, eus-4.20, fast-4.20, fast-4.21, stable-4.20, stable-4.21)

   Updates to 4.21:
     VERSION     ISSUES
     4.21.14     no known issues relevant to this cluster
     4.21.13     no known issues relevant to this cluster
   And 2 older 4.21 updates you can see with '--show-outdated-releases' or '--version VERSION'.

   Updates to 4.20:
     VERSION     ISSUES
     4.20.20     no known issues relevant to this cluster
   ```

#### [2.1.7. Preparing for Gateway API management succession by the Ingress Operator](#nw-ingress-gateway-api-manage-succession_updating-cluster-prepare) Copy linkLink copied to clipboard!

Prepare your cluster for Gateway API management succession by removing existing unsupported definitions and installing compliant resources. This ensures a seamless update to OpenShift Container Platform 4.19 and prevents conflicts with the Ingress Operator.

Starting in OpenShift Container Platform 4.19, the Ingress Operator manages the lifecycle of any Gateway API custom resource definitions (CRDs). This lifecycle control blocks you from creating, updating, or deleting CRDs within the `gateway.networking.k8s.io` API group.

Note

Starting in OpenShift Container Platform 4.22, deploying the Gateway API CRD `gateway.networking.x-k8s.io` is no longer restricted. You can deploy that CRD without interference from the Ingress Operator. Experimental Gateway API CRDs in the `gateway.networking.k8s.io` group remain restricted.

Warning

Updating or deleting Gateway API resources can result in downtime and loss of service or data. Be sure you understand how this affects your cluster before performing the steps in this procedure. If necessary, back up any Gateway API objects in YAML format to restore them later.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have access to an OpenShift Container Platform account with cluster administrator access.
* Optional: You have backed up any necessary Gateway API objects.

Warning

Backup and restore can fail or result in data loss for any CRD fields that were present in the old definitions but are absent in the new definitions.

**Procedure**

1. List all the Gateway API CRDs that you must remove by entering the following command:

   ```
   $ oc get crd | grep -F -e gateway.networking.k8s.io -e gateway.networking.x-k8s.io
   ```

   **Example output**

   ```
   gatewayclasses.gateway.networking.k8s.io
   gateways.gateway.networking.k8s.io
   grpcroutes.gateway.networking.k8s.io
   httproutes.gateway.networking.k8s.io
   referencegrants.gateway.networking.k8s.io
   ```

   If the output lists custom resource definitions (CRDs) for `gateway.networking.x-k8s.io`, retain those resources. The subsequent step removes only CRDs that belong to the `gateway.networking.k8s.io` group.
2. Delete the Gateway API CRDs from the previous step by entering the following command:

   ```
   $ oc delete crd gatewayclasses.gateway.networking.k8s.io && \
   oc delete crd gateways.gateway.networking.k8s.io && \
   oc delete crd grpcroutes.gateway.networking.k8s.io && \
   oc delete crd httproutes.gateway.networking.k8s.io && \
   oc delete crd referencegrants.gateway.networking.k8s.io
   ```

   Important

   Deleting CRDs removes every custom resource that relies on them and can result in data loss. Back up any necessary data before deleting the Gateway API CRDs. Any controller that was previously managing the lifecycle of the Gateway API CRDs ceases to function correctly. Attempting to force its use in conjunction with the Ingress Operator to manage Gateway API CRDs might prevent the cluster update from succeeding.
3. Get the supported Gateway API CRDs by entering the following command:

   ```
   $ oc apply -f https://github.com/kubernetes-sigs/gateway-api/releases/download/v1.2.1/standard-install.yaml
   ```

   Warning

   You can perform this step without deleting your CRDs. If your update to a CRD removes a field that is used by a custom resource, you can lose data. Updating a CRD a second time, to a version that re-adds a field, can cause any previously deleted data to reappear. Any third-party controller that depends on a specific Gateway API CRD version that is not supported in OpenShift Container Platform 4.22 breaks upon updating that CRD to one supported by Red Hat.

   For more information on the OpenShift Container Platform implementation and the dead fields issue, see *Gateway API implementation for OpenShift Container Platform*.

#### [2.1.8. Best practices for cluster updates](#update-best-practices_updating-cluster-prepare) Copy linkLink copied to clipboard!

Follow best practices to ensure successful cluster updates. These best practices include selecting recommended versions, resolving critical alerts, maintaining spare node capacity, and properly configuring pod disruption budgets.

OpenShift Container Platform minimizes workload disruptions during an update. Updates do not begin unless the cluster is in an upgradeable state at the time of the update request.

This design enforces some key conditions before initiating an update, but there are several actions you can take to increase your chances of a successful cluster update.

##### [2.1.8.1. Choose versions recommended by the OpenShift Update Service](#recommended-versions_updating-cluster-prepare) Copy linkLink copied to clipboard!

The OpenShift Update Service (OSUS) provides update recommendations based on cluster characteristics such as the cluster’s subscribed channel. The Cluster Version Operator saves these recommendations as either recommended or conditional updates.

While it is possible to attempt an update to a version that is not recommended by OSUS, following a recommended update path protects users from encountering known issues or unintended consequences on the cluster.

Choose only update targets that are recommended by OSUS to ensure a successful update.

##### [2.1.8.2. Address all critical alerts on the cluster](#critical-alerts_updating-cluster-prepare) Copy linkLink copied to clipboard!

Critical alerts must always be addressed as soon as possible, but it is especially important to address these alerts and resolve any problems before initiating a cluster update.

Failing to address critical alerts before beginning an update can cause problematic conditions for the cluster.

In the **Administrator** perspective of the web console, navigate to **Observe** → **Alerting** to find critical alerts.

##### [2.1.8.3. Ensure that the cluster is in an Upgradeable state](#cluster-upgradeable_updating-cluster-prepare) Copy linkLink copied to clipboard!

When one or more Operators have not reported their `Upgradeable` condition as `True` for more than an hour, the `ClusterNotUpgradeable` warning alert is triggered in the cluster. In most cases this alert does not block patch updates, but you cannot perform a minor version update until you resolve this alert and all Operators report `Upgradeable` as `True`.

For more information about the `Upgradeable` condition, see "Understanding cluster Operator condition types" in the additional resources section.

##### [2.1.8.4. SDN support removal](#sdn-support-removal) Copy linkLink copied to clipboard!

OpenShift SDN network plugin was deprecated in versions 4.15 and 4.16. With this release, the SDN network plugin is no longer supported and the content has been removed from the documentation.

If your OpenShift Container Platform cluster is still using the OpenShift SDN CNI, see [Migrating from the OpenShift SDN network plugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.16/html/networking/ovn-kubernetes-network-plugin#migrate-from-openshift-sdn).

Important

It is not possible to update a cluster to OpenShift Container Platform 4.17 if it is using the OpenShift SDN network plugin. You must migrate to the OVN-Kubernetes plugin before upgrading to OpenShift Container Platform 4.17.

##### [2.1.8.5. Ensure that enough spare nodes are available](#nodes-ready_updating-cluster-prepare) Copy linkLink copied to clipboard!

A cluster should not be running with little to no spare node capacity, especially when initiating a cluster update. Nodes that are not running and available may limit a cluster’s ability to perform an update with minimal disruption to cluster workloads.

Depending on the configured value of the cluster’s `maxUnavailable` spec, the cluster might not be able to apply machine configuration changes to nodes if there is an unavailable node. Additionally, if compute nodes do not have enough spare capacity, workloads might not be able to temporarily shift to another node while the first node is taken offline for an update.

Make sure that you have enough available nodes in each worker pool, as well as enough spare capacity on your compute nodes, to increase the chance of successful node updates.

Warning

The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.

##### [2.1.8.6. Ensure that the cluster’s PodDisruptionBudget is properly configured](#pod-disruption-budget_updating-cluster-prepare) Copy linkLink copied to clipboard!

You can use the `PodDisruptionBudget` object to define the minimum number or percentage of pod replicas that must be available at any given time. This configuration protects workloads from disruptions during maintenance tasks such as cluster updates.

However, it is possible to configure the `PodDisruptionBudget` for a given topology in a way that prevents nodes from being drained and updated during a cluster update.

When planning a cluster update, check the configuration of the `PodDisruptionBudget` object for the following factors:

* For highly available workloads, make sure there are replicas that can be temporarily taken offline without being prohibited by the `PodDisruptionBudget`.
* For workloads that are not highly available, make sure they are either not protected by a `PodDisruptionBudget` or have some alternative mechanism for draining these workloads eventually, such as periodic restart or guaranteed eventual termination.

#### [2.1.9. Minimizing worker node deployment time](#minimizing-worker-node-deployment-time_updating-cluster-prepare) Copy linkLink copied to clipboard!

You can minimize deployment time during cluster worker node installation by applying configuration changes across nodes simultaneously.

**Prerequisites**

* You have access to the configuration file for your required installation method (`install-config.yaml` or similar).
* You have the OpenShift CLI (`oc`) installed.
* You have the OpenShift installation program (`openshift-install`) installed.
* You have access to the cluster as a user with the `cluster-admin` role.
* You create more than one worker Machine Configuration Pool (MCP) in the cluster.

**Procedure**

1. Create a MCP YAML file for each custom worker MCP that you intend to use, as in the following example:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfigPool
   metadata:
     name: worker-0
     labels:
       machineconfiguration.openshift.io/role: worker-0
   spec:
     machineConfigSelector:
       matchExpressions:
         - key: machineconfiguration.openshift.io/role
           operator: In
           values: [ worker, worker-0 ]
     paused: false
     maxUnavailable: 100%
     nodeSelector:
       matchLabels:
         node-role.kubernetes.io/worker-0: ""
   ```

   Ensure the following configurations are present:

   * **maxUnavailable**: Set this value to `100%`. This setting ensures that all nodes within this specific MCP update concurrently during the initial deployment. By default, `maxUnavailable` is set to 1, causing all nodes within this specific MCP to update sequentially during the initial deployment.
   * **nodeSelector**: Define a unique label, such as `node-role.kubernetes.io/worker-0`, to bind specific nodes to this pool.
   * **paused**: Set this value to `true` if you plan to apply additional Day 2 configurations, such as `PerformanceProfile`, after installation. All Day 2 configurations can be applied while the MCP is paused. They will be queued and applied when you unpause the node. Set this value to `false` if no further configurations are required.

     Note

     For bare-metal servers, the reboot time can take up to a couple of minutes.
2. Place the YAML files in the directory generated by the installation program. Ensure that your worker nodes get assigned the correct labels, such as `node-role.kubernetes.io/worker-0`, during the provisioning phase or immediately upon joining.

   Note

   Proper labeling ensures that the nodes get assigned to the correct custom MCP rather than the default worker pool.
3. Optional: If you set the `paused` parameter to `true` to apply additional configurations, complete the following steps:

   1. Apply your Day 2 configuration.
   2. Unpause the MCPs to start the configuration phase and reboot if needed. Clusters must be deployed to access the API and run `oc` commands:

      ```
      $ oc patch mcp/worker-0 --patch '{"spec":{"paused":false}}' --type=merge
      ```

      **Example output**

      ```
      machineconfigpool.machineconfiguration.openshift.io/worker-0 patched
      ```

      Note

      If you did not set the `paused` parameter to `true`, the configuration will apply sequentially and reboot if needed.
4. Verify that the MCPs updated successfully:

   ```
   $ oc get machineconfigpools
   ```

   **Example output**

   ```
   NAME       CONFIG                                           UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   master     rendered-master-b0bb90c4921860f2a5d8a2f8137c1867 True      False      False      3              3                   3                     0                      97m
   worker-0   rendered-worker-config-new                       False     True       False      10             0                   0                     0                      5m
   ```
5. When all MCPs are set to `UPDATED=true`, update the MCPs with the appropriate `maxUnavailable` based on workload requirements. This ensures cluster stability and high availability when users deploy workloads onto the cluster. For example, set `maxUnavailable` to 1 by running the following command:

   ```
   $ oc patch mcp/worker-0 --patch '{"spec":{"maxUnavailable":1}}' --type=merge
   ```

   **Example output**

   ```
   machineconfigpool.machineconfiguration.openshift.io/worker-0 patched
   ```

### [2.2. Preparing to update a cluster with manually maintained credentials](#preparing-manual-creds-update) Copy linkLink copied to clipboard!

Before you update a cluster that uses manually maintained credentials, accommodate any new or changed cloud provider credentials in the target release. This preparation ensures the Cloud Credential Operator (CCO) does not block the upgrade.

The CCO `Upgradeable` status for a cluster with manually maintained credentials is `False` by default.

* For minor releases, for example, from 4.12 to 4.13, this status prevents you from updating until you have addressed any updated permissions and annotated the `CloudCredential` resource to indicate that the permissions are updated as needed for the next version. This annotation changes the `Upgradeable` status to `True`.
* For z-stream releases, for example, from 4.13.0 to 4.13.1, no permissions are added or changed, so the update is not blocked.

#### [2.2.1. Update requirements for clusters with manually maintained credentials](#about-manually-maintained-credentials-upgrade_preparing-manual-creds-update) Copy linkLink copied to clipboard!

Before you update a cluster that uses manually maintained credentials with the Cloud Credential Operator (CCO), you must update the cloud provider resources for the new release.

If the cloud credential management for your cluster was configured using the CCO utility (`ccoctl`), use the `ccoctl` utility to update the resources. Clusters that were configured to use manual mode without the `ccoctl` utility require manual updates for the resources.

After updating the cloud provider resources, you must update the `upgradeable-to` annotation for the cluster to indicate that it is ready to update.

Note

The process to update the cloud provider resources and the `upgradeable-to` annotation can only be completed by using command-line tools.

##### [2.2.1.1. Cloud credential configuration options and update requirements by platform type](#cco-platform-options_preparing-manual-creds-update) Copy linkLink copied to clipboard!

Some platforms only support using the CCO in one mode. For clusters that are installed on those platforms, the platform type determines the credentials update requirements.

For platforms that support using the CCO in multiple modes, you must determine which mode the cluster is configured to use and take the required actions for that configuration.

**Figure 2.1. Credentials update requirements by platform type**

Red Hat OpenStack Platform (RHOSP) and VMware vSphere
:   These platforms do not support using the CCO in manual mode. Clusters on these platforms handle changes in cloud provider resources automatically and do not require an update to the `upgradeable-to` annotation.

    Administrators of clusters on these platforms should skip the manually maintained credentials section of the update process.

IBM Cloud and Nutanix
:   Clusters installed on these platforms are configured using the `ccoctl` utility.

    Administrators of clusters on these platforms must take the following actions:

    1. Extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.
    2. Configure the `ccoctl` utility for the new release and use it to update the cloud provider resources.
    3. Indicate that the cluster is ready to update with the `upgradeable-to` annotation.

Microsoft Azure Stack Hub
:   These clusters use manual mode with long-term credentials and do not use the `ccoctl` utility.

    Administrators of clusters on these platforms must take the following actions:

    1. Extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.
    2. Manually update the cloud provider resources for the new release.
    3. Indicate that the cluster is ready to update with the `upgradeable-to` annotation.

Amazon Web Services (AWS), global Microsoft Azure, and Google Cloud
:   Clusters installed on these platforms support multiple CCO modes.

    The required update process depends on the mode that the cluster is configured to use. If you are not sure what mode the CCO is configured to use on your cluster, you can use the web console or the CLI to determine this information.

##### [2.2.1.2. Determining the Cloud Credential Operator mode by using the web console](#cco-determine-mode-gui_preparing-manual-creds-update) Copy linkLink copied to clipboard!

You can determine what mode the Cloud Credential Operator (CCO) is configured to use by using the web console.

Before you perform upgrades or troubleshoot, ensure you understand your cluster’s credential management configuration.

Note

Only Amazon Web Services (AWS), global Microsoft Azure, and Google Cloud clusters support multiple CCO modes.

**Prerequisites**

* You have access to an OpenShift Container Platform account with cluster administrator permissions.

**Procedure**

1. Log in to the OpenShift Container Platform web console as a user with the `cluster-admin` role.
2. Navigate to **Administration** → **Cluster Settings**.
3. On the **Cluster Settings** page, select the **Configuration** tab.
4. Under **Configuration resource**, select **CloudCredential**.
5. On the **CloudCredential details** page, select the **YAML** tab.
6. In the YAML block, check the value of `spec.credentialsMode`. The following values are possible, though not all are supported on all platforms:

   * `''`: The CCO is operating in the default mode. In this configuration, the CCO operates in mint or passthrough mode, depending on the credentials provided during installation.
   * `Mint`: The CCO is operating in mint mode.
   * `Passthrough`: The CCO is operating in passthrough mode.
   * `Manual`: The CCO is operating in manual mode.

   Important

   To determine the specific configuration of an AWS, Google Cloud, or global Microsoft Azure cluster that has a `spec.credentialsMode` of `''`, `Mint`, or `Manual`, you must investigate further.

   AWS and Google Cloud clusters support using mint mode with the root secret deleted. If the cluster is specifically configured to use mint mode or uses mint mode by default, you must determine if the root secret is present on the cluster before updating.

   An AWS, Google Cloud, or global Microsoft Azure cluster that uses manual mode might be configured to create and manage cloud credentials from outside of the cluster with AWS STS, Google Cloud Workload Identity, or Microsoft Entra Workload ID. You can determine whether your cluster uses this strategy by examining the cluster `Authentication` object.
7. AWS or Google Cloud clusters that use mint mode only: To determine whether the cluster is operating without the root secret, navigate to **Workloads** → **Secrets** and look for the root secret for your cloud provider.

   Note

   Ensure that the **Project** dropdown is set to **All Projects**.

   Expand

   | Platform | Secret name |
   | --- | --- |
   | AWS | `aws-creds` |
   | Google Cloud | `gcp-credentials` |

   Show more

   * If you see one of these values, your cluster is using mint or passthrough mode with the root secret present.
   * If you do not see these values, your cluster is using the CCO in mint mode with the root secret removed.
8. AWS, Google Cloud, or global Microsoft Azure clusters that use manual mode only: To determine whether the cluster is configured to create and manage cloud credentials from outside of the cluster, you must check the cluster `Authentication` object YAML values.

   1. Navigate to **Administration** → **Cluster Settings**.
   2. On the **Cluster Settings** page, select the **Configuration** tab.
   3. Under **Configuration resource**, select **Authentication**.
   4. On the **Authentication details** page, select the **YAML** tab.
   5. In the YAML block, check the value of the `.spec.serviceAccountIssuer` parameter.

      * A value that contains a URL that is associated with your cloud provider indicates that the CCO is using manual mode with short-term credentials for components. These clusters are configured using the `ccoctl` utility to create and manage cloud credentials from outside of the cluster.
      * An empty value (`''`) indicates that the cluster is using the CCO in manual mode but was not configured using the `ccoctl` utility.

##### [2.2.1.3. Determining the Cloud Credential Operator mode by using the CLI](#cco-determine-mode-cli_preparing-manual-creds-update) Copy linkLink copied to clipboard!

You can determine what mode the Cloud Credential Operator (CCO) is configured to use by using the CLI.

Before you perform upgrades or troubleshoot, ensure you understand your cluster’s credential management configuration.

Note

Only Amazon Web Services (AWS), global Microsoft Azure, and Google Cloud clusters support multiple CCO modes.

**Prerequisites**

* You have access to an OpenShift Container Platform account with cluster administrator permissions.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Log in to `oc` on the cluster as a user with the `cluster-admin` role.
2. To determine the mode that the CCO is configured to use, enter the following command:

   ```
   $ oc get cloudcredentials cluster \
     -o=jsonpath={.spec.credentialsMode}
   ```

   The following output values are possible, though not all are supported on all platforms:

   * `''`: The CCO is operating in the default mode. In this configuration, the CCO operates in mint or passthrough mode, depending on the credentials provided during installation.
   * `Mint`: The CCO is operating in mint mode.
   * `Passthrough`: The CCO is operating in passthrough mode.
   * `Manual`: The CCO is operating in manual mode.

   Important

   To determine the specific configuration of an AWS, Google Cloud, or global Microsoft Azure cluster that has a `spec.credentialsMode` of `''`, `Mint`, or `Manual`, you must investigate further.

   AWS and Google Cloud clusters support using mint mode with the root secret deleted. If the cluster is specifically configured to use mint mode or uses mint mode by default, you must determine if the root secret is present on the cluster before updating.

   An AWS, Google Cloud, or global Microsoft Azure cluster that uses manual mode might be configured to create and manage cloud credentials from outside of the cluster with AWS STS, Google Cloud Workload Identity, or Microsoft Entra Workload ID. You can determine whether your cluster uses this strategy by examining the cluster `Authentication` object.
3. AWS or Google Cloud clusters that use mint mode only: To determine whether the cluster is operating without the root secret, run the following command:

   ```
   $ oc get secret <secret_name> \
     -n=kube-system
   ```

   where `<secret_name>` is `aws-creds` for AWS or `gcp-credentials` for Google Cloud.

   If the root secret is present, the output of this command returns information about the secret. An error indicates that the root secret is not present on the cluster.
4. AWS, Google Cloud, or global Microsoft Azure clusters that use manual mode only: To determine whether the cluster is configured to create and manage cloud credentials from outside of the cluster, run the following command:

   ```
   $ oc get authentication cluster \
     -o jsonpath \
     --template='{ .spec.serviceAccountIssuer }'
   ```

   This command displays the value of the `.spec.serviceAccountIssuer` parameter in the cluster `Authentication` object.

   * An output of a URL that is associated with your cloud provider indicates that the CCO is using manual mode with short-term credentials for components. These clusters are configured using the `ccoctl` utility to create and manage cloud credentials from outside of the cluster.
   * An empty output indicates that the cluster is using the CCO in manual mode but was not configured using the `ccoctl` utility.

##### [2.2.1.4. Determining the next steps in the update](#cco-determine-mode-next_preparing-manual-creds-update) Copy linkLink copied to clipboard!

After you determine the Cloud Credential Operator mode, it is important to understand how to proceed with the update.

**Procedure**

* If you are updating a cluster that has the CCO operating in mint or passthrough mode and the root secret is present, you do not need to update any cloud provider resources and can continue to the next part of the update process.
* If your cluster is using the CCO in mint mode with the root secret removed, you must reinstate the credential secret with the administrator-level credential before continuing to the next part of the update process.
* If your cluster was configured using the CCO utility (`ccoctl`), you must take the following actions:

  1. Extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.
  2. Configure the `ccoctl` utility for the new release and use it to update the cloud provider resources.
  3. Update the `upgradeable-to` annotation to indicate that the cluster is ready to update.
* If your cluster is using the CCO in manual mode but was not configured using the `ccoctl` utility, you must take the following actions:

  1. Extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.
  2. Manually update the cloud provider resources for the new release.
  3. Update the `upgradeable-to` annotation to indicate that the cluster is ready to update.

#### [2.2.2. Extracting and preparing credentials request resources](#cco-ccoctl-upgrading-extracting_preparing-manual-creds-update) Copy linkLink copied to clipboard!

Before updating a cluster that uses the Cloud Credential Operator (CCO) in manual mode, you must extract and prepare the `CredentialsRequest` custom resources (CRs) for the new release.

**Prerequisites**

* Install the OpenShift CLI (`oc`) that matches the version for your updated version.
* Log in to the cluster as user with `cluster-admin` privileges.

**Procedure**

1. Obtain the pull spec for the update that you want to apply by running the following command:

   ```
   $ oc adm upgrade
   ```

   The output of this command includes pull specs for the available updates similar to the following:

   **Partial example output**

   ```
   ...
   Recommended updates:

   VERSION IMAGE
   4.22.0  quay.io/openshift-release-dev/ocp-release@sha256:6a899c54dda6b844bb12a247e324a0f6cde367e880b73ba110c056df6d018032
   ...
   ```
2. Set a `$RELEASE_IMAGE` variable with the release image that you want to use by running the following command:

   ```
   $ RELEASE_IMAGE=<update_pull_spec>
   ```

   where `<update_pull_spec>` is the pull spec for the release image that you want to use. For example:

   ```
   quay.io/openshift-release-dev/ocp-release@sha256:6a899c54dda6b844bb12a247e324a0f6cde367e880b73ba110c056df6d018032
   ```
3. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Includes only the manifests that your specific cluster configuration requires for the target release.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       This command creates a YAML file for each `CredentialsRequest` object.
4. For each `CredentialsRequest` CR in the release image, ensure that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster. This field is where the generated secrets that hold the credentials configuration are stored.

   **Sample AWS `CredentialsRequest` object**

   ```
   apiVersion: cloudcredential.openshift.io/v1
   kind: CredentialsRequest
   metadata:
     name: cloud-credential-operator-iam-ro
     namespace: openshift-cloud-credential-operator
   spec:
     providerSpec:
       apiVersion: cloudcredential.openshift.io/v1
       kind: AWSProviderSpec
       statementEntries:
       - effect: Allow
         action:
         - iam:GetUser
         - iam:GetUserPolicy
         - iam:ListAccessKeys
         resource: "*"
     secretRef:
       name: cloud-credential-operator-iam-ro-creds
       namespace: openshift-cloud-credential-operator
   ```

   where:

   `openshift-cloud-credential-operator`
   :   Indicates the namespace which must exist to hold the generated secret.

       The `CredentialsRequest` CRs for other platforms have a similar format with different platform-specific values.
5. For any `CredentialsRequest` CR for which the cluster does not already have a namespace with the name specified in `spec.secretRef.namespace`, create the namespace by running the following command:

   ```
   $ oc create namespace <component_namespace>
   ```

**Next steps**

* If the cloud credential management for your cluster was configured using the CCO utility (`ccoctl`), configure the `ccoctl` utility for a cluster update and use it to update your cloud provider resources.
* If your cluster was not configured with the `ccoctl` utility, manually update your cloud provider resources.

#### [2.2.3. Configuring the Cloud Credential Operator utility for a cluster update](#cco-ccoctl-configuring_preparing-manual-creds-update) Copy linkLink copied to clipboard!

To upgrade a cluster that uses the Cloud Credential Operator (CCO) in manual mode to create and manage cloud credentials from outside of the cluster, extract and prepare the CCO utility (`ccoctl`) binary.

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment.

**Prerequisites**

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the OpenShift CLI (`oc`).

* Your cluster was configured using the `ccoctl` utility to create and manage cloud credentials from outside of the cluster.
* You have extracted the `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image and ensured that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster.

**Procedure**

1. Set a variable for the OpenShift Container Platform release image by running the following command:

   ```
   $ RELEASE_IMAGE=$(oc get clusterversion -o jsonpath={..desired.image})
   ```
2. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:

   ```
   $ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
   ```

   Note

   Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
3. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:

   ```
   $ oc image extract $CCO_IMAGE \
     --file="/usr/bin/ccoctl.<rhel_version>" \
     -a ~/.pull-secret
   ```

   For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid:

   * `rhel8`: Specify this value for hosts that use RHEL 8.
   * `rhel9`: Specify this value for hosts that use RHEL 9.

   Note

   The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
4. Change the permissions to make `ccoctl` executable by running the following command:

   ```
   $ chmod 775 ccoctl
   ```

**Verification**

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:

  ```
  $ ./ccoctl
  ```

  **Example output**

  ```
  OpenShift credentials provisioning tool

  Usage:
    ccoctl [command]

  Available Commands:
    aws          Manage credentials objects for AWS cloud
    azure        Manage credentials objects for Azure
    gcp          Manage credentials objects for Google cloud
    help         Help about any command
    ibmcloud     Manage credentials objects for IBM Cloud
    nutanix      Manage credentials objects for Nutanix

  Flags:
    -h, --help   help for ccoctl

  Use "ccoctl [command] --help" for more information about a command.
  ```

#### [2.2.4. Updating cloud provider resources with the Cloud Credential Operator utility](#cco-ccoctl-upgrading_preparing-manual-creds-update) Copy linkLink copied to clipboard!

Update the cloud provider resources for your OpenShift Container Platform cluster by using the CCO utility (`ccoctl`). The process for upgrading these resources is similar to creating the resources during installation.

Note

On AWS clusters, some `ccoctl` commands make AWS API calls to create or modify AWS resources. You can use the `--dry-run` flag to avoid making API calls. Using this flag creates JSON files on the local file system instead. You can review and modify the JSON files and then apply them with the AWS CLI tool using the `--cli-input-json` parameters.

**Prerequisites**

* You have extracted the `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image and ensured that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster.
* You have extracted and configured the `ccoctl` binary from the release image.

**Procedure**

1. Create the output directory if it does not already exist by running the following command:

   ```
   $ mkdir -p <path_to_ccoctl_output_dir>
   ```
2. Extract the bound service account signing key from the cluster and save it to the output directory by running the following command:

   ```
   $ oc get secret bound-service-account-signing-key \
     -n openshift-kube-apiserver \
     -ojsonpath='{ .data.service-account\.pub }' | base64 \
     -d > <path_to_ccoctl_output_dir>/serviceaccount-signer.public
   ```
3. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the command for your cloud provider. The following commands process `CredentialsRequest` objects:

   **Amazon Web Services (AWS)**

   ```
   $ ccoctl aws create-all \
     --name=<name> \
     --region=<aws_region> \
     --credentials-requests-dir=<path_to_credentials_requests_directory> \
     --output-dir=<path_to_ccoctl_output_dir> \
     --public-key-file= \
     <path_to_ccoctl_output_dir>/serviceaccount-signer.public \
     --create-private-s3-bucket \
     --permissions-boundary-arn=<policy_arn>
   ```

   where:

   `<name>`
   :   Specifies the name used to tag any cloud resources that are created for tracking.

   `<aws_region>`
   :   Specifies the AWS region in which cloud resources will be created.

   `<path_to_credentials_requests_directory>`
   :   Specifies the directory containing the files for the component `CredentialsRequest` objects.

   `<path_to_ccoctl_output_dir>`
   :   Specifies the path to the output directory. For `--public-key-file`, this directory contains the `serviceaccount-signer.public` file that you extracted from the cluster.

   `<policy_arn>`
   :   Optional: Specifies the Amazon Resource Name (ARN) of the AWS IAM policy to use as the permissions boundary for the IAM roles created by the `ccoctl` utility.

   Note

   By default, the `ccoctl` utility stores the OpenID Connect (OIDC) configuration files in a public S3 bucket and uses the S3 URL as the public OIDC endpoint. To store the OIDC configuration in a private S3 bucket that is accessed by the IAM identity provider through a public CloudFront distribution URL instead, use the `--create-private-s3-bucket` parameter. This is an optional parameter.

   Note

   To create the AWS resources individually, use the "Creating AWS resources individually" procedure in the "Installing a cluster on AWS with customizations" content. This option might be useful if you need to review the JSON files that the `ccoctl` tool creates before modifying AWS resources, or if the process the `ccoctl` tool uses to create AWS resources automatically does not meet the requirements of your organization.

   **Google Cloud**

   ```
   $ ccoctl gcp create-all \
     --name=<name> \
     --region=<gcp_region> \
     --project=<gcp_project_id> \
     --credentials-requests-dir=<path_to_credentials_requests_directory> \
     --output-dir=<path_to_ccoctl_output_dir> \
     --public-key-file=<path_to_ccoctl_output_dir>/serviceaccount-signer.public \
     --key-storage-method=<key_storage_method>
   ```

   where:

   `<name>`
   :   Specifies the user-defined name for all created Google Cloud resources used for tracking.

   `<gcp_region>`
   :   Specifies the Google Cloud region in which cloud resources will be created.

   `<gcp_project_id>`
   :   Specifies the Google Cloud project ID in which cloud resources will be created.

   `<path_to_credentials_requests_directory>`
   :   Specifies the directory containing the files of `CredentialsRequest` manifests to create Google Cloud service accounts.

   `<path_to_ccoctl_output_dir>`
   :   Specifies the path to the output directory. For `--public-key-file`, this directory contains the `serviceaccount-signer.public` file that you extracted from the cluster.

   `<key_storage_method>`
   :   Optional: Specifies the method for storing OIDC JWK files. Accepted values are `public-bucket` and `pool-jwk-file`. The default value `public-bucket` creates a public GCS bucket to host the OIDC configuration and JWK files. The `pool-jwk-file` value attaches the JWK directly to the workload identity pool provider without creating a public bucket.

   Note

   If your cluster was previously configured with the `public-bucket` method and you switch to `pool-jwk-file`, the existing GCS bucket is no longer used. You can delete the old `<name>-oidc` bucket from your Google Cloud project to avoid retaining an unnecessary public resource.

   **IBM Cloud**

   ```
   $ ccoctl ibmcloud create-service-id \
     --credentials-requests-dir=<path_to_credential_requests_directory> \
     --name=<cluster_name> \
     --output-dir=<installation_directory> \
     --resource-group-name=<resource_group_name>
   ```

   where:

   `<path_to_credential_requests_directory>`
   :   Specifies the directory containing the files for the component `CredentialsRequest` objects.

   `<cluster_name>`
   :   Specifies the name of the OpenShift Container Platform cluster.

   `<installation_directory>`
   :   Optional: Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run.

   `<resource_group_name>`
   :   Optional: Specifies the name of the resource group used for scoping the access policies.

   **Microsoft Azure**

   ```
   $ ccoctl azure create-managed-identities \
     --name <azure_infra_name> \
     --output-dir=<path_to_ccoctl_output_dir> \
     --region <azure_region> \
     --subscription-id <azure_subscription_id> \
     --credentials-requests-dir <path_to_directory_for_credentials_requests> \
     --issuer-url "${OIDC_ISSUER_URL}" \
     --dnszone-resource-group-name <azure_dns_zone_resourcegroup_name> \
     --installation-resource-group-name "${AZURE_INSTALL_RG}" \
     --preserve-existing-roles
   ```

   where:

   `<azure_infra_name>`
   :   Specifies the value of the `name` parameter used to create an Azure resource group. To use an existing Azure resource group instead of creating a new one, specify the `--oidc-resource-group-name` argument with the existing group name as its value.

   `<path_to_ccoctl_output_dir>`
   :   Specifies the path to the output directory.

   `<azure_region>`
   :   Specifies the region of the existing cluster.

   `<azure_subscription_id>`
   :   Specifies the subscription ID of the existing cluster.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the directory containing the files for the component `CredentialsRequest` objects.

   `"${OIDC_ISSUER_URL}"`
   :   Specifies the OIDC issuer URL from the existing cluster. You can obtain this value by running the following command:

       ```
       $ oc get authentication cluster \
         -o jsonpath \
         --template='{ .spec.serviceAccountIssuer }'
       ```

   `<azure_dns_zone_resourcegroup_name>`
   :   Specifies the name of the resource group that contains the DNS zone.

   `"${AZURE_INSTALL_RG}"`
   :   Specifies the Azure resource group name. You can obtain this value by running the following command:

       ```
       $ oc get infrastructure cluster \
         -o jsonpath \
         --template '{ .status.platformStatus.azure.resourceGroupName }'
       ```

   Note

   Specifying the flag `ccoctl.azure.create-managed-identities.preserve-existing-roles` ensures that any custom role assignments you define on managed identities are not removed during OpenShift Container Platform updates. This flag is optional.

   **Nutanix**

   ```
   $ ccoctl nutanix create-shared-secrets \
     --credentials-requests-dir=<path_to_credentials_requests_directory> \
     --output-dir=<ccoctl_output_dir> \
     --credentials-source-filepath=<path_to_credentials_file>
   ```

   where:

   `<path_to_credentials_requests_directory>`
   :   Specifies the path to the directory that contains the files for the component `CredentialsRequests` objects.

   `<ccoctl_output_dir>`
   :   Optional: Specifies the directory in which you want the `ccoctl` utility to create objects. By default, the utility creates objects in the directory in which the commands are run.

   `<path_to_credentials_file>`
   :   Optional: Specifies the directory that contains the credentials data YAML file. By default, `ccoctl` expects this file to be in `<home_directory>/.nutanix/credentials`.

   For each `CredentialsRequest` object, `ccoctl` creates the required provider resources and a permissions policy as defined in each `CredentialsRequest` object from the OpenShift Container Platform release image.
4. Apply the secrets to your cluster by running the following command:

   ```
   $ ls <path_to_ccoctl_output_dir>/manifests/*-credentials.yaml | xargs -I{} oc apply -f {}
   ```

**Verification**

You can verify that the required provider resources and permissions policies are created by querying the cloud provider. For more information, refer to your cloud provider documentation on listing roles or service accounts.

**Next steps**

* Update the `upgradeable-to` annotation to indicate that the cluster is ready to upgrade.

#### [2.2.5. Manually updating cloud provider resources](#manually-maintained-credentials-upgrade_preparing-manual-creds-update) Copy linkLink copied to clipboard!

Meet the requirements of the target release by manually updating cloud provider credentials. Update these credentials by creating secrets for new components and by adjusting the permissions for existing components.

Before you upgrade a cluster with manually maintained credentials, you must create secrets for any new credentials for the release image that you are upgrading to. You must also review the required permissions for existing credentials and accommodate any new permissions requirements in the new release for those components.

**Prerequisites**

* You have extracted the `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image and ensured that a namespace that matches the text in the `spec.secretRef.namespace` field exists in the cluster.

**Procedure**

1. Create YAML files with secrets for any `CredentialsRequest` custom resources that the new release image adds. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

   **Sample AWS `CredentialsRequest` object with secrets**

   ```
   apiVersion: cloudcredential.openshift.io/v1
   kind: CredentialsRequest
   metadata:
     name: <component_credentials_request>
     namespace: openshift-cloud-credential-operator
     ...
   spec:
     providerSpec:
       apiVersion: cloudcredential.openshift.io/v1
       kind: AWSProviderSpec
       statementEntries:
       - effect: Allow
         action:
         - s3:CreateBucket
         - s3:DeleteBucket
         resource: "*"
         ...
     secretRef:
       name: <component_secret>
       namespace: <component_namespace>
     ...
   ```

   **Sample AWS `Secret` object**

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: <component_secret>
     namespace: <component_namespace>
   data:
     aws_access_key_id: <base64_encoded_aws_access_key_id>
     aws_secret_access_key: <base64_encoded_aws_secret_access_key>
   ```

   Note

   Global Azure and Azure Stack Hub use the same `CredentialsRequest` object and secret formats.

   **Sample Azure `CredentialsRequest` object with secrets**

   ```
   apiVersion: cloudcredential.openshift.io/v1
   kind: CredentialsRequest
   metadata:
     name: <component_credentials_request>
     namespace: openshift-cloud-credential-operator
     ...
   spec:
     providerSpec:
       apiVersion: cloudcredential.openshift.io/v1
       kind: AzureProviderSpec
       roleBindings:
       - role: Contributor
         ...
     secretRef:
       name: <component_secret>
       namespace: <component_namespace>
     ...
   ```

   **Sample Azure `Secret` object**

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: <component_secret>
     namespace: <component_namespace>
   data:
     azure_subscription_id: <base64_encoded_azure_subscription_id>
     azure_client_id: <base64_encoded_azure_client_id>
     azure_client_secret: <base64_encoded_azure_client_secret>
     azure_tenant_id: <base64_encoded_azure_tenant_id>
     azure_resource_prefix: <base64_encoded_azure_resource_prefix>
     azure_resourcegroup: <base64_encoded_azure_resourcegroup>
     azure_region: <base64_encoded_azure_region>
   ```

   **Sample Google Cloud `CredentialsRequest` object with secrets**

   ```
   apiVersion: cloudcredential.openshift.io/v1
   kind: CredentialsRequest
   metadata:
     name: <component_credentials_request>
     namespace: openshift-cloud-credential-operator
     ...
   spec:
     providerSpec:
       apiVersion: cloudcredential.openshift.io/v1
       kind: GCPProviderSpec
         predefinedRoles:
         - roles/iam.securityReviewer
         - roles/iam.roleViewer
         skipServiceCheck: true
         ...
     secretRef:
       name: <component_secret>
       namespace: <component_namespace>
     ...
   ```

   **Sample Google Cloud `Secret` object**

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: <component_secret>
     namespace: <component_namespace>
   data:
     service_account.json: <base64_encoded_gcp_service_account_file>
   ```
2. If the `CredentialsRequest` custom resources for any existing credentials that are stored in secrets have changed permissions requirements, update the permissions as required.

**Next steps**

* Update the `upgradeable-to` annotation to indicate that the cluster is ready to upgrade.

#### [2.2.6. Indicating that the cluster is ready to upgrade](#cco-manual-upgrade-annotation_preparing-manual-creds-update) Copy linkLink copied to clipboard!

Modify the `CloudCredential` resource to include an `upgradeable-to` annotation. This signals that you updated manually maintained credentials and that the cluster is ready to upgrade.

**Prerequisites**

* For the release image that you are upgrading to, you have processed any new credentials manually or by using the Cloud Credential Operator utility (`ccoctl`).
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Log in to `oc` on the cluster as a user with the `cluster-admin` role.
2. Edit the `CloudCredential` resource to add an `upgradeable-to` annotation within the `metadata` field by running the following command:

   ```
   $ oc edit cloudcredential cluster
   ```

   **Text to add**

   ```
   ...
     metadata:
       annotations:
         cloudcredential.openshift.io/upgradeable-to: <version_number>
   ...
   ```

   Where `<version_number>` is the version that you are upgrading to, in the format `x.y.z`. For example, use `4.12.2` for OpenShift Container Platform 4.12.2.

   It may take several minutes after adding the annotation for the upgradeable status to change.

**Verification**

1. In the **Administrator** perspective of the web console, navigate to **Administration** → **Cluster Settings**.
2. To view the CCO status details, click **cloud-credential** in the **Cluster Operators** list.

   * If the **Upgradeable** status in the **Conditions** section is **False**, verify that the `upgradeable-to` annotation is free of typographical errors.
3. When the **Upgradeable** status in the **Conditions** section is **True**, begin the OpenShift Container Platform upgrade.

### [2.3. Preflight validation for Kernel Module Management (KMM) Modules](#kmm-preflight-validation) Copy linkLink copied to clipboard!

Before you upgrade a cluster that uses Kernel Module Management (KMM) modules, verify that the kernel modules can be installed on the nodes after the upgrade. This preflight validation helps you avoid unexpected module failures caused by kernel changes.

Preflight attempts to validate every `Module` loaded in the cluster, in parallel. Preflight does not wait for validation of one `Module` to complete before starting validation of another `Module`.

#### [2.3.1. Validation kickoff](#kmm-validation-kickoff_kmm-preflight-validation) Copy linkLink copied to clipboard!

Create a `PreflightValidationOCP` resource to trigger preflight validation and specify the kernel version and DTK image for validation.

Preflight validation is triggered by creating a `PreflightValidationOCP` resource in the cluster. This resource contains the following fields:

`dtkImage`
:   The DTK container image released for the specific OpenShift Container Platform version of the cluster. If this value is not set, the `DTK_AUTO` feature cannot be used.

    You can obtain the image by running one of the following commands in the cluster:

    ```
    # For x86_64 image:
    $ oc adm release info quay.io/openshift-release-dev/ocp-release:4.22.0-x86_64 --image-for=driver-toolkit
    ```

    ```
    # For ARM64 image:
    $ oc adm release info quay.io/openshift-release-dev/ocp-release:4.22.0-aarch64 --image-for=driver-toolkit
    ```

`kernelVersion`
:   Required field that provides the version of the kernel that the cluster is upgraded to.

    You can obtain the version by running the following command in the cluster:

    ```
    $ podman run -it --rm $(oc adm release info quay.io/openshift-release-dev/ocp-release:4.22.0-x86_64 --image-for=driver-toolkit) cat /etc/driver-toolkit-release.json
    ```

`pushBuiltImage`
:   If `true`, then the images created during the Build and Sign validation are pushed to their repositories. This field is `false` by default.

#### [2.3.2. Validation lifecycle](#kmm-validation-lifecycle_kmm-preflight-validation) Copy linkLink copied to clipboard!

Preflight validation continuously validates all cluster modules, retrying failures after changes until all modules succeed or the validation resource is deleted.

Each module stops being validated after it succeeds individually. Failed modules are retried in subsequent validation loops.

If you want to run Preflight validation for an additional kernel, then you should create another `PreflightValidationOCP` resource for that kernel. After all the modules have been validated, it is recommended to delete the `PreflightValidationOCP` resource.

#### [2.3.3. Validation status](#kmm-validation-status_kmm-preflight-validation) Copy linkLink copied to clipboard!

The `PreflightValidationOCP` resource reports validation status and progress for each cluster module in its `.status.modules` list.

The following outlines the fields included in the `.status.modules` list:

`name`
:   The name of the `Module` resource.

`namespace`
:   The namespace of the `Module` resource.

`statusReason`
:   Verbal explanation regarding the status.

`verificationStage`
:   Describes the validation stage being executed:

    * `Image`: Image existence verification
    * `Done`: Verification is done

`verificationStatus`
:   The status of the Module verification:

    * `Success`: Verified
    * `Failure`: Verification failed
    * `InProgress`: Verification is in progress

#### [2.3.4. Image validation stage](#kmm-image-validation-stage_kmm-preflight-validation) Copy linkLink copied to clipboard!

Image validation checks whether kernel module images exist and are accessible before attempting to build or sign new images.

Image validation is always the first stage of the preflight validation to be executed. If image validation is successful, no other validations are run on that specific module. The Operator uses the container runtime to check the image existence and accessibility for the updated kernel in the module.

If the image validation fails and there is a `build/sign` section in the module that is relevant to the upgraded kernel, the controller tries to build or sign the image. If the `PushBuiltImage` flag is defined in the `PreflightValidationOCP` resource, the controller will also try to push the resulting image into its repository. The resulting image name is taken from the definition of the `containerImage` field of the `Module` CR.

Note

In case a `build` section exists, the input image in the `sign` section is used as the output image by the `build` section. Therefore, in order for the input image to be available to the `sign` section, the `PushBuiltImage` flag must be defined in the `PreflightValidationOCP` CR.

#### [2.3.5. Example PreflightValidationOCP resource](#kmm-example-cr_kmm-preflight-validation) Copy linkLink copied to clipboard!

The example `PreflightValidationOCP` resource validates kernel modules and pushes built images to repositories.

The example verifies all of the currently present modules against the upcoming `5.14.0-570.19.1.el9_6.x86_64` kernel. Because `.spec.pushBuiltImage` is set to `true`, KMM pushes the resulting images of Build/Sign in to the defined repositories.

```
apiVersion: kmm.sigs.x-k8s.io/v1beta2
kind: PreflightValidationOCP
metadata:
  name: preflight
spec:
  kernelVersion: 5.14.0-570.19.1.el9_6.x86_64
  dtkImage: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:fe0322730440f1cbe6fffaaa8cac131b56574bec8abe3ec5b462e17557fecb32
  pushBuiltImage: true
```

## [Chapter 3. Performing a cluster update](#performing-a-cluster-update) Copy linkLink copied to clipboard!

### [3.1. Updating a cluster using the CLI](#updating-cluster-cli) Copy linkLink copied to clipboard!

You can perform minor version and patch updates on an OpenShift Container Platform cluster by using the OpenShift CLI (`oc`).

#### [3.1.1. About updating single node OpenShift Container Platform](#update-single-node-openshift_updating-cluster-cli) Copy linkLink copied to clipboard!

You can update a single-node OpenShift Container Platform cluster by using either the console or CLI.

However, note the following limitations:

* The prerequisite to pause the `MachineHealthCheck` resources is not required because there is no other node to perform the health check.
* Restoring a single-node OpenShift Container Platform cluster using an etcd backup is not officially supported. However, it is good practice to perform the etcd backup in case your update fails. If your control plane is healthy, you might be able to restore your cluster to a previous state by using the backup.
* Updating a single-node OpenShift Container Platform cluster requires downtime and can include an automatic reboot. The amount of downtime depends on the update payload, as described in the following scenarios:

  + If the update payload contains an operating system update, which requires a reboot, the downtime is significant and impacts cluster management and user workloads.
  + If the update contains machine configuration changes that do not require a reboot, the downtime is less, and the impact on the cluster management and user workloads is lessened. In this case, the node draining step is skipped with single-node OpenShift Container Platform because there is no other node in the cluster to reschedule the workloads to.
  + If the update payload does not contain an operating system update or machine configuration changes, a short API outage occurs and resolves quickly.

Important

There are conditions, such as bugs in an updated package, that can cause the single node to not restart after a reboot. In this case, the update does not rollback automatically.

#### [3.1.2. Prerequisites for a cluster update](#updating-cli-prereqs_updating-cluster-cli) Copy linkLink copied to clipboard!

You must satisfy the following prerequisites before updating a cluster using the CLI.

* Have access to the cluster as a user with `admin` privileges. See "Using RBAC to define and apply permissions" for more information.
* Have a recent etcd backup in case your update fails and you must restore your cluster to a previous state.
* Have a recent Container Storage Interface (CSI) volume snapshot in case you need to restore persistent volumes due to a pod failure.
* Your RHEL7 workers are replaced with RHEL8 or RHCOS workers. Red Hat does not support in-place RHEL7 to RHEL8 updates for RHEL workers; those hosts must be replaced with a clean operating system install.
* You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default software catalogs switch from the current minor version to the next during a cluster update. See "Updating installed Operators" for more information on how to check compatibility and, if necessary, update the installed Operators.
* Ensure that all machine config pools (MCPs) are running and not paused. Nodes associated with a paused MCP are skipped during the update process. You can pause the MCPs if you are performing a canary rollout update strategy.
* If your cluster uses manually maintained credentials, update the cloud provider resources for the new release. For more information, including how to determine if this is a requirement for your cluster, see "Preparing to update a cluster with manually maintained credentials".
* Ensure that you address all `Upgradeable=False` conditions so the cluster allows an update to the next minor version. An alert displays at the top of the **Cluster Settings** page when you have one or more cluster Operators that cannot be updated. You can still update to the next available patch update for the minor release you are currently on.
* If you run an Operator or you have configured any application with the pod disruption budget, you might experience an interruption during the update process. If `minAvailable` is set to 1 in `PodDisruptionBudget`, the nodes are drained to apply pending machine configs which might block the eviction process. If several nodes are rebooted, all the pods might run on only one node, and the `PodDisruptionBudget` field can prevent the node drain.

Important

* When an update is failing to complete, the Cluster Version Operator (CVO) reports the status of any blocking components while attempting to reconcile the update. Rolling your cluster back to a previous version is not supported. If your update is failing to complete, contact Red Hat support.
* Using the `unsupportedConfigOverrides` section to modify the configuration of an Operator is unsupported and might block cluster updates. You must remove this setting before you can update your cluster.

#### [3.1.3. Pausing a MachineHealthCheck resource](#machine-health-checks-pausing_updating-cluster-cli) Copy linkLink copied to clipboard!

During the update process, nodes in the cluster might become temporarily unavailable. For worker nodes, the `MachineHealthCheck` resources might identify such nodes as unhealthy and reboot them. To avoid rebooting worker nodes, you must pause all the `MachineHealthCheck` resources before updating the cluster.

Note

Some `MachineHealthCheck` resources might not need to be paused. If your `MachineHealthCheck` resource relies on unrecoverable conditions, pausing that MHC is unnecessary.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).

**Procedure**

1. List all of the available `MachineHealthCheck` resources that you want to pause by running the following command:

   ```
   $ oc get machinehealthcheck -n openshift-machine-api
   ```
2. For each `MachineHealthCheck` resource, pause the machine health check by running the following command:

   ```
   $ oc -n openshift-machine-api annotate mhc <mhc_name> cluster.x-k8s.io/paused=""
   ```

   The annotated `MachineHealthCheck` resource resembles the following YAML file:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineHealthCheck
   metadata:
     name: example
     namespace: openshift-machine-api
     annotations:
       cluster.x-k8s.io/paused: ""
   spec:
     selector:
       matchLabels:
         role: worker
     unhealthyConditions:
     - type:    "Ready"
       status:  "Unknown"
       timeout: "300s"
     - type:    "Ready"
       status:  "False"
       timeout: "300s"
     maxUnhealthy: "40%"
   status:
     currentHealthy: 5
     expectedMachines: 5
   ```

   Important

   Resume the machine health checks after updating the cluster. To resume the check, remove the pause annotation from the `MachineHealthCheck` resource by running the following command:

   ```
   $ oc -n openshift-machine-api annotate mhc <mhc-name> cluster.x-k8s.io/paused-
   ```

#### [3.1.4. Updating a cluster by using the CLI](#update-upgrading-cli_updating-cluster-cli) Copy linkLink copied to clipboard!

You can use the OpenShift CLI (`oc`) to review and request cluster updates.

You can find information about available OpenShift Container Platform advisories and updates [in the errata section](https://access.redhat.com/downloads/content/290) of the Customer Portal.

**Prerequisites**

* You installed the OpenShift CLI (`oc`) that matches the version for your updated version.
* You are logged in to the cluster as user with `cluster-admin` privileges.
* You have paused all `MachineHealthCheck` resources.

**Procedure**

1. View the available updates and note the version number of the update that you want to apply by running the following command:

   ```
   $ oc adm upgrade recommend
   ```

   **Example output**

   ```
   The following conditions found no cause for concern in updating this cluster to later releases: recommended/CriticalAlerts (AsExpected), recommended/NodeAlerts (AsExpected), recommended/PodDisruptionBudgetAlerts (AsExpected), recommended/PodImagePullAlerts (AsExpected), recommended/UpdatePrecheckAlerts (AsExpected)

   Upstream update service is unset, so the cluster will use an appropriate default.
   Channel: stable-4.21 (available channels: candidate-4.20, candidate-4.21, candidate-4.22, eus-4.20, fast-4.20, fast-4.21, stable-4.20, stable-4.21)

   Updates to 4.21:
     VERSION     ISSUES
     4.21.14     no known issues relevant to this cluster
     4.21.13     no known issues relevant to this cluster
   And 2 older 4.21 updates you can see with '--show-outdated-releases' or '--version VERSION'.

   Updates to 4.20:
     VERSION     ISSUES
     4.20.20     no known issues relevant to this cluster
   ```

   Note

   * You can use the `--version` flag to determine whether a specific version is recommended for your update. If there are no recommended updates, updates that have known issues might still be available.
   * For details and information on how to perform a *Control Plane Only* update, see "Performing a Control Plane Only update".
2. Based on your organization requirements, set the appropriate update channel by running the following command. For example, you can set your channel to `stable-4.13` or `fast-4.13`. For more information about channels, see "Understanding update channels and releases".

   ```
   $ oc adm upgrade channel <channel>
   ```

   **Example command**

   ```
   $ oc adm upgrade channel stable-4.22
   ```

   Important

   For production clusters, you must subscribe to a `stable-*`, `eus-*`, or `fast-*` channel.

   Note

   When you are ready to move to the next minor version, choose the channel that corresponds to that minor version. The sooner you declare the update channel, the more effectively the cluster can recommend update paths to your target version. The cluster might take some time to evaluate all the possible updates that are available and offer the best update recommendations to choose from. Update recommendations can change over time, as they are based on what update options are available at the time.

   If you cannot see an update path to your target minor version, keep updating your cluster to the latest patch release for your current version until the next minor version is available in the path.
3. Apply an update:

   * To update to the latest version, run the following command:

     ```
     $ oc adm upgrade --to-latest=true
     ```
   * To update to a specific version, run the following command:

     ```
     $ oc adm upgrade --to=<version>
     ```

     Replace `<version>` with the update version that you obtained from the output of the `oc adm upgrade recommend` command.

     Important

     When using the `oc adm upgrade --help` command, there is a listed option for the `--force` flag. This is *heavily discouraged*, because using the `--force` option bypasses cluster-side guards, including release verification and precondition checks. Using the `--force` flag does not guarantee a successful update. Bypassing guards puts the cluster at risk.
4. If the cluster administrator evaluates the potential known risks and decides it is acceptable for the current cluster, then the administrator can waive the safety guards and proceed with the update by running the following command:

   ```
   $ oc adm upgrade --allow-not-recommended --to <version>
   ```
5. Optional: Review the status of the Cluster Version Operator by running the following command:

   ```
   $ oc adm upgrade status
   ```

   Note

   To monitor the update in real time, run `oc adm upgrade status` in a `watch` utility.
6. After the update completes, confirm that the cluster version has updated to the new version by running the following command:

   ```
   $ oc adm upgrade
   ```

   **Example output**

   ```
   Cluster version is <version>

   Upstream is unset, so the cluster will use an appropriate default.
   Channel: stable-<version> (available channels: candidate-<version>, eus-<version>, fast-<version>, stable-<version>)

   No updates available. You may force an update to a specific release image, but doing so might not be supported and might result in downtime or data loss.
   ```
7. If you are updating your cluster to the next minor version, such as version X.y to X.(y+1), confirm that your nodes are updated before deploying workloads that rely on a new feature. Run the following command:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                           STATUS   ROLES    AGE   VERSION
   ip-10-0-168-251.ec2.internal   Ready    master   82m   v1.35.4
   ip-10-0-170-223.ec2.internal   Ready    master   82m   v1.35.4
   ip-10-0-179-95.ec2.internal    Ready    worker   70m   v1.35.4
   ip-10-0-182-134.ec2.internal   Ready    worker   70m   v1.35.4
   ip-10-0-211-16.ec2.internal    Ready    master   82m   v1.35.4
   ip-10-0-250-100.ec2.internal   Ready    worker   69m   v1.35.4
   ```

#### [3.1.5. Cluster update status using oc adm upgrade status](#update-upgrading-oc-adm-upgrade-status_updating-cluster-cli) Copy linkLink copied to clipboard!

When updating your cluster, the `oc adm upgrade` command returns limited information about the status of your update. The cluster administrator can use the `oc adm upgrade status` command to return specific information regarding a cluster update, including the status of the control plane and worker node updates. Worker is also known as compute.

The `oc adm upgrade status` command is read-only and does not alter any state in your cluster.

The `oc adm upgrade status` command can be used for clusters on versions 4.12 or later.

The `oc adm upgrade status` command will output three sections, control plane update, worker nodes update, and health insights.

Control Plane Update
:   Displays details about the updating cluster control plane, contains a high-level assessment, completion status, duration estimate, or cluster Operator health. The section also shows a table with control plane node update information.

    The control plane update section can also show an additional table that lists cluster Operators being updated if the `--details=operators` or `--details-all` flags are used. Please note that due the asynchronous distributed nature of OpenShift Container Platform, an operator may appear in this section more than once during the update, or not at all. The section is only shown when a cluster Operator is observed to be updating. It is normal during an update to observe no updating cluster Operator at certain periods; not every performed action can be assigned to an observable updating cluster Operator.

Worker Notes Update
:   Displays the worker node update information. The worker nodes section starts with a table that displays a summary of information about each worker pool configured in the cluster. Each non-empty worker pool output will show a dedicated table listing update information about nodes that belong to that pool. If a cluster does not have any worker nodes, the output will not contain the worker node section. You can make the node tables show all lines by using the `--details=nodes` or `--details=all` flags.

Health Insights
:   Displays insights about states and events present in the cluster that may be relevant for the ongoing update. You can use the `--details=health` flag to expand the items in this section into a more verbose form with more content such as documentation links, longer form descriptions, or cluster resources involved in the insight.

Note

The `oc adm upgrade status` command is currently not supported on hosted control planes clusters.

The following is an example of the output you will see for an update progressing successfully:

```
= Control Plane =
Assessment:      Progressing
Target Version:  4.17.1 (from 4.17.0)
Updating:        machine-config
Completion:      97% (32 operators updated, 1 updating, 0 waiting)
Duration:        54m (Est. Time Remaining: <10m)
Operator Status: 32 Healthy, 1 Unavailable

Control Plane Nodes
NAME                                        ASSESSMENT    PHASE      VERSION   EST    MESSAGE
ip-10-0-53-40.us-east-2.compute.internal    Progressing   Draining   4.17.0    +10m
ip-10-0-30-217.us-east-2.compute.internal   Outdated      Pending    4.17.0    ?
ip-10-0-92-180.us-east-2.compute.internal   Outdated      Pending    4.17.0    ?

= Worker Upgrade =

WORKER POOL   ASSESSMENT    COMPLETION   STATUS
worker        Progressing   0% (0/2)     1 Available, 1 Progressing, 1 Draining
infra         Progressing   50% (1/2)    1 Available, 1 Progressing, 1 Draining

Worker Pool Nodes: Worker
NAME                                       ASSESSMENT    PHASE      VERSION   EST    MESSAGE
ip-10-0-4-159.us-east-2.compute.internal   Progressing   Draining   4.17.0    +10m
ip-10-0-99-40.us-east-2.compute.internal   Outdated      Pending    4.17.0    ?

Worker Pool Nodes: infra
NAME                                             ASSESSMENT    PHASE      VERSION   EST    MESSAGE
ip-10-0-4-159-infra.us-east-2.compute.internal   Progressing   Draining   4.17.0    +10m
ip-10-0-20-162.us-east-2.compute.internal        Completed     Updated    4.17.1    -

= Update Health =

SINCE   LEVEL   IMPACT   MESSAGE
54m4s   Info    None     Update is proceeding well
```

#### [3.1.6. Changing the update server by using the CLI](#update-changing-update-server-cli_updating-cluster-cli) Copy linkLink copied to clipboard!

You can change the update server your cluster uses to retrieve information about update paths.

Changing the update server is optional. If you have an OpenShift Update Service (OSUS) installed and configured locally, you must set the URL for the server as the `upstream` to use the local server during updates. The default value for `upstream` is `https://api.openshift.com/api/upgrades_info/v1/graph`.

**Procedure**

* Change the `upstream` parameter value in the cluster version by running the following command:

  ```
  $ oc patch clusterversion/version --patch '{"spec":{"upstream":"<update_server_url>"}}' --type=merge
  ```

  Replace `<update_server_url>` with the URL for the update server.

  **Example output**

  ```
  clusterversion.config.openshift.io/version patched
  ```

### [3.2. Updating a cluster using the web console](#updating-cluster-web-console) Copy linkLink copied to clipboard!

You can perform minor version and patch updates on an OpenShift Container Platform cluster by using the web console.

Note

Use the web console or `oc adm upgrade channel <channel>` to change the update channel. You can follow the steps in [Updating a cluster using the CLI](#updating-cluster-cli "3.1. Updating a cluster using the CLI") to complete the update after you change to a 4.22 channel.

#### [3.2.1. Before updating the OpenShift Container Platform cluster](#before-updating-ocp_updating-cluster-web-console) Copy linkLink copied to clipboard!

Before updating your cluster, you must consider several factors in order to improve the chances of performing a successful update.

Consider the following information:

* Whether you have recently backed up etcd.
* In `PodDisruptionBudget`, if `minAvailable` is set to `1`, the nodes are drained to apply pending machine configs that might block the eviction process. If several nodes are rebooted, all the pods might run on only one node, and the `PodDisruptionBudget` field can prevent the node drain.
* You might need to update the cloud provider resources for the new release if your cluster uses manually maintained credentials.
* You must review administrator acknowledgement requests, take any recommended actions, and provide the acknowledgement when you are ready.
* You can perform a partial update by updating the worker or custom pool nodes to accommodate the time it takes to update. You can pause and resume within the progress bar of each pool.

Important

* When an update is failing to complete, the Cluster Version Operator (CVO) reports the status of any blocking components while attempting to reconcile the update. Rolling your cluster back to a previous version is not supported. If your update is failing to complete, contact Red Hat support.
* Using the `unsupportedConfigOverrides` section to modify the configuration of an Operator is unsupported and might block cluster updates. You must remove this setting before you can update your cluster.

#### [3.2.2. Changing the update server by using the web console](#update-changing-update-server-web_updating-cluster-web-console) Copy linkLink copied to clipboard!

You can change the update server your cluster uses to retrieve information about update paths.

Changing the update server is optional. If you have an OpenShift Update Service (OSUS) installed and configured locally, you must set the URL for the server as the `upstream` to use the local server during updates.

**Prerequisites**

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

**Procedure**

1. On the web console, navigate to **Administration** → **Cluster Settings** and click **version**.
2. Click the **YAML** tab and then edit the `upstream` parameter value:

   **Example YAML snippet**

   ```
     ...
     spec:
       clusterID: db93436d-7b05-42cc-b856-43e11ad2d31a
       upstream: '<update_server_url>'
     ...
   ```

   Replace `<update_server_url>` with the URL for the update server.

   The default `upstream` value is `https://api.openshift.com/api/upgrades_info/v1/graph`.
3. Click **Save**.

#### [3.2.3. Pausing a MachineHealthCheck resource by using the web console](#machine-health-checks-pausing-web-console_updating-cluster-web-console) Copy linkLink copied to clipboard!

During the update process, nodes in the cluster might become temporarily unavailable. For worker nodes, the machine health check might identify such nodes as unhealthy and reboot them. To avoid rebooting such nodes, pause all the `MachineHealthCheck` resources before updating the cluster.

**Prerequisites**

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

**Procedure**

1. On the web console, navigate to **Compute** → **MachineHealthChecks**.
2. For each `MachineHealthCheck` resource, pause the machine health checks by adding the `cluster.x-k8s.io/paused=""` annotation to the resource. For example, to add the annotation to the `machine-api-termination-handler` resource, complete the following steps:

   1. Click the Options menu
      next to the `machine-api-termination-handler` and click **Edit annotations**.
   2. In the **Edit annotations** dialog, click **Add more**.
   3. In the **Key** and **Value** fields, add `cluster.x-k8s.io/paused` and `""` values, respectively, and click **Save**.

#### [3.2.4. Updating a cluster by using the web console](#update-upgrading-web_updating-cluster-web-console) Copy linkLink copied to clipboard!

If updates are available, you can update your cluster from the web console.

You can find information about available OpenShift Container Platform advisories and updates [in the errata section](https://access.redhat.com/downloads/content/290) of the Customer Portal.

**Prerequisites**

* Have access to the web console as a user with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* Pause all `MachineHealthCheck` resources.
* You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default software catalogs switch from the current minor version to the next during a cluster update. See "Updating installed Operators" in the "Additional resources" section for more information on how to check compatibility and, if necessary, update the installed Operators.
* Your machine config pools (MCPs) are running and not paused. Nodes associated with a paused MCP are skipped during the update process. You can pause the MCPs if you are performing a canary rollout update strategy.
* Your RHEL7 workers are replaced with RHEL8 or RHCOS workers. Red Hat does not support in-place RHEL7 to RHEL8 updates for RHEL workers; those hosts must be replaced with a clean operating system install.

**Procedure**

1. From the web console, click **Administration** → **Cluster Settings** and review the contents of the **Details** tab.
2. For production clusters, ensure that the **Channel** is set to the correct channel for the version that you want to update to, such as `stable-4.22`.

   Important

   For production clusters, you must subscribe to a `stable-*`, `eus-*` or `fast-*` channel.

   Note

   When you are ready to move to the next minor version, choose the channel that corresponds to that minor version. The sooner you declare the update channel, the more effectively the cluster can recommend update paths to your target version. The cluster might take some time to evaluate all the possible updates that are available and offer the best update recommendations to choose from. Update recommendations can change over time, as they are based on what update options are available at the time.

   If you cannot see an update path to your target minor version, keep updating your cluster to the latest patch release for your current version until the next minor version is available in the path.

   If the **Update status** is not **Updates available**, you cannot update your cluster.

   **Select channel** indicates the cluster version that your cluster is running or is updating to.
3. Select a version to update to, and click **Save**.

   The Input channel **Update status** changes to **Update to <product-version> in progress**, and you can review the progress of the cluster update by watching the progress bars for the Operators and nodes.

   Note

   If you are updating your cluster to the next minor version, for example from version 4.10 to 4.11, confirm that your nodes are updated before deploying workloads that rely on a new feature. Any pools with worker nodes that are not yet updated are displayed on the **Cluster Settings** page.
4. After the update completes and the Cluster Version Operator refreshes the available updates, check if more updates are available in your current channel.

   * If updates are available, continue to perform updates in the current channel until you can no longer update.
   * If no updates are available, change the **Channel** to the `stable-*`, `eus-*` or `fast-*` channel for the next minor version, and update to the version that you want in that channel.

   You might need to perform several intermediate updates until you reach the version that you want.

#### [3.2.5. Viewing conditional updates in the web console](#update-conditional-web-console_updating-cluster-web-console) Copy linkLink copied to clipboard!

You can view and assess the risks associated with particular updates with conditional updates.

**Prerequisites**

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.
* Pause all `MachineHealthCheck` resources.
* You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default software catalogs switch from the current minor version to the next during a cluster update. See "Updating installed Operators" in the "Additional resources" section for more information on how to check compatibility and, if necessary, update the installed Operators.
* Your machine config pools (MCPs) are running and not paused. Nodes associated with a paused MCP are skipped during the update process. You can pause the MCPs if you are performing an advanced update strategy, such as a canary rollout, an EUS update, or a control-plane update.

**Procedure**

1. From the web console, click **Administration** → **Cluster settings** page and review the contents of the **Details** tab.
2. You can enable the `Include versions with known issues` feature in the **Select new version** dropdown of the **Update cluster** modal to populate the dropdown list with conditional updates.

   Note

   If a version with known issues is selected, more information is provided with potential risks that are associated with the version.
3. Review the notification detailing the potential risks to updating.

#### [3.2.6. Performing a canary rollout update](#update-using-custom-machine-config-pools-canary_updating-cluster-web-console) Copy linkLink copied to clipboard!

In some specific use cases, you might want a more controlled update process where you do not want specific nodes updated concurrently with the rest of the cluster.

These use cases include, but are not limited to the following situations:

* You have mission-critical applications that you do not want unavailable during the update. You can slowly test the applications on your nodes in small batches after the update.
* You have a small maintenance window that does not allow the time for all nodes to be updated, or you have multiple maintenance windows.

The rolling update process is **not** a typical update workflow. With larger clusters, it can be a time-consuming process that requires you execute multiple commands. This complexity can result in errors that can affect the entire cluster. It is recommended that you carefully consider whether your organization wants to use a rolling update and carefully plan the implementation of the process before you start.

The rolling update process described in this topic involves:

* Creating one or more custom machine config pools (MCPs).
* Labeling each node that you do not want to update immediately to move those nodes to the custom MCPs.
* Pausing those custom MCPs, which prevents updates to those nodes.
* Performing the cluster update.
* Unpausing one custom MCP, which triggers the update on those nodes.
* Testing the applications on those nodes to make sure the applications work as expected on those newly-updated nodes.
* Optionally removing the custom labels from the remaining nodes in small batches and testing the applications on those nodes.

Note

Pausing an MCP should be done with careful consideration and for short periods of time only.

If you want to use the canary rollout update process, see "Performing a canary rollout update".

#### [3.2.7. About updating single node OpenShift Container Platform](#update-single-node-openshift_updating-cluster-web-console) Copy linkLink copied to clipboard!

You can update a single-node OpenShift Container Platform cluster by using either the console or CLI.

However, note the following limitations:

* The prerequisite to pause the `MachineHealthCheck` resources is not required because there is no other node to perform the health check.
* Restoring a single-node OpenShift Container Platform cluster using an etcd backup is not officially supported. However, it is good practice to perform the etcd backup in case your update fails. If your control plane is healthy, you might be able to restore your cluster to a previous state by using the backup.
* Updating a single-node OpenShift Container Platform cluster requires downtime and can include an automatic reboot. The amount of downtime depends on the update payload, as described in the following scenarios:

  + If the update payload contains an operating system update, which requires a reboot, the downtime is significant and impacts cluster management and user workloads.
  + If the update contains machine configuration changes that do not require a reboot, the downtime is less, and the impact on the cluster management and user workloads is lessened. In this case, the node draining step is skipped with single-node OpenShift Container Platform because there is no other node in the cluster to reschedule the workloads to.
  + If the update payload does not contain an operating system update or machine configuration changes, a short API outage occurs and resolves quickly.

Important

There are conditions, such as bugs in an updated package, that can cause the single node to not restart after a reboot. In this case, the update does not rollback automatically.

### [3.3. Performing a Control Plane Only update](#control-plane-only-update) Copy linkLink copied to clipboard!

To reduce the rebooting of non-control plane hosts during cluster updates, you can perform a Control Plane Only update for your cluster.

Due to fundamental Kubernetes design, all OpenShift Container Platform updates between minor versions must be serialized. You must update from OpenShift Container Platform <4.y> to <4.y+1>, and then to <4.y+2>. You cannot update from OpenShift Container Platform <4.y> to <4.y+2> directly. However, administrators who want to update between two even-numbered minor versions can do so incurring only a single reboot of non-control plane hosts.

Important

This update was previously known as an **EUS-to-EUS** update and is now referred to as a **Control Plane Only** update. These updates are only viable between **even-numbered minor versions** of OpenShift Container Platform.

There are several caveats to consider when attempting a Control Plane Only update.

* Control Plane Only updates are only offered after updates between all versions involved have been made available in `stable` channels.
* If you encounter issues during or after updating to the odd-numbered minor version but before updating to the next even-numbered version, then remediation of those issues may require that non-control plane hosts complete the update to the odd-numbered version before moving forward.
* You can do a partial update by updating the worker or custom pool nodes to accommodate the time it takes for maintenance.
* Until the machine config pools are unpaused and the update is complete, some features and bugs fixes in <4.y+1> and <4.y+2> of OpenShift Container Platform are not available.
* All the clusters might update using EUS channels for a conventional update without pools paused, but only clusters with non control-plane `MachineConfigPools` objects can do Control Plane Only updates with pools paused.

#### [3.3.1. Performing a Control Plane Only update](#updating-control-plane-only-update_control-plane-only-update) Copy linkLink copied to clipboard!

You can perform a Control Plane Only update by pausing all non-`master` machine config pools, performing updates from OpenShift Container Platform <4.y> to <4.y+1> to <4.y+2>, then unpausing the machine config pools.

Following this procedure reduces the total update duration and the number of times worker nodes are restarted.

**Prerequisites**

* You reviewed the release notes for OpenShift Container Platform <4.y+1> and <4.y+2>.
* You reviewed the release notes and product lifecycles for any layered products and Operator Lifecycle Manager (OLM) Operators. Some products and OLM Operators might require updates either before or during a Control Plane Only update.
* You are familiar with version-specific prerequisites, such as the removal of deprecated APIs, that are required before updating from OpenShift Container Platform <4.y+1> to <4.y+2>.
* If your cluster uses in-tree vSphere volumes, you updated vSphere to version 7.0u3L+ or 8.0u2+.

  Important

  If you do not update vSphere to 7.0u3L+ or 8.0u2+ before initiating an OpenShift Container Platform update, known issues might occur with your cluster after the update. For more information, see [Known Issues with OpenShift 4.12 to 4.13 or 4.13 to 4.14 vSphere CSI Storage Migration](https://access.redhat.com/node/7011683).

##### [3.3.1.1. Control Plane Only update using the web console](#updating-control-plane-only-update-console_control-plane-only-update) Copy linkLink copied to clipboard!

You can perform a Control Plane Only update by using the web console.

**Prerequisites**

* You verified that machine config pools are unpaused.
* You have access to the web console as a user with `cluster-admin` privileges.

**Procedure**

1. Using the web console, update any Operator Lifecycle Manager (OLM) Operators to the versions that are compatible with your intended updated version. For more information, see "Updating installed Operators".
2. Verify that all machine config pools display a status of `Up to date` and that no machine config pool displays a status of `UPDATING`.

   To view the status of all machine config pools, click **Compute** → **MachineConfigPools** and review the contents of the **Update status** column.

   Note

   If your machine config pools have an `Updating` status, wait for this status to change to `Up to date`. This process could take several minutes.
3. Set your channel to `eus-<4.y+2>`.

   To set your channel, click **Administration** → **Cluster Settings** → **Channel**. You can edit your channel by clicking on the current hyperlinked channel.
4. Pause all worker machine pools except for the master pool. You can perform this action on the **MachineConfigPools** tab under the **Compute** page. Select the vertical ellipses next to the machine config pool you’d like to pause and click **Pause updates**.
5. Update to version <4.y+1> and complete up to the **Save** step. For more information, see "Updating a cluster by using the web console".
6. Ensure that the <4.y+1> updates are complete by viewing the **Last completed version** of your cluster. You can find this information on the **Cluster Settings** page under the **Details** tab.
7. If necessary, update your OLM Operators by using the Administrator perspective on the web console. For more information, see "Updating installed Operators".
8. Update to version <4.y+2> and complete up to the **Save** step. For more information, see "Updating a cluster by using the web console".
9. Ensure that the <4.y+2> update is complete by viewing the **Last completed version** of your cluster. You can find this information on the **Cluster Settings** page under the **Details** tab.
10. Unpause all previously paused machine config pools. You can perform this action on the **MachineConfigPools** tab under the **Compute** page. Select the vertical ellipses next to the machine config pool you’d like to unpause and click **Unpause updates**.

    Important

    If pools are paused, the cluster is not permitted to upgrade to any future minor versions, and some maintenance tasks are inhibited. This puts the cluster at risk for future degradation.
11. Verify that your previously paused pools are updated and that your cluster has completed the update to version <4.y+2>.

    You can verify that your pools have updated on the **MachineConfigPools** tab under the **Compute** page by confirming that the **Update status** has a value of **Up to date**.

    Important

    When you update a cluster that contains Red Hat Enterprise Linux (RHEL) compute machines, those machines temporarily become unavailable during the update process. You must run the upgrade playbook against each RHEL machine as it enters the `NotReady` state for the cluster to finish updating. For more information, see "Updating a cluster that includes RHEL compute machines".

    You can verify that your cluster has completed the update by viewing the **Last completed version** of your cluster. You can find this information on the **Cluster Settings** page under the **Details** tab.

##### [3.3.1.2. Control Plane Only update using the CLI](#updating-control-plane-only-update-cli_control-plane-only-update) Copy linkLink copied to clipboard!

You can perform a Control Plane Only update by using the OpenShift CLI (`oc`).

**Prerequisites**

* You verified that machine config pools are unpaused.
* You have access to the OpenShift Container Platform web console as a user with `cluster-admin` privileges.
* You updated the OpenShift CLI (`oc`) to the target version before each update.

  Important

  It is highly discouraged to skip this prerequisite. If the OpenShift CLI (`oc`) is not updated to the target version before your update, unexpected issues may occur.

**Procedure**

1. Using the web console, update any Operator Lifecycle Manager (OLM) Operators to the versions that are compatible with your intended updated version. You can find more information on how to perform this action in "Updating installed Operators"; see "Additional resources".
2. Verify that all machine config pools display a status of `UPDATED` and that no machine config pool displays a status of `UPDATING`. To view the status of all machine config pools, run the following command:

   ```
   $ oc get mcp
   ```

   **Example output**

   ```
   NAME     CONFIG                                         	UPDATED   UPDATING
   master   rendered-master-ecbb9582781c1091e1c9f19d50cf836c       True  	  False
   worker   rendered-worker-00a3f0c68ae94e747193156b491553d5       True  	  False
   ```
3. Your current version is <4.y>, and your intended version to update is <4.y+2>. Change to the `eus-<4.y+2>` channel by running the following command:

   ```
   $ oc adm upgrade channel eus-<4.y+2>
   ```

   Note

   If you receive an error message indicating that `eus-<4.y+2>` is not one of the available channels, this indicates that Red Hat is still rolling out EUS version updates. This rollout process generally takes 45-90 days starting at the GA date.
4. Pause all worker machine pools except for the master pool by running the following command:

   ```
   $ oc patch mcp/worker --type merge --patch '{"spec":{"paused":true}}'
   ```

   Note

   You cannot pause the master pool.
5. Update to the latest version by running the following command:

   ```
   $ oc adm upgrade --to-latest
   ```

   **Example output**

   ```
   Updating to latest version <4.y+1.z>
   ```
6. Review the cluster version to ensure that the updates are complete by running the following command:

   ```
   $ oc adm upgrade
   ```

   **Example output**

   ```
   Cluster version is <4.y+1.z>
   ...
   ```
7. Update to version <4.y+2> by running the following command:

   ```
   $ oc adm upgrade --to-latest
   ```
8. Retrieve the cluster version to ensure that the <4.y+2> updates are complete by running the following command:

   ```
   $ oc adm upgrade
   ```

   **Example output**

   ```
   Cluster version is <4.y+2.z>
   ...
   ```
9. To update your worker nodes to <4.y+2>, unpause all previously paused machine config pools by running the following command:

   ```
   $ oc patch mcp/worker --type merge --patch '{"spec":{"paused":false}}'
   ```

   Important

   If pools are not unpaused, the cluster is not permitted to update to any future minor versions, and some maintenance tasks are inhibited. This puts the cluster at risk for future degradation.
10. Verify that your previously paused pools are updated and that the update to version <4.y+2> is complete by running the following command:

    ```
    $ oc get mcp
    ```

    Important

    When you update a cluster that contains Red Hat Enterprise Linux (RHEL) compute machines, those machines temporarily become unavailable during the update process. You must run the upgrade playbook against each RHEL machine as it enters the `NotReady` state for the cluster to finish updating. For more information, see "Updating a cluster that includes RHEL compute machines" in the additional resources section.

    **Example output**

    ```
    NAME 	   CONFIG                                            UPDATED     UPDATING
    master   rendered-master-52da4d2760807cb2b96a3402179a9a4c    True  	 False
    worker   rendered-worker-4756f60eccae96fb9dcb4c392c69d497    True 	 False
    ```

##### [3.3.1.3. Control Plane Only updates for layered products and Operators installed through Operator Lifecycle Manager](#updating-control-plane-only-olm-operators_control-plane-only-update) Copy linkLink copied to clipboard!

There are additional steps to consider when performing Control Plane Only updates for clusters with either layered products or Operators installed through Operator Lifecycle Manager (OLM).

Layered products refer to products that are made of multiple underlying products that are intended to be used together and cannot be broken into individual subscriptions. For examples of layered OpenShift Container Platform products, see [Layered Offering On OpenShift](https://access.redhat.com/support/policy/updates/openshift/#layered).

As you perform a Control Plane Only update for the clusters of layered products and those of Operators that have been installed through OLM, you must complete the following actions:

1. You have updated all Operators previously installed through Operator Lifecycle Manager (OLM) to a version that is compatible with your target release. Updating the Operators ensures they have a valid update path when the default software catalogs switch from the current minor version to the next during a cluster update. See "Updating installed Operators" for more information on how to check compatibility and, if necessary, update the installed Operators.
2. Confirm the cluster version compatibility between the current and intended Operator versions. You can verify which versions your OLM Operators are compatible with by using the [Red Hat OpenShift Container Platform Operator Update Information Checker](https://access.redhat.com/labs/ocpouic/?operator=logging&&ocp_versions=4.10,4.11,4.12).

For example, the following high level steps describe how to perform a Control Plane Only update from <4.y> to <4.y+2> for OpenShift Data Foundation (ODF). This can be done through the CLI or web console. For information about how to update clusters through your desired interface, see "Control Plane Only update using the web console" and "Control Plane Only update using the CLI".

1. Pause the worker machine pools.
2. Update OpenShift Container Platform from <4.y> to <4.y+1>.
3. Update ODF from <4.y> to <4.y+1>.
4. Update OpenShift Container Platform from <4.y+1> to <4.y+2>.
5. Update ODF to <4.y+2>.
6. Unpause the worker machine pools.

Note

The update to ODF <4.y+2> can happen before or after worker machine pools have been unpaused.

### [3.4. Performing a canary rollout update](#update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

For a more controlled rollout of worker node updates, you can use a *canary update*. A canary update is an update strategy where worker node updates are performed in discrete, sequential stages instead of updating all worker nodes at the same time.

This strategy can be useful in the following scenarios:

* You want a more controlled rollout of worker node updates to ensure that mission-critical applications stay available during the entire update, even if the update process causes your applications to fail.
* You want to update a small subset of worker nodes, evaluate cluster and workload health over a period of time, and then update the remaining nodes.
* You want to fit worker node updates, which often require a host reboot, into smaller defined maintenance windows when it is not possible to take a large maintenance window to update the entire cluster at one time.

In these scenarios, you can create multiple custom machine config pools (MCPs) to prevent certain worker nodes from updating when you update the cluster. After the rest of the cluster is updated, you can update those worker nodes in batches at appropriate times.

#### [3.4.1. Example Canary update strategy](#example_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

To better understand how the canary rollout strategy works, it is useful to consider an example of an update using the strategy.

The following example describes a canary update strategy where you have a cluster with 100 nodes with 10% excess capacity, you have maintenance windows that must not exceed 4 hours, and you know that it takes no longer than 8 minutes to drain and reboot a worker node.

Note

The previous values are an example only. The time it takes to drain a node might vary depending on factors such as workloads.

##### [3.4.1.1. Definition of custom machine config pools](#defining-custom-mcps_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

In order to organize the worker node updates into separate stages, you can begin by defining the following machine config pools:

* **workerpool-canary** with 10 nodes
* **workerpool-A** with 30 nodes
* **workerpool-B** with 30 nodes
* **workerpool-C** with 30 nodes

##### [3.4.1.2. Update of the canary worker pool](#updating-canary-worker-pool_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

During your first maintenance window, you pause the machine config pools (MCPs) for **workerpool-A**, **workerpool-B**, and **workerpool-C**, and then initiate the cluster update. This updates components that run on top of OpenShift Container Platform and the 10 nodes that are part of the unpaused **workerpool-canary** MCP. The other three MCPs are not updated because they were paused.

##### [3.4.1.3. Whether or not to proceed with the remaining worker pool updates](#determining-remaining-worker-pools_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

If for some reason you determine that your cluster or workload health was negatively affected by the **workerpool-canary** update, you then cordon and drain all nodes in that pool while still maintaining sufficient capacity until you have diagnosed and resolved the problem. When everything is working as expected, you evaluate the cluster and workload health before deciding to unpause, and thus update, **workerpool-A**, **workerpool-B**, and **workerpool-C** in succession during each additional maintenance window.

Managing worker node updates using custom machine config pools (MCPs) provides flexibility, however it can be a time-consuming process that requires you execute multiple commands. This complexity can result in errors that might affect the entire cluster. It is recommended that you carefully consider your organizational needs and carefully plan the implementation of the process before you start.

Important

Pausing a machine config pool prevents the Machine Config Operator from applying any configuration changes on the associated nodes. Pausing an MCP also prevents any automatically rotated certificates from being pushed to the associated nodes, including the automatic CA rotation of the `kube-apiserver-to-kubelet-signer` CA certificate.

If the MCP is paused when the `kube-apiserver-to-kubelet-signer` CA certificate expires and the MCO attempts to automatically renew the certificate, the MCO cannot push the newly rotated certificates to those nodes. This causes failure in multiple `oc` commands, including `oc debug`, `oc logs`, `oc exec`, and `oc attach`. You receive alerts in the Alerting UI of the OpenShift Container Platform web console if an MCP is paused when the certificates are rotated.

Pausing an MCP should be done with careful consideration about the `kube-apiserver-to-kubelet-signer` CA certificate expiration and for short periods of time only.

Note

It is not recommended to update the MCPs to different OpenShift Container Platform versions. For example, do not update one MCP from 4.y.10 to 4.y.11 and another to 4.y.12. This scenario has not been tested and might result in an undefined cluster state.

#### [3.4.2. About the canary rollout update process and MCPs](#update-using-custom-machine-config-pools-about-mcp_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

In OpenShift Container Platform, nodes are not considered individually. Instead, they are grouped into machine config pools (MCPs). By default, nodes in an OpenShift Container Platform cluster are grouped into two MCPs: one for the control plane nodes and one for the worker nodes.

An OpenShift Container Platform update affects all MCPs concurrently.

During the update, the Machine Config Operator (MCO) drains and cordons all nodes within an MCP up to the specified `maxUnavailable` number of nodes, if a max number is specified. By default, `maxUnavailable` is set to `1`. Draining and cordoning a node deschedules all pods on the node and marks the node as unschedulable.

After the node is drained, the Machine Config Daemon applies a new machine configuration, which can include updating the operating system (OS). Updating the OS requires the host to reboot.

##### [3.4.2.1. Using custom machine config pools](#using-custom-mcps_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

To prevent specific nodes from being updated, you can create custom MCPs. Because the MCO does not update nodes within paused MCPs, you can pause the MCPs containing nodes that you do not want to update before initiating a cluster update.

Using one or more custom MCPs can give you more control over the sequence in which you update your worker nodes. For example, after you update the nodes in the first MCP, you can verify the application compatibility and then update the rest of the nodes gradually to the new version.

Warning

The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.

Note

To ensure the stability of the control plane, creating a custom MCP from the control plane nodes is not supported. The Machine Config Operator (MCO) ignores any custom MCP created for the control plane nodes.

##### [3.4.2.2. Considerations when using custom machine config pools](#custom-mcp-considerations_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

Give careful consideration to the number of MCPs that you create and the number of nodes in each MCP, based on your workload deployment topology. For example, if you must fit updates into specific maintenance windows, you must know how many nodes OpenShift Container Platform can update within a given window. This number is dependent on your unique cluster and workload characteristics.

You must also consider how much extra capacity is available in your cluster to determine the number of custom MCPs and the amount of nodes within each MCP. In a case where your applications fail to work as expected on newly updated nodes, you can cordon and drain those nodes in the pool, which moves the application pods to other nodes. However, you must determine whether the available nodes in the remaining MCPs can provide sufficient quality-of-service (QoS) for your applications.

Note

You can use this update process with all documented OpenShift Container Platform update processes. However, the process does not work with Red Hat Enterprise Linux (RHEL) machines, which are updated using Ansible playbooks.

#### [3.4.3. About performing a canary rollout update](#update-using-custom-machine-config-pools-about_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

The process of a canary update can be understood as several high-level steps.

The following steps outline the high-level workflow of the process:

1. Create custom machine config pools (MCP) based on the worker pool.

   Note

   You can change the `maxUnavailable` setting in an MCP to specify the percentage or the number of machines that can be updating at any given time. The default is `1`.

   Warning

   The default setting for `maxUnavailable` is `1` for all the machine config pools in OpenShift Container Platform. It is recommended to not change this value and update one control plane node at a time. Do not change this value to `3` for the control plane pool.
2. Add a node selector to the custom MCPs. For each node that you do not want to update simultaneously with the rest of the cluster, add a matching label to the nodes. This label associates the node to the MCP.

   Important

   Do not remove the default worker label from the nodes. The nodes must have a role label to function properly in the cluster.
3. Pause the MCPs you do not want to update as part of the update process.
4. Perform the cluster update. The update process updates the MCPs that are not paused, including the control plane nodes.
5. Test your applications on the updated nodes to ensure they are working as expected.
6. Unpause one of the remaining MCPs, wait for the nodes in that pool to finish updating, and test the applications on those nodes. Repeat this process until all worker nodes are updated.
7. Optional: Remove the custom label from updated nodes and delete the custom MCPs.

#### [3.4.4. Creating machine config pools to perform a canary rollout update](#update-using-custom-machine-config-pools-mcp_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

To perform a canary rollout update, you must first create one or more custom machine config pools (MCP).

**Procedure**

1. List the worker nodes in your cluster by running the following command:

   ```
   $ oc get -l 'node-role.kubernetes.io/master!=' -o 'jsonpath={range .items[*]}{.metadata.name}{"\n"}{end}' nodes
   ```

   **Example output**

   ```
   ci-ln-pwnll6b-f76d1-s8t9n-worker-a-s75z4
   ci-ln-pwnll6b-f76d1-s8t9n-worker-b-dglj2
   ci-ln-pwnll6b-f76d1-s8t9n-worker-c-lldbm
   ```
2. For each node that you want to delay, add a custom label to the node by running the following command:

   ```
   $ oc label node <node_name> node-role.kubernetes.io/<custom_label>=
   ```

   For example:

   ```
   $ oc label node ci-ln-0qv1yp2-f76d1-kl2tq-worker-a-j2ssz node-role.kubernetes.io/workerpool-canary=
   ```

   **Example output**

   ```
   node/ci-ln-gtrwm8t-f76d1-spbl7-worker-a-xk76k labeled
   ```
3. Create the new MCP:

   1. Create an MCP YAML file:

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfigPool
      metadata:
        name: workerpool-canary
      spec:
        machineConfigSelector:
          matchExpressions:
            - {
               key: machineconfiguration.openshift.io/role,
               operator: In,
               values: [worker,workerpool-canary]
              }
        nodeSelector:
          matchLabels:
            node-role.kubernetes.io/workerpool-canary: ""
      ```

      where:

      `metadata.name`
      :   Specifies a name for the MCP.

      `spec.machineConfigSelector.matchExpressions.values`
      :   Specifies the `worker` and custom MCP name.

      `spec.nodeSelectormatchLabels.node-role.kubernetes.io/workerpool-canary`
      :   Specifies the custom label you added to the nodes that you want in this pool.
   2. Create the `MachineConfigPool` object by running the following command:

      ```
      $ oc create -f <file_name>
      ```

      **Example output**

      ```
      machineconfigpool.machineconfiguration.openshift.io/workerpool-canary created
      ```
4. View the list of MCPs in the cluster and their current state by running the following command:

   ```
   $ oc get machineconfigpool
   ```

   **Example output**

   ```
   NAME              CONFIG                                                        UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   master            rendered-master-b0bb90c4921860f2a5d8a2f8137c1867              True      False      False      3              3                   3                     0                      97m
   workerpool-canary rendered-workerpool-canary-87ba3dec1ad78cb6aecebf7fbb476a36   True      False      False      1              1                   1                     0                      2m42s
   worker            rendered-worker-87ba3dec1ad78cb6aecebf7fbb476a36              True      False      False      2              2                   2                     0                      97m
   ```

   The new machine config pool, `workerpool-canary`, is created and the number of nodes to which you added the custom label are shown in the machine counts. The worker MCP machine counts are reduced by the same number. It can take several minutes to update the machine counts. In this example, one node was moved from the `worker` MCP to the `workerpool-canary` MCP.

#### [3.4.5. Managing machine configuration inheritance for a worker pool canary](#update-using-custom-machine-config-pools-mcp-inheritance_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

You can configure a machine config pool (MCP) canary to inherit any `MachineConfig` assigned to an existing MCP. This configuration is useful when you want to use an MCP canary to test as you update nodes one at a time for an existing MCP.

**Prerequisites**

* You have created one or more MCPs.

**Procedure**

1. Create a secondary MCP as described in the following two steps:

   1. Save the following configuration file as `machineConfigPool.yaml`.

      **Example `machineConfigPool` YAML**

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfigPool
      metadata:
        name: worker-perf
      spec:
        machineConfigSelector:
          matchExpressions:
            - {
               key: machineconfiguration.openshift.io/role,
               operator: In,
               values: [worker,worker-perf]
              }
        nodeSelector:
          matchLabels:
            node-role.kubernetes.io/worker-perf: ""
      # ...
      ```
   2. Create the new machine config pool by running the following command:

      ```
      $ oc create -f machineConfigPool.yaml
      ```

      **Example output**

      ```
      machineconfigpool.machineconfiguration.openshift.io/worker-perf created
      ```
2. Add some machines to the secondary MCP. The following example labels the worker nodes `worker-a`, `worker-b`, and `worker-c` to the MCP `worker-perf`:

   ```
   $ oc label node worker-a node-role.kubernetes.io/worker-perf=''
   ```

   ```
   $ oc label node worker-b node-role.kubernetes.io/worker-perf=''
   ```

   ```
   $ oc label node worker-c node-role.kubernetes.io/worker-perf=''
   ```
3. Create a new `MachineConfig` for the MCP `worker-perf` as described in the following two steps:

   1. Save the following `MachineConfig` example as a file called `new-machineconfig.yaml`:

      **Example `MachineConfig` YAML**

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfig
      metadata:
        labels:
          machineconfiguration.openshift.io/role: worker-perf
        name: 06-kdump-enable-worker-perf
      spec:
        config:
          ignition:
            version: 3.2.0
          systemd:
            units:
            - enabled: true
              name: kdump.service
        kernelArguments:
          - crashkernel=512M
      # ...
      ```
   2. Apply the `MachineConfig` by running the following command:

      ```
      $ oc create -f new-machineconfig.yaml
      ```
4. Create the new canary MCP and add machines from the MCP you created in the previous steps. The following example creates an MCP called `worker-perf-canary`, and adds machines from the `worker-perf` MCP that you previosuly created.

   1. Label the canary worker node `worker-a` by running the following command:

      ```
      $ oc label node worker-a node-role.kubernetes.io/worker-perf-canary=''
      ```
   2. Remove the canary worker node `worker-a` from the original MCP by running the following command:

      ```
      $ oc label node worker-a node-role.kubernetes.io/worker-perf-
      ```
   3. Save the following file as `machineConfigPool-Canary.yaml`.

      **Example `machineConfigPool-Canary.yaml` file**

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfigPool
      metadata:
        name: worker-perf-canary
      spec:
        machineConfigSelector:
          matchExpressions:
            - {
               key: machineconfiguration.openshift.io/role,
               operator: In,
               values: [worker,worker-perf,worker-perf-canary]
              }
        nodeSelector:
          matchLabels:
            node-role.kubernetes.io/worker-perf-canary: ""
      ```

      where:

      `spec.machineConfigSelector.matchExpressions.values`
      :   Specifies a value you can use to configure members of an additional `MachineConfig`. This example includes `worker-perf-canary` as an additional value. This is an optional value.
   4. Create the new `worker-perf-canary` by running the following command:

      ```
      $ oc create -f machineConfigPool-Canary.yaml
      ```

      **Example output**

      ```
      machineconfigpool.machineconfiguration.openshift.io/worker-perf-canary created
      ```
5. Check if the `MachineConfig` is inherited in `worker-perf-canary`.

   1. Verify that no MCP is degraded by running the following command:

      ```
      $ oc get mcp
      ```

      **Example output**

      ```
      NAME                  CONFIG                                                          UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
      master                rendered-master-2bf1379b39e22bae858ea1a3ff54b2ac                True      False      False      3              3                   3                     0                      5d16h
      worker                rendered-worker-b9576d51e030413cfab12eb5b9841f34                True      False      False      0              0                   0                     0                      5d16h
      worker-perf          rendered-worker-perf-b98a1f62485fa702c4329d17d9364f6a          True      False      False      2              2                   2                     0                      56m
      worker-perf-canary   rendered-worker-perf-canary-b98a1f62485fa702c4329d17d9364f6a   True      False      False      1              1                   1                     0                      44m
      ```
   2. Verify that the machines are inherited from `worker-perf` into `worker-perf-canary`.

      ```
      $ oc get nodes
      ```

      **Example output**

      ```
      NAME       STATUS   ROLES                        AGE     VERSION
      ...
      worker-a   Ready    worker,worker-perf-canary   5d15h   v1.27.13+e709aa5
      worker-b   Ready    worker,worker-perf          5d15h   v1.27.13+e709aa5
      worker-c   Ready    worker,worker-perf          5d15h   v1.27.13+e709aa5
      ```
   3. Verify that `kdump` service is enabled on `worker-a` by running the following command:

      ```
      $ systemctl status kdump.service
      ```

      **Example output**

      ```
      NAME       STATUS   ROLES                        AGE     VERSION
      ...
      kdump.service - Crash recovery kernel arming
           Loaded: loaded (/usr/lib/systemd/system/kdump.service; enabled; preset: disabled)
           Active: active (exited) since Tue 2024-09-03 12:44:43 UTC; 10s ago
          Process: 4151139 ExecStart=/usr/bin/kdumpctl start (code=exited, status=0/SUCCESS)
         Main PID: 4151139 (code=exited, status=0/SUCCESS)
      ```
   4. Verify that the MCP has updated the `crashkernel` by running the following command:

      ```
      $ cat /proc/cmdline
      ```

      The output should include the updated `crashekernel` value, for example:

      **Example output**

      ```
      crashkernel=512M
      ```
6. Optional: If you are satisfied with the upgrade, you can return `worker-a` to `worker-perf`.

   1. Return `worker-a` to `worker-perf` by running the following command:

      ```
      $ oc label node worker-a node-role.kubernetes.io/worker-perf=''
      ```
   2. Remove `worker-a` from the canary MCP by running the following command:

      ```
      $ oc label node worker-a node-role.kubernetes.io/worker-perf-canary-
      ```

#### [3.4.6. Pausing the machine config pools](#update-using-custom-machine-config-pools-pause_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

After you create your custom machine config pools (MCPs), you then pause those MCPs. Pausing an MCP prevents the Machine Config Operator (MCO) from updating the nodes associated with that MCP.

**Procedure**

* Patch the MCP that you want paused by running the following command:

  ```
  $ oc patch mcp/<mcp_name> --patch '{"spec":{"paused":true}}' --type=merge
  ```

  For example:

  ```
  $  oc patch mcp/workerpool-canary --patch '{"spec":{"paused":true}}' --type=merge
  ```

  **Example output**

  ```
  machineconfigpool.machineconfiguration.openshift.io/workerpool-canary patched
  ```

#### [3.4.7. Performing the cluster update](#update-using-custom-machine-config-pools-update_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

After the machine config pools (MCP) enter a ready state, you can perform the cluster update.

**Procedure**

* See one of the following update methods, as appropriate for your cluster:

  + "Updating a cluster using the web console"
  + "Updating a cluster using the CLI"

#### [3.4.8. Unpausing the machine config pools](#update-using-custom-machine-config-pools-unpause_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

After the OpenShift Container Platform update is complete, unpause your custom machine config pools (MCP) one at a time. Unpausing an MCP allows the Machine Config Operator (MCO) to update the nodes associated with that MCP.

**Procedure**

1. Patch the MCP that you want to unpause:

   ```
   $ oc patch mcp/<mcp_name> --patch '{"spec":{"paused":false}}' --type=merge
   ```

   For example:

   ```
   $  oc patch mcp/workerpool-canary --patch '{"spec":{"paused":false}}' --type=merge
   ```

   **Example output**

   ```
   machineconfigpool.machineconfiguration.openshift.io/workerpool-canary patched
   ```
2. Optional: Check the progress of the update by using one of the following options:

   1. Check the progress from the web console by clicking **Administration** → **Cluster settings**.
   2. Check the progress by running the following command:

      ```
      $ oc get machineconfigpools
      ```
3. Test your applications on the updated nodes to ensure that they are working as expected.
4. Repeat this process for any other paused MCPs, one at a time.

   Note

   In case of a failure, such as your applications not working on the updated nodes, you can cordon and drain the nodes in the pool, which moves the application pods to other nodes to help maintain the quality-of-service for the applications. This first MCP should be no larger than the excess capacity.

#### [3.4.9. Moving a node to the original machine config pool](#update-using-custom-machine-config-pools-mcp-remove_update-using-custom-machine-config-pools) Copy linkLink copied to clipboard!

After you update and verify applications on nodes in a custom machine config pool (MCP), move the nodes back to their original MCP by removing the custom label that you added to the nodes.

Important

A node must have a role to be properly functioning in the cluster.

**Procedure**

1. For each node in a custom MCP, remove the custom label from the node by running the following command:

   ```
   $ oc label node <node_name> node-role.kubernetes.io/<custom_label>-
   ```

   For example:

   ```
   $ oc label node ci-ln-0qv1yp2-f76d1-kl2tq-worker-a-j2ssz node-role.kubernetes.io/workerpool-canary-
   ```

   **Example output**

   ```
   node/ci-ln-0qv1yp2-f76d1-kl2tq-worker-a-j2ssz labeled
   ```

   The Machine Config Operator moves the nodes back to the original MCP and reconciles the node to the MCP configuration.
2. To ensure that node has been removed from the custom MCP, view the list of MCPs in the cluster and their current state by running the following command:

   ```
   $ oc get mcp
   ```

   **Example output**

   ```
   NAME                CONFIG                                                   UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   master              rendered-master-1203f157d053fd987c7cbd91e3fbc0ed         True      False      False      3              3                   3                     0                      61m
   workerpool-canary   rendered-mcp-noupdate-5ad4791166c468f3a35cd16e734c9028   True      False      False      0              0                   0                     0                      21m
   worker              rendered-worker-5ad4791166c468f3a35cd16e734c9028         True      False      False      3              3                   3                     0                      61m
   ```

   When the node is removed from the custom MCP and moved back to the original MCP, it can take several minutes to update the machine counts. In this example, one node was moved from the removed `workerpool-canary` MCP to the `worker` MCP.
3. Optional: Delete the custom MCP by running the following command:

   ```
   $ oc delete mcp <mcp_name>
   ```

### [3.5. Updating a cluster in a disconnected environment](#updating-disconnected-cluster) Copy linkLink copied to clipboard!

You can update a cluster in an environment without access to the internet by taking additional steps to prepare your environment.

For information about updating a cluster in a disconnected environment, see [About cluster updates in a disconnected environment](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#about-disconnected-updates).

### [3.6. Updating hardware on nodes running on vSphere](#updating-hardware-on-nodes-running-on-vsphere) Copy linkLink copied to clipboard!

You must ensure that your nodes running in vSphere are running on the hardware version supported by OpenShift Container Platform. Currently, hardware version 15 or later is supported for vSphere virtual machines in a cluster. You can update your virtual hardware immediately or schedule an update in vCenter.

Important

* Version 4.22 of OpenShift Container Platform requires VMware virtual hardware version 15 or later.
* Before upgrading OpenShift 4.12 to OpenShift 4.13, you must update vSphere to **v8.0 Update 1 or later**; otherwise, the OpenShift 4.12 cluster is marked **un-upgradeable**.

Warning

Updating custom API certificates triggers the Machine Config Operator (MCO) to initiate a rolling reboot of the control plane nodes. These nodes must be updated serially. Ensure each node returns to a `Ready` state and the `etcd` static pods are healthy before the next node in the sequence begins its update. Failure to do so might result in a loss of etcd quorum and cluster-wide downtime.

#### [3.6.1. Updating the virtual hardware for control plane nodes on vSphere](#update-vsphere-virtual-hardware-on-control-plane-nodes_updating-hardware-on-nodes-running-in-vsphere) Copy linkLink copied to clipboard!

You can update the virtual hardware for control plane nodes on vSphere.

To reduce the risk of downtime, it is recommended that control plane nodes be updated serially. This ensures that the Kubernetes API remains available and etcd retains quorum.

**Prerequisites**

* You have cluster administrator permissions to execute the required permissions in the vCenter instance hosting your OpenShift Container Platform cluster.
* Your vSphere ESXi hosts are version 8.0 Update 1 or later, or VWware vSphere Foundation 9, or VMware Cloud Foundation 9.

**Procedure**

1. List the control plane nodes in your cluster by running the following command:

   ```
   $ oc get nodes -l node-role.kubernetes.io/master
   ```

   **Example output**

   ```
   NAME                    STATUS   ROLES    AGE   VERSION
   control-plane-node-0    Ready    master   75m   v1.35.4
   control-plane-node-1    Ready    master   75m   v1.35.4
   control-plane-node-2    Ready    master   75m   v1.35.4
   ```

   Note the names of your control plane nodes.
2. Mark the control plane node as unschedulable by running the following command:

   ```
   $ oc adm cordon <control_plane_node>
   ```
3. Shut down the virtual machine (VM) associated with the control plane node. Do this in the vSphere client by right-clicking the VM and selecting **Power** → **Shut Down Guest OS**. Do not shut down the VM using **Power Off** because it might not shut down safely.
4. Update the VM in the vSphere client. Follow [Upgrade the Compatibility of a Virtual Machine Manually](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-60768C2F-72E1-42E0-8A17-CA76849F2950.html) (VMware vSphere documentation).
5. Power on the VM associated with the control plane node. Do this in the vSphere client by right-clicking the VM and selecting **Power On**.
6. Run the following command and wait for the node to report as `Ready`:

   ```
   $ oc wait --for=condition=Ready node/<control_plane_node>
   ```
7. Mark the control plane node as schedulable again by running the following command:

   ```
   $ oc adm uncordon <control_plane_node>
   ```
8. Repeat this procedure for each control plane node in your cluster.

#### [3.6.2. Updating the virtual hardware for compute nodes on vSphere](#update-vsphere-virtual-hardware-on-compute-nodes_updating-hardware-on-nodes-running-in-vsphere) Copy linkLink copied to clipboard!

You can update the virtual hardware for compute nodes on vSphere.

To reduce the risk of downtime, it is recommended that compute nodes be updated serially.

Note

Multiple compute nodes can be updated in parallel given workloads are tolerant of having multiple nodes in a `NotReady` state. It is the responsibility of the administrator to ensure that the required compute nodes are available.

**Prerequisites**

* You have cluster administrator permissions to execute the required permissions in the vCenter instance hosting your OpenShift Container Platform cluster.
* Your vSphere ESXi hosts are version 8.0 Update 1 or later, or VWware vSphere Foundation 9, or VMware Cloud Foundation 9.

**Procedure**

1. List the compute nodes in your cluster by running the following command:

   ```
   $ oc get nodes -l node-role.kubernetes.io/worker
   ```

   **Example output**

   ```
   NAME              STATUS   ROLES    AGE   VERSION
   compute-node-0    Ready    worker   30m   v1.35.4
   compute-node-1    Ready    worker   30m   v1.35.4
   compute-node-2    Ready    worker   30m   v1.35.4
   ```

   Note the names of your compute nodes.
2. Mark the compute node as unschedulable by running the following command:

   ```
   $ oc adm cordon <compute_node>
   ```
3. Evacuate the pods from the compute node. There are several ways to do this. For example, you can evacuate all or selected pods on a node by running the following command:

   ```
   $ oc adm drain <compute_node> [--pod-selector=<pod_selector>]
   ```

   See "Evacuating pods on nodes" for other options to evacuate pods from a node.
4. Shut down the virtual machine (VM) associated with the compute node. Do this in the vSphere client by right-clicking the VM and selecting **Power** → **Shut Down Guest OS**. Do not shut down the VM using **Power Off** because it might not shut down safely.
5. Update the VM in the vSphere client. Follow [Upgrade the Compatibility of a Virtual Machine Manually](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-60768C2F-72E1-42E0-8A17-CA76849F2950.html) (VMware vSphere documentation).
6. Power on the VM associated with the compute node. Do this in the vSphere client by right-clicking the VM and selecting **Power On**.
7. Run the following command and wait for the node to report as `Ready`:

   ```
   $ oc wait --for=condition=Ready node/<compute_node>
   ```
8. Mark the compute node as schedulable again by running the following command:

   ```
   $ oc adm uncordon <compute_node>
   ```
9. Repeat this procedure for each compute node in your cluster.

#### [3.6.3. Updating the virtual hardware for template on vSphere](#update-vsphere-virtual-hardware-on-template_updating-hardware-on-nodes-running-in-vsphere) Copy linkLink copied to clipboard!

You can update the virtual hardware for templates on vSphere.

**Prerequisites**

* You have cluster administrator permissions to execute the required permissions in the vCenter instance hosting your OpenShift Container Platform cluster.
* Your vSphere ESXi hosts are version 8.0 Update 1 or later, or VWware vSphere Foundation 9, or VMware Cloud Foundation 9.

**Procedure**

1. If the RHCOS template is configured as a vSphere template, follow [Convert a Template to a Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-D632CAC5-BA5E-4A1E-959B-382D9ACB1DD0_copy.html) (VMware vSphere documentation).

   Note

   Once converted from a template, do not power on the virtual machine.
2. Update the virtual machine (VM) in the VMware vSphere client. Complete the steps outlined in [Upgrade the Compatibility of a Virtual Machine Manually](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-60768C2F-72E1-42E0-8A17-CA76849F2950.html) (VMware vSphere documentation).

   Important

   If you modified the VM settings, those changes might reset after moving to a newer virtual hardware. Please review that all your configured settings are still in place after your upgrade before proceeding to the next step.
3. Convert the VM in the vSphere client to a template by right-clicking on the VM and then selecting **Template → Convert to Template**.

   Important

   The steps for converting a VM to a template might change in future vSphere documentation versions.

#### [3.6.4. Scheduled updates for virtual hardware on vSphere](#scheduling-virtual-hardware-update-on-vsphere_updating-hardware-on-nodes-running-in-vsphere) Copy linkLink copied to clipboard!

Virtual hardware updates can be scheduled to occur when a virtual machine is powered on or rebooted. You can schedule your virtual hardware updates exclusively in vCenter by following [Schedule a Compatibility Upgrade for a Virtual Machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-96C06236-C271-4CFE-857E-22D1FDEECC95.html) (VMware vSphere documentation).

When scheduling an update prior to performing an update of OpenShift Container Platform, the virtual hardware update occurs when the nodes are rebooted during the course of the OpenShift Container Platform update.

### [3.7. Migrating to a cluster with multi-architecture compute machines](#migrating-clusters-to-multi-payload) Copy linkLink copied to clipboard!

You can migrate your current cluster with single-architecture compute machines to a cluster with multi-architecture compute machines by updating to a multi-architecture, manifest-listed payload. This allows you to add mixed architecture compute nodes to your cluster.

For information about configuring your multi-architecture compute machines, see "Configuring multi-architecture compute machines on an OpenShift Container Platform cluster".

Before migrating your single-architecture cluster to a cluster with multi-architecture compute machines, it is recommended to install the Multiarch Tuning Operator, and deploy a `ClusterPodPlacementConfig` custom resource. For more information, see [Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#multiarch-tuning-operator).

Important

Migration from a multi-architecture payload to a single-architecture payload is not supported. Once a cluster has transitioned to using a multi-architecture payload, it can no longer accept a single-architecture update payload.

#### [3.7.1. Migrating to a cluster with multi-architecture compute machines using the CLI](#migrating-to-multi-arch-cli_updating-clusters-overview) Copy linkLink copied to clipboard!

You can use the OpenShift CLI (`oc`) to migrate to a cluster with multi-architecture compute machines.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* Your OpenShift Container Platform version is 4.13.0 or later.

  For more information on how to update your cluster version, see "Updating a cluster using the web console" or "Updating a cluster using the CLI".
* You have installed the OpenShift CLI (`oc`) that matches the version for your current cluster.
* Your `oc` client is updated to version 4.13.0 or later.
* Your OpenShift Container Platform cluster is installed on AWS, Azure, Google Cloud, bare metal, or IBM P/Z platforms.

  For more information on selecting a supported platform for your cluster installation, see "Selecting a cluster installation type".

**Procedure**

1. Verify that the `RetrievedUpdates` condition is `True` in the Cluster Version Operator (CVO) by running the following command:

   ```
   $ oc get clusterversion/version -o=jsonpath="{.status.conditions[?(.type=='RetrievedUpdates')].status}"
   ```

   If the `RetrievedUpates` condition is `False`, you can find supplemental information regarding the failure by using the following command:

   ```
   $ oc adm upgrade
   ```

   For more information about cluster version condition types, see "Understanding cluster version condition types".
2. If the condition `RetrievedUpdates` is `False`, change the channel to `stable-<4.y>` or `fast-<4.y>` by running the following command:

   ```
   $ oc adm upgrade channel <channel>
   ```

   After setting the channel, verify if `RetrievedUpdates` is `True`.

   For more information about channels, see "Understanding update channels and releases".
3. Migrate to the multi-architecture payload by running the following command:

   ```
   $ oc adm upgrade --to-multi-arch
   ```

**Verification**

* Monitor the migration by running the following command:

  ```
  $ oc adm upgrade
  ```

  **Example output**

  ```
  working towards ${VERSION}: 106 of 841 done (12% complete), waiting on machine-config
  ```

  Important

  Machine launches may fail as the cluster settles into the new state. To notice and recover when machines fail to launch, it is recommended that you deploy machine health checks. For more information about machine health checks and how to deploy them, see "About machine health checks".

  1. Optional: Retrieve more detailed information about the status of your update and monitor the migration by running the following command:

     ```
     $ oc adm upgrade status
     ```

     For more information about how to use the `oc adm upgrade status` command, see "Gathering cluster update status using oc adm upgrade status (Technology Preview)".

The migrations must be complete and all the cluster operators must be stable before you can add compute machine sets with different architectures to your cluster.

#### [3.7.2. Migrating the x86 control plane to arm64 architecture on Amazon Web Services](#migrating-from-x86-to-arm64-cp_updating-clusters-overview) Copy linkLink copied to clipboard!

You can migrate the control plane in your cluster from `x86` to `arm64` architecture on Amazon Web Services (AWS).

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You logged in to `oc` as a user with `cluster-admin` privileges.

**Procedure**

1. Check the architecture of the control plane nodes by running the following command:

   ```
   $ oc get nodes -o wide
   ```

   **Example output**

   ```
   NAME                          STATUS   ROLES                  AGE    VERSION   INTERNAL-IP EXTERNAL-IP   OS-IMAGE                                         KERNEL-VERSION                 CONTAINER-RUNTIME
   worker-001.example.com        Ready    worker                 100d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
   worker-002.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
   worker-003.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
   master-001.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
   master-002.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
   master-003.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
   ```

   The `KERNEL-VERSION` field in the output indicates the architecture of the nodes.
2. Check that your cluster uses the multi payload by running the following command:

   ```
   $ oc adm release info -o jsonpath="{ .metadata.metadata}"
   ```

   If you see the following output, the cluster is multi-architecture compatible.

   ```
   {
    "release.openshift.io/architecture": "multi",
    "url": "https://access.redhat.com/errata/<errata_version>"
   }
   ```

   If the cluster is not using the multi payload, migrate the cluster to a multi-architecture cluster. For more information, see "Migrating to a cluster with multi-architecture compute machines using the CLI".
3. Update your image stream from single-architecture to multi-architecture by running the following command:

   ```
   $ oc import-image <multiarch_image_stream_tag>  --from=<registry>/<project_name>/<image_name> \
   --import-mode='PreserveOriginal'
   ```
4. Get the `arm64` compatible Amazon Machine Image (AMI) for configuring the control plane machine set by running the following command:

   ```
   $ oc get configmap/coreos-bootimages -n openshift-machine-config-operator -o jsonpath='{.data.stream}' | jq -r '.architectures.aarch64.images.aws.regions."<aws_region>".image'
   ```

   Replace `<aws_region>` with the AWS region where the current cluster is installed. You can get the AWS region for the installed cluster by running the following command:

   ```
   $ oc get infrastructure cluster -o jsonpath='{.status.platformStatus.aws.region}'
   ```

   **Example output**

   ```
   ami-xxxxxxx
   ```
5. Update the control plane machine set to support the `arm64` architecture by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster -n openshift-machine-api
   ```

   1. Update the `instanceType` field to a type that supports the `arm64` architecture, and set the `ami.id` field to an AMI that is compatible with the `arm64` architecture. For information about supported instance types, see "Tested instance types for AWS on 64-bit ARM infrastructures".

      For more information about configuring the control plane machine set for AWS, see "Control plane configuration options for Amazon Web Services".

**Verification**

* Verify that the control plane nodes are now running on the `arm64` architecture by running the following command:

  ```
  $ oc get nodes -o wide
  ```

  **Example output**

  ```
  NAME                          STATUS   ROLES                  AGE    VERSION   INTERNAL-IP EXTERNAL-IP   OS-IMAGE                                         KERNEL-VERSION                 CONTAINER-RUNTIME
  worker-001.example.com        Ready    worker                 100d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
  worker-002.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
  worker-003.example.com        Ready    worker                 98d    v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
  master-001.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.aarch64   cri-o://1.30.x
  master-002.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.aarch64   cri-o://1.30.x
  master-003.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.aarch64   cri-o://1.30.x
  ```

#### [3.7.3. Migrating control plane or infra machine sets between architectures on Google Cloud](#multiarch-migrating-cp-infra-gcp_updating-clusters-overview) Copy linkLink copied to clipboard!

You can migrate the control plane or infra machine sets in your Google Cloud cluster between `x86` and `arm64` architectures.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You logged in to `oc` as a user with `cluster-admin` privileges.

**Procedure**

1. Check the architecture of the control plane or infra nodes by running the following command:

   ```
   $ oc get nodes -o wide
   ```

   **Example output**

   ```
   NAME                          STATUS   ROLES                  AGE    VERSION   INTERNAL-IP EXTERNAL-IP   OS-IMAGE                                         KERNEL-VERSION                 CONTAINER-RUNTIME
   worker-001.example.com        Ready    infra                  100d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
   master-001.example.com        Ready    control-plane,master   120d   v1.30.7   10.x.x.x    <none>        Red Hat Enterprise Linux CoreOS 4xx.xx.xxxxx-0   5.x.x-xxx.x.x.el9_xx.x86_64    cri-o://1.30.x
   ```

   The `KERNEL-VERSION` field in the output indicates the architecture of the nodes.
2. Check that your cluster uses the multi payload by running the following command:

   ```
   $ oc adm release info -o jsonpath="{ .metadata.metadata}"
   ```

   If you see the following output, the cluster is multi-architecture compatible.

   ```
   {
    "release.openshift.io/architecture": "multi",
    "url": "https://access.redhat.com/errata/<errata_version>"
   }
   ```

   If the cluster is not using the multi payload, migrate the cluster to a multi-architecture cluster. For more information, see "Migrating to a cluster with multi-architecture compute machines".
3. If you use any custom image streams, update them from single-architecture to multi-architecture by running the following command for each image stream:

   ```
   $ oc import-image <multiarch_image_stream_tag>  --from=<registry>/<project_name>/<image_name> \
   --import-mode='PreserveOriginal'
   ```
4. Select an instance type that matches the target architecture from [General-purpose machine family for Compute engine](https://cloud.google.com/compute/docs/general-purpose-machines) (Google documentation). Check the [Available regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) table (Google documentation) to verify that the instance type is supported in your zone.
5. Select a supported disk type for the instance type that you selected from the "Supported disk types" section of [General-purpose machine family for Compute engine](https://cloud.google.com/compute/docs/general-purpose-machines) (Google documentation).
6. Determine the Google Cloud image that the machine set uses after migration by running the following command:

   ```
   $ oc get configmap/coreos-bootimages \
     -n openshift-machine-config-operator \
     -o jsonpath='{.data.stream}' | jq \
     -r '.architectures.aarch64.images.gcp'
   ```

   **Example output**

   ```
   "gcp": {
       "release": "415.92.202309142014-0",
       "project": "rhcos-cloud",
       "name": "rhcos-415-92-202309142014-0-gcp-aarch64"
     }
   ```

   Use the `project` and `name` parameters from the output to form the `image` parameter in the following format: `projects/<project>/global/images/<name>`.
7. To migrate the control plane to another architecture, run the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster -n openshift-machine-api
   ```

   1. Replace the `disks.type` parameter with the disk type that you selected.
   2. Replace the `disks.image` parameter with the `image` parameter that you formed previously.
   3. Replace the `machineType` parameter with the instance type that you selected.
8. To migrate an infra machine set to another architecture, run the following command using the ID of an infra machine set:

   ```
   $ oc edit machineset <infra-machine-set_id> -n openshift-machine-api
   ```

   1. Replace the `disks.type` parameter with the disk type that you selected.
   2. Replace the `disks.image` parameter with the `image` parameter that you formed previously.
   3. Replace the `machineType` parameter with the instance type that you selected.

### [3.8. Updating the boot loader on RHCOS nodes using bootupd](#updating-bootloader-rhcos) Copy linkLink copied to clipboard!

To update the boot loader on RHCOS nodes using `bootupd`, you must either run the `bootupctl update` command on RHCOS machines manually or provide a machine config with a `systemd` unit.

Unlike `grubby` or other boot loader tools, `bootupd` does not manage kernel space configuration such as passing kernel arguments. To configure kernel arguments, see [Adding kernel arguments to nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-nodes-kernel-arguments_nodes-nodes-managing).

Note

You can use `bootupd` to update the boot loader to protect against the BootHole vulnerability.

#### [3.8.1. Updating the boot loader manually](#updating-bootloader-manual_updating-bootloader-rhcos) Copy linkLink copied to clipboard!

You can manually inspect the status of the system and update the boot loader by using the `bootupctl` command-line tool.

**Procedure**

1. Inspect the system status by running the following command:

   ```
   # bootupctl status
   ```

   **Example output for `x86_64`**

   ```
   Component EFI
     Installed: grub2-efi-x64-1:2.04-31.el8_4.1.x86_64,shim-x64-15-8.el8_1.x86_64
     Update: At latest version
   ```

   **Example output for `aarch64`**

   ```
   Component EFI
     Installed: grub2-efi-aa64-1:2.02-99.el8_4.1.aarch64,shim-aa64-15.4-2.el8_1.aarch64
     Update: At latest version
   ```

2. OpenShift Container Platform clusters initially installed on version 4.4 and older require an explicit adoption phase.

   If the system status is `Adoptable`, perform the adoption by running the following command:

   ```
   # bootupctl adopt-and-update
   ```

   **Example output**

   ```
   Updated: grub2-efi-x64-1:2.04-31.el8_4.1.x86_64,shim-x64-15-8.el8_1.x86_64
   ```
3. If an update is available, apply the update so that the changes take effect on the next reboot by running the following command:

   ```
   # bootupctl update
   ```

   **Example output**

   ```
   Updated: grub2-efi-x64-1:2.04-31.el8_4.1.x86_64,shim-x64-15-8.el8_1.x86_64
   ```

#### [3.8.2. Updating the boot loader automatically by using a machine config](#updating-bootloader-auto_updating-bootloader-rhcos) Copy linkLink copied to clipboard!

You can automatically update the boot loader with `bootupd` by creating a systemd service unit that will update the boot loader as needed on every boot. This unit will run the `bootupctl update` command during the boot process and will be installed on the nodes via a machine config.

Note

This configuration is not enabled by default because unexpected interruptions of the update operation might lead to unbootable nodes. If you enable this configuration, make sure to avoid interrupting nodes during the boot process while the boot loader update is in progress. The boot loader update operation generally completes quickly thus the risk is low.

**Procedure**

1. Create a Butane config file, `99-worker-bootupctl-update.bu`, including the contents of the `bootupctl-update.service` systemd unit.

   Note

   The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane.

   **Example output**

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     name: 99-worker-chrony
     labels:
       machineconfiguration.openshift.io/role: worker
   systemd:
     units:
     - name: bootupctl-update.service
       enabled: true
       contents: |
         [Unit]
         Description=Bootupd automatic update

         [Service]
         ExecStart=/usr/bin/bootupctl update
         RemainAfterExit=yes

         [Install]
         WantedBy=multi-user.target
   ```

   On control plane nodes, substitute `master` for `worker` in `metadata.name` and `metadata.labels.machineconfiguration.openshift.io/role`.
2. Generate a `MachineConfig` object file, `99-worker-bootupctl-update.yaml`, containing the configuration to be delivered to the nodes by running the following command:

   ```
   $ butane 99-worker-bootupctl-update.bu -o 99-worker-bootupctl-update.yaml
   ```
3. Apply the configurations in one of two ways:

   * If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster.
   * If the cluster is already running, apply the file by running the following command:

     ```
     $ oc apply -f ./99-worker-bootupctl-update.yaml
     ```

## [Chapter 4. Troubleshooting a cluster update](#troubleshooting-a-cluster-update) Copy linkLink copied to clipboard!

### [4.1. Gathering data about your cluster update](#gathering-data-cluster-update) Copy linkLink copied to clipboard!

Collect cluster data, logs, and update history to help Red Hat Support diagnose and troubleshoot failed cluster updates.

#### [4.1.1. Gathering log data for a support case](#gathering-log-data_troubleshooting_updates) Copy linkLink copied to clipboard!

Use the `oc adm must-gather` command to collect cluster data and logs. Red Hat Support can then use the data and logs to diagnose and resolve support cases.

#### [4.1.2. Changing CVO log level (Technology Preview)](#changing-log-data_troubleshooting_updates) Copy linkLink copied to clipboard!

Important

Changing the CVO log level is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Adjust the verbosity of the Cluster Version Operator (CVO) log to troubleshoot update issues or diagnose errors by using four available log levels.

The following list outlines the four log levels:

* `Normal` - The default log level. Contains working log information. Used when everything is fine. Provides helpful notices for auditing or common operations.
* `Debug` - Used when something goes wrong. Expect a higher quantity of notices.
* `Trace` - Used to diagnose errors.
* `TraceAll` - Used to get the complete body content of the logs.

Note

If `TraceAll` is turned on in a production cluster it may cause widespread performance issues and large log files.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the OpenShift CLI (`oc`).
* You have the `TechPreviewNoUpgrade` feature set enabled.

**Procedure**

1. Enter the following command into the CLI to change the log level:

   ```
   $ oc patch clusterversionoperator/cluster --type=merge --patch '{"spec":{"operatorLogLevel":"<log_level>"}}'
   ```

   **Example output**

   ```
   clusterversionoperator.operator.openshift.io/cluster patched
   ```

#### [4.1.3. Gathering ClusterVersion history](#gathering-clusterversion-history_troubleshooting_updates) Copy linkLink copied to clipboard!

The Cluster Version Operator (CVO) records updates made to a cluster, known as the ClusterVersion history. The entries can reveal correlation between changes in cluster behavior with potential triggers, although correlation does not imply causation.

Note

The initial, minor, and z-stream version updates are stored by the ClusterVersion history. However, the ClusterVersion history has a size limit. If the limit is reached, the oldest z-stream updates in previous minor versions are pruned to accommodate the limit.

You can view the ClusterVersion history by using the OpenShift Container Platform web console or by using the OpenShift CLI (`oc`).

##### [4.1.3.1. Gathering ClusterVersion history in the OpenShift Container Platform web console](#gathering-clusterversion-history-console_troubleshooting_updates) Copy linkLink copied to clipboard!

You can view the ClusterVersion history and status information in the OpenShift Container Platform web console. Use the history to verify successful updates and to troubleshoot failures.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have access to the OpenShift Container Platform web console.

**Procedure**

* From the web console, click **Administration** → **Cluster Settings** and review the contents of the **Details** tab.

##### [4.1.3.2. Gathering ClusterVersion history using the OpenShift CLI (oc)](#gathering-clusterversion-history-cli_troubleshooting_updates) Copy linkLink copied to clipboard!

Use the OpenShift CLI (`oc`) to view ClusterVersion history. You can use the history to troubleshoot update issues or to verify completed updates.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. View the cluster update history by entering the following command:

   ```
   $ oc describe clusterversions/version
   ```

   **Example output**

   ```
     Desired:
       Channels:
         candidate-4.13
         candidate-4.14
         fast-4.13
         fast-4.14
         stable-4.13
       Image:    quay.io/openshift-release-dev/ocp-release@sha256:a148b19231e4634196717c3597001b7d0af91bf3a887c03c444f59d9582864f4
       URL:      https://access.redhat.com/errata/RHSA-2023:6130
       Version:  4.13.19
     History:
       Completion Time:    2023-11-07T20:26:04Z
       Image:              quay.io/openshift-release-dev/ocp-release@sha256:a148b19231e4634196717c3597001b7d0af91bf3a887c03c444f59d9582864f4
       Started Time:       2023-11-07T19:11:36Z
       State:              Completed
       Verified:           true
       Version:            4.13.19
       Completion Time:    2023-10-04T18:53:29Z
       Image:              quay.io/openshift-release-dev/ocp-release@sha256:eac141144d2ecd6cf27d24efe9209358ba516da22becc5f0abc199d25a9cfcec
       Started Time:       2023-10-04T17:26:31Z
       State:              Completed
       Verified:           true
       Version:            4.13.13
       Completion Time:    2023-09-26T14:21:43Z
       Image:              quay.io/openshift-release-dev/ocp-release@sha256:371328736411972e9640a9b24a07be0af16880863e1c1ab8b013f9984b4ef727
       Started Time:       2023-09-26T14:02:33Z
       State:              Completed
       Verified:           false
       Version:            4.13.12
     Observed Generation:  4
     Version Hash:         CMLl3sLq-EA=
   Events:                 <none>
   ```

## [Legal Notice](#idm139685294070656) Copy linkLink copied to clipboard!

Copyright © Red Hat

OpenShift documentation is licensed under the Apache License 2.0 (<https://www.apache.org/licenses/LICENSE-2.0>).

Modified versions must remove all Red Hat trademarks.

Portions adapted from <https://github.com/kubernetes-incubator/service-catalog/> with modifications by Red Hat.

Red Hat, Red Hat Enterprise Linux, the Red Hat logo, the Shadowman logo, JBoss, OpenShift, Fedora, the Infinity logo, and RHCE are trademarks of Red Hat, Inc., registered in the United States and other countries.

Linux® is the registered trademark of Linus Torvalds in the United States and other countries.

Java® is a registered trademark of Oracle and/or its affiliates.

XFS® is a trademark of Silicon Graphics International Corp. or its subsidiaries in the United States and/or other countries.

MySQL® is a registered trademark of MySQL AB in the United States, the European Union and other countries.

Node.js® is an official trademark of the OpenJS Foundation.

The OpenStack® Word Mark and OpenStack logo are either registered trademarks/service marks or trademarks/service marks of the OpenStack Foundation, in the United States and other countries and are used with the OpenStack Foundation’s permission. We are not affiliated with, endorsed or sponsored by the OpenStack Foundation, or the OpenStack community.

All other trademarks are the property of their respective owners.
