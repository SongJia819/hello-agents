---
title: "Installation overview"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/index
retrieved_at: 2026-09-05T05:41:54.851511+00:00
---

# Installation overview

---

OpenShift Container Platform 4.22

## Overview content for installing OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139645397856912)

**Abstract**

This document provides an overview on how to install OpenShift Container Platform.

---

## [Chapter 1. OpenShift Container Platform installation overview](#ocp-installation-overview) Copy linkLink copied to clipboard!

Learn about the installation methods, requirements, and process for deploying an OpenShift Container Platform cluster.

### [1.1. The OpenShift Container Platform installation](#installation-overview_ocp-installation-overview) Copy linkLink copied to clipboard!

The OpenShift Container Platform installation program offers four methods for deploying a cluster. Each method has unique characteristics so that you can choose a method that meets your needs.

The following list details these methods:

* **Interactive**: You can deploy a cluster with the web-based Assisted Installer. This is an ideal approach for clusters with networks connected to the internet. The Assisted Installer is the easiest way to install OpenShift Container Platform. Assisted Installer provides smart defaults and performs pre-flight validations before installing the cluster. Assisted Installer also provides a RESTful API for automation and advanced configuration scenarios.
* **Local Agent-based**: You can deploy a cluster locally with the Agent-based Installer for disconnected environments or restricted networks. The Local Agent-based installer provides many of the benefits of the Assisted Installer, but you must download and configure the Agent-based Installer first. Configuration is done with a command-line interface. This approach is ideal for disconnected environments.

  + Additionally, you can deploy a cluster without an external registry, using self-contained installation media that also provides a simplified user interface similar to the Assisted Installer during on-premise installations. For more information, see "Installing a cluster without an external registry".
* **Automated**: You can deploy a cluster on installer-provisioned infrastructure. The installation program uses each cluster host’s baseboard management controller (BMC) for provisioning. You can deploy clusters in connected or disconnected environments.
* **Full control**: You can deploy a cluster on infrastructure that you prepare and maintain, which provides maximum customizability. You can deploy clusters in connected or disconnected environments.

Each method deploys a cluster with the following characteristics:

* Highly available infrastructure with no single points of failure, which is available by default.
* Administrators can control what updates are applied and when.

#### [1.1.1. Glossary of common terms for OpenShift Container Platform installing](#install-openshift-common-terms_ocp-installation-overview) Copy linkLink copied to clipboard!

The glossary defines common terms that relate to the installation content. Read the following list of terms to better understand the installation process.

