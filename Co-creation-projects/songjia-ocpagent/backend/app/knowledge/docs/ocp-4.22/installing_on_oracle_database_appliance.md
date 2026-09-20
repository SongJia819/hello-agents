---
title: "Installing on Oracle Database Appliance"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_oracle_database_appliance/index
retrieved_at: 2026-09-05T05:42:08.581005+00:00
---

# Installing on Oracle Database Appliance

---

OpenShift Container Platform 4.22

## Installing OpenShift Container Platform on Installing on Oracle Database Appliance

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140510641815488)

**Abstract**

This document describes how to install OpenShift Container Platform on Oracle Database Appliance.

---

## [Chapter 1. Installing a cluster on Oracle Database Appliance by using the Assisted Installer](#installing-oda-assisted-installer) Copy linkLink copied to clipboard!

You can use the Assisted Installer to install a cluster on Oracle Database Appliance (ODA).

### [1.1. Preparing the Oracle Database Appliance environment](#ai-oda-env_installing-oda-assisted-installer) Copy linkLink copied to clipboard!

Before you can deploy an OpenShift Container Platform cluster on Oracle Database Appliance (ODA), you must prepare the ODA environment.

**Prerequisites**

* You have reviewed the requirements and additional prerequisites described in section 1 of the [Red Hat OpenShift Container Platform on Oracle Database Appliance Deployment Guide](https://www.oracle.com/a/otn/docs/red-hat-openshift-container-platform-4-19.pdf) (Oracle documentation).

**Procedure**

1. Complete the pre-deployment tasks as described in section 2 of the "Red Hat OpenShift Container Platform on Oracle Database Appliance Deployment Guide".
2. Complete the final environment preparations as described in sections 3.1 and 3.2 of the "Red Hat OpenShift Container Platform on Oracle Database Appliance Deployment Guide".

### [1.2. Beginning the cluster installation and generating the Discovery ISO](#abi-oda-discovery-iso_installing-oda-assisted-installer) Copy linkLink copied to clipboard!

Begin installing the OpenShift Container Platform cluster in the Oracle Database Appliance (ODA) environment by using the Red Hat Hybrid Cloud Console.

**Procedure**

1. Log in to the [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift/cluster-list).
2. On the **Cluster List** page, click **Create cluster**.
3. Click the **Datacenter** tab.
4. Under **Assisted Installer**, click **Create cluster**.
5. Configure your cluster on the **Cluster details** page:

   1. Enter a name for the cluster in the **Cluster name** field.
   2. Enter a base domain for the cluster in the **Base domain** field. All subdomains for the cluster will use this base domain.

      Note

      The base domain must be a valid DNS name. You must not have a wildcard domain set up for the base domain.
   3. Select a version from the **OpenShift version** dropdown list. By default, the dropdown list displays the latest version.
   4. Optional: In the **Number of control plane nodes** field, select the number of control plane nodes for your installation from the dropdown menu. The default value is `3`.
   5. Optional: Select the **Include custom manifests** checkbox if you want to upload custom manifests to further configure your cluster. This option adds an additional page for custom manifests that you use later in the configuration process.

      Important

      If you have already added custom manifests, clearing the **Include custom manifests** checkbox automatically deletes them all. You must confirm the deletion.
   6. Click **Next** to continue. Once you proceed to the next page, you cannot go back to change any of these cluster details.
6. Choose additional Operators to install on the **Operators** page:

   1. If you want to install an Operator bundle, select an option in the **Bundles** section.
   2. If you want to install only some Operators, select the individual Operators from the **Single Operators** section.
   3. Click **Next** to continue.
7. Upload an SSH public key and generate the Discovery ISO:

   1. Click the **Add Hosts** button in the **Host Discovery** page.
   2. Upload an SSH public key in the **SSH public key** section so that you can connect to the cluster nodes as the `core` user. If you do not already have an SSH public key, see "Generating a key pair for cluster node SSH access" for more information.
   3. Select **Show proxy settings**.
   4. Enter values for the **HTTP proxy URL**, **HTTPS URL proxy**, and **No proxy domains** fields.
   5. Click **Generate Discovery ISO**.
8. Copy the command from the **Command to download the ISO** field and run the command as a root user in the ODA environment.

   **Example command**

   ```
   # wget -O discovery_image_example.iso 'https://api.openshift.com/api/assisted-images/bytoken/eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3Njg0Mjc3MDIsInN1YiI6ImNhMzZjZWU1LTQ3ZWEtNDc0Ny05OTg5LTVhZTYyMmMzMjZlNSJ9.jl-HvaxBR-WX73vpxO-Fy65bmY-RE5iL6AqL0wbWCmE/4.20/x86_64/minimal.iso'
   ```

### [1.3. Creating nodes in the Oracle Database Appliance environment](#abi-oda-create-nodes_installing-oda-assisted-installer) Copy linkLink copied to clipboard!

After generating and downloading the Discovery ISO to your Oracle Database Appliance (ODA) environment, create control plane nodes and worker nodes in the environment.

**Procedure**

1. Run the script to create control plane nodes as described in section 3.4 of the [Red Hat OpenShift Container Platform on Oracle Database Appliance Deployment Guide](https://www.oracle.com/a/otn/docs/red-hat-openshift-container-platform-4-19.pdf) (Oracle documentation).
2. Run the script to create worker nodes as described in section 3.5 of the "Red Hat OpenShift Container Platform on Oracle Database Appliance Deployment Guide".
3. Update the MAC address for each node as described in section 3.6 of the "Red Hat OpenShift Container Platform on Oracle Database Appliance Deployment Guide".

### [1.4. Completing host discovery and starting cluster installation](#abi-oda-start-install_installing-oda-assisted-installer) Copy linkLink copied to clipboard!

After preparing control plane and worker nodes in the Oracle Database Appliance (ODA) environment, complete host discovery and initiate the cluster installation.

As you create hosts using the provided scripts, the hosts begin to appear in the table of the **Host Discovery** page, where you can configure the hosts as needed.

**Procedure**

1. Go to the **Host Discovery** page.
2. Assign host roles in the **Host Inventory** table:

   1. In the **Role** column of the table, expand the **Auto-Assign** arrow for the host.
   2. Assign the host with either a **Control Plane node** or a **Worker** role.
   3. Repeat this process for each host in the table.
3. Click **Next**.
4. On the **Storage** page, verify storage details and configure host storage as needed.
5. Click **Next**.
6. Configure networking details on the **Networking** page:

   1. Select **User-Managed Networking** as the **Network Management** type.
   2. Select **Host SSH Public Key for troubleshooting after installation** to connect to hosts using a public SSH key for troubleshooting after installation.
7. Click **Next**.
8. Validate cluster details on the **Review and create** page.
9. Click **Install cluster** to begin the installation.
10. Monitor installation progress and wait for all nodes to reach a `Ready` state.

### [1.5. Completing the installation](#abi-oda-complete-install_installing-oda-assisted-installer) Copy linkLink copied to clipboard!

After the cluster is installed and initialized, the Assisted Installer indicates that the installation is finished. The Assisted Installer provides the console URL, the `kubeadmin` username and password, and the `kubeconfig` file.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Make a copy of the `kubeadmin` username and password.
2. Download the `kubeconfig` file and copy it to the auth directory under your working directory by running the following commands:

   ```
   $ mkdir -p <working_directory>/auth
   ```

   ```
   $ cp kubeconfig <working_directory>/auth
   ```

   Note

   The `kubeconfig` file is available for download for 20 days after completing the installation.
3. Add the `kubeconfig` file to your environment by running the following command:

   ```
   $ export KUBECONFIG=<working_directory>/auth/kubeconfig
   ```
4. Log in with the OpenShift CLI (`oc`) by running the following command:

   ```
   $ oc login -u kubeadmin -p <password>
   ```

   Replace `<password>` with the password of the `kubeadmin` user.
5. Click the web console URL or click **Launch OpenShift Console** to open the console.
6. Enter the `kubeadmin` username and password. Follow the instructions in the OpenShift Container Platform console to configure an identity provider and configure alert receivers.

## [Legal Notice](#idm140510641815488) Copy linkLink copied to clipboard!

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
