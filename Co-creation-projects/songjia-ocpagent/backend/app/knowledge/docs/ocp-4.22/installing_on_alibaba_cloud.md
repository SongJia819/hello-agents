---
title: "Installing on Alibaba Cloud"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_alibaba_cloud/index
retrieved_at: 2026-09-05T05:41:56.141746+00:00
---

# Installing on Alibaba Cloud

---

OpenShift Container Platform 4.22

## Installing OpenShift Container Platform on Alibaba Cloud

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140372590960080)

**Abstract**

This document describes how to install OpenShift Container Platform on Alibaba Cloud.

---

## [Chapter 1. Installing a cluster on Alibaba Cloud by using the Assisted Installer](#installing-alibaba-assisted-installer) Copy linkLink copied to clipboard!

You can install an OpenShift Container Platform cluster on Alibaba Cloud using the Assisted Installer.

Alibaba Cloud provides a broad range of cloud computing and data storage services to online businesses and global enterprises.

Important

Installing Alibaba Cloud with Assisted Installer is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

### [1.1. Process outline for creating a cluster with the Assisted Installer](#alibaba-ai-installing_installing-alibaba-assisted-installer) Copy linkLink copied to clipboard!

You can install an OpenShift Container Platform cluster on Alibaba Cloud by using both the Assisted Installer and the Alibaba Cloud consoles.

The main steps of the installation process are as follows:

1. Create the cluster with the Assisted Installer and download the generated image.
2. Convert the image to `QCOW2` format. For more information, see the following section.
3. Upload the image to the Object Storage Service bucket in Alibaba Cloud.
4. Import the image to the Elastic Compute Service in Alibaba Cloud.
5. Provision the Alibaba Cloud resources:

   1. In the Virtual Private Cloud (VPC) console, set the networking configurations.
   2. In the Alibaba Cloud DNS console, define the Domain Name System.
   3. In the Elastic Compute Service (ECS) console, provision the compute instances.
6. Complete host discovery in the Assisted Installer.
7. Complete the network configurations in Alibaba Cloud.
8. Complete the cluster configuration and installation in the Assisted Installer.

**Additional resources**

* [Installing OpenShift Container Platform with the Assisted Installer](https://docs.redhat.com/en/documentation/assisted_installer_for_openshift_container_platform/2025)

### [1.2. Converting the discovery image to QCOW2 format](#alibaba-ai-converting-image-to-qcow2_installing-alibaba-assisted-installer) Copy linkLink copied to clipboard!

Convert the generated ISO to `QCOW2` format before importing it into Alibaba Cloud.

**Prerequisites**

* You have created a cluster and downloaded the discovery image in the Assisted Installer.
* You have access to a Linux machine that is outside the cluster, such as your desktop machine.

**Procedure**

1. Open the command-line interface on the Linux machine.
2. Verify that the system has virtualization flags enabled by running the following command:

   ```
   $ grep -e lm -e svm -e vmx /proc/cpuinfo
   ```
3. Install the `qemu-img` package on a RHEL or Fedora machine by running the following command:

   ```
   $ sudo dnf install -y qemu-img
   ```

   Note

   If your system uses the `APT` package manager, install the package using the name `qemu-utils` instead.
4. Convert the image to `QCOW2` by running the following command:

   ```
   $ qemu-img convert -O qcow2 ${CLUSTER_NAME}.iso ${CLUSTER_NAME}.qcow2
   ```

## [Legal Notice](#idm140372590960080) Copy linkLink copied to clipboard!

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
