---
title: "API overview"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/api_overview/index
retrieved_at: 2026-09-05T05:41:31.982895+00:00
---

# API overview

---

OpenShift Container Platform 4.22

## Overview content for the OpenShift Container Platform API

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139711186143376)

**Abstract**

This document provides overview information for OpenShift Container Platform API.

---

## [Chapter 1. Understanding API tiers](#understanding-api-support-tiers) Copy linkLink copied to clipboard!

Important

This guidance does not cover layered OpenShift Container Platform offerings.

API tiers for bare-metal configurations also apply to virtualized configurations except for any feature that directly interacts with hardware. Those features directly related to hardware have no application operating environment (AOE) compatibility level beyond that which is provided by the hardware vendor. For example, applications that rely on Graphics Processing Units (GPU) features are subject to the AOE compatibility provided by the GPU vendor driver.

API tiers in a cloud environment for cloud specific integration points have no API or AOE compatibility level beyond that which is provided by the hosting cloud vendor. For example, APIs that exercise dynamic management of compute, ingress, or storage are dependent upon the underlying API capabilities exposed by the cloud platform. Where a cloud vendor modifies a prerequisite API, Red Hat will provide commercially reasonable efforts to maintain support for the API with the capability presently offered by the cloud infrastructure vendor.

Red Hat requests that application developers validate that any behavior they depend on is explicitly defined in the formal API documentation to prevent introducing dependencies on unspecified implementation-specific behavior or dependencies on bugs in a particular implementation of an API. For example, new releases of an ingress router may not be compatible with older releases if an application uses an undocumented API or relies on undefined behavior.

### [1.1. API tiers](#api-tiers_understanding-api-tiers) Copy linkLink copied to clipboard!

All commercially supported APIs, components, and features are associated under one of the following support levels:

#### [1.1.1. API tier 1](#api-tier-1_understanding-api-tiers) Copy linkLink copied to clipboard!

APIs and application operating environments (AOEs) are stable within a major version. APIs and AOEs can be deprecated within a major version; however, they will not be removed until a subsequent major version.

After an API or AOE is deprecated, the API or AOE will be available for a minimum of one year or until the next major version is released, whichever is longer.

#### [1.1.2. API tier 2](#api-tier-2_understanding-api-tiers) Copy linkLink copied to clipboard!

APIs and AOEs are stable within a major release for a minimum of 9 months or 3 minor releases from the announcement of deprecation, whichever is longer.

#### [1.1.3. API tier 3](#api-tier-3_understanding-api-tiers) Copy linkLink copied to clipboard!

This level applies to languages, tools, applications, and optional Operators included with OpenShift Container Platform through Operator Hub. Each component will specify a lifetime during which the API and AOE will be supported. Newer versions of language runtime specific components will attempt to be as API and AOE compatible from minor version to minor version as possible. Minor version to minor version compatibility is not guaranteed, however.

Components and developer tools that receive continuous updates through the Operator Hub, referred to as Operators and operands, should be considered API tier 3. Developers should use caution and understand how these components may change with each minor release. Users are encouraged to consult the compatibility guidelines documented by the component.

#### [1.1.4. API tier 4](#api-tier-4_understanding-api-tiers) Copy linkLink copied to clipboard!

No compatibility is provided. API and AOE can change at any point. These capabilities should not be used by applications needing long-term support.

It is common practice for Operators to use custom resource definitions (CRDs) internally to accomplish a task. These objects are not meant for use by actors external to the Operator and are intended to be hidden. If any CRD is not meant for use by actors external to the Operator, the `operators.operatorframework.io/internal-objects` annotation in the Operators `ClusterServiceVersion` (CSV) should be specified to signal that the corresponding resource is internal use only and the CRD may be explicitly labeled as tier 4.

### [1.2. Mapping API tiers to API groups](#api-support-tiers-mapping_understanding-api-tiers) Copy linkLink copied to clipboard!

For each API tier defined by Red Hat, we provide a mapping table for specific API groups where the upstream communities are committed to maintain forward compatibility. Any API group that does not specify an explicit compatibility level and is not specifically discussed below is assigned API tier 3 by default except for `v1alpha1` APIs which are assigned tier 4 by default.

#### [1.2.1. Support for Kubernetes API groups](#mapping-support-tiers-to-kubernetes-api-groups_understanding-api-tiers) Copy linkLink copied to clipboard!

API groups that end with the suffix `*.k8s.io` or have the form `version.<name>` with no suffix are governed by the Kubernetes deprecation policy and follow a general mapping between API version exposed and corresponding support tier unless otherwise specified.

Expand

| API version example | API tier |
| --- | --- |
| `v1` | Tier 1 |
| `v1beta1` | Tier 2 |
| `v1alpha1` | Tier 4 |

Show more

#### [1.2.2. Support for OpenShift API groups](#mapping-support-tiers-to-openshift-api-groups_understanding-api-tiers) Copy linkLink copied to clipboard!

API groups that end with the suffix `*.openshift.io` are governed by the OpenShift Container Platform deprecation policy and follow a general mapping between API version exposed and corresponding compatibility level unless otherwise specified.

Expand

| API version example | API tier |
| --- | --- |
| `apps.openshift.io/v1` | Tier 1 |
| `authorization.openshift.io/v1` | Tier 1, some tier 1 deprecated |
| `build.openshift.io/v1` | Tier 1, some tier 1 deprecated |
| `config.openshift.io/v1` | Tier 1 |
| `image.openshift.io/v1` | Tier 1 |
| `network.openshift.io/v1` | Tier 1 |
| `network.operator.openshift.io/v1` | Tier 1 |
| `oauth.openshift.io/v1` | Tier 1 |
| `imagecontentsourcepolicy.operator.openshift.io/v1alpha1` | Tier 1 |
| `project.openshift.io/v1` | Tier 1 |
| `quota.openshift.io/v1` | Tier 1 |
| `route.openshift.io/v1` | Tier 1 |
| `quota.openshift.io/v1` | Tier 1 |
| `security.openshift.io/v1` | Tier 1 except for `RangeAllocation` (tier 4) and `*Reviews` (tier 2) |
| `template.openshift.io/v1` | Tier 1 |
| `console.openshift.io/v1` | Tier 2 |

Show more

#### [1.2.3. Support for Monitoring API groups](#mapping-support-tiers-to-monitoring-api-groups_understanding-api-tiers) Copy linkLink copied to clipboard!

API groups that end with the suffix `monitoring.coreos.com` have the following mapping:

Expand

| API version example | API tier |
| --- | --- |
| `v1` | Tier 1 |
| `v1alpha1` | Tier 1 |
| `v1beta1` | Tier 1 |

Show more

#### [1.2.4. Support for Operator Lifecycle Manager API groups](#mapping-support-tiers-to-olm-api-groups_understanding-api-tiers) Copy linkLink copied to clipboard!

