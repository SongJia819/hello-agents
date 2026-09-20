---
title: "Installing on Oracle Distributed Cloud"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_oracle_distributed_cloud/index
retrieved_at: 2026-09-05T05:42:08.865341+00:00
---

# Installing on Oracle Distributed Cloud

---

OpenShift Container Platform 4.22

## Installing OpenShift Container Platform on Oracle Distributed Cloud

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140295380332752)

**Abstract**

This document describes how to install OpenShift Container Platform on Oracle Distributed Cloud Infrastructure.

---

## [Chapter 1. Installing a cluster on Oracle Distributed Cloud by using the Assisted Installer](#installing-oci-assisted-installer) Copy linkLink copied to clipboard!

You can use the Assisted Installer to install a cluster on Oracle® Distributed Cloud. This method is recommended for most users, and requires an internet connection.

If you want to set up the cluster manually or using other automation tools, or if you are working in a disconnected environment, you can use the Red Hat Agent-based Installer for the installation. For details, see "Installing a cluster on Oracle Distributed Cloud by using the Agent-based Installer".

### [1.1. Supported Oracle Distributed Cloud infrastructures](#installing-oci-distributed-infra-support_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

There are several different Oracle® Distributed Cloud infrastructure offerings you can choose for your installation.

The following table describes the support status of each Oracle® Distributed Cloud infrastructure offering:

Expand

Table 1.1. Oracle Distributed Cloud infrastructure support statuses

| Infrastructure type | Support status |
| --- | --- |
| Commercial Public Cloud | General Availability |
| Dedicated Region | General Availability |
| US Government Cloud | Technology Preview |
| UK Government Cloud | General Availability |
| EU Sovereign Cloud | Technology Preview |
| Isolated Region | Technology Preview |
| Oracle Alloy | General Availability |

Show more

### [1.2. About the Assisted Installer and Oracle Distributed Cloud integration](#installing-oci-about-assisted-installer_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

You can run cluster workloads on Oracle® Distributed Cloud infrastructure that supports dedicated, hybrid, public, and multiple cloud environments. Both Red Hat and Oracle test, validate, and support running an OpenShift Container Platform cluster on Oracle Distributed Cloud.

This section explains how to use the Assisted Installer to install an OpenShift Container Platform cluster on the Oracle Cloud Infrastructure (OCI) platform. The installation deploys cloud-native components such as Oracle Cloud Controller Manager (CCM) and Oracle Container Storage Interface (CSI), and integrates your cluster with OCI API resources such as instance node, load balancer, and storage.

The installation process uses the OpenShift Container Platform discovery ISO image provided by Red Hat, together with the scripts and manifests provided and maintained by Oracle.

#### [1.2.1. Preinstallation considerations](#installing-oci-preinstallation-considerations_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

Before installing OpenShift Container Platform on Oracle Distributed Cloud, you must consider the following configuration choices.

Deployment platforms
:   The integration between OpenShift Container Platform and Oracle Distributed Cloud is certified on both virtual machines (VMs) and bare-metal (BM) machines. Bare-metal installations using iSCSI boot drives require a secondary vNIC that is automatically created in the Terraform stack provided by Oracle.

    Before you create a virtual machine (VM) or bare-metal (BM) machine, you must identify the relevant OCI shape. For details, see "Cloud instance types".

VPU sizing recommendations
:   To ensure the best performance conditions for your cluster workloads that operate on Oracle Distributed Cloud, ensure that volume performance units (VPUs) for your block volume are sized for your workloads. The following list provides guidance for selecting the VPUs needed for specific performance needs:

    * Test or proof of concept environment: 100 GB, and 20 to 30 VPUs.
    * Basic environment: 500 GB, and 60 VPUs.
    * Heavy production environment: More than 500 GB, and 100 or more VPUs.

    Consider reserving additional VPUs to provide sufficient capacity for updates and scaling activities. For more information about VPUs, see "Volume Performance Units".

Instance sizing recommendations
:   Find recommended values for compute instance CPU, memory, VPU, and volume size for OpenShift Container Platform nodes. For details, see "Instance Sizing Recommendations for OpenShift Container Platform Nodes".

#### [1.2.2. Workflow](#installing-oci-workflow_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

**Figure 1.1. High-level workflow for using the Assisted Installer in a connected environment to install a cluster on Oracle Distributed Cloud**

The procedure for using the Assisted Installer in a connected environment to install a cluster on Oracle Distributed Cloud is outlined below:

1. In the Oracle Cloud Infrastructure (OCI) console, configure an OCI account to host the cluster:

   1. Create a new child compartment under an existing compartment.
   2. Create a new object storage bucket or use one provided by Oracle Distributed Cloud.
   3. Download the stack file template stored locally.
2. In the Assisted Installer console, set up a cluster:

   1. Enter the cluster configurations.
   2. Generate and download the discovery ISO image.
3. In the OCI console, create the infrastructure:

   1. Upload the discovery ISO image to the OCI bucket.
   2. Create a Pre-Authenticated Request (PAR) for the ISO image.
   3. Upload the stack file template, and use it to create and apply the stack.
   4. Copy the custom manifest YAML file from the stack.
4. In the Assisted Installer console, complete the cluster installation:

   1. Set roles for the cluster nodes.
   2. Upload the manifests provided by Oracle.
   3. Install the cluster.

Important

The steps for provisioning OCI resources are provided as an example only. You can also choose to create the required resources through other methods; the scripts are just an example. Installing a cluster with infrastructure that you provide requires knowledge of the cloud provider and the installation process on OpenShift Container Platform. You can access OCI configurations to complete these steps, or use the configurations to model your own custom script.

### [1.3. Preparing the Oracle Distributed Cloud environment](#creating-oci-resources-services_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

Before installing OpenShift Container Platform using Assisted Installer, create the necessary resources and download the configuration file in the Oracle Distributed Cloud environment.

