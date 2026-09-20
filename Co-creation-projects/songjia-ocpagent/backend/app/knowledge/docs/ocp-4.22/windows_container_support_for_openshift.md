---
title: "Windows Container Support for OpenShift"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/windows_container_support_for_openshift/index
retrieved_at: 2026-09-05T05:43:05.364098+00:00
---

# Windows Container Support for OpenShift

---

OpenShift Container Platform 4.22

## Red Hat OpenShift for Windows Containers Guide

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140458186682752)

**Abstract**

Red Hat OpenShift for Windows Containers provides built-in support for running Microsoft Windows Server containers on OpenShift Container Platform. This guide provides all the details.

---

## [Chapter 1. Red Hat OpenShift support for Windows Containers overview](#windows-container-overview) Copy linkLink copied to clipboard!

You can use Red Hat OpenShift support for Windows Containers to run Windows compute nodes in an OpenShift Container Platform cluster by using the Red Hat Windows Machine Config Operator (WMCO) to install and manage Windows nodes.

### [1.1. Managing Windows container workloads](#managing-windows-container-workloads_windows-container-overview) Copy linkLink copied to clipboard!

With a Red Hat subscription, you can get support for running Windows workloads in OpenShift Container Platform.

Windows instances deployed by the WMCO are configured with the containerd container runtime. For more information, see the [release notes](#windows-containers-release-notes "2.1. Red Hat OpenShift support for Windows Containers release notes").

You can add Windows nodes either by creating a [compute machine set](#creating-windows-machineset-aws "6.1. Creating a Windows machine set on AWS") or by specifying existing Bring-Your-Own-Host (BYOH) Windows instances through a [ConfigMap](#byoh-windows-instance "Chapter 9. Using Bring-Your-Own-Host (BYOH) Windows instances as nodes").

Note

Compute machine sets are not supported for bare metal or provider agnostic clusters.

For workloads including both Linux and Windows, OpenShift Container Platform allows you to deploy Windows workloads running on Windows Server containers while also providing traditional Linux workloads hosted on Red Hat Enterprise Linux CoreOS (RHCOS) or Red Hat Enterprise Linux (RHEL). For more information, see [getting started with Windows container workloads](#understanding-windows-container-workloads "Chapter 4. Understanding Windows container workloads").

You need the WMCO to run Windows workloads in your cluster. The WMCO orchestrates the process of deploying and managing Windows workloads on a cluster. For more information, see [how to enable Windows container workloads](#enabling-windows-container-workloads "Chapter 5. Enabling Windows container workloads").

You can create a Windows `MachineSet` object to create infrastructure Windows machine sets and related machines so that you can move supported Windows workloads to the new Windows machines. You can create a Windows `MachineSet` object on multiple platforms.

You can [schedule Windows workloads](#scheduling-windows-workloads "Chapter 7. Scheduling Windows container workloads") to Windows compute nodes.

You can [perform Windows Machine Config Operator upgrades](#windows-node-upgrades "Chapter 8. Windows node updates") to ensure that your Windows nodes have the latest updates.

You can [remove a Windows node](#removing-windows-nodes "Chapter 10. Removing Windows nodes") by deleting a specific machine.

You can [use Bring-Your-Own-Host (BYOH) Windows instances](#byoh-windows-instance "Chapter 9. Using Bring-Your-Own-Host (BYOH) Windows instances as nodes") to repurpose Windows Server VMs and bring them to OpenShift Container Platform. BYOH Windows instances benefit users who are looking to mitigate major disruptions when a Windows server goes offline. You can use BYOH Windows instances as nodes on OpenShift Container Platform 4.8 and later versions.

You can [disable Windows container workloads](#disabling-windows-container-workloads "Chapter 11. Disabling Windows container workloads") by performing the following:

* Uninstalling the Windows Machine Config Operator
* Deleting the Windows Machine Config Operator namespace

## [Chapter 2. Release notes](#release-notes) Copy linkLink copied to clipboard!

### [2.1. Red Hat OpenShift support for Windows Containers release notes](#windows-containers-release-notes) Copy linkLink copied to clipboard!

You can review the release notes to learn about the changes introduced through each release of the Red Hat OpenShift support for Windows Containers and the Windows Machine Config Operator (WMCO).

#### [2.1.1. Release notes for Red Hat Windows Machine Config Operator 10.22.1](#windows-containers-release-notes-10-22-1_windows-containers-release-notes) Copy linkLink copied to clipboard!

Issued: 28 July 2026

You can review the release notes to learn about the bug fixes and Common Vulnerabilities and Exposures (CVEs) fixes in the Windows Machine Config Operator (WMCO) version 10.22.1.

The components of the WMCO version 10.22.1 were released in [RHSA-2026:47173](https://access.redhat.com/errata/RHSA-2026:47173).

##### [2.1.1.1. Bug fixes](#windows-containers-release-notes-10-22-1-bugs_windows-containers-release-notes) Copy linkLink copied to clipboard!

* Before this update, the SSH connection between the WMCO and a Windows node would terminate when the WMCO rebooted the node after a configuration update. As a consequence, the WMCO incorrectly treated the SSH disconnection as a reboot failure, preventing the Windows node from completing required reboots. With this release, the reboot validation process is modified to ignore SSH termination errors and instead verify a successful reboot by using explicit node reachability checks and the SSH reconnection. As a result, Windows nodes successfully reboot upon node configuration changes. ([OCPBUGS-98228](https://issues.redhat.com/browse/OCPBUGS-98228))

##### [2.1.1.2. CVE fixes](#cve-fixes) Copy linkLink copied to clipboard!

* [CVE-2026-54099](https://access.redhat.com/security/cve/cve-2026-54099)
* [CVE-2026-54100](https://access.redhat.com/security/cve/cve-2026-54100)

### [2.2. Release notes for past releases of the Windows Machine Config Operator](#windows-containers-release-notes-past) Copy linkLink copied to clipboard!

You can review the release notes to learn about changes in previous versions of the Windows Machine Config Operator (WMCO).

For the current Red Hat OpenShift support for Windows Containers release notes, see "Red Hat OpenShift support for Windows Containers release notes".

#### [2.2.1. Release notes for Red Hat Windows Machine Config Operator 10.22.0](#windows-containers-release-notes-10-22-0_windows-containers-release-notes-past) Copy linkLink copied to clipboard!

Issued: 20 May 2026

You can review the following release notes to learn about the new features and bug fixes in the Windows Machine Config Operator (WMCO) version 10.22.0.

The components of the WMCO version 10.22.0 were released in [RHBA-2026:19710](https://access.redhat.com/errata/RHBA-2026:19710).

##### [2.2.1.1. New features and improvements](#wmco-10-22-0-new-features_windows-containers-release-notes-past) Copy linkLink copied to clipboard!

Windows Server 2025 support
:   The WMCO now supports Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later for all supported platforms.

Kubernetes upgrade
:   The WMCO now uses Kubernetes version 1.35.

##### [2.2.1.2. Bug fixes](#wmco-10-22-0-bug-fixes_windows-containers-release-notes-past) Copy linkLink copied to clipboard!

* Before this update, if you enabled the `ClusterAPIMachineManagement` feature gate by enabling the `TechPreviewNoUpgrade` feature set, OpenShift Container Platform provisioned the `openshift-cluster-api` namespace. However, the WMCO was not adding the `windows-user-data` secret to that namespace, which is required by Cluster API compute machine sets. Because of the missing secret, CAPI-provisioned Windows machines would not bootstrap, remaining stuck in the `Pending` phase, and never joining the cluster. With this release, the OpenShift Container Platform now detects whether the `openshift-cluster-api` namespace exists and mirrors the `windows-user-data` secret into that namespace. CAPI-provisioned Windows machines successfully receive the bootstrap secret, are no longer getting stuck in `Pending` state, and join the cluster as expected. ([OCPBUGS-38401](https://issues.redhat.com/browse/OCPBUGS-38401))

### [2.3. Windows Machine Config Operator prerequisites](#windows-containers-release-notes-prereqs) Copy linkLink copied to clipboard!

You can review the following information for details on the supported platform versions, Windows Server versions, and networking configurations for the Windows Machine Config Operator (WMCO). See the vSphere documentation for any information that is relevant to only that platform.

#### [2.3.1. WMCO supported installation method](#wmco-prerequisites-supported-install_windows-containers-release-notes-prereqs) Copy linkLink copied to clipboard!

The WMCO fully supports installing Windows nodes into installer-provisioned infrastructure (IPI) clusters. This is the preferred OpenShift Container Platform installation method.

For user-provisioned infrastructure (UPI) clusters, the WMCO supports installing Windows nodes only into a UPI cluster installed with the `platform: none` field set in the `install-config.yaml` file (bare-metal or provider-agnostic) and only for the [BYOH (Bring Your Own Host)](#byoh-windows-instance "Chapter 9. Using Bring-Your-Own-Host (BYOH) Windows instances as nodes") use case. UPI is not supported for any other platform.

#### [2.3.2. WMCO supported platforms and Windows Server versions](#wmco-prerequisites-supported_windows-containers-release-notes-prereqs) Copy linkLink copied to clipboard!

The following table lists the [Windows Server versions](https://docs.microsoft.com/en-us/windows/release-health/windows-server-release-info) that are supported by WMCO 10.20.0, based on the applicable platform. Windows Server versions not listed are not supported and attempting to use them will cause errors. To prevent these errors, use only an appropriate version for your platform.

Expand

| Platform | Supported Windows Server version |
| --- | --- |
| Amazon Web Services (AWS) | * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later [1] * Windows Server 2019, version 1809 |
| Microsoft Azure | * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later * Windows Server 2019, version 1809 |
| VMware vSphere | * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later |
| Google Cloud | * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later |
| Nutanix | * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later |
| Bare metal or provider agnostic | * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later |

Show more

1. For disconnected clusters, the Windows AMI must have the EC2LaunchV2 agent version 2.0.2107 or later installed. For more information, see "Install the latest version of EC2Launch v2 (AWS documentation)".

#### [2.3.3. Supported networking](#supported-networking) Copy linkLink copied to clipboard!

Hybrid networking with OVN-Kubernetes is the only supported networking configuration. See the additional resources below for more information on this functionality. The following tables outline the type of networking configuration and Windows Server versions to use based on your platform. You must specify the network configuration when you install the cluster.

Note

* The WMCO does not support OVN-Kubernetes without hybrid networking or OpenShift SDN.
* Dual NIC is not supported on WMCO-managed Windows instances.

Expand

Table 2.1. Platform networking support

| Platform | Supported networking |
| --- | --- |
| Amazon Web Services (AWS) | Hybrid networking with OVN-Kubernetes |
| Microsoft Azure | Hybrid networking with OVN-Kubernetes |
| VMware vSphere | Hybrid networking with OVN-Kubernetes with a custom VXLAN port |
| Google Cloud | Hybrid networking with OVN-Kubernetes |
| Nutanix | Hybrid networking with OVN-Kubernetes |
| Bare metal or provider agnostic | Hybrid networking with OVN-Kubernetes |

Show more

Expand

Table 2.2. Hybrid OVN-Kubernetes Windows Server support

| Hybrid networking with OVN-Kubernetes | Supported Windows Server version |
| --- | --- |
| Default VXLAN port | * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later * Windows Server 2019, version 1809 |
| Custom VXLAN port | * Windows Server 2025, OS Build [10.0.26100](https://support.microsoft.com/en-us/topic/may-12-2026-kb5087539-os-build-26100-32860-fe3fd635-23fc-41bd-b7a7-00e57c1c4f91) or later * Windows Server 2022, OS Build [20348.681](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d) or later |

Show more

### [2.4. Windows Machine Config Operator known limitations](#windows-containers-release-notes-limitations) Copy linkLink copied to clipboard!

Note the following limitations when working with Windows nodes managed by the WMCO (Windows nodes):

* The following OpenShift Container Platform features are not supported on Windows nodes:

  + Image builds
  + OpenShift Pipelines
  + OpenShift Service Mesh
  + OpenShift monitoring of user-defined projects
  + OpenShift Serverless
  + Vertical Pod Autoscaling
  + Hosted Control Planes
* The following Red Hat features are not supported on Windows nodes:

  + [Red Hat Lightspeed cost management](https://docs.redhat.com/en/documentation/cost_management_service/1-latest)
  + [Red Hat OpenShift Local](https://developers.redhat.com/products/openshift-local/overview)
* Dual NIC is not supported on WMCO-managed Windows instances.
* Windows nodes do not support workloads created by using deployment configs. You can use a deployment or other method to deploy workloads.
* Red Hat OpenShift support for Windows Containers does not support adding Windows nodes to a cluster through a trunk port. The only supported networking configuration for adding Windows nodes is through an access port that carries traffic for the VLAN.
* Red Hat OpenShift support for Windows Containers does not support any Windows operating system language other than English (United States).
* Due to a limitation within the Windows operating system, `clusterNetwork` CIDR addresses of class E, such as `240.0.0.0`, are not compatible with Windows nodes.
* Kubernetes has identified the following node feature limitations. For more information, see "Compatibility and limitations (Kubernetes documenation)".

  + Huge pages are not supported for Windows containers.
  + Privileged containers are not supported for Windows containers.
* Kubernetes has identified several API compatibility issues. For more information, see "API compatibility (Kubernetes documenation)".

## [Chapter 3. Getting support](#windows-containers-support) Copy linkLink copied to clipboard!

Windows Container Support for Red Hat OpenShift is provided and available as an optional, installable component. Windows Container Support for Red Hat OpenShift is not part of the OpenShift Container Platform subscription. It requires an additional Red Hat subscription and is supported according to the [Scope of coverage](https://access.redhat.com/support/offerings/production/soc/) and [Service level agreements](https://access.redhat.com/support/offerings/production/sla).

You must have this separate subscription to receive support for Windows Container Support for Red Hat OpenShift. Without this additional Red Hat subscription, deploying Windows container workloads in production clusters is not supported. You can request support through the [Red Hat Customer Portal](http://access.redhat.com/).

For more information, see the Red Hat OpenShift Container Platform Life Cycle Policy document for [Red Hat OpenShift support for Windows Containers](https://access.redhat.com/support/policy/updates/openshift#windows).

If you do not have this additional Red Hat subscription, you can use the Community Windows Machine Config Operator, a distribution that lacks official support.

## [Chapter 4. Understanding Windows container workloads](#understanding-windows-container-workloads) Copy linkLink copied to clipboard!

You can use the Windows Machine Config Operator (WMCO) to run Microsoft Windows Server containers on OpenShift Container Platform.

For those that administer heterogeneous environments with a mix of Linux and Windows workloads, OpenShift Container Platform allows you to deploy Windows workloads running on Windows Server containers while also providing traditional Linux workloads hosted on Red Hat Enterprise Linux CoreOS (RHCOS) or Red Hat Enterprise Linux (RHEL).

Note

Multi-tenancy for clusters that have Windows nodes is not supported. Clusters are considered *multi-tenant* when multiple workloads operate on shared infrastructure and resources. If one or more workloads running on an infrastructure cannot be trusted, the multi-tenant environment is considered *hostile*.

Hostile multi-tenant clusters introduce security concerns in all Kubernetes environments. Additional security features, such as pod security policies or more fine-grained role-based access control (RBAC) for nodes, make exploiting your environment more difficult. However, if you choose to run hostile multi-tenant workloads, a hypervisor is the only security option you should use. The security domain for Kubernetes encompasses the entire cluster, not an individual node. For these types of hostile multi-tenant workloads, you should use physically isolated clusters.

Windows Server Containers provide resource isolation using a shared kernel but are not intended to be used in hostile multitenancy scenarios.

### [4.1. Windows workload management](#windows-workload-management_understanding-windows-container-workloads) Copy linkLink copied to clipboard!

To run Windows workloads in your cluster, you must install the Windows Machine Config Operator (WMCO).

The WMCO is a Linux-based Operator that runs on the Linux-based control plane and compute nodes. The WMCO orchestrates the process of deploying and managing Windows workloads on a cluster.

**Figure 4.1. WMCO design**

Before deploying Windows workloads, you must create a Windows compute node and have it join the cluster. The Windows node hosts the Windows workloads in a cluster, and can run alongside other Linux-based compute nodes. You can create a Windows compute node by creating a Windows compute machine set to host Windows Server compute machines. You must apply a Windows-specific label to the compute machine set that specifies a Windows OS image.

The WMCO watches for machines with the Windows label. After a Windows compute machine set is detected and its respective machines are provisioned, the WMCO configures the underlying Windows virtual machine (VM) so that it can join the cluster as a compute node.

**Figure 4.2. Mixed Windows and Linux workloads**

The WMCO expects a predetermined secret in its namespace containing a private key that is used to interact with the Windows instance. WMCO checks for this secret during boot up time and creates a user data secret which you must reference in the Windows `MachineSet` object that you created. Then the WMCO populates the user data secret with a public key that corresponds to the private key. With this data in place, the cluster can connect to the Windows VM using an SSH connection.

After the cluster establishes a connection with the Windows VM, you can manage the Windows node using similar practices as you would a Linux-based node.

Note

The OpenShift Container Platform web console provides most of the same monitoring capabilities for Windows nodes that are available for Linux nodes. However, the ability to monitor workload graphs for pods running on Windows nodes is not available at this time.

Scheduling Windows workloads to a Windows node can be done with typical pod scheduling practices, such as taints, tolerations, and node selectors. Alternatively, you can differentiate your Windows workloads from Linux workloads and other Windows-versioned workloads by using a `RuntimeClass` object.

### [4.2. Windows node services](#windows-node-services_understanding-windows-container-workloads) Copy linkLink copied to clipboard!

By default, the installation process installs several Windows-specific services on each Windows node.

Expand

| Service | Description |
| --- | --- |
| kubelet | Registers the Windows node and manages its status. |
| Container Network Interface (CNI) plugins | Exposes [networking](https://kubernetes.io/docs/setup/production-environment/windows/intro-windows-in-kubernetes/#networking) for Windows nodes. |
| Windows Instance Config Daemon (WICD) | Maintains the state of all services running on the Windows instance to ensure the instance functions as a worker node. |
| [Windows Exporter](https://github.com/openshift/prometheus-community-windows_exporter) | Exports Prometheus metrics from Windows nodes |
| [Kubernetes Cloud Controller Manager (CCM)](https://kubernetes.io/docs/concepts/architecture/cloud-controller/) | Interacts with the underlying Azure cloud platform. |
| hybrid-overlay | Creates the OpenShift Container Platform [Host Network Service (HNS)](https://docs.microsoft.com/en-us/virtualization/windowscontainers/container-networking/architecture#container-network-management-with-host-network-service). |
| kube-proxy | Maintains network rules on nodes allowing outside communication. |
| containerd container runtime | Manages the complete container lifecycle. |
| CSI Proxy | Enables CSI drivers to perform storage operations on the node, which allows containerized CSI drivers to run on Windows nodes. |

Show more

## [Chapter 5. Enabling Windows container workloads](#enabling-windows-container-workloads) Copy linkLink copied to clipboard!

Before adding Windows workloads to your cluster, you must install the Windows Machine Config Operator (WMCO), which is available in the OpenShift Container Platform software catalog. The WMCO orchestrates the process of deploying and managing Windows workloads on a cluster.

Note

Dual NIC is not supported on WMCO-managed Windows instances.

### [5.1. Prerequisites](#prerequisites) Copy linkLink copied to clipboard!

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).
* You have installed your cluster using one of the following infrastructures:

  + Any installer-provisioned infrastructure
  + A user-provisioned infrastructure with the `platform: none` field set in your `install-config.yaml` file
* You have configured hybrid networking with OVN-Kubernetes for your cluster. For more information, see "Configuring hybrid networking".
* You are running an OpenShift Container Platform cluster version 4.6.8 or later.

Note

Windows instances deployed by the WMCO are configured with the containerd container runtime. Because WMCO installs and manages the runtime, it is recommended that you do not manually install containerd on nodes.

For the comprehensive prerequisites for the Windows Machine Config Operator, see "Windows Machine Config Operator prerequisites".

### [5.2. Installing the Windows Machine Config Operator](#installing-the-wmco) Copy linkLink copied to clipboard!

You can install the Windows Machine Config Operator using either the web console or OpenShift CLI (`oc`).

Note

Due to a limitation within the Windows operating system, `clusterNetwork` CIDR addresses of class E, such as `240.0.0.0`, are not compatible with Windows nodes.

#### [5.2.1. Installing the Windows Machine Config Operator using the web console](#installing-wmco-using-web-console_enabling-windows-container-workloads) Copy linkLink copied to clipboard!

You can use the OpenShift Container Platform web console to install the Windows Machine Config Operator (WMCO).

Note

Dual NIC is not supported on WMCO-managed Windows instances.

**Procedure**

1. From the **Administrator** perspective in the OpenShift Container Platform web console, navigate to the **Ecosystem** → **Software Catalog** page.
2. Use the **Filter by keyword** box to search for `Windows Machine Config Operator` in the catalog. Click the **Windows Machine Config Operator** tile.
3. Review the information about the Operator and click **Install**.
4. On the **Install Operator** page:

   1. Select the **stable** channel as the **Update Channel**. The **stable** channel enables the latest stable release of the WMCO to be installed.
   2. The **Installation Mode** is preconfigured because the WMCO must be available in a single namespace only.
   3. Choose the **Installed Namespace** for the WMCO. The default Operator recommended namespace is `openshift-windows-machine-config-operator`.
   4. Click the **Enable Operator recommended cluster monitoring on the Namespace** checkbox to enable cluster monitoring for the WMCO.
   5. Select an **Approval Strategy**.

      * The **Automatic** strategy allows Operator Lifecycle Manager (OLM) to automatically update the Operator when a new version is available.
      * The **Manual** strategy requires a user with appropriate credentials to approve the Operator update.
5. Click **Install**. The WMCO is now listed on the **Installed Operators** page.

   Note

   The WMCO is installed automatically into the namespace you defined, like `openshift-windows-machine-config-operator`.
6. Verify that the **Status** shows **Succeeded** to confirm successful installation of the WMCO.

#### [5.2.2. Installing the Windows Machine Config Operator using the CLI](#installing-wmco-using-cli_enabling-windows-container-workloads) Copy linkLink copied to clipboard!

You can use the OpenShift CLI (`oc`) to install the Windows Machine Config Operator (WMCO).

Note

Dual NIC is not supported on WMCO-managed Windows instances.

**Procedure**

1. Create a namespace for the WMCO.

   1. Create a `Namespace` object YAML file for the WMCO. For example, `wmco-namespace.yaml`:

      ```
      apiVersion: v1
      kind: Namespace
      metadata:
        name: openshift-windows-machine-config-operator
        labels:
          openshift.io/cluster-monitoring: "true"
      ```

      where

      `metadata.name`
      :   Specifies the namespace to create the secret. You should deploy the WMCO in the `openshift-windows-machine-config-operator` namespace.

      `metadata.labels`
      :   Specifies the label required for enabling cluster monitoring for the WMCO.
   2. Create the namespace:

      ```
      $ oc create -f <file-name>.yaml
      ```

      For example:

      ```
      $ oc create -f wmco-namespace.yaml
      ```
2. Create the Operator group for the WMCO.

   1. Create an `OperatorGroup` object YAML file. For example, `wmco-og.yaml`:

      ```
      apiVersion: operators.coreos.com/v1
      kind: OperatorGroup
      metadata:
        name: windows-machine-config-operator
        namespace: openshift-windows-machine-config-operator
      spec:
        targetNamespaces:
        - openshift-windows-machine-config-operator
      ```
   2. Create the Operator group:

      ```
      $ oc create -f <file-name>.yaml
      ```

      For example:

      ```
      $ oc create -f wmco-og.yaml
      ```
3. Subscribe the namespace to the WMCO.

   1. Create a `Subscription` object YAML file. For example, `wmco-sub.yaml`:

      ```
      apiVersion: operators.coreos.com/v1alpha1
      kind: Subscription
      metadata:
        name: windows-machine-config-operator
        namespace: openshift-windows-machine-config-operator
      spec:
        channel: "stable"
        installPlanApproval: "Automatic"
        name: "windows-machine-config-operator"
        source: "redhat-operators"
        sourceNamespace: "openshift-marketplace"
      ```

      where:

      `spec.channel`
      :   Specifies `stable` as the channel.

      `spec.installPlanApproval`
      :   Specifies an approval strategy. You can set `Automatic` or `Manual`.

      `spec.source`
      :   Specifies the `redhat-operators` catalog source, which contains the `windows-machine-config-operator` package manifests. If your OpenShift Container Platform is installed on a restricted network, also known as a disconnected cluster, specify the name of the `CatalogSource` object you created when you configured the Operator LifeCycle Manager (OLM).

      `spec.sourceNamespace`
      :   Specifies the namespace of the catalog source. Use `openshift-marketplace` for the default software catalog sources.
   2. Create the subscription:

      ```
      $ oc create -f <file-name>.yaml
      ```

      For example:

      ```
      $ oc create -f wmco-sub.yaml
      ```

      The WMCO is now installed to the `openshift-windows-machine-config-operator`.
4. Verify the WMCO installation:

   ```
   $ oc get csv -n openshift-windows-machine-config-operator
   ```

   **Example output**

   ```
   NAME                                    DISPLAY                           VERSION   REPLACES   PHASE
   windows-machine-config-operator.2.0.0   Windows Machine Config Operator   2.0.0                Succeeded
   ```

### [5.3. Configuring a secret for the Windows Machine Config Operator](#configuring-secret-for-wmco_enabling-windows-container-workloads) Copy linkLink copied to clipboard!

Before you can use the Windows Machine Config Operator (WMCO), you must create a secret in the same WMCO namespace as your private key.

This secret is required to allow the WMCO to communicate with the Windows virtual machine (VM). Use a different private key than the one used when installing the cluster.

**Prerequisites**

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You created a PEM-encoded file containing a private key by using a strong algorithm, such as ECDSA.

  If you created the key pair on a Red Hat Enterprise Linux (RHEL) system, before you can use the public key on a Windows system, make sure the public key is saved using ASCII encoding. For example, the following PowerShell command copies a public key, encoding it for the ASCII character set:

  ```
  C:\> echo "ssh-rsa <ssh_pub_key>" | Out-File <ssh_key_path> -Encoding ascii
  ```

  where:

  `<ssh_pub_key>`
  :   Specifies the SSH public key used to access the cluster.

  `<ssh_key_path>`
  :   Specifies the path to the SSH public key.

**Procedure**

* Define the secret required to access the Windows VMs:

  ```
  $ oc create secret generic cloud-private-key --from-file=private-key.pem=${HOME}/.ssh/<key> \
      -n openshift-windows-machine-config-operator
  ```

  You must create the private key in the WMCO namespace, such as `openshift-windows-machine-config-operator`.

### [5.4. Configuring debug-level logging for the Windows Machine Config Operator](#wmco-configure-debug-logging_enabling-windows-container-workloads) Copy linkLink copied to clipboard!

You can edit the WMCO `Subscription` object to change the Windows Machine Config Operator (WMCO) log level to `debug`, if you need more verbose output.

By default, the WMCO is configured to use the `info` log level.

**Procedure**

1. Edit the `windows-machine-config-operator` subscription in the `windows-machine-config-operator` namespace by using the following command:

   ```
   $ oc edit subscription windows-machine-config-operator -n openshift-windows-machine-config-operator
   ```
2. Add the follwing parameters to the `.spec.config.env` stanza:

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   # ...
     name: windows-machine-config-operator
     namespace: openshift-windows-machine-config-operator
   # ...
   spec:
   # ...
     config:
       env:
       - name: ARGS
         value: --debugLogging
   ```

   where:

   `spec.config.env.name`
   :   Specifies a list of environment variables that must exist in all containers in the pod.

   `spec.config.env.value`
   :   Specifies the `debug` level of verbosity for log messages.

   You can revert to the default `info` log level by removing the `name` and `value` parameters that you added.

### [5.5. Using Windows containers in a proxy-enabled cluster](#wmco-cluster-wide-proxy_enabling-windows-container-workloads) Copy linkLink copied to clipboard!

You can add Windows nodes and run workloads in a proxy-enabled cluster because Windows Machine Config Operator (WMCO) can consume and use the cluster-wide egress proxy when making external requests outside the cluster’s internal network.

Because of the support for the cluster-wide egress proxy, your Windows nodes can pull images from registries that are secured behind your proxy server or to make requests to off-cluster services and services that use a custom public key infrastructure.

Note

The cluster-wide proxy affects system components only, not user workloads.

In proxy-enabled clusters, the WMCO is aware of the `NO_PROXY`, `HTTP_PROXY`, and `HTTPS_PROXY` values that are set for the cluster. The WMCO periodically checks whether the proxy environment variables have changed. If there is a discrepancy, the WMCO reconciles and updates the proxy environment variables on the Windows instances.

Windows workloads created on Windows nodes in proxy-enabled clusters do not inherit proxy settings from the node by default, the same as with Linux nodes. Also, by default PowerShell sessions do not inherit proxy settings on Windows nodes in proxy-enabled clusters.

For more information on the cluster-wide proxy, see "Configuring the cluster-wide proxy".

### [5.6. Using Windows containers with a mirror registry](#wmco-disconnected-cluster_enabling-windows-container-workloads) Copy linkLink copied to clipboard!

When using the Windows Machine Config Operator (WMCO), your Windows workloads can pull images from a registry mirror rather than from a public registry by using an `ImageDigestMirrorSet` (IDMS) or `ImageTagMirrorSet` (ITMS) object to configure your cluster to pull images from the mirror registry.

A mirror registry has the following benefits:

* Avoids public registry outages
* Speeds up node and pod creation
* Pulls images from behind your organization’s firewall

A mirror registry can also be used with a OpenShift Container Platform cluster in a disconnected, or air-gapped, network. A *disconnected network* is a restricted network without direct internet connectivity. Because the cluster does not have access to the internet, any external container images cannot be referenced.

Using a mirror registry requires the following general steps:

* Create the mirror registry, using a tool such as Red Hat Quay.
* Create a container image registry credentials file.
* Copy the images from your online image repository to your mirror registry.

For information about these steps, see "About disconnected installation mirroring."

After creating the mirror registry and mirroring the images, you can use an `ImageDigestMirrorSet` (IDMS) or `ImageTagMirrorSet` (ITMS) object to configure your cluster to pull images from the mirror registry without needing to update each of your pod specs. The IDMS and ITMS objects redirect requests to pull images from a repository on a source image registry and have it resolved by the mirror repository instead.

If changes are made to the IDMS or ITMS object, the WMCO automatically updates the appropriate `hosts.toml` file on your Windows nodes with the new information. Note that the WMCO sequentially updates each Windows node when mirror settings are changed. As such, the time required for these updates increases with the number of Windows nodes in the cluster.

Because Windows nodes configured by the WMCO rely on the containerd container runtime, the WMCO ensures that the containerd configuration files are up-to-date with the registry settings. For new nodes, these files are copied to the instances upon creation. For existing nodes, after activating the mirror registry, the registry controller uses SSH to access each node and copy the generated configuration files, replacing any existing files.

You can use a mirror registry with machine set or Bring-Your-Own-Host (BYOH) Windows nodes.

When using an IDMS or ITMS object to mirror container images on Windows nodes, take note of the following behaviors that differ from Linux nodes:

* Mirroring on Windows nodes works on the registry level, rather than on the image level used by Linux nodes. As such, Windows images mirrored by using IDMS or ITMS objects have specific naming requirements.

  The final portion of the namespace and the image name of the mirror image must match the image being mirrored. For example, when mirroring the `mcr.microsoft.com/oss/kubernetes/pause:3.9` image, the mirror must be in the `$mirrorRegistry/<organization>/oss/kubernetes/pause:3.9` format, where `$org` can be any organization name or namespace or excluded entirely. Some valid values are `$mirrorRegistry/oss/kubernetes/pause:3.9`, `$mirrorRegistry/custom/oss/kubernetes/pause:3.9`, and `$mirrorRegistry/x/y/z/oss/kubernetes/pause:3.9`.
* A Windows node takes the ITMS object and uses it to configure registry-wide mirrors. In the following example, configuring `quay.io/remote-org/image` to mirror to `quay.io/my-org/image` results in the Windows node using that mirror for all images from `quay.io/remote-org`. As such, `quay.io/remote-org/image:tag` uses the `quay.io/my-org/image:tag` image, as expected, but another container using `quay.io/remote-org/different-image:tag` would also try to use the `quay.io/remote-org/different-image:tag` mirror. This can cause unintended behavior if it is not accounted for.

  For this reason, specify container images using a digest by an IDMS object instead of an ITMS object. Using a digest can prevent the wrong container image from being used, by ensuring that the image the container specifies and the image being pulled have the same digest.

#### [5.6.1. Understanding image registry repository mirroring](#images-configuration-registry-mirror_enabling-windows-container-workloads) Copy linkLink copied to clipboard!

You must mirror images to update clusters in disconnected environments.

By setting up container registry repository mirroring, you can perform the following tasks:

* Configure your OpenShift Container Platform cluster to redirect requests to pull images from a repository on a source image registry and have it resolved by a repository on a mirrored image registry.
* Identify multiple mirrored repositories for each target repository, to make sure that if one mirror is down, another can be used.

Repository mirroring in OpenShift Container Platform includes the following attributes:

* Image pulls are resilient to registry downtimes.
* Clusters in disconnected environments can pull images from critical locations, such as `quay.io`, and have registries behind a company firewall provide the requested images.
* A particular order of registries is tried when an image pull request is made, with the permanent registry typically being the last one tried.
* The mirror information you enter is added to the appropriate `hosts.toml` containerd configuration file(s) on every Windows node in the OpenShift Container Platform cluster.
* When a node makes a request for an image from the source repository, it tries each mirrored repository in turn until it finds the requested content. If all mirrors fail, the cluster tries the source repository. If successful, the image is pulled to the node.

You can set up repository mirroring in the following ways:

* At OpenShift Container Platform installation:

  By pulling container images needed by OpenShift Container Platform and then bringing those images behind your company’s firewall, you can install OpenShift Container Platform into a data center that is in a disconnected environment.
* After OpenShift Container Platform installation:

  If you did not configure mirroring during OpenShift Container Platform installation, you can do so postinstallation by using any of the following custom resource (CR) objects:

  + `ImageDigestMirrorSet` (IDMS). This object allows you to pull images from a mirrored registry by using digest specifications. The IDMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails.
  + `ImageTagMirrorSet` (ITMS). This object allows you to pull images from a mirrored registry by using image tags. The ITMS CR enables you to set a fall back policy that allows or stops continued attempts to pull from the source registry if the image pull fails.

Each of these custom resource objects identify the following information:

* The source of the container image repository you want to mirror.
* A separate entry for each mirror repository you want to offer the content

Note the following actions and how they affect node drain behavior:

* If you create an IDMS or ICSP CR object, the MCO does not drain or reboot the node.
* If you create an ITMS CR object, the MCO drains and reboots the node.
* If you delete an ITMS or IDMS CR object, the MCO drains and reboots the node.
* If you modify an ITMS or IDMS CR object, the MCO drains and reboots the node.

The Windows Machine Config Operator (WMCO) watches for changes to the IDMS and ITMS resources and generates a set of `hosts.toml` containerd configuration files, one file for each source registry, with those changes. The WMCO then updates any existing Windows nodes to use the new registry configuration.

Note

The IDMS and ITMS objects must be created before you can add Windows nodes using a mirrored registry.

#### [5.6.2. Configuring image registry repository mirroring](#images-configuration-registry-mirror-configuring_enabling-windows-container-workloads) Copy linkLink copied to clipboard!

You can create postinstallation mirror configuration custom resources (CR) to redirect image pull requests from a source image registry to a mirrored image registry.

Important

Windows images mirrored through `ImageDigestMirrorSet` and `ImageTagMirrorSet` objects have specific naming requirements as described in "Using Windows containers with a mirror registry".

**Prerequisites**

* Access to the cluster as a user with the `cluster-admin` role.

**Procedure**

1. Configure mirrored repositories, by either:

   * Setting up a mirrored repository with Red Hat Quay. You can copy images from one repository to another and also automatically sync those repositories repeatedly over time by using Red Hat Quay.

     + [Red Hat Quay Repository Mirroring](https://docs.redhat.com/en/documentation/red_hat_quay/3/html/manage_red_hat_quay/arch-mirroring-intro#enabling-repository-mirroring-quay)
   * Using a tool such as `skopeo` to copy images manually from the source repository to the mirrored repository.

     For example, after installing the skopeo RPM package on a {op-system-base-full system}, use the `skopeo` command as shown in the following example:

     ```
     $ skopeo copy --all \
     docker://registry.access.redhat.com/ubi9/ubi-minimal:latest@sha256:5cf... \
     docker://example.io/example/ubi-minimal
     ```

     In this example, you have a container image registry named `example.io` and image repository named `example`. You want to copy the `ubi9/ubi-minimal` image from `registry.access.redhat.com` to `example.io`. After you create the mirrored registry, you can configure your OpenShift Container Platform cluster to redirect requests made to the source repository to the mirrored repository.

   Important

   You must mirror the `mcr.microsoft.com/oss/kubernetes/pause:3.9` image. For example, you could use the following `skopeo` command to mirror the image:

   ```
   $ skopeo copy \
   docker://mcr.microsoft.com/oss/kubernetes/pause:3.9\
   docker://example.io/oss/kubernetes/pause:3.9
   ```
2. Log in to your OpenShift Container Platform cluster.
3. Create an `ImageDigestMirrorSet` or `ImageTagMirrorSet` CR, as needed, replacing the source and mirrors with your own registry and repository pairs and images:

   ```
   apiVersion: config.openshift.io/v1
   kind: ImageDigestMirrorSet
   metadata:
     name: ubi9repo
   spec:
     imageDigestMirrors:
     - mirrors:
       - example.io/example/ubi-minimal
       - example.com/example2/ubi-minimal
       source: registry.access.redhat.com/ubi9/ubi-minimal
       mirrorSourcePolicy: AllowContactingSource
     - mirrors:
       - mirror.example.com
       source: registry.redhat.io
       mirrorSourcePolicy: NeverContactSource
     - mirrors:
       - docker.io
       source: docker-mirror.internal
       mirrorSourcePolicy: AllowContactingSource
   ```
4. Create the new object by running the following command:

   ```
   $ oc create -f registryrepomirror.yaml
   ```
5. To check that the mirrored configuration settings are applied, do the following on one of the nodes.

   1. List your nodes:

      ```
      $ oc get node
      ```

      **Example output**

      ```
      NAME                           STATUS                     ROLES    AGE  VERSION
      worker-1.compute.local         Ready                      worker   7m   v1.35.4
      master-1.compute.local         Ready                      master   11m  v1.35.4
      master-2.compute.local         Ready                      master   11m  v1.35.4
      worker-2.compute.local         Ready                      worker   7m   v1.35.4
      worker-3.compute.local         Ready                      worker   7m   v1.35.4
      master-3.compute.local         Ready                      master   11m  v1.35.4
      ```
   2. Start the debugging process to access the node:

      ```
      $ oc debug node/worker-1.compute.local
      ```

      **Example output**

      ```
      Starting pod/worker-1.compute.local-debug ...
      To use host binaries, run `chroot /host`
      ```
   3. Change your root directory to `/host`:

      ```
      sh-4.2# chroot /host
      ```
   4. Check that the WMCO generated a `hosts.toml` file for each registry on each Windows instance. For the previous example IDMS object, there should be three files in the following file structure:

      ```
      $ tree $config_path
      ```

      **Example output**

      ```
      C:/k/containerd/registries/
      |── registry.access.redhat.com
      |   └── hosts.toml
      |── mirror.example.com
      |   └── hosts.toml
      └── docker.io
          └── hosts.toml:
      ```

      The following output represents a `hosts.toml` containerd configuration file where the previous example IDMS object was applied.

      **Example host.toml files**

      ```
      $ cat "$config_path"/registry.access.redhat.com/host.toml
      server = "https://registry.access.redhat.com" # default fallback server since "AllowContactingSource" mirrorSourcePolicy is set

      [host."https://example.io/example/ubi-minimal"]
       capabilities = ["pull"]

      [host."https://example.com/example2/ubi-minimal"] # secondary mirror
       capabilities = ["pull"]

      $ cat "$config_path"/registry.redhat.io/host.toml
      # "server" omitted since "NeverContactSource" mirrorSourcePolicy is set

      [host."https://mirror.example.com"]
       capabilities = ["pull"]

      $ cat "$config_path"/docker.io/host.toml
      server = "https://docker.io"

      [host."https://docker-mirror.internal"]
       capabilities = ["pull", "resolve"] # resolve tags
      ```
   5. Pull an image to the node from the source and check if it is resolved by the mirror.

      ```
      sh-4.2# podman pull --log-level=debug registry.access.redhat.com/ubi9/ubi-minimal@sha256:5cf...
      ```

**Troubleshooting**

If the repository mirroring procedure does not work as described, use the following information about how repository mirroring works to help troubleshoot the problem:

* The first working mirror is used to supply the pulled image.
* The main registry is only used if no other mirror works.
* From the system context, the `Insecure` flags are used as fallback.

### [5.7. Rebooting a node gracefully](#nodes-nodes-rebooting-gracefully_enabling-windows-container-workloads) Copy linkLink copied to clipboard!

You can perform a graceful restart of a node, where all workloads are moved to other nodes, without data loss or service disruption.

The Windows Machine Config Operator (WMCO) minimizes node reboots whenever possible. However, certain operations and updates require a reboot to ensure that changes are applied correctly and securely. To safely reboot your Windows nodes, use the graceful reboot process. For information on gracefully rebooting a standard OpenShift Container Platform node, see "Rebooting a node gracefully" in the Nodes documentation.

Before rebooting a node, it is recommended to backup etcd data to avoid any data loss on the node.

Note

For single-node OpenShift clusters that require users to perform the `oc login` command rather than having the certificates in `kubeconfig` file to manage the cluster, the `oc adm` commands might not be available after cordoning and draining the node. This is because the `openshift-oauth-apiserver` pod is not running due to the cordon. You can use SSH to access the nodes as indicated in the following procedure.

In a single-node OpenShift cluster, pods cannot be rescheduled when cordoning and draining. However, doing so gives the pods, especially your workload pods, time to properly stop and release associated resources.

The following procedure demonstrates how to perform a graceful restart of a node.

**Procedure**

1. Mark the node as unschedulable:

   ```
   $ oc adm cordon <node1>
   ```
2. Drain the node to remove all the running pods:

   ```
   $ oc adm drain <node1> --ignore-daemonsets --delete-emptydir-data --force
   ```

   You might receive errors that pods associated with custom pod disruption budgets (PDB) cannot be evicted.

   **Example error**

   ```
   error when evicting pods/"rails-postgresql-example-1-72v2w" -n "rails" (will retry after 5s): Cannot evict pod as it would violate the pod's disruption budget.
   ```

   In this case, run the drain command again, adding the `disable-eviction` flag, which bypasses the PDB checks:

   ```
   $ oc adm drain <node1> --ignore-daemonsets --delete-emptydir-data --force --disable-eviction
   ```
3. SSH into the Windows node and enter PowerShell by running the following command:

   ```
   C:\> powershell
   ```
4. Restart the node by running the following command:

   ```
   C:\>  Restart-Computer -Force
   ```
5. Windows nodes on Amazon Web Services (AWS) do not return to `READY` state after a graceful reboot due to an inconsistency with the EC2 instance metadata routes and the Host Network Service (HNS) networks.

   After the reboot, SSH into any Windows node on AWS and add the route by running the following command in a shell prompt:

   ```
   C:\> route add 169.254.169.254 mask 255.255.255.0 <gateway_ip>
   ```

   where:

   `169.254.169.254`
   :   Specifies the address of the EC2 instance metadata endpoint.

   `255.255.255.255`
   :   Specifies the network mask of the EC2 instance metadata endpoint.

   `<gateway_ip>`
   :   Specifies the corresponding IP address of the gateway in the Windows instance, which you can find by running the following command:

       ```
       C:\> ipconfig | findstr /C:"Default Gateway"
       ```
6. After the reboot is complete, mark the node as schedulable by running the following command:

   ```
   $ oc adm uncordon <node1>
   ```
7. Verify that the node is ready:

   ```
   $ oc get node <node1>
   ```

   **Example output**

   ```
   NAME    STATUS  ROLES    AGE     VERSION
   <node1> Ready   worker   6d22h   v1.18.3+b0068a8
   ```

## [Chapter 6. Creating Windows machine sets](#creating-windows-machine-sets) Copy linkLink copied to clipboard!

### [6.1. Creating a Windows machine set on AWS](#creating-windows-machineset-aws) Copy linkLink copied to clipboard!

You can use a `MachineSet` custom resource (CR) to add a Windows compute node to your Amazon Web Services cluster, where you can run Windows container workloads.

For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines. For more information about machine sets, see "Overview of machine management" in the *Additional resources* section.

#### [6.1.1. Prerequisites](#prerequisites_creating-windows-machineset-aws) Copy linkLink copied to clipboard!

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a supported Windows Server as the operating system image.

  Use one of the following `aws` commands, as appropriate for your Windows Server release, to query valid AMI images:

  **Example Windows Server 2025 command**

  ```
  $ aws ec2 describe-images --region <aws_region_name> --filters "Name=name,Values=Windows_Server-2025*English*Core*Base*" "Name=is-public,Values=true" --query "reverse(sort_by(Images, &CreationDate))[*].{name: Name, id: ImageId}" --output table
  ```

  **Example Windows Server 2022 command**

  ```
  $ aws ec2 describe-images --region <aws_region_name> --filters "Name=name,Values=Windows_Server-2022*English*Core*Base*" "Name=is-public,Values=true" --query "reverse(sort_by(Images, &CreationDate))[*].{name: Name, id: ImageId}" --output table
  ```

  **Example Windows Server 2019 command**

  ```
  $ aws ec2 describe-images --region <aws_region_name> --filters "Name=name,Values=Windows_Server-2019*English*Core*Base*" "Name=is-public,Values=true" --query "reverse(sort_by(Images, &CreationDate))[*].{name: Name, id: ImageId}" --output table
  ```

  where:

  <aws\_region\_name>
  :   Specifies the name of your AWS region.
* For disconnected clusters, the Windows AMI must have the EC2LaunchV2 agent version 2.0.2107 or later installed. For more information, see "Install the latest version of EC2Launch v2 (AWS documentation)" in the *Additional references* section.

#### [6.1.2. Sample YAML for a Windows MachineSet object on AWS](#windows-machineset-aws_creating-windows-machineset-aws) Copy linkLink copied to clipboard!

You can add Windows nodes to an Amazon Web Services (AWS) cluster by defining a Windows `MachineSet` object that the Windows Machine Config Operator (WMCO) can react upon.

The following example is a YAML file for creating a `MachineSet` object for AWS.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-windows-worker-<zone>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone>
        machine.openshift.io/os-id: Windows
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: ""
      providerSpec:
        value:
          ami:
            id: <windows_container_ami>
          apiVersion: awsproviderconfig.openshift.io/v1beta1
          blockDevices:
            - ebs:
                iops: 0
                volumeSize: 120
                volumeType: gp2
          credentialsSecret:
            name: aws-cloud-credentials
          deviceIndex: 0
          iamInstanceProfile:
            id: <infrastructure_id>-worker-profile
          instanceType: m5a.large
          kind: AWSMachineProviderConfig
          placement:
            availabilityZone: <zone>
            region: <region>
          securityGroups:
          - filters:
            - name: tag:Name
              values:
              - <infrastructure_id>-node
          - filters:
            - name: tag:Name
              values:
              - <infrastructure_id>-lb
          subnet:
            filters:
            - name: tag:Name
              values:
              - <infrastructure_id>-subnet-private-<zone>
          tags:
            - name: kubernetes.io/cluster/<infrastructure_id>
              value: owned
          userDataSecret:
            name: windows-user-data
            namespace: openshift-machine-api
```

where:

`metadata.labels`
:   For the `machine.openshift.io/cluster-api-cluster` label, replace `<infrastructure_id>` with the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`metadata.name`
:   Replace the infrastructure ID, worker label, and zone.

`spec.selector.matchLabels`
:   Replace the parameters for the following labels:

    * `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
    * `machine.openshift.io/cluster-api-machineset`. Replace the infrastructure ID, worker label, and zone.

`spec.template.metadata.labels`
:   Replace the parameters for the following labels:

    * `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
    * `machine.openshift.io/cluster-api-machineset`. Replace the infrastructure ID, worker label, and zone.
    * `machine.openshift.io/os-id: Windows`. When set to `Windows`, configures the compute machine set as a Windows machine.

`spec.template.spec.metadata.labels`
:   When set to `node-role.kubernetes.io/worker`, configures the node as a compute machine.

`spec.template.spec.providerSpec`
:   Specify the following parameters:

    * `value.ami.id`. Specify the AMI ID of a supported Windows image with a container runtime installed.

      Note

      For disconnected clusters, the Windows AMI must have the EC2LaunchV2 agent version 2.0.2107 or later installed. For more information, see the [Install the latest version of EC2Launch v2 (AWS documentation)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-v2-install.html).
    * `value.iamInstanceProfile.id`. Replace the infrastructure ID.
    * `value.placement.availabilityZone`. Specifies the AWS zone, such as `us-east-1a`.
    * `value.placement.region`. Specifies the AWS region, such as `us-east-1`.
    * `value.securityGroups.filters.values`. Replace the infrastructure ID.
    * `value.subnet.filters.values`. Replace the infrastructure ID and zone.
    * `value.tags.name`. Replace the infrastructure ID.
    * `value.userDataSecret.name`. Specifies the name of the secret in the user data YAML file that is in the `openshift-machine-api` namespace. Use the value that installation program populates in the default compute machine set.

#### [6.1.3. Creating a compute machine set](#machineset-creating_creating-windows-machineset-aws) Copy linkLink copied to clipboard!

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

**Prerequisites**

* Deploy an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.
* In disconnected environments, the image specified in the `MachineSet` custom resource (CR) must have the [OpenSSH server v0.0.1.0 installed](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell#install-openssh-for-windows).

**Procedure**

1. Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.

   Ensure that you set the `<clusterID>` and `<role>` parameter values.
2. Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster.

   1. To list the compute machine sets in your cluster, run the following command:

      ```
      $ oc get machinesets -n openshift-machine-api
      ```

      The following is example output:

      ```
      NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
      agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1d   0         0                             55m
      agl030519-vplxk-worker-us-east-1e   0         0                             55m
      agl030519-vplxk-worker-us-east-1f   0         0                             55m
      ```
   2. To view values of a specific compute machine set custom resource (CR), run the following command:

      ```
      $ oc get machineset <machineset_name> \
        -n openshift-machine-api -o yaml
      ```

      The following is example output:

      ```
      apiVersion: machine.openshift.io/v1beta1
      kind: MachineSet
      metadata:
        labels:
          machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        name: <infrastructure_id>-<role>
        namespace: openshift-machine-api
      spec:
        replicas: 1
        selector:
          matchLabels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
            machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
        template:
          metadata:
            labels:
              machine.openshift.io/cluster-api-cluster: <infrastructure_id>
              machine.openshift.io/cluster-api-machine-role: <role>
              machine.openshift.io/cluster-api-machine-type: <role>
              machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
          spec:
            providerSpec:
              ...
      ```

      where:

      `metadata.labels.machine.openshift.io/cluster-api-cluster`
      :   Specifies the cluster infrastructure ID.

      `metadata.labels.name`
      :   Specifies a default node label.

          Note

          For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines.

      `spec.template.metadata.spec.providerSpec`
      :   Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider.
3. Create a `MachineSet` CR by running the following command:

   ```
   $ oc create -f <file_name>.yaml
   ```

**Verification**

* View the list of compute machine sets by running the following command:

  ```
  $ oc get machineset -n openshift-machine-api
  ```

  The following is example output:

  ```
  NAME                                       DESIRED   CURRENT   READY   AVAILABLE   AGE
  agl030519-vplxk-windows-worker-us-east-1a  1         1         1       1           11m
  agl030519-vplxk-worker-us-east-1a          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1b          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1c          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1d          0         0                             55m
  agl030519-vplxk-worker-us-east-1e          0         0                             55m
  agl030519-vplxk-worker-us-east-1f          0         0                             55m
  ```

  When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

### [6.2. Creating a Windows machine set on Azure](#creating-windows-machineset-azure) Copy linkLink copied to clipboard!

You can use a `MachineSet` custom resource (CR) to add a Windows compute node to your Microsoft Azure cluster, where you can run Windows container workloads.

For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines. For more information about machine sets, see "Overview of machine management".

#### [6.2.1. Prerequisites](#prerequisites_creating-windows-machineset-azure) Copy linkLink copied to clipboard!

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a supported Windows Server as the operating system image.

#### [6.2.2. Sample YAML for a Windows MachineSet object on Azure](#windows-machineset-azure_creating-windows-machineset-azure) Copy linkLink copied to clipboard!

You can add Windows nodes to an Microsoft Azure cluster by defining a Windows `MachineSet` object that the Windows Machine Config Operator (WMCO) can react upon.

The following example is a YAML file for creating a `MachineSet` object for Azure.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <windows_machine_set_name>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <windows_machine_set_name>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <windows_machine_set_name>
        machine.openshift.io/os-id: Windows
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: ""
      providerSpec:
        value:
          apiVersion: azureproviderconfig.openshift.io/v1beta1
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image:
            offer: WindowsServer
            publisher: MicrosoftWindowsServer
            resourceID: ""
            sku: 2022-datacenter
            version: latest
          kind: AzureMachineProviderSpec
          location: <location>
          networkResourceGroup: <infrastructure_id>-rg
          osDisk:
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Windows
          publicIP: false
          resourceGroup: <infrastructure_id>-rg
          subnet: <infrastructure_id>-worker-subnet
          userDataSecret:
            name: windows-user-data
            namespace: openshift-machine-api
          vmSize: Standard_D2s_v3
          vnet: <infrastructure_id>-vnet
          zone: "<zone>"
```

where:

`metadata.labels`
:   For the `machine.openshift.io/cluster-api-cluster` label, replace `<infrastructure_id>` with the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`metadata.name`
:   Replace `<windows_machine_set_name>` with the Windows compute machine set name. Windows machine names on Azure cannot be more than 15 characters long. Therefore, the compute machine set name cannot be more than 9 characters long, due to the way machine names are generated from it.

`spec.selector.matchLabels`
:   Replace the parameters for the following labels:

    * `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
    * `machine.openshift.io/cluster-api-machineset`. Replace the Windows compute machine set name.

`spec.template.metadata.labels`
:   Replace the parameters for the following labels:

    * `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
    * `machine.openshift.io/cluster-api-machineset`. Replace the Windows compute machine set name.
    * `machine.openshift.io/os-id: Windows`. When set to `Windows`, configures the compute machine set as a Windows machine.

`spec.template.spec.metadata.labels`
:   When set to `node-role.kubernetes.io/worker`, configures the node as a compute machine.

`spec.template.spec.providerSpec`
:   Specify the following parameters:

    * `value.image`. Specifies a `WindowsServer` image offering that defines the `2022-datacenter` SKU.
    * `value.location`. Specifies the Azure region, such as `centralus`.
    * `value.networkResourceGroup`. Replace the infrastructure ID.
    * `value.resourceGroup`. Replace the infrastructure ID.
    * `value.userDataSecret.name`. Specifies the name of the secret in the user data YAML file that is in the `openshift-machine-api` namespace. Use the value that installation program populates in the default compute machine set.
    * `value.zone`. Specifies the zone within your region to place machines on. Be sure that your region supports the zone that you specify.

#### [6.2.3. Creating a compute machine set](#machineset-creating_creating-windows-machineset-azure) Copy linkLink copied to clipboard!

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

**Prerequisites**

* Deploy an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.
* In disconnected environments, the image specified in the `MachineSet` custom resource (CR) must have the [OpenSSH server v0.0.1.0 installed](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell#install-openssh-for-windows).

**Procedure**

1. Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.

   Ensure that you set the `<clusterID>` and `<role>` parameter values.
2. Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster.

   1. To list the compute machine sets in your cluster, run the following command:

      ```
      $ oc get machinesets -n openshift-machine-api
      ```

      The following is example output:

      ```
      NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
      agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1d   0         0                             55m
      agl030519-vplxk-worker-us-east-1e   0         0                             55m
      agl030519-vplxk-worker-us-east-1f   0         0                             55m
      ```
   2. To view values of a specific compute machine set custom resource (CR), run the following command:

      ```
      $ oc get machineset <machineset_name> \
        -n openshift-machine-api -o yaml
      ```

      The following is example output:

      ```
      apiVersion: machine.openshift.io/v1beta1
      kind: MachineSet
      metadata:
        labels:
          machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        name: <infrastructure_id>-<role>
        namespace: openshift-machine-api
      spec:
        replicas: 1
        selector:
          matchLabels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
            machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
        template:
          metadata:
            labels:
              machine.openshift.io/cluster-api-cluster: <infrastructure_id>
              machine.openshift.io/cluster-api-machine-role: <role>
              machine.openshift.io/cluster-api-machine-type: <role>
              machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
          spec:
            providerSpec:
              ...
      ```

      where:

      `metadata.labels.machine.openshift.io/cluster-api-cluster`
      :   Specifies the cluster infrastructure ID.

      `metadata.labels.name`
      :   Specifies a default node label.

          Note

          For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines.

      `spec.template.metadata.spec.providerSpec`
      :   Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider.
3. Create a `MachineSet` CR by running the following command:

   ```
   $ oc create -f <file_name>.yaml
   ```

**Verification**

* View the list of compute machine sets by running the following command:

  ```
  $ oc get machineset -n openshift-machine-api
  ```

  The following is example output:

  ```
  NAME                                       DESIRED   CURRENT   READY   AVAILABLE   AGE
  agl030519-vplxk-windows-worker-us-east-1a  1         1         1       1           11m
  agl030519-vplxk-worker-us-east-1a          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1b          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1c          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1d          0         0                             55m
  agl030519-vplxk-worker-us-east-1e          0         0                             55m
  agl030519-vplxk-worker-us-east-1f          0         0                             55m
  ```

  When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

### [6.3. Creating a Windows machine set on Google Cloud](#creating-windows-machineset-gcp) Copy linkLink copied to clipboard!

You can use a `MachineSet` custom resource (CR) to add a Windows compute node to your Google Cloud cluster, where you can run Windows container workloads.

For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines. For more information about machine sets, see "Overview of machine management".

#### [6.3.1. Prerequisites](#prerequisites_creating-windows-machineset-gcp) Copy linkLink copied to clipboard!

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a supported Windows Server as the operating system image.

#### [6.3.2. Sample YAML for a Windows MachineSet object on Google Cloud](#windows-machineset-gcp_creating-windows-machineset-gcp) Copy linkLink copied to clipboard!

You can add Windows nodes to a Google Cloud cluster by defining a Windows `MachineSet` object that the Windows Machine Config Operator (WMCO) can react upon.

The following example is a YAML file for creating a `MachineSet` object for Google Cloud.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-windows-worker-<zone_suffix>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone_suffix>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone_suffix>
        machine.openshift.io/os-id: Windows
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          canIPForward: false
          credentialsSecret:
            name: gcp-cloud-credentials
          deletionProtection: false
          disks:
          - autoDelete: true
            boot: true
            image: <windows_server_image>
            sizeGb: 128
            type: pd-ssd
          kind: GCPMachineProviderSpec
          machineType: n1-standard-4
          networkInterfaces:
          - network: <infrastructure_id>-network
            subnetwork: <infrastructure_id>-worker-subnet
          projectID: <project_id>
          region: <region>
          serviceAccounts:
          - email: <infrastructure_id>-w@<project_id>.iam.gserviceaccount.com
            scopes:
            - https://www.googleapis.com/auth/cloud-platform
          tags:
          - <infrastructure_id>-worker
          userDataSecret:
            name: windows-user-data
          zone: <zone>
```

where:

`metadata.labels`
:   For the `machine.openshift.io/cluster-api-cluster` label, replace `<infrastructure_id>` with the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`metadata.name`
:   Replace the infrastructure ID, worker label, and zone suffix, such as `a`.

`spec.selector.matchLabels`
:   Replace the parameters for the following labels:

    * `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
    * `machine.openshift.io/cluster-api-machineset`. Replace the infrastructure ID, worker label, and zone suffix.

`spec.template.metadata.labels`
:   Replace the parameters for the following labels:

    * `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
    * `machine.openshift.io/cluster-api-machineset`. Replace the infrastructure ID, worker label, and zone suffix.
    * `machine.openshift.io/os-id: Windows`. When set to `Windows`, configures the compute machine set as a Windows machine.

`spec.template.spec.metadata.labels`
:   When set to `node-role.kubernetes.io/worker`, configures the node as a compute machine.

`spec.template.spec.providerSpec`
:   Specify the following parameters:

    * `value.disks.image`. Specifies the full path to an image of a supported version of Windows Server.
    * `value.networkInterfaces.network`. Replace the infrastructure ID.
    * `value.networkInterfaces.subnetwork`. Replace the infrastructure ID.
    * `value.projectID`. Specifies the Google Cloud project that this cluster was created in.
    * `value.region`. Specifies the Google Cloud region, such as `us-central1`.
    * `value.userDataSecret.name`. Specifies the name of the secret in the user data YAML file that is in the `openshift-machine-api` namespace. Use the value that installation program populates in the default compute machine set.
    * `value.zone`. Specifies the zone within the chosen region, such as `us-central1-a`.

#### [6.3.3. Creating a compute machine set](#machineset-creating_creating-windows-machineset-gcp) Copy linkLink copied to clipboard!

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

**Prerequisites**

* Deploy an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.

**Procedure**

1. Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.

   Ensure that you set the `<clusterID>` and `<role>` parameter values.
2. Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster.

   1. To list the compute machine sets in your cluster, run the following command:

      ```
      $ oc get machinesets -n openshift-machine-api
      ```

      The following is example output:

      ```
      NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
      agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1d   0         0                             55m
      agl030519-vplxk-worker-us-east-1e   0         0                             55m
      agl030519-vplxk-worker-us-east-1f   0         0                             55m
      ```
   2. To view values of a specific compute machine set custom resource (CR), run the following command:

      ```
      $ oc get machineset <machineset_name> \
        -n openshift-machine-api -o yaml
      ```

      The following is example output:

      ```
      apiVersion: machine.openshift.io/v1beta1
      kind: MachineSet
      metadata:
        labels:
          machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        name: <infrastructure_id>-<role>
        namespace: openshift-machine-api
      spec:
        replicas: 1
        selector:
          matchLabels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
            machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
        template:
          metadata:
            labels:
              machine.openshift.io/cluster-api-cluster: <infrastructure_id>
              machine.openshift.io/cluster-api-machine-role: <role>
              machine.openshift.io/cluster-api-machine-type: <role>
              machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
          spec:
            providerSpec:
              ...
      ```

      where:

      `metadata.labels.machine.openshift.io/cluster-api-cluster`
      :   Specifies the cluster infrastructure ID.

      `metadata.labels.name`
      :   Specifies a default node label.

          Note

          For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines.

      `spec.template.metadata.spec.providerSpec`
      :   Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider.
3. Create a `MachineSet` CR by running the following command:

   ```
   $ oc create -f <file_name>.yaml
   ```

**Verification**

* View the list of compute machine sets by running the following command:

  ```
  $ oc get machineset -n openshift-machine-api
  ```

  The following is example output:

  ```
  NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
  agl030519-vplxk-infra-us-east-1a    1         1         1       1           11m
  agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1d   0         0                             55m
  agl030519-vplxk-worker-us-east-1e   0         0                             55m
  agl030519-vplxk-worker-us-east-1f   0         0                             55m
  ```

  When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

### [6.4. Creating a Windows MachineSet object on Nutanix](#creating-windows-machineset-nutanix) Copy linkLink copied to clipboard!

You can use a `MachineSet` custom resource (CR) to add a Windows compute node to your Nutanix cluster, where you can run Windows container workloads.

For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines. For more information about machine sets, see "Overview of machine management".

#### [6.4.1. Prerequisites](#prerequisites_creating-windows-machineset-nutanix) Copy linkLink copied to clipboard!

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a supported Windows Server as the operating system image.
* You added a new DNS entry for the internal API server URL, `api-int.<cluster_name>.<base_domain>`, that points to the external API server URL, `api.<cluster_name>.<base_domain>`. This can be a CNAME or an additional A record.

#### [6.4.2. Sample YAML for a Windows MachineSet object on Nutanix](#windows-machineset-nutanix_creating-windows-machineset-nutanix) Copy linkLink copied to clipboard!

You can define a Windows `MachineSet` object running on Nutanix by creating a YAML file similar to the following example that the Windows Machine Config Operator (WMCO) can react upon.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-windows-worker-<zone>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-windows-worker-<zone>
        machine.openshift.io/os-id: Windows
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1
          bootType: ""
          categories: null
          cluster:
            type: uuid
            uuid: <cluster_uuid>
          credentialsSecret:
            name: nutanix-credentials
          image:
            name: <image_id>
            type: name
          kind: NutanixMachineProviderConfig
          memorySize: 16Gi
          project:
            type: ""
          subnets:
          - type: uuid
            uuid: <subnet_uuid>
          systemDiskSize: 120Gi
          userDataSecret:
            name: windows-user-data
          vcpuSockets: 4
          vcpusPerSocket: 1
```

where:

`metadata.labels.machine.openshift.io/cluster-api-cluster`
:   Replace `<infrastructure_id>` with the infrastructure ID. You can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`metadata.name`
:   Replace the infrastructure ID, worker label, and zone.

`spec.selector.matchLabels`
:   Replace the parameters for the following labels:

    * `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
    * `machine.openshift.io/cluster-api-machineset`. Replace the infrastructure ID, worker label, and zone.

`spec.template.metadata.labels`
:   Replace the parameters for the following labels:

    * `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
    * `machine.openshift.io/cluster-api-machineset`. Replace the infrastructure ID, worker label, and zone.
    * `machine.openshift.io/os-id: Windows`. When set to `Windows`, configures the compute machine set as a Windows machine.

`spec.template.spec.metadata.labels`
:   When set to `node-role.kubernetes.io/worker`, configures the node as a compute machine.

`spec.template.spec.providerSpec`
:   Specify the following parameters:

    * `value.bootType`. Specifies the boot type that the compute machines use. Valid values are `Legacy`, `SecureBoot`, or `UEFI`. The default is `Legacy`. For more information about boot types, see "Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment (Nutanix documentaiton)" in the *Additional resources* section.

      Note

      You must use the `Legacy` boot type in OpenShift Container Platform 4.22.
    * `value.cluster`. Specifies a Nutanix Prism Element cluster configuration. In this example, the cluster type is `uuid`, so there is a `uuid` stanza. Replace `<cluster_uuid>` with the cluster UUID.
    * `value.credentialsSecret.name`. Specifies the secret name for the cluster. Do not change this value.
    * `value.image`. Specifies the image to use. Replace `<image_id>` with an image from an existing default compute machine set for the cluster, one of the following options:

      + `nutanix-windows-server-2022` for Windows Server 2022
      + `nutanix-windows-server-2025` for Windows Server 2025
    * `value.kind`. Specifies the cloud provider platform type. Do not change this value.
    * `value.memorySize`. Specifies the amount of memory for the cluster in Gi.
    * `value.subnets`. Specifies a subnet configuration. In this example, the subnet type is `uuid`, so there is a `uuid` stanza. Replace `<subnet_uuid>` with the subnet UUID.
    * `value.systemDiskSize`. Specifies the size of the system disk in Gi.
    * `value.userDataSecret.name`. Specifies the name of the secret in the user data YAML file that is in the `openshift-machine-api` namespace. Use the value that installation program populates in the default compute machine set.
    * `value.vcpuSockets`. Specifies the number of vCPU sockets.
    * `value.vcpusPerSocket`. Specifies the number of vCPUs per socket.

#### [6.4.3. Creating a compute machine set](#machineset-creating_creating-windows-machineset-nutanix) Copy linkLink copied to clipboard!

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

**Prerequisites**

* Deploy an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.

**Procedure**

1. Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.

   Ensure that you set the `<clusterID>` and `<role>` parameter values.
2. Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster.

   1. To list the compute machine sets in your cluster, run the following command:

      ```
      $ oc get machinesets -n openshift-machine-api
      ```

      The following is example output:

      ```
      NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
      agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1d   0         0                             55m
      agl030519-vplxk-worker-us-east-1e   0         0                             55m
      agl030519-vplxk-worker-us-east-1f   0         0                             55m
      ```
   2. To view values of a specific compute machine set custom resource (CR), run the following command:

      ```
      $ oc get machineset <machineset_name> \
        -n openshift-machine-api -o yaml
      ```

      The following is example output:

      ```
      apiVersion: machine.openshift.io/v1beta1
      kind: MachineSet
      metadata:
        labels:
          machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        name: <infrastructure_id>-<role>
        namespace: openshift-machine-api
      spec:
        replicas: 1
        selector:
          matchLabels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
            machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
        template:
          metadata:
            labels:
              machine.openshift.io/cluster-api-cluster: <infrastructure_id>
              machine.openshift.io/cluster-api-machine-role: <role>
              machine.openshift.io/cluster-api-machine-type: <role>
              machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
          spec:
            providerSpec:
              ...
      ```

      where:

      `metadata.labels.machine.openshift.io/cluster-api-cluster`
      :   Specifies the cluster infrastructure ID.

      `metadata.labels.name`
      :   Specifies a default node label.

          Note

          For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines.

      `spec.template.metadata.spec.providerSpec`
      :   Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider.
3. Create a `MachineSet` CR by running the following command:

   ```
   $ oc create -f <file_name>.yaml
   ```

**Verification**

* View the list of compute machine sets by running the following command:

  ```
  $ oc get machineset -n openshift-machine-api
  ```

  The following is example output:

  ```
  NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
  agl030519-vplxk-infra-us-east-1a    1         1         1       1           11m
  agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1d   0         0                             55m
  agl030519-vplxk-worker-us-east-1e   0         0                             55m
  agl030519-vplxk-worker-us-east-1f   0         0                             55m
  ```

  When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

### [6.5. Creating a Windows machine set on vSphere](#creating-windows-machineset-vsphere) Copy linkLink copied to clipboard!

You can use a `MachineSet` custom resource (CR) to add a Windows compute node to your VMware vSphere cluster, where you can run Windows container workloads.

For example, you might create infrastructure Windows machine sets and related machines so that you can move supporting Windows workloads to the new Windows machines. For more information about machine sets, see "Overview of machine management" in the *Additional resources* section.

#### [6.5.1. Prerequisites](#prerequisites_creating-windows-machineset-vsphere) Copy linkLink copied to clipboard!

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a supported Windows Server as the operating system image.
* You must prepare your vSphere environment for Windows container workloads by creating the vSphere Windows VM golden image. See "Creating the vSphere Windows VM golden image" in this section.
* You must enable communication with the internal API server for the WMCO. See "Enabling communication with the internal API server for the WMCO on vSphere" in this section.

#### [6.5.2. Creating the vSphere Windows VM golden image](#creating-the-vsphere-windows-vm-golden-image_creating-windows-machineset-vsphere) Copy linkLink copied to clipboard!

You must prepare your vSphere environment for Windows container workloads by creating the vSphere Windows VM golden image.

**Prerequisites**

* You have created a private/public key pair, which is used to configure key-based authentication in the OpenSSH server. The private key must be configured in the Windows Machine Config Operator (WMCO) namespace so that the WMCO can communicate with the Windows VM.

  If you created the key pair on a Red Hat Enterprise Linux (RHEL) system, before you can use the public key on a Windows system, make sure the public key is saved using ASCII encoding. For example, the following PowerShell command copies a public key, encoding it for the ASCII character set:

  ```
  C:\> echo "ssh-rsa <ssh_pub_key>" | Out-File <ssh_key_path> -Encoding ascii
  ```

  where:

  `<ssh_pub_key>`
  :   Specifies the SSH public key used to access the cluster.

  `<ssh_key_path>`
  :   Specifies the path to the SSH public key.

  See the "Configuring a secret for the Windows Machine Config Operator" section for more details.

Note

You must use [Microsoft PowerShell](https://docs.microsoft.com/en-us/powershell/scripting/install/installing-powershell) commands in several cases when creating your Windows VM. PowerShell commands in this guide are distinguished by the `PS C:\>` prefix.

**Procedure**

1. Select a compatible Windows Server version. Currently, the Windows Machine Config Operator (WMCO) stable version supports the following versions:

   * Windows Server 2025 Long-Term Servicing Channel
   * Windows Server 2022 Long-Term Servicing Channel with the OS-level container networking patch [KB5012637, Microsoft Windows documentation](https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d).
2. Create a new VM in the vSphere client using the VM golden image with a compatible Windows Server version. For more information about compatible versions, see the "Windows Machine Config Operator prerequisites" section of the "Red Hat OpenShift support for Windows Containers release notes."

   Important

   The virtual hardware version for your VM must meet the infrastructure requirements for OpenShift Container Platform. For more information, see the "VMware vSphere infrastructure requirements" section in the OpenShift Container Platform documentation. Also, you can refer to VMware’s documentation on [virtual machine hardware versions](https://kb.vmware.com/s/article/1003746).
3. Install and configure VMware Tools version 11.0.6 or greater on the Windows VM. See the [VMware Tools documentation](https://docs.vmware.com/en/VMware-Tools/index.html) for more information.
4. After installing VMware Tools on the Windows VM, verify the following:

   1. The `C:\ProgramData\VMware\VMware Tools\tools.conf` file exists with the following entry:

      ```
      exclude-nics=
      ```

      If the `tools.conf` file does not exist, create it with the `exclude-nics` option uncommented and set as an empty value.

      This entry ensures the cloned vNIC generated on the Windows VM by the hybrid-overlay is not ignored.
   2. The Windows VM has a valid IP address in vCenter:

      ```
      C:\> ipconfig
      ```
   3. The VMTools Windows service is running:

      ```
      PS C:\> Get-Service -Name VMTools | Select Status, StartType
      ```
5. Install and configure the OpenSSH Server on the Windows VM. See Microsoft’s documentation on [installing OpenSSH](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse) for more details.
6. Set up SSH access for an administrative user. See Microsoft’s documentation on the [Administrative user](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement#administrative-user) to do this.

   Important

   The public key used in the instructions must correspond to the private key you create later in the WMCO namespace that holds your secret. See the "Configuring a secret for the Windows Machine Config Operator" section for more details.
7. You must create a new firewall rule in the Windows VM that allows incoming connections for container logs. Run the following PowerShell command to create the firewall rule on TCP port 10250:

   ```
   PS C:\> New-NetFirewallRule -DisplayName "ContainerLogsPort" -LocalPort 10250 -Enabled True -Direction Inbound -Protocol TCP -Action Allow -EdgeTraversalPolicy Allow
   ```
8. Clone the Windows VM so it is a reusable image. Follow the VMware documentation on how to [clone an existing virtual machine](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-1E185A80-0B97-4B46-A32B-3EF8F309BEED.html) for more details.
9. In the cloned Windows VM, run the [Windows Sysprep tool](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation):

   ```
   C:\> C:\Windows\System32\Sysprep\sysprep.exe /generalize /oobe /shutdown /unattend:<path_to_unattend.xml>
   ```

   Replace `<path_to_unattend.xml>` with the path to your `unattend.xml` file.

   Note

   There is a limit on how many times you can run the `sysprep` command on a Windows image. Consult Microsoft’s [documentation](https://docs.microsoft.com/en-us/windows-hardware/manufacture/desktop/sysprep--generalize--a-windows-installation#limits-on-how-many-times-you-can-run-sysprep) for more information.

   An example `unattend.xml` is provided, which maintains all the changes needed for the WMCO. You must modify this example; it cannot be used directly.

   **Example `unattend.xml`**

   ```
   <?xml version="1.0" encoding="UTF-8"?>
   <unattend xmlns="urn:schemas-microsoft-com:unattend">
      <settings pass="specialize">
         <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-International-Core" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
            <InputLocale>0409:00000409</InputLocale>
            <SystemLocale>en-US</SystemLocale>
            <UILanguage>en-US</UILanguage>
            <UILanguageFallback>en-US</UILanguageFallback>
            <UserLocale>en-US</UserLocale>
         </component>
         <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-Security-SPP-UX" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
            <SkipAutoActivation>true</SkipAutoActivation>
         </component>
         <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-SQMApi" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
            <CEIPEnabled>0</CEIPEnabled>
         </component>
         <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
            <ComputerName>winhost</ComputerName>
         </component>
      </settings>
      <settings pass="oobeSystem">
         <component xmlns:wcm="http://schemas.microsoft.com/WMIConfig/2002/State" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" name="Microsoft-Windows-Shell-Setup" processorArchitecture="amd64" publicKeyToken="31bf3856ad364e35" language="neutral" versionScope="nonSxS">
            <AutoLogon>
               <Enabled>false</Enabled>
            </AutoLogon>
            <OOBE>
               <HideEULAPage>true</HideEULAPage>
               <HideLocalAccountScreen>true</HideLocalAccountScreen>
               <HideOEMRegistrationScreen>true</HideOEMRegistrationScreen>
               <HideOnlineAccountScreens>true</HideOnlineAccountScreens>
               <HideWirelessSetupInOOBE>true</HideWirelessSetupInOOBE>
               <NetworkLocation>Work</NetworkLocation>
               <ProtectYourPC>1</ProtectYourPC>
               <SkipMachineOOBE>true</SkipMachineOOBE>
               <SkipUserOOBE>true</SkipUserOOBE>
            </OOBE>
            <RegisteredOrganization>Organization</RegisteredOrganization>
            <RegisteredOwner>Owner</RegisteredOwner>
            <DisableAutoDaylightTimeSet>false</DisableAutoDaylightTimeSet>
            <TimeZone>Eastern Standard Time</TimeZone>
            <UserAccounts>
               <AdministratorPassword>
                  <Value>MyPassword</Value>
                  <PlainText>true</PlainText>
               </AdministratorPassword>
            </UserAccounts>
         </component>
      </settings>
   </unattend>
   ```

   where:

   `<ComputerName>`
   :   Replace the `winhost` placeholder with a computer name, which must follow the Kubernetes' names specification. These specifications also apply to Guest OS customization performed on the resulting template while creating new VMs. For more information, see "Object Names and IDs specification (Kubernetes documentation)".

   `<AutoLogon>.<Enabled>`
   :   When `false`, automatic logon is disabled to avoid the security issue of leaving an open terminal with Administrator privileges at boot. This is the default value and must not be changed.

   `<UserAccounts>.<AdministratorPassword>.<Value>`
   :   Replace the `MyPassword` placeholder with the password for the Administrator account. This prevents the built-in Administrator account from having a blank password by default. Follow Microsoft’s best practices for choosing a password. For more information on Microsoft’s best practices, see "Password must meet complexity requirements (Microsoft documentation)".

       After the Sysprep tool has completed, the Windows VM will power off. You must not use or power on this VM anymore.
10. Convert the Windows VM to a template in vCenter. For more information, see "vSphere Virtual Machine Administration (vSphere documentation)".

#### [6.5.3. Enabling communication with the internal API server for the WMCO on vSphere](#enabling-internal-api-server-vsphere_creating-windows-machineset-vsphere) Copy linkLink copied to clipboard!

You must enable communication with the internal API server so that your Windows virtual machine (VM) can download the Ignition config files, and the kubelet on the configured VM can only communicate with the internal API server.

The Windows Machine Config Operator (WMCO) can download the Ignition config files from the internal API server endpoint only after communication with the server is enabled.

**Prerequisites**

* You have installed a cluster on vSphere.

**Procedure**

* Add a new DNS entry for `api-int.<cluster_name>.<base_domain>` that points to the external API server URL `api.<cluster_name>.<base_domain>`. This can be a CNAME or an additional A record.

  Note

  The external API endpoint was already created as part of the initial cluster installation on vSphere.

#### [6.5.4. Sample YAML for a Windows MachineSet object on vSphere](#windows-machineset-vsphere_creating-windows-machineset-vsphere) Copy linkLink copied to clipboard!

You can define a Windows `MachineSet` object running on VMware vSphere by creating a YAML file similar to the following example, which the Windows Machine Config Operator (WMCO) can react upon.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <windows_machine_set_name>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <windows_machine_set_name>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: worker
        machine.openshift.io/cluster-api-machine-type: worker
        machine.openshift.io/cluster-api-machineset: <windows_machine_set_name>
        machine.openshift.io/os-id: Windows
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/worker: ""
      providerSpec:
        value:
          apiVersion: vsphereprovider.openshift.io/v1beta1
          credentialsSecret:
            name: vsphere-cloud-credentials
          diskGiB: 128
          kind: VSphereMachineProviderSpec
          memoryMiB: 16384
          network:
            devices:
            - networkName: "<vm_network_name>"
          numCPUs: 4
          numCoresPerSocket: 1
          snapshot: ""
          template: <windows_vm_template_name>
          userDataSecret:
            name: windows-user-data
          workspace:
             datacenter: <vcenter_data_center_name>
             datastore: <vcenter_datastore_name>
             folder: <vcenter_vm_folder_path>
             resourcePool: <vsphere_resource_pool>
             server: <vcenter_server_ip>
```

where:

`metadata.labels`
:   For the `machine.openshift.io/cluster-api-cluster` label, replace `<infrastructure_id>` with the infrastructure ID. You can obtain the infrastructure ID by running the following command: Specify the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`metadata.name`
:   Replace the infrastructure ID, worker label, and zone.

`spec.selector.matchLabels`
:   Replace the parameters for the following labels:

    * `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
    * `machine.openshift.io/cluster-api-machineset`. Specify the Windows compute machine set name. The compute machine set name cannot be more than 9 characters long, due to the way machine names are generated in vSphere.

`spec.template.metadata.labels`
:   Replace the parameters for the following labels:

    * `machine.openshift.io/cluster-api-cluster`. Replace the infrastructure ID.
    * `machine.openshift.io/cluster-api-machineset`. Specify the Windows compute machine set name. The compute machine set name cannot be more than 9 characters long, due to the way machine names are generated in vSphere.
    * `machine.openshift.io/os-id: Windows`. When set to `Windows`, configures the compute machine set as a Windows machine.

`spec.template.spec.metadata.labels`
:   When set to `node-role.kubernetes.io/worker`, configures the node as a compute machine.

`spec.template.spec.providerSpec`
:   Specify the following parameters:

    * `value.diskGiB`. Specifies the size of the vSphere Virtual Machine Disk (VMDK).

      Note

      This parameter does not set the size of the Windows partition. You can resize the Windows partition by using the `unattend.xml` file or by creating the vSphere Windows virtual machine (VM) golden image with the required disk size.
    * `value.network.devices.networkName`. Specifies the vSphere VM network to deploy the compute machine set to. This VM network must be where other Linux compute machines reside in the cluster.
    * `value.template`. Specifies the full path of the Windows vSphere VM template to use, such as `golden-images/windows-server-template`. The name must be unique.

      Important

      Do not specify the original VM template. The VM template must remain off and must be cloned for new Windows machines. Starting the VM template configures the VM template as a VM on the platform, which prevents it from being used as a template that compute machine sets can apply configurations to.
    * `value.userDataSecret.name`. The `windows-user-data` is created by the WMCO when the first Windows machine is configured. After that, the `windows-user-data` is available for all subsequent compute machine sets to consume.
    * `value.workspace.datacenter`. Specifies the vCenter data center to deploy the compute machine set on.
    * `value.workspace.datastore`. Specifies the vCenter datastore to deploy the compute machine set on.
    * `value.workspace.folder`. Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`.
    * `value.workspace.resourcePool`. Specifies the vSphere resource pool for your Windows VMs. This parameter is optional.
    * `value.workspace.server`. Specifies the vCenter server IP or fully qualified domain name. This parameter is optional.

#### [6.5.5. Creating a compute machine set](#machineset-creating_creating-windows-machineset-vsphere) Copy linkLink copied to clipboard!

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

**Prerequisites**

* Deploy an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.
* In disconnected environments, the image specified in the `MachineSet` custom resource (CR) must have the [OpenSSH server v0.0.1.0 installed](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_install_firstuse?tabs=powershell#install-openssh-for-windows).

**Procedure**

1. Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.

   Ensure that you set the `<clusterID>` and `<role>` parameter values.
2. Optional: If you are not sure which value to set for a specific field, you can check an existing compute machine set from your cluster.

   1. To list the compute machine sets in your cluster, run the following command:

      ```
      $ oc get machinesets -n openshift-machine-api
      ```

      The following is example output:

      ```
      NAME                                DESIRED   CURRENT   READY   AVAILABLE   AGE
      agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1c   1         1         1       1           55m
      agl030519-vplxk-worker-us-east-1d   0         0                             55m
      agl030519-vplxk-worker-us-east-1e   0         0                             55m
      agl030519-vplxk-worker-us-east-1f   0         0                             55m
      ```
   2. To view values of a specific compute machine set custom resource (CR), run the following command:

      ```
      $ oc get machineset <machineset_name> \
        -n openshift-machine-api -o yaml
      ```

      The following is example output:

      ```
      apiVersion: machine.openshift.io/v1beta1
      kind: MachineSet
      metadata:
        labels:
          machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        name: <infrastructure_id>-<role>
        namespace: openshift-machine-api
      spec:
        replicas: 1
        selector:
          matchLabels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
            machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
        template:
          metadata:
            labels:
              machine.openshift.io/cluster-api-cluster: <infrastructure_id>
              machine.openshift.io/cluster-api-machine-role: <role>
              machine.openshift.io/cluster-api-machine-type: <role>
              machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
          spec:
            providerSpec:
              ...
      ```

      where:

      `metadata.labels.machine.openshift.io/cluster-api-cluster`
      :   Specifies the cluster infrastructure ID.

      `metadata.labels.name`
      :   Specifies a default node label.

          Note

          For clusters that have user-provisioned infrastructure, a compute machine set can only create `worker` and `infra` type machines.

      `spec.template.metadata.spec.providerSpec`
      :   Specifies the values of the compute machine set CR. The values are platform-specific. For more information about `<providerSpec>` parameters in the CR, see the sample compute machine set CR configuration for your provider.
3. Create a `MachineSet` CR by running the following command:

   ```
   $ oc create -f <file_name>.yaml
   ```

**Verification**

* View the list of compute machine sets by running the following command:

  ```
  $ oc get machineset -n openshift-machine-api
  ```

  The following is example output:

  ```
  NAME                                       DESIRED   CURRENT   READY   AVAILABLE   AGE
  agl030519-vplxk-windows-worker-us-east-1a  1         1         1       1           11m
  agl030519-vplxk-worker-us-east-1a          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1b          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1c          1         1         1       1           55m
  agl030519-vplxk-worker-us-east-1d          0         0                             55m
  agl030519-vplxk-worker-us-east-1e          0         0                             55m
  agl030519-vplxk-worker-us-east-1f          0         0                             55m
  ```

  When the new compute machine set is available, the `DESIRED` and `CURRENT` values match. If the compute machine set is not available, wait a few minutes and run the command again.

## [Chapter 7. Scheduling Windows container workloads](#scheduling-windows-workloads) Copy linkLink copied to clipboard!

You can use the Windows Machine Config Operator (WMCO) to schedule Windows workloads to Windows compute nodes.

### [7.1. Prerequisites](#prerequisites-2) Copy linkLink copied to clipboard!

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You are using a Windows container as the OS image.
* You have created a Windows compute machine set.

### [7.2. Windows pod placement](#windows-pod-placement_scheduling-windows-workloads) Copy linkLink copied to clipboard!

Before deploying your Windows workloads to the cluster, you must configure your Windows node scheduling so pods are assigned correctly.

The machine hosting your Windows node is managed the same as a Linux-based node. Likewise, scheduling a Windows pod to the appropriate Windows node is completed similarly, using mechanisms like taints, tolerations, and node selectors.

With multiple operating systems, and the ability to run multiple Windows OS variants in the same cluster, you must map your Windows pods to a base Windows OS variant by using a `RuntimeClass` object. For example, if you have multiple Windows nodes running on different Windows Server container versions, the cluster could schedule your Windows pods to an incompatible Windows OS variant. You must have `RuntimeClass` objects configured for each Windows OS variant on your cluster. Using a `RuntimeClass` object is also recommended if you have only one Windows OS variant available in your cluster.

For more information, see "Host and container version compatibility" in the Microsoft Windows documentation.

Also, it is recommended that you set the `spec.os.name.windows` parameter in your workload pods. The Windows Machine Config Operator (WMCO) uses this field to authoritatively identify the pod operating system for validation and is used to enforce Windows-specific pod security context constraints (SCCs). Currently, this parameter has no effect on pod scheduling. For more information about this parameter, see the Kubernetes Pod OS documentation.

Important

The container base image must be the same Windows OS version and build number that is running on the node where the conainer is to be scheduled.

Also, if you upgrade the Windows nodes from one version to another, for example going from 2022 to 2025, you must upgrade your container base image to match the new version. For more information, see Windows container version compatibility in the Microsoft Windows documentation.

### [7.3. Creating a RuntimeClass object to encapsulate scheduling mechanisms](#creating-runtimeclass_scheduling-windows-workloads) Copy linkLink copied to clipboard!

To deploy Windows workloads, you must create a `RuntimeClass` object to map your Windows pods to a base Windows OS variant.

Using a `RuntimeClass` object simplifies the use of scheduling mechanisms like taints and tolerations; you deploy a runtime class that encapsulates your taints and tolerations and then apply it to your pods to schedule them to the appropriate node.

Creating a runtime class is also necessary in clusters that support multiple operating system variants.

**Procedure**

1. Create a `RuntimeClass` object YAML file. For example, `runtime-class.yaml`:

   ```
   apiVersion: node.k8s.io/v1
   kind: RuntimeClass
   metadata:
     name: windows2025
   handler: 'runhcs-wcow-process'
   scheduling:
     nodeSelector:
       kubernetes.io/os: 'windows'
       kubernetes.io/arch: 'amd64'
       node.kubernetes.io/windows-build: '10.0.26100'
     tolerations:
     - effect: NoSchedule
       key: os
       operator: Equal
       value: "windows"
     - effect: NoSchedule
       key: os
       operator: Equal
       value: "Windows"
   ```

   where:

   `metadata.name`
   :   Specifies the `RuntimeClass` object name, which is defined in the pods you want to be managed by this runtime class.

   `scheduling.nodeSelector`
   :   Specifies labels that must be present on nodes that support this runtime class. Pods using this runtime class can only be scheduled to a node matched by this selector. The node selector of the runtime class is merged with the existing node selector of the pod. Any conflicts prevent the pod from being scheduled to the node.

       * For Windows 2025, specify the `node.kubernetes.io/windows-build: '10.0.26100'` label.
       * For Windows 2022, specify the `node.kubernetes.io/windows-build: '10.0.20348'` label.
       * For Windows 2019, specify the `node.kubernetes.io/windows-build: '10.0.17763'` label.

   `scheduling.tolerations`
   :   Specifies tolerations to append to pods, excluding duplicates, running with this runtime class during admission. This combines the set of nodes tolerated by the pod and the runtime class.
2. Create the `RuntimeClass` object:

   ```
   $ oc create -f <file-name>.yaml
   ```

   For example:

   ```
   $ oc create -f runtime-class.yaml
   ```
3. Apply the `RuntimeClass` object to your pod to ensure it is scheduled to the appropriate operating system variant:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: my-windows-pod
   spec:
     runtimeClassName: windows2025
   # ...
   ```

   where:

   `spec.runtimeClassName`
   :   Specifies the runtime class to manage the scheduling of your pod.

### [7.4. Sample Windows container workload deployment](#sample-windows-workload-deployment_scheduling-windows-workloads) Copy linkLink copied to clipboard!

You can deploy Windows container workloads to your cluster after you have a Windows compute node available.

Note

This sample deployment is provided for reference only.

**Example `Service` object**

```
apiVersion: v1
kind: Service
metadata:
  name: win-webserver
  labels:
    app: win-webserver
spec:
  ports:
    # the port that this service should serve on
  - port: 80
    targetPort: 80
  selector:
    app: win-webserver
  type: LoadBalancer
```

**Example `Deployment` object**

```
apiVersion: apps/v1
kind: Deployment
metadata:
  labels:
    app: win-webserver
  name: win-webserver
spec:
  selector:
    matchLabels:
      app: win-webserver
  replicas: 1
  template:
    metadata:
      labels:
        app: win-webserver
      name: win-webserver
    spec:
      containers:
      - name: windowswebserver
        image: mcr.microsoft.com/windows/servercore:ltsc2025
        imagePullPolicy: IfNotPresent
        command:
        - powershell.exe
        - -command
        - $listener = New-Object System.Net.HttpListener; $listener.Prefixes.Add('http://*:80/'); $listener.Start();Write-Host('Listening at http://*:80/'); while ($listener.IsListening) { $context = $listener.GetContext(); $response = $context.Response; $content='<html><body><H1>Red Hat OpenShift + Windows Container Workloads</H1></body></html>'; $buffer = [System.Text.Encoding]::UTF8.GetBytes($content); $response.ContentLength64 = $buffer.Length; $response.OutputStream.Write($buffer, 0, $buffer.Length); $response.Close(); };
        securityContext:
          runAsNonRoot: false
          windowsOptions:
            runAsUserName: "ContainerAdministrator"
      os:
        name: "windows"
      runtimeClassName: windows2025
```

where:

`spec.template.spec.containers.image`
:   Specifies the container image to use: `mcr.microsoft.com/powershell:<tag>` or `mcr.microsoft.com/windows/servercore:<tag>`. The container image must match the Windows version running on the node.

    * For Windows 2025, use the `ltsc2025` tag.
    * For Windows 2022, use the `ltsc2022` tag.
    * For Windows 2019, use the `ltsc2019` tag.

`spec.template.spec.containers.command`
:   Specifies the commands to execute on the container.

    * For the `mcr.microsoft.com/powershell:<tag>` container image, you must define the command as `pwsh.exe`.
    * For the `mcr.microsoft.com/windows/servercore:<tag>` container image, you must define the command as `powershell.exe`.

`spec.template.spec.runtimeClassName`
:   Specifies the runtime class you created for the Windows operating system variant on your cluster.

### [7.5. Support for Windows CSI drivers](#wmco-supported-csi-drivers_scheduling-windows-workloads) Copy linkLink copied to clipboard!

You can use the CSI PROXY plug-in to perform storage operations on the nodes in your cluster.

Red Hat OpenShift support for Windows Containers installs CSI Proxy, which is a plug-in that enables CSI drivers for performing storage operations, on all Windows nodes in the cluster. For more information, see "CSI Proxy".

To use persistent storage with Windows workloads, you must deploy a specific Windows CSI driver daemon set, as described in your storage provider’s documentation. By default, the WMCO does not automatically create the Windows CSI driver daemon set. For more information, see the list of production drivers in the Kubernetes CSI Developer Documentation.

Note

Red Hat does not provide support for the third-party production drivers listed in the Kubernetes CSI Developer Documentation.

### [7.6. Scaling a compute machine set manually](#machineset-manually-scaling_scheduling-windows-workloads) Copy linkLink copied to clipboard!

To add or remove an instance of a machine in a compute machine set, you can manually scale the compute machine set.

This guidance is relevant to fully automated, installer-provisioned infrastructure installations. Customized, user-provisioned infrastructure installations do not have compute machine sets.

**Prerequisites**

* Install an OpenShift Container Platform cluster and the `oc` command line.
* Log in to `oc` as a user with `cluster-admin` permission.

**Procedure**

1. View the compute machine sets that are in the cluster by running the following command:

   ```
   $ oc get machinesets.machine.openshift.io -n openshift-machine-api
   ```

   The compute machine sets are listed in the form of `<clusterid>-worker-<aws-region-az>`.
2. View the compute machines that are in the cluster by running the following command:

   ```
   $ oc get machines.machine.openshift.io -n openshift-machine-api
   ```
3. Set the annotation on the compute machine that you want to delete by running the following command:

   ```
   $ oc annotate machines.machine.openshift.io/<machine_name> -n openshift-machine-api machine.openshift.io/delete-machine="true"
   ```
4. Scale the compute machine set by running one of the following commands:

   ```
   $ oc scale --replicas=2 machinesets.machine.openshift.io <machineset> -n openshift-machine-api
   ```

   Or:

   ```
   $ oc edit machinesets.machine.openshift.io <machineset> -n openshift-machine-api
   ```

   Tip

   You can alternatively apply the following YAML to scale the compute machine set:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   metadata:
     name: <machineset>
     namespace: openshift-machine-api
   spec:
     replicas: 2
   ```

   You can scale the compute machine set up or down. It takes several minutes for the new machines to be available.

   Important

   By default, the machine controller tries to drain the node that is backed by the machine until it succeeds. In some situations, such as with a misconfigured pod disruption budget, the drain operation might not be able to succeed. If the drain operation fails, the machine controller cannot proceed removing the machine.

   You can skip draining the node by annotating `machine.openshift.io/exclude-node-draining` in a specific machine.

**Verification**

* Verify the deletion of the intended machine by running the following command:

  ```
  $ oc get machines.machine.openshift.io
  ```

## [Chapter 8. Windows node updates](#windows-node-upgrades) Copy linkLink copied to clipboard!

You can ensure your Windows nodes have the latest updates by updating the Windows Machine Config Operator (WMCO).

You can update the WMCO in any of the following scenarios:

* Within the current version. for example, from <10.y.z> to <10.y.z+1>.
* To a new, contiguous version. For example, from <10.y> to <10.y+1>.
* From an EUS version to another EUS version by using a Control Plane Only update. For example, from <10.y> to <10.y+2>.

### [8.1. Windows Machine Config Operator updates](#wmco-upgrades_windows-node-upgrades) Copy linkLink copied to clipboard!

When a new version of the Windows Machine Config Operator (WMCO) is released that is compatible with the current cluster version, the Operator is updated based on the update channel and subscription approval strategy it was installed with when using the Operator Lifecycle Manager (OLM).

The WMCO update results in the Kubernetes components in the Windows machine being updated.

Note

If you are updating to a new version of the WMCO and want to use cluster monitoring, you must have the `openshift.io/cluster-monitoring=true` label present in the WMCO namespace. If you add the label to a pre-existing WMCO namespace, and there are already Windows nodes configured, restart the WMCO pod to allow monitoring graphs to display.

For a non-disruptive update, the WMCO terminates the Windows machines configured by the previous version of the WMCO and recreates them using the current version. This is done by deleting the `Machine` object, which results in the drain and deletion of the Windows node. To facilitate an update, the WMCO adds a version annotation to all the configured nodes. During an update, a mismatch in version annotation results in the deletion and recreation of a Windows machine. To have minimal service disruptions during an update, the WMCO only updates one Windows machine at a time.

After the update, it is recommended that you set the `spec.os.name.windows` parameter in your workload pods. The WMCO uses this field to authoritatively identify the pod operating system for validation and is used to enforce Windows-specific pod security context constraints (SCCs).

Important

The WMCO is only responsible for updating Kubernetes components, not for Windows operating system updates. You provide the Windows image when creating the VMs; therefore, you are responsible for providing an updated image. You can provide an updated Windows image by changing the image configuration in the `MachineSet` spec.

### [8.2. Windows Machine Config Operator Control Plane Only update](#wmco-upgrades-eus_windows-node-upgrades) Copy linkLink copied to clipboard!

You can use the **Control Plane Only** process to update the OpenShift Container Platform from one EUS version to another EUS version of OpenShift Container Platform. After you update the cluster, the Windows nodes are updated the new EUS version.

During the update, the Windows workloads are kept in a healthy state with no disruptions.

Important

This update was previously known as an **EUS-to-EUS** update and is now referred to as a **Control Plane Only** update. These updates are only viable between **even-numbered minor versions** of OpenShift Container Platform.

#### [8.2.1. WMCO Control Plane Only update by using the web console](#wmco-upgrades-eus-using-web-console_windows-node-upgrades) Copy linkLink copied to clipboard!

You can use the OpenShift Container Platform web console to perform a Control Plane Only update of the Windows Machine Config Operator (WMCO).

**Prerequisites**

* The cluster must be running on a supported EUS version of OpenShift Container Platform.
* All Windows nodes must be in a healthy state.
* All Windows nodes must be running on the same version of the WMCO.
* All the of the prerequisites of the Control Plane Only update are met, as described in "Performing a Control Plane Only update."

**Procedure**

1. Uninstall WMCO operator by using the following the steps:

   Important

   Delete the Operator only. Do not delete the Windows namespace or any Windows workloads.

   1. Log in to the OpenShift Container Platform web console.
   2. Navigate to **Ecosystem** → **Software Catalog**.
   3. Use the **Filter by keyword** box to search for `Red Hat Windows Machine Config Operator`.
   4. Click the **Red Hat Windows Machine Config Operator** tile. The Operator tile indicates it is installed.
   5. In the **Windows Machine Config Operator** descriptor page, click **Uninstall**.
2. Update OpenShift Container Platform by following the steps in "Performing a Control Plane Only update."
3. Install the new WMCO version by following the steps in "Installing the Windows Machine Config Operator using the web console."

#### [8.2.2. WMCO Control Plane Only update by using the CLI](#wmco-upgrades-eus-using-cli_windows-node-upgrades) Copy linkLink copied to clipboard!

You can use the OpenShift CLI (`oc`) to perform a Control Plane Only update of the Windows Machine Config Operator (WMCO).

**Prerequisites**

* The cluster must be running on a supported EUS version of OpenShift Container Platform.
* All Windows nodes must be in a healthy state.
* All Windows nodes must be running on the same version of the WMCO.
* All the of the prerequisites of the Control Plane Only update are met, as described in "Performing a Control Plane Only update."

**Procedure**

1. Uninstall the WMCO Operator from the cluster by following the steps in "Deleting Operators from a cluster using the CLI."

   Important

   Delete the Operator only. Do not delete the Windows namespace or any Windows workloads.
2. Update OpenShift Container Platform by following the steps in "Performing a Control Plane Only update."
3. Install the new WMCO version by following the steps in "Installing the Windows Machine Config Operator using the CLI."

**Verification**

* On the Verify that the **Status** shows **Succeeded** to confirm successful installation of the WMCO.

## [Chapter 9. Using Bring-Your-Own-Host (BYOH) Windows instances as nodes](#byoh-windows-instance) Copy linkLink copied to clipboard!

You can create Bring-Your-Own-Host (BYOH) Windows instances to bring existing Windows Server VMs into OpenShift Container Platform. By using BYOH Windows instances, you can mitigate major disruptions if a Windows server goes offline.

### [9.1. Configuring a BYOH Windows instance](#configuring-byoh-windows-instance) Copy linkLink copied to clipboard!

To create a Bring-Your-Own-Host (BYOH) Windows instance, you must create a config map in the Windows Machine Config Operator (WMCO) namespace.

**Prerequisites**

Any Windows instances that are to be attached to the cluster as a node must fulfill the following requirements:

* The instance must be on the same network as the Linux worker nodes in the cluster.
* Port 22 must be open and running an SSH server.
* The default shell for the SSH server must be the [Windows Command shell](https://docs.microsoft.com/en-us/windows-server/administration/openssh/openssh_server_configuration#configuring-the-default-shell-for-openssh-in-windows), or `cmd.exe`.
* Port 10250 must be open for log collection.
* An administrator user is present with the [private key used in the secret set as an authorized SSH key](https://learn.microsoft.com/en-us/windows-server/administration/openssh/openssh_keymanagement#configure-key-based-authentication) (Microsoft documentation).
* If you are creating a BYOH Windows instance for an installer-provisioned infrastructure (IPI) AWS cluster, you must add a tag to the AWS instance that matches the `spec.template.spec.value.tag` value in the compute machine set for your worker nodes. For example, `kubernetes.io/cluster/<cluster_id>: owned` or `kubernetes.io/cluster/<cluster_id>: shared`.
* If you are creating a BYOH Windows instance on vSphere, communication with the internal API server must be enabled.
* The hostname of the instance must follow the [RFC 1123](https://datatracker.ietf.org/doc/html/rfc1123) DNS label requirements, which include the following standards:

  + Contains only lowercase alphanumeric characters or '-'.
  + Starts with an alphanumeric character.
  + Ends with an alphanumeric character.

Note

Windows instances deployed by the WMCO are configured with the containerd container runtime. Because the WMCO installs and manages the runtime, it is recommended that you not manually install containerd on nodes.

**Procedure**

1. Create a ConfigMap named `windows-instances` in the WMCO namespace that describes the Windows instances to be added.

   Note

   Format each entry in the config map’s data section by using the address as the key while formatting the value as `username=<username>`.

   **Example config map**

   ```
   kind: ConfigMap
   apiVersion: v1
   metadata:
     name: windows-instances
     namespace: openshift-windows-machine-config-operator
   data:
     10.1.42.1: |-
       username=Administrator
     instance.example.com: |-
       username=core
   ```

   where:

   `data`
   :   Specifies the address that the WMCO uses to reach the instance over SSH, either a DNS name or an IPv4 address. A DNS PTR record must exist for this address. You should use a DNS name with your BYOH instance if your organization uses DHCP to assign IP addresses. If not, you need to update the `windows-instances` ConfigMap whenever the instance is assigned a new IP address.

       Also, specify the user name of the administrator user created in the prerequisites.

### [9.2. Removing BYOH Windows instances](#removing-byoh-windows-instance) Copy linkLink copied to clipboard!

You can remove a Bring-Your-Own-Host (BYOH) instance that is attached to the cluster by deleting the instance’s entry in the BYOH config map. Deleting an instance reverts that instance back to its previous state, before it was added to the cluster.

The removal process does not remove any logs or container runtime artifacts from the instances.

For an instance to be cleanly removed, it must be accessible with the current private key provided to WMCO. For example, to remove the `10.1.42.1` instance from the previous example, the config map would be changed to the following:

```
kind: ConfigMap
apiVersion: v1
metadata:
  name: windows-instances
  namespace: openshift-windows-machine-config-operator
data:
  instance.example.com: |-
    username=core
```

Deleting `windows-instances` is viewed as a request to deconstruct all Windows instances added as nodes.

## [Chapter 10. Removing Windows nodes](#removing-windows-nodes) Copy linkLink copied to clipboard!

You can remove a Windows node by deleting its host Windows machine.

### [10.1. Deleting a specific machine](#machine-delete_removing-windows-nodes) Copy linkLink copied to clipboard!

To remove a machine from your cluster, or restart a machine that is part of a machine set, you can use the OpenShift CLI (`oc`) to delete a specific machine.

Important

Do not delete a control plane machine unless your cluster uses a control plane machine set. If the machine that you delete belongs to a machine set, a new machine is immediately created to satisfy the specified number of replicas.

**Prerequisites**

* Install an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.

**Procedure**

1. View the machines that are in the cluster by running the following command:

   ```
   $ oc get machine -n openshift-machine-api
   ```

   The command output contains a list of machines in the `<clusterid>-<role>-<cloud_region>` format.
2. Identify the machine that you want to delete.
3. Delete the machine by running the following command:

   ```
   $ oc delete machine <machine> -n openshift-machine-api
   ```

   Replace `<machine>` with the name of the machine.

   Important

   By default, the machine controller tries to drain the node that is backed by the machine until it succeeds. In some situations, such as with a misconfigured pod disruption budget, the drain operation might not be able to succeed. If the drain operation fails, the machine controller cannot proceed removing the machine.

   You can skip draining the node by annotating `machine.openshift.io/exclude-node-draining` in a specific machine.

## [Chapter 11. Disabling Windows container workloads](#disabling-windows-container-workloads) Copy linkLink copied to clipboard!

You can disable the capability to run Windows container workloads by uninstalling the Windows Machine Config Operator (WMCO) and deleting the namespace that was added by default when you installed the WMCO.

### [11.1. Uninstalling the Windows Machine Config Operator](#uninstalling-wmco_disabling-windows-container-workloads) Copy linkLink copied to clipboard!

If you want to disable the capability to run Windows container workloads, you can uninstall the Windows Machine Config Operator (WMCO) from your cluster.

**Prerequisites**

* Delete the Windows `Machine` objects hosting your Windows workloads.

**Procedure**

1. From the **Ecosystem** → **Software Catalog** page, use the **Filter by keyword** box to search for `Red Hat Windows Machine Config Operator`.
2. Click the **Red Hat Windows Machine Config Operator** tile. The Operator tile indicates it is installed.
3. In the **Windows Machine Config Operator** descriptor page, click **Uninstall**.

### [11.2. Deleting the Windows Machine Config Operator namespace](#deleting-wmco-namespace_disabling-windows-container-workloads) Copy linkLink copied to clipboard!

If you want to disable the capability to run Windows container workloads, after you uninstall the Windows Machine Config Operator (WMCO), you can delete the namespace that was generated by default for the WMCO.

**Prerequisites**

* The WMCO is removed from your cluster.

**Procedure**

1. Remove all Windows workloads that were created in the `openshift-windows-machine-config-operator` namespace:

   ```
   $ oc delete --all pods --namespace=openshift-windows-machine-config-operator
   ```
2. Verify that all pods in the `openshift-windows-machine-config-operator` namespace are deleted or are reporting a terminating state:

   ```
   $ oc get pods --namespace openshift-windows-machine-config-operator
   ```
3. Delete the `openshift-windows-machine-config-operator` namespace:

   ```
   $ oc delete namespace openshift-windows-machine-config-operator
   ```

## [Chapter 12. Troubleshooting Windows container workloads](#windows-containers-troubleshooting) Copy linkLink copied to clipboard!

You can troubleshoot Windows container workload issues to ensure that your Windows nodes are running correctly in your cluster.

### [12.1. Windows Machine Config Operator does not install](#wmco-does-not-install_windows-containers-troubleshooting) Copy linkLink copied to clipboard!

If you have completed the process of installing the Windows Machine Config Operator (WMCO), but the Operator is stuck in the `InstallWaiting` phase, your issue is likely caused by a networking issue.

The WMCO requires your OpenShift Container Platform cluster to be configured with hybrid networking using OVN-Kubernetes; the WMCO cannot complete the installation process without hybrid networking available. This is necessary to manage nodes on multiple operating systems (OS) and OS variants. This must be completed during the installation of your cluster.

### [12.2. Investigating why Windows Machine does not become compute node](#investigating-why-windows-machine-compute-node_windows-containers-troubleshooting) Copy linkLink copied to clipboard!

There are various reasons why a Windows Machine does not become a compute node. The best way to investigate this problem is to collect the Windows Machine Config Operator (WMCO) logs.

**Prerequisites**

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.

**Procedure**

* Run the following command to collect the WMCO logs:

  ```
  $ oc logs -f deployment/windows-machine-config-operator -n openshift-windows-machine-config-operator
  ```

### [12.3. Accessing a Windows node](#accessing-windows-node_windows-containers-troubleshooting) Copy linkLink copied to clipboard!

Windows nodes cannot be accessed using the `oc debug node` command; the command requires running a privileged pod on the node, which is not yet supported for Windows. Instead, a Windows node can be accessed using a secure shell (SSH) or Remote Desktop Protocol (RDP). An SSH bastion is required for both methods.

#### [12.3.1. Accessing a Windows node using SSH](#accessing-windows-node-using-ssh_windows-containers-troubleshooting) Copy linkLink copied to clipboard!

You can access a Windows node by using a secure shell (SSH).

**Prerequisites**

* You have installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.
* You have added the key used in the `cloud-private-key` secret and the key used when creating the cluster to the ssh-agent. For security reasons, remember to remove the keys from the ssh-agent after use.
* You have connected to the Windows node [using an `ssh-bastion` pod](https://access.redhat.com/solutions/4073041).

**Procedure**

* Access the Windows node by running the following command:

  ```
  $ ssh -t -o StrictHostKeyChecking=no -o ProxyCommand='ssh -A -o StrictHostKeyChecking=no \
      -o ServerAliveInterval=30 -W %h:%p core@$(oc get service --all-namespaces -l run=ssh-bastion \
      -o go-template="{{ with (index (index .items 0).status.loadBalancer.ingress 0) }}{{ or .hostname .ip }}{{end}}")' <username>@<windows_node_internal_ip>
  ```

  where:

  `<username>`
  :   Specifies the cloud provider username, such as `Administrator` for Amazon Web Services (AWS) or `capi` for Microsoft Azure.

  `<windows_node_internal_ip>`
  :   Specifies the internal IP address of the node, which can be discovered by running the following command:

      ```
      $ oc get nodes <node_name> -o jsonpath={.status.addresses[?\(@.type==\"InternalIP\"\)].address}
      ```

#### [12.3.2. Accessing a Windows node using RDP](#accessing-windows-node-using-rdp_windows-containers-troubleshooting) Copy linkLink copied to clipboard!

You can access a Windows node by using a Remote Desktop Protocol (RDP).

**Prerequisites**

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.
* You have added the key used in the `cloud-private-key` secret and the key used when creating the cluster to the ssh-agent. For security reasons, remember to remove the keys from the ssh-agent after use.
* You have connected to the Windows node [using an `ssh-bastion` pod](https://access.redhat.com/solutions/4073041).

**Procedure**

1. Run the following command to set up an SSH tunnel:

   ```
   $ ssh -L 2020:<windows_node_internal_ip>:3389 \
       core@$(oc get service --all-namespaces -l run=ssh-bastion -o go-template="{{ with (index (index .items 0).status.loadBalancer.ingress 0) }}{{ or .hostname .ip }}{{end}}")
   ```

   where:

   `<windows_node_internal_ip>`
   :   Specifies the internal IP address of the node, which can be discovered by running the following command:

       ```
       $ oc get nodes <node_name> -o jsonpath={.status.addresses[?\(@.type==\"InternalIP\"\)].address}
       ```
2. From within the resulting shell, SSH into the Windows node and run the following command to create a password for the user:

   ```
   C:\> net user <username> *
   ```

   Specify the cloud provider user name, such as `Administrator` for AWS or `capi` for Azure. You can now remotely access the Windows node at `localhost:2020` using an RDP client.

### [12.4. Collecting Kubernetes node logs for Windows containers](#collecting-kube-node-logs-windows_windows-containers-troubleshooting) Copy linkLink copied to clipboard!

Windows container logging works differently from Linux container logging; the Kubernetes node logs for Windows workloads are streamed to the `C:\var\logs` directory by default. Therefore, you must gather the Windows node logs from that directory.

**Prerequisites**

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.

**Procedure**

1. To view the logs under all directories in `C:\var\logs`, run the following command:

   ```
   $ oc adm node-logs -l kubernetes.io/os=windows --path= \
       /ip-10-0-138-252.us-east-2.compute.internal containers \
       /ip-10-0-138-252.us-east-2.compute.internal hybrid-overlay \
       /ip-10-0-138-252.us-east-2.compute.internal kube-proxy \
       /ip-10-0-138-252.us-east-2.compute.internal kubelet \
       /ip-10-0-138-252.us-east-2.compute.internal pods
   ```
2. You can now list files in the directories using the same command and view the individual log files. For example, to view the kubelet logs, run the following command:

   ```
   $ oc adm node-logs -l kubernetes.io/os=windows --path=/kubelet/kubelet.log
   ```

### [12.5. Collecting Windows application event logs](#collecting-windows-application-event-logs_windows-containers-troubleshooting) Copy linkLink copied to clipboard!

The `Get-WinEvent` shim on the kubelet `logs` endpoint can be used to collect application event logs from Windows machines.

**Prerequisites**

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.

**Procedure**

* To view logs from all applications logging to the event logs on the Windows machine, run:

  ```
  $ oc adm node-logs -l kubernetes.io/os=windows --path=journal
  ```

  The same command is executed when collecting logs with `oc adm must-gather`.

  Other Windows application logs from the event log can also be collected by specifying the respective service with a `-u` flag. For example, you can run the following command to collect logs for the containerd container runtime service:

  ```
  $ oc adm node-logs -l kubernetes.io/os=windows --path=journal -u containerd
  ```

### [12.6. Collecting containerd logs for Windows containers](#collecting-docker-logs-windows_windows-containers-troubleshooting) Copy linkLink copied to clipboard!

The Windows containerd container service does not stream log data to stdout, but instead, it stream log data to the Windows event log. You can view the containerd event logs to investigate issues you think might be caused by the Windows containerd container service.

**Prerequisites**

* You installed the Windows Machine Config Operator (WMCO) using Operator Lifecycle Manager (OLM).
* You have created a Windows compute machine set.

**Procedure**

* View the containerd logs by running the following command:

  ```
  $ oc adm node-logs -l kubernetes.io/os=windows --path=containerd
  ```

## [Legal Notice](#idm140458186682752) Copy linkLink copied to clipboard!

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