Operator Lifecycle Manager (OLM) provides APIs that include API groups with the suffix `operators.coreos.com`. These APIs have the following mapping:

Expand

| API version example | API tier |
| --- | --- |
| `v2` | Tier 1 |
| `v1` | Tier 1 |
| `v1alpha1` | Tier 1 |

Show more

### [1.3. API deprecation policy](#api-deprecation-policy_understanding-api-tiers) Copy linkLink copied to clipboard!

OpenShift Container Platform is composed of many components sourced from many upstream communities. It is anticipated that the set of components, the associated API interfaces, and correlated features will evolve over time and might require formal deprecation in order to remove the capability.

#### [1.3.1. Deprecating parts of the API](#deprecating-parts-of-the-api_understanding-api-tiers) Copy linkLink copied to clipboard!

OpenShift Container Platform is a distributed system where multiple components interact with a shared state managed by the cluster control plane through a set of structured APIs. Per Kubernetes conventions, each API presented by OpenShift Container Platform is associated with a group identifier and each API group is independently versioned. Each API group is managed in a distinct upstream community including Kubernetes, Metal3, Multus, Operator Framework, Open Cluster Management, OpenShift itself, and more.

While each upstream community might define their own unique deprecation policy for a given API group and version, Red Hat normalizes the community specific policy to one of the compatibility levels defined prior based on our integration in and awareness of each upstream community to simplify end-user consumption and support.

The deprecation policy and schedule for APIs vary by compatibility level.

The deprecation policy covers all elements of the API including:

* REST resources, also known as API objects
* Fields of REST resources
* Annotations on REST resources, excluding version-specific qualifiers
* Enumerated or constant values

Other than the most recent API version in each group, older API versions must be supported after their announced deprecation for a duration of no less than:

Expand

| API tier | Duration |
| --- | --- |
| Tier 1 | Stable within a major release. They may be deprecated within a major release, but they will not be removed until a subsequent major release. |
| Tier 2 | 9 months or 3 releases from the announcement of deprecation, whichever is longer. |
| Tier 3 | See the component-specific schedule. |
| Tier 4 | None. No compatibility is guaranteed. |

Show more

The following rules apply to all tier 1 APIs:

* API elements can only be removed by incrementing the version of the group.
* API objects must be able to round-trip between API versions without information loss, with the exception of whole REST resources that do not exist in some versions. In cases where equivalent fields do not exist between versions, data will be preserved in the form of annotations during conversion.
* API versions in a given group can not deprecate until a new API version at least as stable is released, except in cases where the entire API object is being removed.

#### [1.3.2. Deprecating CLI elements](#deprecating-cli-elements_understanding-api-tiers) Copy linkLink copied to clipboard!

Client-facing CLI commands are not versioned in the same way as the API, but are user-facing component systems. The two major ways a user interacts with a CLI are through a command or flag, which is referred to in this context as CLI elements.

All CLI elements default to API tier 1 unless otherwise noted or the CLI depends on a lower tier API.

Expand

|  | Element | API tier |
| --- | --- | --- |
| Generally available (GA) | Flags and commands | Tier 1 |
| Technology Preview | Flags and commands | Tier 3 |
| Developer Preview | Flags and commands | Tier 4 |

Show more

#### [1.3.3. Deprecating an entire component](#deprecating-entire-component_understanding-api-tiers) Copy linkLink copied to clipboard!

The duration and schedule for deprecating an entire component maps directly to the duration associated with the highest API tier of an API exposed by that component. For example, a component that surfaced APIs with tier 1 and 2 could not be removed until the tier 1 deprecation schedule was met.

Expand

| API tier | Duration |
| --- | --- |
| Tier 1 | Stable within a major release. They may be deprecated within a major release, but they will not be removed until a subsequent major release. |
| Tier 2 | 9 months or 3 releases from the announcement of deprecation, whichever is longer. |
| Tier 3 | See the component-specific schedule. |
| Tier 4 | None. No compatibility is guaranteed. |

Show more

## [Chapter 2. Understanding API compatibility guidelines](#compatibility-guidelines) Copy linkLink copied to clipboard!

Important

This guidance does not cover layered OpenShift Container Platform offerings.

### [2.1. API compatibility guidelines](#api-compatibility-guidelines_compatibility-guidelines) Copy linkLink copied to clipboard!

Red Hat recommends that application developers adopt the following principles in order to improve compatibility with OpenShift Container Platform:

* Use APIs and components with support tiers that match the application’s need.
* Build applications using the published client libraries where possible.
* Applications are only guaranteed to run correctly if they execute in an environment that is as new as the environment it was built to execute against. An application that was built for OpenShift Container Platform 4.14 is not guaranteed to function properly on OpenShift Container Platform 4.13.
* Do not design applications that rely on configuration files provided by system packages or other components. These files can change between versions unless the upstream community is explicitly committed to preserving them. Where appropriate, depend on any Red Hat provided interface abstraction over those configuration files in order to maintain forward compatibility. Direct file system modification of configuration files is discouraged, and users are strongly encouraged to integrate with an Operator provided API where available to avoid dual-writer conflicts.
* Do not depend on API fields prefixed with `unsupported<FieldName>` or annotations that are not explicitly mentioned in product documentation.
* Do not depend on components with shorter compatibility guarantees than your application.
* Do not perform direct storage operations on the etcd server. All etcd access must be performed via the api-server or through documented backup and restore procedures.