**Prerequisites**

* You have an Oracle Cloud Infrastructure (OCI) account to host the cluster.
* If you use a firewall and you plan to use a Telemetry service, you configured your firewall to allow OpenShift Container Platform to access the sites required.

**Procedure**

1. Log in to your [OCI](https://cloud.oracle.com/a/) account with administrator privileges.
2. Configure the account by defining the [Cloud Accounts and Resources (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/install-prereq.htm). Ensure that you create the following resources:

   1. Create a child compartment for organizing, restricting access, and setting usage limits to OCI resources. For the full procedure, see [Creating a Compartment (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Identity/compartments/To_create_a_compartment.htm#To).
   2. Create a new object storage bucket into which you will upload the discovery ISO image. For the full procedure, see [Creating an Object Storage Bucket (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingbuckets_topic-To_create_a_bucket.htm#top).
3. Download the latest versions of the following configuration files from the [`oracle-quickstart/oci-openshift`](https://github.com/oracle-quickstart/oci-openshift/releases) releases page:

   * `create-resource-attribution-tags-vX.X.X.zip`: The Terraform stack for creating the required resource attribution tags in your OCI tenancy.

     Important

     Resource attribution tags are mandatory for OpenShift Container Platform on Oracle Distributed Cloud. If you have not previously applied the `create-resource-attribution-tags` stack in your tenancy, you must download and apply it before proceeding. After the tags exist, later cluster deployments can reuse them. For more details, see [OpenShift on OCI (OSO) Prerequisites](https://github.com/oracle-quickstart/oci-openshift?tab=readme-ov-file#prerequisites).
   * `create-cluster-vX.X.X.zip`: The Terraform stack and custom manifests for provisioning OCI resources and installing OpenShift Container Platform clusters on Oracle Distributed Cloud.

     The `create-cluster` configuration file contains the following:

     + **Terraform Stacks**: The Terraform stack code for provisioning OCI resources to create and manage OpenShift Container Platform clusters on Oracle Distributed Cloud.
     + **Custom Manifests**: The manifest files needed for the installation of OpenShift Container Platform clusters on Oracle Distributed Cloud.

     Note

     To make any changes to the manifests, you can clone the entire Oracle GitHub repository and access the `custom_manifests` and `terraform-stacks` directories directly. For details, see [Configuration Files (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/install-prereq.htm#install-configuration-files).

### [1.4. Using the Assisted Installer to generate a discovery ISO image](#using-assisted-installer-oci-agent-iso_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

Create the cluster configuration and generate the discovery ISO image in the Assisted Installer web console.

#### [1.4.1. Creating the cluster](#using-assisted-installer-oci-create-cluster_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

To begin creating the cluster, set the cluster details.

**Prerequisites**

* You created a child compartment and an object storage bucket on Oracle Distributed Cloud. For details, see *Preparing the Oracle Distributed Cloud environment*.
* You reviewed details about the OpenShift Container Platform installation and update processes.

**Procedure**

1. Log in to the [Assisted Installer web console](https://console.redhat.com/) with your credentials.
2. In the **Red Hat OpenShift** tile, select **OpenShift**.
3. In the **Red Hat OpenShift Container Platform** tile, select **Create Cluster**.
4. On the **Cluster Type** page, scroll down to the end of the **Cloud** tab, and select **Oracle Cloud Infrastructure (virtual machines)**.
5. On the **Create an OpenShift Cluster** page, select the **Interactive** tile.
6. On the **Cluster Details** page, complete the following fields:

   Expand

   | Field | Action required |
   | --- | --- |
   | **Cluster name** | Specify the name of your cluster, such as `oci`. This is the same value as the cluster name in Oracle Distributed Cloud. |
   | **Base domain** | Specify the base domain of the cluster, such as `openshift-demo.devcluster.openshift.com`.  This must be the same value as the zone DNS server in Oracle Distributed Cloud. |
   | **OpenShift version** | \* For installations on virtual machines only, specify `OpenShift 4.14` or a later version.  \* For installations that include bare metal machines, specify `OpenShift 4.16` or a later version. |
   | **CPU architecture** | Specify `x86_64` or `Arm64`. |
   | **Integrate with external partner platforms** | Specify `Oracle Cloud Infrastructure`.  After you specify this value, the **Include custom manifests** checkbox is selected by default and the **Custom manifests** page is added to the wizard. |

   Show more
7. Leave the default settings for the remaining fields, and click **Next**.
8. On the **Operators** page, click **Next**.

#### [1.4.2. Generating the Discovery ISO image](#using-assisted-installer-oci-generating-iso_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

After setting cluster details, generate and download the Discovery ISO image.

**Procedure**

1. On the **Host Discovery** page, click **Add hosts** and complete the following steps:

   1. For the **Provisioning type** field, select **Minimal image file**.
   2. For the **SSH public key** field, add the SSH public key from your local system, by copying the output of the following command:

      ```
      $ cat ~/.ssh/id_rsa.put
      ```

      The SSH public key will be installed on all OpenShift Container Platform control plane and compute nodes.
   3. Click **Generate Discovery ISO** to generate the discovery ISO image file.
   4. Click **Download Discovery ISO** to save the file to your local system.

### [1.5. Provisioning OCI infrastructure for your cluster](#provision-oci-infrastructure-ocp-cluster_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

When using the Assisted Installer to create details for your OpenShift Container Platform cluster, you specify these details in a Terraform stack.

A stack is an Oracle Cloud Infrastructure (OCI) feature that automates the provisioning of all necessary OCI infrastructure resources that are required for installing an OpenShift Container Platform cluster on Oracle Distributed Cloud.

**Prerequisites**

* You downloaded the discovery ISO image to a local directory. For details, see *Using the Assisted Installer to generate a discovery ISO image*.
* You downloaded the Terraform stack template to a local directory. For details, see "Preparing the Oracle Distributed Cloud environment".

**Procedure**

1. Log in to your [Oracle Distributed Cloud](https://cloud.oracle.com/a/) account.
2. Upload the discovery ISO image from your local drive to the new object storage bucket you created. For the full procedure, see [Uploading an Object Storage Object to a Bucket (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/managingobjects_topic-To_upload_objects_to_a_bucket.htm).
3. Locate the uploaded discovery ISO, and complete the following steps:

   1. Create a Pre-Authenticated Request (PAR) for the ISO from the adjacent options menu.
   2. Copy the generated URL to use as the OpenShift Image Source URI in the next step.

   For the full procedure, see [Creating a Pre-Authenticated Requests in Object Storage (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/Object/Tasks/usingpreauthenticatedrequests_topic-To_create_a_preauthenticated_request_for_all_objects_in_a_bucket.htm).
4. If you have not already done so, apply the `create-resource-attribution-tags` Terraform stack to create the required resource attribution tags:

   Important

   Resource attribution tags are mandatory for OpenShift Container Platform on Oracle Distributed Cloud. If the tags do not already exist in your tenancy, you must apply the `create-resource-attribution-tags` stack before creating the cluster. You typically apply this stack once for the first cluster deployment in a tenancy. After the tags exist, later cluster deployments can reuse them.

   1. In the Oracle Distributed Cloud console, navigate to **Resource Manager** → **Stacks** and click **Create Stack**.
   2. Upload the `create-resource-attribution-tags-vX.X.X.zip` file and click **Next**.
   3. Click **Apply** to create the resource attribution tags.

   For details, see [create-resource-attribution-tags (Oracle GitHub)](https://github.com/oracle-quickstart/oci-openshift/tree/main/terraform-stacks/create-resource-attribution-tags).
5. Create and apply the `create-cluster` Terraform stack:

   Important

   The Terraform stack includes files for creating cluster resources and custom manifests. The stack also includes a script, and when you apply the stack, the script creates OCI resources, such as DNS records, an instance, and other resources. For a list of the resources, see the `terraform-stacks` folder in [OpenShift on OCI (OSO)](https://github.com/oracle-quickstart/oci-openshift/tree/main).

   1. Upload the Terraform stacks template [terraform-stacks](https://github.com/oracle-quickstart/oci-openshift/tree/main/terraform-stacks) to the new object storage bucket.
   2. Complete the stack information and click **Next**.

      Important

      * Make sure that **Cluster Name** matches **Cluster Name** in Assisted Installer, and **Zone DNS** matches **Base Domain** in Assisted Installer.
      * In the **OpenShift Image Source URI** field, paste the Pre-Authenticated Request URL link that you generated in the previous step.
      * Ensure that the correct **Compute Shape** field value is defined, depending on whether you are installing on bare metal or a virtual machine. If not, select a different shape from the list. For details, see [Compute Shapes (Oracle documentation)](docs.oracle.com/en-us/iaas/Content/Compute/References/computeshapes.htm).
   3. Click **Apply** to apply the stack.

   For the full procedure, see [Creating OpenShift Container Platform Infrastructure Using Resource Manager (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/openshift-on-oci/installing-assisted.htm#install-cluster-apply-stack).
6. Copy the `dynamic_custom_manifest.yml` file from the **Outputs** page of the Terraform stack.

   Note

   The YAML file contains all the required manifests, concatenated and preformatted with the configuration values. For details, see the [Custom Manifests README file](https://github.com/oracle-openshift/oci-openshift/blob/main/custom_manifests/README.md).

   For the full procedure, see [Getting the OpenShift Container Platform Custom Manifests for Installation (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/openshift-on-oci/installing-assisted.htm#install-cluster-edit-manifests).

### [1.6. Completing the remaining Assisted Installer steps](#completing-assisted-installer-oci_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

After you provision Oracle® Distributed Cloud resources and upload OpenShift Container Platform custom manifest configuration files to Oracle Distributed Cloud, you must complete the remaining cluster installation steps on the Assisted Installer before you can create an Oracle Distributed Cloud instance. These steps include assigning node roles and adding custom manifests.

#### [1.6.1. Assigning node roles](#assigning-node-roles-oci_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

Following host discovery, the role of all nodes appears as **Auto-assign** by default. Change each of the node roles to either **Control Plane node** or **Worker**.

**Prerequisites**

* You created and applied the Terraform stack in Oracle Distributed Cloud. For details, see "Provisioning OCI infrastructure for your cluster".

**Procedure**

1. From the Assisted Installer user interface, go to the **Host discovery** page.
2. Under the **Role** column, select either **Control plane node** or **Worker** for each targeted hostname. Then click **Next**.

   Note

   1. Before continuing to the next step, wait for each node to reach `Ready` status.
   2. Expand the node to verify that the hardware type is bare metal.
3. Accept the default settings for the **Storage** and **Networking** pages. Then click **Next**.

#### [1.6.2. Adding custom manifests](#adding-custom-manifests-oci_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

Add the mandatory custom manifests provided by Oracle.

For details, see [Custom Manifests (Oracle documentation).](https://github.com/dfoster-oracle/oci-openshift/blob/v1.0.0-release-preview/custom_manifests/README.md)

**Prerequisites**

* You copied the `dynamic_custom_manifest.yml` file from the Terraform stack in Oracle Distributed Cloud. For details, see "Provisioning OCI infrastructure for your cluster".

**Procedure**

1. On the **Custom manifests** page, in the **Folder** field, select `manifests`. This is the Assisted Installer folder where you want to save the custom manifest file.
2. In the **File name** field, enter a filename, for example, `dynamic_custom_manifest.yml`.
3. Paste the contents of the `dynamic_custom_manifest.yml` file that you copied from Oracle Distributed Cloud:

   1. In the **Content** section, click the **Paste content** icon.
   2. If you are using Firefox, click **OK** to close the dialog box, and then press **Ctrl+V**. Otherwise, skip this step.
4. Click **Next** to save the custom manifest.
5. From the **Review and create** page, click **Install cluster** to create your OpenShift Container Platform cluster on Oracle Distributed Cloud.

   After the cluster installation and initialization operations, the Assisted Installer indicates the completion of the cluster installation operation. For more information, see "Completing the installation" section in the Assisted Installer for OpenShift Container Platform document.

### [1.7. Verifying a successful cluster installation on Oracle Distributed Cloud](#verifying-cluster-install-ai-oci_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

Verify that your cluster was installed and is running effectively on Oracle® Distributed Cloud.

**Procedure**

1. From the [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift), go to **Clusters > Assisted Clusters** and select your cluster’s name.
2. On the **Installation Progress** page, check that the Installation progress bar is at 100% and a message displays indicating `Installation completed successfully`.
3. Under **Host inventory**, confirm that the status of all control plane and compute nodes is `Installed`.

   Note

   OpenShift Container Platform designates one of the control plane nodes as the bootstrap virtual machine, eliminating the need for a separate bootstrap machine.
4. Click the Web Console URL, to access the OpenShift Container Platform web console.
5. From the menu, select **Compute > Nodes**.
6. Locate your node from the **Nodes** table.
7. From the **Terminal** tab, verify that iSCSI appears next to the serial number.
8. From the **Overview** tab, check that your node has a **Ready** status.
9. Select the **YAML** tab.
10. Check the `labels` parameter, and verify that the listed labels apply to your configuration. For example, the `topology.kubernetes.io/region=us-sanjose-1` label indicates in what Oracle Distributed Cloud region the node was deployed.

### [1.8. Adding hosts to the cluster following the installation](#installing-oci-adding-hosts-day-two_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

After creating a cluster with the Assisted Installer, you can use the Red Hat Hybrid Cloud Console to add new host nodes to the cluster and approve their certificate signing requests (CSRs).

**Procedure**

* See the instructions in [Adding Nodes to a Cluster (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/openshift-on-oci/adding-nodes.htm).

### [1.9. Installation troubleshooting of a cluster on Oracle Distributed Cloud](#installing-troubleshooting-assisted-installer-oci_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

If you experience issues with using the Assisted Installer to install an OpenShift Container Platform cluster on Oracle® Distributed Cloud, you can troubleshoot the installation.

Read the following sections to troubleshoot common problems.

#### [1.9.1. The Ingress Load Balancer in Oracle Distributed Cloud is not at a healthy status](#installing-troubleshooting-load-balancer_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

This issue is classed as a `Warning` because by using Oracle Distributed Cloud to create a stack, you created a pool of compute nodes, 3 by default, that are automatically added as backend listeners for the Ingress Load Balancer. By default, the OpenShift Container Platform deploys 2 router pods, which are based on the default values from the OpenShift Container Platform manifest files. The `Warning` is expected because a mismatch exists with the number of router pods available, 2, to run on the 3 compute nodes.

**Figure 1.2. Example of a `Warning` message that is under the Backend set information tab on Oracle Distributed Cloud**

You do not need to modify the Ingress Load Balancer configuration. Instead, you can point the Ingress Load Balancer to specific compute nodes that operate in your cluster on OpenShift Container Platform. To do this, use placement mechanisms, such as annotations, on OpenShift Container Platform to ensure router pods only run on the compute nodes that you originally configured on the Ingress Load Balancer as backend listeners.

#### [1.9.2. Oracle Distributed Cloud create stack operation fails with an Error: 400-InvalidParameter message](#installing-troubleshooting-stack-operation_installing-oci-assisted-installer) Copy linkLink copied to clipboard!

On attempting to create a stack on Oracle Distributed Cloud, you identified that the **Logs** section of the job outputs an error message. For example:

```
Error: 400-InvalidParameter, DNS Label oci-demo does not follow Oracle requirements
Suggestion: Please update the parameter(s) in the Terraform config as per error message DNS Label oci-demo does not follow Oracle requirements
Documentation: https://registry.terraform.io/providers/oracle/oci/latest/docs/resources/core_vcn
```

Go to the **Install OpenShift with the Assisted Installer** page on the Hybrid Cloud Console, and check the **Cluster name** field on the **Cluster Details** step. Remove any special characters, such as a hyphen (`-`), from the name, because these special characters are not compatible with the OCI naming conventions. For example, change `oci-demo` to `ocidemo`.

For more information, see "Red Hat Hybrid Cloud Console".

## [Chapter 2. Installing a cluster on Oracle Distributed Cloud by using the Agent-based Installer](#installing-oci-agent-based-installer) Copy linkLink copied to clipboard!

You can use the Agent-based Installer to install a cluster on Oracle® Distributed Cloud, so that you can run cluster workloads on infrastructure that supports dedicated, hybrid, public, and multiple cloud environments.

Installing a cluster on Oracle Distributed Cloud is supported for virtual machines (VMs) and bare-metal machines.

### [2.1. Supported Oracle Distributed Cloud infrastructures](#installing-oci-distributed-infra-support_installing-oci-agent-based-installer) Copy linkLink copied to clipboard!

There are several different Oracle® Distributed Cloud infrastructure offerings you can choose for your installation.

The following table describes the support status of each Oracle® Distributed Cloud infrastructure offering:

Expand

Table 2.1. Oracle Distributed Cloud infrastructure support statuses

| Infrastructure type | Support status |
| --- | --- |
| Commercial Public Cloud | General Availability |
| Dedicated Region | General Availability |
| US Government Cloud | Technology Preview |
| UK Government Cloud | General Availability |
| EU Sovereign Cloud | Technology Preview |
| Isolated Region | Technology Preview |
| Oracle Alloy | General Availability |

Show more

### [2.2. The Agent-based Installer and Oracle Distributed Cloud overview](#installing-oci-about-agent-based-installer_installing-oci-agent-based-installer) Copy linkLink copied to clipboard!

You can install an OpenShift Container Platform cluster on Oracle® Distributed Cloud by using the Agent-based Installer. Red Hat and Oracle test, validate, and support running Oracle Distributed Cloud workloads in an OpenShift Container Platform cluster.

The Agent-based Installer provides the ease of use of the Assisted Installation service, but with the capability to install a cluster in either a connected or disconnected environment.

The following diagrams show workflows for connected and disconnected environments:

**Figure 2.1. Workflow for using the Agent-based installer in a connected environment to install a cluster on Oracle Cloud Infrastructure (OCI)**

**Figure 2.2. Workflow for using the Agent-based installer in a disconnected environment to install a cluster on OCI**

Oracle Distributed Cloud provides services that can meet your regulatory compliance, performance, and cost-effectiveness needs. Oracle Distributed Cloud supports 64-bit `x86` instances and 64-bit `ARM` instances.

Note

Consider selecting a nonvolatile memory express (NVMe) drive or a solid-state drive (SSD) for your boot disk, because these drives offer low latency and high throughput capabilities for your boot disk.

By running your OpenShift Container Platform cluster on Oracle Distributed Cloud, you can access the following capabilities:

* Compute flexible shapes, where you can customize the number of Oracle® CPUs (OCPUs) and memory resources for your VM. With access to this capability, a cluster’s workload can perform operations in a resource-balanced environment. You can find all RHEL-certified OCI shapes by going to the Oracle page on the Red Hat Ecosystem Catalog portal.
* Block Volume storage, where you can configure scaling and auto-tuning settings for your storage volume, so that the Block Volume service automatically adjusts the performance level to optimize performance.

Important

To ensure the best performance conditions for your cluster workloads that operate on Oracle Distributed Cloud and on the OCVS service, ensure volume performance units (VPUs) for your block volume is sized for your workloads. The following list provides some guidance in selecting the VPUs needed for specific performance needs:

* Test or proof of concept environment: 100 GB, and 20 to 30 VPUs.
* Basic environment: 500 GB, and 60 VPUs.
* Heavy production environment: More than 500 GB, and 100 or more VPUs.

Consider reserving additional VPUs to provide sufficient capacity for updates and scaling activities. For more information about VPUs, see Volume Performance Units (Oracle documentation).

### [2.3. Installation process workflow](#abi-oci-process-checklist_installing-oci-agent-based-installer) Copy linkLink copied to clipboard!

To better understand the process, see a high-level outline of installing an OpenShift Container Platform cluster on Oracle Distributed Cloud using the Agent-based Installer.

The following workflow describes the general installation process:

1. Create Oracle Cloud Infrastructure (OCI) resources and services (Oracle).
2. Disconnected environments: Prepare a web server that is accessible by OCI instances (Red Hat).
3. Prepare configuration files for the Agent-based Installer (Red Hat).
4. Generate the agent ISO image (Red Hat).
5. Disconnected environments: Upload the rootfs image to the web server (Red Hat).
6. Configure your firewall for OpenShift Container Platform (Red Hat).
7. Upload the agent ISO image to a storage bucket (Oracle).
8. Create a custom image from the uploaded agent ISO image (Oracle).
9. Create compute instances on Oracle Distributed Cloud (Oracle).
10. Verify that your cluster runs on Oracle Distributed Cloud (Oracle).

### [2.4. Creating OCI infrastructure resources and services](#abi-oci-resources-services_installing-oci-agent-based-installer) Copy linkLink copied to clipboard!

You must create an Oracle Distributed Cloud environment on your virtual machine (VM) or bare-metal shape. By creating this environment, you can install OpenShift Container Platform and deploy a cluster on an infrastructure that supports a wide range of cloud options and strong security policies.

Having prior knowledge of Oracle Cloud Infrastructure (OCI) components can help you with understanding the concept of OCI resources and how you can configure them to meet your organizational needs.

The Agent-based Installer method for installing an OpenShift Container Platform cluster on Oracle Distributed Cloud requires that you manually create OCI resources and services.

Important

To ensure compatibility with OpenShift Container Platform, you must set `A` as the record type for each DNS record and name records as follows:

* `api.<cluster_name>.<base_domain>`, which targets the `apiVIP` parameter of the API load balancer
* `api-int.<cluster_name>.<base_domain>`, which targets the `apiVIP` parameter of the API load balancer
* `*.apps.<cluster_name>.<base_domain>`, which targets the `ingressVIP` parameter of the Ingress load balancer

The `api.*` and `api-int.*` DNS records relate to control plane machines, so you must ensure that all nodes in your installed OpenShift Container Platform cluster can access these DNS records.

**Prerequisites**

* You configured an OCI account to host the OpenShift Container Platform cluster. See [Prerequisites (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/install-prereq.htm).

**Procedure**

* Create the required OCI resources and services.

  For installations in a connected environment, see [Provisioning Cluster Infrastructure Using Terraform (Oracle documentation)](https://docs.oracle.com/en-us/iaas/Content/openshift-on-oci/agent-installer-using-stack.htm).

  For installations in a disconnected environment, see [Provisioning OCI Resources for the Agent-based Installer in Disconnected Environments (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/agent-prereq.htm).

### [2.5. Creating configuration files for installing a cluster on Oracle Distributed Cloud](#creating-config-files-cluster-install-oci_installing-oci-agent-based-installer) Copy linkLink copied to clipboard!

You must create the `install-config.yaml` and the `agent-config.yaml` configuration files so that you can use the Agent-based Installer to generate a bootable ISO image. The Agent-based installation comprises a bootable ISO that has the Assisted discovery agent and the Assisted Service.

Both of these components are required to perform the cluster installation, but the latter component runs on only one of the hosts.

Note

You can also use the Agent-based Installer to generate or accept Zero Touch Provisioning (ZTP) custom resources.

**Prerequisites**

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing the method for users.
* You have read the "Preparing to install with the Agent-based Installer" documentation.
* You downloaded the Agent-Based Installer and the command-line interface (CLI) from the [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift/install/metal/agent-based).
* If you are installing in a disconnected environment, you have prepared a mirror registry in your environment and mirrored release images to the registry.

  Important

  Check that your `openshift-install` binary version relates to your local image container registry and not a shared registry, such as Red Hat Quay, by running the following command:

  ```
  $ ./openshift-install version
  ```

  **Example output for a shared registry binary**

  ```
  ./openshift-install 4.22.0
  built from commit ae7977b7d1ca908674a0d45c5c243c766fa4b2ca
  release image registry.ci.openshift.org/origin/release:4.22ocp-release@sha256:0da6316466d60a3a4535d5fed3589feb0391989982fba59d47d4c729912d6363
  release architecture amd64
  ```
* You have logged in to the OpenShift Container Platform with administrator privileges.

**Procedure**

1. Create an installation directory to store configuration files in by running the following command:

   ```
   $ mkdir ~/<directory_name>
   ```
2. Configure the `install-config.yaml` configuration file to meet the needs of your organization and save the file in the directory you created.

   **`install-config.yaml` file that sets an external platform**

   ```
   # install-config.yaml
   apiVersion: v1
   baseDomain: <base_domain>
   networking:
     clusterNetwork:
     - cidr: 10.128.0.0/14
       hostPrefix: 23
     network type: OVNKubernetes
     machineNetwork:
     - cidr: <ip_address_from_cidr>
     serviceNetwork:
     - 172.30.0.0/16
   compute:
     - architecture: amd64
     hyperthreading: Enabled
     name: worker
     replicas: 0
   controlPlane:
     architecture: amd64
     hyperthreading: Enabled
     name: master
     replicas: 3
   platform:
      external:
       platformName: oci
       cloudControllerManager: External
   sshKey: <public_ssh_key>
   pullSecret: '<pull_secret>'
   # ...
   ```

   where:

   `baseDomain`
   :   Specifies the base domain of your cloud provider.

   `machineNetwork.cidr`
   :   Specifies the IP address from the virtual cloud network (VCN) that the CIDR allocates to resources and components that operate on your network.

   `compute.architecture`
   :   Specifies the `compute.architecture` parameter. Depending on your infrastructure, you can select either `arm64` or `amd64`.

   `controlPlane.architecture`
   :   Specifies the `controlPlane.architecture` parameter. Depending on your infrastructure, you can select either `arm64` or `amd64`.

   `platformName`
   :   Specifies `OCI` as the external platform, so that OpenShift Container Platform can integrate with OCI.

   `sshKey`
   :   Specifies you SSH public key.

   `pullSecret`
   :   Specifies the pull secret that you need for authenticate purposes when downloading container images for OpenShift Container Platform components and services, such as Quay.io. See [Install OpenShift Container Platform 4](https://console.redhat.com/openshift/install/pull-secret) from the Red Hat Hybrid Cloud Console.
3. Create a directory on your local system named `openshift`. This must be a subdirectory of the installation directory.

   Important

   Do not move the `install-config.yaml` or `agent-config.yaml` configuration files to the `openshift` directory.
4. If you used a stack to provision OCI infrastructure resources: Copy and paste the `dynamic_custom_manifest` output of the OCI stack into a file titled `manifest.yaml` and save the file in the `openshift` directory.
5. If you did not use a stack to provision OCI infrastructure resources: Download and prepare custom manifests to create an Agent ISO image:

   1. Go to [Configuration Files](https://docs.oracle.com/iaas/Content/openshift-on-oci/install-prereq.htm#install-configuration-files) (Oracle documentation) and follow the link to the custom manifests directory on GitHub.
   2. Copy the contents of the `condensed-manifest.yml` file and save it locally to a file in the `openshift` directory.
   3. In the `condensed-manifest.yml` file, update the sections marked with `TODO` to specify the compartment Oracle® Cloud Identifier (OCID), VCN OCID, subnet OCID from the load balancer, and the security lists OCID.
6. Configure the `agent-config.yaml` configuration file to meet your organization’s requirements.

   **Sample `agent-config.yaml` file for an IPv4 network.**

   ```
   apiVersion: v1beta1
   metadata:
     name: <cluster_name>
     namespace: <cluster_namespace>
   rendezvousIP: <ip_address_from_CIDR>
   bootArtifactsBaseURL: <server_URL>
   # ...
   ```

   where:

   `name`
   :   Specifies the cluster name that you specified in your DNS record.

   `namespace`
   :   Specifies the namespace of your cluster on OpenShift Container Platform.

   `rendezvousIP`
   :   Specifies the `rendezvousIP` parameter. If you use IPv4 as the network IP address format, ensure that you set the `rendezvousIP` parameter to an IPv4 address that the VCN’s Classless Inter-Domain Routing (CIDR) method allocates on your network. Also ensure that at least one instance from the pool of instances that you booted with the ISO matches the IP address value you set for the `rendezvousIP` parameter.

   `bootArtifactsBaseURL`
   :   Specifies the URL of the server where you want to upload the rootfs image. This parameter is required only for disconnected environments.
7. Generate a minimal ISO image, which excludes the rootfs image, by entering the following command in your installation directory:

   ```
   $ ./openshift-install agent create image --log-level debug
   ```

   The command also completes the following actions:

   * Creates a subdirectory, `./<installation_directory>/auth directory:`, and places `kubeadmin-password` and `kubeconfig` files in the subdirectory.
   * Creates a `rendezvousIP` file based on the IP address that you specified in the `agent-config.yaml` configuration file.
   * Optional: Any modifications you made to `agent-config.yaml` and `install-config.yaml` configuration files get imported to the Zero Touch Provisioning (ZTP) custom resources.

     Important

     The Agent-based Installer uses Red Hat Enterprise Linux CoreOS (RHCOS). The rootfs image, which is mentioned in a later step, is required for booting, recovering, and repairing your operating system.
8. Disconnected environments only: Upload the rootfs image to a web server.

   1. Go to the `./<installation_directory>/boot-artifacts` directory that was generated when you created the minimal ISO image.
   2. Use your preferred web server, such as any Hypertext Transfer Protocol daemon (`httpd`), to upload the rootfs image to the location specified in the `bootArtifactsBaseURL` parameter of the `agent-config.yaml` file.

      For example, if the `bootArtifactsBaseURL` parameter states `http://192.168.122.20`, you would upload the generated rootfs image to this location so that the Agent-based installer can access the image from `http://192.168.122.20/agent.x86_64-rootfs.img`. After the Agent-based installer boots the minimal ISO for the external platform, the Agent-based Installer downloads the rootfs image from the `http://192.168.122.20/agent.x86_64-rootfs.img` location into the system memory.

      Note

      The Agent-based Installer also adds the value of the `bootArtifactsBaseURL` to the minimal ISO Image’s configuration, so that when the Operator boots a cluster’s node, the Agent-based Installer downloads the rootfs image into system memory.

      Important

      Consider that the full ISO image, which is in excess of `1` GB, includes the rootfs image. The image is larger than the minimal ISO Image, which is typically less than `150` MB.

### [2.6. Configuring your firewall for OpenShift Container Platform](#configuring-firewall-module_installing-oci-agent-based-installer) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform, you must configure your firewall to grant access to the sites that OpenShift Container Platform requires.

For a disconnected environment, you must mirror content from both Red Hat and Oracle. This environment requires that you create firewall rules to expose your firewall to specific ports and registries.

Note

If your environment has a dedicated load balancer in front of your OpenShift Container Platform cluster, review the allowlists between your firewall and load balancer to prevent unwanted network restrictions to your cluster.

**Procedure**

1. Allowlist the following container registry URLs for cluster installation and upgrades:

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `registry.redhat.io` | 443 | Provides core container images |
   | `access.redhat.com` | 443 | Hosts a signature store that a container client requires for verifying images pulled from `registry.access.redhat.com`. In a firewall environment, ensure that this resource is on the allowlist. |
   | `registry.access.redhat.com` | 443 | Hosts all the container images that are stored on the Red Hat Ecosystem Catalog, including core container images. |
   | `quay.io` | 443 | Provides core container images |
   | `cdn.quay.io` | 443 | Provides core container images |
   | `cdn01.quay.io` | 443 | Provides core container images |
   | `cdn02.quay.io` | 443 | Provides core container images |
   | `cdn03.quay.io` | 443 | Provides core container images |
   | `cdn04.quay.io` | 443 | Provides core container images |
   | `cdn05.quay.io` | 443 | Provides core container images |
   | `cdn06.quay.io` | 443 | Provides core container images |
   | `icr.io` | 443 | Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks. |
   | `cp.icr.io` | 443 | Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks. |

   Show more

   * You can use the wildcard `*.quay.io` instead of `cdn.quay.io` and `cdn0[1-6].quay.io` in your allowlist.
   * You can use the wildcard `*.access.redhat.com` to simplify the configuration and ensure that all subdomains, including `registry.access.redhat.com`, are allowed.
   * When adding a site such as `quay.io` to your allowlist, do not add a wildcard entry such as `*.quay.io` to your denylist. In most cases, image registries use a content delivery network (CDN) to serve images. If a firewall blocks access, image downloads are denied when the initial download request redirects to a hostname such as `cdn01.quay.io`.
2. Allowlist the following URLs to enable cluster access, authentication, and updates:

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `*.apps.<cluster_name>.<base_domain>` | 443 | Allowlist these URLs to enable cluster access, authentication, and updates. |
   | `api.openshift.com` | 443 | API endpoint for cluster tokens and update checks. |
   | `console.redhat.com` | 443 | Authentication service for cluster tokens. |
   | `sso.redhat.com` | 443 | The `https://console.redhat.com` site uses authentication from `sso.redhat.com` |

   Show more

   For egress traffic, Operators require route access to perform health checks to establish a connection for reaching endpoints. The authentication and web console Operators connect to two routes to verify functionality. Cluster administrators who do not want to allow `*.apps.<cluster_name>.<base_domain>`, must allow the following routes:

   * `oauth-openshift.apps.<cluster_name>.<base_domain>`
   * `canary-openshift-ingress-canary.apps.<cluster_name>.<base_domain>`
   * `console-openshift-console.apps.<cluster_name>.<base_domain>`, or the hostname that is specified in the `spec.route.hostname` field of the `consoles.operator/cluster` object if the field is not empty.
3. Allowlist the following registry URLs that host related artifacts for cluster installation and upgrades, such as installation content, release images, and client tools:

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `mirror.openshift.com` | 443 | Required to access mirrored installation content and images. This site is also a source of release image signatures, although the Cluster Version Operator needs only a single functioning source. |
   | `quayio-production-s3.s3.amazonaws.com` | 443 | Required to access Quay image content in AWS. |
   | `rhcos.mirror.openshift.com` | 443 | Required to download Red Hat Enterprise Linux CoreOS (RHCOS) images. |
   | `storage.googleapis.com/openshift-release` | 443 | A source of release image signatures, although the Cluster Version Operator needs only a single functioning source. |

   Show more
4. Set your firewall’s allowlist to include any site that provides resources for a language or framework that your builds require.
5. If you do not disable Telemetry, you must grant access to the following URLs to access Telemetry and Red Hat Lightspeed:

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `cert-api.access.redhat.com` | 443 | Required for Telemetry |
   | `api.access.redhat.com` | 443 | Required for Telemetry |
   | `infogw.api.openshift.com` | 443 | Required for Telemetry |
   | `console.redhat.com` | 443 | Required for Telemetry and for `insights-operator` |

   Show more
6. Set your firewall’s allowlist to include the following registry URLs:

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `api.openshift.com` | 443 | Required both for your cluster token and to check if updates are available for the cluster. |
   | `rhcos.mirror.openshift.com` | 443 | Required to download Red Hat Enterprise Linux CoreOS (RHCOS) images. |

   Show more
7. Set your firewall’s allowlist to include the following external URLs. Each repository URL hosts OCI containers. Consider mirroring images to as few repositories as possible to reduce any performance issues.

   Expand

   | URL | Port | Function |
   | --- | --- | --- |
   | `k8s.gcr.io` | port | A Kubernetes registry that hosts container images for a community-based image registry. This image registry is hosted on a custom Google Container Registry (GCR) domain. |
   | `ghcr.io` | port | A GitHub image registry where you can store and manage Open Container Initiative images. Requires an access token to publish, install, and delete private, internal, and public packages. |
   | `storage.googleapis.com` | 443 | A source of release image signatures, although the Cluster Version Operator needs only a single functioning source. |
   | `registry.k8s.io` | port | Replaces the `k8s.gcr.io` image registry because the `k8s.gcr.io` image registry does not support other platforms and vendors. |

   Show more

### [2.7. Running a cluster on Oracle Distributed Cloud](#running-cluster-oci-agent-based_installing-oci-agent-based-installer) Copy linkLink copied to clipboard!

To run a cluster on Oracle® Distributed Cloud, you must upload the generated agent ISO image to the default Object Storage bucket on Oracle Distributed Cloud.

Additionally, you must create a compute instance from the supplied base image, so that OpenShift Container Platform and Oracle Distributed Cloud can communicate with each other for the purposes of running the cluster on Oracle Distributed Cloud.

Note

Oracle Distributed Cloud supports the following OpenShift Container Platform cluster topologies:

* Installing an OpenShift Container Platform cluster on a single node.
* A highly available cluster that has a minimum of three control plane instances and two compute instances.
* A compact three-node cluster that has a minimum of three control plane instances.

**Prerequisites**

* You generated an agent ISO image. See the "Creating configuration files for installing a cluster on OCI" section.

**Procedure**

1. Upload the agent ISO image to Oracle’s default Object Storage bucket and import the agent ISO image as a custom image to this bucket. Ensure you that you configure the custom image to boot in Unified Extensible Firmware Interface (UEFI) mode. For more information, see [Creating the OpenShift Container Platform ISO Image (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/installing-agent-image-creation.htm).
2. Create a compute instance from the supplied base image for your cluster topology. See [Creating the OpenShift Container Platform cluster on OCI (Oracle documentation)](https://docs.oracle.com/iaas/Content/openshift-on-oci/installing-agent-first-node.htm).

   Important

   Before you create the compute instance, check that you have enough memory and disk resources for your cluster. Additionally, ensure that at least one compute instance has the same IP address as the address stated under `rendezvousIP` in the `agent-config.yaml` file.

### [2.8. Verifying that your Agent-based cluster installation runs on Oracle Distributed Cloud](#verifying-cluster-install-oci-agent-based_installing-oci-agent-based-installer) Copy linkLink copied to clipboard!

Verify that your cluster was installed and is running effectively on Oracle® Distributed Cloud.

**Prerequisites**

* You created all the required OCI resources and services. See the "Creating Oracle Distributed Cloud infrastructure resources and services" section.
* You created `install-config.yaml` and `agent-config.yaml` configuration files. See the "Creating configuration files for installing a cluster on Oracle Distributed Cloud" section.
* You uploaded the agent ISO image to a default Oracle Object Storage bucket, and you created a compute instance on Oracle Distributed Cloud. For more information, see "Running a cluster on Oracle Distributed Cloud".

**Procedure**

* After you deploy the compute instance on a self-managed node in your OpenShift Container Platform cluster, monitor the cluster’s status by choosing one of the following options:

  + From the OpenShift Container Platform CLI, enter the following command:

    ```
    $ ./openshift-install agent wait-for install-complete --log-level debug
    ```

    Check the status of the `rendezvous` host node that runs the bootstrap node. After the host reboots, the host forms part of the cluster.
  + Use the `kubeconfig` API to check the status of various OpenShift Container Platform components. For the `KUBECONFIG` environment variable, set the relative path of the cluster’s `kubeconfig` configuration file:

    ```
    $  export KUBECONFIG=~/auth/kubeconfig
    ```

    Check the status of each of the cluster’s self-managed nodes. CCM applies a label to each node to designate the node as running in a cluster on OCI.

    ```
    $ oc get nodes -A
    ```

    **Output example**

    ```
    NAME                                   STATUS ROLES                 AGE VERSION
    main-0.private.agenttest.oraclevcn.com Ready  control-plane, master 7m  v1.27.4+6eeca63
    main-1.private.agenttest.oraclevcn.com Ready  control-plane, master 15m v1.27.4+d7fa83f
    main-2.private.agenttest.oraclevcn.com Ready  control-plane, master 15m v1.27.4+d7fa83f
    ```

    Check the status of each of the cluster’s Operators, with the CCM Operator status being a good indicator that your cluster is running.

    ```
    $ oc get co
    ```

    **Truncated output example**

    ```
    NAME           VERSION     AVAILABLE  PROGRESSING    DEGRADED   SINCE   MESSAGE
    authentication 4.22.0-0    True       False          False      6m18s
    baremetal      4.22.0-0    True       False          False      2m42s
    network        4.22.0-0    True       True           False      5m58s  Progressing: …
        …
    ```

## [Legal Notice](#idm140295380332752) Copy linkLink copied to clipboard!

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