Assisted Installer
:   An installer hosted at [console.redhat.com](https://console.redhat.com/openshift/assisted-installer/clusters/~new) that provides a web-based user interface or a RESTful API for creating a cluster configuration. The [Assisted Installer](https://access.redhat.com/documentation/en-us/assisted_installer_for_openshift_container_platform) generates a discovery image. Cluster machines boot with the discovery image, which installs RHCOS and an agent. Together, the Assisted Installer and agent provide preinstallation validation and installation for the cluster.

Agent-based Installer
:   An installer similar to the Assisted Installer, but you must download the [Agent-based Installer](https://console.redhat.com/openshift/install/metal/agent-based) first. The Agent-based Installer is ideal for disconnected environments.

Bootstrap node
:   A temporary machine that runs a minimal Kubernetes configuration required to deploy the OpenShift Container Platform control plane.

Control plane
:   A container orchestration layer that exposes the API and interfaces to define, deploy, and manage the lifecycle of containers. Also known as control plane machines.

Compute node
:   Nodes that are responsible for executing workloads for cluster users. Also known as worker nodes.

Disconnected installation
:   In some situations, parts of a data center might not have access to the internet, even through proxy servers. You can still install the OpenShift Container Platform in these environments, but you must download the required software and images and make them available to the disconnected environment.

The OpenShift Container Platform installation program
:   A program that provisions the infrastructure and deploys a cluster.

Installer-provisioned infrastructure
:   The installation program deploys and configures the infrastructure that the cluster runs on.

Ignition config files
:   A file that the Ignition tool uses to configure Red Hat Enterprise Linux CoreOS (RHCOS) during operating system initialization. The installation program generates different Ignition configuration files to initialize bootstrap, control plane, and worker nodes.

Kubernetes manifests
:   Specifications of a Kubernetes API object in a JSON or YAML format. A configuration file can include deployments, config maps, secrets, daemonsets, and so on.

kubelet
:   A primary node agent that runs on each node in the cluster to ensure that containers are running in a pod.

Load balancers
:   A load balancer serves as the single point of contact for clients. Load balancers for the API distribute incoming traffic across control plane nodes.

Machine Config Operator
:   An Operator that manages and applies configurations and updates of the base operating system and container runtime, including everything between the kernel and kubelet, for the nodes in the cluster.

Operators
:   The preferred method of packaging, deploying, and managing a Kubernetes application in an OpenShift Container Platform cluster. An operator takes human operational knowledge and encodes it into software that is easily packaged and shared with customers.

User-provisioned infrastructure
:   You can install OpenShift Container Platform on infrastructure that you provide. You can use the installation program to generate the assets required to provision the cluster infrastructure, create the cluster infrastructure, and then deploy the cluster to the infrastructure that you provided.

#### [1.1.2. Installation process](#installation-process_ocp-installation-overview) Copy linkLink copied to clipboard!

The OpenShift Container Platform installation program transforms a set of assets into a running cluster, using an installation process that varies depending on your installation method.

Except for the Assisted Installer, when you install an OpenShift Container Platform cluster, you must download the installation program from the appropriate **Cluster Type** page on the OpenShift Cluster Manager Hybrid Cloud Console. This console manages:

* REST API for accounts.
* Registry tokens, which are the pull secrets that you use to obtain the required components.
* Cluster registration, which associates the cluster identity to your Red Hat account to facilitate the gathering of usage metrics.

In OpenShift Container Platform 4.22, the installation program is a Go binary file that performs a series of file transformations on a set of assets. The way you interact with the installation program differs depending on your installation type. Consider the following installation use cases:

* To deploy a cluster with the Assisted Installer, you must configure the cluster settings by using the Assisted Installer. There is no installation program to download and configure. After you finish setting the cluster configuration, you download a discovery ISO and then boot cluster machines with that image. You can install clusters with the Assisted Installer on Nutanix, vSphere, and bare metal with full integration, and other platforms without integration. If you install on bare metal, you must provide all of the cluster infrastructure and resources, including the networking, load balancing, storage, and individual cluster machines.
* To deploy clusters with the Agent-based Installer, you can download the Agent-based Installer first. You can then configure the cluster and generate a discovery image. You boot cluster machines with the discovery image, which installs an agent that communicates with the installation program and handles the provisioning for you instead of you interacting with the installation program or setting up a provisioner machine yourself. You must provide all of the cluster infrastructure and resources, including the networking, load balancing, storage, and individual cluster machines. This approach is ideal for disconnected environments.
* For clusters with installer-provisioned infrastructure, you delegate the infrastructure bootstrapping and provisioning to the installation program instead of doing it yourself. The installation program creates all of the networking, machines, and operating systems that are required to support the cluster, except if you install on bare metal. If you install on bare metal, you must provide all of the cluster infrastructure and resources, including the bootstrap machine, networking, load balancing, storage, and individual cluster machines.
* If you provision and manage the infrastructure for your cluster, you must provide all of the cluster infrastructure and resources, including the bootstrap machine, networking, load balancing, storage, and individual cluster machines.

The installation program uses three sets of files during installation: an installation configuration file that is named `install-config.yaml`, Kubernetes manifests, and Ignition config files for your machine types.

Important

You can modify Kubernetes and the Ignition config files that control the underlying RHCOS operating system during installation. However, no validation is available to confirm the suitability of any modifications that you make to these objects. If you modify these objects, you might render your cluster non-functional. Because of this risk, modifying Kubernetes and Ignition config files is not supported unless you are following documented procedures or are instructed to do so by Red Hat support.

The installation configuration file is transformed into Kubernetes manifests, and then the manifests are wrapped into Ignition config files. The installation program uses these Ignition config files to create the cluster.

The installation configuration files are all pruned when you run the installation program, ensure you back up all the configuration files that you want to use again.

Important

You cannot modify the parameters that you set during installation, but you can modify many cluster attributes after installation.

The installation process with the Assisted Installer
:   Installation with the Assisted Installer involves creating a cluster configuration interactively by using the web-based user interface or the RESTful API. The Assisted Installer user interface prompts you for required values and provides reasonable default values for the remaining parameters, unless you change them in the user interface or with the API. The Assisted Installer generates a discovery image, which you download and use to boot the cluster machines. The image installs RHCOS and an agent, and the agent handles the provisioning for you. You can install OpenShift Container Platform with the Assisted Installer and full integration on Nutanix, vSphere, and bare metal. Additionally, you can install OpenShift Container Platform with the Assisted Installer on other platforms without integration.

    OpenShift Container Platform manages all aspects of the cluster, including the operating system itself. Each machine boots with a configuration that references resources hosted in the cluster that it joins. This configuration allows the cluster to manage itself as updates are applied.

    If possible, use the Assisted Installer feature to avoid having to download and configure the Agent-based Installer.

The installation process with Agent-based infrastructure
:   Agent-based installation is similar to using the Assisted Installer, except that you must initially download and install the Agent-based Installer. An Agent-based installation is useful when you want the convenience of the Assisted Installer, but you need to install a cluster in a disconnected environment.

    If possible, use the Agent-based installation feature to avoid having to create a provisioner machine with a bootstrap VM, and then provision and maintain the cluster infrastructure.

The installation process with installer-provisioned infrastructure
:   The default installation type uses installer-provisioned infrastructure. By default, the installation program acts as an installation wizard, prompting you for values that it cannot determine on its own and providing reasonable default values for the remaining parameters. You can also customize the installation process to support advanced infrastructure scenarios. The installation program provisions the underlying infrastructure for the cluster.

    You can install either a standard cluster or a customized cluster. With a standard cluster, you provide minimum details that are required to install the cluster. With a customized cluster, you can specify more details about the platform, such as the number of machines that the control plane uses, the type of virtual machine that the cluster deploys, or the CIDR range for the Kubernetes service network.

    If possible, use this feature to avoid having to provision and maintain the cluster infrastructure. In all other environments, you use the installation program to generate the assets that you require to provision your cluster infrastructure.

    With installer-provisioned infrastructure clusters, OpenShift Container Platform manages all aspects of the cluster, including the operating system itself. Each machine boots with a configuration that references resources hosted in the cluster that it joins. This configuration allows the cluster to manage itself as updates are applied.

The installation process with user-provisioned infrastructure
:   You can also install OpenShift Container Platform on infrastructure that you provide. You use the installation program to generate the assets that you require to provision the cluster infrastructure, create the cluster infrastructure, and then deploy the cluster to the infrastructure that you provided.

    If you do not use infrastructure that the installation program provisioned, you must manage and maintain the cluster resources yourself. The following list details some of these self-managed resources:

    * The underlying infrastructure for the control plane and compute machines that make up the cluster
    * Load balancers
    * Cluster networking, including the DNS records and required subnets
    * Storage for the cluster infrastructure and applications

      If your cluster uses user-provisioned infrastructure, you have the option of adding RHEL compute machines to your cluster.

#### [1.1.3. Verifying node state after installation](#ipi-verifying-nodes-after-installation_ocp-installation-overview) Copy linkLink copied to clipboard!

The OpenShift Container Platform installation completes when the following installation health checks are successful:

* The provisioner can access the OpenShift Container Platform web console.
* All control plane nodes are ready.
* All cluster Operators are available.

Note

After the installation completes, the specific cluster Operators responsible for the worker nodes continuously attempt to provision all worker nodes. Some time is required before all worker nodes report as `READY`. For installations on bare metal, wait a minimum of 60 minutes before troubleshooting a worker node. For installations on all other platforms, wait a minimum of 40 minutes before troubleshooting a worker node. A `DEGRADED` state for the cluster Operators responsible for the worker nodes depends on the Operators' own resources and not on the state of the nodes.

After your installation completes, you can continue to monitor the condition of the nodes in your cluster.

**Prerequisites**

* The installation program resolves successfully in the terminal.

**Procedure**

1. Show the status of all worker nodes:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                           STATUS   ROLES    AGE   VERSION
   example-compute1.example.com   Ready    worker   13m   v1.21.6+bb8d50a
   example-compute2.example.com   Ready    worker   13m   v1.21.6+bb8d50a
   example-compute4.example.com   Ready    worker   14m   v1.21.6+bb8d50a
   example-control1.example.com   Ready    master   52m   v1.21.6+bb8d50a
   example-control2.example.com   Ready    master   55m   v1.21.6+bb8d50a
   example-control3.example.com   Ready    master   55m   v1.21.6+bb8d50a
   ```
2. Show the phase of all worker machine nodes:

   ```
   $ oc get machines -A
   ```

   **Example output**

   ```
   NAMESPACE               NAME                           PHASE         TYPE   REGION   ZONE   AGE
   openshift-machine-api   example-zbbt6-master-0         Running                              95m
   openshift-machine-api   example-zbbt6-master-1         Running                              95m
   openshift-machine-api   example-zbbt6-master-2         Running                              95m
   openshift-machine-api   example-zbbt6-worker-0-25bhp   Running                              49m
   openshift-machine-api   example-zbbt6-worker-0-8b4c2   Running                              49m
   openshift-machine-api   example-zbbt6-worker-0-jkbqt   Running                              49m
   openshift-machine-api   example-zbbt6-worker-0-qrl5b   Running                              49m
   ```

#### [1.1.4. Installation scope](#installation-overview-scope-reference_ocp-installation-overview) Copy linkLink copied to clipboard!

The scope of the OpenShift Container Platform installation program is intentionally narrow. It is designed for simplicity and ensured success. You can complete many more configuration tasks after installation completes.

#### [1.1.5. OpenShift Local overview](#installation-openshift-local_ocp-installation-overview) Copy linkLink copied to clipboard!

OpenShift Local supports rapid application development to get started building OpenShift Container Platform clusters. OpenShift Local is designed to run on a local computer to simplify setup and testing, and to emulate the cloud development environment locally with all of the tools needed to develop container-based applications.

Regardless of the programming language you use, OpenShift Local hosts your application and brings a minimal, preconfigured Red Hat OpenShift Container Platform cluster to your local PC without the need for a server-based infrastructure.

On a hosted environment, OpenShift Local can create microservices, convert them into images, and run them in Kubernetes-hosted containers directly on your laptop or desktop running Linux, macOS, or Windows 10 or later.

### [1.2. Supported platforms for OpenShift Container Platform clusters](#supported-platforms-for-openshift-clusters_ocp-installation-overview) Copy linkLink copied to clipboard!

Review the platform support matrix to choose the installation method that meets your requirements.

Expand

Table 1.1. Supported platforms

| Platform | Installer-provisioned infrastructure [1] | User-provisioned infrastructure [2] | Agent-based Installer | Assisted Installer |
| --- | --- | --- | --- | --- |
| **Amazon Web Services (AWS)** | X | X |  |  |
| **Bare metal** | X | X | X | X |
| **External** |  |  | X | X |
| **Google Cloud** | X | X |  |  |
| **IBM Cloud® Classic** | X |  |  |  |
| **IBM Cloud® Virtual Private Cloud (VPC)** | X |  |  |  |
| **IBM Power®** |  | X | X | X |
| **IBM Z® or IBM® LinuxONE** |  | X | X | X |
| **Microsoft Azure** | X | X |  |  |
| **Microsoft Azure Stack Hub** | X | X |  |  |
| **None** |  |  | X | X |
| **Nutanix** | X |  |  | X |
| **Oracle Cloud Infrastructure (OCI)** |  |  | X | X |
| **Red Hat OpenStack Platform (RHOSP) [3]** | X | X |  |  |
| **VMware vSphere** | X | X | X | X |

Show more

The following list describes three different deployment pathways and their prerequisites:

* For installer-provisioned infrastructure: All machines, including the computer that you run the installation process on, must have direct internet access to pull images for platform containers and provide telemetry data to Red Hat.

  Important

  After installation, the following changes are not supported:

  + Mixing cloud provider platforms.
  + Mixing cloud provider components. For example, using a persistent storage framework from another platform on the platform where you installed the cluster.
* For user-provisioned infrastructure: Depending on the supported cases for the platform, you can perform installations on user-provisioned infrastructure so that you can run machines with full internet access, place your cluster behind a proxy, or perform a disconnected installation.

  In a disconnected installation, you can download the images that are required to install a cluster, place them in a mirror registry, and use that data to install your cluster. While you require internet access to pull images for platform containers, with a disconnected installation on vSphere or bare-metal infrastructure, your cluster machines do not require direct internet access.
* For Red Hat OpenStack Platform (RHOSP): The latest OpenShift Container Platform release supports both the latest RHOSP long-life release and intermediate release. For complete RHOSP release compatibility, see "OpenShift Container Platform on RHOSP support matrix". See "OpenShift Container Platform 4.x Tested Integrations" for details about integration testing for different platforms.

## [Chapter 2. Selecting a cluster installation method and preparing it for users](#installing-preparing) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform, decide what kind of installation process to follow and verify that you have all of the required resources to prepare the cluster for users.

### [2.1. Selecting a cluster installation type](#installing-preparing-selecting-cluster-type_installing-preparing) Copy linkLink copied to clipboard!

Decide what kind of installation process to follow based on your infrastructure, experience, and security requirements.

Before you install an OpenShift Container Platform cluster, you need to select the best installation instructions to follow. Think about your answers to the following questions to select the best option.

#### [2.1.1. Do you want to install and manage an OpenShift Container Platform cluster yourself?](#installing-preparing-install-manage_installing-preparing) Copy linkLink copied to clipboard!

If you want to install and manage OpenShift Container Platform yourself, you can install it on the following platforms:

* Amazon Web Services (AWS) on 64-bit x86 instances
* Amazon Web Services (AWS) on 64-bit ARM instances
* Microsoft Azure on 64-bit x86 instances
* Microsoft Azure on 64-bit ARM instances
* Microsoft Azure Stack Hub
* Google Cloud on 64-bit x86 instances
* Google Cloud on 64-bit ARM instances
* Red Hat OpenStack Platform (RHOSP)
* IBM Cloud®
* IBM Z® or IBM® LinuxONE with z/VM
* IBM Z® or IBM® LinuxONE with Red Hat Enterprise Linux (RHEL) KVM
* IBM Z® or IBM® LinuxONE in an LPAR
* IBM Power®
* IBM Power® Virtual Server
* Nutanix
* VMware vSphere
* Bare metal or other platform agnostic infrastructure

You can deploy an OpenShift Container Platform 4 cluster to both on-premise hardware and to cloud hosting services, but all of the machines in a cluster must be in the same data center or cloud hosting service.

If you want to use OpenShift Container Platform but you do not want to manage the cluster yourself, you can choose from several managed service options. If you want a cluster that is fully managed by Red Hat, you can use [OpenShift Dedicated](https://www.openshift.com/products/dedicated/). You can also use OpenShift as a managed service on Azure, AWS, IBM Cloud®, or Google Cloud. For more information about managed services, see the [OpenShift Products](https://www.openshift.com/products) page. If you install an OpenShift Container Platform cluster with a cloud virtual machine as a virtual bare metal, the corresponding cloud-based storage is not supported.

#### [2.1.2. Have you used OpenShift Container Platform 3 and want to use OpenShift Container Platform 4?](#installing-preparing-migrate_installing-preparing) Copy linkLink copied to clipboard!

If you used OpenShift Container Platform 3 and want to try OpenShift Container Platform 4, you need to understand how different OpenShift Container Platform 4 is. OpenShift Container Platform 4 weaves the Operators that package, deploy, and manage Kubernetes applications and the operating system that the platform runs on, Red Hat Enterprise Linux CoreOS (RHCOS), together seamlessly. Instead of deploying machines and configuring their operating systems so that you can install OpenShift Container Platform on them, the RHCOS operating system is an integral part of the OpenShift Container Platform cluster. Deploying the operating system for the cluster machines is part of the installation process for OpenShift Container Platform. See [Differences between OpenShift Container Platform 3 and 4](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/migrating_from_version_3_to_4/#migration-comparing-ocp-3-4).

Because you need to provision machines as part of the OpenShift Container Platform cluster installation process, you cannot upgrade an OpenShift Container Platform 3 cluster to OpenShift Container Platform 4. Instead, you must create a new OpenShift Container Platform 4 cluster and migrate your OpenShift Container Platform 3 workloads to them. For more information about migrating, see [Migrating from OpenShift Container Platform 3 to 4 overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/migrating_from_version_3_to_4/#migration-from-version-3-to-4-overview). Because you must migrate to OpenShift Container Platform 4, you can use any type of production cluster installation process to create your new cluster.

#### [2.1.3. Do you want to use existing components in your cluster?](#installing-preparing-existing-components_installing-preparing) Copy linkLink copied to clipboard!

Because the operating system is integral to OpenShift Container Platform, it is easier to let the installation program for OpenShift Container Platform stand up all of the infrastructure. These are called *installer provisioned infrastructure* installations. In this type of installation, you can provide some existing infrastructure to the cluster, but the installation program deploys all of the machines that your cluster initially needs.

You can deploy an installer-provisioned infrastructure cluster without specifying any customizations to the cluster or its underlying machines to [AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-default), [Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-default), [Azure Stack Hub](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure_stack_hub/#installing-azure-stack-hub-default), [Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-default), [Nutanix](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_nutanix/#installing-nutanix-installer-provisioned).

If you need to perform basic configuration for your installer-provisioned infrastructure cluster, such as the instance type for the cluster machines, you can customize an installation for [AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations), [Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-customizations), [Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-customizations), [Nutanix](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_nutanix/#installing-nutanix-installer-provisioned).

For installer-provisioned infrastructure installations, you can use an existing [VPC in AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-vpc), [vNet in Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-vnet), or [VPC in Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-vpc). You can also reuse part of your networking infrastructure so that your cluster in [AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations), [Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-customizations), [Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-customizations) can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations. If you have existing accounts and credentials on these clouds, you can re-use them, but you might need to modify the accounts to have the required permissions to install OpenShift Container Platform clusters on them.

You can use the installer-provisioned infrastructure method to create appropriate machine instances on your hardware for [vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere-installer-provisioned), and [bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#ipi-install-overview). Additionally, for [vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere-installer-provisioned-customizations), you can also customize additional network parameters during installation.

For some installer-provisioned infrastructure installations, for example on the VMware vSphere and bare metal platforms, the external traffic that reaches the ingress virtual IP (VIP) is not balanced between the default `IngressController` replicas. For vSphere and bare-metal installer-provisioned infrastructure installations where exceeding the baseline `IngressController` router performance is expected, you must configure an external load balancer. Configuring an external load balancer achieves the performance of multiple `IngressController` replicas. For more information about the baseline `IngressController` performance, see [Baseline Ingress Controller (router) performance](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#baseline-router-performance_routing-optimization). For more information about configuring an external load balancer, see [Configuring a user-managed load balancer](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#nw-osp-configuring-external-load-balancer_ipi-install-installation-workflow).

If you want to reuse extensive cloud infrastructure, you can complete a *user-provisioned infrastructure* installation. With these installations, you manually deploy the machines that your cluster requires during the installation process. If you perform a user-provisioned infrastructure installation on [AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-user-infra), [Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-user-infra), [Azure Stack Hub](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure_stack_hub/#installing-azure-stack-hub-user-infra), you can use the provided templates to help you stand up all of the required components. You can also reuse a shared [VPC on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-user-infra-vpc). Otherwise, you can use the [provider-agnostic](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_any_platform/#installing-platform-agnostic) installation method to deploy a cluster into other clouds.

You can also complete a user-provisioned infrastructure installation on your existing hardware. If you use [RHOSP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_openstack/#installing-openstack-user), [IBM Z® or IBM® LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z), [IBM Z® and IBM® LinuxONE with RHEL KVM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-kvm), [IBM Z® and IBM® LinuxONE in an LPAR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-lpar), [IBM Power](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power/#installing-ibm-power), or [vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere), use the specific installation instructions to deploy your cluster. If you use other supported hardware, follow the [bare metal installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal) procedure. For some of these platforms, such as [vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere) and [bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal-network-customizations), you can also customize additional network parameters during installation.

#### [2.1.4. Do you need extra security for your cluster?](#installing-preparing-security_installing-preparing) Copy linkLink copied to clipboard!

If you use a user-provisioned installation method, you can configure a proxy for your cluster. The instructions are included in each installation procedure.

If you want to prevent your cluster on a public cloud from exposing endpoints externally, you can deploy a private cluster with installer-provisioned infrastructure on [AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-private), [Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-private), or [Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-private).

If you need to install your cluster that has limited access to the internet, such as a disconnected or restricted network cluster, you can [mirror the installation packages](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-mirroring-installation-images) and install the cluster from them. Follow detailed instructions for user-provisioned infrastructure installations into restricted networks for [AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-restricted-networks-aws), [Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-restricted-networks-gcp), [IBM Z® or IBM® LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-restricted-networks-ibm-z), [IBM Z® or IBM® LinuxONE with RHEL KVM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-restricted-networks-ibm-z-kvm), [IBM Z® or IBM® LinuxONE in an LPAR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-restricted-networks-ibm-z-lpar), [IBM Power®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power/#installing-restricted-networks-ibm-power), [vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-restricted-networks-vsphere), or [bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-restricted-networks-bare-metal). You can also install a cluster into a restricted network by using installer-provisioned infrastructure by following detailed instructions for [AWS](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-restricted-networks-aws-installer-provisioned), [Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-restricted-networks-gcp-installer-provisioned), [IBM Cloud®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_cloud/#installing-ibm-cloud-restricted), [Nutanix](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_nutanix/#installing-restricted-networks-nutanix-installer-provisioned), [RHOSP](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_openstack/#installing-openstack-installer-restricted), and [vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-restricted-networks-installer-provisioned-vsphere).

If you need to deploy your cluster to an [AWS GovCloud region](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-specialized-region), [AWS China region](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-specialized-region), or [Azure government region](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-government-region), you can configure those custom regions during an installer-provisioned infrastructure installation.

You can also configure the cluster machines to use the RHEL cryptographic libraries that have been submitted to NIST for [FIPS 140-2/140-3 Validation](#installing-fips "Chapter 4. Support for FIPS cryptography") during installation.

Important

When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86\_64, ppc64le, and s390x architectures.

### [2.2. Preparing your cluster for users after installation](#installing-preparing-cluster-for-users_installing-preparing) Copy linkLink copied to clipboard!

Configure a production cluster for users before they access it.

Some configuration is not required to install the cluster but recommended before your users access the cluster. You can customize the cluster itself by [customizing](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations) the Operators that make up your cluster and integrate you cluster with other required systems, such as an identity provider.

For a production cluster, you must configure the following integrations:

* [Persistent storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#understanding-persistent-storage)
* [An identity provider](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-identity-provider)
* [Monitoring core OpenShift Container Platform components](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/getting_started/core-platform-monitoring-first-steps)

### [2.3. Preparing your cluster for workloads](#installing-preparing-cluster-for-workloads_installing-preparing) Copy linkLink copied to clipboard!

Take extra steps to prepare your cluster before deploying applications, depending on your workload needs.

Depending on your workload needs, you might need to take extra steps before you begin deploying applications. For example, after you prepare infrastructure to support your application [build strategy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/builds_using_buildconfig/#build-strategies), you might need to make provisions for [low-latency](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/scalability_and_performance/#cnf-tuning-low-latency-nodes-with-perf-profile) workloads or to [protect sensitive workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/nodes/#nodes-pods-secrets). You can also configure [monitoring](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_user_workload_monitoring/preparing-to-configure-the-monitoring-stack-uwm#enabling-monitoring-for-user-defined-projects-uwm_preparing-to-configure-the-monitoring-stack-uwm) for application workloads.

If you plan to run [Windows workloads](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/windows_container_support_for_openshift/#enabling-windows-container-workloads), you must enable [hybrid networking with OVN-Kubernetes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#configuring-hybrid-networking) during the installation process; hybrid networking cannot be enabled after your cluster is installed.

### [2.4. Supported installation methods for different platforms](#installing-preparing-supported-installation-methods-reference_installing-preparing) Copy linkLink copied to clipboard!

You can perform different types of installations on different platforms.

Note

Not all installation options are supported for all platforms, as shown in the following tables. A checkmark indicates that the option is supported and links to the relevant section.

Expand

Table 2.1. Installer-provisioned infrastructure options

|  | AWS (64-bit x86) | AWS (64-bit ARM) | Azure (64-bit x86) | Azure (64-bit ARM) | Azure Stack Hub | GCP (64-bit x86) | GCP (64-bit ARM) | Nutanix | RHOSP | Bare metal (64-bit x86) | Bare metal (64-bit ARM) | vSphere | IBM Cloud® | IBM Z® | IBM Power® | IBM Power® Virtual Server |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Default | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-default) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-default) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-default) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-default) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure_stack_hub/#installing-azure-stack-hub-default) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-default) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-default) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_nutanix/#installing-nutanix-installer-provisioned) |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#ipi-install-overview) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#ipi-install-overview) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere-installer-provisioned) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_cloud/#installing-ibm-cloud-customizations) |  |  |  |
| Custom | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure_stack_hub/#installing-azure-stack-hub-default) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_nutanix/#installing-nutanix-installer-provisioned) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_openstack/#installing-openstack-installer-custom) |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere-installer-provisioned-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_cloud/#installing-ibm-cloud-customizations) |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power_virtual_server/#installing-ibm-power-vs-customizations) |
| Network customization | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure_stack_hub/#installing-azure-stack-hub-network-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-customizations) |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#configuring-host-network-interfaces-in-the-install-config-yaml-file_ipi-install-installation-workflow) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#configuring-host-network-interfaces-in-the-install-config-yaml-file_ipi-install-installation-workflow) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere-installer-provisioned-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_cloud/#installing-ibm-cloud-customizations) |  |  |  |
| Restricted network | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-restricted-networks-aws-installer-provisioned) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-restricted-networks-aws-installer-provisioned) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-restricted-networks-azure-installer-provisioned) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-restricted-networks-azure-installer-provisioned) |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-restricted-networks-gcp-installer-provisioned) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-restricted-networks-gcp-installer-provisioned) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_nutanix/#installing-restricted-networks-nutanix-installer-provisioned) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_openstack/#installing-openstack-installer-restricted) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#ipi-install-installation-workflow) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#ipi-install-installation-workflow) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-restricted-networks-installer-provisioned-vsphere) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_cloud/#installing-ibm-cloud-restricted) |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power_virtual_server/#installing-restricted-networks-ibm-power-vs) |
| Private clusters | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-private) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-private) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-private) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-private) |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-private) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-private) |  |  |  |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_cloud/#installing-ibm-cloud-private) |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power_virtual_server/#installing-ibm-power-vs-private-cluster) |
| Existing virtual private networks | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-vpc) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-vpc) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-vnet) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-vnet) |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-vpc) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-vpc) |  |  |  |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_cloud/#installing-ibm-cloud-vpc) |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power_virtual_server/#installing-ibm-powervs-vpc) |
| Government regions | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-specialized-region) |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-government-region) |  |  |  |  |  |  |  |  |  |  |  |  |  |
| Secret regions | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-specialized-region) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| China regions | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-specialized-region) |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |

Show more

Expand

Table 2.2. User-provisioned infrastructure options

|  | AWS (64-bit x86) | AWS (64-bit ARM) | Azure (64-bit x86) | Azure (64-bit ARM) | Azure Stack Hub | GCP (64-bit x86) | GCP (64-bit ARM) | Nutanix | RHOSP | Bare metal (64-bit x86) | Bare metal (64-bit ARM) | vSphere | IBM Cloud® | IBM Z® | IBM Z® with RHEL KVM | IBM Power® | Platform agnostic |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Custom | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-user-infra) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-user-infra) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-user-infra) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-user-infra) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure_stack_hub/#installing-azure-stack-hub-user-infra) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-user-infra) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-user-infra) |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_openstack/#installing-openstack-user) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere) |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-kvm) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power/#installing-ibm-power) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_any_platform/#installing-platform-agnostic) |
| Network customization |  |  |  |  |  |  |  |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal-network-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal-network-customizations) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere-network-customizations) |  |  |  |  |  |
| Restricted network | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-restricted-networks-aws) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-restricted-networks-aws) |  |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-restricted-networks-gcp) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-restricted-networks-gcp) |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-restricted-networks-bare-metal) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-restricted-networks-bare-metal) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-restricted-networks-vsphere) |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-restricted-networks-ibm-z) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-restricted-networks-ibm-z-kvm) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power/#installing-restricted-networks-ibm-power) |  |
| Shared VPC hosted outside of cluster project |  |  |  |  |  | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-user-infra-vpc) | [✓](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-user-infra-vpc) |  |  |  |  |  |  |  |  |  |  |

Show more

## [Chapter 3. Cluster capabilities](#cluster-capabilities) Copy linkLink copied to clipboard!

As a cluster administrator, you can use cluster capabilities to enable or disable optional components before installation. Additionally, you can enable cluster capabilities at anytime after installation.

Note

You cannot disable a cluster capability after it is enabled.

### [3.1. Enabling cluster capabilities](#enabling-cluster-capabilities_cluster-capabilities) Copy linkLink copied to clipboard!

If you are using an installation method that includes customizing your cluster by creating an `install-config.yaml` file, you can select which cluster capabilities you want to make available on the cluster.

Note

If you customize your cluster by enabling or disabling specific cluster capabilities, you must manually maintain your `install-config.yaml` file. New OpenShift Container Platform updates might declare new capability handles for existing components, or introduce new components altogether. Users who customize their `install-config.yaml` file should consider periodically updating their `install-config.yaml` file as OpenShift Container Platform is updated.

You can use the following configuration parameters to select cluster capabilities:

```
capabilities:
  baselineCapabilitySet: v4.11
  additionalEnabledCapabilities:
  - CSISnapshot
  - Console
  - Storage
```

`capabilities.baselineCapabilitySet`
:   Specifies a baseline set of capabilities to install. Valid values are `None`, `vCurrent` and `v4.x`. If you select `None`, all optional capabilities are disabled. The default value is `vCurrent`, which enables all optional capabilities.

Note

`v4.x` refers to any value up to and including the current cluster version. For example, valid values for a OpenShift Container Platform 4.12 cluster are `v4.11` and `v4.12`.

`capabilities.additionalEnabledCapabilities`
:   Specifies a list of capabilities to explicitly enable. These capabilities are enabled in addition to the capabilities specified in `baselineCapabilitySet`.

Note

In this example, the default capability is set to `v4.11`. The `additionalEnabledCapabilities` field enables additional capabilities over the default `v4.11` capability set.

The following table describes the `baselineCapabilitySet` values.

Expand

Table 3.1. Cluster capabilities baselineCapabilitySet values description

| Value | Description |
| --- | --- |
| `vCurrent` | Specify this option when you want to automatically add new, default capabilities that are introduced in new releases. |
| `v4.11` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.11. By specifying `v4.11`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.11 are `baremetal`, `MachineAPI`, `marketplace`, and `openshift-samples`. |
| `v4.12` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.12. By specifying `v4.12`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.12 are `baremetal`, `MachineAPI`, `marketplace`, `openshift-samples`, `Console`, `Insights`, `Storage`, and `CSISnapshot`. |
| `v4.13` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.13. By specifying `v4.13`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.13 are `baremetal`, `MachineAPI`, `marketplace`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, and `NodeTuning`. |
| `v4.14` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.14. By specifying `v4.14`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.14 are `baremetal`, `MachineAPI`, `marketplace`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, and `DeploymentConfig`. |
| `v4.15` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.15. By specifying `v4.15`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.15 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, and `DeploymentConfig`. |
| `v4.16` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.16. By specifying `v4.16`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.16 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, `DeploymentConfig`, and `CloudControllerManager`. |
| `v4.17` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.17. By specifying `v4.17`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.17 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, `DeploymentConfig`, and `CloudControllerManager`. |
| `v4.18` | Specify this option when you want to enable the default capabilities for OpenShift Container Platform 4.18. By specifying `v4.18`, capabilities that are introduced in newer versions of OpenShift Container Platform are not enabled. The default capabilities in OpenShift Container Platform 4.18 are `baremetal`, `MachineAPI`, `marketplace`, `OperatorLifecycleManager`, `OperatorLifecycleManagerV1`, `openshift-samples`, `Console`, `Insights`, `Storage`, `CSISnapshot`, `NodeTuning`, `ImageRegistry`, `Build`, `CloudCredential`, `DeploymentConfig`, and `CloudControllerManager`. |
| `None` | Specify when the other sets are too large, and you do not need any capabilities or want to fine-tune via `additionalEnabledCapabilities`. |

Show more

### [3.2. Optional cluster capabilities in OpenShift Container Platform 4.22](#explanation_of_capabilities_cluster-capabilities) Copy linkLink copied to clipboard!

Currently, cluster Operators provide the features for these optional capabilities.

The following sections summarize the features provided by each capability and what functionality you lose if you disable a functionality.

#### [3.2.1. Cluster Baremetal Operator](#cluster-bare-metal-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Cluster Baremetal Operator provides the features for the `baremetal` capability.

The Cluster Baremetal Operator (CBO) deploys all the components necessary to take a bare-metal server to a fully functioning worker node ready to run OpenShift Container Platform compute nodes. The CBO ensures that the metal3 deployment, which consists of the Bare Metal Operator (BMO) and Ironic containers, runs on one of the control plane nodes within the OpenShift Container Platform cluster. The CBO also listens for OpenShift Container Platform updates to resources that it watches and takes appropriate action.

The bare-metal capability is required for deployments using installer-provisioned infrastructure. Disabling the bare-metal capability can result in unexpected problems with these deployments.

Important

If the bare-metal capability is disabled, the cluster cannot provision or manage bare-metal nodes. Only disable the capability if there are no `BareMetalHost` resources in your deployment. The `baremetal` capability depends on the `MachineAPI` capability. If you enable the `baremetal` capability, you must also enable `MachineAPI`.

Note

Red Hat recommends that cluster administrators only disable the bare-metal capability during installations with user-provisioned infrastructure that do not have any `BareMetalHost` resources in the cluster.

#### [3.2.2. Build capability](#build-config-capability_cluster-capabilities) Copy linkLink copied to clipboard!

The `Build` capability enables the `Build` API. The `Build` API manages the lifecycle of `Build` and `BuildConfig` objects.

Important

If you disable the `Build` capability, the following resources will not be available in the cluster:

* `Build` and `BuildConfig` resources
* The `builder` service account

Disable the `Build` capability only if you do not require `Build` and `BuildConfig` resources or the `builder` service account in the cluster.

#### [3.2.3. Cloud Controller Manager Operator](#cluster-cloud-controller-manager-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Cloud Controller Manager Operator provides features for the `CloudControllerManager` capability.

Note

Currently, disabling the `CloudControllerManager` capability is not supported on all platforms.

You can determine if your cluster supports disabling the `CloudControllerManager` capability by checking values in the installation configuration (`install-config.yaml`) file for your cluster.

In the `install-config.yaml` file, locate the `platform` parameter.

* If the value of the `platform` parameter is `Baremetal` or `None`, you can disable the `CloudControllerManager` capability on your cluster.
* If the value of the `platform` parameter is `External`, locate the `platform.external.cloudControllerManager` parameter. If the value of the `platform.external.cloudControllerManager` parameter is `None`, you can disable the `CloudControllerManager` capability on your cluster.

Important

If these parameters contain any other values than those listed, you cannot disable the `CloudControllerManager` capability on your cluster.

Note

The status of this Operator is General Availability for Amazon Web Services (AWS), Google Cloud, IBM Cloud®, global Microsoft Azure, Microsoft Azure Stack Hub, Nutanix, Red Hat OpenStack Platform (RHOSP), and VMware vSphere.

The Operator is available as a Technology Preview for IBM Power® Virtual Server.

The Cloud Controller Manager Operator manages and updates the cloud controller managers deployed on top of OpenShift Container Platform. The Operator is based on the Kubebuilder framework and `controller-runtime` libraries. You can install the Cloud Controller Manager Operator by using the Cluster Version Operator (CVO).

The Cloud Controller Manager Operator includes the following components:

* Operator
* Cloud configuration observer

By default, the Operator exposes Prometheus metrics through the `metrics` service.

#### [3.2.4. Cloud Credential Operator](#cloud-credential-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Cloud Credential Operator provides features for the `CloudCredential` capability.

Note

Currently, disabling the `CloudCredential` capability is only supported for bare-metal clusters.

The Cloud Credential Operator (CCO) manages cloud provider credentials as Kubernetes custom resource definitions (CRDs). The CCO syncs on `CredentialsRequest` custom resources (CRs) to allow OpenShift Container Platform components to request cloud provider credentials with the specific permissions that are required for the cluster to run.

By setting different values for the `credentialsMode` parameter in the `install-config.yaml` file, the CCO can be configured to operate in several different modes. If no mode is specified, or the `credentialsMode` parameter is set to an empty string (`""`), the CCO operates in its default mode.

#### [3.2.5. Cluster Image Registry Operator](#cluster-image-registry-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Cluster Image Registry Operator provides features for the `ImageRegistry` capability.

The Cluster Image Registry Operator manages a singleton instance of the OpenShift image registry. It manages all configuration of the registry, including creating storage.

On initial start up, the Operator creates a default `image-registry` resource instance based on the configuration detected in the cluster. This indicates what cloud storage type to use based on the cloud provider.

If insufficient information is available to define a complete `image-registry` resource, then an incomplete resource is defined and the Operator updates the resource status with information about what is missing.

The Cluster Image Registry Operator runs in the `openshift-image-registry` namespace and it also manages the registry instance in that location. All configuration and workload resources for the registry reside in that namespace.

In order to integrate the image registry into the cluster’s user authentication and authorization system, an image pull secret is generated for each service account in the cluster.

Important

If you disable the `ImageRegistry` capability or if you disable the integrated OpenShift image registry in the Cluster Image Registry Operator’s configuration, the image pull secret is not generated for each service account.

If you disable the `ImageRegistry` capability, you can reduce the overall resource footprint of OpenShift Container Platform in Telco environments. Depending on your deployment, you can disable this component if you do not need it.

#### [3.2.6. Cluster Storage Operator](#cluster-storage-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Cluster Storage Operator provides the features for the `Storage` capability.

The Cluster Storage Operator sets OpenShift Container Platform cluster-wide storage defaults. It ensures a default `storageclass` exists for OpenShift Container Platform clusters. It also installs Container Storage Interface (CSI) drivers which enable your cluster to use various storage backends.

Important

If the cluster storage capability is disabled, the cluster will not have a default `storageclass` or any CSI drivers. Users with administrator privileges can create a default `storageclass` and manually install CSI drivers if the cluster storage capability is disabled.

Notes
:   The storage class that the Operator creates can be made non-default by editing its annotation, but this storage class cannot be deleted if the Operator runs.

#### [3.2.7. Console Operator](#console-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Console Operator provides the features for the `Console` capability.

The Console Operator installs and maintains the OpenShift Container Platform web console on a cluster. The Console Operator is installed by default and automatically maintains a console.

#### [3.2.8. Cluster CSI Snapshot Controller Operator](#cluster-csi-snapshot-controller-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Cluster CSI Snapshot Controller Operator provides the features for the `CSISnapshot` capability.

The Cluster CSI Snapshot Controller Operator installs and maintains the CSI Snapshot Controller. The CSI Snapshot Controller is responsible for watching the `VolumeSnapshot` CRD objects and manages the creation and deletion lifecycle of volume snapshots.

#### [3.2.9. DeploymentConfig capability](#deployment-config-capability_cluster-capabilities) Copy linkLink copied to clipboard!

The `DeploymentConfig` capability enables and manages the `DeploymentConfig` API.

Important

If you disable the `DeploymentConfig` capability, the following resources will not be available in the cluster:

* `DeploymentConfig` resources
* The `deployer` service account

Disable the `DeploymentConfig` capability only if you do not require `DeploymentConfig` resources and the `deployer` service account in the cluster.

#### [3.2.10. Ingress Operator](#ingress-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Ingress Operator provides the features for the `Ingress` capability.

The Ingress Operator configures and manages the OpenShift Container Platform router.

CRDs
:   * `clusteringresses.ingress.openshift.io`

      + Scope: Namespaced
      + CR: `clusteringresses`
      + Validation: No

Configuration objects
:   * Cluster config

      + Type Name: `clusteringresses.ingress.openshift.io`
      + Instance Name: `default`
      + View Command:

        ```
        $ oc get clusteringresses.ingress.openshift.io -n openshift-ingress-operator default -o yaml
        ```

Notes
:   The Ingress Operator sets up the router in the `openshift-ingress` project and creates the deployment for the router:

    ```
    $ oc get deployment -n openshift-ingress
    ```

    The Ingress Operator uses the `clusterNetwork[].cidr` from the `network/cluster` status to determine what mode (IPv4, IPv6, or dual stack) the managed Ingress Controller (router) should operate in. For example, if `clusterNetwork` contains only a v6 `cidr`, then the Ingress Controller operates in IPv6-only mode.

    In the following example, Ingress Controllers managed by the Ingress Operator will run in IPv4-only mode because only one cluster network exists and the network is an IPv4 `cidr`:

    ```
    $ oc get network/cluster -o jsonpath='{.status.clusterNetwork[*]}'
    ```

    **Example output**

    ```
    map[cidr:10.128.0.0/14 hostPrefix:23]
    ```

#### [3.2.11. Insights Operator](#insights-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Insights Operator provides the features for the `Insights` capability.

The Insights Operator gathers OpenShift Container Platform configuration data and sends it to Red Hat. The data is used to produce proactive insights recommendations about potential issues that a cluster might be exposed to. These insights are communicated to cluster administrators through the Red Hat Lightspeed advisor service on [console.redhat.com](https://console.redhat.com/).

Notes
:   Insights Operator complements OpenShift Container Platform Telemetry.

#### [3.2.12. Machine API capability](#machine-api-capability_cluster-capabilities) Copy linkLink copied to clipboard!

The `machine-api-operator`, `cluster-autoscaler-operator`, and `cluster-control-plane-machine-set-operator` Operators provide the features for the `MachineAPI` capability. You can disable this capability only if you install a cluster with user-provisioned infrastructure.

The Machine API capability is responsible for all machine configuration and management in the cluster. If you disable the Machine API capability during installation, you need to manage all machine-related tasks manually.

#### [3.2.13. Marketplace Operator](#marketplace-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Marketplace Operator provides the features for the `marketplace` capability.

The Marketplace Operator simplifies the process for bringing off-cluster Operators to your cluster by using a set of default Operator Lifecycle Manager (OLM) catalogs on the cluster. When the Marketplace Operator is installed, it creates the `openshift-marketplace` namespace. OLM ensures catalog sources installed in the `openshift-marketplace` namespace are available for all namespaces on the cluster.

If you disable the `marketplace` capability, the Marketplace Operator does not create the `openshift-marketplace` namespace. Catalog sources can still be configured and managed on the cluster manually, but OLM depends on the `openshift-marketplace` namespace in order to make catalogs available to all namespaces on the cluster. Users with elevated permissions to create namespaces prefixed with `openshift-`, such as system or cluster administrators, can manually create the `openshift-marketplace` namespace.

If you enable the `marketplace` capability, you can enable and disable individual catalogs by configuring the Marketplace Operator.

#### [3.2.14. Node Tuning Operator](#about-node-tuning-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Node Tuning Operator provides features for the `NodeTuning` capability.

The Node Tuning Operator helps you manage node-level tuning by orchestrating the TuneD daemon and achieves low latency performance by using the Performance Profile controller. The majority of high-performance applications require some level of kernel tuning. The Node Tuning Operator provides a unified management interface to users of node-level sysctls and more flexibility to add custom tuning specified by user needs.

If you disable the NodeTuning capability, some default tuning settings will not be applied to the control-plane nodes. This might limit the scalability and performance of large clusters with over 900 nodes or 900 routes.

#### [3.2.15. Cluster Samples Operator](#cluster-samples-operator_cluster-capabilities) Copy linkLink copied to clipboard!

The Cluster Samples Operator provides the features for the `openshift-samples` capability.

The Cluster Samples Operator manages the sample image streams and templates stored in the `openshift` namespace.

On initial start up, the Operator creates the default samples configuration resource to initiate the creation of the image streams and templates. The configuration object is a cluster scoped object with the key `cluster` and type `configs.samples`.

The image streams are the Red Hat Enterprise Linux CoreOS (RHCOS)-based OpenShift Container Platform image streams pointing to images on `registry.redhat.io`. Similarly, the templates are those categorized as OpenShift Container Platform templates.

If you disable the samples capability, users cannot access the image streams, samples, and templates it provides. Depending on your deployment, you might want to disable this component if you do not need it.

#### [3.2.16. About Operator Lifecycle Manager (OLM) Classic](#olm-overview_cluster-capabilities) Copy linkLink copied to clipboard!

OLM (Classic) provides the features for the `OperatorLifecycleManager` capability.

Operator Lifecycle Manager (OLM) Classic helps users install, update, and manage the lifecycle of Kubernetes native applications (Operators) and their associated services running across their OpenShift Container Platform clusters. Operator Lifecycle Manager (OLM) Classic forms part of the Operator Framework, an open source toolkit designed to manage Operators in an effective, automated, and scalable way.

If an Operator requires any of the following APIs, then you must enable the `OperatorLifecycleManager` capability:

* `ClusterServiceVersion`
* `CatalogSource`
* `Subscription`
* `InstallPlan`
* `OperatorGroup`

Important

The `marketplace` capability depends on the `OperatorLifecycleManager` capability. You cannot disable the `OperatorLifecycleManager` capability and enable the `marketplace` capability.

#### [3.2.17. Operator Lifecycle Manager (OLM) v1 Operator](#cluster-operators-ref-olmv1_cluster-capabilities) Copy linkLink copied to clipboard!

OLM v1 provides the features for the `OperatorLifecycleManagerV1` capability.

Starting in OpenShift Container Platform 4.18, OLM v1 is enabled by default alongside OLM (Classic). This next-generation iteration provides an updated framework that evolves many of OLM (Classic) concepts that enable cluster administrators to extend capabilities for their users.

OLM v1 manages the lifecycle of the new `ClusterExtension` object, which includes Operators via the `registry+v1` bundle format, and controls installation, upgrade, and role-based access control (RBAC) of extensions within a cluster.

In OpenShift Container Platform, OLM v1 is provided by the `olm` cluster Operator.

Note

The `olm` cluster Operator informs cluster administrators if there are any installed extensions blocking cluster upgrade, based on their `olm.maxOpenShiftVersion` properties. For more information, see "Compatibility with OpenShift Container Platform versions".

Operator Lifecycle Manager (OLM) v1 comprises the following component projects:

* Operator Controller: The central component of OLM v1 that extends Kubernetes with an API through which users can install and manage the lifecycle of Operators and extensions. It consumes information from catalogd.
* Catalogd: A Kubernetes extension that unpacks file-based catalog (FBC) content packaged and shipped in container images for consumption by on-cluster clients. As a component of the OLM v1 microservices architecture, catalogd hosts metadata for Kubernetes extensions packaged by the authors of the extensions, and as a result helps users discover installable content.
* CRDs:

  + `clusterextension.olm.operatorframework.io`

    - Scope: Cluster
    - CR: `ClusterExtension`
  + `clustercatalog.olm.operatorframework.io`

    - Scope: Cluster
    - CR: `ClusterCatalog`
* See the following projects in the *Additional resources* section:

  + `operator-framework/operator-controller`
  + `operator-framework/catalogd`

### [3.3. Viewing the cluster capabilities](#viewing-cluster-capabilities_cluster-capabilities) Copy linkLink copied to clipboard!

As a cluster administrator, you can view the capabilities by using the `clusterversion` resource status.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).

**Procedure**

* To view the status of the cluster capabilities, run the following command:

  ```
  $ oc get clusterversion version -o jsonpath='{.spec.capabilities}{"\n"}{.status.capabilities}{"\n"}'
  ```

  **Example output**

  ```
  {"additionalEnabledCapabilities":["openshift-samples"],"baselineCapabilitySet":"None"}
  {"enabledCapabilities":["openshift-samples"],"knownCapabilities":["CSISnapshot","Console","Insights","Storage","baremetal","marketplace","openshift-samples"]}
  ```

### [3.4. Enabling the cluster capabilities by setting baseline capability set](#enabling-baseline-capability-set_cluster-capabilities) Copy linkLink copied to clipboard!

As a cluster administrator, you can enable cluster capabilities any time after a OpenShift Container Platform installation by setting the `baselineCapabilitySet` configuration parameter.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).

**Procedure**

* To set the `baselineCapabilitySet` configuration parameter, run the following command:

  ```
  $ oc patch clusterversion version --type merge -p '{"spec":{"capabilities":{"baselineCapabilitySet":"vCurrent"}}}'
  ```

  For `baselineCapabilitySet` you can specify `vCurrent`, `v4.22`, or `None`.

### [3.5. Enabling the cluster capabilities by setting additional enabled capabilities](#enabling-additional-enabled-capabilities_cluster-capabilities) Copy linkLink copied to clipboard!

As a cluster administrator, you can enable cluster capabilities any time after a OpenShift Container Platform installation by setting the `additionalEnabledCapabilities` configuration parameter.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. View the additional enabled capabilities by running the following command:

   ```
   $ oc get clusterversion version -o jsonpath='{.spec.capabilities.additionalEnabledCapabilities}{"\n"}'
   ```

   **Example output**

   ```
   ["openshift-samples"]
   ```
2. To set the `additionalEnabledCapabilities` configuration parameter, run the following command:

   ```
   $ oc patch clusterversion/version --type merge -p '{"spec":{"capabilities":{"additionalEnabledCapabilities":["openshift-samples", "marketplace"]}}}'
   ```

   Important

   You cannot disable a capability that is already enabled in a cluster. The cluster version Operator (CVO) continues to reconcile the capability which is already enabled in the cluster.

   If you try to disable a capability, then CVO shows the divergent spec:

   ```
   $ oc get clusterversion version -o jsonpath='{.status.conditions[?(@.type=="ImplicitlyEnabledCapabilities")]}{"\n"}'
   ```

   **Example output**

   ```
   {"lastTransitionTime":"2022-07-22T03:14:35Z","message":"The following capabilities could not be disabled: openshift-samples","reason":"CapabilitiesImplicitlyEnabled","status":"True","type":"ImplicitlyEnabledCapabilities"}
   ```

   Note

   During the cluster upgrades, it is possible that a given capability could be implicitly enabled. If a resource was already running on the cluster before the upgrade, then any capabilities that is part of the resource will be enabled. For example, during a cluster upgrade, a resource that is already running on the cluster has been changed to be part of the `marketplace` capability by the system. Even if a cluster administrator does not explicitly enabled the `marketplace` capability, it is implicitly enabled by the system.

## [Chapter 4. Support for FIPS cryptography](#installing-fips) Copy linkLink copied to clipboard!

You can install an OpenShift Container Platform cluster in FIPS mode.

OpenShift Container Platform is designed for FIPS. When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86\_64, ppc64le, and s390x architectures.

For more information about the NIST validation program, see "Cryptographic Module Validation Program" in the *Additional resources* section. For the latest NIST status for the individual versions of RHEL cryptographic libraries that have been submitted for validation, see "Compliance Activities and Government Standards" in the *Additional resources* section.

Important

To enable FIPS mode for your cluster, you must run the installation program from a RHEL 9 computer that is configured to operate in FIPS mode, and you must use a FIPS-capable version of the installation program. See the section titled *Obtaining a FIPS-capable installation program using `oc adm extract`*.

For more information about configuring FIPS mode on RHEL, see "Installing the system in FIPS mode" in the *Additional resources* section.

For the Red Hat Enterprise Linux CoreOS (RHCOS) machines in your cluster, this change is applied when the machines are deployed based on the status of an option in the `install-config.yaml` file, which governs the cluster options that a user can change during cluster deployment. With Red Hat Enterprise Linux (RHEL) machines, you must enable FIPS mode when you install the operating system on the machines that you plan to use as worker machines.

Because FIPS must be enabled before the operating system that your cluster uses boots for the first time, you cannot enable FIPS after you deploy a cluster.

### [4.1. Obtaining a FIPS-capable installation program using oc adm extract](#installation-obtaining-fips-installer-oc_installing-fips) Copy linkLink copied to clipboard!

You must get a FIPS-capable installation binary to install a OpenShift Container Platform cluster in FIPS mode. Extract the binary from the release image by using the OpenShift CLI (`oc`). After you get the binary, you must proceed with the cluster installation, replacing all instances of the `openshift-install` command with `openshift-install-fips`.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`) with version 4.16 or newer.

**Procedure**

1. Extract the FIPS-capable binary from the installation program by running the following command:

   ```
   $ oc adm release extract --registry-config "${pullsecret_file}" --command=openshift-install-fips --to "${extract_dir}" ${RELEASE_IMAGE}
   ```

   where:

   `<pullsecret_file>`
   :   Specifies the name of a file that contains your pull secret.

   `<extract_dir>`
   :   Specifies the directory where you want to extract the binary.

   `<RELEASE_IMAGE>`
   :   Specifies the Quay.io URL of the OpenShift Container Platform release you are using. For more information on finding the release image, see *Extracting the OpenShift Container Platform installation program*.
2. Proceed with cluster installation, replacing all instances of the `openshift-install` command with `openshift-install-fips`.

### [4.3. Obtaining a FIPS-capable installation program using the public OpenShift mirror](#installation-obtaining-fips-installer-mirror_installing-fips) Copy linkLink copied to clipboard!

OpenShift Container Platform requires the use of a FIPS-capable installation binary to install a cluster in FIPS mode. You can obtain this binary by downloading it from the public OpenShift mirror. After you have obtained the binary, proceed with the cluster installation, replacing all instances of the `openshift-install` binary with `openshift-install-fips`.

**Prerequisites**

* You have access to the internet.

**Procedure**

1. Download the installation program from <https://mirror.openshift.com/pub/openshift-v4/clients/ocp/latest-4.18/openshift-install-rhel9-amd64.tar.gz>.
2. Extract the installation program. For example, on a computer that uses a Linux operating system, run the following command:

   ```
   $ tar -xvf openshift-install-rhel9-amd64.tar.gz
   ```
3. Proceed with cluster installation, replacing all instances of the `openshift-install` command with `openshift-install-fips`.

### [4.4. FIPS validation in OpenShift Container Platform](#installation-about-fips-validation_installing-fips) Copy linkLink copied to clipboard!

OpenShift Container Platform uses certain FIPS validated or Modules In Process modules within RHEL and RHCOS for the operating system components that it uses.

For more information, see "RHEL core crypto components" in the *Additional resources* section. For example, when users use SSH to connect to OpenShift Container Platform clusters and containers, those connections are properly encrypted.

OpenShift Container Platform components are written in Go and built with Red Hat’s golang compiler. When you enable FIPS mode for your cluster, all OpenShift Container Platform components that require cryptographic signing call RHEL and RHCOS cryptographic libraries.

Expand

Table 4.1. FIPS mode attributes and limitations in OpenShift Container Platform 4.22

| Attributes | Limitations |
| --- | --- |
| FIPS support in RHEL 9 and RHCOS operating systems. | The FIPS implementation does not use a function that performs hash computation and signature generation or validation in a single step. This limitation will continue to be evaluated and improved in future OpenShift Container Platform releases. |
| FIPS support in CRI-O runtimes. |
| FIPS support in OpenShift Container Platform services. |
| FIPS validated or Modules In Process cryptographic module and algorithms that are obtained from RHEL 9 and RHCOS binaries and images. |
| Use of FIPS compatible golang compiler. | TLS FIPS support is not complete but is planned for future OpenShift Container Platform releases. |
| FIPS support across multiple architectures. | FIPS is currently only supported on OpenShift Container Platform deployments using `x86_64`, `ppc64le`, and `s390x` architectures. |

Show more

### [4.5. FIPS support in components that the cluster uses](#installation-about-fips-components_installing-fips) Copy linkLink copied to clipboard!

Although the OpenShift Container Platform cluster itself uses FIPS validated or Modules In Process modules, ensure that the systems that support your OpenShift Container Platform cluster use FIPS validated or Modules In Process modules for cryptography.

etcd
:   To ensure that the secrets that are stored in etcd use FIPS validated or Modules In Process encryption, boot the node in FIPS mode. After you install the cluster in FIPS mode, you can encrypt the etcd data by using the FIPS-approved `aes cbc` cryptographic algorithm.

Storage
:   For local storage, use RHEL-provided disk encryption or Container Native Storage that uses RHEL-provided disk encryption. By storing all data in volumes that use RHEL-provided disk encryption and enabling FIPS mode for your cluster, both data at rest and data in motion, or network data, are protected by FIPS validated or Modules In Process encryption. You can configure your cluster to encrypt the root filesystem of each node. For more information, see "Customizing nodes" in the *Additional resources* section.

Runtimes
:   To ensure that containers know that they are running on a host that is using FIPS validated or Modules In Process cryptography modules, use CRI-O to manage your runtimes.

### [4.6. Installation of a cluster in FIPS mode](#installing-fips-mode_installing-fips) Copy linkLink copied to clipboard!

To install a cluster in FIPS mode, follow the instructions to install a customized cluster on your preferred infrastructure. Ensure that you set `fips: true` in the `install-config.yaml` file before you deploy your cluster.

Important

To enable FIPS mode for your cluster, you must run the installation program from a RHEL computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Installing the system in FIPS mode](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/security_hardening/assembly_installing-the-system-in-fips-mode_security-hardening).

* [Amazon Web Services](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-customizations)
* [Microsoft Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installing-azure-customizations)
* [Bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal)
* [Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installing-gcp-customizations)
* [IBM Cloud®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_cloud/#installing-ibm-cloud-customizations)
* [IBM Power®](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power/#installing-ibm-power)
* [IBM Z® and IBM® LinuxONE](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z)
* [IBM Z® and IBM® LinuxONE with RHEL KVM](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-kvm)
* [IBM Z® and IBM® LinuxONE in an LPAR](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_z_and_ibm_linuxone/#installing-ibm-z-lpar)
* [Red Hat OpenStack Platform (RHOSP)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_openstack/#installing-openstack-installer-custom)
* [VMware vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere)

Note

If you are using Azure File storage, you cannot enable FIPS mode.

To apply `AES CBC` encryption to your etcd data store, follow the "Encrypting etcd data" process after you install your cluster.

## [Legal Notice](#idm139645397856912) Copy linkLink copied to clipboard!

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