Red Hat recommends that application developers follow the [compatibility guidelines](https://access.redhat.com/articles/rhel8-abi-compatibility#Guidelines) defined by Red Hat Enterprise Linux (RHEL). OpenShift Container Platform strongly recommends the following guidelines when building an application or hosting an application on the platform:

* Do not depend on a specific Linux kernel or OpenShift Container Platform version.
* Avoid reading from `proc`, `sys`, and `debug` file systems, or any other pseudo file system.
* Avoid using `ioctls` to directly interact with hardware.
* Avoid direct interaction with `cgroups` in order to not conflict with OpenShift Container Platform host-agents that provide the container execution environment.

Note

During the lifecycle of a release, Red Hat makes commercially reasonable efforts to maintain API and application operating environment (AOE) compatibility across all minor releases and z-stream releases. If necessary, Red Hat might make exceptions to this compatibility goal for critical impact security or other significant issues.

### [2.2. API compatibility exceptions](#api-compatibility-exceptions_compatibility-guidelines) Copy linkLink copied to clipboard!

The following are exceptions to compatibility in OpenShift Container Platform:

#### [2.2.1. RHEL CoreOS file system modifications not made with a supported Operator](#OS-file-system-modifications-not-made_compatibility-guidelines) Copy linkLink copied to clipboard!

No assurances are made at this time that a modification made to the host operating file system is preserved across minor releases except for where that modification is made through the public interface exposed via a supported Operator, such as the Machine Config Operator or Node Tuning Operator.

#### [2.2.2. Modifications to cluster infrastructure in cloud or virtualized environments](#modifications-to-cluster-infrastructure-in-cloud_compatibility-guidelines) Copy linkLink copied to clipboard!

No assurances are made at this time that a modification to the cloud hosting environment that supports the cluster is preserved except for where that modification is made through a public interface exposed in the product or is documented as a supported configuration. Cluster infrastructure providers are responsible for preserving their cloud or virtualized infrastructure except for where they delegate that authority to the product through an API.

#### [2.2.3. Functional defaults between an upgraded cluster and a new installation](#Functional-defaults-between-upgraded-cluster-new-installation_compatibility-guidelines) Copy linkLink copied to clipboard!

No assurances are made at this time that a new installation of a product minor release will have the same functional defaults as a version of the product that was installed with a prior minor release and upgraded to the equivalent version. For example, future versions of the product may provision cloud infrastructure with different defaults than prior minor versions. In addition, different default security choices may be made in future versions of the product than those made in past versions of the product. Past versions of the product will forward upgrade, but preserve legacy choices where appropriate specifically to maintain backwards compatibility.

#### [2.2.4. Usage of API fields that have the prefix "unsupported” or undocumented annotations](#API-fields-that-have-the-prefix-unsupported-annotations_compatibility-guidelines) Copy linkLink copied to clipboard!

Select APIs in the product expose fields with the prefix `unsupported<FieldName>`. No assurances are made at this time that usage of this field is supported across releases or within a release. Product support can request a customer to specify a value in this field when debugging specific problems, but its usage is not supported outside of that interaction. Usage of annotations on objects that are not explicitly documented are not assured support across minor releases.

#### [2.2.5. API availability per product installation topology](#API-availability-per-product-installation-topology_compatibility-guidelines) Copy linkLink copied to clipboard!

The OpenShift distribution will continue to evolve its supported installation topology, and not all APIs in one install topology will necessarily be included in another. For example, certain topologies may restrict read/write access to particular APIs if they are in conflict with the product installation topology or not include a particular API at all if not pertinent to that topology. APIs that exist in a given topology will be supported in accordance with the compatibility tiers defined above.

### [2.3. API compatibility common terminology](#api-compatibility-common-terminology_compatibility-guidelines) Copy linkLink copied to clipboard!

#### [2.3.1. Application Programming Interface (API)](#api-compatibility-common-terminology-api_compatibility-guidelines) Copy linkLink copied to clipboard!

An API is a public interface implemented by a software program that enables it to interact with other software. In OpenShift Container Platform, the API is served from a centralized API server and is used as the hub for all system interaction.

#### [2.3.2. Application Operating Environment (AOE)](#api-compatibility-common-terminology-aoe_compatibility-guidelines) Copy linkLink copied to clipboard!

An AOE is the integrated environment that executes the end-user application program. The AOE is a containerized environment that provides isolation from the host operating system (OS). At a minimum, AOE allows the application to run in an isolated manner from the host OS libraries and binaries, but still share the same OS kernel as all other containers on the host. The AOE is enforced at runtime and it describes the interface between an application and its operating environment. It includes intersection points between the platform, operating system and environment, with the user application including projection of downward API, DNS, resource accounting, device access, platform workload identity, isolation among containers, isolation between containers and host OS.

The AOE does not include components that might vary by installation, such as Container Network Interface (CNI) plugin selection or extensions to the product such as admission hooks. Components that integrate with the cluster at a level below the container environment might be subjected to additional variation between versions.

#### [2.3.3. Compatibility in a virtualized environment](#api-compatibility-common-terminology-virtualized_compatibility-guidelines) Copy linkLink copied to clipboard!

Virtual environments emulate bare-metal environments such that unprivileged applications that run on bare-metal environments will run, unmodified, in corresponding virtual environments. Virtual environments present simplified abstracted views of physical resources, so some differences might exist.

#### [2.3.4. Compatibility in a cloud environment](#api-compatibility-common-terminology-cloud_compatibility-guidelines) Copy linkLink copied to clipboard!

OpenShift Container Platform might choose to offer integration points with a hosting cloud environment via cloud provider specific integrations. The compatibility of these integration points are specific to the guarantee provided by the native cloud vendor and its intersection with the OpenShift Container Platform compatibility window. Where OpenShift Container Platform provides an integration with a cloud environment natively as part of the default installation, Red Hat develops against stable cloud API endpoints to provide commercially reasonable support with forward looking compatibility that includes stable deprecation policies. Example areas of integration between the cloud provider and OpenShift Container Platform include, but are not limited to, dynamic volume provisioning, service load balancer integration, pod workload identity, dynamic management of compute, and infrastructure provisioned as part of initial installation.

#### [2.3.5. Major, minor, and z-stream releases](#api-compatibility-common-terminology-releases_compatibility-guidelines) Copy linkLink copied to clipboard!

A Red Hat major release represents a significant step in the development of a product. Minor releases appear more frequently within the scope of a major release and represent deprecation boundaries that might impact future application compatibility. A z-stream release is an update to a minor release which provides a stream of continuous fixes to an associated minor release. API and AOE compatibility is never broken in a z-stream release except when this policy is explicitly overridden in order to respond to an unforeseen security impact.

For example, in the release 4.13.2:

* 4 is the major release version
* 13 is the minor release version
* 2 is the z-stream release version

#### [2.3.6. Extended user support (EUS)](#api-compatibility-common-terminology-eus_compatibility-guidelines) Copy linkLink copied to clipboard!

A minor release in an OpenShift Container Platform major release that has an extended support window for critical bug fixes. Users are able to migrate between EUS releases by incrementally adopting minor versions between EUS releases. It is important to note that the deprecation policy is defined across minor releases and not EUS releases. As a result, an EUS user might have to respond to a deprecation when migrating to a future EUS while sequentially upgrading through each minor release.

#### [2.3.7. Developer Preview](#api-compatibility-common-terminology-dev-preview_compatibility-guidelines) Copy linkLink copied to clipboard!

An optional product capability that is not officially supported by Red Hat, but is intended to provide a mechanism to explore early phase technology. By default, Developer Preview functionality is opt-in, and subject to removal at any time. Enabling a Developer Preview feature might render a cluster unsupportable dependent upon the scope of the feature.

If you are a Red( )Hat customer or partner and have feedback about these developer preview versions, file an issue by using the [OpenShift Bugs tracker](https://issues.redhat.com/projects/OCPBUGS/issues). Do not use the formal Red( )Hat support service ticket process. You can read more about support handling in the following [knowledge article](https://access.redhat.com/support/offerings/devpreview).

#### [2.3.8. Technology Preview](#api-compatibility-common-terminology-tech-preview_compatibility-guidelines) Copy linkLink copied to clipboard!

An optional product capability that provides early access to upcoming product innovations to test functionality and provide feedback during the development process. The feature is not fully supported, might not be functionally complete, and is not intended for production use. Usage of a Technology Preview function requires explicit opt-in. Learn more about the [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview).

## [Chapter 3. Editing kubelet log level verbosity and gathering logs](#editing-kubelet-log-level-verbosity) Copy linkLink copied to clipboard!

To troubleshoot some issues with nodes, establish the kubelet’s log level verbosity depending on the issue to be tracked.

### [3.1. Modifying the kubelet as a one-time scenario](#modifying-kubelet-one-time_editing-kubelet-log-level-verbosity) Copy linkLink copied to clipboard!

To modify the kubelet in a one-time scenario without rebooting the node due to the change of `machine-config(spec":{"paused":false}})`, allowing you to modify the kubelet without affecting the service, follow this procedure.

**Procedure**

1. Connect to the node in debug mode:

   ```
   $ oc debug node/<node>
   ```

   ```
   $ chroot /host
   ```

   Alternatively, it is possible to SSH to the node and become root.
2. After access is established, check the default log level:

   ```
   $ systemctl cat kubelet
   ```

   **Example output**

   ```
   # /etc/systemd/system/kubelet.service.d/20-logging.conf
   [Service]
   Environment="KUBELET_LOG_LEVEL=2"
   ```
3. Define the new verbosity required in a new `/etc/systemd/system/kubelet.service.d/30-logging.conf` file, which overrides `/etc/systemd/system/kubelet.service.d/20-logging.conf`. In this example, the verbosity is changed from `2` to `8`:

   ```
   $ echo -e "[Service]\nEnvironment=\"KUBELET_LOG_LEVEL=8\"" > /etc/systemd/system/kubelet.service.d/30-logging.conf
   ```
4. Reload systemd and restart the service:

   ```
   $ systemctl daemon-reload
   ```

   ```
   $ systemctl restart kubelet
   ```
5. Gather the logs, and then revert the log level increase:

   ```
   $ rm -f /etc/systemd/system/kubelet.service.d/30-logging.conf
   ```

   ```
   $ systemctl daemon-reload
   ```

   ```
   $ systemctl restart kubelet
   ```

### [3.2. Persistent kubelet log level configuration](#persistent-kubelet-log-level-configuration_editing-kubelet-log-level-verbosity) Copy linkLink copied to clipboard!

**Procedure**

* Use the following `MachineConfig` object for persistent kubelet log level configuration:

  ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfig
   metadata:
     labels:
       machineconfiguration.openshift.io/role: master
     name: 99-master-kubelet-loglevel
   spec:
     config:
       ignition:
         version: 3.2.0
       systemd:
         units:
           - name: kubelet.service
             enabled: true
             dropins:
               - name: 30-logging.conf
                 contents: |
                   [Service]
                   Environment="KUBELET_LOG_LEVEL=2"
  ```

  Generally, it is recommended to apply `0-4` as debug-level logs and `5-8` as trace-level logs.

### [3.3. Log verbosity descriptions](#log-verbosity-descriptions_editing-kubelet-log-level-verbosity) Copy linkLink copied to clipboard!

Expand

| Log verbosity | Description |
| --- | --- |
| `--v=0` | Always visible to an Operator. |
| `--v=1` | A reasonable default log level if you do not want verbosity. |
| `--v=2` | Useful steady state information about the service and important log messages that might correlate to significant changes in the system. This is the recommended default log level. |
| `--v=3` | Extended information about changes. |
| `--v=4` | Debug level verbosity. |
| `--v=6` | Display requested resources. |
| `--v=7` | Display HTTP request headers. |
| `--v=8` | Display HTTP request contents. |

Show more

### [3.4. Gathering kubelet logs](#gathering-kubelet-logs_editing-kubelet-log-level-verbosity) Copy linkLink copied to clipboard!

**Procedure**

* After the kubelet’s log level verbosity is configured properly, you can gather logs by running the following commands:

  ```
  $ oc adm node-logs --role master -u kubelet
  ```

  ```
  $ oc adm node-logs --role worker -u kubelet
  ```

  Alternatively, inside the node, run the following command:

  ```
  $ journalctl -b -f -u kubelet.service
  ```
* To collect master container logs, run the following command:

  ```
  $ sudo tail -f /var/log/containers/*
  ```
* To directly gather the logs of all nodes, run the following command:

  ```
  - for n in $(oc get node --no-headers | awk '{print $1}'); do oc adm node-logs $n | gzip > $n.log.gz; done
  ```

## [Chapter 4. API index](#api-index) Copy linkLink copied to clipboard!

Expand

| API | API group |
| --- | --- |
| [AdminNetworkPolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#adminnetworkpolicy-policy-networking-k8s-io-v1alpha1) | policy.networking.k8s.io/v1alpha1 |
| [AdminPolicyBasedExternalRoute](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#adminpolicybasedexternalroute-k8s-ovn-org-v1) | k8s.ovn.org/v1 |
| [AlertingRule](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#alertingrule-monitoring-openshift-io-v1) | monitoring.openshift.io/v1 |
| [Alertmanager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#alertmanager-monitoring-coreos-com-v1) | monitoring.coreos.com/v1 |
| [AlertmanagerConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#alertmanagerconfig-monitoring-coreos-com-v1beta1) | monitoring.coreos.com/v1beta1 |
| [AlertRelabelConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#alertrelabelconfig-monitoring-openshift-io-v1) | monitoring.openshift.io/v1 |
| [APIRequestCount](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#apirequestcount-apiserver-openshift-io-v1) | apiserver.openshift.io/v1 |
| [APIServer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#apiserver-config-openshift-io-v1) | config.openshift.io/v1 |
| [APIService](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#apiservice-apiregistration-k8s-io-v1) | apiregistration.k8s.io/v1 |
| [AppliedClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#appliedclusterresourcequota-quota-openshift-io-v1) | quota.openshift.io/v1 |
| [Authentication](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#authentication-config-openshift-io-v1) | config.openshift.io/v1 |
| [Authentication](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#authentication-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [BackendTLSPolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#backendtlspolicy-gateway-networking-k8s-io-v1) | gateway.networking.k8s.io/v1 |
| [BareMetalHost](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#baremetalhost-metal3-io-v1alpha1) | metal3.io/v1alpha1 |
| [BaselineAdminNetworkPolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1) | policy.networking.k8s.io/v1alpha1 |
| [Binding](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#binding-v1) | v1 |
| [BMCEventSubscription](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#bmceventsubscription-metal3-io-v1alpha1) | metal3.io/v1alpha1 |
| [BrokerTemplateInstance](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/template_apis/#brokertemplateinstance-template-openshift-io-v1) | template.openshift.io/v1 |
| [Build](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#build-build-openshift-io-v1) | build.openshift.io/v1 |
| [Build](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#build-config-openshift-io-v1) | config.openshift.io/v1 |
| [BuildConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#buildconfig-build-openshift-io-v1) | build.openshift.io/v1 |
| [BuildLog](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#buildlog-build-openshift-io-v1) | build.openshift.io/v1 |
| [BuildRequest](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#buildrequest-build-openshift-io-v1) | build.openshift.io/v1 |
| [CatalogSource](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#catalogsource-operators-coreos-com-v1alpha1) | operators.coreos.com/v1alpha1 |
| [CertificateSigningRequest](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#certificatesigningrequest-certificates-k8s-io-v1) | certificates.k8s.io/v1 |
| [CloudCredential](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#cloudcredential-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [CloudPrivateIPConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#cloudprivateipconfig-cloud-network-openshift-io-v1) | cloud.network.openshift.io/v1 |
| [ClusterAutoscaler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#clusterautoscaler-autoscaling-openshift-io-v1) | autoscaling.openshift.io/v1 |
| [ClusterCatalog](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#clustercatalog-olm-operatorframework-io-v1) | olm.operatorframework.io/v1 |
| [ClusterCSIDriver](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#clustercsidriver-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [ClusterExtension](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#clusterextension-olm-operatorframework-io-v1) | olm.operatorframework.io/v1 |
| [ClusterImagePolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#clusterimagepolicy-config-openshift-io-v1) | config.openshift.io/v1 |
| [ClusterOperator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#clusteroperator-config-openshift-io-v1) | config.openshift.io/v1 |
| [ClusterResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#clusterresourcequota-quota-openshift-io-v1) | quota.openshift.io/v1 |
| [ClusterRole](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/#clusterrole-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [ClusterRole](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/rbac_apis/#clusterrole-rbac-authorization-k8s-io-v1) | rbac.authorization.k8s.io/v1 |
| [ClusterRoleBinding](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/#clusterrolebinding-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [ClusterRoleBinding](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/rbac_apis/#clusterrolebinding-rbac-authorization-k8s-io-v1) | rbac.authorization.k8s.io/v1 |
| [ClusterServiceVersion](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#clusterserviceversion-operators-coreos-com-v1alpha1) | operators.coreos.com/v1alpha1 |
| [ClusterUserDefinedNetwork](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#clusteruserdefinednetwork-k8s-ovn-org-v1) | k8s.ovn.org/v1 |
| [ClusterVersion](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#clusterversion-config-openshift-io-v1) | config.openshift.io/v1 |
| [ComponentStatus](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#componentstatus-v1) | v1 |
| [Config](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#config-imageregistry-operator-openshift-io-v1) | imageregistry.operator.openshift.io/v1 |
| [Config](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#config-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [Config](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#config-samples-operator-openshift-io-v1) | samples.operator.openshift.io/v1 |
| [ConfigMap](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#configmap-v1) | v1 |
| [Console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#console-config-openshift-io-v1) | config.openshift.io/v1 |
| [Console](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#console-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [ConsoleCLIDownload](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consoleclidownload-console-openshift-io-v1) | console.openshift.io/v1 |
| [ConsoleExternalLogLink](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consoleexternalloglink-console-openshift-io-v1) | console.openshift.io/v1 |
| [ConsoleLink](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consolelink-console-openshift-io-v1) | console.openshift.io/v1 |
| [ConsoleNotification](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consolenotification-console-openshift-io-v1) | console.openshift.io/v1 |
| [ConsolePlugin](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consoleplugin-console-openshift-io-v1) | console.openshift.io/v1 |
| [ConsoleQuickStart](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consolequickstart-console-openshift-io-v1) | console.openshift.io/v1 |
| [ConsoleSample](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consolesample-console-openshift-io-v1) | console.openshift.io/v1 |
| [ConsoleYAMLSample](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/console_apis/#consoleyamlsample-console-openshift-io-v1) | console.openshift.io/v1 |
| [ContainerRuntimeConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#containerruntimeconfig-machineconfiguration-openshift-io-v1) | machineconfiguration.openshift.io/v1 |
| [ControllerConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#controllerconfig-machineconfiguration-openshift-io-v1) | machineconfiguration.openshift.io/v1 |
| [ControllerRevision](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#controllerrevision-apps-v1) | apps/v1 |
| [ControlPlaneMachineSet](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#controlplanemachineset-machine-openshift-io-v1) | machine.openshift.io/v1 |
| [CredentialsRequest](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#credentialsrequest-cloudcredential-openshift-io-v1) | cloudcredential.openshift.io/v1 |
| [CronJob](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#cronjob-batch-v1) | batch/v1 |
| [CSIDriver](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#csidriver-storage-k8s-io-v1) | storage.k8s.io/v1 |
| [CSINode](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#csinode-storage-k8s-io-v1) | storage.k8s.io/v1 |
| [CSISnapshotController](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#csisnapshotcontroller-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [CSIStorageCapacity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#csistoragecapacity-storage-k8s-io-v1) | storage.k8s.io/v1 |
| [CustomResourceDefinition](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#customresourcedefinition-apiextensions-k8s-io-v1) | apiextensions.k8s.io/v1 |
| [DaemonSet](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#daemonset-apps-v1) | apps/v1 |
| [DataGather](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#datagather-insights-openshift-io-v1) | insights.openshift.io/v1 |
| [DataImage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#dataimage-metal3-io-v1alpha1) | metal3.io/v1alpha1 |
| [Deployment](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#deployment-apps-v1) | apps/v1 |
| [DeploymentConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#deploymentconfig-apps-openshift-io-v1) | apps.openshift.io/v1 |
| [DeploymentConfigRollback](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#deploymentconfigrollback-apps-openshift-io-v1) | apps.openshift.io/v1 |
| [DeploymentLog](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#deploymentlog-apps-openshift-io-v1) | apps.openshift.io/v1 |
| [DeploymentRequest](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#deploymentrequest-apps-openshift-io-v1) | apps.openshift.io/v1 |
| [DeviceClass](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#deviceclass-resource-k8s-io-v1) | resource.k8s.io/v1 |
| [DNS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#dns-config-openshift-io-v1) | config.openshift.io/v1 |
| [DNS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#dns-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [DNSRecord](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#dnsrecord-ingress-operator-openshift-io-v1) | ingress.operator.openshift.io/v1 |
| [EgressFirewall](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#egressfirewall-k8s-ovn-org-v1) | k8s.ovn.org/v1 |
| [EgressIP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#egressip-k8s-ovn-org-v1) | k8s.ovn.org/v1 |
| [EgressQoS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#egressqos-k8s-ovn-org-v1) | k8s.ovn.org/v1 |
| [EgressRouter](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#egressrouter-network-operator-openshift-io-v1) | network.operator.openshift.io/v1 |
| [EgressService](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#egressservice-k8s-ovn-org-v1) | k8s.ovn.org/v1 |
| [Endpoints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#endpoints-v1) | v1 |
| [EndpointSlice](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#endpointslice-discovery-k8s-io-v1) | discovery.k8s.io/v1 |
| [Etcd](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#etcd-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [Event](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#event-v1) | v1 |
| [Event](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#event-events-k8s-io-v1) | events.k8s.io/v1 |
| [Eviction](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/policy_apis/#eviction-policy-v1) | policy/v1 |
| [FeatureGate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#featuregate-config-openshift-io-v1) | config.openshift.io/v1 |
| [FirmwareSchema](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#firmwareschema-metal3-io-v1alpha1) | metal3.io/v1alpha1 |
| [FlowSchema](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#flowschema-flowcontrol-apiserver-k8s-io-v1) | flowcontrol.apiserver.k8s.io/v1 |
| [Gateway](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#gateway-gateway-networking-k8s-io-v1) | gateway.networking.k8s.io/v1 |
| [GatewayClass](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#gatewayclass-gateway-networking-k8s-io-v1) | gateway.networking.k8s.io/v1 |
| [Group](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/user_and_group_apis/#group-user-openshift-io-v1) | user.openshift.io/v1 |
| [GRPCRoute](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#grpcroute-gateway-networking-k8s-io-v1) | gateway.networking.k8s.io/v1 |
| [HardwareData](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#hardwaredata-metal3-io-v1alpha1) | metal3.io/v1alpha1 |
| [HelmChartRepository](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#helmchartrepository-helm-openshift-io-v1beta1) | helm.openshift.io/v1beta1 |
| [HorizontalPodAutoscaler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#horizontalpodautoscaler-autoscaling-v2) | autoscaling/v2 |
| [HostFirmwareComponents](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#hostfirmwarecomponents-metal3-io-v1alpha1) | metal3.io/v1alpha1 |
| [HostFirmwareSettings](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#hostfirmwaresettings-metal3-io-v1alpha1) | metal3.io/v1alpha1 |
| [HostUpdatePolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#hostupdatepolicy-metal3-io-v1alpha1) | metal3.io/v1alpha1 |
| [HTTPRoute](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#httproute-gateway-networking-k8s-io-v1) | gateway.networking.k8s.io/v1 |
| [Identity](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/user_and_group_apis/#identity-user-openshift-io-v1) | user.openshift.io/v1 |
| [Image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#image-config-openshift-io-v1) | config.openshift.io/v1 |
| [Image](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#image-image-openshift-io-v1) | image.openshift.io/v1 |
| [ImageContentPolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#imagecontentpolicy-config-openshift-io-v1) | config.openshift.io/v1 |
| [ImageContentSourcePolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) | operator.openshift.io/v1alpha1 |
| [ImageDigestMirrorSet](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#imagedigestmirrorset-config-openshift-io-v1) | config.openshift.io/v1 |
| [ImagePolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#imagepolicy-config-openshift-io-v1) | config.openshift.io/v1 |
| [ImagePruner](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#imagepruner-imageregistry-operator-openshift-io-v1) | imageregistry.operator.openshift.io/v1 |
| [ImageSignature](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagesignature-image-openshift-io-v1) | image.openshift.io/v1 |
| [ImageStream](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagestream-image-openshift-io-v1) | image.openshift.io/v1 |
| [ImageStreamImage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagestreamimage-image-openshift-io-v1) | image.openshift.io/v1 |
| [ImageStreamImport](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagestreamimport-image-openshift-io-v1) | image.openshift.io/v1 |
| [ImageStreamLayers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagestreamlayers-image-openshift-io-v1) | image.openshift.io/v1 |
| [ImageStreamMapping](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagestreammapping-image-openshift-io-v1) | image.openshift.io/v1 |
| [ImageStreamTag](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagestreamtag-image-openshift-io-v1) | image.openshift.io/v1 |
| [ImageTag](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#imagetag-image-openshift-io-v1) | image.openshift.io/v1 |
| [ImageTagMirrorSet](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#imagetagmirrorset-config-openshift-io-v1) | config.openshift.io/v1 |
| [Infrastructure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#infrastructure-config-openshift-io-v1) | config.openshift.io/v1 |
| [Ingress](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#ingress-config-openshift-io-v1) | config.openshift.io/v1 |
| [Ingress](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ingress-networking-k8s-io-v1) | networking.k8s.io/v1 |
| [IngressClass](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ingressclass-networking-k8s-io-v1) | networking.k8s.io/v1 |
| [IngressController](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#ingresscontroller-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [InsightsDataGather](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#insightsdatagather-config-openshift-io-v1) | config.openshift.io/v1 |
| [InsightsOperator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#insightsoperator-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [InstallPlan](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#installplan-operators-coreos-com-v1alpha1) | operators.coreos.com/v1alpha1 |
| [IPAddress](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ipaddress-networking-k8s-io-v1) | networking.k8s.io/v1 |
| [IPAddressClaim](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ipaddressclaim-ipam-cluster-x-k8s-io-v1beta1) | ipam.cluster.x-k8s.io/v1beta1 |
| [IPAMClaim](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ipamclaim-k8s-cni-cncf-io-v1alpha1) | k8s.cni.cncf.io/v1alpha1 |
| [IPPool](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#ippool-whereabouts-cni-cncf-io-v1alpha1) | whereabouts.cni.cncf.io/v1alpha1 |
| [Job](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#job-batch-v1) | batch/v1 |
| [KubeAPIServer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#kubeapiserver-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [KubeControllerManager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#kubecontrollermanager-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [KubeletConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#kubeletconfig-machineconfiguration-openshift-io-v1) | machineconfiguration.openshift.io/v1 |
| [KubeScheduler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#kubescheduler-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [KubeStorageVersionMigrator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#kubestorageversionmigrator-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [Lease](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#lease-coordination-k8s-io-v1) | coordination.k8s.io/v1 |
| [LimitRange](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#limitrange-v1) | v1 |
| [LocalResourceAccessReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#localresourceaccessreview-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [LocalSubjectAccessReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#localsubjectaccessreview-authorization-k8s-io-v1) | authorization.k8s.io/v1 |
| [LocalSubjectAccessReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#localsubjectaccessreview-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [Machine](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machine-machine-openshift-io-v1beta1) | machine.openshift.io/v1beta1 |
| [MachineAutoscaler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#machineautoscaler-autoscaling-openshift-io-v1beta1) | autoscaling.openshift.io/v1beta1 |
| [MachineConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineconfig-machineconfiguration-openshift-io-v1) | machineconfiguration.openshift.io/v1 |
| [MachineConfigNode](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineconfignode-machineconfiguration-openshift-io-v1) | machineconfiguration.openshift.io/v1 |
| [MachineConfigPool](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineconfigpool-machineconfiguration-openshift-io-v1) | machineconfiguration.openshift.io/v1 |
| [MachineConfiguration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#machineconfiguration-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [MachineHealthCheck](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machinehealthcheck-machine-openshift-io-v1beta1) | machine.openshift.io/v1beta1 |
| [MachineOSBuild](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineosbuild-machineconfiguration-openshift-io-v1) | machineconfiguration.openshift.io/v1 |
| [MachineOSConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineosconfig-machineconfiguration-openshift-io-v1) | machineconfiguration.openshift.io/v1 |
| [MachineSet](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#machineset-machine-openshift-io-v1beta1) | machine.openshift.io/v1beta1 |
| [Metal3Remediation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) | infrastructure.cluster.x-k8s.io/v1beta1 |
| [Metal3RemediationTemplate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1) | infrastructure.cluster.x-k8s.io/v1beta1 |
| [MultiNetworkPolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#multinetworkpolicy-k8s-cni-cncf-io-v1beta1) | k8s.cni.cncf.io/v1beta1 |
| [MutatingWebhookConfiguration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#mutatingwebhookconfiguration-admissionregistration-k8s-io-v1) | admissionregistration.k8s.io/v1 |
| [Namespace](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/metadata_apis/#namespace-v1) | v1 |
| [Network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#network-config-openshift-io-v1) | config.openshift.io/v1 |
| [Network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#network-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [NetworkAttachmentDefinition](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#networkattachmentdefinition-k8s-cni-cncf-io-v1) | k8s.cni.cncf.io/v1 |
| [NetworkPolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#networkpolicy-networking-k8s-io-v1) | networking.k8s.io/v1 |
| [Node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#node-v1) | v1 |
| [Node](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#node-config-openshift-io-v1) | config.openshift.io/v1 |
| [NodeMetrics](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#nodemetrics-metrics-k8s-io-v1beta1) | metrics.k8s.io/v1beta1 |
| [NodeSlicePool](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) | whereabouts.cni.cncf.io/v1alpha1 |
| [OAuth](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#oauth-config-openshift-io-v1) | config.openshift.io/v1 |
| [OAuthAccessToken](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/#oauthaccesstoken-oauth-openshift-io-v1) | oauth.openshift.io/v1 |
| [OAuthAuthorizeToken](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/#oauthauthorizetoken-oauth-openshift-io-v1) | oauth.openshift.io/v1 |
| [OAuthClient](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/#oauthclient-oauth-openshift-io-v1) | oauth.openshift.io/v1 |
| [OAuthClientAuthorization](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/#oauthclientauthorization-oauth-openshift-io-v1) | oauth.openshift.io/v1 |
| [OLM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#olm-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [OLMConfig](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#olmconfig-operators-coreos-com-v1) | operators.coreos.com/v1 |
| [OpenShiftAPIServer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#openshiftapiserver-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [OpenShiftControllerManager](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#openshiftcontrollermanager-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#operator-operators-coreos-com-v1) | operators.coreos.com/v1 |
| [OperatorCondition](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#operatorcondition-operators-coreos-com-v2) | operators.coreos.com/v2 |
| [OperatorGroup](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#operatorgroup-operators-coreos-com-v1) | operators.coreos.com/v1 |
| [OperatorHub](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#operatorhub-config-openshift-io-v1) | config.openshift.io/v1 |
| [OperatorPKI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#operatorpki-network-operator-openshift-io-v1) | network.operator.openshift.io/v1 |
| [OverlappingRangeIPReservation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) | whereabouts.cni.cncf.io/v1alpha1 |
| [PackageManifest](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#packagemanifest-packages-operators-coreos-com-v1) | packages.operators.coreos.com/v1 |
| [PerformanceProfile](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#performanceprofile-performance-openshift-io-v2) | performance.openshift.io/v2 |
| [PersistentVolume](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#persistentvolume-v1) | v1 |
| [PersistentVolumeClaim](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#persistentvolumeclaim-v1) | v1 |
| [PinnedImageSet](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_apis/#pinnedimageset-machineconfiguration-openshift-io-v1) | machineconfiguration.openshift.io/v1 |
| [Pod](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#pod-v1) | v1 |
| [PodDisruptionBudget](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/policy_apis/#poddisruptionbudget-policy-v1) | policy/v1 |
| [PodMetrics](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#podmetrics-metrics-k8s-io-v1beta1) | metrics.k8s.io/v1beta1 |
| [PodMonitor](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#podmonitor-monitoring-coreos-com-v1) | monitoring.coreos.com/v1 |
| [PodNetworkConnectivityCheck](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1) | controlplane.operator.openshift.io/v1alpha1 |
| [PodSecurityPolicyReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#podsecuritypolicyreview-security-openshift-io-v1) | security.openshift.io/v1 |
| [PodSecurityPolicySelfSubjectReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#podsecuritypolicyselfsubjectreview-security-openshift-io-v1) | security.openshift.io/v1 |
| [PodSecurityPolicySubjectReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#podsecuritypolicysubjectreview-security-openshift-io-v1) | security.openshift.io/v1 |
| [PodTemplate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/template_apis/#podtemplate-v1) | v1 |
| [PreprovisioningImage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#preprovisioningimage-metal3-io-v1alpha1) | metal3.io/v1alpha1 |
| [PriorityClass](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#priorityclass-scheduling-k8s-io-v1) | scheduling.k8s.io/v1 |
| [PriorityLevelConfiguration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1) | flowcontrol.apiserver.k8s.io/v1 |
| [Probe](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#probe-monitoring-coreos-com-v1) | monitoring.coreos.com/v1 |
| [Profile](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#profile-tuned-openshift-io-v1) | tuned.openshift.io/v1 |
| [Project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#project-config-openshift-io-v1) | config.openshift.io/v1 |
| [Project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/project_apis/#project-project-openshift-io-v1) | project.openshift.io/v1 |
| [ProjectHelmChartRepository](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#projecthelmchartrepository-helm-openshift-io-v1beta1) | helm.openshift.io/v1beta1 |
| [ProjectRequest](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/project_apis/#projectrequest-project-openshift-io-v1) | project.openshift.io/v1 |
| [Prometheus](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#prometheus-monitoring-coreos-com-v1) | monitoring.coreos.com/v1 |
| [PrometheusRule](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#prometheusrule-monitoring-coreos-com-v1) | monitoring.coreos.com/v1 |
| [Provisioning](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/provisioning_apis/#provisioning-metal3-io-v1alpha1) | metal3.io/v1alpha1 |
| [Proxy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#proxy-config-openshift-io-v1) | config.openshift.io/v1 |
| [RangeAllocation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#rangeallocation-security-openshift-io-v1) | security.openshift.io/v1 |
| [ReferenceGrant](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#referencegrant-gateway-networking-k8s-io-v1beta1) | gateway.networking.k8s.io/v1beta1 |
| [ReplicaSet](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#replicaset-apps-v1) | apps/v1 |
| [ReplicationController](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#replicationcontroller-v1) | v1 |
| [ResourceAccessReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#resourceaccessreview-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [ResourceClaim](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#resourceclaim-resource-k8s-io-v1) | resource.k8s.io/v1 |
| [ResourceClaimTemplate](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#resourceclaimtemplate-resource-k8s-io-v1) | resource.k8s.io/v1 |
| [ResourceQuota](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#resourcequota-v1) | v1 |
| [ResourceSlice](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/schedule_and_quota_apis/#resourceslice-resource-k8s-io-v1) | resource.k8s.io/v1 |
| [Role](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/#role-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [Role](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/rbac_apis/#role-rbac-authorization-k8s-io-v1) | rbac.authorization.k8s.io/v1 |
| [RoleBinding](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/#rolebinding-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [RoleBinding](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/rbac_apis/#rolebinding-rbac-authorization-k8s-io-v1) | rbac.authorization.k8s.io/v1 |
| [RoleBindingRestriction](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/role_apis/#rolebindingrestriction-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [Route](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#route-route-openshift-io-v1) | route.openshift.io/v1 |
| [RuntimeClass](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#runtimeclass-node-k8s-io-v1) | node.k8s.io/v1 |
| [Scale](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/autoscale_apis/#scale-autoscaling-v1) | autoscaling/v1 |
| [Scheduler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/config_apis/#scheduler-config-openshift-io-v1) | config.openshift.io/v1 |
| [Secret](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#secret-v1) | v1 |
| [SecretList](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/image_apis/#secretlist-image-openshift-io-v1) | image.openshift.io/v1 |
| [SecurityContextConstraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#securitycontextconstraints-security-openshift-io-v1) | security.openshift.io/v1 |
| [SelfSubjectAccessReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#selfsubjectaccessreview-authorization-k8s-io-v1) | authorization.k8s.io/v1 |
| [SelfSubjectReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#selfsubjectreview-authentication-k8s-io-v1) | authentication.k8s.io/v1 |
| [SelfSubjectRulesReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#selfsubjectrulesreview-authorization-k8s-io-v1) | authorization.k8s.io/v1 |
| [SelfSubjectRulesReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#selfsubjectrulesreview-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [Service](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#service-v1) | v1 |
| [ServiceAccount](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_apis/#serviceaccount-v1) | v1 |
| [ServiceCA](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#serviceca-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [ServiceCIDR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#servicecidr-networking-k8s-io-v1) | networking.k8s.io/v1 |
| [ServiceMonitor](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#servicemonitor-monitoring-coreos-com-v1) | monitoring.coreos.com/v1 |
| [StatefulSet](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/workloads_apis/#statefulset-apps-v1) | apps/v1 |
| [Storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operator_apis/#storage-operator-openshift-io-v1) | operator.openshift.io/v1 |
| [StorageClass](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#storageclass-storage-k8s-io-v1) | storage.k8s.io/v1 |
| [StorageState](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#storagestate-migration-k8s-io-v1alpha1) | migration.k8s.io/v1alpha1 |
| [StorageVersionMigration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#storageversionmigration-migration-k8s-io-v1alpha1) | migration.k8s.io/v1alpha1 |
| [SubjectAccessReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#subjectaccessreview-authorization-k8s-io-v1) | authorization.k8s.io/v1 |
| [SubjectAccessReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#subjectaccessreview-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [SubjectRulesReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#subjectrulesreview-authorization-openshift-io-v1) | authorization.openshift.io/v1 |
| [Subscription](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operatorhub_apis/#subscription-operators-coreos-com-v1alpha1) | operators.coreos.com/v1alpha1 |
| [Template](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/template_apis/#template-template-openshift-io-v1) | template.openshift.io/v1 |
| [TemplateInstance](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/template_apis/#templateinstance-template-openshift-io-v1) | template.openshift.io/v1 |
| [TestExtensionAdmission](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#testextensionadmission-testextension-redhat-io-v1) | testextension.redhat.io/v1 |
| [ThanosRuler](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring_apis/#thanosruler-monitoring-coreos-com-v1) | monitoring.coreos.com/v1 |
| [TokenRequest](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#tokenrequest-authentication-k8s-io-v1) | authentication.k8s.io/v1 |
| [TokenReview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authorization_apis/#tokenreview-authentication-k8s-io-v1) | authentication.k8s.io/v1 |
| [Tuned](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/node_apis/#tuned-tuned-openshift-io-v1) | tuned.openshift.io/v1 |
| [User](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/user_and_group_apis/#user-user-openshift-io-v1) | user.openshift.io/v1 |
| [UserDefinedNetwork](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_apis/#userdefinednetwork-k8s-ovn-org-v1) | k8s.ovn.org/v1 |
| [UserIdentityMapping](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/user_and_group_apis/#useridentitymapping-user-openshift-io-v1) | user.openshift.io/v1 |
| [UserOAuthAccessToken](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/oauth_apis/#useroauthaccesstoken-oauth-openshift-io-v1) | oauth.openshift.io/v1 |
| [ValidatingAdmissionPolicy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#validatingadmissionpolicy-admissionregistration-k8s-io-v1) | admissionregistration.k8s.io/v1 |
| [ValidatingAdmissionPolicyBinding](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) | admissionregistration.k8s.io/v1 |
| [ValidatingWebhookConfiguration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/extension_apis/#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) | admissionregistration.k8s.io/v1 |
| [VolumeAttachment](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumeattachment-storage-k8s-io-v1) | storage.k8s.io/v1 |
| [VolumeAttributesClass](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumeattributesclass-storage-k8s-io-v1) | storage.k8s.io/v1 |
| [VolumePopulator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumepopulator-populator-storage-k8s-io-v1beta1) | populator.storage.k8s.io/v1beta1 |
| [VolumeSnapshot](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumesnapshot-snapshot-storage-k8s-io-v1) | snapshot.storage.k8s.io/v1 |
| [VolumeSnapshotClass](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumesnapshotclass-snapshot-storage-k8s-io-v1) | snapshot.storage.k8s.io/v1 |
| [VolumeSnapshotContent](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage_apis/#volumesnapshotcontent-snapshot-storage-k8s-io-v1) | snapshot.storage.k8s.io/v1 |

Show more

## [Legal Notice](#idm139711186143376) Copy linkLink copied to clipboard!

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
