---
title: "Machine management"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_management/index
retrieved_at: 2026-09-05T05:42:14.188275+00:00
---

# Machine management

---

OpenShift Container Platform 4.22

## Adding and maintaining cluster machines

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140199739129536)

**Abstract**

This document provides instructions for managing the machines that make up an OpenShift Container Platform cluster. Some tasks make use of the enhanced automatic machine management functions of an OpenShift Container Platform cluster and some tasks are manual. Not all tasks that are described in this document are available in all installation types.

---

## [Chapter 1. Overview of machine management](#overview-of-machine-management) Copy linkLink copied to clipboard!

You can use machine management to flexibly work with underlying infrastructure such as Amazon Web Services (AWS), Microsoft Azure, Google Cloud, Red Hat OpenStack Platform (RHOSP), and VMware vSphere to manage the OpenShift Container Platform cluster. You can control the cluster and perform auto-scaling, such as scaling up and down the cluster based on specific workload policies.

It is important to have a cluster that adapts to changing workloads. The OpenShift Container Platform cluster can horizontally scale up and down when the load increases or decreases.

Machine management is implemented as a custom resource definition (CRD). A CRD object defines a new unique object `Kind` in the cluster and enables the Kubernetes API server to handle the object’s entire lifecycle.

The Machine API Operator provisions the following resources:

* `MachineSet`
* `Machine`
* `ClusterAutoscaler`
* `MachineAutoscaler`
* `MachineHealthCheck`

### [1.1. Machine API overview](#machine-api-overview_overview-of-machine-management) Copy linkLink copied to clipboard!

The Machine API performs all node host provisioning management actions after the cluster installation finishes. Because of this system, OpenShift Container Platform offers an elastic, dynamic provisioning method on top of public or private cloud infrastructure.

The Machine API is a combination of primary resources that are based on the upstream Cluster API project and custom OpenShift Container Platform resources.

The two primary resources are:

Machines
:   A fundamental unit that describes the host for a node. A machine has a `providerSpec` specification, which describes the types of compute nodes that are offered for different cloud platforms. For example, a machine type for a compute node might define a specific machine type and required metadata.

Machine sets
:   `MachineSet` resources are groups of compute machines. Compute machine sets are to compute machines as replica sets are to pods. If you need more compute machines or must scale them down, you change the `replicas` field on the `MachineSet` resource to meet your compute need.

    Warning

    Control plane machines cannot be managed by compute machine sets.

    Control plane machine sets provide management capabilities for supported control plane machines that are similar to what compute machine sets provide for compute machines.

    For more information, see “Managing control plane machines".

The following custom resources add more capabilities to your cluster:

Machine autoscaler
:   The `MachineAutoscaler` resource automatically scales compute machines in a cloud. You can set the minimum and maximum scaling boundaries for nodes in a specified compute machine set, and the machine autoscaler maintains that range of nodes.

    The `MachineAutoscaler` object takes effect after a `ClusterAutoscaler` object exists. Both `ClusterAutoscaler` and `MachineAutoscaler` resources are made available by the `ClusterAutoscalerOperator` object.

Cluster autoscaler
:   This resource is based on the upstream cluster autoscaler project. In the OpenShift Container Platform implementation, it is integrated with the Machine API by extending the compute machine set API. You can use the cluster autoscaler to manage your cluster in the following ways:

    * Set cluster-wide scaling limits for resources such as cores, nodes, memory, and GPU
    * Set the priority so that the cluster prioritizes pods and new nodes are not brought online for less important pods
    * Set the scaling policy so that you can scale up nodes but not scale them down

Machine health check
:   The `MachineHealthCheck` resource detects when a machine is unhealthy, deletes it, and, on supported platforms, makes a new machine.

In OpenShift Container Platform version 3.11, you could not roll out a multi-zone architecture easily because the cluster did not manage machine provisioning. Beginning with OpenShift Container Platform version 4.1, this process is easier. Each compute machine set is scoped to a single zone, so the installation program sends out compute machine sets across availability zones on your behalf. And then because your compute is dynamic, and in the face of a zone failure, you always have a zone for when you must rebalance your machines. In global Azure regions that do not have multiple availability zones, you can use availability sets to ensure high availability. The autoscaler provides best-effort balancing over the life of a cluster.

### [1.2. Compute machine management](#machine-mgmt-intro-managing-compute_overview-of-machine-management) Copy linkLink copied to clipboard!

As a cluster administrator, you can manage the compute machines in your OpenShift Container Platform cluster.

For example, you can perform the following actions:

* Create a compute machine set for the following cloud providers:

  + [AWS](#creating-machineset-aws "2.1. Creating a compute machine set on AWS")
  + [Azure](#creating-machineset-azure "2.2. Creating a compute machine set on Azure")
  + [Azure Stack Hub](#creating-machineset-azure-stack-hub "2.3. Creating a compute machine set on Azure Stack Hub")
  + [Google Cloud](#creating-machineset-gcp "2.4. Creating a compute machine set on Google Cloud")
  + [IBM Cloud](#creating-machineset-ibm-cloud "2.5. Creating a compute machine set on IBM Cloud")
  + [IBM Power Virtual Server](#creating-machineset-ibm-power-vs "2.6. Creating a compute machine set on IBM Power Virtual Server")
  + [Nutanix](#creating-machineset-nutanix "2.7. Creating a compute machine set on Nutanix")
  + [RHOSP](#creating-machineset-osp "2.8. Creating a compute machine set on OpenStack")
  + [vSphere](#creating-machineset-vsphere "2.9. Creating a compute machine set on vSphere")
* Create a machine set for a bare metal deployment: [Creating a compute machine set on bare metal](#creating-machineset-bare-metal "2.10. Creating a compute machine set on bare metal")
* [Manually scale a compute machine set](#manually-scaling-machineset "Chapter 3. Manually scaling a compute machine set") by adding or removing a machine from the compute machine set.
* [Modify a compute machine set](#modifying-machineset "Chapter 4. Modifying a compute machine set") through the `MachineSet` YAML configuration file.
* [Delete](#deleting-machine "Chapter 6. Deleting a machine") a machine.
* [Create infrastructure compute machine sets](#creating-infrastructure-machinesets "Chapter 8. Creating infrastructure machine sets").
* Configure and deploy a [machine health check](#deploying-machine-health-checks "Chapter 12. Deploying machine health checks") to automatically fix damaged machines in a machine pool.

Note

When creating a new machine set, you should specify the latest image to use for the boot image. For more information about updating the boot image on your cluster, see "Manually updating the boot image" and "Boot image management". The method to update or specify the image varies by platform.

### [1.3. Control plane machine management](#machine-mgmt-intro-managing-control-plane_overview-of-machine-management) Copy linkLink copied to clipboard!

As a cluster administrator, you can manage the control plane machines in your OpenShift Container Platform cluster.

For example, you can perform the following actions:

* [Update your control plane configuration](#cpmso-feat-config-update_cpmso-managing-machines "10.3.1. Updating the control plane configuration") with a control plane machine set for the following cloud providers:

  + [Amazon Web Services](#cpmso-config-options-aws "10.5.1. Control plane configuration options for Amazon Web Services")
  + [Google Cloud](#cpmso-config-options-gcp "10.5.5. Control plane configuration options for Google Cloud")
  + [Microsoft Azure](#cpmso-config-options-azure "10.5.3. Control plane configuration options for Microsoft Azure")
  + [Nutanix](#cpmso-config-options-nutanix "10.5.7. Control plane configuration options for Nutanix")
  + [Red Hat OpenStack Platform (RHOSP)](#cpmso-config-options-openstack "10.5.8. Control plane configuration options for Red Hat OpenStack Platform (RHOSP)")
  + [VMware vSphere](#cpmso-config-options-vsphere "10.5.10. Control plane configuration options for VMware vSphere")
* Configure and deploy a [machine health check](#deploying-machine-health-checks "Chapter 12. Deploying machine health checks") to automatically recover unhealthy control plane machines.

### [1.4. Cluster autoscaling](#machine-mgmt-intro-autoscaling_overview-of-machine-management) Copy linkLink copied to clipboard!

You can automatically scale your OpenShift Container Platform cluster to ensure flexibility for changing workloads.

To [autoscale](#applying-autoscaling "Chapter 7. Applying autoscaling to an OpenShift Container Platform cluster") your cluster, you must first deploy a cluster autoscaler, and then deploy a machine autoscaler for each compute machine set.

* The [*cluster autoscaler*](#cluster-autoscaler-about_applying-autoscaling "7.1. The cluster autoscaler") increases and decreases the size of the cluster based on deployment needs.
* The [*machine autoscaler*](#machine-autoscaler-about_applying-autoscaling "7.2. About the machine autoscaler") adjusts the number of machines in the compute machine sets that you deploy in your OpenShift Container Platform cluster.

### [1.5. Compute machine creation on user-provisioned infrastructure](#machine-mgmt-intro-add-for-upi_overview-of-machine-management) Copy linkLink copied to clipboard!

User-provisioned infrastructure is an environment where you can deploy infrastructure such as compute, network, and storage resources that host the OpenShift Container Platform. You can add compute machines to a cluster on user-provisioned infrastructure during or after the installation process.

## [Chapter 2. Managing compute machines with the Machine API](#managing-compute-machines-with-the-machine-api) Copy linkLink copied to clipboard!

### [2.1. Creating a compute machine set on AWS](#creating-machineset-aws) Copy linkLink copied to clipboard!

You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on Amazon Web Services (AWS). For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

#### [2.1.1. Sample YAML for a compute machine set custom resource on AWS](#machineset-yaml-aws_creating-machineset-aws) Copy linkLink copied to clipboard!

The sample YAML defines a compute machine set that runs in the `us-east-1a` Amazon Web Services (AWS) Local Zone and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`.

In this sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-<role>-<zone>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<zone>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<zone>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/<role>: ""
      providerSpec:
        value:
          ami:
            id: ami-046fe691f52a953f9
          apiVersion: machine.openshift.io/v1beta1
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
          instanceType: m6i.large
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
            - name: <custom_tag_name>
              value: <custom_tag_value>
          userDataSecret:
            name: worker-user-data
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`<infrastructure_id>-<role>-<zone>`
:   Specifies the infrastructure ID, role node label, and zone.

`<role>`
:   Specifies the role node label to add.

`<zone>`
:   Specifies the zone name, for example, `us-east-1a`.

`<region>`
:   Specifies the region, for example, `us-east-1`.

`<infrastructure_id>-subnet-private-<zone>`
:   Specifies the infrastructure ID and zone.

`<custom_tag_name>`
:   Optional: Specifies custom tag data for your cluster. For example, you might add an admin contact email address by specifying a `name:value` pair of `Email:admin-email@example.com`.

    Note

    Custom tags can also be specified during installation in the `install-config.yaml` file. If the `install-config.yaml` file and the machine set include a tag with the same `name` data, the value for the tag from the machine set takes priority over the value for the tag in the `install-config.yaml` file.

Note

The `spec.template.spec.providerSpec.value.ami.id` stanza specifies a valid Red Hat Enterprise Linux CoreOS (RHCOS) Amazon Machine Image (AMI) for your AWS zone for your OpenShift Container Platform nodes. If you want to use an AWS Marketplace image, you must complete the OpenShift Container Platform subscription from the [AWS Marketplace](https://aws.amazon.com/marketplace/fulfillment?productId=59ead7de-2540-4653-a8b0-fa7926d5c845) to obtain an AMI ID for your region.

```
$ oc -n openshift-machine-api \
    -o jsonpath='{.spec.template.spec.providerSpec.value.ami.id}{"\n"}' \
    get machineset/<infrastructure_id>-<role>-<zone>
```

#### [2.1.2. Creating a compute machine set](#machineset-creating_creating-machineset-aws) Copy linkLink copied to clipboard!

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
4. If you need compute machine sets in other availability zones, repeat this process to create more compute machine sets.

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

#### [2.1.3. Labeling GPU machine sets for the cluster autoscaler](#machineset-label-gpu-autoscaler_creating-machineset-aws) Copy linkLink copied to clipboard!

Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

**Prerequisites**

* Your cluster uses a cluster autoscaler.

**Procedure**

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    name: machine-set-name
  spec:
    template:
      spec:
        metadata:
          labels:
            cluster-api/accelerator: <accelerator_name>
  ```

  where:

  `<accelerator_name>`
  :   Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.

      Note

      You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR. For more information, see "Cluster autoscaler resource definition".

#### [2.1.4. Assigning machines to placement groups for Elastic Fabric Adapter instances by using machine sets](#machineset-aws-existing-placement-group_creating-machineset-aws) Copy linkLink copied to clipboard!

You can configure a machine set to deploy machines on Elastic Fabric Adapter (EFA) instances within an existing Amazon Web Services (AWS) placement group.

[EFA](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA. This example uses both to demonstrate a configuration that can improve network performance for machines within the specified placement group.

**Prerequisites**

* You have access to the OpenShift CLI (`oc`) as a user with administrator privileges.
* You created a placement group in the AWS console.

  Note

  Ensure that the [rules and limitations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#limitations-placement-groups) for the type of placement group that you create are compatible with your intended use case.

**Procedure**

1. In a text editor, open an existing machine set custom resource (CR) or create a new one.
2. Update the CR to implement your configuration changes:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             instanceType: <supported_instance_type>
             networkInterfaceType: <interface_type>
             placement:
               availabilityZone: <zone>
               region: <region>
             placementGroupName: <placement_group>
             placementGroupPartition: <placement_group_partition_number>
   ```

   where:

   `<supported_instance_type>`
   :   Specifies an instance type that [supports EFAs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types).

   `<interface_type>`
   :   Specifies the network interface type. To use an EFA, set this value to `EFA`.

   `<zone>`
   :   Specifies the zone; for example, `us-east-1a`.

   `<region>`
   :   Specifies the region; for example, `us-east-1`.

   `<placement_group>`
   :   Specifies the name of the existing AWS placement group to deploy machines in.

   `<placement_group_partition_number>`
   :   Specifies the partition number of the existing AWS placement group to deploy machines in. This parameter is optional.
3. Save your changes and exit the object specification.

**Verification**

* In the AWS console, find a machine that the machine set created and verify the following in the machine properties:

  + The placement group field has the value that you specified for the `placementGroupName` parameter in the machine set.
  + If you specified a partition number, the partition number field has the value that you specified for the `placementGroupPartition` parameter in the machine set.
  + The interface type field indicates that it uses an EFA.

#### [2.1.5. Configuring the AWS EC2 Instance Metadata Service by using machine sets](#machineset-creating-imds-options_creating-machineset-aws) Copy linkLink copied to clipboard!

You can use machine sets to create machines that use the version of the Amazon EC2 Instance Metadata Service (IMDS) that meets the security requirements of your organization.

Machine sets can create machines that allow the use of both IMDSv1 and [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) or machines that require the use of IMDSv2.

You can specify whether to require the use of IMDSv2 by adding or editing the value of `metadataServiceOptions.authentication` in the machine set.

Important

Before configuring a machine set to create machines that require IMDSv2, ensure that any workloads that interact with the AWS metadata service support IMDSv2.

**Prerequisites**

* To use IMDSv2, your AWS cluster must have been created with OpenShift Container Platform version 4.7 or later.

  Note

  To use IMDSv2 on AWS clusters that were created with OpenShift Container Platform version 4.6 or earlier, you must update your boot image. For more information, see "Boot image management".

**Procedure**

1. In a text editor, open an existing machine set custom resource (CR) or create a new one.
2. Update the CR to implement your configuration changes:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             metadataServiceOptions:
               authentication: Required
   ```

   To require IMDSv2, set the `metadataServiceOptions.authentication` parameter value to `Required`. To allow the use of both IMDSv1 and IMDSv2, set the parameter value to `Optional`. If you do not specify a value, machines that the machine set creates allow the use of both IMDSv1 and IMDSv2.
3. Save your changes and exit the object specification.

#### [2.1.6. Configuring storage throughput for gp3 drives](#machineset-creating-gp3-throughput_creating-machineset-aws) Copy linkLink copied to clipboard!

You can improve performance for high traffic services by increasing the throughput of gp3 storage volumes in an AWS cluster. You can configure the storage throughput by editing your compute or control plane machine set.

**Prerequisites**

* You use gp3 storage volume(s).

**Procedure**

* Add or edit the following lines under the `providerSpec` field in your compute or control plane machine set:

  ```
  providerSpec:
    value:
      blockDevices:
        - ebs:
            throughputMib: <throughput_value>
  ```

  where:

  `<throughput_value>`
  :   Specifies a value in MiB per second between 125 and 2,000. You can only edit this value on gp3 volumes. The default value is `125`.

#### [2.1.7. Creating Dedicated Instances by using machine sets](#machineset-creating-dedicated-instance_creating-machineset-aws) Copy linkLink copied to clipboard!

You can configure a machine set to deploy machines as Dedicated Instances that run in a virtual private cloud (VPC) on hardware that only a single customer can use. To change use Dedicated Instances, you update the placement tenancy value in the machine set custom resource (CR).

Amazon Web Services (AWS) Dedicated Instances are EC2 instances that are physically isolated at the host hardware level. This isolation applies to instances that a single payer account owns even if the instances belong to different AWS accounts.

Public tenancy is the default tenancy. Instances with public tenancy run on shared hardware and can share hardware with Dedicated Instances that belong to the same AWS account.

**Prerequisites**

* You have access to the OpenShift CLI (`oc`) as a user with administrator privileges.

**Procedure**

1. In a text editor, open an existing machine set custom resource (CR) or create a new one.
2. Update the CR to implement your configuration changes:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             placement:
               tenancy: dedicated
   ```

   To use Dedicated Instances, set the `placement.tenancy` parameter value to `dedicated`.
3. Save your changes and exit the object specification.

#### [2.1.8. Machine sets that place machines on Dedicated Hosts](#machineset-dedicated-hosts_creating-machineset-aws) Copy linkLink copied to clipboard!

You can configure machine sets to place machines on Amazon Web Services (AWS) Dedicated Hosts. Dedicated Hosts are physical servers with instance capacity that is fully dedicated to your use. You can use Dedicated Hosts with your existing per-socket, per-core, or per-VM software licenses. With dynamic host allocation, the Machine API Operator requests a Dedicated Host from AWS and applies the specified tags to the Dedicated Host.

Important

AWS Dedicated Host support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

##### [2.1.8.1. Place machines on Dedicated Hosts by using machine sets](#machineset-creating-dedicated-hosts_creating-machineset-aws) Copy linkLink copied to clipboard!

You can configure a machine set to place machines on Amazon Web Services (AWS) Dedicated Hosts. With dynamic host allocation, the Machine API Operator requests a Dedicated Host from AWS and applies the specified tags to the Dedicated Host.

Important

AWS Dedicated Host support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Procedure**

* Specify the following `placement` fields in your machine set YAML file:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  # ...
  spec:
    template:
      spec:
        providerSpec:
          placement:
            tenancy: host
            host:
              affinity: DedicatedHost
              dedicatedHost:
                allocationStrategy: Dynamic
                dynamicHostAllocation:
                  tags:
                  - name: <tag_name>
                    value: <tag_value>
  ```

  where:

  `spec.template.spec.providerSpec.placement.host.dedicatedHost.dynamicHostAllocation.tags`
  :   Optional: Specifies tags to apply to the dynamically allocated Dedicated Host. If you specify tags, you must specify both a key and a value. For `<tag_name>`, specify the tag key, for example `Environment`. For `<tag_value>`, specify the tag value, for example `production`.

**Verification**

* Verify that the machine set exists by running the following command:

  ```
  $ oc get machineset -n openshift-machine-api
  ```

##### [2.1.8.2. Place machines on a specific Dedicated Host by using machine sets](#machineset-creating-dedicated-hosts-byo-machineset_creating-machineset-aws) Copy linkLink copied to clipboard!

You can configure a machine set to place machines on a specific Amazon Web Services (AWS) Dedicated Host by specifying the host ID.

Important

AWS Dedicated Host support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Procedure**

* Specify the following `placement` fields in your machine set YAML file:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  # ...
  spec:
    template:
      spec:
        providerSpec:
          placement:
            tenancy: host
            host:
              affinity: DedicatedHost
              dedicatedHost:
                id: <dedicated_host_id>
  ```

  where:

  `<dedicated_host_id>`
  :   Specifies the ID of the AWS Dedicated Host on which to place the machine, for example `h-0123456789abcdef0`.

**Verification**

* Verify that the machine set exists by running the following command:

  ```
  $ oc get machineset -n openshift-machine-api
  ```

#### [2.1.9. Machine sets that deploy machines as Spot Instances](#machineset-non-guaranteed-instance_creating-machineset-aws) Copy linkLink copied to clipboard!

You can save on costs by creating a compute machine set running on Amazon Web Services (AWS) that deploys machines as non-guaranteed Spot Instances. Spot Instances utilize unused AWS EC2 capacity and are less expensive than On-Demand Instances. You can use Spot Instances for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.

AWS EC2 can terminate a Spot Instance at any time. AWS gives a two-minute warning to the user when an interruption occurs. OpenShift Container Platform begins to remove the workloads from the affected instances when AWS issues the termination warning.

Interruptions can occur when using Spot Instances for the following reasons:

* The instance price exceeds your maximum price
* The demand for Spot Instances increases
* The supply of Spot Instances decreases

When AWS terminates an instance, a termination handler running on the Spot Instance node deletes the machine resource. To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a Spot Instance.

##### [2.1.9.1. Creating Spot Instances by using compute machine sets](#machineset-creating-non-guaranteed-instance_creating-machineset-aws) Copy linkLink copied to clipboard!

You can save on costs by creating a compute machine set that deploys machines as non-guaranteed instances. To launch a Spot Instance on AWS, you add `spotMarketOptions` to your compute machine set YAML file.

**Procedure**

* Add the following line under the `providerSpec` field:

  ```
  providerSpec:
    value:
      spotMarketOptions: {}
  ```

  You can optionally set the `spotMarketOptions.maxPrice` field to limit the cost of the Spot Instance. For example you can set `maxPrice: '2.50'`.

  Note

  If the `maxPrice` is set, this value is used as the hourly maximum spot price. If it is not set, the maximum price defaults to charge up to the On-Demand Instance price.

  It is strongly recommended to use the default On-Demand price as the `maxPrice` value and to not set the maximum price for Spot Instances.

#### [2.1.10. Configuring Capacity Reservations by using machine sets](#machineset-capacity-reservation_creating-machineset-aws) Copy linkLink copied to clipboard!

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define by using Capacity Reservations on Amazon Web Services clusters, including On-Demand Capacity Reservations and Capacity Blocks for ML.

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define.

These parameters specify the instance type, region, and number of instances that you want to reserve. If your Capacity Reservation can accommodate the capacity request, the deployment succeeds.

For more information, including limitations and suggested use cases for this Amazon Web Services offering, see [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) in the AWS documentation.

**Prerequisites**

* You have access to the cluster with `cluster-admin` privileges.
* You installed the OpenShift CLI (`oc`).
* You have purchased an On-Demand Capacity Reservation or Capacity Block for ML. For more information, see [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) in the AWS documentation.

**Procedure**

1. In a text editor, open an existing machine set custom resource (CR) or create a new one.
2. Update the CR to implement your configuration changes:

   **Sample configuration**

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             capacityReservationId: <capacity_reservation>
             marketType: <market_type>
   # ...
   ```

   where:

   `<capacity_reservation>`
   :   Specifies the ID of the Capacity Block for ML or On-Demand Capacity Reservation that you want the machine set to deploy machines on.

   `<market_type>`
   :   Specifies the market type to use. The following values are valid:

       `CapacityBlock`
       :   Use this market type with Capacity Blocks for ML.

       `OnDemand`
       :   Use this market type with On-Demand Capacity Reservations.

       `Spot`
       :   Use this market type with Spot Instances. This option is not compatible with Capacity Reservations.
3. Save your changes and exit the object specification.

**Verification**

* To verify machine deployment, list the machines that the machine set created by running the following command:

  ```
  $ oc get machines.machine.openshift.io \
    -n openshift-machine-api \
    -l machine.openshift.io/cluster-api-machineset=<machine_set_name>
  ```

  where `<machine_set_name>` is the name of the compute machine set.

  In the output, verify that the characteristics of the listed machines match the parameters of your Capacity Reservation.

#### [2.1.11. Adding a GPU node to an existing OpenShift Container Platform cluster](#nvidia-gpu-aws-adding-a-gpu-node_creating-machineset-aws) Copy linkLink copied to clipboard!

You can copy and modify a default compute machine set configuration to create a GPU-enabled machine set and machines for the AWS EC2 cloud provider.

For more information about the supported instance types, see the following NVIDIA documentation:

* [NVIDIA GPU Operator Community support matrix](https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/platform-support.html)
* [NVIDIA AI Enterprise support matrix](https://docs.nvidia.com/ai-enterprise/latest/product-support-matrix/index.html)

**Procedure**

1. View the existing nodes, machines, and machine sets by running the following command. Note that each node is an instance of a machine definition with a specific AWS region and OpenShift Container Platform role.

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                                        STATUS   ROLES                  AGE     VERSION
   ip-10-0-52-50.us-east-2.compute.internal    Ready    worker                 3d17h   v1.35.4
   ip-10-0-58-24.us-east-2.compute.internal    Ready    control-plane,master   3d17h   v1.35.4
   ip-10-0-68-148.us-east-2.compute.internal   Ready    worker                 3d17h   v1.35.4
   ip-10-0-68-68.us-east-2.compute.internal    Ready    control-plane,master   3d17h   v1.35.4
   ip-10-0-72-170.us-east-2.compute.internal   Ready    control-plane,master   3d17h   v1.35.4
   ip-10-0-74-50.us-east-2.compute.internal    Ready    worker                 3d17h   v1.35.4
   ```
2. View the machines and machine sets that exist in the `openshift-machine-api` namespace by running the following command. Each compute machine set is associated with a different availability zone within the AWS region. The installation program automatically load balances compute machines across availability zones.

   ```
   $ oc get machinesets -n openshift-machine-api
   ```

   **Example output**

   ```
   NAME                                        DESIRED   CURRENT   READY   AVAILABLE   AGE
   preserve-dsoc12r4-ktjfc-worker-us-east-2a   1         1         1       1           3d11h
   preserve-dsoc12r4-ktjfc-worker-us-east-2b   2         2         2       2           3d11h
   ```
3. View the machines that exist in the `openshift-machine-api` namespace by running the following command. At this time, there is only one compute machine per machine set, though a compute machine set could be scaled to add a node in a particular region and zone.

   ```
   $ oc get machines -n openshift-machine-api | grep worker
   ```

   **Example output**

   ```
   preserve-dsoc12r4-ktjfc-worker-us-east-2a-dts8r      Running   m5.xlarge   us-east-2   us-east-2a   3d11h
   preserve-dsoc12r4-ktjfc-worker-us-east-2b-dkv7w      Running   m5.xlarge   us-east-2   us-east-2b   3d11h
   preserve-dsoc12r4-ktjfc-worker-us-east-2b-k58cw      Running   m5.xlarge   us-east-2   us-east-2b   3d11h
   ```
4. Make a copy of one of the existing compute `MachineSet` definitions and output the result to a JSON file by running the following command. This will be the basis for the GPU-enabled compute machine set definition.

   ```
   $ oc get machineset preserve-dsoc12r4-ktjfc-worker-us-east-2a -n openshift-machine-api -o json > <output_file.json>
   ```
5. Edit the JSON file and make the following changes to the new `MachineSet` definition:

   * Replace `worker` with `gpu`. This will be the name of the new machine set.
   * Change the instance type of the new `MachineSet` definition to `g4dn`, which includes an NVIDIA Tesla T4 GPU. To learn more about AWS `g4dn` instance types, see [Accelerated Computing](https://aws.amazon.com/ec2/instance-types/#Accelerated_Computing).

     ```
     $ jq .spec.template.spec.providerSpec.value.instanceType preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a.json

     "g4dn.xlarge"
     ```

     The `<output_file.json>` file is saved as `preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a.json`.
6. Update the following fields in `preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a.json`:

   * `.metadata.name` to a name containing `gpu`.
   * `.spec.selector.matchLabels["machine.openshift.io/cluster-api-machineset"]` to match the new `.metadata.name`.
   * `.spec.template.metadata.labels["machine.openshift.io/cluster-api-machineset"]` to match the new `.metadata.name`.
   * `.spec.template.spec.providerSpec.value.instanceType` to `g4dn.xlarge`.
7. To verify your changes, perform a `diff` of the original compute definition and the new GPU-enabled node definition by running the following command:

   ```
   $ oc -n openshift-machine-api get preserve-dsoc12r4-ktjfc-worker-us-east-2a -o json | diff preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a.json -
   ```

   **Example output**

   ```
   10c10

   < "name": "preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a",
   ---
   > "name": "preserve-dsoc12r4-ktjfc-worker-us-east-2a",

   21c21

   < "machine.openshift.io/cluster-api-machineset": "preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a"
   ---
   > "machine.openshift.io/cluster-api-machineset": "preserve-dsoc12r4-ktjfc-worker-us-east-2a"

   31c31

   < "machine.openshift.io/cluster-api-machineset": "preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a"
   ---
   > "machine.openshift.io/cluster-api-machineset": "preserve-dsoc12r4-ktjfc-worker-us-east-2a"

   60c60

   < "instanceType": "g4dn.xlarge",
   ---
   > "instanceType": "m5.xlarge",
   ```
8. Create the GPU-enabled compute machine set from the definition by running the following command:

   ```
   $ oc create -f preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a.json
   ```

   **Example output**

   ```
   machineset.machine.openshift.io/preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a created
   ```

**Verification**

1. View the machine set you created by running the following command:

   ```
   $ oc -n openshift-machine-api get machinesets | grep gpu
   ```

   The MachineSet replica count is set to `1` so a new `Machine` object is created automatically.

   **Example output**

   ```
   preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a   1         1         1       1           4m21s
   ```
2. View the `Machine` object that the machine set created by running the following command:

   ```
   $ oc -n openshift-machine-api get machines | grep gpu
   ```

   **Example output**

   ```
   preserve-dsoc12r4-ktjfc-worker-gpu-us-east-2a    running    g4dn.xlarge   us-east-2   us-east-2a  4m36s
   ```

Note that there is no need to specify a namespace for the node. The node definition is cluster scoped.

#### [2.1.12. Deploying the Node Feature Discovery Operator](#nvidia-gpu-aws-deploying-the-node-feature-discovery-operator_creating-machineset-aws) Copy linkLink copied to clipboard!

After the GPU-enabled node is created, you need to discover the GPU-enabled node so it can be scheduled. To do this, install the Node Feature Discovery (NFD) Operator.

The NFD Operator identifies hardware device features in nodes. It solves the general problem of identifying and cataloging hardware resources in the infrastructure nodes so they can be made available to OpenShift Container Platform.

**Procedure**

1. Install the Node Feature Discovery Operator from the software catalog in the OpenShift Container Platform console.
2. After installing the NFD Operator, select **Node Feature Discovery** from the installed Operators list and select **Create instance**. This installs the `nfd-master` and `nfd-worker` pods, one `nfd-worker` pod for each compute node, in the `openshift-nfd` namespace.
3. Verify that the Operator is installed and running by running the following command:

   ```
   $ oc get pods -n openshift-nfd
   ```

   **Example output**

   ```
   NAME                                       READY    STATUS     RESTARTS   AGE

   nfd-controller-manager-8646fcbb65-x5qgk    2/2      Running 7  (8h ago)   1d
   ```
4. Browse to the installed Operator in the console and select **Create Node Feature Discovery**.
5. Select **Create** to build a NFD custom resource. This creates NFD pods in the `openshift-nfd` namespace that poll the OpenShift Container Platform nodes for hardware resources and catalog them.

**Verification**

1. After a successful build, verify that a NFD pod is running on each nodes by running the following command:

   ```
   $ oc get pods -n openshift-nfd
   ```

   **Example output**

   ```
   NAME                                       READY   STATUS      RESTARTS        AGE
   nfd-controller-manager-8646fcbb65-x5qgk    2/2     Running     7 (8h ago)      12d
   nfd-master-769656c4cb-w9vrv                1/1     Running     0               12d
   nfd-worker-qjxb2                           1/1     Running     3 (3d14h ago)   12d
   nfd-worker-xtz9b                           1/1     Running     5 (3d14h ago)   12d
   ```

   The NFD Operator uses vendor PCI IDs to identify hardware in a node. NVIDIA uses the PCI ID `10de`.
2. View the NVIDIA GPU discovered by the NFD Operator by running the following command:

   ```
   $ oc describe node ip-10-0-132-138.us-east-2.compute.internal | egrep 'Roles|pci'
   ```

   **Example output**

   ```
   Roles: worker

   feature.node.kubernetes.io/pci-1013.present=true

   feature.node.kubernetes.io/pci-10de.present=true

   feature.node.kubernetes.io/pci-1d0f.present=true
   ```

   `10de` appears in the node feature list for the GPU-enabled node. This mean the NFD Operator correctly identified the node from the GPU-enabled MachineSet.

### [2.2. Creating a compute machine set on Azure](#creating-machineset-azure) Copy linkLink copied to clipboard!

You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on Microsoft Azure. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

#### [2.2.1. Sample YAML for a compute machine set custom resource on Azure](#machineset-yaml-azure_creating-machineset-azure) Copy linkLink copied to clipboard!

You can define a machine set YAML to provision nodes by specifying parameters such as `vmSize` and `image`. You can use this to automate and scale infrastructure consistently, to ensure compute nodes meet specific workload requirements within the cluster.

The sample YAML defines a compute machine set that runs in the `1` Microsoft Azure zone in a region and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`. ifdef::infra[`node-role.kubernetes.io/infra: ""`. The YAML specifies a taint to prevent user workloads from being scheduled on infra nodes. After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <role>
    machine.openshift.io/cluster-api-machine-type: <role>
  name: <infrastructure_id>-<role>-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
    spec:
      metadata:
        creationTimestamp: null
        labels:
          machine.openshift.io/cluster-api-machineset: <machineset_name>
          node-role.kubernetes.io/<role>: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image:
            offer: ""
            publisher: ""
            resourceID: /resourceGroups/<infrastructure_id>-rg/providers/Microsoft.Compute/galleries/gallery_<infrastructure_id>/images/<infrastructure_id>-gen2/versions/latest
            sku: ""
            version: ""
          internalLoadBalancer: ""
          kind: AzureMachineProviderSpec
          location: <region>
          managedIdentity: <infrastructure_id>-identity
          metadata:
            creationTimestamp: null
          natRule: null
          networkResourceGroup: ""
          osDisk:
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Linux
          publicIP: false
          publicLoadBalancer: ""
          resourceGroup: <infrastructure_id>-rg
          sshPrivateKey: ""
          sshPublicKey: ""
          tags:
            <custom_tag_name_1>: <custom_tag_value_1>
            <custom_tag_name_2>: <custom_tag_value_2>
          subnet: <infrastructure_id>-<role>-subnet
          userDataSecret:
            name: worker-user-data
          vmSize: Standard_D4s_v3
          vnet: <infrastructure_id>-vnet
          zone: "1"
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

    You can obtain the subnet by running the following command:

    ```
    $  oc -n openshift-machine-api \
        -o jsonpath='{.spec.template.spec.providerSpec.value.subnet}{"\n"}' \
        get machineset/<infrastructure_id>-worker-centralus1
    ```

    You can obtain the vnet by running the following command:

    ```
    $  oc -n openshift-machine-api \
        -o jsonpath='{.spec.template.spec.providerSpec.value.vnet}{"\n"}' \
        get machineset/<infrastructure_id>-worker-centralus1
    ```

`<role>`
:   Specifies the node label to add.

`<infrastructure_id>-<role>-<region>`
:   Specifies the infrastructure ID, node label, and region.

Note

The value of the `spec.template.spec.providerSpec.value.image` parameter specifies the image details for your compute machine set. If you want to use an Azure Marketplace image, see "Using the Azure Marketplace offering".

The value of the `spec.template.spec.providerSpec.value.image.resourceID` parameter specifies an image that is compatible with your instance type. The Hyper-V generation V2 images created by the installation program have a `-gen2` suffix, while V1 images have the same name without the suffix.

The value of the `spec.template.spec.providerSpec.value.location` parameter specifies the region to place machines on.

`<custom_tag_name_1>`
:   Optional: Specifies custom tags in your machine set. Provide the tag name in `<custom_tag_name>` field and the corresponding tag value in `<custom_tag_value>` field.

Note

The value of the `spec.template.spec.providerSpec.value.zone` parameter specifies the zone within your region to place machines on. Ensure that your region supports the zone that you specify. If your region supports availability zones, you must specify the zone. Specifying the zone avoids volume node affinity failure when a pod requires a persistent volume attachment. To do this, you can create a compute machine set for each zone in the same region.

#### [2.2.2. Creating a compute machine set](#machineset-creating_creating-machineset-azure) Copy linkLink copied to clipboard!

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

#### [2.2.3. Labeling GPU machine sets for the cluster autoscaler](#machineset-label-gpu-autoscaler_creating-machineset-azure) Copy linkLink copied to clipboard!

Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

**Prerequisites**

* Your cluster uses a cluster autoscaler.

**Procedure**

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    name: machine-set-name
  spec:
    template:
      spec:
        metadata:
          labels:
            cluster-api/accelerator: <accelerator_name>
  ```

  where:

  `<accelerator_name>`
  :   Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.

      Note

      You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR. For more information, see "Cluster autoscaler resource definition".

#### [2.2.4. Using the Azure Marketplace offering](#installation-azure-marketplace-subscribe_creating-machineset-azure) Copy linkLink copied to clipboard!

You can create a machine set running on Azure that deploys machines that use the Azure Marketplace offering. To use this offering, you must first obtain the Azure Marketplace image. When obtaining your image, consider the following:

* While the images are the same, the Azure Marketplace publisher is different depending on your region. If you are located in North America, specify `redhat` as the publisher. If you are located in EMEA, specify `redhat-limited` as the publisher.
* The offer includes a `rh-ocp-worker` SKU and a `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker` SKU represents a Hyper-V generation version 2 VM image. The default instance types used in OpenShift Container Platform are version 2 compatible. If you plan to use an instance type that is only version 1 compatible, use the image associated with the `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker-gen1` SKU represents a Hyper-V version 1 VM image.

Important

Installing images with the Azure marketplace is not supported on clusters with 64-bit ARM instances.

You should only modify the RHCOS image for compute machines to use an Azure Marketplace image. Control plane machines and infrastructure nodes do not require an OpenShift Container Platform subscription and use the public RHCOS default image by default, which does not incur subscription costs on your Azure bill. Therefore, you should not modify the cluster default boot image or the control plane boot images. Applying the Azure Marketplace image to them will incur additional licensing costs that cannot be recovered.

**Prerequisites**

* You have installed the Azure CLI client `(az)`.
* Your Azure account is entitled for the offer and you have logged into this account with the Azure CLI client.

**Procedure**

1. Display all of the available OpenShift Container Platform images by running one of the following commands:

   * North America:

     ```
     $  az vm image list --all --offer rh-ocp-worker --publisher redhat -o table
     ```

     **Example output**

     ```
     Offer          Publisher       Sku                 Urn                                                             Version
     -------------  --------------  ------------------  --------------------------------------------------------------  -----------------
     rh-ocp-worker  RedHat          rh-ocp-worker       RedHat:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
     rh-ocp-worker  RedHat          rh-ocp-worker-gen1  RedHat:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
     ```
   * EMEA:

     ```
     $  az vm image list --all --offer rh-ocp-worker --publisher redhat-limited -o table
     ```

     **Example output**

     ```
     Offer          Publisher       Sku                 Urn                                                                     Version
     -------------  --------------  ------------------  --------------------------------------------------------------          -----------------
     rh-ocp-worker  redhat-limited  rh-ocp-worker       redhat-limited:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
     rh-ocp-worker  redhat-limited  rh-ocp-worker-gen1  redhat-limited:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
     ```

   Note

   Use the latest image that is available for compute and control plane nodes. If required, your VMs are automatically upgraded as part of the installation process.
2. Inspect the image for your offer by running one of the following commands:

   * North America:

     ```
     $ az vm image show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
     ```
   * EMEA:

     ```
     $ az vm image show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
     ```
3. Review the terms of the offer by running one of the following commands:

   * North America:

     ```
     $ az vm image terms show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
     ```
   * EMEA:

     ```
     $ az vm image terms show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
     ```
4. Accept the terms of the offering by running one of the following commands:

   * North America:

     ```
     $ az vm image terms accept --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
     ```
   * EMEA:

     ```
     $ az vm image terms accept --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
     ```
5. Record the image details of your offer, specifically the values for `publisher`, `offer`, `sku`, and `version`.
6. Add the following parameters to the `providerSpec` section of your machine set YAML file using the image details for your offer:

   **Sample `providerSpec` image values for Azure Marketplace machines**

   ```
   providerSpec:
     value:
       image:
         offer: rh-ocp-worker
         publisher: redhat
         resourceID: ""
         sku: rh-ocp-worker
         type: MarketplaceWithPlan
         version: 413.92.2023101700
   ```

#### [2.2.5. Enabling Microsoft Azure boot diagnostics](#machineset-azure-boot-diagnostics_creating-machineset-azure) Copy linkLink copied to clipboard!

You can enable boot diagnostics on Microsoft Azure machines that your machine set creates. Use this to store console logs that you can use to troubleshoot why a node fails to boot.

**Prerequisites**

* Have an existing Azure cluster.

**Procedure**

* Add the `diagnostics` configuration that is applicable to your storage type to the `providerSpec` field in your machine set YAML file:

  + For an Azure Managed storage account:

    ```
    providerSpec:
      value:
        diagnostics:
          boot:
            storageAccountType: <azure_managed>
    ```

    where:

    `<azure_managed>`
    :   Specifies an Azure Managed storage account.
  + For an Azure Unmanaged storage account:

    ```
    providerSpec:
      value:
        diagnostics:
          boot:
            storageAccountType: <customer_managed>
            customerManaged:
              storageAccountURI: <https://<storage_account>.blob.core.windows.net>
    ```

    where:

    `<customer_managed>`
    :   Specifies an Azure Unmanaged storage account.

    `https://<storage_account>.blob.core.windows.net`
    :   Specifies the storage account URL. Replace `<storage_account>` with the name of your storage account.

    Note

    Only the Azure Blob Storage data service is supported.

**Verification**

* On the Azure portal, review the **Boot diagnostics** page for a machine deployed by the machine set, and verify that you can see the serial logs for the machine.

#### [2.2.6. Machine sets that deploy machines as Spot VMs](#machineset-non-guaranteed-instance_creating-machineset-azure) Copy linkLink copied to clipboard!

You can save on costs by creating a compute machine set running on Microsoft Azure that deploys machines as non-guaranteed Spot VMs. Spot VMs use unused Azure capacity and are less expensive than standard VMs. You can use Spot VMs for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.

Azure can terminate a Spot VM at any time. Azure gives a 30-second warning to the user when an interruption occurs. OpenShift Container Platform begins to remove the workloads from the affected instances when Azure issues the termination warning.

Interruptions can occur when using Spot VMs for the following reasons:

* The instance price exceeds your maximum price
* The supply of Spot VMs decreases
* Azure needs capacity back

When Azure terminates an instance, a termination handler running on the Spot VM node deletes the machine resource. To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a Spot VM.

##### [2.2.6.1. Creating Spot VMs by using compute machine sets](#machineset-creating-non-guaranteed-instance_creating-machineset-azure) Copy linkLink copied to clipboard!

You can save on costs by creating a compute machine set that deploys machines as non-guaranteed instances. To launch a Spot VM on Azure, you add `spotVMOptions` to your compute machine set YAML file.

**Procedure**

* Add the following line under the `providerSpec` field:

  ```
  providerSpec:
    value:
      spotVMOptions: {}
  ```

  You can optionally set the `spotVMOptions.maxPrice` field to limit the cost of the Spot VM. For example you can set `maxPrice: '0.98765'`. If the `maxPrice` is set, this value is used as the hourly maximum spot price. If it is not set, the maximum price defaults to `-1` and charges up to the standard VM price.

  Microsoft Azure caps Spot VM prices at the standard price. Azure will not evict an instance due to pricing if the instance is set with the default `maxPrice`. However, an instance can still be evicted due to capacity restrictions.

  Note

  It is strongly recommended to use the default standard VM price as the `maxPrice` value and to not set the maximum price for Spot VMs.

#### [2.2.7. Machine sets that deploy machines on Ephemeral OS disks](#machineset-azure-ephemeral-os_creating-machineset-azure) Copy linkLink copied to clipboard!

You can create a compute machine set running on Microsoft Azure that deploys machines on Ephemeral OS disks. Ephemeral OS disks use local VM capacity rather than remote Microsoft Azure Storage. The configuration, therefore, incurs no additional cost and provides lower latency for reading, writing, and reimaging.

##### [2.2.7.1. Creating machines on Ephemeral OS disks by using compute machine sets](#machineset-creating-azure-ephemeral-os_creating-machineset-azure) Copy linkLink copied to clipboard!

To improve performance and reduce storage costs, you can host the OS disk directly on the local storage of the virtual machines (VMs) rather than on remote Microsoft Azure Storage.

You launch machines on Ephemeral OS disks on Azure by editing your compute machine set YAML file.

**Prerequisites**

* Have an existing Azure cluster.

**Procedure**

1. Edit the custom resource (CR) by running the following command:

   ```
   $ oc edit machineset <machine-set-name>
   ```

   where `<machine-set-name>` is the compute machine set that you want to provision machines on Ephemeral OS disks.
2. Add the following to the `providerSpec` field:

   ```
   providerSpec:
     value:
       ...
       osDisk:
          ...
          diskSettings:
            ephemeralStorageLocation: Local
          cachingType: ReadOnly
          managedDisk:
            storageAccountType: Standard_LRS
          ...
   ```

   where:

   `providerSpec.value.osDisk.diskSettings`, `providerSpec.value.osDisk.diskSettings.ephemeralStorageLocation`, and `providerSpec.value.osDisk.cachingType`
   :   Enables the use of Ephemeral OS disks.

   `providerSpec.value.osDisk.managedDisk.storageAccountType`
   :   Ephemeral OS disks are only supported for VMs or scale set instances that use the Standard LRS storage account type.

       Important

       The implementation of Ephemeral OS disk support in OpenShift Container Platform only supports the `CacheDisk` placement type. Do not change the `placement` configuration setting.
3. Create a compute machine set using the updated configuration:

   ```
   $ oc create -f <machine-set-config>.yaml
   ```

**Verification**

* On the Azure portal, review the **Overview** page for a machine deployed by the compute machine set, and verify that the `Ephemeral OS disk` field is set to `OS cache placement`.

#### [2.2.8. Machine sets that deploy machines with ultra disks as data disks](#machineset-azure-ultra-disk_creating-machineset-azure) Copy linkLink copied to clipboard!

You can create a machine set running on Microsoft Azure that deploys machines with ultra disks. Ultra disks are high-performance storage that are intended for use with the most demanding data workloads.

You can also create a persistent volume claim (PVC) that dynamically binds to a storage class backed by Azure ultra disks and mounts them to pods.

Note

Data disks do not support the ability to specify disk throughput or disk IOPS. You can configure these properties by using PVCs.

##### [2.2.8.1. Creating machines with ultra disks by using machine sets](#machineset-creating-azure-ultra-disk_creating-machineset-azure) Copy linkLink copied to clipboard!

You can deploy machines with ultra disks on Microsoft Azure by editing your machine set YAML file.

**Prerequisites**

* Have an existing Microsoft Azure cluster.

**Procedure**

1. Create a custom secret in the `openshift-machine-api` namespace by using the `worker` data secret by running the following command:

   ```
   $ oc -n openshift-machine-api \
   get secret <role>-user-data \
   --template='{{index .data.userData | base64decode}}' | jq > userData.txt
   ```

   where:

   `<role>`
   :   Replace with `worker`.

   `userData.txt`
   :   Specifies `userData.txt` as the name of the new custom secret.
2. In a text editor, open the `userData.txt` file and locate the final `}` character in the file.

   1. On the immediately preceding line, add a `,`.
   2. Create a new line after the `,` and add the following configuration details:

      ```
      "storage": {
        "disks": [
          {
            "device": "/dev/disk/azure/scsi1/lun0",
            "partitions": [
              {
                "label": "lun0p1",
                "sizeMiB": 1024,
                "startMiB": 0
              }
            ]
          }
        ],
        "filesystems": [
          {
            "device": "/dev/disk/by-partlabel/lun0p1",
            "format": "xfs",
            "path": "/var/lib/lun0p1"
          }
        ]
      },
      "systemd": {
        "units": [
          {
            "contents": "[Unit]\nBefore=local-fs.target\n[Mount]\nWhere=/var/lib/lun0p1\nWhat=/dev/disk/by-partlabel/lun0p1\nOptions=defaults,pquota\n[Install]\nWantedBy=local-fs.target\n",
            "enabled": true,
            "name": "var-lib-lun0p1.mount"
          }
        ]
      }
      ```

      where:

      `"disks"`
      :   Specifies the configuration details for the disk that you want to attach to a node as an ultra disk.

      `"device"`
      :   Specifies the `lun` value that is defined in the `dataDisks` stanza of the machine set you are using. For example, if the machine set contains `lun: 0`, specify `lun0`. You can initialize multiple data disks by specifying multiple `"disks"` entries in this configuration file. If you specify multiple `"disks"` entries, ensure that the `lun` value for each matches the value in the machine set.

      `"partitions"`
      :   Specifies the configuration details for a new partition on the disk.

      `"label"`
      :   Specifies a label for the partition. You might find it helpful to use hierarchical names, such as `lun0p1` for the first partition of `lun0`.

      `"sizeMiB"`
      :   Specifies the total size in MiB of the partition.

      `"filesystems"`
      :   Specifies the filesystem to use when formatting a partition. Use the partition label to specify the partition.

      `"units"`
      :   Specifies a `systemd` unit to mount the partition at boot. Use the partition label to specify the partition. You can create multiple partitions by specifying multiple `"partitions"` entries in this configuration file. If you specify multiple `"partitions"` entries, you must specify a `systemd` unit for each.

      `"contents"`
      :   Specifies the value of `storage.filesystems.path` for `Where`. Specifies the value of `storage.filesystems.device` for `What`.
3. Extract the disabling template value to a file called `disableTemplating.txt` by running the following command:

   ```
   $ oc -n openshift-machine-api get secret <role>-user-data \
   --template='{{index .data.disableTemplating | base64decode}}' | jq > disableTemplating.txt
   ```

   Replace `<role>` with `worker`.
4. Combine the `userData.txt` file and `disableTemplating.txt` file to create a data secret file by running the following command:

   ```
   $ oc -n openshift-machine-api create secret generic <role>-user-data-x5 \
   --from-file=userData=userData.txt \
   --from-file=disableTemplating=disableTemplating.txt
   ```

   For `<role>-user-data-x5`, specify the name of the secret. Replace `<role>` with `worker`.
5. Copy an existing Azure `MachineSet` custom resource (CR) and edit it by running the following command:

   ```
   $ oc edit machineset <machine_set_name>
   ```

   where:

   `<machine_set_name>`
   :   Indicates the machine set that you want to provision machines with ultra disks.
6. Add the following lines in the positions indicated:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   spec:
     template:
       spec:
         metadata:
           labels:
             disk: ultrassd
         providerSpec:
           value:
             ultraSSDCapability: Enabled
             dataDisks:
             - nameSuffix: ultrassd
               lun: 0
               diskSizeGB: 4
               deletionPolicy: Delete
               cachingType: None
               managedDisk:
                 storageAccountType: UltraSSD_LRS
             userDataSecret:
               name: <role>-user-data-x5
   ```

   where:

   `spec.template.spec.metadata.labels.disk`
   :   Specifies a label to use to select a node that is created by this machine set. The example uses `disk.ultrassd` for this value.

   `spec.template.spec.providerSpec.value.ultraSSDCapability`
   :   Enables the use of ultra disks. For `dataDisks`, include the entire stanza.

   `spec.template.spec.providerSpec.value.dataDisks`
   :   Ensure you include the entire stanza for `dataDisks`.

   `spec.template.spec.providerSpec.value.userDataSecret.name`
   :   Specifies the user data secret created earlier. Replace `<role>` with `worker`.
7. Create a machine set by using the updated configuration by running the following command:

   ```
   $ oc create -f <machine_set_name>.yaml
   ```

**Verification**

1. Validate that the machines are created by running the following command:

   ```
   $ oc get machines
   ```

   The machines should be in the `Running` state.
2. For a machine that is running and has a node attached, validate the partition by running the following command:

   ```
   $ oc debug node/<node_name> -- chroot /host lsblk
   ```

   In this command, `oc debug node/<node_name>` starts a debugging shell on the node `<node_name>` and passes a command with `--`. The passed command `chroot /host` provides access to the underlying host OS binaries, and `lsblk` shows the block devices that are attached to the host OS machine.

**Next steps**

* To use an ultra disk from within a pod, create a workload that uses the mount point. Create a YAML file similar to the following example:

  ```
  apiVersion: v1
  kind: Pod
  metadata:
    name: ssd-benchmark1
  spec:
    containers:
    - name: ssd-benchmark1
      image: nginx
      ports:
        - containerPort: 80
          name: "http-server"
      volumeMounts:
      - name: lun0p1
        mountPath: "/tmp"
    volumes:
      - name: lun0p1
        hostPath:
          path: /var/lib/lun0p1
          type: DirectoryOrCreate
    nodeSelector:
      disktype: ultrassd
  ```

##### [2.2.8.2. Troubleshooting resources for machine sets that enable ultra disks](#machineset-troubleshooting-azure-ultra-disk_creating-machineset-azure) Copy linkLink copied to clipboard!

You can recover from issues that you might encounter when you enable ultra disks for machine sets. Review fields, such as disk settings, and ensure that the parameters are correctly configured.

##### [2.2.8.2.1. Incorrect ultra disk configuration](#ts-mapi-attach-misconfigure_creating-machineset-azure) Copy linkLink copied to clipboard!

If an incorrect configuration of the `ultraSSDCapability` parameter is specified in the machine set, the machine provisioning fails.

For example, if the `ultraSSDCapability` parameter is set to `Disabled`, but an ultra disk is specified in the `dataDisks` parameter, the following error message appears:

```
StorageAccountType UltraSSD_LRS can be used only when additionalCapabilities.ultraSSDEnabled is set.
```

* To resolve this issue, verify that your machine set configuration is correct.

##### [2.2.8.2.2. Unsupported disk parameters](#ts-mapi-attach-unsupported_creating-machineset-azure) Copy linkLink copied to clipboard!

If a region, availability zone, or instance size that is not compatible with ultra disks is specified in the machine set, the machine provisioning fails. Check the logs for the following error message:

```
failed to create vm <machine_name>: failure sending request for machine <machine_name>: cannot create vm: compute.VirtualMachinesClient#CreateOrUpdate: Failure sending request: StatusCode=400 -- Original Error: Code="BadRequest" Message="Storage Account type 'UltraSSD_LRS' is not supported <more_information_about_why>."
```

* To resolve this issue, verify that you are using this feature in a supported environment and that your machine set configuration is correct.

##### [2.2.8.2.3. Unable to delete disks](#ts-mapi-delete_creating-machineset-azure) Copy linkLink copied to clipboard!

If the deletion of ultra disks as data disks is not working as expected, the machines are deleted and the data disks are orphaned. You must delete the orphaned disks manually if desired.

#### [2.2.9. Enabling customer-managed encryption keys for a machine set](#machineset-enabling-customer-managed-encryption-azure_creating-machineset-azure) Copy linkLink copied to clipboard!

To enhance data security, enable customer-managed encryption on Microsoft Azure by adding the disk encryption set ID to your machine set.

You can supply an encryption key to Azure to encrypt data on managed disks at rest. You can enable server-side encryption with customer-managed keys by using the Machine API.

An Azure Key Vault, a disk encryption set, and an encryption key are required to use a customer-managed key. The disk encryption set must be in a resource group where the Cloud Credential Operator (CCO) has granted permissions. If not, an additional reader role is required to be granted on the disk encryption set.

**Prerequisites**

* [You created an Azure Key Vault instance (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#create-an-azure-key-vault-instance).
* [You created an instance of a disk encryption set (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#create-an-instance-of-a-diskencryptionset).
* [You granted the disk encryption set access to key vault (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#grant-the-diskencryptionset-access-to-key-vault).

**Procedure**

* Configure the disk encryption set under the `providerSpec` field in your machine set YAML file. For example:

  ```
  providerSpec:
    value:
      osDisk:
        diskSizeGB: 128
        managedDisk:
          diskEncryptionSet:
            id: /subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.Compute/diskEncryptionSets/<disk_encryption_set_name>
          storageAccountType: Premium_LRS
  ```

#### [2.2.10. Configuring trusted launch for Azure virtual machines by using machine sets](#machineset-azure-trusted-launch_creating-machineset-azure) Copy linkLink copied to clipboard!

By editing the machine set YAML file, you can configure the trusted launch for Microsoft Azure virtual machines (VMs) options that a machine set uses for machines that it deploys.

For example, you can configure these machines to use UEFI security features such as Secure Boot or a dedicated virtual Trusted Platform Module (vTPM) instance.

Note

Some feature combinations result in an invalid configuration.

Expand

Table 2.1. UEFI feature combination compatibility

| Secure Boot[1] | vTPM[2] | Valid configuration |
| --- | --- | --- |
| Enabled | Enabled | Yes |
| Enabled | Disabled | Yes |
| Enabled | Omitted | Yes |
| Disabled | Enabled | Yes |
| Omitted | Enabled | Yes |
| Disabled | Disabled | No |
| Omitted | Disabled | No |
| Omitted | Omitted | No |

Show more

1. Using the `secureBoot` field.
2. Using the `virtualizedTrustedPlatformModule` field.

For more information about related features and functionality, see the Microsoft Azure documentation about [Trusted launch for Azure virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch).

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following section under the `providerSpec` field to provide a valid configuration:

   **Sample valid configuration with UEFI Secure Boot and vTPM enabled**

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       machines_v1beta1_machine_openshift_io:
         spec:
           providerSpec:
             value:
               securityProfile:
                 settings:
                   securityType: TrustedLaunch
                   trustedLaunch:
                     uefiSettings:
                       secureBoot: Enabled
                       virtualizedTrustedPlatformModule: Enabled
   # ...
   ```

   where:

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.securityType`
   :   Enables the use of trusted launch for Azure virtual machines. This value is required for all valid configurations.

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings`
   :   Specifies which UEFI security features to use. This section is required for all valid configurations.

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings.secureBoot`
   :   Enables UEFI Secure Boot.

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings.virtualizedTrustedPlatformModule`
   :   Enables the use of a vTPM.

**Verification**

* On the Microsoft Azure portal, review the details for a machine deployed by the machine set and verify that the trusted launch options match the values that you configured.

#### [2.2.11. Configuring Azure confidential virtual machines by using machine sets](#machineset-azure-confidential-vms_creating-machineset-azure) Copy linkLink copied to clipboard!

You can enable Microsoft Azure confidential virtual machines (VMs) to use memory encryption to improve data confidentiality.

Note

Confidential VMs are currently not supported on 64-bit ARM architectures.

By editing the machine set YAML file, you can configure the confidential VM options that a machine set uses for machines that it deploys. For example, you can configure these machines to use UEFI security features such as Secure Boot or a dedicated virtual Trusted Platform Module (vTPM) instance.

For more information about related features and functionality, see the Microsoft Azure documentation about [Confidential virtual machines](https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview).

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following section under the `providerSpec` field:

   **Sample configuration**

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             osDisk:
               # ...
               managedDisk:
                 securityProfile:
                   securityEncryptionType: VMGuestStateOnly
               # ...
             securityProfile:
               settings:
                   securityType: ConfidentialVM
                   confidentialVM:
                     uefiSettings:
                       secureBoot: Disabled
                       virtualizedTrustedPlatformModule: Enabled
             vmSize: Standard_DC16ads_v5
   # ...
   ```

   where:

   `spec.template.spec.providerSpec.value.osDisk.managedDisk.securityProfile`
   :   Specifies security profile settings for the managed disk when using a confidential VM.

   `spec.template.spec.providerSpec.value.osDisk.managedDisk.securityProfile.securityEncryptionType`
   :   Enables encryption of the Microsoft Azure VM Guest State (VMGS) blob. This setting requires the use of vTPM.

   `spec.template.spec.providerSpec.value.securityProfile`
   :   Specifies security profile settings for the confidential VM.

   `spec.template.spec.providerSpec.value.securityProfile.settings.securityType`
   :   Enables the use of confidential VMs. This value is required for all valid configurations.

   `spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings`
   :   Specifies which UEFI security features to use. This section is required for all valid configurations.

   `spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings.secureBoot`
   :   Disables UEFI Secure Boot.

   `spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings.virtualizedTrustedPlatformModule`
   :   Enables the use of a vTPM.

   `spec.template.spec.providerSpec.value.vmSize`
   :   Specifies an instance type that supports confidential VMs.

**Verification**

* On the Microsoft Azure portal, review the details for a machine deployed by the machine set and verify that the confidential VM options match the values that you configured.

#### [2.2.12. Accelerated Networking for Microsoft Azure VMs](#machineset-azure-accelerated-networking_creating-machineset-azure) Copy linkLink copied to clipboard!

You can enable Accelerated Networking, which uses single root I/O virtualization (SR-IOV) to provide Microsoft Azure VMs with a more direct path to the switch, during or after installation. This enhances network performance.

##### [2.2.12.1. Limitations](#machineset-azure-accelerated-networking-limits_creating-machineset-azure) Copy linkLink copied to clipboard!

Consider the following limitations when deciding whether to use Accelerated Networking:

* Accelerated Networking is only supported on clusters where the Machine API is operational.
* Although the minimum requirement for an Azure worker node is two vCPUs, Accelerated Networking requires an Azure VM size that includes at least four vCPUs. To satisfy this requirement, you can change the value of `vmSize` in your machine set. For information about Azure VM sizes, see [Microsoft Azure documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes).

* When this feature is enabled on an existing Azure cluster, only newly provisioned nodes are affected. Currently running nodes are not reconciled. To enable the feature on all nodes, you must replace each existing machine. This can be done for each machine individually, or by scaling the replicas down to zero, and then scaling back up to your desired number of replicas.

##### [2.2.12.2. Enabling Accelerated Networking on an existing Microsoft Azure cluster](#machineset-azure-enabling-accelerated-networking-existing_creating-machineset-azure) Copy linkLink copied to clipboard!

You can enable Accelerated Networking on Microsoft Azure by adding `acceleratedNetworking` to your machine set YAML file. Accelerated Networking uses SR-IOV to help improve network performance for new nodes.

**Prerequisites**

* Have an existing Azure cluster where the Machine API is operational.

**Procedure**

* Add the following to the `providerSpec` field:

  ```
  providerSpec:
    value:
      acceleratedNetworking: true
      vmSize: <azure-vm-size>
  ```

  where:

  `providerSpec.value.acceleratedNetworking`
  :   Enables Accelerated Networking.

  `providerSpec.value.vmSize`
  :   Specifies an Azure VM size that includes at least four vCPUs. For information about VM sizes, see the Microsoft Azure documentation [Sizes for virtual machines in Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes).

**Next steps**

* To enable the feature on currently running nodes, you must replace each existing machine. This can be done for each machine individually, or by scaling the replicas down to zero, and then scaling back up to your desired number of replicas.

**Verification**

* On the Microsoft Azure portal, review the **Networking** settings page for a machine provisioned by the machine set, and verify that the `Accelerated networking` field is set to `Enabled`.

#### [2.2.13. Configuring Capacity Reservations by using machine sets](#machineset-capacity-reservation_creating-machineset-azure) Copy linkLink copied to clipboard!

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define by using on-demand Capacity Reservation with Capacity Reservation groups on Microsoft Azure clusters.

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define.

These parameters specify the VM size, region, and number of instances that you want to reserve. If your Azure subscription quota can accommodate the capacity request, the deployment succeeds.

For more information, including limitations and suggested use cases for this Microsoft Azure offering, see [On-demand Capacity Reservation](https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-overview) in the Azure documentation.

Note

You cannot change an existing Capacity Reservation configuration for a machine set. To use a different Capacity Reservation group, you must replace the machine set and the machines that the previous machine set deployed.

**Prerequisites**

* You have access to the cluster with `cluster-admin` privileges.
* You installed the OpenShift CLI (`oc`).
* You have created a Capacity Reservation group. For more information, see [Create a Capacity Reservation](https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-create) in the Microsoft Azure documentation.

**Procedure**

1. In a text editor, open an existing machine set custom resource (CR) or create a new one.
2. Update the CR to implement your configuration changes:

   **Sample configuration**

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             capacityReservationGroupID: <capacity_reservation_group>
   # ...
   ```

   where:

   `<capacity_reservation_group>`
   :   Specifies the ID of the Capacity Reservation group that you want the machine set to deploy machines on.
3. Save your changes and exit the object specification.

**Verification**

* To verify machine deployment, list the machines that the machine set created by running the following command:

  ```
  $ oc get machines.machine.openshift.io \
    -n openshift-machine-api \
    -l machine.openshift.io/cluster-api-machineset=<machine_set_name>
  ```

  where `<machine_set_name>` is the name of the compute machine set.

  In the output, verify that the characteristics of the listed machines match the parameters of your Capacity Reservation.

#### [2.2.14. Adding a GPU node to an existing OpenShift Container Platform cluster](#nvidia-gpu-aws-adding-a-gpu-node_creating-machineset-azure) Copy linkLink copied to clipboard!

To provide specialized hardware for compute-intensive workloads that require NVIDIA GPU acceleration, you can copy and modify a default compute machine set configuration to create a GPU-enabled machine set and machines for the Microsoft Azure cloud provider.

The following table lists the validated instance types:

Expand

| vmSize | NVIDIA GPU accelerator | Maximum number of GPUs | Architecture |
| --- | --- | --- | --- |
| `Standard_NC24s_v3` | V100 | 4 | x86 |
| `Standard_NC4as_T4_v3` | T4 | 1 | x86 |
| `ND A100 v4` | A100 | 8 | x86 |

Show more

Note

By default, Microsoft Azure subscriptions do not have a quota for the Microsoft Azure instance types with GPU. Customers have to request a quota increase for the Microsoft Azure instance families in the preceding list.

**Procedure**

1. View the machines and machine sets that exist in the `openshift-machine-api` namespace by running the following command. Each compute machine set is associated with a different availability zone within the Microsoft Azure region. The installation program automatically load balances compute machines across availability zones.

   ```
   $ oc get machineset -n openshift-machine-api
   ```

   **Example output**

   ```
   NAME                              DESIRED   CURRENT   READY   AVAILABLE   AGE
   myclustername-worker-centralus1   1         1         1       1           6h9m
   myclustername-worker-centralus2   1         1         1       1           6h9m
   myclustername-worker-centralus3   1         1         1       1           6h9m
   ```
2. Make a copy of one of the existing compute `MachineSet` definitions and output the result to a YAML file by running the following command. This will be the basis for the GPU-enabled compute machine set definition.

   ```
   $ oc get machineset -n openshift-machine-api myclustername-worker-centralus1 -o yaml > machineset-azure.yaml
   ```
3. View the content of the compute machine set:

   ```
   $ cat machineset-azure.yaml
   ```

   **Example `machineset-azure.yaml` file**

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   metadata:
     annotations:
       machine.openshift.io/GPU: "0"
       machine.openshift.io/memoryMb: "16384"
       machine.openshift.io/vCPU: "4"
     creationTimestamp: "2023-02-06T14:08:19Z"
     generation: 1
     labels:
       machine.openshift.io/cluster-api-cluster: myclustername
       machine.openshift.io/cluster-api-machine-role: worker
       machine.openshift.io/cluster-api-machine-type: worker
     name: myclustername-worker-centralus1
     namespace: openshift-machine-api
     resourceVersion: "23601"
     uid: acd56e0c-7612-473a-ae37-8704f34b80de
   spec:
     replicas: 1
     selector:
       matchLabels:
         machine.openshift.io/cluster-api-cluster: myclustername
         machine.openshift.io/cluster-api-machineset: myclustername-worker-centralus1
     template:
       metadata:
         labels:
           machine.openshift.io/cluster-api-cluster: myclustername
           machine.openshift.io/cluster-api-machine-role: worker
           machine.openshift.io/cluster-api-machine-type: worker
           machine.openshift.io/cluster-api-machineset: myclustername-worker-centralus1
       spec:
         lifecycleHooks: {}
         metadata: {}
         providerSpec:
           value:
             acceleratedNetworking: true
             apiVersion: machine.openshift.io/v1beta1
             credentialsSecret:
               name: azure-cloud-credentials
               namespace: openshift-machine-api
             diagnostics: {}
             image:
               offer: ""
               publisher: ""
               resourceID: /resourceGroups/myclustername-rg/providers/Microsoft.Compute/galleries/gallery_myclustername_n6n4r/images/myclustername-gen2/versions/latest
               sku: ""
               version: ""
             kind: AzureMachineProviderSpec
             location: centralus
             managedIdentity: myclustername-identity
             metadata:
               creationTimestamp: null
             networkResourceGroup: myclustername-rg
             osDisk:
               diskSettings: {}
               diskSizeGB: 128
               managedDisk:
                 storageAccountType: Premium_LRS
               osType: Linux
             publicIP: false
             publicLoadBalancer: myclustername
             resourceGroup: myclustername-rg
             spotVMOptions: {}
             subnet: myclustername-worker-subnet
             userDataSecret:
               name: worker-user-data
             vmSize: Standard_D4s_v3
             vnet: myclustername-vnet
             zone: "1"
   status:
     availableReplicas: 1
     fullyLabeledReplicas: 1
     observedGeneration: 1
     readyReplicas: 1
     replicas: 1
   ```
4. Make a copy of the `machineset-azure.yaml` file by running the following command:

   ```
   $ cp machineset-azure.yaml machineset-azure-gpu.yaml
   ```
5. Update the following fields in `machineset-azure-gpu.yaml`:

   * Change `.metadata.name` to a name containing `gpu`.
   * Change `.spec.selector.matchLabels["machine.openshift.io/cluster-api-machineset"]` to match the new .metadata.name.
   * Change `.spec.template.metadata.labels["machine.openshift.io/cluster-api-machineset"]` to match the new `.metadata.name`.
   * Change `.spec.template.spec.providerSpec.value.vmSize` to `Standard_NC4as_T4_v3`.

     **Example `machineset-azure-gpu.yaml` file**

     ```
     apiVersion: machine.openshift.io/v1beta1
     kind: MachineSet
     metadata:
       annotations:
         machine.openshift.io/GPU: "1"
         machine.openshift.io/memoryMb: "28672"
         machine.openshift.io/vCPU: "4"
       creationTimestamp: "2023-02-06T20:27:12Z"
       generation: 1
       labels:
         machine.openshift.io/cluster-api-cluster: myclustername
         machine.openshift.io/cluster-api-machine-role: worker
         machine.openshift.io/cluster-api-machine-type: worker
       name: myclustername-nc4ast4-gpu-worker-centralus1
       namespace: openshift-machine-api
       resourceVersion: "166285"
       uid: 4eedce7f-6a57-4abe-b529-031140f02ffa
     spec:
       replicas: 1
       selector:
         matchLabels:
           machine.openshift.io/cluster-api-cluster: myclustername
           machine.openshift.io/cluster-api-machineset: myclustername-nc4ast4-gpu-worker-centralus1
       template:
         metadata:
           labels:
             machine.openshift.io/cluster-api-cluster: myclustername
             machine.openshift.io/cluster-api-machine-role: worker
             machine.openshift.io/cluster-api-machine-type: worker
             machine.openshift.io/cluster-api-machineset: myclustername-nc4ast4-gpu-worker-centralus1
         spec:
           lifecycleHooks: {}
           metadata: {}
           providerSpec:
             value:
               acceleratedNetworking: true
               apiVersion: machine.openshift.io/v1beta1
               credentialsSecret:
                 name: azure-cloud-credentials
                 namespace: openshift-machine-api
               diagnostics: {}
               image:
                 offer: ""
                 publisher: ""
                 resourceID: /resourceGroups/myclustername-rg/providers/Microsoft.Compute/galleries/gallery_myclustername_n6n4r/images/myclustername-gen2/versions/latest
                 sku: ""
                 version: ""
               kind: AzureMachineProviderSpec
               location: centralus
               managedIdentity: myclustername-identity
               metadata:
                 creationTimestamp: null
               networkResourceGroup: myclustername-rg
               osDisk:
                 diskSettings: {}
                 diskSizeGB: 128
                 managedDisk:
                   storageAccountType: Premium_LRS
                 osType: Linux
               publicIP: false
               publicLoadBalancer: myclustername
               resourceGroup: myclustername-rg
               spotVMOptions: {}
               subnet: myclustername-worker-subnet
               userDataSecret:
                 name: worker-user-data
               vmSize: Standard_NC4as_T4_v3
               vnet: myclustername-vnet
               zone: "1"
     status:
       availableReplicas: 1
       fullyLabeledReplicas: 1
       observedGeneration: 1
       readyReplicas: 1
       replicas: 1
     ```
6. To verify your changes, perform a `diff` of the original compute definition and the new GPU-enabled node definition by running the following command:

   ```
   $ diff machineset-azure.yaml machineset-azure-gpu.yaml
   ```

   **Example output**

   ```
   14c14
   <   name: myclustername-worker-centralus1
   ---
   >   name: myclustername-nc4ast4-gpu-worker-centralus1
   23c23
   <       machine.openshift.io/cluster-api-machineset: myclustername-worker-centralus1
   ---
   >       machine.openshift.io/cluster-api-machineset: myclustername-nc4ast4-gpu-worker-centralus1
   30c30
   <         machine.openshift.io/cluster-api-machineset: myclustername-worker-centralus1
   ---
   >         machine.openshift.io/cluster-api-machineset: myclustername-nc4ast4-gpu-worker-centralus1
   67c67
   <           vmSize: Standard_D4s_v3
   ---
   >           vmSize: Standard_NC4as_T4_v3
   ```
7. Create the GPU-enabled compute machine set from the definition file by running the following command:

   ```
   $ oc create -f machineset-azure-gpu.yaml
   ```

   **Example output**

   ```
   machineset.machine.openshift.io/myclustername-nc4ast4-gpu-worker-centralus1 created
   ```
8. View the machines and machine sets that exist in the `openshift-machine-api` namespace by running the following command. Each compute machine set is associated with a different availability zone within the Microsoft Azure region. The installation program automatically load balances compute machines across availability zones.

   ```
   $ oc get machineset -n openshift-machine-api
   ```

   **Example output**

   ```
   NAME                                               DESIRED   CURRENT   READY   AVAILABLE   AGE
   clustername-n6n4r-nc4ast4-gpu-worker-centralus1    1         1         1       1           122m
   clustername-n6n4r-worker-centralus1                1         1         1       1           8h
   clustername-n6n4r-worker-centralus2                1         1         1       1           8h
   clustername-n6n4r-worker-centralus3                1         1         1       1           8h
   ```
9. View the machines that exist in the `openshift-machine-api` namespace by running the following command. You can only configure one compute machine per set, although you can scale a compute machine set to add a node in a particular region and zone.

   ```
   $ oc get machines -n openshift-machine-api
   ```

   **Example output**

   ```
   NAME                                                PHASE     TYPE                   REGION      ZONE   AGE
   myclustername-master-0                              Running   Standard_D8s_v3        centralus   2      6h40m
   myclustername-master-1                              Running   Standard_D8s_v3        centralus   1      6h40m
   myclustername-master-2                              Running   Standard_D8s_v3        centralus   3      6h40m
   myclustername-nc4ast4-gpu-worker-centralus1-w9bqn   Running      centralus   1      21m
   myclustername-worker-centralus1-rbh6b               Running   Standard_D4s_v3        centralus   1      6h38m
   myclustername-worker-centralus2-dbz7w               Running   Standard_D4s_v3        centralus   2      6h38m
   myclustername-worker-centralus3-p9b8c               Running   Standard_D4s_v3        centralus   3      6h38m
   ```
10. View the existing nodes, machines, and machine sets by running the following command. Note that each node is an instance of a machine definition with a specific Azure region and OpenShift Container Platform role.

    ```
    $ oc get nodes
    ```

    **Example output**

    ```
    NAME                                                STATUS   ROLES                  AGE     VERSION
    myclustername-master-0                              Ready    control-plane,master   6h39m   v1.35.4
    myclustername-master-1                              Ready    control-plane,master   6h41m   v1.35.4
    myclustername-master-2                              Ready    control-plane,master   6h39m   v1.35.4
    myclustername-nc4ast4-gpu-worker-centralus1-w9bqn   Ready    worker                 14m     v1.35.4
    myclustername-worker-centralus1-rbh6b               Ready    worker                 6h29m   v1.35.4
    myclustername-worker-centralus2-dbz7w               Ready    worker                 6h29m   v1.35.4
    myclustername-worker-centralus3-p9b8c               Ready    worker                 6h31m   v1.35.4
    ```
11. View the list of compute machine sets:

    ```
    $ oc get machineset -n openshift-machine-api
    ```

    **Example output**

    ```
    NAME                                   DESIRED   CURRENT   READY   AVAILABLE   AGE
    myclustername-worker-centralus1        1         1         1       1           8h
    myclustername-worker-centralus2        1         1         1       1           8h
    myclustername-worker-centralus3        1         1         1       1           8h
    ```
12. Create the GPU-enabled compute machine set from the definition file by running the following command:

    ```
    $ oc create -f machineset-azure-gpu.yaml
    ```
13. View the list of compute machine sets:

    ```
    oc get machineset -n openshift-machine-api
    ```

    **Example output**

    ```
    NAME                                          DESIRED   CURRENT   READY   AVAILABLE   AGE
    myclustername-nc4ast4-gpu-worker-centralus1   1         1         1       1           121m
    myclustername-worker-centralus1               1         1         1       1           8h
    myclustername-worker-centralus2               1         1         1       1           8h
    myclustername-worker-centralus3               1         1         1       1           8h
    ```

**Verification**

1. View the machine set you created by running the following command:

   ```
   $ oc get machineset -n openshift-machine-api | grep gpu
   ```

   The MachineSet replica count is set to `1` so a new `Machine` object is created automatically.

   **Example output**

   ```
   myclustername-nc4ast4-gpu-worker-centralus1   1         1         1       1           121m
   ```
2. View the `Machine` object that the machine set created by running the following command:

   ```
   $ oc -n openshift-machine-api get machines | grep gpu
   ```

   **Example output**

   ```
   myclustername-nc4ast4-gpu-worker-centralus1-w9bqn   Running   Standard_NC4as_T4_v3   centralus   1      21m
   ```

Note

There is no need to specify a namespace for the node. The node definition is cluster scoped.

#### [2.2.15. Deploying the Node Feature Discovery Operator](#nvidia-gpu-aws-deploying-the-node-feature-discovery-operator_creating-machineset-azure) Copy linkLink copied to clipboard!

After the GPU-enabled node is created, you need to discover the GPU-enabled node so it can be scheduled. To do this, install the Node Feature Discovery (NFD) Operator.

The NFD Operator identifies hardware device features in nodes. It solves the general problem of identifying and cataloging hardware resources in the infrastructure nodes so they can be made available to OpenShift Container Platform.

**Procedure**

1. Install the Node Feature Discovery Operator from the software catalog in the OpenShift Container Platform console.
2. After installing the NFD Operator, select **Node Feature Discovery** from the installed Operators list and select **Create instance**. This installs the `nfd-master` and `nfd-worker` pods, one `nfd-worker` pod for each compute node, in the `openshift-nfd` namespace.
3. Verify that the Operator is installed and running by running the following command:

   ```
   $ oc get pods -n openshift-nfd
   ```

   **Example output**

   ```
   NAME                                       READY    STATUS     RESTARTS   AGE

   nfd-controller-manager-8646fcbb65-x5qgk    2/2      Running 7  (8h ago)   1d
   ```
4. Browse to the installed Operator in the console and select **Create Node Feature Discovery**.
5. Select **Create** to build a NFD custom resource. This creates NFD pods in the `openshift-nfd` namespace that poll the OpenShift Container Platform nodes for hardware resources and catalog them.

**Verification**

1. After a successful build, verify that a NFD pod is running on each nodes by running the following command:

   ```
   $ oc get pods -n openshift-nfd
   ```

   **Example output**

   ```
   NAME                                       READY   STATUS      RESTARTS        AGE
   nfd-controller-manager-8646fcbb65-x5qgk    2/2     Running     7 (8h ago)      12d
   nfd-master-769656c4cb-w9vrv                1/1     Running     0               12d
   nfd-worker-qjxb2                           1/1     Running     3 (3d14h ago)   12d
   nfd-worker-xtz9b                           1/1     Running     5 (3d14h ago)   12d
   ```

   The NFD Operator uses vendor PCI IDs to identify hardware in a node. NVIDIA uses the PCI ID `10de`.
2. View the NVIDIA GPU discovered by the NFD Operator by running the following command:

   ```
   $ oc describe node ip-10-0-132-138.us-east-2.compute.internal | egrep 'Roles|pci'
   ```

   **Example output**

   ```
   Roles: worker

   feature.node.kubernetes.io/pci-1013.present=true

   feature.node.kubernetes.io/pci-10de.present=true

   feature.node.kubernetes.io/pci-1d0f.present=true
   ```

   `10de` appears in the node feature list for the GPU-enabled node. This mean the NFD Operator correctly identified the node from the GPU-enabled MachineSet.

### [2.3. Creating a compute machine set on Azure Stack Hub](#creating-machineset-azure-stack-hub) Copy linkLink copied to clipboard!

You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on Microsoft Azure Stack Hub. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

#### [2.3.1. Sample YAML for a compute machine set custom resource on Azure Stack Hub](#machineset-yaml-azure-stack-hub_creating-machineset-azure-stack-hub) Copy linkLink copied to clipboard!

You can create a machine set on Microsoft Azure Stack Hub. By defining a YAML configuration with specific cluster IDs and provider details, you can automate the provisioning of specialized nodes.

The Microsoft Azure sample YAML defines a compute machine set that runs in the `1` Azure zone in a region and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <role>
    machine.openshift.io/cluster-api-machine-type: <role>
  name: <infrastructure_id>-<role>-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
    spec:
      metadata:
        creationTimestamp: null
        labels:
          node-role.kubernetes.io/<role>: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          availabilitySet: <availability_set>
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image:
            offer: ""
            publisher: ""
            resourceID: /resourceGroups/<infrastructure_id>-rg/providers/Microsoft.Compute/images/<infrastructure_id>
            sku: ""
            version: ""
          internalLoadBalancer: ""
          kind: AzureMachineProviderSpec
          location: <region>
          managedIdentity: <infrastructure_id>-identity
          metadata:
            creationTimestamp: null
          natRule: null
          networkResourceGroup: ""
          osDisk:
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Linux
          publicIP: false
          publicLoadBalancer: ""
          resourceGroup: <infrastructure_id>-rg
          sshPrivateKey: ""
          sshPublicKey: ""
          subnet: <infrastructure_id>-<role>-subnet
          userDataSecret:
            name: worker-user-data
          vmSize: Standard_DS4_v2
          vnet: <infrastructure_id>-vnet
          zone: "1"
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift Container Platform CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

    You can obtain the subnet by running the following command:

    ```
    $  oc -n openshift-machine-api \
        -o jsonpath='{.spec.template.spec.providerSpec.value.subnet}{"\n"}' \
        get machineset/<infrastructure_id>-worker-centralus1
    ```

    You can obtain the vnet by running the following command:

    ```
    $  oc -n openshift-machine-api \
        -o jsonpath='{.spec.template.spec.providerSpec.value.vnet}{"\n"}' \
        get machineset/<infrastructure_id>-worker-centralus1
    ```

`<role>`
:   Specifies the node label to add.

`<infrastructure_id>-<role>-<region>`
:   Specifies the infrastructure ID, node label, and region.

`<region>`
:   Specifies the region to place machines on.

    Note

    The `spec.template.spec.providerSpec.value.zone` specifies the zone within your region to place machines on. Be sure that your region supports the zone that you specify.

`<availability_set>`
:   Specifies the availability set for the cluster.

`<image>`
:   Specifies the boot image to use. You should use the use the latest image when adding a new machine set.

Note

Machine sets running on Azure Stack Hub do not support non-guaranteed Spot VMs.

#### [2.3.2. Creating a compute machine set](#machineset-creating_creating-machineset-azure-stack-hub) Copy linkLink copied to clipboard!

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

**Prerequisites**

* Deploy an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.
* Create an availability set in which to deploy Azure Stack Hub compute machines.

**Procedure**

1. Create a new YAML file that contains the compute machine set custom resource (CR) sample and is named `<file_name>.yaml`.

   Ensure that you set the `<availabilitySet>`, `<clusterID>`, and `<role>` parameter values.
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

#### [2.3.3. Labeling GPU machine sets for the cluster autoscaler](#machineset-label-gpu-autoscaler_creating-machineset-azure-stack-hub) Copy linkLink copied to clipboard!

Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

**Prerequisites**

* Your cluster uses a cluster autoscaler.

**Procedure**

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    name: machine-set-name
  spec:
    template:
      spec:
        metadata:
          labels:
            cluster-api/accelerator: <accelerator_name>
  ```

  where:

  `<accelerator_name>`
  :   Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.

      Note

      You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR. For more information, see "Cluster autoscaler resource definition".

#### [2.3.4. Enabling Microsoft Azure boot diagnostics](#machineset-azure-boot-diagnostics_creating-machineset-azure-stack-hub) Copy linkLink copied to clipboard!

You can enable boot diagnostics on Microsoft Azure machines that your machine set creates. Use this to store console logs that you can use to troubleshoot why a node fails to boot.

**Prerequisites**

* Have an existing Azure Stack Hub cluster.

**Procedure**

* Add the `diagnostics` configuration that is applicable to your storage type to the `providerSpec` field in your machine set YAML file:

  + For an Azure Managed storage account:

    ```
    providerSpec:
      value:
        diagnostics:
          boot:
            storageAccountType: <azure_managed>
    ```

    where:

    `<azure_managed>`
    :   Specifies an Azure Managed storage account.
  + For an Azure Unmanaged storage account:

    ```
    providerSpec:
      value:
        diagnostics:
          boot:
            storageAccountType: <customer_managed>
            customerManaged:
              storageAccountURI: <https://<storage_account>.blob.core.windows.net>
    ```

    where:

    `<customer_managed>`
    :   Specifies an Azure Unmanaged storage account.

    `https://<storage_account>.blob.core.windows.net`
    :   Specifies the storage account URL. Replace `<storage_account>` with the name of your storage account.

    Note

    Only the Azure Blob Storage data service is supported.

**Verification**

* On the Azure portal, review the **Boot diagnostics** page for a machine deployed by the machine set, and verify that you can see the serial logs for the machine.

#### [2.3.5. Enabling customer-managed encryption keys for a machine set](#machineset-enabling-customer-managed-encryption-azure_creating-machineset-azure-stack-hub) Copy linkLink copied to clipboard!

To enhance data security, enable customer-managed encryption on Microsoft Azure by adding the disk encryption set ID to your machine set.

You can supply an encryption key to Azure to encrypt data on managed disks at rest. You can enable server-side encryption with customer-managed keys by using the Machine API.

An Azure Key Vault, a disk encryption set, and an encryption key are required to use a customer-managed key. The disk encryption set must be in a resource group where the Cloud Credential Operator (CCO) has granted permissions. If not, an additional reader role is required to be granted on the disk encryption set.

**Prerequisites**

* [You created an Azure Key Vault instance (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#create-an-azure-key-vault-instance).
* [You created an instance of a disk encryption set (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#create-an-instance-of-a-diskencryptionset).
* [You granted the disk encryption set access to key vault (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#grant-the-diskencryptionset-access-to-key-vault).

**Procedure**

* Configure the disk encryption set under the `providerSpec` field in your machine set YAML file. For example:

  ```
  providerSpec:
    value:
      osDisk:
        diskSizeGB: 128
        managedDisk:
          diskEncryptionSet:
            id: /subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.Compute/diskEncryptionSets/<disk_encryption_set_name>
          storageAccountType: Premium_LRS
  ```

### [2.4. Creating a compute machine set on Google Cloud](#creating-machineset-gcp) Copy linkLink copied to clipboard!

You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on Google Cloud. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

#### [2.4.1. Sample YAML for a compute machine set custom resource on Google Cloud](#machineset-yaml-gcp_creating-machineset-gcp) Copy linkLink copied to clipboard!

The sample YAML defines a compute machine set for Google Cloud, enabling the automated provisioning of nodes within a specific VPC. When you apply this configuration by using the OpenShift Container Platform CLI, you can ensure consistent scaling, scheduling, and infrastructure ID labeling for compute resources in your cluster.

The sample YAML defines a compute machine set that runs in Google Cloud and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`, where `<role>` is the node label to add.

##### [2.4.1.1. Values obtained by using the OpenShift CLI](#cpmso-yaml-provider-spec-gcp-oc_creating-machineset-gcp) Copy linkLink copied to clipboard!

In the following example, you can obtain some of the values for your cluster by using the OpenShift Container Platform CLI.

Infrastructure ID
:   The `<infrastructure_id>` string is the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

Image path
:   The `<path_to_image>` string is the path to the image that was used to create the disk. If you have the OpenShift CLI installed, you can obtain the path to the image by running the following command:

    ```
    $ oc -n openshift-machine-api \
      -o jsonpath='{.spec.template.spec.providerSpec.value.disks[0].image}{"\n"}' \
      get machineset/<infrastructure_id>-worker-a
    ```

**Sample Google Cloud `MachineSet` values**

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-w-a
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-w-a
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-w-a
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/<role>: ""
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
            image: <path_to_image>
            labels: null
            sizeGb: 128
            type: pd-ssd
          gcpMetadata:
          - key: <custom_metadata_key>
            value: <custom_metadata_value>
          kind: GCPMachineProviderSpec
          machineType: n1-standard-4
          metadata:
            creationTimestamp: null
          networkInterfaces:
          - network: <infrastructure_id>-network
            subnetwork: <infrastructure_id>-worker-subnet
          projectID: <project_name>
          region: us-central1
          serviceAccounts:
          - email: <infrastructure_id>-w@<project_name>.iam.gserviceaccount.com
            scopes:
            - https://www.googleapis.com/auth/cloud-platform
          tags:
            - <infrastructure_id>-worker
          userDataSecret:
            name: worker-user-data
          zone: us-central1-a
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster.

`<role>`
:   Specifies the node label to add.

`<path_to_image>`
:   Specifies the path to the image that is used as a boot image in current compute machine sets. You should use the use the latest image when adding a new machine set. To use a Google Cloud Marketplace image, specify the offer to use:

    * OpenShift Container Platform: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-ocp-413-x86-64-202305021736`
    * OpenShift Platform Plus: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-opp-413-x86-64-202305021736`
    * OpenShift Kubernetes Engine: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-oke-413-x86-64-202305021736`

`<gcpMetadata>`
:   Optional: Specifies the custom metadata in the form of a `key:value` pair. For example use cases, see the Google Cloud documentation for [setting custom metadata](https://cloud.google.com/compute/docs/metadata/setting-custom-metadata).

`<project_name>`
:   Specifies the name of the Google Cloud project that you use for your cluster.

`<serviceAccounts>`
:   Specifies a single service account. Multiple service accounts are not supported.

#### [2.4.2. Creating a compute machine set](#machineset-creating_creating-machineset-gcp) Copy linkLink copied to clipboard!

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

#### [2.4.3. Labeling GPU machine sets for the cluster autoscaler](#machineset-label-gpu-autoscaler_creating-machineset-gcp) Copy linkLink copied to clipboard!

Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

**Prerequisites**

* Your cluster uses a cluster autoscaler.

**Procedure**

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    name: machine-set-name
  spec:
    template:
      spec:
        metadata:
          labels:
            cluster-api/accelerator: <accelerator_name>
  ```

  where:

  `<accelerator_name>`
  :   Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.

      Note

      You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR. For more information, see "Cluster autoscaler resource definition".

#### [2.4.4. Configuring persistent disk types by using machine sets](#machineset-gcp-pd-disk-types_creating-machineset-gcp) Copy linkLink copied to clipboard!

Configure the persistent disk type for your machine set on Google Cloud to match your workload requirements. Editing the `MachineSet` YAML file allows you to choose between standard, balanced, or SSD persistent disks.

For more information about persistent disk types, compatibility, regional availability, and limitations, see the Google Cloud Compute Engine documentation about [persistent disks](https://cloud.google.com/compute/docs/disks#pdspecs).

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following line under the `providerSpec` field:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             disks:
               type: <pd-disk-type>
   ```

   where:

   `spec.template.spec.providerSpec.value.disks.type`
   :   Specifies the persistent disk type. Valid values are `pd-ssd`, `pd-standard`, and `pd-balanced`. The default value is `pd-standard`.

**Verification**

* Using the Google Cloud console, review the details for a machine deployed by the machine set and verify that the `Type` field matches the configured disk type.

#### [2.4.5. Configuring Confidential VM by using machine sets](#machineset-gcp-confidential-vm_creating-machineset-gcp) Copy linkLink copied to clipboard!

You create machine sets to scale clusters on Google Cloud. By editing the machine set YAML file, you can configure the Confidential VM options that a machine set uses for machines that it deploys.

For more information about Confidential VM features, functions, and compatibility, see the Google Cloud Compute Engine documentation about [Confidential VM](https://cloud.google.com/confidential-computing/confidential-vm/docs/about-cvm#confidential-vm).

Note

Confidential VMs are currently not supported on 64-bit ARM architectures. If you use Confidential VM, you must ensure that you select a supported region. For details on supported regions and configurations, see the Google Cloud Compute Engine documentation about [supported zones](https://cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones).

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following section under the `providerSpec` field:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             confidentialCompute: Enabled
             onHostMaintenance: Terminate
             machineType: n2d-standard-8
   # ...
   ```

   where:

   `spec.template.spec.providerSpec.value.confidentialCompute`
   :   Specifies whether Confidential VM is enabled. The following values are valid:

   `Enabled`
   :   Enables Confidential VM with a default selection of Confidential VM technology. The default selection is AMD Secure Encrypted Virtualization (AMD SEV).

       Important

       The `Enabled` value selects Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV), which is deprecated.

   `Disabled`
   :   Disables Confidential VM.

   `AMDEncryptedVirtualizationNestedPaging`
   :   Enables Confidential VM using AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). AMD SEV-SNP supports n2d machines.

   `AMDEncryptedVirtualization`
   :   Enables Confidential VM using AMD SEV. AMD SEV supports c2d, n2d, and c3d machines.

       Important

       The use of Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV) has been deprecated and will be removed in a future release.

   `IntelTrustedDomainExtensions`
   :   Enables Confidential VM using Intel Trusted Domain Extensions (Intel TDX). Intel TDX supports n2d machines.

   `spec.template.spec.providerSpec.value.onHostMaintenance`
   :   Specifies the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VM does not support live VM migration.

   `spec.template.spec.providerSpec.value.machineType`
   :   Specifies a machine type that supports the Confidential VM option that you specified in the `confidentialCompute` field.

**Verification**

* On the Google Cloud console, review the details for a machine deployed by the machine set and verify that the Confidential VM options match the values that you configured.

#### [2.4.6. Machine sets that deploy machines as Spot VMs](#machineset-non-guaranteed-instance_creating-machineset-gcp) Copy linkLink copied to clipboard!

You can save on costs by creating a compute machine set running on Google Cloud that deploys machines as non-guaranteed Spot VMs. Spot VMs use excess Compute Engine capacity and are less expensive than normal instances. You can use Spot VMs for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.

Note

Google Cloud recommends using Spot VMs over preemptible VMs because Spot VMs include new features that preemptible VMs do not support.

Google Cloud Compute Engine can terminate a Spot VM at any time. Compute Engine sends a best-effort preemption notice to the user indicating that an interruption will occur after 30 seconds. OpenShift Container Platform begins to remove the workloads from the affected instances when Compute Engine issues the preemption notice. An ACPI G3 Mechanical Off signal is sent to the operating system after 30 seconds if the instance is not stopped. The Spot VM is then transitioned to a `TERMINATED` state by Compute Engine.

Interruptions can occur when using Spot VMs for the following reasons:

* There is a system or maintenance event
* The supply of Spot VMs decreases

When Google Cloud terminates an instance, a termination handler running on the Spot VM node deletes the machine resource. To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a Spot VM.

##### [2.4.6.1. Creating Spot VMs by using compute machine sets](#machineset-creating-non-guaranteed-instance_creating-machineset-gcp) Copy linkLink copied to clipboard!

You can save on costs by creating a compute machine set that deploys machines as non-guaranteed instances. To launch a Spot VM on Google Cloud, you add `provisioningModel: "Spot"` to your compute machine set YAML file.

**Procedure**

* Add the following line under the `providerSpec` field:

  ```
  providerSpec:
    value:
      provisioningModel: "Spot"
  ```

  If you specify `provisioningModel: "Spot"`, the machine is labeled as an `interruptible-instance` after the instance is launched.

  Note

  This parameter is not compatible with setting the `providerSpec.value.preemptible` value to `true`.

#### [2.4.7. Machine sets that deploy machines preemptible VM instances](#machineset-non-guaranteed-instance_legacy-preempt) Copy linkLink copied to clipboard!

You can save on costs by creating a compute machine set running on Google Cloud that deploys machines as non-guaranteed preemptible VM instances. Preemptible VM instances use excess Compute Engine capacity and are less expensive than normal instances. You can use preemptible VM instances for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.

Note

Google Cloud recommends using Spot VMs over preemptible VMs because Spot VMs include new features that preemptible VMs do not support.

Google Cloud Compute Engine can terminate a preemptible VM instance at any time. Compute Engine sends a preemption notice to the user indicating that an interruption will occur after 30 seconds. OpenShift Container Platform begins to remove the workloads from the affected instances when Compute Engine issues the preemption notice. An ACPI G3 Mechanical Off signal is sent to the operating system after 30 seconds if the instance is not stopped. The preemptible VM instance is then transitioned to a `TERMINATED` state by Compute Engine.

Interruptions can occur when using preemptible VM instances for the following reasons:

* There is a system or maintenance event
* The supply of preemptible VM instances decreases
* The instance reaches the end of the allotted 24-hour period for preemptible VM instances

When Google Cloud terminates an instance, a termination handler running on the preemptible VM instance node deletes the machine resource. To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a preemptible VM instance.

##### [2.4.7.1. Creating preemptible VM instances by using compute machine sets](#machineset-creating-non-guaranteed-instance_legacy-preempt) Copy linkLink copied to clipboard!

You can save on costs by creating a compute machine set that deploys machines as non-guaranteed instances. To launch a preemptible VM instance on Google Cloud, you add `preemptible` to your compute machine set YAML file.

Note

Google Cloud recommends using Spot VMs over preemptible VMs because Spot VMs include new features that preemptible VMs do not support.

**Procedure**

* Add the following line under the `providerSpec` field:

  ```
  providerSpec:
    value:
      preemptible: true
  ```

  If `preemptible` is set to `true`, the machine is labeled as an `interruptible-instance` after the instance is launched.

  Note

  This parameter is not compatible with setting the `providerSpec.value.provisioningModel` value to `"Spot"`.

#### [2.4.8. Configuring Shielded VM options by using machine sets](#machineset-gcp-shielded-vms_creating-machineset-gcp) Copy linkLink copied to clipboard!

To help secure your cluster instances, you can configure Shielded Virtual Machine (VM) options for your machine sets on Google Cloud by editing the `MachineSet` YAML file.

For more information about Shielded VM features and functionality, see the Google Cloud Compute Engine documentation about [Shielded VM](https://cloud.google.com/compute/shielded-vm/docs/shielded-vm).

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following section under the `providerSpec` field:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             shieldedInstanceConfig:
               integrityMonitoring: Enabled
               secureBoot: Disabled
               virtualizedTrustedPlatformModule: Enabled
   # ...
   ```

   where:

   `spec.template.spec.providerSpec.value.shieldedInstanceConfig`
   :   Specifies the Shielded VM configuration.

   `spec.template.spec.providerSpec.value.shieldedInstanceConfig.integrityMonitoring`
   :   Specifies whether integrity monitoring is enabled. Valid values are `Disabled` or `Enabled`.

       Note

       When integrity monitoring is enabled, you must not disable virtual trusted platform module (vTPM).

   `spec.template.spec.providerSpec.value.shieldedInstanceConfig.secureBoot`
   :   Specifies whether UEFI Secure Boot is enabled. Valid values are `Disabled` or `Enabled`.

   `spec.template.spec.providerSpec.value.shieldedInstanceConfig.virtualizedTrustedPlatformModule`
   :   Specifies whether vTPM is enabled. Valid values are `Disabled` or `Enabled`.

**Verification**

* Using the Google Cloud console, review the details for a machine deployed by the machine set and verify that the Shielded VM options match the values that you configured.

#### [2.4.9. Enabling customer-managed encryption keys for a machine set](#machineset-gcp-enabling-customer-managed-encryption_creating-machineset-gcp) Copy linkLink copied to clipboard!

Use Google Cloud Compute Engine to supply an encryption key to encrypt data on disks at rest. The key is used to encrypt the data encryption key, not to encrypt the customer’s data. By default, Compute Engine encrypts this data by using Compute Engine keys.

You can enable encryption with a customer-managed key in clusters that use the Machine API. You must first [create a KMS key](https://cloud.google.com/compute/docs/disks/customer-managed-encryption#before_you_begin) and assign the correct permissions to a service account. The KMS key name, key ring name, and location are required to allow a service account to use your key.

Note

If you do not want to use a dedicated service account for the KMS encryption, the Compute Engine default service account is used instead. You must grant the default service account permission to access the keys if you do not use a dedicated service account. The Compute Engine default service account name follows the `service-<project_number>@compute-system.iam.gserviceaccount.com` pattern.

**Procedure**

1. To allow a specific service account to use your KMS key and to grant the service account the correct IAM role, run the following command with your KMS key name, key ring name, and location:

   ```
   $ gcloud kms keys add-iam-policy-binding <key_name> \
     --keyring <key_ring_name> \
     --location <key_ring_location> \
     --member "serviceAccount:service-<project_number>@compute-system.iam.gserviceaccount.com” \
     --role roles/cloudkms.cryptoKeyEncrypterDecrypter
   ```
2. Configure the encryption key under the `providerSpec` field in your machine set YAML file. For example:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             disks:
             - type:
               encryptionKey:
                 kmsKey:
                   name: machine-encryption-key
                   keyRing: openshift-encryption-ring
                   location: global
                   projectID: openshift-gcp-project
                 kmsKeyServiceAccount: openshift-service-account@openshift-gcp-project.iam.gserviceaccount.com
   ```

   where:

   `spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.name`
   :   Specifies the name of the customer-managed encryption key that is used for the disk encryption.

   `spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.keyRing`
   :   Specifies the name of the KMS key ring that the KMS key belongs to.

   `spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.location`
   :   Specifies the Google Cloud location in which the KMS key ring exists.

   `spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.projectID`
   :   Optional: Specifies the ID of the project in which the KMS key ring exists. If a project ID is not set, the machine set `projectID` in which the machine set was created is used.

   `spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKeyServiceAccount`
   :   Optional: Specifies the service account that is used for the encryption request for the given KMS key. If a service account is not set, the Compute Engine default service account is used.

       When a new machine is created by using the updated `providerSpec` object configuration, the disk encryption key is encrypted with the KMS key.

#### [2.4.10. Enabling GPU support for a compute machine set](#machineset-gcp-enabling-gpu-support_creating-machineset-gcp) Copy linkLink copied to clipboard!

Use the Google Cloud Compute Engine to add GPUs to Virtual Machine (VM) instances. Workloads that benefit from access to GPU resources can perform better on compute machines with this feature enabled. OpenShift Container Platform on Google Cloud supports NVIDIA GPU models in the A2 and N1 machine series.

Expand

Table 2.2. Supported GPU configurations

| Model name | GPU type | Machine types [1] |
| --- | --- | --- |
| NVIDIA A100 | `nvidia-tesla-a100` | * `a2-highgpu-1g` * `a2-highgpu-2g` * `a2-highgpu-4g` * `a2-highgpu-8g` * `a2-megagpu-16g` |
| NVIDIA K80 | `nvidia-tesla-k80` | * `n1-standard-1` * `n1-standard-2` * `n1-standard-4` * `n1-standard-8` * `n1-standard-16` * `n1-standard-32` * `n1-standard-64` * `n1-standard-96` * `n1-highmem-2` * `n1-highmem-4` * `n1-highmem-8` * `n1-highmem-16` * `n1-highmem-32` * `n1-highmem-64` * `n1-highmem-96` * `n1-highcpu-2` * `n1-highcpu-4` * `n1-highcpu-8` * `n1-highcpu-16` * `n1-highcpu-32` * `n1-highcpu-64` * `n1-highcpu-96` |
| NVIDIA P100 | `nvidia-tesla-p100` |
| NVIDIA P4 | `nvidia-tesla-p4` |
| NVIDIA T4 | `nvidia-tesla-t4` |
| NVIDIA V100 | `nvidia-tesla-v100` |

Show more

1. For more information about machine types, including specifications, compatibility, regional availability, and limitations, see the Google Cloud Compute Engine documentation about [N1 machine series](https://cloud.google.com/compute/docs/general-purpose-machines#n1_machines), [A2 machine series](https://cloud.google.com/compute/docs/accelerator-optimized-machines#a2_vms), and [GPU regions and zones availability](https://cloud.google.com/compute/docs/gpus/gpu-regions-zones#gpu_regions_and_zones).

You can define which supported GPU to use for an instance by using the Machine API.

You can configure machines in the N1 machine series to deploy with one of the supported GPU types. Machines in the A2 machine series come with associated GPUs, and cannot use guest accelerators.

Note

GPUs for graphics workloads are not supported.

**Procedure**

1. In a text editor, open the YAML file for an existing compute machine set or create a new one.
2. Specify a GPU configuration under the `providerSpec` field in your compute machine set YAML file. See the following examples of valid configurations:

   **Example configuration for the A2 machine series**

   ```
     providerSpec:
       value:
         machineType: a2-highgpu-1g
         onHostMaintenance: Terminate
         restartPolicy: Always
   ```

   where

   `spec.template.spec.providerSpec.value.machineType`
   :   Specifies the machine type. Ensure that the machine type is included in the A2 machine series.

   `spec.template.spec.providerSpec.value.onHostMaintenance`
   :   Sets `onHostMaintenance` to `Terminate`. When using GPU support, you must set `onHostMaintenance` to `Terminate`.

   `spec.template.spec.providerSpec.value.restartPolicy`
   :   Specifies the restart policy for machines deployed by the compute machine set. The allowed values are `Always` or `Never`.

   **Example configuration for the N1 machine series**

   ```
   providerSpec:
     value:
       gpus:
       - count: 1
         type: nvidia-tesla-p100
       machineType: n1-standard-1
       onHostMaintenance: Terminate
       restartPolicy: Always
   ```

   where

   `spec.template.spec.providerSpec.value.gpus.count`
   :   Specifies the number of GPUs to attach to the machine.

   `spec.template.spec.providerSpec.value.gpus.type`
   :   Specifies the type of GPUs to attach to the machine. Ensure that the machine type and GPU type are compatible.

   `spec.template.spec.providerSpec.value.machineType`
   :   Specifies the machine type. Ensure that the machine type and GPU type are compatible.

   `spec.template.spec.providerSpec.value.onHostMaintenance`
   :   Sets `onHostMaintenance` to `Terminate`. When using GPU support, you must set `onHostMaintenance` to `Terminate`.

   `spec.template.spec.providerSpec.value.restartPolicy`
   :   Specifies the restart policy for machines deployed by the compute machine set. The allowed values are `Always` or `Never`.

#### [2.4.11. Adding a GPU node to an existing OpenShift Container Platform cluster](#nvidia-gpu-gcp-adding-a-gpu-node_creating-machineset-gcp) Copy linkLink copied to clipboard!

You can copy and modify a default compute machine set configuration to create a GPU-enabled machine set and machines for the Google Cloud provider. This assists compute-intensive workloads that require hardware acceleration.

The following table lists the validated instance types:

Expand

| Instance type | NVIDIA GPU accelerator | Maximum number of GPUs | Architecture |
| --- | --- | --- | --- |
| `a2-highgpu-1g` | A100 | 1 | x86 |
| `n1-standard-4` | T4 | 1 | x86 |

Show more

**Procedure**

1. Make a copy of an existing `MachineSet` configuration.
2. In the new copy, change the machine set `name` in `metadata.name` and in both instances of `machine.openshift.io/cluster-api-machineset`.
3. Change the instance type to add the following two lines to the newly copied `MachineSet` configuration:

   ```
   machineType: a2-highgpu-1g
   onHostMaintenance: Terminate
   ```

   **Example `a2-highgpu-1g.json` file**

   ```
   {
       "apiVersion": "machine.openshift.io/v1beta1",
       "kind": "MachineSet",
       "metadata": {
           "annotations": {
               "machine.openshift.io/GPU": "0",
               "machine.openshift.io/memoryMb": "16384",
               "machine.openshift.io/vCPU": "4"
           },
           "creationTimestamp": "2023-01-13T17:11:02Z",
           "generation": 1,
           "labels": {
               "machine.openshift.io/cluster-api-cluster": "myclustername-2pt9p"
           },
           "name": "myclustername-2pt9p-worker-gpu-a",
           "namespace": "openshift-machine-api",
           "resourceVersion": "20185",
           "uid": "2daf4712-733e-4399-b4b4-d43cb1ed32bd"
       },
       "spec": {
           "replicas": 1,
           "selector": {
               "matchLabels": {
                   "machine.openshift.io/cluster-api-cluster": "myclustername-2pt9p",
                   "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-gpu-a"
               }
           },
           "template": {
               "metadata": {
                   "labels": {
                       "machine.openshift.io/cluster-api-cluster": "myclustername-2pt9p",
                       "machine.openshift.io/cluster-api-machine-role": "worker",
                       "machine.openshift.io/cluster-api-machine-type": "worker",
                       "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-gpu-a"
                   }
               },
               "spec": {
                   "lifecycleHooks": {},
                   "metadata": {},
                   "providerSpec": {
                       "value": {
                           "apiVersion": "machine.openshift.io/v1beta1",
                           "canIPForward": false,
                           "credentialsSecret": {
                               "name": "gcp-cloud-credentials"
                           },
                           "deletionProtection": false,
                           "disks": [
                               {
                                   "autoDelete": true,
                                   "boot": true,
                                   "image": "projects/rhcos-cloud/global/images/rhcos-412-86-202212081411-0-gcp-x86-64",
                                   "labels": null,
                                   "sizeGb": 128,
                                   "type": "pd-ssd"
                               }
                           ],
                           "kind": "GCPMachineProviderSpec",
                           "machineType": "a2-highgpu-1g",
                           "onHostMaintenance": "Terminate",
                           "metadata": {
                               "creationTimestamp": null
                           },
                           "networkInterfaces": [
                               {
                                   "network": "myclustername-2pt9p-network",
                                   "subnetwork": "myclustername-2pt9p-worker-subnet"
                               }
                           ],
                           "preemptible": true,
                           "projectID": "myteam",
                           "region": "us-central1",
                           "serviceAccounts": [
                               {
                                   "email": "myclustername-2pt9p-w@myteam.iam.gserviceaccount.com",
                                   "scopes": [
                                       "https://www.googleapis.com/auth/cloud-platform"
                                   ]
                               }
                           ],
                           "tags": [
                               "myclustername-2pt9p-worker"
                           ],
                           "userDataSecret": {
                               "name": "worker-user-data"
                           },
                           "zone": "us-central1-a"
                       }
                   }
               }
           }
       },
       "status": {
           "availableReplicas": 1,
           "fullyLabeledReplicas": 1,
           "observedGeneration": 1,
           "readyReplicas": 1,
           "replicas": 1
       }
   }
   ```
4. View the existing nodes, machines, and machine sets by running the following command. Note that each node is an instance of a machine definition with a specific Google Cloud region and OpenShift Container Platform role.

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                                                             STATUS     ROLES                  AGE     VERSION
   myclustername-2pt9p-master-0.c.openshift-qe.internal             Ready      control-plane,master   8h      v1.35.4
   myclustername-2pt9p-master-1.c.openshift-qe.internal             Ready      control-plane,master   8h      v1.35.4
   myclustername-2pt9p-master-2.c.openshift-qe.internal             Ready      control-plane,master   8h      v1.35.4
   myclustername-2pt9p-worker-a-mxtnz.c.openshift-qe.internal       Ready      worker                 8h      v1.35.4
   myclustername-2pt9p-worker-b-9pzzn.c.openshift-qe.internal       Ready      worker                 8h      v1.35.4
   myclustername-2pt9p-worker-c-6pbg6.c.openshift-qe.internal       Ready      worker                 8h      v1.35.4
   myclustername-2pt9p-worker-gpu-a-wxcr6.c.openshift-qe.internal   Ready      worker                 4h35m   v1.35.4
   ```
5. View the machines and machine sets that exist in the `openshift-machine-api` namespace by running the following command. Each compute machine set is associated with a different availability zone within the Google Cloud region. The installation program automatically load balances compute machines across availability zones.

   ```
   $ oc get machinesets -n openshift-machine-api
   ```

   **Example output**

   ```
   NAME                               DESIRED   CURRENT   READY   AVAILABLE   AGE
   myclustername-2pt9p-worker-a       1         1         1       1           8h
   myclustername-2pt9p-worker-b       1         1         1       1           8h
   myclustername-2pt9p-worker-c       1         1                             8h
   myclustername-2pt9p-worker-f       0         0                             8h
   ```
6. View the machines that exist in the `openshift-machine-api` namespace by running the following command. You can only configure one compute machine per set, although you can scale a compute machine set to add a node in a particular region and zone.

   ```
   $ oc get machines -n openshift-machine-api | grep worker
   ```

   **Example output**

   ```
   myclustername-2pt9p-worker-a-mxtnz       Running   n2-standard-4   us-central1   us-central1-a   8h
   myclustername-2pt9p-worker-b-9pzzn       Running   n2-standard-4   us-central1   us-central1-b   8h
   myclustername-2pt9p-worker-c-6pbg6       Running   n2-standard-4   us-central1   us-central1-c   8h
   ```
7. Make a copy of one of the existing compute `MachineSet` definitions and output the result to a JSON file by running the following command. This will be the basis for the GPU-enabled compute machine set definition.

   ```
   $ oc get machineset myclustername-2pt9p-worker-a -n openshift-machine-api -o json  > <output_file.json>
   ```
8. Edit the JSON file to make the following changes to the new `MachineSet` definition:

   * Rename the machine set `name` by inserting the substring `gpu` in `metadata.name` and in both instances of `machine.openshift.io/cluster-api-machineset`.
   * Change the `machineType` of the new `MachineSet` definition to `a2-highgpu-1g`, which includes an NVIDIA A100 GPU.

     ```
     jq .spec.template.spec.providerSpec.value.machineType ocp_4.22_machineset-a2-highgpu-1g.json

     "a2-highgpu-1g"
     ```

     The `<output_file.json>` file is saved as `ocp_4.22_machineset-a2-highgpu-1g.json`.
9. Update the following fields in `ocp_4.22_machineset-a2-highgpu-1g.json`:

   * Change `.metadata.name` to a name containing `gpu`.
   * Change `.spec.selector.matchLabels["machine.openshift.io/cluster-api-machineset"]` to match the new `.metadata.name`.
   * Change `.spec.template.metadata.labels["machine.openshift.io/cluster-api-machineset"]` to match the new `.metadata.name`.
   * Change `.spec.template.spec.providerSpec.value.MachineType` to `a2-highgpu-1g`.
   * Add the following line under `machineType`: `"onHostMaintenance": "Terminate". For example:

     ```
     "machineType": "a2-highgpu-1g",
     "onHostMaintenance": "Terminate",
     ```
10. To verify your changes, perform a `diff` of the original compute definition and the new GPU-enabled node definition by running the following command:

    ```
    $ oc get machineset/myclustername-2pt9p-worker-a -n openshift-machine-api -o json | diff ocp_4.22_machineset-a2-highgpu-1g.json -
    ```

    **Example output**

    ```
    15c15
    <         "name": "myclustername-2pt9p-worker-gpu-a",
    ---
    >         "name": "myclustername-2pt9p-worker-a",
    25c25
    <                 "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-gpu-a"
    ---
    >                 "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-a"
    34c34
    <                     "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-gpu-a"
    ---
    >                     "machine.openshift.io/cluster-api-machineset": "myclustername-2pt9p-worker-a"
    59,60c59
    <                         "machineType": "a2-highgpu-1g",
    <                         "onHostMaintenance": "Terminate",
    ---
    >                         "machineType": "n2-standard-4",
    ```
11. Create the GPU-enabled compute machine set from the definition file by running the following command:

    ```
    $ oc create -f ocp_4.22_machineset-a2-highgpu-1g.json
    ```

    **Example output**

    ```
    machineset.machine.openshift.io/myclustername-2pt9p-worker-gpu-a created
    ```

**Verification**

1. View the machine set you created by running the following command:

   ```
   $ oc -n openshift-machine-api get machinesets | grep gpu
   ```

   The `MachineSet` replica count is set to `1` so a new `Machine` object is created automatically.

   **Example output**

   ```
   myclustername-2pt9p-worker-gpu-a   1         1         1       1           5h24m
   ```
2. View the `Machine` object that the machine set created by running the following command:

   ```
   $ oc -n openshift-machine-api get machines | grep gpu
   ```

   **Example output**

   ```
   myclustername-2pt9p-worker-gpu-a-wxcr6   Running   a2-highgpu-1g   us-central1   us-central1-a   5h25m
   ```

Note

Note that there is no need to specify a namespace for the node. The node definition is cluster scoped.

#### [2.4.12. Deploying the Node Feature Discovery Operator](#nvidia-gpu-aws-deploying-the-node-feature-discovery-operator_creating-machineset-gcp) Copy linkLink copied to clipboard!

After the GPU-enabled node is created, you need to discover the GPU-enabled node so it can be scheduled. To do this, install the Node Feature Discovery (NFD) Operator.

The NFD Operator identifies hardware device features in nodes. It solves the general problem of identifying and cataloging hardware resources in the infrastructure nodes so they can be made available to OpenShift Container Platform.

**Procedure**

1. Install the Node Feature Discovery Operator from the software catalog in the OpenShift Container Platform console.
2. After installing the NFD Operator, select **Node Feature Discovery** from the installed Operators list and select **Create instance**. This installs the `nfd-master` and `nfd-worker` pods, one `nfd-worker` pod for each compute node, in the `openshift-nfd` namespace.
3. Verify that the Operator is installed and running by running the following command:

   ```
   $ oc get pods -n openshift-nfd
   ```

   **Example output**

   ```
   NAME                                       READY    STATUS     RESTARTS   AGE

   nfd-controller-manager-8646fcbb65-x5qgk    2/2      Running 7  (8h ago)   1d
   ```
4. Browse to the installed Operator in the console and select **Create Node Feature Discovery**.
5. Select **Create** to build a NFD custom resource. This creates NFD pods in the `openshift-nfd` namespace that poll the OpenShift Container Platform nodes for hardware resources and catalog them.

**Verification**

1. After a successful build, verify that a NFD pod is running on each nodes by running the following command:

   ```
   $ oc get pods -n openshift-nfd
   ```

   **Example output**

   ```
   NAME                                       READY   STATUS      RESTARTS        AGE
   nfd-controller-manager-8646fcbb65-x5qgk    2/2     Running     7 (8h ago)      12d
   nfd-master-769656c4cb-w9vrv                1/1     Running     0               12d
   nfd-worker-qjxb2                           1/1     Running     3 (3d14h ago)   12d
   nfd-worker-xtz9b                           1/1     Running     5 (3d14h ago)   12d
   ```

   The NFD Operator uses vendor PCI IDs to identify hardware in a node. NVIDIA uses the PCI ID `10de`.
2. View the NVIDIA GPU discovered by the NFD Operator by running the following command:

   ```
   $ oc describe node ip-10-0-132-138.us-east-2.compute.internal | egrep 'Roles|pci'
   ```

   **Example output**

   ```
   Roles: worker

   feature.node.kubernetes.io/pci-1013.present=true

   feature.node.kubernetes.io/pci-10de.present=true

   feature.node.kubernetes.io/pci-1d0f.present=true
   ```

   `10de` appears in the node feature list for the GPU-enabled node. This mean the NFD Operator correctly identified the node from the GPU-enabled MachineSet.

### [2.5. Creating a compute machine set on IBM Cloud](#creating-machineset-ibm-cloud) Copy linkLink copied to clipboard!

You can create compute machine sets in your OpenShift Container Platform cluster on IBM Cloud® to perform specific tasks. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines. Moving supporting workloads to dedicated machines helps ensure that your cluster resources are allocated efficiently.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

#### [2.5.1. Sample YAML for a compute machine set custom resource on IBM Cloud](#machineset-yaml-ibm-cloud_creating-machineset-ibm-cloud) Copy linkLink copied to clipboard!

You can use the sample YAML file to automate the provisioning of compute or infrastructure nodes within a specific Virtual Private Cloud (VPC). The sample YAML defines a compute machine set that runs in a specified IBM Cloud® zone in a region and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <role>
    machine.openshift.io/cluster-api-machine-type: <role>
  name: <infrastructure_id>-<role>-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/<role>: ""
      providerSpec:
        value:
          apiVersion: ibmcloudproviderconfig.openshift.io/v1beta1
          credentialsSecret:
            name: ibmcloud-credentials
          image: <infrastructure_id>-rhcos
          kind: IBMCloudMachineProviderSpec
          primaryNetworkInterface:
              securityGroups:
              - <infrastructure_id>-sg-cluster-wide
              - <infrastructure_id>-sg-openshift-net
              subnet: <infrastructure_id>-subnet-compute-<zone>
          profile: <instance_profile>
          region: <region>
          resourceGroup: <resource_group>
          userDataSecret:
              name: <role>-user-data
          vpc: <vpc_name>
          zone: <zone>
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`<role>`
:   Specifies the node label to add.

`<infrastructure_id>-<role>-<region>`
:   Specifies the infrastructure ID, node label, and region.

`<infrastructure_id>-rhcos`
:   Specifies the custom Red Hat Enterprise Linux CoreOS (RHCOS) image to use as a boot image for your nodes. You should use the use the latest image when adding a new machine set.

`<infrastructure_id>-subnet-compute-<zone>`
:   Specifies the infrastructure ID and zone within your region to place machines on. Be sure that your region supports the zone that you specify.

`<instance_profile>`
:   Specifies the [IBM Cloud® instance profile](https://cloud.ibm.com/docs/vpc?topic=vpc-profiles&interface=ui).

`<region>`
:   Specifies the region to place machines on.

`<resource_group>`
:   Specifies the resource group that machine resources are placed in. This is either an existing resource group specified at installation time, or an installer-created resource group named based on the infrastructure ID.

`<vpc_name>`
:   Specifies the VPC name.

`<zone>`
:   Specifies the zone within your region to place machines on. Be sure that your region supports the zone that you specify.

#### [2.5.2. Creating a compute machine set](#machineset-creating_creating-machineset-ibm-cloud) Copy linkLink copied to clipboard!

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

#### [2.5.3. Labeling GPU machine sets for the cluster autoscaler](#machineset-label-gpu-autoscaler_creating-machineset-ibm-cloud) Copy linkLink copied to clipboard!

Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

**Prerequisites**

* Your cluster uses a cluster autoscaler.

**Procedure**

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    name: machine-set-name
  spec:
    template:
      spec:
        metadata:
          labels:
            cluster-api/accelerator: <accelerator_name>
  ```

  where:

  `<accelerator_name>`
  :   Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.

      Note

      You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR. For more information, see "Cluster autoscaler resource definition".

### [2.6. Creating a compute machine set on IBM Power Virtual Server](#creating-machineset-ibm-power-vs) Copy linkLink copied to clipboard!

Create compute machine sets in your OpenShift Container Platform cluster on IBM Power® Virtual Server to perform specific tasks. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines. Moving supporting workloads to dedicated machines helps ensure that your cluster resources are allocated efficiently.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

#### [2.6.1. Sample YAML for a compute machine set custom resource on IBM Power Virtual Server](#machineset-yaml-ibm-power-vs_creating-machineset-ibm-power-vs) Copy linkLink copied to clipboard!

You can use the sample YAML file to help automate provisioning and to ensure scaling and scheduling work, as required. The sample YAML file defines a compute machine set that runs in a specified IBM Power® Virtual Server zone in a region and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <role>
    machine.openshift.io/cluster-api-machine-type: <role>
  name: <infrastructure_id>-<role>-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<region>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/<role>: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1
          credentialsSecret:
            name: powervs-credentials
          image:
            name: rhcos-<infrastructure_id>
            type: Name
          keyPairName: <infrastructure_id>-key
          kind: PowerVSMachineProviderConfig
          memoryGiB: 32
          network:
            regex: ^DHCPSERVER[0-9a-z]{32}_Private$
            type: RegEx
          processorType: Shared
          processors: "0.5"
          serviceInstance:
            id: <ibm_power_vs_service_instance_id>
            type: ID
          systemType: s922
          userDataSecret:
            name: <role>-user-data
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`<role>`
:   Specifies the node label to add.

`<infrastructure_id>-<role>-<region>`
:   Specifies the infrastructure ID, node label, and region.

`rhcos-<infrastructure_id>`
:   Specifies the custom Red Hat Enterprise Linux CoreOS (RHCOS) image to use as a boot image for your nodes. You should use the use the latest image when adding a new machine set.

`<ibm_power_vs_service_instance_id>`
:   Specifies the infrastructure ID within your region to place machines on.

#### [2.6.2. Creating a compute machine set](#machineset-creating_creating-machineset-ibm-power-vs) Copy linkLink copied to clipboard!

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

### [2.7. Creating a compute machine set on Nutanix](#creating-machineset-nutanix) Copy linkLink copied to clipboard!

You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on Nutanix. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines, which helps ensure efficient resource allocation.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

#### [2.7.1. Sample YAML for a compute machine set custom resource on Nutanix](#machineset-yaml-nutanix_creating-machineset-nutanix) Copy linkLink copied to clipboard!

You can use a YAML file to automate node provisioning and ensure workloads are scheduled correctly based on role and infrastructure requirements.

The sample YAML shows how to define a Nutanix compute MachineSet for your cluster. It explains how to configure roles, labels, sizing, networking, and boot settings so new nodes are created consistently.

The sample YAML defines a Nutanix compute machine set that creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

##### [2.7.1.1. Values obtained by using the OpenShift CLI](#machineset-yaml-nutanix-oc_creating-machineset-nutanix) Copy linkLink copied to clipboard!

In the following example, you can obtain some of the values for your cluster by using the OpenShift CLI (`oc`).

Infrastructure ID
:   The `<infrastructure_id>` string is the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

    ```
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineSet
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
      name: <infrastructure_id>-<role>-<zone>
      namespace: openshift-machine-api
      annotations:
        machine.openshift.io/memoryMb: "16384"
        machine.openshift.io/vCPU: "4"
    spec:
      replicas: 3
      selector:
        matchLabels:
          machine.openshift.io/cluster-api-cluster: <infrastructure_id>
          machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<zone>
      template:
        metadata:
          labels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
            machine.openshift.io/cluster-api-machine-role: <role>
            machine.openshift.io/cluster-api-machine-type: <role>
            machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>-<zone>
        spec:
          metadata:
            labels:
              node-role.kubernetes.io/<role>: ""
          providerSpec:
            value:
              apiVersion: machine.openshift.io/v1
              bootType: ""
              categories:
              - key: <category_name>
                value: <category_value>
              cluster:
                type: uuid
                uuid: <cluster_uuid>
              credentialsSecret:
                name: nutanix-credentials
              image:
                name: <infrastructure_id>-rhcos
                type: name
              kind: NutanixMachineProviderConfig
              memorySize: 16Gi
              project:
                type: name
                name: <project_name>
              subnets:
              - type: uuid
                uuid: <subnet_uuid>
              systemDiskSize: 120Gi
              userDataSecret:
                name: <user_data_secret>
              vcpuSockets: 4
              vcpusPerSocket: 1
    ```

    where:

    `<infrastructure_id>`
    :   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster.

    `<role>`
    :   Specifies the node label to add.

    `<infrastructure_id>-<infra>-<region>`
    :   Specifies the infrastructure ID, node label, and zone.

    `annotations`
    :   Specifies annotations for the cluster autoscaler.

    `bootType`
    :   Specifies the boot type that the compute machines use. For more information about boot types, see [Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment](https://portal.nutanix.com/page/documents/kbs/details?targetId=kA07V000000H3K9SAK). Valid values are `Legacy`, `SecureBoot`, or `UEFI`. The default is `Legacy`.

        Note

        You must use the `Legacy` boot type in OpenShift Container Platform 4.22.

    `<categories>`
    :   Specifies one or more Nutanix Prism categories to apply to compute machines. This stanza requires `key` and `value` parameters for a category key-value pair that exists in Prism Central. For more information about categories, see [Category management](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html).

    `<cluster>`
    :   Specifies a Nutanix Prism Element cluster configuration. In this example, the cluster type is `uuid`, so there is a `uuid` stanza.

    `<infrastructure_id>-rhcos`
    :   Specifies the image to use as a boot image for your nodes. You should use the use the latest image when adding a new machine set.

    `16Gi`
    :   Specifies the amount of memory for the cluster in Gi.

    `project`
    :   Specifies the Nutanix project that you use for your cluster. In this example, the project type is `name`, so there is a `name` stanza.

    `subnets`
    :   Specifies one or more UUID for the Prism Element subnet object. The CIDR IP address prefix for one of the specified subnets must contain the virtual IP addresses that the OpenShift Container Platform cluster uses. A maximum of 32 subnets for each Prism Element failure domain in the cluster is supported. All subnet UUID values must be unique.

    `120Gi`
    :   Specifies the size of the system disk in Gi.

    `<user_data_secret>`
    :   Specifies the name of the secret in the user data YAML file that is in the `openshift-machine-api` namespace. Use the value that installation program populates in the default compute machine set.

    `4`
    :   Specifies the number of vCPU sockets.

    `1`
    :   Specifies the number of vCPUs per socket.

#### [2.7.2. Creating a compute machine set](#machineset-creating_creating-machineset-nutanix) Copy linkLink copied to clipboard!

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

#### [2.7.3. Labeling GPU machine sets for the cluster autoscaler](#machineset-label-gpu-autoscaler_creating-machineset-nutanix) Copy linkLink copied to clipboard!

Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

**Prerequisites**

* Your cluster uses a cluster autoscaler.

**Procedure**

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    name: machine-set-name
  spec:
    template:
      spec:
        metadata:
          labels:
            cluster-api/accelerator: <accelerator_name>
  ```

  where:

  `<accelerator_name>`
  :   Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.

      Note

      You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR. For more information, see "Cluster autoscaler resource definition".

#### [2.7.4. Failure domains for Nutanix clusters](#mapi-failure-domain-nutanix_creating-machineset-nutanix) Copy linkLink copied to clipboard!

To modify failure domain configurations on a Nutanix cluster, you must modify the cluster infrastructure, control plane machine set, and compute machine set custom resources (CRs) to apply the new configuration.

To add or update the failure domain configuration on a Nutanix cluster, you must make coordinated changes to several resources. The following actions are required:

1. Modify the cluster infrastructure custom resource (CR).
2. Modify the cluster control plane machine set CR.
3. Modify or replace the compute machine set CRs.

For more information, see "Adding failure domains to an existing Nutanix cluster".

#### [2.7.5. Improving reliability for multiple subnet configurations on Nutanix](#cpmso-ts-nutanix-multiple-subnet_creating-machineset-nutanix) Copy linkLink copied to clipboard!

To improve reliability and avoid common networking problems with multiple subnet configurations on Nutanix, adhere to the configuration practices that minimize networking conflicts.

The following networking configuration and management practices can help your multiple subnet configuration perform more reliably:

* To avoid overlapping IP address assignments, use predefined static IP addresses in the `cloud-init` metadata.
* Tag all VMs, disks, and networks with a unique cluster ID.
* Avoid IP address conflicts by using dedicated subnets for each OpenShift Container Platform cluster:

  Nutanix uses Nutanix Acropolis Hypervisor (AHV) and Nutanix Prism networking to assign IP addresses to virtual machines (VMs). If a single subnet provides IP addresses for more than one OpenShift Container Platform cluster, AHV or Prism might assign the same IP address to a VM or pod in more than one cluster.

  To avoid this issue, use dedicated subnets for each OpenShift Container Platform cluster, even when you have more than one cluster on a single Prism Central instance. You can use the Prism UI or automation tools, such as Terraform or Ansible, to create separate IP address pools for each OpenShift Container Platform cluster.
* Ensure that each OpenShift Container Platform cluster uses distinct DNS zones and virtual IP address ranges.
* Avoid DHCP conflicts by maintaining DHCP allocations:

  If you use Nutanix to manage DHCP allocation, objects in your cluster might have duplicate leases. Duplicate leases can cause DHCP conflicts when you apply changes to the control plane machine set custom resource (CR) specification.

  To avoid this issue, regularly remove stale DHCP leases.
* Use automation tools, such as Terraform or Ansible, to isolate the infrastructure for each OpenShift Container Platform cluster.

### [2.8. Creating a compute machine set on OpenStack](#creating-machineset-osp) Copy linkLink copied to clipboard!

To automate the provisioning and scaling of node virtual machines (VMs) on Red Hat OpenStack Platform (RHOSP) for compute workloads, create a `MachineSet` YAML file that defines details, for example image and network, that are specific to RHOSP.

You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on RHOSP. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

#### [2.8.1. Sample YAML for a compute machine set custom resource on RHOSP](#machineset-yaml-osp_creating-machineset-osp) Copy linkLink copied to clipboard!

To enable the Machine API to automate the scaling and management of compute nodes, define a `MachineSet` resource with Red Hat OpenStack Platform (RHOSP) parameters, for example, image and network IDs.

The sample YAML defines a compute machine set that runs on Red Hat OpenStack Platform (RHOSP) and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <role>
    machine.openshift.io/cluster-api-machine-type: <role>
  name: <infrastructure_id>-<role>
  namespace: openshift-machine-api
spec:
  replicas: <number_of_replicas>
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
        value:
          apiVersion: machine.openshift.io/v1alpha1
          cloudName: openstack
          cloudsSecret:
            name: openstack-cloud-credentials
            namespace: openshift-machine-api
          flavor: <nova_flavor>
          image: <glance_image_name_or_location>
          serverGroupID: <optional_UUID_of_server_group>
          kind: OpenstackProviderSpec
          networks:
          - filter: {}
            subnets:
            - filter:
                name: <subnet_name>
                tags: openshiftClusterID=<infrastructure_id>
          primarySubnet: <rhosp_subnet_UUID>
          securityGroups:
          - filter: {}
            name: <infrastructure_id>-worker
          serverMetadata:
            Name: <infrastructure_id>-worker
            openshiftClusterID: <infrastructure_id>
          tags:
          - openshiftClusterID=<infrastructure_id>
          trunk: true
          userDataSecret:
            name: worker-user-data
          availabilityZone: <optional_openstack_availability_zone>
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift Container Platform CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`<role>`
:   Specifies the node label to add.

`<infrastructure_id>-<role>`
:   Specifies the infrastructure ID and node label.

`<glance_image_name_or_location>`
:   Specifies the image to use as a boot image for your nodes. You should use the latest image when adding a new machine set.

`<optional_UUID_of_server_group>`
:   Sets a server group policy for the `MachineSet` YAML by entering the value that is returned from [creating a server group](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.0/html/command_line_interface_reference/server#server_group_create). For most deployments, `anti-affinity` or `soft-anti-affinity` policies are recommended.

`<subnet_name>`
:   Specifies a subnet to use.

    Note

    The `spec.template.spec.providerSpec.value.networks` stanza is required for deployments to multiple networks. If deploying to multiple networks, this list must include the network that is used as the `primarySubnet` value.

`<rhosp_subnet_UUID>`
:   Specifies the RHOSP subnet that you want the endpoints of nodes to be published on. Usually, this is the same subnet that is used as the value of `machinesSubnet` in the `install-config.yaml` file.

#### [2.8.2. Sample YAML for a compute machine set custom resource that uses SR-IOV on RHOSP](#machineset-yaml-osp-sr-iov_creating-machineset-osp) Copy linkLink copied to clipboard!

To provision compute virtual machines (VMs) with single root I/O virtualization (SR-IOV) for high-performance networking, define the SR-IOV ports directly in the `providerSpec` and set `portSecurity` to `False`.

If you configured your cluster for single-root SR-IOV, you can create compute machine sets that use that technology.

This sample YAML defines a compute machine set that uses SR-IOV networks. The nodes that it creates are labeled with `node-role.openshift.io/<node_role>: ""`

In this sample, `infrastructure_id` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `node_role` is the node label to add.

The sample assumes two SR-IOV networks that are named "radio" and "uplink". The networks are used in port definitions in the `spec.template.spec.providerSpec.value.ports` list.

Note

Only parameters that are specific to SR-IOV deployments are described in this sample. To review a more general sample, see "Sample YAML for a compute machine set custom resource on RHOSP".

**An example compute machine set that uses SR-IOV networks**

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <node_role>
    machine.openshift.io/cluster-api-machine-type: <node_role>
  name: <infrastructure_id>-<node_role>
  namespace: openshift-machine-api
spec:
  replicas: <number_of_replicas>
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<node_role>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <node_role>
        machine.openshift.io/cluster-api-machine-type: <node_role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<node_role>
    spec:
      metadata:
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1alpha1
          cloudName: openstack
          cloudsSecret:
            name: openstack-cloud-credentials
            namespace: openshift-machine-api
          flavor: <nova_flavor>
          image: <glance_image_name_or_location>
          serverGroupID: <optional_UUID_of_server_group>
          kind: OpenstackProviderSpec
          networks:
            - subnets:
              - UUID: <machines_subnet_UUID>
          ports:
            - networkID: <radio_network_UUID>
              nameSuffix: radio
              fixedIPs:
                - subnetID: <radio_subnet_UUID>
              tags:
                - sriov
                - radio
              vnicType: direct
              portSecurity: false
            - networkID: <uplink_network_UUID>
              nameSuffix: uplink
              fixedIPs:
                - subnetID: <uplink_subnet_UUID>
              tags:
                - sriov
                - uplink
              vnicType: direct
              portSecurity: false
          primarySubnet: <machines_subnet_UUID>
          securityGroups:
          - filter: {}
            name: <infrastructure_id>-<node_role>
          serverMetadata:
            Name: <infrastructure_id>-<node_role>
            openshiftClusterID: <infrastructure_id>
          tags:
          - openshiftClusterID=<infrastructure_id>
          trunk: true
          userDataSecret:
            name: <node_role>-user-data
          availabilityZone: <optional_openstack_availability_zone>
          configDrive: true
```

where:

`<glance_image_name_or_location>`
:   Specifies the image to use as a boot image for your nodes. You should use the latest image when adding a new machine set.

`<radio_network_UUID>`
:   Specifies a network UUID for each port.

`<radio_subnet_UUID>`
:   Specifies a subnet UUID for each port.

Note

The value of the `spec.template.spec.providerSpec.value.ports.vnicType` parameter must be `direct` for each port.

The value of the `spec.template.spec.providerSpec.value.ports.portSecurity` parameter must be `false` for each port. You cannot set security groups and allowed address pairs for ports when port security is disabled. Setting security groups on the instance applies the groups to all ports that are attached to it.

`<uplink_network_UUID>`
:   Specifies a network UUID for each port.

`<uplink_subnet_UUID>`
:   Specifies a subnet UUID for each port.

Note

The value of the `spec.template.spec.providerSpec.value.configDrive` parameter must be `true`.

Important

After you deploy compute machines that are SR-IOV-capable, you must label them as such. For example, from a command line, enter:

```
$ oc label node <NODE_NAME> feature.node.kubernetes.io/network-sriov.capable="true"
```

Note

Trunking is enabled for ports that are created by entries in the networks and subnets lists. The names of ports that are created from these lists follow the pattern `<machine_name>-<nameSuffix>`. The `nameSuffix` field is required in port definitions.

You can enable trunking for each port.

Optionally, you can add tags to ports as part of their `tags` lists.

#### [2.8.3. Sample YAML for SR-IOV deployments where port security is disabled](#machineset-yaml-osp-sr-iov-port-security_creating-machineset-osp) Copy linkLink copied to clipboard!

To create single-root I/O virtualization (SR-IOV) ports on a network that has port security disabled, define a compute machine set that includes the ports as items in the `spec.template.spec.providerSpec.value.ports` list.

This difference from the standard SR-IOV compute machine set is due to the automatic security group and allowed address pair configuration that occurs for ports that are created by using the network and subnet interfaces.

Ports that you define for machines subnets require:

* Allowed address pairs for the API and ingress virtual IP ports
* The compute security group
* Attachment to the machines network and subnet

Note

Only parameters that are specific to SR-IOV deployments where port security is disabled are described in this sample. To review a more general sample, see "Sample YAML for a compute machine set custom resource that uses SR-IOV on RHOSP".

**An example compute machine set that uses SR-IOV networks and has port security disabled**

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <node_role>
    machine.openshift.io/cluster-api-machine-type: <node_role>
  name: <infrastructure_id>-<node_role>
  namespace: openshift-machine-api
spec:
  replicas: <number_of_replicas>
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<node_role>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <node_role>
        machine.openshift.io/cluster-api-machine-type: <node_role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<node_role>
    spec:
      metadata: {}
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1alpha1
          cloudName: openstack
          cloudsSecret:
            name: openstack-cloud-credentials
            namespace: openshift-machine-api
          flavor: <nova_flavor>
          image: <glance_image_name_or_location>
          kind: OpenstackProviderSpec
          ports:
            - allowedAddressPairs:
              - ipAddress: <API_VIP_port_IP>
              - ipAddress: <ingress_VIP_port_IP>
              fixedIPs:
                - subnetID: <machines_subnet_UUID>
              nameSuffix: nodes
              networkID: <machines_network_UUID>
              securityGroups:
                  - <compute_security_group_UUID>
            - networkID: <SRIOV_network_UUID>
              nameSuffix: sriov
              fixedIPs:
                - subnetID: <SRIOV_subnet_UUID>
              tags:
                - sriov
              vnicType: direct
              portSecurity: False
          primarySubnet: <machines_subnet_UUID>
          serverMetadata:
            Name: <infrastructure_ID>-<node_role>
            openshiftClusterID: <infrastructure_id>
          tags:
          - openshiftClusterID=<infrastructure_id>
          trunk: false
          userDataSecret:
            name: worker-user-data
          configDrive: true
```

where:

`<API_VIP_port_IP>`
:   Specifies the allowed address for the API port. This value is paired with the allowed address for the ingress port.

`<ingress_VIP_port_IP>`
:   Specifies the allowed address for the ingress port. This value is paired with the allowed address for the API port.

`<machines_subnet_UUID>`
:   Specifies the machines subnet.

`<machines_network_UUID>`
:   Specifies the machines network.

`<compute_security_group_UUID>`
:   Specifies the compute machines security group.

Note

The value of the `spec.template.spec.providerSpec.value.configDrive` parameter must be `true`.

Trunking is enabled for ports that are created by entries in the networks and subnets lists. The names of ports that are created from these lists follow the pattern `<machine_name>-<nameSuffix>`. The `nameSuffix` field is required in port definitions.

You can enable trunking for each port.

Optionally, you can add tags to ports as part of their `tags` lists.

#### [2.8.4. Creating a compute machine set](#machineset-creating_creating-machineset-osp) Copy linkLink copied to clipboard!

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

#### [2.8.5. Labeling GPU machine sets for the cluster autoscaler](#machineset-label-gpu-autoscaler_creating-machineset-osp) Copy linkLink copied to clipboard!

Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

**Prerequisites**

* Your cluster uses a cluster autoscaler.

**Procedure**

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    name: machine-set-name
  spec:
    template:
      spec:
        metadata:
          labels:
            cluster-api/accelerator: <accelerator_name>
  ```

  where:

  `<accelerator_name>`
  :   Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.

      Note

      You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR. For more information, see "Cluster autoscaler resource definition".

### [2.9. Creating a compute machine set on vSphere](#creating-machineset-vsphere) Copy linkLink copied to clipboard!

You can define and create a OpenShift Container Platform compute machine set on VMware vSphere to enable the Machine API to automatically scale and manage compute nodes in vSphere. You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on vSphere. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

#### [2.9.1. Sample YAML for a compute machine set custom resource on vSphere](#machineset-yaml-vsphere_creating-machineset-vsphere) Copy linkLink copied to clipboard!

To enable the Machine API to automate node provisioning on VMware vSphere infrastructure, define a `MachineSet` resource with parameters that are specific to vSphere, for example data center, resource pool, and template.

The sample YAML file defines a compute machine set that runs on vSphere and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`.

In this sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  creationTimestamp: null
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
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
    spec:
      metadata:
        creationTimestamp: null
        labels:
          node-role.kubernetes.io/<role>: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: vsphere-cloud-credentials
          dataDisks:
          - name: "<disk_name>"
            provisioningMode: "<mode>"
            sizeGiB: 20
          diskGiB: 120
          kind: VSphereMachineProviderSpec
          memoryMiB: 8192
          metadata:
            creationTimestamp: null
          network:
            devices:
            - networkName: "<vm_network_name>"
          numCPUs: 4
          numCoresPerSocket: 1
          snapshot: ""
          template: <vm_template_name>
          userDataSecret:
            name: worker-user-data
          workspace:
            datacenter: <vcenter_data_center_name>
            datastore: <vcenter_datastore_name>
            folder: <vcenter_vm_folder_path>
            resourcepool: <vsphere_resource_pool>
            server: <vcenter_server_ip>
```

where

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

```
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```

`<infrastructure_id>-<role>`
:   Specifies the infrastructure ID and node label.

`<role>`
:   Specifies the node label to add.

`<disk_name>`
:   Specifies one or more data disk definitions. For more information, see "Configuring data disks by using machine sets".

`<image_name>`
:   Specifies the image to use as a boot image for your nodes.

`<vm_network_name>`
:   Specifies the vSphere VM network to deploy the compute machine set to. This VM network must be where other compute machines reside in the cluster.

`<vm_template_name>`
:   Specifies the vSphere VM template to use as a boot image for your nodes, such as `user-5ddjd-rhcos`. You should use a template with the latest OpenShift Container Platform image when adding a new machine set.

`<vcenter_data_center_name>`
:   Specifies the vCenter datacenter to deploy the compute machine set on.

`<vcenter_datastore_name>`
:   Specifies the vCenter datastore to deploy the compute machine set on.

`<vcenter_vm_folder_path>`
:   Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`.

`<vsphere_resource_pool>`
:   Specifies the vSphere resource pool for your VMs.

`<vcenter_server_ip>`
:   Specifies the vCenter server IP or fully qualified domain name.

#### [2.9.2. Minimum required vCenter privileges for compute machine set management](#machineset-vsphere-requirements-user-provisioned-machine-sets_creating-machineset-vsphere) Copy linkLink copied to clipboard!

To manage compute machine sets in an OpenShift Container Platform cluster on vCenter, you must use an account with privileges to read, create, and delete the required resources. Using an account that has global administrative privileges is the simplest way to access all of the necessary permissions.

If you cannot use an account with global administrative privileges, you must create roles to grant the minimum required privileges. The following table lists the minimum vCenter roles and privileges that are required to create, scale, and delete compute machine sets and to delete machines in your OpenShift Container Platform cluster.

Expand

Table 2.3. Minimum vCenter roles and privileges required for compute machine set management

| vSphere object for role | When required | Required privileges |
| --- | --- | --- |
| vSphere vCenter | Always | `InventoryService.Tagging.AttachTag``InventoryService.Tagging.CreateCategory``InventoryService.Tagging.CreateTag``InventoryService.Tagging.DeleteCategory``InventoryService.Tagging.DeleteTag``InventoryService.Tagging.EditCategory``InventoryService.Tagging.EditTag``Sessions.ValidateSession``StorageProfile.Update`1`StorageProfile.View`1 |
| vSphere vCenter Cluster | Always | `Resource.AssignVMToPool` |
| vSphere datastore | Always | `Datastore.AllocateSpace``Datastore.Browse` |
| vSphere Port Group | Always | `Network.Assign` |
| Virtual Machine Folder | Always | `VirtualMachine.Config.AddRemoveDevice``VirtualMachine.Config.AdvancedConfig``VirtualMachine.Config.Annotation``VirtualMachine.Config.CPUCount``VirtualMachine.Config.DiskExtend``VirtualMachine.Config.Memory``VirtualMachine.Config.Settings``VirtualMachine.Interact.PowerOff``VirtualMachine.Interact.PowerOn``VirtualMachine.Inventory.CreateFromExisting``VirtualMachine.Inventory.Delete``VirtualMachine.Provisioning.Clone` |
| vSphere vCenter data center | If the installation program creates the virtual machine folder. | `Resource.AssignVMToPool``VirtualMachine.Provisioning.DeployTemplate` |
| 1 The `StorageProfile.Update` and `StorageProfile.View` permissions are required only for storage backends that use the Container Storage Interface (CSI). | | |

Show more

The following table details the permissions and propagation settings that are required for compute machine set management.

Expand

Table 2.4. Required permissions and propagation settings

| vSphere object | Folder type | Propagate to children | Permissions required |
| --- | --- | --- | --- |
| vSphere vCenter | Always | Not required | Listed required privileges |
| vSphere vCenter data center | Existing folder | Not required | `ReadOnly` permission |
| Installation program creates the folder | Required | Listed required privileges |
| vSphere vCenter Cluster | Always | Required | Listed required privileges |
| vSphere vCenter datastore | Always | Not required | Listed required privileges |
| vSphere Switch | Always | Not required | `ReadOnly` permission |
| vSphere Port Group | Always | Not required | Listed required privileges |
| vSphere vCenter Virtual Machine Folder | Existing folder | Required | Listed required privileges |

Show more

For more information about creating an account with only the required privileges, see [vSphere Permissions and User Management Tasks](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.security.doc/GUID-5372F580-5C23-4E9C-8A4E-EF1B4DD9033E.html) in the vSphere documentation.

#### [2.9.3. Requirements for clusters with user-provisioned infrastructure to use compute machine sets](#compute-machineset-upi-reqs_creating-machineset-vsphere) Copy linkLink copied to clipboard!

To enable the Machine API to manage and scale compute nodes on user-provisioned infrastructure, you can configure a `MachineSet` YAML file with specific vSphere parameters, for example data center and disk image. To use compute machine sets on clusters that have user-provisioned infrastructure, you must ensure that you cluster configuration supports using the Machine API.

##### [2.9.3.1. Obtaining the infrastructure ID](#machineset-upi-reqs-infra-id_creating-machineset-vsphere) Copy linkLink copied to clipboard!

To ensure the Machine API correctly identifies and manages virtual machines (VMs) that belong to a specific cluster, you must add the unique infrastructure ID to the `MachineSet` YAML file to label and link resources. To create compute machine sets, you must be able to supply the infrastructure ID for your cluster.

**Procedure**

* To obtain the infrastructure ID for your cluster, run the following command:

  ```
  $ oc get infrastructure cluster -o jsonpath='{.status.infrastructureName}'
  ```

##### [2.9.3.2. Satisfying vSphere credentials requirements](#machineset-upi-reqs-vsphere-creds_creating-machineset-vsphere) Copy linkLink copied to clipboard!

To use compute machine sets and manage virtual machine (VM) resources, the Machine API must be able to interact with vCenter. Credentials that authorize the Machine API components to interact with vCenter must exist in a secret in the `openshift-machine-api` namespace.

**Procedure**

1. To determine whether the required credentials exist, run the following command:

   ```
   $ oc get secret \
     -n openshift-machine-api vsphere-cloud-credentials \
     -o go-template='{{range $k,$v := .data}}{{printf "%s: " $k}}{{if not $v}}{{$v}}{{else}}{{$v | base64decode}}{{end}}{{"\n"}}{{end}}'
   ```

   **Sample output**

   ```
   <vcenter-server>.password=<openshift-user-password>
   <vcenter-server>.username=<openshift-user>
   ```

   where

   `<vcenter_server>`
   :   Specifies the IP address or fully qualified domain name (FQDN) of the vCenter server and `<openshift_user_password>` and `<openshift_user>` are the OpenShift Container Platform administrator credentials to use.
2. If the secret does not exist, create it by running the following command:

   ```
   $ oc create secret generic vsphere-cloud-credentials \
     -n openshift-machine-api \
     --from-literal=<vcenter-server>.username=<openshift-user> --from-literal=<vcenter-server>.password=<openshift-user-password>
   ```

##### [2.9.3.3. Satisfying Ignition configuration requirements](#machineset-upi-reqs-ignition-config_creating-machineset-vsphere) Copy linkLink copied to clipboard!

For the Machine API to provision virtual machines (VMs) with the correct initial configuration using Ignition, a valid Ignition configuration is required. The Ignition configuration contains the `machine-config-server` address and a system trust bundle for obtaining further Ignition configurations from the Machine Config Operator.

By default, this configuration is stored in the `worker-user-data` secret in the `machine-api-operator` namespace. Compute machine sets reference the secret during the machine creation process.

**Procedure**

1. To determine whether the required secret exists, run the following command:

   ```
   $ oc get secret \
     -n openshift-machine-api worker-user-data \
     -o go-template='{{range $k,$v := .data}}{{printf "%s: " $k}}{{if not $v}}{{$v}}{{else}}{{$v | base64decode}}{{end}}{{"\n"}}{{end}}'
   ```

   **Sample output**

   ```
   disableTemplating: false
   userData:
     {
       "ignition": {
         ...
         },
       ...
     }
   ```

   The full output is omitted here, but this is the format to use.
2. If the secret does not exist, create it by running the following command:

   ```
   $ oc create secret generic worker-user-data \
     -n openshift-machine-api \
     --from-file=<installation_directory>/worker.ign
   ```

   Specifies the directory that was used to store your installation assets during cluster installation.

#### [2.9.4. Creating a compute machine set](#machineset-creating_creating-machineset-vsphere) Copy linkLink copied to clipboard!

To dynamically manage machine compute resources, you can create your own compute machine sets in addition to the compute machine sets created by the installation program. Use the OpenShift Container Platform CLI to automate node provisioning.

Note

Clusters that are installed with user-provisioned infrastructure have a different networking stack than clusters with infrastructure that is provisioned by the installation program. As a result of this difference, automatic load balancer management is unsupported on clusters that have user-provisioned infrastructure. For these clusters, a compute machine set can only create `worker` and `infra` type machines.

**Prerequisites**

* Deploy an OpenShift Container Platform cluster.
* Install the OpenShift CLI (`oc`).
* Log in to `oc` as a user with `cluster-admin` permission.
* Have the necessary permissions to deploy VMs in your vCenter instance and have the required access to the datastore specified.
* If your cluster uses user-provisioned infrastructure, you have satisfied the specific Machine API requirements for that configuration.

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
   3. If you are creating a compute machine set for a cluster that has user-provisioned infrastructure, note the following important values:

      **Example vSphere `providerSpec` values**

      ```
      apiVersion: machine.openshift.io/v1beta1
      kind: MachineSet
      ...
      template:
        ...
        spec:
          providerSpec:
            value:
              apiVersion: machine.openshift.io/v1beta1
              credentialsSecret:
                name: vsphere-cloud-credentials
              dataDisks:
              - name: <disk_name>
                provisioningMode: <mode>
                sizeGiB: 10
              diskGiB: 120
              kind: VSphereMachineProviderSpec
              memoryMiB: 16384
              network:
                devices:
                  - networkName: "<vm_network_name>"
              numCPUs: 4
              numCoresPerSocket: 4
              snapshot: ""
              template: <vm_template_name>
              userDataSecret:
                name: worker-user-data
              workspace:
                datacenter: <vcenter_data_center_name>
                datastore: <vcenter_datastore_name>
                folder: <vcenter_vm_folder_path>
                resourcepool: <vsphere_resource_pool>
                server: <vcenter_server_address>
      ```

      where:

      `vsphere-cloud-credentials`
      :   Specifies the name of the secret in the `openshift-machine-api` namespace that contains the required vCenter credentials.

      `<disk_name>`
      :   Specifies the collection of data disk definitions. For more information, see "Configuring data disks by using machine sets".

      `<vm_template_name>`
      :   Specifies the name of the RHCOS VM template for your cluster that was created during installation.

      `worker-user-data`
      :   Specifies the name of the secret in the `openshift-machine-api` namespace that contains the required Ignition configuration credentials.

      `<vcenter_server_address>`
      :   Specifies the IP address or fully qualified domain name (FQDN) of the vCenter server.
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

#### [2.9.5. Labeling GPU machine sets for the cluster autoscaler](#machineset-label-gpu-autoscaler_creating-machineset-vsphere) Copy linkLink copied to clipboard!

Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

**Prerequisites**

* Your cluster uses a cluster autoscaler.

**Procedure**

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    name: machine-set-name
  spec:
    template:
      spec:
        metadata:
          labels:
            cluster-api/accelerator: <accelerator_name>
  ```

  where:

  `<accelerator_name>`
  :   Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.

      Note

      You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR. For more information, see "Cluster autoscaler resource definition".

#### [2.9.6. Adding tags to machines by using machine sets](#machine-api-vmw-add-tags_creating-machineset-vsphere) Copy linkLink copied to clipboard!

To ensure that your cluster remains scalable and resilient, you can use a `MachineSet` object and machine health checks to automate the provisioning and repair of nodes.

OpenShift Container Platform adds a cluster-specific tag to each virtual machine (VM) that it creates. The installation program uses these tags to select the VMs to delete when uninstalling a cluster.

In addition to the cluster-specific tags assigned to VMs, you can configure a machine set to add up to 10 additional vSphere tags to the VMs it provisions.

**Prerequisites**

* You have access to an OpenShift Container Platform cluster installed on vSphere using an account with `cluster-admin` permissions.
* You have access to the VMware vCenter console associated with your cluster.
* You have created a tag in the vCenter console.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Use the vCenter console to find the tag ID for any tag that you want to add to your machines:

   1. Log in to the vCenter console.
   2. From the **Home** menu, click **Tags & Custom Attributes**.
   3. Select a tag that you want to add to your machines.
   4. Use the browser URL for the tag that you select to identify the tag ID.

      **Example tag URL**

      ```
      https://vcenter.example.com/ui/app/tags/tag/urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL/permissions
      ```

      **Example tag ID**

      ```
      urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL
      ```
2. In a text editor, open the YAML file for an existing machine set or create a new one.
3. Edit the following lines under the `providerSpec` field:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             tagIDs:
             - <tag_id_value>
   # ...
   ```

   where

   `spec.template.spec.providerSpec.value.tagIDs`
   :   Specifies a list of up to 10 tags to add to the machines that this machine set provisions. Replace `<tag_id_value>` with the tag that you want to add to your machines. For example, `urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL`.

#### [2.9.7. Configuring multiple network interface controllers by using machine sets](#machineset-vsphere-multiple-nics_creating-machineset-vsphere) Copy linkLink copied to clipboard!

By configuring multiple network interface controllers (NICs), you can provide dedicated network links in the node virtual machines (VMs) for uses such as storage or databases. OpenShift Container Platform clusters on VMware vSphere support connecting up to 10 network NICs to a node.

You can use machine sets to manage this configuration.

* If you want to use multiple NICs in a vSphere cluster that was not configured to do so during installation, you can use machine sets to implement this configuration.
* If your cluster was set up during installation to use multiple NICs, machine sets that you create can use your existing failure domain configuration.
* If your failure domain configuration changes, you can use machine sets to make updates that reflect those changes.

**Prerequisites**

* You have administrator access to OpenShift CLI (`oc`) for an OpenShift Container Platform cluster on vSphere.

**Procedure**

1. For a cluster that already uses multiple NICs, obtain the following values from the `Infrastructure` resource by running the following command:

   ```
   $ oc get infrastructure cluster -o=jsonpath={.spec.platformSpec.vsphere.failureDomains}
   ```

   Expand

   Table 2.5. Required network interface controller values

   | `Infrastructure` resource value | Placeholder value for sample machine set | Description |
   | --- | --- | --- |
   | `failureDomain.topology.networks[0]` | `<vm_network_name_1>` | The name of the first NIC to use. |
   | `failureDomain.topology.networks[1]` | `<vm_network_name_2>` | The name of the second NIC to use. |
   | `failureDomain.topology.networks[<n-1>]` | `<vm_network_name_n>` | The name of the *n*th NIC to use. Collect the name of each NIC in the `Infrastructure` resource. |
   | `failureDomain.topology.template` | `<vm_template_name>` | The vSphere VM template to use. |
   | `failureDomain.topology.datacenter` | `<vcenter_data_center_name>` | The vCenter data center to deploy the machine set on. |
   | `failureDomain.topology.datastore` | `<vcenter_datastore_name>` | The vCenter datastore to deploy the machine set on. |
   | `failureDomain.topology.folder` | `<vcenter_vm_folder_path>` | The path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`. |
   | `failureDomain.topology.computeCluster` + `/Resources` | `<vsphere_resource_pool>` | The vSphere resource pool for your VMs. |
   | `failureDomain.server` | `<vcenter_server_ip>` | The vCenter server IP or fully qualified domain name (FQDN). |

   Show more
2. In a text editor, open the YAML file for an existing machine set or create a new one.
3. Use a machine set configuration formatted like the following example.

   * For a cluster that currently uses multiple NICs, use the values from the `Infrastructure` resource to populate the values in the machine set custom resource.
   * For a cluster that is not using multiple NICs, populate the values you want to use in the machine set custom resource.

   **Sample machine set**

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             network:
               devices:
               - networkName: "<vm_network_name_1>"
               - networkName: "<vm_network_name_2>"
             template: <vm_template_name>
             workspace:
               datacenter: <vcenter_data_center_name>
               datastore: <vcenter_datastore_name>
               folder: <vcenter_vm_folder_path>
               resourcepool: <vsphere_resource_pool>
               server: <vcenter_server_ip>
   # ...
   ```

   where:

   `spec.template.spec.providerSpec.value.network.devices`
   :   Specifies a list of up to 10 NICs to use.

   `spec.template.spec.providerSpec.value.network.template`
   :   Specifies the vSphere VM template to use, such as `user-5ddjd-rhcos`.

   `spec.template.spec.providerSpec.value.network.workspace.datacenter`
   :   Specifies the vCenter data center to deploy the machine set on.

   `spec.template.spec.providerSpec.value.network.workspace.datastore`
   :   Specifies the vCenter datastore to deploy the machine set on.

   `spec.template.spec.providerSpec.value.network.workspace.folder`
   :   Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`.

   `spec.template.spec.providerSpec.value.network.workspace.resourcepool`
   :   Specifies the vSphere resource pool for your VMs.

   `spec.template.spec.providerSpec.value.network.workspace.server`
   :   Specifies the vCenter server IP or fully qualified domain name (FQDN).

#### [2.9.8. Configuring data disks by using machine sets](#machineset-vsphere-data-disks_creating-machineset-vsphere) Copy linkLink copied to clipboard!

To provide persistent storage beyond the root volume for specialized application workloads, define a `dataDisks` array in the `MachineSet` YAML file to specify disk size and storage policy.

OpenShift Container Platform clusters on VMware vSphere support adding up to 29 disks to the virtual machine (VM) controller.

Important

Configuring vSphere data disks is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

By configuring data disks, you can attach disks to VMs and use them to store data for etcd, container images, and other uses. Separating data can help avoid filling the primary disk so that important activities such as upgrades have the resources that they require.

Note

Adding data disks attaches them to the VM and mounts them to the location that RHCOS designates.

**Prerequisites**

* You have administrator access to OpenShift CLI (`oc`) for an OpenShift Container Platform cluster on vSphere.

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following lines under the `providerSpec` field:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             dataDisks:
             - name: "<disk_name>"
               provisioningMode: "<mode>"
               sizeGiB: 20
             - name: "<disk_name>"
               provisioningMode: "<mode>"
               sizeGiB: 20
   # ...
   ```

   where

   `spec.template.spec.providerSpec.value.dataDisks`
   :   Specifies a collection of 1-29 data disk definitions. This sample configuration shows the formatting to include two data disk definitions.

   `spec.template.spec.providerSpec.value.dataDisks.name`
   :   Specifies the name of the data disk. The name must meet the following requirements:

       * Start and end with an alphanumeric character
       * Consist only of alphanumeric characters, hyphens (`-`), and underscores (`_`)
       * Have a maximum length of 80 characters

   `spec.template.spec.providerSpec.value.dataDisks.provisioningMode`
   :   Specifies the data disk provisioning method. This value defaults to the vSphere default storage policy if not set. Valid values are `Thin`, `Thick`, and `EagerlyZeroed`.

   `spec.template.spec.providerSpec.value.dataDisks.sizeGiB`
   :   Specifies the size of the data disk in GiB. The maximum size is 16,384 GiB.

### [2.10. Creating a compute machine set on bare metal](#creating-machineset-bare-metal) Copy linkLink copied to clipboard!

You can create a different compute machine set to serve a specific purpose in your OpenShift Container Platform cluster on bare metal. For example, you might create infrastructure machine sets and related machines so that you can move supporting workloads to the new machines.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

#### [2.10.1. Sample YAML for a compute machine set custom resource on bare metal](#machineset-yaml-baremetal_creating-machineset-bare-metal) Copy linkLink copied to clipboard!

You can define and apply a compute machine set on bare-metal infrastructure to automate node provisioning.

The sample bare metal YAML defines a compute machine set that runs on bare-metal infrastructure and creates nodes that are labeled with `node-role.kubernetes.io/<role>: ""`.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<role>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  creationTimestamp: null
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
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <role>
        machine.openshift.io/cluster-api-machine-type: <role>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<role>
    spec:
      metadata:
        creationTimestamp: null
        labels:
          node-role.kubernetes.io/<role>: ""
      providerSpec:
        value:
          apiVersion: baremetal.cluster.k8s.io/v1alpha1
          hostSelector: {}
          image:
            checksum: <image_checksum>
            url: <image_url>
          kind: BareMetalMachineProviderSpec
          metadata:
            creationTimestamp: null
          userData:
            name: worker-user-data-managed
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`<infrastructure_id>-<role>`
:   Specifies the infrastructure ID and `<role>` node label.

`<role>`
:   Specifies the node label to add.

Note

`<image_checksum>`
:   Specifies the image checksum, the URL that you edit to use the API VIP address, in the following format: `http://172.22.0.3:6181/images/rhcos-<version>.<architecture>.qcow2.<md5sum>`.

`<image_url>`
:   Specifies the image URL, the URL that you edit to use the API VIP address, in the following format: `http://172.22.0.3:6181/images/rhcos-<version>.<architecture>.qcow2`.

You should use the latest image when adding a new machine set.

#### [2.10.2. Creating a compute machine set](#machineset-creating_creating-machineset-bare-metal) Copy linkLink copied to clipboard!

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

#### [2.10.3. Labeling GPU machine sets for the cluster autoscaler](#machineset-label-gpu-autoscaler_creating-machineset-bare-metal) Copy linkLink copied to clipboard!

Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

**Prerequisites**

* Your cluster uses a cluster autoscaler.

**Procedure**

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    name: machine-set-name
  spec:
    template:
      spec:
        metadata:
          labels:
            cluster-api/accelerator: <accelerator_name>
  ```

  where:

  `<accelerator_name>`
  :   Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.

      Note

      You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR. For more information, see "Cluster autoscaler resource definition".

## [Chapter 3. Manually scaling a compute machine set](#manually-scaling-machineset) Copy linkLink copied to clipboard!

You can manually add or remove an instance of a machine in a compute machine set. Manually scaling a compute machine set gives you control over the resource utilization of that machine set.

Note

If you need to modify aspects of a compute machine set outside of scaling, see "Modifying a compute machine set".

### [3.1. Prerequisites](#prerequisites) Copy linkLink copied to clipboard!

* If you enabled the cluster-wide proxy and scale up compute machines not included in `networking.machineNetwork[].cidr` from the installation configuration, you must add the compute machines to the Proxy object’s `noProxy` field to prevent connection issues. See "Add the compute machines to the Proxy object’s `noProxy` field" for more information.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

### [3.2. Scaling a compute machine set manually](#machineset-manually-scaling_manually-scaling-machineset) Copy linkLink copied to clipboard!

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

### [3.3. The compute machine set deletion policy](#machineset-delete-policy_manually-scaling-machineset) Copy linkLink copied to clipboard!

Compute machine sets can be configured to use the `Random`, `Newest`, and `Oldest` deletion options. The default is `Random`, meaning that random machines are chosen and deleted when scaling compute machine sets down.

The deletion policy can be set according to the use case by modifying the particular compute machine set as in the following example:

```
spec:
  deletePolicy: <delete_policy>
  replicas: <desired_replica_count>
```

Specific machines can also be prioritized for deletion by adding the annotation `machine.openshift.io/delete-machine=true` to the machine of interest, regardless of the deletion policy.

Important

By default, the OpenShift Container Platform router pods are deployed on workers. Because the router is required to access some cluster resources, including the web console, do not scale the worker compute machine set to `0` unless you first relocate the router pods.

Note

Custom compute machine sets can be used for use cases requiring that services run on specific nodes and that those services are ignored by the controller when the worker compute machine sets are scaling down. This prevents service disruption.

## [Chapter 4. Modifying a compute machine set](#modifying-machineset) Copy linkLink copied to clipboard!

To add labels, change the instance type, change block storage, or make other changes, you can modify a compute machine set.

Note

If you need to scale a compute machine set without making other changes, see "Manually scaling a compute machine set".

### [4.1. Modifying a compute machine set by using the CLI](#machineset-modifying_modifying-machineset) Copy linkLink copied to clipboard!

To enable features or change the properties of machines, you can modify the configuration of a compute machine set using the CLI. You can then propagate the changes to the machines in your cluster.

When you modify a compute machine set, your changes only apply to compute machines that are created after you save the updated `MachineSet` custom resource (CR). The changes do not affect existing machines.

Note

Changes made in the underlying cloud provider are not reflected in the `Machine` or `MachineSet` CRs. To adjust instance configuration in cluster-managed infrastructure, use the cluster-side resources.

You can replace the existing machines with new ones that reflect the updated configuration by scaling the compute machine set to create twice the number of replicas and then scaling it down to the original number of replicas.

If you need to scale a compute machine set without making other changes, you do not need to delete the machines.

Note

By default, the OpenShift Container Platform router pods are deployed on compute machines. Because the router is required to access some cluster resources, including the web console, do not scale the compute machine set to `0` unless you first relocate the router pods.

The output examples in this procedure use the values for an AWS cluster.

**Prerequisites**

* Your OpenShift Container Platform cluster uses the Machine API.
* You are logged in to the cluster as an administrator by using the OpenShift CLI (`oc`).

**Procedure**

1. List the compute machine sets in your cluster by running the following command:

   ```
   $ oc get machinesets.machine.openshift.io -n openshift-machine-api
   ```

   **Example output**

   ```
   NAME                           DESIRED   CURRENT   READY   AVAILABLE   AGE
   <compute_machine_set_name_1>   1         1         1       1           55m
   <compute_machine_set_name_2>   1         1         1       1           55m
   ```
2. Edit a compute machine set by running the following command:

   ```
   $ oc edit machinesets.machine.openshift.io <machine_set_name> \
     -n openshift-machine-api
   ```
3. Note the value of the `spec.replicas` field, because you need it when scaling the machine set to apply the changes.

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   metadata:
     name: <machine_set_name>
     namespace: openshift-machine-api
   spec:
     replicas: 2
   # ...
   ```

   The examples in this procedure show a compute machine set that has a `replicas` value of `2`.
4. Update the compute machine set CR with the configuration options that you want and save your changes.
5. List the machines that are managed by the updated compute machine set by running the following command:

   ```
   $ oc get machines.machine.openshift.io \
     -n openshift-machine-api \
     -l machine.openshift.io/cluster-api-machineset=<machine_set_name>
   ```

   **Example output for an AWS cluster**

   ```
   NAME                        PHASE     TYPE         REGION      ZONE         AGE
   <machine_name_original_1>   Running   m6i.xlarge   us-west-1   us-west-1a   4h
   <machine_name_original_2>   Running   m6i.xlarge   us-west-1   us-west-1a   4h
   ```
6. For each machine that is managed by the updated compute machine set, set the `delete` annotation by running the following command:

   ```
   $ oc annotate machine.machine.openshift.io/<machine_name_original_1> \
     -n openshift-machine-api \
     machine.openshift.io/delete-machine="true"
   ```
7. To create replacement machines with the new configuration, scale the compute machine set to twice the number of replicas by running the following command:

   ```
   $ oc scale --replicas=4 \
     machineset.machine.openshift.io <machine_set_name> \
     -n openshift-machine-api
   ```

   The original example value of `2` is doubled to `4`.
8. List the machines that are managed by the updated compute machine set by running the following command:

   ```
   $ oc get machines.machine.openshift.io \
     -n openshift-machine-api \
     -l machine.openshift.io/cluster-api-machineset=<machine_set_name>
   ```

   **Example output for an AWS cluster**

   ```
   NAME                        PHASE          TYPE         REGION      ZONE         AGE
   <machine_name_original_1>   Running        m6i.xlarge   us-west-1   us-west-1a   4h
   <machine_name_original_2>   Running        m6i.xlarge   us-west-1   us-west-1a   4h
   <machine_name_updated_1>    Provisioned    m6i.xlarge   us-west-1   us-west-1a   55s
   <machine_name_updated_2>    Provisioning   m6i.xlarge   us-west-1   us-west-1a   55s
   ```

   When the new machines are in the `Running` phase, you can scale the compute machine set to the original number of replicas.
9. To remove the machines that were created with the old configuration, scale the compute machine set to the original number of replicas by running the following command:

   ```
   $ oc scale --replicas=2 \
     machineset.machine.openshift.io <machine_set_name> \
     -n openshift-machine-api
   ```

   The `replicas` parameter is set to the original example value of `2`.

**Verification**

* To verify that a machine created by the updated machine set has the correct configuration, examine the relevant fields in the CR for one of the new machines by running the following command:

  ```
  $ oc describe machine.machine.openshift.io <machine_name_updated_1> \
    -n openshift-machine-api
  ```
* To verify that the compute machines without the updated configuration are deleted, list the machines that are managed by the updated compute machine set by running the following command:

  ```
  $ oc get machines.machine.openshift.io \
    -n openshift-machine-api \
    -l machine.openshift.io/cluster-api-machineset=<machine_set_name>
  ```

  **Example output while deletion is in progress for an AWS cluster**

  ```
  NAME                        PHASE           TYPE         REGION      ZONE         AGE
  <machine_name_original_1>   Deleting        m6i.xlarge   us-west-1   us-west-1a   4h
  <machine_name_original_2>   Deleting        m6i.xlarge   us-west-1   us-west-1a   4h
  <machine_name_updated_1>    Running         m6i.xlarge   us-west-1   us-west-1a   5m41s
  <machine_name_updated_2>    Running         m6i.xlarge   us-west-1   us-west-1a   5m41s
  ```

  **Example output when deletion is complete for an AWS cluster**

  ```
  NAME                        PHASE           TYPE         REGION      ZONE         AGE
  <machine_name_updated_1>    Running         m6i.xlarge   us-west-1   us-west-1a   6m30s
  <machine_name_updated_2>    Running         m6i.xlarge   us-west-1   us-west-1a   6m30s
  ```

  end::MAPI[]

## [Chapter 5. Machine phases and lifecycle](#machine-phases-lifecycle) Copy linkLink copied to clipboard!

Machines move through a *lifecycle* that has several defined phases. Understanding the machine lifecycle and its phases can help you verify whether a procedure is complete or troubleshoot undesired behavior. In OpenShift Container Platform, the machine lifecycle is consistent across all supported cloud providers.

### [5.1. Machine phases](#machine-about-phases_machine-phases-lifecycle) Copy linkLink copied to clipboard!

Understanding machine lifecycle phases can help you troubleshoot machine issues. As a machine moves through its lifecycle, it passes through different phases. Each phase is a basic representation of the state of the machine.

`Provisioning`
:   There is a request to provision a new machine. The machine does not yet exist and does not have an instance, a provider ID, or an address.

`Provisioned`
:   The machine exists and has a provider ID or an address. The cloud provider has created an instance for the machine. The machine has not yet become a node and the `status.nodeRef` section of the machine object is not yet populated.

`Running`
:   The machine exists and has a provider ID or address. Ignition has run successfully and the cluster machine approver has approved a certificate signing request (CSR). The machine has become a node and the `status.nodeRef` section of the machine object contains node details.

`Deleting`
:   There is a request to delete the machine. The machine object has a `DeletionTimestamp` field that indicates the time of the deletion request.

`Failed`
:   There is an unrecoverable problem with the machine. This can happen, for example, if the cloud provider deletes the instance for the machine.

### [5.2. The machine lifecycle](#machine-about-lifecycle_machine-phases-lifecycle) Copy linkLink copied to clipboard!

Understanding the machine lifecycle can help you troubleshoot machine issues. The lifecycle begins with the request to provision a machine and continues until the machine no longer exists.

The machine lifecycle proceeds in the following order. Interruptions due to errors or lifecycle hooks are not included in this overview.

1. There is a request to provision a new machine for one of the following reasons:

   * A cluster administrator scales a machine set such that it requires additional machines.
   * An autoscaling policy scales machine set such that it requires additional machines.
   * A machine that is managed by a machine set fails or is deleted and the machine set creates a replacement to maintain the required number of machines.
2. The machine enters the `Provisioning` phase.
3. The infrastructure provider creates an instance for the machine.
4. The machine has a provider ID or address and enters the `Provisioned` phase.
5. The Ignition configuration file is processed.
6. The kubelet issues a certificate signing request (CSR).
7. The cluster machine approver approves the CSR.
8. The machine becomes a node and enters the `Running` phase.
9. An existing machine is slated for deletion for one of the following reasons:

   * A user with `cluster-admin` permissions uses the `oc delete machine` command.
   * The machine gets a `machine.openshift.io/delete-machine` annotation.
   * The machine set that manages the machine marks it for deletion to reduce the replica count as part of reconciliation.
   * The cluster autoscaler identifies a node that is unnecessary to meet the deployment needs of the cluster.
   * A machine health check is configured to replace an unhealthy machine.
10. The machine enters the `Deleting` phase, in which it is marked for deletion but is still present in the API.
11. The machine controller removes the instance from the infrastructure provider.
12. The machine controller deletes the `Node` object.

### [5.3. Determining the phase of a machine by using the CLI](#machine-determine-phase-cli_machine-phases-lifecycle) Copy linkLink copied to clipboard!

To troubleshoot issues with a machine, you can find the phase of a machine by using the OpenShift CLI (`oc`).

**Prerequisites**

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.
* You have installed the `oc` CLI.

**Procedure**

* List the machines on the cluster by running the following command:

  ```
  $ oc get machine -n openshift-machine-api
  ```

  **Example output**

  ```
  NAME                                      PHASE     TYPE         REGION      ZONE         AGE
  mycluster-5kbsp-master-0                  Running   m6i.xlarge   us-west-1   us-west-1a   4h55m
  mycluster-5kbsp-master-1                  Running   m6i.xlarge   us-west-1   us-west-1b   4h55m
  mycluster-5kbsp-master-2                  Running   m6i.xlarge   us-west-1   us-west-1a   4h55m
  mycluster-5kbsp-worker-us-west-1a-fmx8t   Running   m6i.xlarge   us-west-1   us-west-1a   4h51m
  mycluster-5kbsp-worker-us-west-1a-m889l   Running   m6i.xlarge   us-west-1   us-west-1a   4h51m
  mycluster-5kbsp-worker-us-west-1b-c8qzm   Running   m6i.xlarge   us-west-1   us-west-1b   4h51m
  ```

  The `PHASE` column of the output contains the phase of each machine.

### [5.4. Determining the phase of a machine by using the web console](#machine-determine-phase-gui_machine-phases-lifecycle) Copy linkLink copied to clipboard!

To troubleshoot issues with a machine, you can find the phase of a machine by using the OpenShift Container Platform web console.

**Prerequisites**

* You have access to an OpenShift Container Platform cluster using an account with `cluster-admin` permissions.

**Procedure**

1. Log in to the web console as a user with the `cluster-admin` role.
2. Navigate to **Compute** → **Machines**.
3. On the **Machines** page, select the name of the machine that you want to find the phase of.
4. On the **Machine details** page, select the **YAML** tab.
5. In the YAML block, find the value of the `status.phase` field.

   **Example YAML snippet**

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: Machine
   metadata:
     name: mycluster-5kbsp-worker-us-west-1a-fmx8t
   # ...
   status:
     phase: Running
   ```

   In this example, the phase is `Running`.

## [Chapter 6. Deleting a machine](#deleting-machine) Copy linkLink copied to clipboard!

If you need to remove a machine from your cluster, you can delete a specific machine. If the machine is part of a machine set, deleting the machine can help troubleshoot and resolve unhealthy nodes and other technical issues.

### [6.1. Deleting a specific machine](#machine-delete_deleting-machine) Copy linkLink copied to clipboard!

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

### [6.2. Lifecycle hooks for the machine deletion phase](#machine-lifecycle-hook-deletion_deleting-machine) Copy linkLink copied to clipboard!

You can use lifecycle hooks to modify the process of machine deletion. Machine lifecycle hooks are points in the reconciliation lifecycle of a machine where the normal lifecycle process can be interrupted.

For example, you might use a `preDrain` lifecycle hook to maintain etcd quorum when deleting a control plane machine.

#### [6.2.1. Terminology and definitions](#machine-lifecycle-hook-deletion-terms_deleting-machine) Copy linkLink copied to clipboard!

To understand the behavior of lifecycle hooks for the machine deletion phase, you must understand the following concepts:

Reconciliation
:   Reconciliation is the process by which a controller attempts to make the real state of the cluster and the objects that it comprises match the requirements in an object specification.

Machine controller
:   The machine controller manages the reconciliation lifecycle for a machine. For machines on cloud platforms, the machine controller is the combination of an OpenShift Container Platform controller and a platform-specific actuator from the cloud provider.

    In the context of machine deletion, the machine controller performs the following actions:

    * Drain the node that is backed by the machine.
    * Delete the machine instance from the cloud provider.
    * Delete the `Node` object.

Lifecycle hook
:   A lifecycle hook is a defined point in the reconciliation lifecycle of an object where the normal lifecycle process can be interrupted. Components can use a lifecycle hook to inject changes into the process to accomplish a desired outcome.

    There are two lifecycle hooks in the machine `Deleting` phase:

    * `preDrain` lifecycle hooks must be resolved before the node that is backed by the machine can be drained.
    * `preTerminate` lifecycle hooks must be resolved before the instance can be removed from the infrastructure provider.

Hook-implementing controller
:   A hook-implementing controller is a controller, other than the machine controller, that can interact with a lifecycle hook. A hook-implementing controller can do one or more of the following actions:

    * Add a lifecycle hook.
    * Respond to a lifecycle hook.
    * Remove a lifecycle hook.

    Each lifecycle hook has a single hook-implementing controller, but a hook-implementing controller can manage one or more hooks.

#### [6.2.2. Machine deletion processing order](#machine-lifecycle-hook-deletion-order_deleting-machine) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, there are two lifecycle hooks for the machine deletion phase: `preDrain` and `preTerminate`. When all hooks for a given lifecycle point are removed, reconciliation continues as normal.

**Figure 6.1. Machine deletion flow**

The machine `Deleting` phase proceeds in the following order:

1. An existing machine is slated for deletion for one of the following reasons:

   * A user with `cluster-admin` permissions uses the `oc delete machine` command.
   * The machine gets a `machine.openshift.io/delete-machine` annotation.
   * The machine set that manages the machine marks it for deletion to reduce the replica count as part of reconciliation.
   * The cluster autoscaler identifies a node that is unnecessary to meet the deployment needs of the cluster.
   * A machine health check is configured to replace an unhealthy machine.
2. The machine enters the `Deleting` phase, in which it is marked for deletion but is still present in the API.
3. If a `preDrain` lifecycle hook exists, the hook-implementing controller that manages it does a specified action.

   Until all `preDrain` lifecycle hooks are satisfied, the machine status condition `Drainable` is set to `False`.
4. There are no unresolved `preDrain` lifecycle hooks and the machine status condition `Drainable` is set to `True`.
5. The machine controller attempts to drain the node that is backed by the machine.

   * If draining fails, `Drained` is set to `False` and the machine controller attempts to drain the node again.
   * If draining succeeds, `Drained` is set to `True`.
6. The machine status condition `Drained` is set to `True`.
7. If a `preTerminate` lifecycle hook exists, the hook-implementing controller that manages it does a specified action.

   Until all `preTerminate` lifecycle hooks are satisfied, the machine status condition `Terminable` is set to `False`.
8. There are no unresolved `preTerminate` lifecycle hooks and the machine status condition `Terminable` is set to `True`.
9. The machine controller removes the instance from the infrastructure provider.
10. The machine controller deletes the `Node` object.

#### [6.2.3. Deletion lifecycle hook configuration](#machine-lifecycle-hook-deletion-format_deleting-machine) Copy linkLink copied to clipboard!

The following YAML snippets demonstrate the format and placement of deletion lifecycle hook configurations within a machine set:

**YAML snippet demonstrating a `preDrain` lifecycle hook**

```
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  ...
spec:
  lifecycleHooks:
    preDrain:
    - name: <hook_name>
      owner: <hook_owner>
  ...
```

where:

`<hook_name>`
:   Specifies the name of the `preDrain` lifecycle hook.

`<hook_owner>`
:   Specifies the hook-implementing controller that manages the `preDrain` lifecycle hook.

**YAML snippet demonstrating a `preTerminate` lifecycle hook**

```
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  ...
spec:
  lifecycleHooks:
    preTerminate:
    - name: <hook_name>
      owner: <hook_owner>
  ...
```

where:

`<hook_name>`
:   Specifies the name of the `preDrain` lifecycle hook.

`<hook_owner>`
:   Specifies the hook-implementing controller that manages the `preDrain` lifecycle hook.

##### [6.2.3.1. Example lifecycle hook configuration](#machine-lifecycle-hook-deletion-example_deleting-machine) Copy linkLink copied to clipboard!

The following example demonstrates the implementation of multiple fictional lifecycle hooks that interrupt the machine deletion process:

**Example configuration for lifecycle hooks**

```
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  ...
spec:
  lifecycleHooks:
    preDrain:
    - name: MigrateImportantApp
      owner: my-app-migration-controller
    preTerminate:
    - name: BackupFileSystem
      owner: my-backup-controller
    - name: CloudProviderSpecialCase
      owner: my-custom-storage-detach-controller
    - name: WaitForStorageDetach
      owner: my-custom-storage-detach-controller
  ...
```

where:

`spec.lifecycleHooks.preDrain`
:   Specifies a `preDrain` lifecycle hook stanza that contains a single lifecycle hook.

`spec.lifecycleHooks.preTerminate`
:   Specifies a `preTerminate` lifecycle hook stanza that contains three lifecycle hooks. Note that one controller can own multiple lifecycle hooks, as `my-custom-storage-detach-controller` does in the example.

#### [6.2.4. Machine deletion lifecycle hook examples for Operator developers](#machine-lifecycle-hook-deletion-uses_deleting-machine) Copy linkLink copied to clipboard!

Operators can use lifecycle hooks for the machine deletion phase to modify the machine deletion process.

The following examples demonstrate possible ways that an Operator can use this functionality.

##### [6.2.4.1. Example use cases for preDrain lifecycle hooks](#machine-lifecycle-hook-deletion-uses-predrain_deleting-machine) Copy linkLink copied to clipboard!

Proactively replacing machines
:   An Operator can use a `preDrain` lifecycle hook to ensure that a replacement machine is successfully created and joined to the cluster before removing the instance of a deleted machine. This can mitigate the impact of disruptions during machine replacement or of replacement instances that do not initialize promptly.

Implementing custom draining logic
:   An Operator can use a `preDrain` lifecycle hook to replace the machine controller draining logic with a different draining controller. By replacing the draining logic, the Operator would have more flexibility and control over the lifecycle of the workloads on each node.

    For example, the machine controller drain libraries do not support ordering, but a custom drain provider could provide this functionality. By using a custom drain provider, an Operator could prioritize moving mission-critical applications before draining the node to ensure that service interruptions are minimized in cases where cluster capacity is limited.

##### [6.2.4.2. Example use cases for preTerminate lifecycle hooks](#machine-lifecycle-hook-deletion-uses-preterminate_deleting-machine) Copy linkLink copied to clipboard!

Verifying storage detachment
:   An Operator can use a `preTerminate` lifecycle hook to ensure that storage that is attached to a machine is detached before the machine is removed from the infrastructure provider.

Improving log reliability
:   After a node is drained, the log exporter daemon requires some time to synchronize logs to the centralized logging system.

    A logging Operator can use a `preTerminate` lifecycle hook to add a delay between when the node drains and when the machine is removed from the infrastructure provider. This delay would provide time for the Operator to ensure that the main workloads are removed and no longer adding to the log backlog. When no new data is being added to the log backlog, the log exporter can catch up on the synchronization process, thus ensuring that all application logs are captured.

#### [6.2.5. Quorum protection with machine lifecycle hooks](#machine-lifecycle-hook-deletion-etcd_deleting-machine) Copy linkLink copied to clipboard!

To protect etcd quorum on OpenShift Container Platform clusters that use the Machine API Operator, the etcd Operator uses lifecycle hooks for the machine deletion phase to implement a quorum protection mechanism.

By using a `preDrain` lifecycle hook, the etcd Operator can control when the pods on a control plane machine are drained and removed. To protect etcd quorum, the etcd Operator prevents the removal of an etcd member until it migrates that member onto a new node within the cluster.

This mechanism allows the etcd Operator precise control over the members of the etcd quorum and allows the Machine API Operator to safely create and remove control plane machines without specific operational knowledge of the etcd cluster.

##### [6.2.5.1. Control plane deletion with quorum protection processing order](#machine-lifecycle-hook-deletion-etcd-order_deleting-machine) Copy linkLink copied to clipboard!

When a control plane machine is replaced on a cluster that uses a control plane machine set, the cluster temporarily has four control plane machines. When the fourth control plane node joins the cluster, the etcd Operator starts a new etcd member on the replacement node. When the etcd Operator observes that the old control plane machine is marked for deletion, it stops the etcd member on the old node and promotes the replacement etcd member to join the quorum of the cluster.

The control plane machine `Deleting` phase proceeds in the following order:

1. A control plane machine is slated for deletion.
2. The control plane machine enters the `Deleting` phase.
3. To satisfy the `preDrain` lifecycle hook, the etcd Operator takes the following actions:

   1. The etcd Operator waits until a fourth control plane machine is added to the cluster as an etcd member. This new etcd member has a state of `Running` but not `ready` until it receives the full database update from the etcd leader.
   2. When the new etcd member receives the full database update, the etcd Operator promotes the new etcd member to a voting member and removes the old etcd member from the cluster.

   After this transition is complete, it is safe for the old etcd pod and its data to be removed, so the `preDrain` lifecycle hook is removed.
4. The control plane machine status condition `Drainable` is set to `True`.
5. The machine controller attempts to drain the node that is backed by the control plane machine.

   * If draining fails, `Drained` is set to `False` and the machine controller attempts to drain the node again.
   * If draining succeeds, `Drained` is set to `True`.
6. The control plane machine status condition `Drained` is set to `True`.
7. If no other Operators have added a `preTerminate` lifecycle hook, the control plane machine status condition `Terminable` is set to `True`.
8. The machine controller removes the instance from the infrastructure provider.
9. The machine controller deletes the `Node` object.

**YAML snippet demonstrating the etcd quorum protection `preDrain` lifecycle hook**

```
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  ...
spec:
  lifecycleHooks:
    preDrain:
    - name: EtcdQuorumOperator
      owner: clusteroperator/etcd
  ...
```

where:

`spec.lifecycleHooks.preDrain.name`
:   Specifies the name of the `preDrain` lifecycle hook.

`spec.lifecycleHooks.preDrain.owner`
:   Specifies the hook-implementing controller that manages the `preDrain` lifecycle hook.

## [Chapter 7. Applying autoscaling to an OpenShift Container Platform cluster](#applying-autoscaling) Copy linkLink copied to clipboard!

Apply autoscaling to an OpenShift Container Platform cluster to automatically adjust the size of the cluster to meet deployment needs. You can deploy a cluster autoscaler and then deploy machine autoscalers for each machine type in your cluster. After you configure the cluster autoscaler, you must configure at least one machine autoscaler.

Important

You can configure the cluster autoscaler only in clusters where the Machine API Operator is operational.

### [7.1. The cluster autoscaler](#cluster-autoscaler-about_applying-autoscaling) Copy linkLink copied to clipboard!

The cluster autoscaler adjusts the size of an OpenShift Container Platform cluster to meet its current deployment needs. It uses declarative, Kubernetes-style arguments to provide infrastructure management that does not rely on objects of a specific cloud provider.

The cluster autoscaler increases the size of the cluster when there are pods that fail to schedule on any of the current worker nodes due to insufficient resources or when another node is necessary to meet deployment needs. The cluster autoscaler does not increase the cluster resources beyond the limits that you specify.

The cluster autoscaler computes the total memory, CPU, and GPU on all nodes the cluster, even though it does not manage the control plane nodes. These values are not single-machine oriented. They are an aggregation of all the resources in the entire cluster. For example, if you set the maximum memory resource limit, the cluster autoscaler includes all the nodes in the cluster when calculating the current memory usage. That calculation is then used to determine if the cluster autoscaler has the capacity to add more worker resources.

Important

Ensure that the `maxNodesTotal` value in the `ClusterAutoscaler` custom resource (CR) that you create is large enough to account for the total possible number of machines in your cluster. This value must encompass the number of control plane machines and the possible number of compute machines that you might scale to.

#### [7.1.1. Automatic node removal](#cluster-autoscaler-scale-down_applying-autoscaling) Copy linkLink copied to clipboard!

Every 10 seconds, the cluster autoscaler checks which nodes are unnecessary in the cluster and removes them. The cluster autoscaler considers a node for removal if the following conditions apply:

* The node utilization is less than the *node utilization level* threshold for the cluster. The node utilization level is the sum of the requested resources divided by the allocated resources for the node. If you do not specify a value in the `ClusterAutoscaler` custom resource, the cluster autoscaler uses a default value of `0.5`, which corresponds to 50% utilization.
* The cluster autoscaler can move all pods running on the node to the other nodes. The Kubernetes scheduler is responsible for scheduling pods on the nodes.
* The cluster autoscaler does not have scale down disabled annotation.

If the following types of pods are present on a node, the cluster autoscaler will not remove the node:

* Pods with restrictive pod disruption budgets (PDBs).
* Kube-system pods that do not run on the node by default.
* Kube-system pods that do not have a PDB or have a PDB that is too restrictive.
* Pods that are not backed by a controller object such as a deployment, replica set, or stateful set.
* Pods with local storage.
* Pods that cannot be moved elsewhere because of a lack of resources, incompatible node selectors or affinity, matching anti-affinity, and so on.
* Unless they also have a `"cluster-autoscaler.kubernetes.io/safe-to-evict": "true"` annotation, pods that have a `"cluster-autoscaler.kubernetes.io/safe-to-evict": "false"` annotation.

For example, you set the maximum CPU limit to 64 cores and configure the cluster autoscaler to only create machines that have 8 cores each. If your cluster starts with 30 cores, the cluster autoscaler can add up to 4 more nodes with 32 cores, for a total of 62.

Note

By default, when the cluster autoscaler removes a node, it does not cordon the node when draining the pods from the node. You can configure the cluster autoscaler to cordon the node before draining and moving the pods by setting the `spec.scaleDown.cordonNodeBeforeTerminating` parameter to `enabled` in the `ClusterAutoscaler` CR. This parameter is disabled by default. It is recommended to enable this parameter in production clusters because of the risk of data loss, application errors, pods getting stuck in the terminating state, or other issues if the cluster autoscaler removes a node when the parameter is disabled. Leaving this parameter disabled, which can result in faster node removal, might be appropriate in clusters that run only stateless workloads.

#### [7.1.2. Limitations](#cluster-autoscaler-limitations_applying-autoscaling) Copy linkLink copied to clipboard!

If you configure the cluster autoscaler, additional usage restrictions apply:

* Do not change the nodes that are in autoscaled node groups directly. All nodes within the same node group have the same capacity and labels and run the same system pods.
* Specify requests for your pods.
* If you have to prevent pods from being deleted too quickly, configure appropriate PDBs.
* Confirm that your cloud provider quota is large enough to support the maximum node pools that you configure.
* Do not run additional node group autoscalers, especially the ones offered by your cloud provider.

Note

The cluster autoscaler only adds nodes in autoscaled node groups if doing so would result in a schedulable pod. If the available node types cannot meet the requirements for a pod request, or if the node groups that could meet these requirements are at their maximum size, the cluster autoscaler cannot scale up.

#### [7.1.3. Interaction with other scheduling features](#cluster-autoscaler-interaction_applying-autoscaling) Copy linkLink copied to clipboard!

The horizontal pod autoscaler (HPA) and the cluster autoscaler change cluster resources in different ways. The HPA changes the deployment’s or replica set’s number of replicas based on the current CPU load. If the load increases, the HPA creates new replicas, regardless of the amount of resources available to the cluster. If there are not enough resources, the cluster autoscaler adds resources so that the HPA-created pods can run. If the load decreases, the HPA stops some replicas. If this action causes some nodes to be underutilized or completely empty, the cluster autoscaler deletes the unnecessary nodes.

The cluster autoscaler takes pod priorities into account. The Pod Priority and Preemption feature enables scheduling pods based on priorities if the cluster does not have enough resources, but the cluster autoscaler ensures that the cluster has resources to run all pods. To honor the intention of both features, the cluster autoscaler includes a priority cutoff function. You can use this cutoff to schedule "best-effort" pods, which do not cause the cluster autoscaler to increase resources but instead run only when spare resources are available.

Pods with priority lower than the cutoff value do not cause the cluster to scale up or prevent the cluster from scaling down. No new nodes are added to run the pods, and nodes running these pods might be deleted to free resources.

#### [7.1.4. Cluster autoscaler resource definition](#cluster-autoscaler-cr_applying-autoscaling) Copy linkLink copied to clipboard!

This `ClusterAutoscaler` resource definition shows the parameters and sample values for the cluster autoscaler.

Note

When you change the configuration of an existing cluster autoscaler, it restarts.

```
apiVersion: "autoscaling.openshift.io/v1"
kind: "ClusterAutoscaler"
metadata:
  name: "default"
spec:
  podPriorityThreshold: -10
  resourceLimits:
    maxNodesTotal: 24
    cores:
      min: 8
      max: 128
    memory:
      min: 4
      max: 256
    gpus:
    - type: <gpu_type>
      min: 0
      max: 16
  logVerbosity: 4
  scaleDown:
    cordonNodeBeforeTerminating: Enabled
    enabled: true
    delayAfterAdd: 10m
    delayAfterDelete: 5m
    delayAfterFailure: 30s
    unneededTime: 5m
    utilizationThreshold: "0.4"
  scaleUp:
    newPodScaleUpDelay: "10s"
  expanders: ["Random"]
```

Expand

Table 7.1. Cluster autoscaler parameters

| Parameter | Description |
| --- | --- |
| `podPriorityThreshold` | Specify the priority that a pod must exceed to cause the cluster autoscaler to deploy additional nodes. Enter a 32-bit integer value. The `podPriorityThreshold` value is compared to the value of the `PriorityClass` that you assign to each pod. |
| `maxNodesTotal` | Specify the maximum number of nodes to deploy. This value is the total number of machines that are deployed in your cluster, not just the ones that the autoscaler controls. Ensure that this value is large enough to account for all of your control plane and compute machines and the total number of replicas that you specify in your `MachineAutoscaler` resources. |
| `cores.min` | Specify the minimum number of cores to deploy in the cluster. |
| `cores.max` | Specify the maximum number of cores to deploy in the cluster. |
| `memory.min` | Specify the minimum amount of memory, in GiB, in the cluster. |
| `memory.max` | Specify the maximum amount of memory, in GiB, in the cluster. |
| `gpus.type` | Optional: To configure the cluster autoscaler to deploy GPU-enabled nodes, specify a `type` value. This value must match the value of the `spec.template.spec.metadata.labels[cluster-api/accelerator]` label in the machine set that manages the GPU-enabled nodes of that type. For example, this value might be `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs. For more information, see "Labeling GPU machine sets for the cluster autoscaler". |
| `gpus.min` | Specify the minimum number of GPUs of the specified type to deploy in the cluster. |
| `gpus.max` | Specify the maximum number of GPUs of the specified type to deploy in the cluster. |
| `logVerbosity` | Specify the logging verbosity level between `0` and `10`. The following log level thresholds are provided for guidance:  * `1`: (Default) Basic information about changes. * `4`: Debug-level verbosity for troubleshooting typical issues. * `9`: Extensive, protocol-level debugging information.  If you do not specify a value, the default value of `1` is used. |
| `scaleDown` | In this section, you can specify the period to wait for each action by using any valid [ParseDuration](https://golang.org/pkg/time/#ParseDuration) interval, including `ns`, `us`, `ms`, `s`, `m`, and `h`. |
| `scaleDown.cordonNodeBeforeTerminating` | Optional: Specify whether the cluster autoscaler should cordon a node before removing that node by using one of the following values:  * `Enabled`: The cluster autoscaler cordons the node before draining any pods and removing that node. * `Disabled`: The cluster autoscaler does not cordon the node before draining any pods and removing that node. This is the default. |
| `scaleDown.enabled` | Specify whether the cluster autoscaler can remove unnecessary nodes. |
| `scaleDown.delayAfterAdd` | Optional: Specify the period to wait before deleting a node after a node has recently been *added*. If you do not specify a value, the default value of `10m` is used. |
| `scaleDown.delayAfterDelete` | Optional: Specify the period to wait before deleting a node after a node has recently been *deleted*. If you do not specify a value, the default value of `0s` is used. |
| `scaleDown.delayAfterFailure` | Optional: Specify the period to wait before deleting a node after a scale down failure occurred. If you do not specify a value, the default value of `3m` is used. |
| `scaleDown.unneededTime` | Optional: Specify a period of time before an unnecessary node is eligible for deletion. If you do not specify a value, the default value of `10m` is used. |
| `scaleDown.utilizationThreshold` | Optional: Specify the *node utilization level*. Nodes below this utilization level are eligible for deletion.  The node utilization level is the sum of the requested resources divided by the allocated resources for the node, and must be a value greater than `"0"` but less than `"1"`. If you do not specify a value, the cluster autoscaler uses a default value of `"0.5"`, which corresponds to 50% utilization. You must express this value as a string. |
| `scaleUp` | In this section, you can specify the period to wait before recognizing newly pending pods by using any valid [ParseDuration](https://golang.org/pkg/time/#ParseDuration) interval, including `ns`, `us`, `ms`, `s`, `m`, and `h`. |
| `scaleUp.newPodScaleUpDelay` | Optional: Specify the period to ignore a new unschedulable pod before adding a new node. If you do not specify a value, the default value of `0s` is used. |
| `expanders` | Optional: Specify any expanders that you want the cluster autoscaler to use. The following values are valid:  * `LeastWaste`: Selects the machine set that minimizes the idle CPU after scaling. If multiple machine sets would yield the same amount of idle CPU, the selection minimizes unused memory. * `Priority`: Selects the machine set with the highest user-assigned priority. To use this expander, you must create a config map that defines the priority of your machine sets. For more information, see "Configuring a priority expander for the cluster autoscaler." * `Random`: (Default) Selects the machine set randomly.  If you do not specify a value, the default value of `Random` is used.  You can specify multiple expanders by using the `[LeastWaste, Priority]` format. The cluster autoscaler applies each expander according to the specified order.  In the `[LeastWaste, Priority]` example, the cluster autoscaler first evaluates according to the `LeastWaste` criteria. If more than one machine set satisfies the `LeastWaste` criteria equally well, the cluster autoscaler then evaluates according to the `Priority` criteria. If more than one machine set satisfies all of the specified expanders equally well, the cluster autoscaler selects one to use at random. |

Show more

Note

When performing a scaling operation, the cluster autoscaler remains within the ranges set in the `ClusterAutoscaler` resource definition, such as the minimum and maximum number of cores to deploy or the amount of memory in the cluster. However, the cluster autoscaler does not correct the current values in your cluster to be within those ranges.

The minimum and maximum CPUs, memory, and GPU values are determined by calculating those resources on all nodes in the cluster, even if the cluster autoscaler does not manage the nodes. For example, the control plane nodes are considered in the total memory in the cluster, even though the cluster autoscaler does not manage the control plane nodes.

#### [7.1.5. Configuring a priority expander for the cluster autoscaler](#cluster-autoscaler-config-priority-expander_applying-autoscaling) Copy linkLink copied to clipboard!

Configure a priority expander to control which machine set expands when the cluster autoscaler increases the size of the cluster. You can create a priority expander config map by listing priority values and regular expressions that define machine sets.

**Prerequisites**

* You have deployed an OpenShift Container Platform cluster that uses the Machine API.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. List the compute machine sets on your cluster by running the following command:

   ```
   $ oc get machinesets.machine.openshift.io
   ```

   **Example output**

   ```
   NAME                                        DESIRED   CURRENT   READY   AVAILABLE   AGE
   archive-agl030519-vplxk-worker-us-east-1c   1         1         1       1           25m
   fast-01-agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
   fast-02-agl030519-vplxk-worker-us-east-1a   1         1         1       1           55m
   fast-03-agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
   fast-04-agl030519-vplxk-worker-us-east-1b   1         1         1       1           55m
   prod-01-agl030519-vplxk-worker-us-east-1a   1         1         1       1           33m
   prod-02-agl030519-vplxk-worker-us-east-1c   1         1         1       1           33m
   ```
2. Using regular expressions, construct one or more patterns that match the name of any compute machine set that you want to set a priority level for.

   For example, use the regular expression pattern `*fast*` to match any compute machine set that includes the string `fast` in its name.
3. Create a `cluster-autoscaler-priority-expander.yml` YAML file that defines a config map similar to the following:

   ```
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: cluster-autoscaler-priority-expander
     namespace: openshift-machine-api
   data:
     priorities: |-
       10:
         - .*fast.*
         - .*archive.*
       40:
         - .*prod.*
   ```

   Define the priority of your machine sets. The `priorities` values must be positive integers. The cluster autoscaler uses higher-value priorities before lower-value priorities. For each priority level, specify the regular expressions that correspond to the machine sets you want to use.
4. Create the config map by running the following command:

   ```
   $ oc create configmap cluster-autoscaler-priority-expander \
     --from-file=<location_of_config_map_file>/cluster-autoscaler-priority-expander.yml
   ```

**Verification**

* Review the config map by running the following command:

  ```
  $ oc get configmaps cluster-autoscaler-priority-expander -o yaml
  ```

**Next steps**

* To use the priority expander, ensure that the `ClusterAutoscaler` resource definition is configured to use the `expanders: ["Priority"]` parameter.

#### [7.1.6. Labeling GPU machine sets for the cluster autoscaler](#machineset-label-gpu-autoscaler_applying-autoscaling) Copy linkLink copied to clipboard!

Label your machine sets to indicate which machines the cluster autoscaler can use for GPU-enabled nodes. Applying the accelerator label helps ensure that the autoscaler deploys the correct resources for your GPU workloads.

**Prerequisites**

* Your cluster uses a cluster autoscaler.

**Procedure**

* On the machine set that you want to create machines for the cluster autoscaler to use to deploy GPU-enabled nodes, add a `cluster-api/accelerator` label:

  ```
  apiVersion: machine.openshift.io/v1beta1
  kind: MachineSet
  metadata:
    name: machine-set-name
  spec:
    template:
      spec:
        metadata:
          labels:
            cluster-api/accelerator: <accelerator_name>
  ```

  where:

  `<accelerator_name>`
  :   Specifies a label of your choice that consists of alphanumeric characters, `-`, `_`, or `.` and starts and ends with an alphanumeric character. For example, you might use `nvidia-t4` to represent Nvidia T4 GPUs, or `nvidia-a10g` for A10G GPUs.

      Note

      You must specify the value of this label for the `spec.resourceLimits.gpus.type` parameter in your `ClusterAutoscaler` CR. For more information, see "Cluster autoscaler resource definition".

#### [7.1.7. Deploying a cluster autoscaler](#ClusterAutoscaler-deploying_applying-autoscaling) Copy linkLink copied to clipboard!

To deploy a cluster autoscaler, you create an instance of the `ClusterAutoscaler` resource.

**Procedure**

1. Create a YAML file for a `ClusterAutoscaler` resource that contains the custom resource definition.
2. Create the custom resource in the cluster by running the following command:

   ```
   $ oc create -f <filename>.yaml
   ```

   where:

   `<filename>`
   :   Specifies the name of the YAML file you created.

### [7.2. About the machine autoscaler](#machine-autoscaler-about_applying-autoscaling) Copy linkLink copied to clipboard!

The machine autoscaler adjusts the number of Machines in the compute machine sets that you deploy in an OpenShift Container Platform cluster. You can scale both the default `worker` compute machine set and any other compute machine sets that you create. The machine autoscaler makes more Machines when the cluster runs out of resources to support more deployments. Any changes to the values in `MachineAutoscaler` resources, such as the minimum or maximum number of instances, are immediately applied to the compute machine set they target.

Important

You must deploy a machine autoscaler for the cluster autoscaler to scale your machines. The cluster autoscaler uses the annotations on compute machine sets that the machine autoscaler sets to determine the resources that it can scale. If you define a cluster autoscaler without also defining machine autoscalers, the cluster autoscaler will never scale your cluster.

#### [7.2.1. Configuring machine autoscalers](#configuring-machineautoscaler_applying-autoscaling) Copy linkLink copied to clipboard!

After you deploy the cluster autoscaler, deploy `MachineAutoscaler` resources that reference the compute machine sets that are used to scale the cluster.

Important

You must deploy at least one `MachineAutoscaler` resource after you deploy the `ClusterAutoscaler` resource.

Note

You must configure separate resources for each compute machine set. Remember that compute machine sets are different in each region, so consider whether you want to enable machine scaling in multiple regions. The compute machine set that you scale must have at least one machine in it.

##### [7.2.1.1. Machine autoscaler resource definition](#machine-autoscaler-cr_applying-autoscaling) Copy linkLink copied to clipboard!

This `MachineAutoscaler` resource definition shows the parameters and sample values for the machine autoscaler.

```
apiVersion: "autoscaling.openshift.io/v1beta1"
kind: "MachineAutoscaler"
metadata:
  name: "worker-us-east-1a"
  namespace: "openshift-machine-api"
spec:
  minReplicas: 1
  maxReplicas: 12
  scaleTargetRef:
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineSet
    name: worker-us-east-1a
```

where:

<name>
:   Specify the machine autoscaler name. To make it easier to identify which compute machine set this machine autoscaler scales, specify or include the name of the compute machine set to scale. The compute machine set name takes the following form: `<clusterid>-<machineset>-<region>`.

<minReplicas>
:   Specify the minimum number machines of the specified type that must remain in the specified zone after the cluster autoscaler initiates cluster scaling. If running in AWS, Google Cloud, Azure, RHOSP, or vSphere, this value can be set to `0`. For other providers, do not set this value to `0`.

    You can save on costs by setting this value to `0` for use cases such as running expensive or limited-usage hardware that is used for specialized workloads, or by scaling a compute machine set with extra large machines. The cluster autoscaler scales the compute machine set down to zero if the machines are not in use.

    Important

    Do not set the `spec.minReplicas` value to `0` for the three compute machine sets that are created during the OpenShift Container Platform installation process for an installer provisioned infrastructure.

<maxReplicas>
:   Specify the maximum number machines of the specified type that the cluster autoscaler can deploy in the specified zone after it initiates cluster scaling. Ensure that the `maxNodesTotal` value in the `ClusterAutoscaler` resource definition is large enough to allow the machine autoscaler to deploy this number of machines.

<scaleTargetRef>
:   In this section, provide values that describe the existing compute machine set to scale.

<kind>
:   The `kind` parameter value is always `MachineSet`.

<name>
:   The `name` value must match the name of an existing compute machine set, as shown in the `metadata.name` parameter value.

#### [7.2.2. Deploying a machine autoscaler](#MachineAutoscaler-deploying_applying-autoscaling) Copy linkLink copied to clipboard!

To deploy a machine autoscaler, you create an instance of the `MachineAutoscaler` resource.

**Procedure**

1. Create a YAML file for a `MachineAutoscaler` resource that contains the custom resource definition.
2. Create the custom resource in the cluster by running the following command:

   ```
   $ oc create -f <filename>.yaml
   ```

   where:

   `<filename>`
   :   Specifies the name of the YAML file you created.

### [7.3. Disabling a machine autoscaler](#deleting-machine-autoscaler_applying-autoscaling) Copy linkLink copied to clipboard!

To disable a machine autoscaler, you delete the corresponding `MachineAutoscaler` custom resource (CR).

Note

Disabling a machine autoscaler does not disable the cluster autoscaler. To disable the cluster autoscaler, follow the instructions in "Disabling the cluster autoscaler".

**Procedure**

1. List the `MachineAutoscaler` CRs for the cluster by running the following command:

   ```
   $ oc get MachineAutoscaler -n openshift-machine-api
   ```

   **Example output**

   ```
   NAME                 REF KIND     REF NAME             MIN   MAX   AGE
   compute-us-east-1a   MachineSet   compute-us-east-1a   1     12    39m
   compute-us-west-1a   MachineSet   compute-us-west-1a   2     4     37m
   ```
2. Optional: Create a YAML file backup of the `MachineAutoscaler` CR by running the following command:

   ```
   $ oc get MachineAutoscaler/<machine_autoscaler_name> \
     -n openshift-machine-api \
     -o yaml> <machine_autoscaler_name_backup>.yaml
   ```

   where:

   <machine\_autoscaler\_name\_backup>
   :   Specifies the file name in which to store the backup.
3. Delete the `MachineAutoscaler` CR by running the following command:

   ```
   $ oc delete MachineAutoscaler/<machine_autoscaler_name> -n openshift-machine-api
   ```

   **Example output**

   ```
   machineautoscaler.autoscaling.openshift.io "compute-us-east-1a" deleted
   ```

**Verification**

* To verify that the machine autoscaler is disabled, run the following command:

  ```
  $ oc get MachineAutoscaler -n openshift-machine-api
  ```

  The disabled machine autoscaler does not appear in the list of machine autoscalers.

**Next steps**

* If you need to re-enable the machine autoscaler, use the `<machine_autoscaler_name_backup>.yaml` backup file and follow the instructions in "Deploying a machine autoscaler".

### [7.4. Disabling the cluster autoscaler](#deleting-cluster-autoscaler_applying-autoscaling) Copy linkLink copied to clipboard!

To disable the cluster autoscaler, you delete the corresponding `ClusterAutoscaler` resource.

Note

Disabling the cluster autoscaler disables autoscaling on the cluster, even if the cluster has existing machine autoscalers.

**Procedure**

1. List the `ClusterAutoscaler` resource for the cluster by running the following command:

   ```
   $ oc get ClusterAutoscaler
   ```

   **Example output**

   ```
   NAME      AGE
   default   42m
   ```
2. Optional: Create a YAML file backup of the `ClusterAutoscaler` CR by running the following command:

   ```
   $ oc get ClusterAutoscaler/default \
     -o yaml> <cluster_autoscaler_backup_name>.yaml
   ```

   where:

   <cluster\_autoscaler\_backup\_name>
   :   Specifies the file name in which to store the backup.
3. Delete the `ClusterAutoscaler` CR by running the following command:

   ```
   $ oc delete ClusterAutoscaler/default
   ```

   **Example output**

   ```
   clusterautoscaler.autoscaling.openshift.io "default" deleted
   ```

**Verification**

* To verify that the cluster autoscaler is disabled, run the following command:

  ```
  $ oc get ClusterAutoscaler
  ```

  **Expected output**

  ```
  No resources found
  ```

**Next steps**

* Disabling the cluster autoscaler by deleting the `ClusterAutoscaler` CR prevents the cluster from autoscaling but does not delete any existing machine autoscalers on the cluster. To clean up unneeded machine autoscalers, see "Disabling a machine autoscaler".
* If you need to re-enable the cluster autoscaler, use the `<cluster_autoscaler_name_backup>.yaml` backup file and follow the instructions in "Deploying a cluster autoscaler".

## [Chapter 8. Creating infrastructure machine sets](#creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

To reduce subscription costs, you can use infrastructure machine sets to create machines that host only infrastructure components, such as the default router, the integrated container image registry, cluster metrics, and monitoring. These infrastructure machines are not counted toward the total number of subscriptions that are required to run the environment.

For information about infrastructure nodes and which components can run on infrastructure nodes, see the "Red Hat OpenShift control plane and infrastructure nodes" section in the OpenShift sizing and subscription guide for enterprise Kubernetes document.

To create an infrastructure node, see "Creating a compute machine set", "Creating an infrastructure node", or "Creating an infrastructure node". Use the sample compute machine set for your cloud to deploy an infrastructure machine set. Modify the sample configuration file with the details of your environment.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

### [8.1. OpenShift Container Platform infrastructure components](#infrastructure-components_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

To reduce subscription costs, you can review the following information to understand which components you can move to an infrastructure node. Components that you move to an infrastructure node do not need to be accounted for during sizing.

Each self-managed Red Hat OpenShift subscription includes entitlements for OpenShift Container Platform and other OpenShift-related components. These entitlements are included for running OpenShift Container Platform control plane and infrastructure workloads and do not need to be accounted for during sizing.

To qualify as an infrastructure node and use the included entitlement, only components that are supporting the cluster, and not part of an end-user application, can run on those instances. Examples include the following components:

* Kubernetes and OpenShift Container Platform control plane services
* The default router
* The integrated container image registry
* The HAProxy-based Ingress Controller
* The cluster metrics collection, or monitoring service, including components for monitoring user-defined projects
* Cluster aggregated logging
* Red Hat Quay
* Red Hat OpenShift Data Foundation
* Red Hat Advanced Cluster Management for Kubernetes
* Red Hat Advanced Cluster Security for Kubernetes
* Red Hat OpenShift GitOps
* Red Hat OpenShift Pipelines
* Red Hat OpenShift Service Mesh

Any node that runs any other container, pod, or component is a worker node that your subscription must cover.

For information about infrastructure nodes and which components can run on infrastructure nodes, see the "Red Hat OpenShift control plane and infrastructure nodes" section in the OpenShift sizing and subscription guide for enterprise Kubernetes document.

### [8.2. Sample YAML for a compute machine set custom resource on AWS](#machineset-yaml-aws_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

The sample YAML defines a compute machine set that runs in the `us-east-1a` Amazon Web Services (AWS) Local Zone and creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`.

The sample YAML specifies a taint to prevent user workloads from being scheduled on `infra` nodes.

After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).

In this sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<infra>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-infra-<zone>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<zone>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: infra
        machine.openshift.io/cluster-api-machine-type: infra
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<zone>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          ami:
            id: ami-046fe691f52a953f9
          apiVersion: machine.openshift.io/v1beta1
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
          instanceType: m6i.large
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
            - name: <custom_tag_name>
              value: <custom_tag_value>
          userDataSecret:
            name: worker-user-data
      taints:
        - key: node-role.kubernetes.io/infra
          effect: NoSchedule
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`<infrastructure_id>-infra-<zone>`
:   Specifies the infrastructure ID, `infra` role node label, and zone.

`<infra>`
:   Specifies the `infra` role node label.

`<zone>`
:   Specifies the zone name, for example, `us-east-1a`.

`<region>`
:   Specifies the region, for example, `us-east-1`.

`<infrastructure_id>-subnet-private-<zone>`
:   Specifies the infrastructure ID and zone.

`<custom_tag_name>`
:   Optional: Specifies custom tag data for your cluster. For example, you might add an admin contact email address by specifying a `name:value` pair of `Email:admin-email@example.com`.

    Note

    Custom tags can also be specified during installation in the `install-config.yaml` file. If the `install-config.yaml` file and the machine set include a tag with the same `name` data, the value for the tag from the machine set takes priority over the value for the tag in the `install-config.yaml` file.

Note

The `spec.template.spec.providerSpec.value.ami.id` stanza specifies a valid Red Hat Enterprise Linux CoreOS (RHCOS) Amazon Machine Image (AMI) for your AWS zone for your OpenShift Container Platform nodes. If you want to use an AWS Marketplace image, you must complete the OpenShift Container Platform subscription from the [AWS Marketplace](https://aws.amazon.com/marketplace/fulfillment?productId=59ead7de-2540-4653-a8b0-fa7926d5c845) to obtain an AMI ID for your region.

```
$ oc -n openshift-machine-api \
    -o jsonpath='{.spec.template.spec.providerSpec.value.ami.id}{"\n"}' \
    get machineset/<infrastructure_id>-<role>-<zone>
```

Machine sets running on AWS support non-guaranteed Spot Instances. You can save on costs by using Spot Instances at a lower price compared to On-Demand Instances on AWS. For more information, see "Machine sets that deploy machines as Spot Instances".

### [8.3. Sample YAML for a compute machine set custom resource on Azure](#machineset-yaml-azure_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

You can define a machine set YAML to provision nodes by specifying parameters such as `vmSize` and `image`. You can use this to automate and scale infrastructure consistently, to ensure compute nodes meet specific workload requirements within the cluster.

The sample YAML defines a compute machine set that runs in the `1` Microsoft Azure zone in a region and creates nodes that are labeled with ifdef::infra[`node-role.kubernetes.io/infra: ""`. The YAML specifies a taint to prevent user workloads from being scheduled on infra nodes. After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `infra` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: infra
    machine.openshift.io/cluster-api-machine-type: infra
  name: <infrastructure_id>-infra-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<region>
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: infra
        machine.openshift.io/cluster-api-machine-type: infra
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<region>
    spec:
      metadata:
        creationTimestamp: null
        labels:
          machine.openshift.io/cluster-api-machineset: <machineset_name>
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image:
            offer: ""
            publisher: ""
            resourceID: /resourceGroups/<infrastructure_id>-rg/providers/Microsoft.Compute/galleries/gallery_<infrastructure_id>/images/<infrastructure_id>-gen2/versions/latest
            sku: ""
            version: ""
          internalLoadBalancer: ""
          kind: AzureMachineProviderSpec
          location: <region>
          managedIdentity: <infrastructure_id>-identity
          metadata:
            creationTimestamp: null
          natRule: null
          networkResourceGroup: ""
          osDisk:
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Linux
          publicIP: false
          publicLoadBalancer: ""
          resourceGroup: <infrastructure_id>-rg
          sshPrivateKey: ""
          sshPublicKey: ""
          tags:
            <custom_tag_name_1>: <custom_tag_value_1>
            <custom_tag_name_2>: <custom_tag_value_2>
          subnet: <infrastructure_id>-<role>-subnet
          userDataSecret:
            name: worker-user-data
          vmSize: Standard_D4s_v3
          vnet: <infrastructure_id>-vnet
          zone: "1"
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

    You can obtain the subnet by running the following command:

    ```
    $  oc -n openshift-machine-api \
        -o jsonpath='{.spec.template.spec.providerSpec.value.subnet}{"\n"}' \
        get machineset/<infrastructure_id>-worker-centralus1
    ```

    You can obtain the vnet by running the following command:

    ```
    $  oc -n openshift-machine-api \
        -o jsonpath='{.spec.template.spec.providerSpec.value.vnet}{"\n"}' \
        get machineset/<infrastructure_id>-worker-centralus1
    ```

Note

The value of the `metadata.labels.machine.openshift.io/cluster-api-machine-role` parameter specifies the `infra` node label.

`<infrastructure_id>-infra-<region>`
:   Specifies the infrastructure ID, `infra` node label, and region.

Note

The value of the `spec.template.spec.providerSpec.value.image` parameter specifies the image details for your compute machine set. If you want to use an Azure Marketplace image, see "Using the Azure Marketplace offering".

The value of the `spec.template.spec.providerSpec.value.image.resourceID` parameter specifies an image that is compatible with your instance type. The Hyper-V generation V2 images created by the installation program have a `-gen2` suffix, while V1 images have the same name without the suffix.

The value of the `spec.template.spec.providerSpec.value.location` parameter specifies the region to place machines on.

`<custom_tag_name_1>`
:   Optional: Specifies custom tags in your machine set. Provide the tag name in `<custom_tag_name>` field and the corresponding tag value in `<custom_tag_value>` field.

Note

The value of the `spec.template.spec.providerSpec.value.zone` parameter specifies the zone within your region to place machines on. Ensure that your region supports the zone that you specify. If your region supports availability zones, you must specify the zone. Specifying the zone avoids volume node affinity failure when a pod requires a persistent volume attachment. To do this, you can create a compute machine set for each zone in the same region.

### [8.4. Sample YAML for a compute machine set custom resource on Azure Stack Hub](#machineset-yaml-azure-stack-hub_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

You can create a machine set on Microsoft Azure Stack Hub. By defining a YAML configuration with specific cluster IDs and provider details, you can automate the provisioning of specialized nodes.

The Microsoft Azure sample YAML defines a compute machine set that runs in the `1` Azure zone in a region and creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`. The sample YAML specifies a taint to prevent user workloads from being scheduled on infra nodes. After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<infra>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <infra>
    machine.openshift.io/cluster-api-machine-type: <infra>
  name: <infrastructure_id>-infra-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<region>
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <infra>
        machine.openshift.io/cluster-api-machine-type: <infra>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra-<region>
    spec:
      metadata:
        creationTimestamp: null
        labels:
          node-role.kubernetes.io/infra: ""
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          availabilitySet: <availability_set>
          credentialsSecret:
            name: azure-cloud-credentials
            namespace: openshift-machine-api
          image:
            offer: ""
            publisher: ""
            resourceID: /resourceGroups/<infrastructure_id>-rg/providers/Microsoft.Compute/images/<infrastructure_id>
            sku: ""
            version: ""
          internalLoadBalancer: ""
          kind: AzureMachineProviderSpec
          location: <region>
          managedIdentity: <infrastructure_id>-identity
          metadata:
            creationTimestamp: null
          natRule: null
          networkResourceGroup: ""
          osDisk:
            diskSizeGB: 128
            managedDisk:
              storageAccountType: Premium_LRS
            osType: Linux
          publicIP: false
          publicLoadBalancer: ""
          resourceGroup: <infrastructure_id>-rg
          sshPrivateKey: ""
          sshPublicKey: ""
          subnet: <infrastructure_id>-<role>-subnet
          userDataSecret:
            name: worker-user-data
          vmSize: Standard_DS4_v2
          vnet: <infrastructure_id>-vnet
          zone: "1"
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift Container Platform CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

    You can obtain the subnet by running the following command:

    ```
    $  oc -n openshift-machine-api \
        -o jsonpath='{.spec.template.spec.providerSpec.value.subnet}{"\n"}' \
        get machineset/<infrastructure_id>-worker-centralus1
    ```

    You can obtain the vnet by running the following command:

    ```
    $  oc -n openshift-machine-api \
        -o jsonpath='{.spec.template.spec.providerSpec.value.vnet}{"\n"}' \
        get machineset/<infrastructure_id>-worker-centralus1
    ```

`<infra>`
:   Specifies the `<infra>` node label.

`<infrastructure_id>-infra-<region>`
:   Specifies the infrastructure ID, `<infra>` node label, and region.

`<region>`
:   Specifies the region to place machines on.

    Note

    The `spec.template.spec.providerSpec.value.zone` specifies the zone within your region to place machines on. Be sure that your region supports the zone that you specify.

`<availability_set>`
:   Specifies the availability set for the cluster.

`<image>`
:   Specifies the boot image to use. You should use the use the latest image when adding a new machine set.

Note

Machine sets running on Azure Stack Hub do not support non-guaranteed Spot VMs.

### [8.5. Sample YAML for a compute machine set custom resource on IBM Cloud](#machineset-yaml-ibm-cloud_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

You can use the sample YAML file to automate the provisioning of compute or infrastructure nodes within a specific Virtual Private Cloud (VPC). The sample YAML defines a compute machine set that runs in a specified IBM Cloud® zone in a region and creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<infra>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: <infra>
    machine.openshift.io/cluster-api-machine-type: <infra>
  name: <infrastructure_id>-<infra>-<region>
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<infra>-<region>
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <infra>
        machine.openshift.io/cluster-api-machine-type: <infra>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<infra>-<region>
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          apiVersion: ibmcloudproviderconfig.openshift.io/v1beta1
          credentialsSecret:
            name: ibmcloud-credentials
          image: <infrastructure_id>-rhcos
          kind: IBMCloudMachineProviderSpec
          primaryNetworkInterface:
              securityGroups:
              - <infrastructure_id>-sg-cluster-wide
              - <infrastructure_id>-sg-openshift-net
              subnet: <infrastructure_id>-subnet-compute-<zone>
          profile: <instance_profile>
          region: <region>
          resourceGroup: <resource_group>
          userDataSecret:
              name: <role>-user-data
          vpc: <vpc_name>
          zone: <zone>
        taints:
        - key: node-role.kubernetes.io/infra
          effect: NoSchedule
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`<infra>`
:   Specifies the `<infra>` node label.

`<infrastructure_id>-<infra>-<region>`
:   Specifies the infrastructure ID, `<infra>` node label, and region.

`<infrastructure_id>-rhcos`
:   Specifies the custom Red Hat Enterprise Linux CoreOS (RHCOS) image to use as a boot image for your nodes. You should use the use the latest image when adding a new machine set.

`<infrastructure_id>-subnet-compute-<zone>`
:   Specifies the infrastructure ID and zone within your region to place machines on. Be sure that your region supports the zone that you specify.

`<instance_profile>`
:   Specifies the [IBM Cloud® instance profile](https://cloud.ibm.com/docs/vpc?topic=vpc-profiles&interface=ui).

`<region>`
:   Specifies the region to place machines on.

`<resource_group>`
:   Specifies the resource group that machine resources are placed in. This is either an existing resource group specified at installation time, or an installer-created resource group named based on the infrastructure ID.

`<vpc_name>`
:   Specifies the VPC name.

`<zone>`
:   Specifies the zone within your region to place machines on. Be sure that your region supports the zone that you specify.

`taints`
:   Specifies the taint to prevent user workloads from being scheduled on infra nodes.

    Note

    After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).

### [8.6. Sample YAML for a compute machine set custom resource on Google Cloud](#machineset-yaml-gcp_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

The sample YAML defines a compute machine set for Google Cloud, enabling the automated provisioning of nodes within a specific VPC. When you apply this configuration by using the OpenShift Container Platform CLI, you can ensure consistent scaling, scheduling, and infrastructure ID labeling for compute resources in your cluster.

The sample YAML defines a compute machine set that runs in Google Cloud and creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`, where `infra` is the node label to add.

#### [8.6.1. Values obtained by using the OpenShift CLI](#cpmso-yaml-provider-spec-gcp-oc_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

In the following example, you can obtain some of the values for your cluster by using the OpenShift Container Platform CLI.

Infrastructure ID
:   The `<infrastructure_id>` string is the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

Image path
:   The `<path_to_image>` string is the path to the image that was used to create the disk. If you have the OpenShift CLI installed, you can obtain the path to the image by running the following command:

    ```
    $ oc -n openshift-machine-api \
      -o jsonpath='{.spec.template.spec.providerSpec.value.disks[0].image}{"\n"}' \
      get machineset/<infrastructure_id>-worker-a
    ```

**Sample Google Cloud `MachineSet` values**

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-w-a
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-w-a
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <infra>
        machine.openshift.io/cluster-api-machine-type: <infra>
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-w-a
    spec:
      metadata:
        labels:
          node-role.kubernetes.io/infra: ""
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
            image: <path_to_image>
            labels: null
            sizeGb: 128
            type: pd-ssd
          gcpMetadata:
          - key: <custom_metadata_key>
            value: <custom_metadata_value>
          kind: GCPMachineProviderSpec
          machineType: n1-standard-4
          metadata:
            creationTimestamp: null
          networkInterfaces:
          - network: <infrastructure_id>-network
            subnetwork: <infrastructure_id>-worker-subnet
          projectID: <project_name>
          region: us-central1
          serviceAccounts:
          - email: <infrastructure_id>-w@<project_name>.iam.gserviceaccount.com
            scopes:
            - https://www.googleapis.com/auth/cloud-platform
          tags:
            - <infrastructure_id>-worker
          userDataSecret:
            name: worker-user-data
          zone: us-central1-a
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster.

`<infra>`
:   Specifies the `<infra>` node label.

`<path_to_image>`
:   Specifies the path to the image that is used as a boot image in current compute machine sets. You should use the use the latest image when adding a new machine set. To use a Google Cloud Marketplace image, specify the offer to use:

    * OpenShift Container Platform: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-ocp-413-x86-64-202305021736`
    * OpenShift Platform Plus: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-opp-413-x86-64-202305021736`
    * OpenShift Kubernetes Engine: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-oke-413-x86-64-202305021736`

`<gcpMetadata>`
:   Optional: Specifies the custom metadata in the form of a `key:value` pair. For example use cases, see the Google Cloud documentation for [setting custom metadata](https://cloud.google.com/compute/docs/metadata/setting-custom-metadata).

`<project_name>`
:   Specifies the name of the Google Cloud project that you use for your cluster.

`<serviceAccounts>`
:   Specifies a single service account. Multiple service accounts are not supported.

`<taints>`
:   Specifies a taint to prevent user workloads from being scheduled on infra nodes.

Note

After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).

Machine sets running on Google Cloud support non-guaranteed preemptible VM instances. You can save on costs by using preemptible VM instances at a lower price compared to normal instances on Google Cloud. You can configure preemptible VM instances by adding `preemptible` to the `MachineSet` YAML file.

### [8.7. Sample YAML for a compute machine set custom resource on Nutanix](#machineset-yaml-nutanix_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

You can use a YAML file to automate node provisioning and ensure workloads are scheduled correctly based on role and infrastructure requirements.

The sample YAML shows how to define a Nutanix compute MachineSet for your cluster. It explains how to configure roles, labels, sizing, networking, and boot settings so new nodes are created consistently.

The sample YAML defines a Nutanix compute machine set that creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`.

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<infra>` is the node label to add.

#### [8.7.1. Values obtained by using the OpenShift CLI](#machineset-yaml-nutanix-oc_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

In the following example, you can obtain some of the values for your cluster by using the OpenShift CLI (`oc`).

Infrastructure ID
:   The `<infrastructure_id>` string is the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

    ```
    apiVersion: machine.openshift.io/v1beta1
    kind: MachineSet
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: <infra>
        machine.openshift.io/cluster-api-machine-type: <infra>
      name: <infrastructure_id>-<infra>-<zone>
      namespace: openshift-machine-api
      annotations:
        machine.openshift.io/memoryMb: "16384"
        machine.openshift.io/vCPU: "4"
    spec:
      replicas: 3
      selector:
        matchLabels:
          machine.openshift.io/cluster-api-cluster: <infrastructure_id>
          machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<infra>-<zone>
      template:
        metadata:
          labels:
            machine.openshift.io/cluster-api-cluster: <infrastructure_id>
            machine.openshift.io/cluster-api-machine-role: <infra>
            machine.openshift.io/cluster-api-machine-type: <infra>
            machine.openshift.io/cluster-api-machineset: <infrastructure_id>-<infra>-<zone>
        spec:
          metadata:
            labels:
              node-role.kubernetes.io/infra: ""
          providerSpec:
            value:
              apiVersion: machine.openshift.io/v1
              bootType: ""
              categories:
              - key: <category_name>
                value: <category_value>
              cluster:
                type: uuid
                uuid: <cluster_uuid>
              credentialsSecret:
                name: nutanix-credentials
              image:
                name: <infrastructure_id>-rhcos
                type: name
              kind: NutanixMachineProviderConfig
              memorySize: 16Gi
              project:
                type: name
                name: <project_name>
              subnets:
              - type: uuid
                uuid: <subnet_uuid>
              systemDiskSize: 120Gi
              userDataSecret:
                name: <user_data_secret>
              vcpuSockets: 4
              vcpusPerSocket: 1
          taints:
          - key: node-role.kubernetes.io/infra
            effect: NoSchedule
    ```

    where:

    `<infrastructure_id>`
    :   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster.

    `<infra>`
    :   Specifies the `<infra>` node label.

    `<infrastructure_id>-<role>-<zone>`
    :   Specifies the infrastructure ID, `<infra>` node label, and zone.

    `annotations`
    :   Specifies annotations for the cluster autoscaler.

    `bootType`
    :   Specifies the boot type that the compute machines use. For more information about boot types, see [Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment](https://portal.nutanix.com/page/documents/kbs/details?targetId=kA07V000000H3K9SAK). Valid values are `Legacy`, `SecureBoot`, or `UEFI`. The default is `Legacy`.

        Note

        You must use the `Legacy` boot type in OpenShift Container Platform 4.22.

    `<categories>`
    :   Specifies one or more Nutanix Prism categories to apply to compute machines. This stanza requires `key` and `value` parameters for a category key-value pair that exists in Prism Central. For more information about categories, see [Category management](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html).

    `<cluster>`
    :   Specifies a Nutanix Prism Element cluster configuration. In this example, the cluster type is `uuid`, so there is a `uuid` stanza.

    `<infrastructure_id>-rhcos`
    :   Specifies the image to use as a boot image for your nodes. You should use the use the latest image when adding a new machine set.

    `16Gi`
    :   Specifies the amount of memory for the cluster in Gi.

    `project`
    :   Specifies the Nutanix project that you use for your cluster. In this example, the project type is `name`, so there is a `name` stanza.

    `subnets`
    :   Specifies one or more UUID for the Prism Element subnet object. The CIDR IP address prefix for one of the specified subnets must contain the virtual IP addresses that the OpenShift Container Platform cluster uses. A maximum of 32 subnets for each Prism Element failure domain in the cluster is supported. All subnet UUID values must be unique.

    `120Gi`
    :   Specifies the size of the system disk in Gi.

    `<user_data_secret>`
    :   Specifies the name of the secret in the user data YAML file that is in the `openshift-machine-api` namespace. Use the value that installation program populates in the default compute machine set.

    `4`
    :   Specifies the number of vCPU sockets.

    `1`
    :   Specifies the number of vCPUs per socket.

    taints
    :   Specifies a taint to prevent user workloads from being scheduled on infra nodes.

        Note

        After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).

### [8.8. Sample YAML for a compute machine set custom resource on RHOSP](#machineset-yaml-osp_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

To enable the Machine API to automate the scaling and management of compute nodes, define a `MachineSet` resource with Red Hat OpenStack Platform (RHOSP) parameters, for example, image and network IDs.

The sample YAML defines a compute machine set that runs on Red Hat OpenStack Platform (RHOSP) and creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`. It specifies a taint to prevent user workloads from being scheduled on infra nodes. After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).

In the sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `<infra>` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
    machine.openshift.io/cluster-api-machine-role: infra
    machine.openshift.io/cluster-api-machine-type: infra
  name: <infrastructure_id>-infra
  namespace: openshift-machine-api
spec:
  replicas: <number_of_replicas>
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra
  template:
    metadata:
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: infra
        machine.openshift.io/cluster-api-machine-type: infra
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra
    spec:
      metadata:
        creationTimestamp: null
        labels:
          node-role.kubernetes.io/infra: ""
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1alpha1
          cloudName: openstack
          cloudsSecret:
            name: openstack-cloud-credentials
            namespace: openshift-machine-api
          flavor: <nova_flavor>
          image: <glance_image_name_or_location>
          serverGroupID: <optional_UUID_of_server_group>
          kind: OpenstackProviderSpec
          networks:
          - filter: {}
            subnets:
            - filter:
                name: <subnet_name>
                tags: openshiftClusterID=<infrastructure_id>
          primarySubnet: <rhosp_subnet_UUID>
          securityGroups:
          - filter: {}
            name: <infrastructure_id>-worker
          serverMetadata:
            Name: <infrastructure_id>-worker
            openshiftClusterID: <infrastructure_id>
          tags:
          - openshiftClusterID=<infrastructure_id>
          trunk: true
          userDataSecret:
            name: worker-user-data
          availabilityZone: <optional_openstack_availability_zone>
```

where:

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift Container Platform CLI installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`<infrastructure_id>-infra`
:   Specifies the infrastructure ID and `infra` node label.

`<glance_image_name_or_location>`
:   Specifies the image to use as a boot image for your nodes. You should use the latest image when adding a new machine set.

`<optional_UUID_of_server_group>`
:   Sets a server group policy for the `MachineSet` YAML, by entering the value that is returned from [creating a server group](https://access.redhat.com/documentation/en-us/red_hat_openstack_platform/16.0/html/command_line_interface_reference/server#server_group_create). For most deployments, `anti-affinity` or `soft-anti-affinity` policies are recommended.

`<subnet_name>`
:   Specifies a subnet to use.

    Note

    The `spec.template.spec.providerSpec.value.networks` stanza is required for deployments to multiple networks. If deploying to multiple networks, this list must include the network that is used as the `primarySubnet` value.

`<rhosp_subnet_UUID>`
:   Specifies the RHOSP subnet that you want the endpoints of nodes to be published on. Usually, this is the same subnet that is used as the value of `machinesSubnet` in the `install-config.yaml` file.

### [8.9. Sample YAML for a compute machine set custom resource on vSphere](#machineset-yaml-vsphere_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

To enable the Machine API to automate node provisioning on VMware vSphere infrastructure, define a `MachineSet` resource with parameters that are specific to vSphere, for example data center, resource pool, and template.

The sample YAML file defines a compute machine set that runs on vSphere and creates nodes that are labeled with `node-role.kubernetes.io/infra: ""`.

In this sample, `<infrastructure_id>` is the infrastructure ID label that is based on the cluster ID that you set when you provisioned the cluster, and `infra` is the node label to add.

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineSet
metadata:
  creationTimestamp: null
  labels:
    machine.openshift.io/cluster-api-cluster: <infrastructure_id>
  name: <infrastructure_id>-infra
  namespace: openshift-machine-api
spec:
  replicas: 1
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <infrastructure_id>
      machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra
  template:
    metadata:
      creationTimestamp: null
      labels:
        machine.openshift.io/cluster-api-cluster: <infrastructure_id>
        machine.openshift.io/cluster-api-machine-role: infra
        machine.openshift.io/cluster-api-machine-type: infra
        machine.openshift.io/cluster-api-machineset: <infrastructure_id>-infra
    spec:
      metadata:
        creationTimestamp: null
        labels:
          node-role.kubernetes.io/infra: ""
      providerSpec:
        value:
          apiVersion: machine.openshift.io/v1beta1
          credentialsSecret:
            name: vsphere-cloud-credentials
          dataDisks:
          - name: "<disk_name>"
            provisioningMode: "<mode>"
            sizeGiB: 20
          diskGiB: 120
          kind: VSphereMachineProviderSpec
          memoryMiB: 8192
          metadata:
            creationTimestamp: null
          network:
            devices:
            - networkName: "<vm_network_name>"
          numCPUs: 4
          numCoresPerSocket: 1
          snapshot: ""
          template: <vm_template_name>
          userDataSecret:
            name: worker-user-data
          workspace:
            datacenter: <vcenter_data_center_name>
            datastore: <vcenter_datastore_name>
            folder: <vcenter_vm_folder_path>
            resourcepool: <vsphere_resource_pool>
            server: <vcenter_server_ip>
      taints:
      - key: node-role.kubernetes.io/infra
        effect: NoSchedule
```

where

`<infrastructure_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

```
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```

`<infrastructure_id>-infra`
:   Specifies the infrastructure ID and `infra` node label.

`infra`
:   Specifies the `infra` node label.

`<disk_name>`
:   Specifies one or more data disk definitions. For more information, see "Configuring data disks by using machine sets".

`<image_name>`
:   Specifies the image to use as a boot image for your nodes.

`<vm_network_name>`
:   Specifies the vSphere VM network to deploy the compute machine set to. This VM network must be where other compute machines reside in the cluster.

`<vm_template_name>`
:   Specifies the vSphere VM template to use as a boot image for your nodes, such as `user-5ddjd-rhcos`. You should use a template with the latest OpenShift Container Platform image when adding a new machine set.

`<vcenter_data_center_name>`
:   Specifies the vCenter datacenter to deploy the compute machine set on.

`<vcenter_datastore_name>`
:   Specifies the vCenter datastore to deploy the compute machine set on.

`<vcenter_vm_folder_path>`
:   Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`.

`<vsphere_resource_pool>`
:   Specifies the vSphere resource pool for your VMs.

`<vcenter_server_ip>`
:   Specifies the vCenter server IP or fully qualified domain name.

`taints`
:   Specifies a taint to prevent user workloads from being scheduled on infra nodes.

    Note

    After adding the `NoSchedule` taint on the infrastructure node, existing DNS pods running on that node are marked as `misscheduled`. You must either delete or [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171).

### [8.10. Creating a compute machine set](#machineset-creating_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

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

### [8.11. Creating an infrastructure node](#creating-an-infra-node_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

To reduce subscription costs, you can use labels to configure compute nodes as infrastructure nodes, where you can move infrastructure resources.

After you create the infrastructure nodes, you can move appropriate workloads to those nodes by using taints and tolerations.

You can optionally create a default cluster-wide node selector. The default node selector is applied to pods created in all namespaces and creates an intersection with any existing node selectors on a pod, which additionally constrains the pod’s selector.

Important

* See "Creating infrastructure machine sets" for installer-provisioned infrastructure environments or for any cluster where the control plane nodes are managed by the Machine API.
* If the default node selector key conflicts with the key of a pod’s label, then the default node selector is not applied.

  However, do not set a default node selector that might cause a pod to become unschedulable. For example, setting the default node selector to a specific node role, such as `node-role.kubernetes.io/infra=""`, when a pod’s label is set to a different node role, such as `node-role.kubernetes.io/master=""`, can cause the pod to become unschedulable. For this reason, use caution when setting the default node selector to specific node roles.

  You can alternatively use a project node selector to avoid cluster-wide node selector key conflicts.

**Procedure**

1. Add a label to the compute nodes that you want to act as infrastructure nodes by running the following command:

   ```
   $ oc label node <node-name> node-role.kubernetes.io/infra=""
   ```
2. Check to see if applicable nodes now have the `infra` role by running the following command:

   ```
   $ oc get nodes
   ```
3. Optional: Create a default cluster-wide node selector.

   1. Edit the `Scheduler` object by running the following command:

      ```
      $ oc edit scheduler cluster
      ```
   2. Add the `defaultNodeSelector` field with the appropriate node selector by running the following command:

      ```
      apiVersion: config.openshift.io/v1
      kind: Scheduler
      metadata:
        name: cluster
      spec:
        defaultNodeSelector: node-role.kubernetes.io/infra=""
      # ...
      ```

      This example node selector deploys pods on infrastructure nodes by default.
   3. Save the file to apply the changes.

   You can now move infrastructure resources to the new infrastructure nodes and remove any workloads that you do not want, or that do not belong, on the new infrastructure node. See the list of workloads supported for use on infrastructure nodes in "OpenShift Container Platform infrastructure components".

### [8.12. Creating a machine config pool for infrastructure machines](#creating-infra-machines_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

You can create a machine configuration pool for infrastructure machines to apply dedicated configuration to infra machines. You might want to apply dedicated configuration to infra machines because they run distinct workloads from other nodes in the cluster.

Important

Creating a custom machine configuration pool overrides default worker pool configurations if they refer to the same file or unit.

**Procedure**

1. Add a label to the node you want to assign as the infra node by running the following command:

   ```
   $ oc label node <node_name> node-role.kubernetes.io/infra=
   ```

   where:

   `<node_name>`
   :   Specifies the name of the node you want to assign as an infra node.
2. Create a YAML file that defines the machine config pool, as in the following example:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfigPool
   metadata:
     name: infra
   spec:
     machineConfigSelector:
       matchExpressions:
         - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,infra]}
     nodeSelector:
       matchLabels:
         node-role.kubernetes.io/infra: ""
   ```

   * Add the worker role and your custom role in the `spec.machineConfigSelector.matchExpressions[]` field.
   * Add the label you added to the node in the `spec.nodeSelector.matchLabels` field.

     Note

     Custom machine config pools inherit machine configs from the worker pool. Custom pools use any machine config targeted for the worker pool, but add the ability to also deploy changes that are targeted at only the custom pool. Because a custom pool inherits resources from the worker pool, any change to the worker pool also affects the custom pool.
3. After you have the YAML file, you can create the machine config pool by specifying the file you created in the following command:

   ```
   $ oc create -f <filename>
   ```
4. Check the machine configs to ensure that the infrastructure configuration rendered successfully by running the following command:

   ```
   $ oc get machineconfig
   ```

   **Example output**

   ```
   NAME                                                        GENERATEDBYCONTROLLER                      IGNITIONVERSION   CREATED
   00-master                                                   365c1cfd14de5b0e3b85e0fc815b0060f36ab955   3.5.0             31d
   00-worker                                                   365c1cfd14de5b0e3b85e0fc815b0060f36ab955   3.5.0             31d
   # ...
   rendered-infra-4e48906dca84ee702959c71a53ee80e7             365c1cfd14de5b0e3b85e0fc815b0060f36ab955   3.5.0             23m
   ```

   You should see a new machine config, with the `rendered-infra-*` prefix.
5. Optional: To deploy changes to a custom pool, create a machine config that uses the custom pool name as the label, such as `infra`. Note that this is not required and only shown for instructional purposes. In this manner, you can apply any custom configurations specific to only your infra nodes.

   Note

   After you create the new machine config pool, the MCO generates a new rendered config for that pool, and associated nodes of that pool reboot to apply the new configuration.

   1. Create a YAML file that defines the machine config pool, as in the following example:

      ```
      $ cat infra.mc.yaml
      ```

      **Example output**

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfig
      metadata:
        name: 51-infra
        labels:
          machineconfiguration.openshift.io/role: <role>
      spec:
        config:
          ignition:
            version: 3.5.0
          storage:
            files:
            - path: /etc/infratest
              mode: 0644
              contents:
                source: data:,infra
      ```

      where:

      `role`
      :   Specifies the label you added to the node as a `nodeSelector`.
   2. Apply the machine config to the infra-labeled nodes by running the following command:

      ```
      $ oc create -f infra.mc.yaml
      ```
6. Confirm that your new machine config pool is available by running the following command:

   ```
   $ oc get mcp
   ```

   **Example output**

   ```
   NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   infra    rendered-infra-60e35c2e99f42d976e084fa94da4d0fc    True      False      False      1              1                   1                     0                      4m20s
   master   rendered-master-9360fdb895d4c131c7c4bebbae099c90   True      False      False      3              3                   3                     0                      91m
   worker   rendered-worker-60e35c2e99f42d976e084fa94da4d0fc   True      False      False      2              2                   2                     0                      91m
   ```

   In this example, the role of the node was changes from `worker` to `infra`.

### [8.13. Binding infrastructure node workloads using taints and tolerations](#binding-infra-node-workloads-using-taints-tolerations_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

To avoid user workloads being inadvertently assigned to an infra node, you can apply a taint to the infra node and tolerations for the pods you want to control. After creating an infrastructure machine set, the `worker` and `infra` roles are applied to new infra nodes.

Nodes with the `infra` role applied are not counted toward the total number of subscriptions that are required to run the environment, even when the `worker` role is also applied. If you have an infrastructure node that has the `infra` and `worker` roles assigned, you must configure the node so that user workloads are not assigned to it.

Important

It is recommended that you preserve the dual `infra,worker` label that is created for infrastructure nodes and use taints and tolerations to manage nodes that user workloads are scheduled on. If you remove the `worker` label from the node, you must create a custom pool to manage it. A node with a label other than `master` or `worker` is not recognized by the MCO without a custom pool. Maintaining the `worker` label allows the node to be managed by the default worker machine config pool, if no custom pools that select the custom label exists. The `infra` label communicates to the cluster that it does not count toward the total number of subscriptions.

**Prerequisites**

* Configure additional `MachineSet` objects in your OpenShift Container Platform cluster.

**Procedure**

1. Add a taint to the infrastructure node to prevent scheduling user workloads on it:

   1. Determine if the node has the taint by running the following command:

      ```
      $ oc describe nodes <node_name>
      ```

      **Sample output**

      ```
      oc describe node ci-ln-iyhx092-f76d1-nvdfm-worker-b-wln2l
      Name:               ci-ln-iyhx092-f76d1-nvdfm-worker-b-wln2l
      Roles:              worker
       ...
      Taints:             node-role.kubernetes.io/infra=reserved:NoSchedule
       ...
      ```

      This example shows that the node has a taint. You can proceed with adding a toleration to your pod in the next step.
   2. If you have not configured a taint to prevent scheduling user workloads on it, configure a taint by running the following command:

      ```
      $ oc adm taint nodes <node_name> <key>=<value>:<effect>
      ```

      For example:

      ```
      $ oc adm taint nodes node1 node-role.kubernetes.io/infra=reserved:NoSchedule
      ```

      Tip

      You can alternatively edit the pod specification to add the taint:

      ```
      apiVersion: v1
      kind: Node
      metadata:
        name: node1
      # ...
      spec:
        taints:
          - key: node-role.kubernetes.io/infra
            value: reserved
            effect: NoSchedule
      # ...
      ```

      These examples place a taint on `node1` that has the `node-role.kubernetes.io/infra` key and the `NoSchedule` taint effect. Nodes with the `NoSchedule` effect schedule only pods that tolerate the taint, but allow existing pods to remain scheduled on the node. If you added a `NoSchedule` taint to the infrastructure node, any pods that are controlled by a daemon set on that node are marked as `misscheduled`. You must either delete the pods or add a toleration to the pods as shown in the Red Hat Knowledgebase solution [add toleration on `misscheduled` DNS pods](https://access.redhat.com/solutions/6592171). Note that you cannot add a toleration to a daemon set object that is managed by an operator.

      Note

      If a descheduler is used, pods violating node taints could be evicted from the cluster.
2. Add tolerations to the pods that you want to schedule on the infrastructure node, such as the router, registry, and monitoring workloads. Referencing the previous examples, add the following tolerations to the `Pod` object specification:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     annotations:

   # ...
   spec:
   # ...
     tolerations:
       - key: <node_taint_key>
         value: <node_taint_value>
         effect: <taint_effect>
         operator: Equal
   ```

   where:

   `<node_taint_key>`
   :   Specifies the key that you added to the taint on the node.

   `<node_taint_value>`
   :   Specifies the value of the key-value pair taint that you added to the node.

   `<taint_effect>`
   :   Specifies the effect that you added to the node.

   `Equal`
   :   Specifies that a taint with a key matching `<node_taint_key>` is required to be present on the node.

       This toleration matches the taint created by the `oc adm taint` command. A pod with this toleration can be scheduled onto the infrastructure node.

       Note

       Moving pods for an Operator installed via OLM to an infrastructure node is not always possible. The capability to move Operator pods depends on the configuration of each Operator.
3. Schedule the pod to the infrastructure node by using a scheduler. See the documentation for "Controlling pod placement using the scheduler" for details.
4. Remove any workloads that you do not want, or that do not belong, on the new infrastructure node. See the list of workloads supported for use on infrastructure nodes in "OpenShift Container Platform infrastructure components".

### [8.14. Moving resources to infrastructure machine sets](#moving-resources-to-infrastructure-machinesets_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

Some of the infrastructure resources are deployed in your cluster by default. You can move them to the infrastructure machine sets that you created by adding the infrastructure node selector.

Applying a specific node selector to all infrastructure components causes OpenShift Container Platform to schedule those workloads on nodes with that label.

**Procedure**

1. Add a `nodeSelector` parameter with the appropriate value to the component you want to move. You can use a `nodeSelector` in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. See the following example:

   ```
   apiVersion: imageregistry.operator.openshift.io/v1
   kind: Config
   metadata:
     name: cluster
   # ...
   spec:
     nodePlacement:
       nodeSelector:
         matchLabels:
           node-role.kubernetes.io/infra: ""
       tolerations:
       - effect: NoSchedule
         key: node-role.kubernetes.io/infra
         value: reserved
       - effect: NoExecute
         key: node-role.kubernetes.io/infra
         value: reserved
   ```
2. If you added a taint to the infrastructure node, also add a matching toleration.

#### [8.14.1. Moving the router](#infrastructure-moving-router_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

Deploying the router pod on an infrastructure node can reduce your OpenShift Container Platform subscription size. Move the router pod by editing the `IngressController` object in the `openshift-ingress-operator` namespace. By default, the pod is deployed to a worker node.

**Prerequisites**

* Configure additional compute machine sets in your OpenShift Container Platform cluster.

**Procedure**

1. View the `IngressController` custom resource for the router Operator by running the following command:

   ```
   $ oc get ingresscontroller default -n openshift-ingress-operator -o yaml
   ```

   **Example output**

   ```
   apiVersion: operator.openshift.io/v1
   kind: IngressController
   metadata:
     creationTimestamp: 2019-04-18T12:35:39Z
     finalizers:
     - ingresscontroller.operator.openshift.io/finalizer-ingresscontroller
     generation: 1
     name: default
     namespace: openshift-ingress-operator
     resourceVersion: "11341"
     selfLink: /apis/operator.openshift.io/v1/namespaces/openshift-ingress-operator/ingresscontrollers/default
     uid: 79509e05-61d6-11e9-bc55-02ce4781844a
   spec: {}
   status:
     availableReplicas: 2
     conditions:
     - lastTransitionTime: 2019-04-18T12:36:15Z
       status: "True"
       type: Available
     domain: apps.<cluster>.example.com
     endpointPublishingStrategy:
       type: LoadBalancerService
     selector: ingresscontroller.operator.openshift.io/deployment-ingresscontroller=default
   ```
2. Edit the `ingresscontroller` resource and change the `nodeSelector` to use the `infra` label by running the following command:

   ```
   $ oc edit ingresscontroller default -n openshift-ingress-operator
   ```

   **Example output**

   ```
   apiVersion: operator.openshift.io/v1
   kind: IngressController
   metadata:
     creationTimestamp: "2025-03-26T21:15:43Z"
     finalizers:
     - ingresscontroller.operator.openshift.io/finalizer-ingresscontroller
     generation: 1
     name: default
   # ...
   spec:
     nodePlacement:
       nodeSelector:
         matchLabels:
           node-role.kubernetes.io/infra: ""
       tolerations:
       - effect: NoSchedule
         key: node-role.kubernetes.io/infra
         value: reserved
   # ...
   ```

   Add a `nodeSelector` parameter with the appropriate value to the component you want to move. You can use a `nodeSelector` parameter in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. If you added a taint to the infrastructure node, also add a matching toleration.

**Verification**

* Confirm that the router pod is running on the `infra` node.

  1. View the list of router pods and note the node name of the running pod by running the following command:

     ```
     $ oc get pod -n openshift-ingress -o wide
     ```

     **Example output**

     ```
     NAME                              READY     STATUS        RESTARTS   AGE       IP           NODE                           NOMINATED NODE   READINESS GATES
     router-default-86798b4b5d-bdlvd   1/1      Running       0          28s       10.130.2.4   ip-10-0-217-226.ec2.internal   <none>           <none>
     router-default-955d875f4-255g8    0/1      Terminating   0          19h       10.129.2.4   ip-10-0-148-172.ec2.internal   <none>           <none>
     ```

     In this example, the running pod is on the `ip-10-0-217-226.ec2.internal` node.
  2. View the node status of the running pod by running the following command:

     ```
     $ oc get node <node_name>
     ```

     Specify the `<node_name>` that you obtained from the pod list.

     **Example output**

     ```
     NAME                          STATUS  ROLES         AGE   VERSION
     ip-10-0-217-226.ec2.internal  Ready   infra,worker  17h   v1.35.4
     ```

     Because the role list includes `infra`, the pod is running on the correct node.

#### [8.14.2. Moving the default registry](#infrastructure-moving-registry_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

Deploying the registry pod on an infrastructure node can reduce your OpenShift Container Platform subscription size. Move the registry pod by editing the `configs.imageregistry.operator.openshift.io/cluster` config object.

**Prerequisites**

* Configure additional compute machine sets in your OpenShift Container Platform cluster.

**Procedure**

1. Edit the `configs.imageregistry.operator.openshift.io/cluster` object by running the following command:

   ```
   $ oc edit configs.imageregistry.operator.openshift.io/cluster
   ```
2. Add a `nodeSelector` parameter with the appropriate value to the component you want to move, as shown in the following example.

   ```
   apiVersion: imageregistry.operator.openshift.io/v1
   kind: Config
   metadata:
     name: cluster
   # ...
   spec:
     logLevel: Normal
     managementState: Managed
     nodeSelector:
       node-role.kubernetes.io/infra: ""
     tolerations:
     - effect: NoSchedule
       key: node-role.kubernetes.io/infra
       value: reserved
   ```

   You can use a `nodeSelector` parameter in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. If you added a taint to the infrastructure node, also add a matching toleration.

**Verification**

* Verify the registry pod has been moved to the infrastructure node.

  1. Identify the node where the registry pod is located by running the following command:

     ```
     $ oc get pods -o wide -n openshift-image-registry
     ```
  2. Confirm the node has the label you specified:

     ```
     $ oc describe node <node_name>
     ```

     where:

     `<node_name>`
     :   Specifies the name of the node that you modified. Review the command output and confirm that `node-role.kubernetes.io/infra` is in the `LABELS` list.

#### [8.14.3. Moving the monitoring solution](#infrastructure-moving-monitoring_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

Redeploy the monitoring stack to infrastructure nodes to reduce your subscription requirements. Create and apply a custom config map to move the monitoring stack to infrastructure nodes. The monitoring stack includes Prometheus, Thanos Querier, and Alertmanager, and is managed by the Cluster Monitoring Operator (CMO).

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` cluster role.
* You have created the `cluster-monitoring-config` `ConfigMap` object.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Edit the `cluster-monitoring-config` config map and change the `nodeSelector` to use the `infra` label by running the following command:

   ```
   $ oc edit configmap cluster-monitoring-config -n openshift-monitoring
   ```

   ```
   apiVersion: v1
   kind: ConfigMap
   metadata:
     name: cluster-monitoring-config
     namespace: openshift-monitoring
   data:
     config.yaml: |+
       alertmanagerMain:
         nodeSelector:
           node-role.kubernetes.io/infra: ""
         tolerations:
         - key: node-role.kubernetes.io/infra
           value: reserved
           effect: NoSchedule
       prometheusK8s:
         nodeSelector:
           node-role.kubernetes.io/infra: ""
         tolerations:
         - key: node-role.kubernetes.io/infra
           value: reserved
           effect: NoSchedule
       prometheusOperator:
         nodeSelector:
           node-role.kubernetes.io/infra: ""
         tolerations:
         - key: node-role.kubernetes.io/infra
           value: reserved
           effect: NoSchedule
       metricsServer:
         nodeSelector:
           node-role.kubernetes.io/infra: ""
         tolerations:
         - key: node-role.kubernetes.io/infra
           value: reserved
           effect: NoSchedule
       kubeStateMetrics:
         nodeSelector:
           node-role.kubernetes.io/infra: ""
         tolerations:
         - key: node-role.kubernetes.io/infra
           value: reserved
           effect: NoSchedule
       telemeterClient:
         nodeSelector:
           node-role.kubernetes.io/infra: ""
         tolerations:
         - key: node-role.kubernetes.io/infra
           value: reserved
           effect: NoSchedule
       openshiftStateMetrics:
         nodeSelector:
           node-role.kubernetes.io/infra: ""
         tolerations:
         - key: node-role.kubernetes.io/infra
           value: reserved
           effect: NoSchedule
       thanosQuerier:
         nodeSelector:
           node-role.kubernetes.io/infra: ""
         tolerations:
         - key: node-role.kubernetes.io/infra
           value: reserved
           effect: NoSchedule
       monitoringPlugin:
         nodeSelector:
           node-role.kubernetes.io/infra: ""
         tolerations:
         - key: node-role.kubernetes.io/infra
           value: reserved
           effect: NoSchedule
   ```

   Add a `nodeSelector` parameter with the appropriate value to the component you want to move. You can use a `nodeSelector` parameter in the format shown or use `<key>: <value>` pairs, based on the value specified for the node. If you added a taint to the infrastructure node, also add a matching toleration.
2. Watch the monitoring pods move to the new machines by running the following command:

   ```
   $ watch 'oc get pod -n openshift-monitoring -o wide'
   ```
3. If a component has not moved to the `infra` node, delete the pod with this component by running the following command:

   ```
   $ oc delete pod -n openshift-monitoring <pod>
   ```

   The component from the deleted pod is re-created on the `infra` node.

#### [8.14.4. Moving the Vertical Pod Autoscaler Operator components](#infrastructure-moving-vpa_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

You can move the VPA Operator and component pods to infrastructure nodes by adding a node selector to the VPA subscription and the `VerticalPodAutoscalerController` CR.

The Vertical Pod Autoscaler Operator (VPA) consists of three components: the recommender, updater, and admission controller. The Operator and each component has its own pod in the VPA namespace on the control plane nodes.

The following example shows the default deployment of the VPA pods to the control plane nodes.

```
NAME                                                READY   STATUS    RESTARTS   AGE     IP            NODE                  NOMINATED NODE   READINESS GATES
vertical-pod-autoscaler-operator-6c75fcc9cd-5pb6z   1/1     Running   0          7m59s   10.128.2.24   c416-tfsbj-master-1   <none>           <none>
vpa-admission-plugin-default-6cb78d6f8b-rpcrj       1/1     Running   0          5m37s   10.129.2.22   c416-tfsbj-master-1   <none>           <none>
vpa-recommender-default-66846bd94c-dsmpp            1/1     Running   0          5m37s   10.129.2.20   c416-tfsbj-master-0   <none>           <none>
vpa-updater-default-db8b58df-2nkvf                  1/1     Running   0          5m37s   10.129.2.21   c416-tfsbj-master-1   <none>           <none>
```

**Procedure**

1. Move the VPA Operator pod by adding a node selector to the `Subscription` custom resource (CR) for the VPA Operator:

   1. Edit the CR:

      ```
      $ oc edit Subscription vertical-pod-autoscaler -n openshift-vertical-pod-autoscaler
      ```
   2. Add a node selector to match the node role label on the infra node:

      ```
      apiVersion: operators.coreos.com/v1alpha1
      kind: Subscription
      metadata:
        labels:
          operators.coreos.com/vertical-pod-autoscaler.openshift-vertical-pod-autoscaler: ""
        name: vertical-pod-autoscaler
      # ...
      spec:
        config:
          nodeSelector:
            node-role.kubernetes.io/infra: ""
      ```

      where:

      `spec.config.nodeSelector.node-role.kubernetes.io/infra`
      :   Specifies the node role of an infra node.

      Note

      If the infra node uses taints, you need to add a toleration to the `Subscription` CR.

      For example:

      ```
      apiVersion: operators.coreos.com/v1alpha1
      kind: Subscription
      metadata:
        labels:
          operators.coreos.com/vertical-pod-autoscaler.openshift-vertical-pod-autoscaler: ""
        name: vertical-pod-autoscaler
      # ...
      spec:
        config:
          nodeSelector:
            node-role.kubernetes.io/infra: ""
          tolerations:
          - key: "node-role.kubernetes.io/infra"
            operator: "Exists"
            effect: "NoSchedule"
      ```

      where:

      `spec.config.tolerations`
      :   Specifies a toleration for a taint on the infra node.
2. Move each VPA component by adding node selectors to the `VerticalPodAutoscaler` custom resource (CR):

   1. Edit the CR:

      ```
      $ oc edit VerticalPodAutoscalerController default -n openshift-vertical-pod-autoscaler
      ```
   2. Add node selectors to match the node role label on the infra node:

      ```
      apiVersion: autoscaling.openshift.io/v1
      kind: VerticalPodAutoscalerController
      metadata:
        name: default
        namespace: openshift-vertical-pod-autoscaler
      # ...
      spec:
        deploymentOverrides:
          admission:
            container:
              resources: {}
            nodeSelector:
              node-role.kubernetes.io/infra: ""
          recommender:
            container:
              resources: {}
            nodeSelector:
              node-role.kubernetes.io/infra: ""
          updater:
            container:
              resources: {}
            nodeSelector:
              node-role.kubernetes.io/infra: ""
      ```

      where:

      `spec.deploymentOverrides.admission.nodeselector`
      :   Optional: Specifies the node role for the VPA admission pod.

      `spec.deploymentOverrides.recommender.nodeselector`
      :   Optional: Specifies the node role for the VPA recommender pod.

      `spec.deploymentOverrides.updater.nodeselector`
      :   Optional: Specifies the node role for the VPA updater pod.

      Note

      If a target node uses taints, you need to add a toleration to the `VerticalPodAutoscalerController` CR.

      For example:

      ```
      apiVersion: autoscaling.openshift.io/v1
      kind: VerticalPodAutoscalerController
      metadata:
        name: default
        namespace: openshift-vertical-pod-autoscaler
      # ...
      spec:
        deploymentOverrides:
          admission:
            container:
              resources: {}
            nodeSelector:
              node-role.kubernetes.io/infra: ""
            tolerations:
            - key: "my-example-node-taint-key"
              operator: "Exists"
              effect: "NoSchedule"
          recommender:
            container:
              resources: {}
            nodeSelector:
              node-role.kubernetes.io/infra: ""
            tolerations:
            - key: "my-example-node-taint-key"
              operator: "Exists"
              effect: "NoSchedule"
          updater:
            container:
              resources: {}
            nodeSelector:
              node-role.kubernetes.io/infra: ""
            tolerations:
            - key: "my-example-node-taint-key"
              operator: "Exists"
              effect: "NoSchedule"
      ```

      where:

      `spec.deploymentOverrides.admission.tolerations`
      :   Specifies a toleration for the admission controller pod for a taint on the infra node.

      `spec.deploymentOverrides.recommender.tolerations`
      :   Specifies a toleration for the recommender pod for a taint on the infra node.

      `spec.deploymentOverrides.updater.tolerations`
      :   Specifies a toleration for the updater pod for a taint on the infra node.

**Verification**

* You can verify the pods have moved by using the following command:

  ```
  $ oc get pods -n openshift-vertical-pod-autoscaler -o wide
  ```

  The pods are no longer deployed to the control plane nodes. In the following example output, the node is now an infra node, not a control plane node.

  **Example output**

  ```
  NAME                                                READY   STATUS    RESTARTS   AGE     IP            NODE                              NOMINATED NODE   READINESS GATES
  vertical-pod-autoscaler-operator-6c75fcc9cd-5pb6z   1/1     Running   0          7m59s   10.128.2.24   c416-tfsbj-infra-eastus3-2bndt   <none>           <none>
  vpa-admission-plugin-default-6cb78d6f8b-rpcrj       1/1     Running   0          5m37s   10.129.2.22   c416-tfsbj-infra-eastus1-lrgj8   <none>           <none>
  vpa-recommender-default-66846bd94c-dsmpp            1/1     Running   0          5m37s   10.129.2.20   c416-tfsbj-infra-eastus1-lrgj8   <none>           <none>
  vpa-updater-default-db8b58df-2nkvf                  1/1     Running   0          5m37s   10.129.2.21   c416-tfsbj-infra-eastus1-lrgj8   <none>           <none>
  ```

#### [8.14.5. Moving the Cluster Resource Override Operator pods](#nodes-cluster-resource-override-move-infra_creating-infrastructure-machinesets) Copy linkLink copied to clipboard!

By default, the Cluster Resource Override Operator installation process creates an Operator pod and two Cluster Resource Override pods on nodes in the `clusterresourceoverride-operator` namespace. You can move these pods to other nodes, such as infrastructure nodes, as needed.

The following example shows that the Cluster Resource Override pods are deployed to control plane nodes.

```
NAME                                                READY   STATUS    RESTARTS   AGE   IP            NODE                                        NOMINATED NODE   READINESS GATES
clusterresourceoverride-786b8c898c-9wrdq            1/1     Running   0          23s   10.128.2.32   ip-10-0-14-183.us-west-2.compute.internal   <none>           <none>
clusterresourceoverride-786b8c898c-vn2lf            1/1     Running   0          26s   10.130.2.10   ip-10-0-20-140.us-west-2.compute.internal   <none>           <none>
clusterresourceoverride-operator-6b8b8b656b-lvr62   1/1     Running   0          56m   10.131.0.33   ip-10-0-2-39.us-west-2.compute.internal     <none>           <none>
```

The following example shows that the Cluster Resource Override Operator pod is deployed to a worker node.

```
NAME                                        STATUS   ROLES                  AGE   VERSION
ip-10-0-14-183.us-west-2.compute.internal   Ready    control-plane,master   65m   v1.35.4
ip-10-0-2-39.us-west-2.compute.internal     Ready    worker                 58m   v1.35.4
ip-10-0-20-140.us-west-2.compute.internal   Ready    control-plane,master   65m   v1.35.4
ip-10-0-23-244.us-west-2.compute.internal   Ready    infra                  55m   v1.35.4
ip-10-0-77-153.us-west-2.compute.internal   Ready    control-plane,master   65m   v1.35.4
ip-10-0-99-108.us-west-2.compute.internal   Ready    worker                 24m   v1.35.4
ip-10-0-24-233.us-west-2.compute.internal   Ready    infra                  55m   v1.35.4
ip-10-0-88-109.us-west-2.compute.internal   Ready    worker                 24m   v1.35.4
ip-10-0-67-453.us-west-2.compute.internal   Ready    infra                  55m   v1.35.4
```

**Procedure**

1. Move the Cluster Resource Override Operator pod by adding a node selector to the `Subscription` custom resource (CR) for the Cluster Resource Override Operator.

   1. Edit the CR:

      ```
      $ oc edit -n clusterresourceoverride-operator subscriptions.operators.coreos.com clusterresourceoverride
      ```
   2. Add a node selector to match the node role label on the node where you want to install the Cluster Resource Override Operator pod:

      ```
      apiVersion: operators.coreos.com/v1alpha1
      kind: Subscription
      metadata:
        name: clusterresourceoverride
        namespace: clusterresourceoverride-operator
      # ...
      spec:
        config:
          nodeSelector:
            node-role.kubernetes.io/infra: ""
      ```

      where:

      `spec.config.nodeSelector`
      :   Specifies the role of the node where you want to deploy the Cluster Resource Override Operator pod.

   Note

   If the infra node uses taints, you need to add a toleration to the `Subscription` CR. For example:

   ```
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: clusterresourceoverride
     namespace: clusterresourceoverride-operator
   # ...
   spec:
     config:
       nodeSelector:
         node-role.kubernetes.io/infra: ""
       tolerations:
       - key: "node-role.kubernetes.io/infra"
         operator: "Exists"
         effect: "NoSchedule"
   ```

   where:

   `spec.config.tolerations`
   :   Specifies a toleration for a taint on the infra node.
2. Move the Cluster Resource Override pods by adding a node selector to the `ClusterResourceOverride` custom resource (CR):

   1. Edit the CR:

      ```
      $ oc edit ClusterResourceOverride cluster -n clusterresourceoverride-operator
      ```
   2. Add a node selector to match the node role label on the infra node:

      ```
      apiVersion: operator.autoscaling.openshift.io/v1
      kind: ClusterResourceOverride
      metadata:
        name: cluster
        resourceVersion: "37952"
      spec:
        podResourceOverride:
          spec:
            cpuRequestToLimitPercent: 25
            limitCPUToMemoryPercent: 200
            memoryRequestToLimitPercent: 50
        deploymentOverrides:
          replicas: 1
          nodeSelector:
            node-role.kubernetes.io/infra: ""
      # ...
      ```

      where:

      `spec.deploymentOverrides.replicas`
      :   Specifies the number of Cluster Resource Override pods to deploy. The default is `2`. Only one pod is allowed per node. This parameter is optional.

      `spec.deploymentOverrides.nodeSelector`
      :   Specifies the role of the node where you want to deploy the Cluster Resource Override pods. This parameter is optional.

   Note

   If the infra node uses taints, you need to add a toleration to the `ClusterResourceOverride` CR. For example:

   ```
   apiVersion: operator.autoscaling.openshift.io/v1
   kind: ClusterResourceOverride
   metadata:
     name: cluster
   # ...
   spec:
     podResourceOverride:
       spec:
         memoryRequestToLimitPercent: 50
         cpuRequestToLimitPercent: 25
         limitCPUToMemoryPercent: 200
     deploymentOverrides:
       replicas: 3
       nodeSelector:
         node-role.kubernetes.io/worker: ""
       tolerations:
       - key: "key"
         operator: "Equal"
         value: "value"
         effect: "NoSchedule"
   ```

   where:

   `spec.deploymentOverrides.tolerations`
   :   Specifies a toleration for a taint on the infra node.

**Verification**

* You can verify that the pods have moved by using the following command:

  ```
  $ oc get pods -n clusterresourceoverride-operator -o wide
  ```

  The Cluster Resource Override pods are now deployed to the infra nodes.

  **Example output**

  ```
  NAME                                                READY   STATUS    RESTARTS   AGE   IP            NODE                                        NOMINATED NODE   READINESS GATES
  clusterresourceoverride-786b8c898c-9wrdq            1/1     Running   0          23s   10.127.2.25   ip-10-0-23-244.us-west-2.compute.internal   <none>           <none>
  clusterresourceoverride-786b8c898c-vn2lf            1/1     Running   0          26s   10.128.0.80   ip-10-0-24-233.us-west-2.compute.internal   <none>           <none>
  clusterresourceoverride-operator-6b8b8b656b-lvr62   1/1     Running   0          56m   10.129.0.71   ip-10-0-67-453.us-west-2.compute.internal   <none>           <none>
  ```

## [Chapter 9. Managing user-provisioned infrastructure manually](#managing-user-provisioned-infrastructure-manually) Copy linkLink copied to clipboard!

### [9.1. Adding compute machines to clusters with user-provisioned infrastructure manually](#adding-compute-user-infra-general) Copy linkLink copied to clipboard!

To scale a OpenShift Container Platform cluster that uses user-provisioned infrastructure, you can manually add compute machines during or after installation. The postinstallation process requires some of the same configuration files and parameters that you used for installation.

#### [9.1.1. Adding compute machines to Amazon Web Services](#upi-adding-compute-aws) Copy linkLink copied to clipboard!

You can add more compute machines to your OpenShift Container Platform cluster on AWS.

See [Adding compute machines to AWS by using CloudFormation templates](#adding-aws-compute-user-infra "9.2. Adding compute machines to AWS by using CloudFormation templates") for more information.

#### [9.1.2. Adding compute machines to Microsoft Azure](#upi-adding-compute-azure) Copy linkLink copied to clipboard!

You can add more compute machines to your OpenShift Container Platform cluster on Microsoft Azure.

See [Creating additional worker machines in Azure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure/#installation-creating-azure-worker_installing-azure-user-infra) for more information.

#### [9.1.3. Adding compute machines to Azure Stack Hub](#upi-adding-compute-ash) Copy linkLink copied to clipboard!

You can add more compute machines to your OpenShift Container Platform cluster on Azure Stack Hub.

See [Creating additional worker machines in Azure Stack Hub](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_azure_stack_hub/#installation-creating-azure-worker_installing-azure-stack-hub-user-infra) for more information.

#### [9.1.4. Adding compute machines to Google Cloud](#upi-adding-compute-gcp) Copy linkLink copied to clipboard!

You can add more compute machines to your OpenShift Container Platform cluster on GCP.

See [Creating additional worker machines in Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/#installation-creating-gcp-worker_installing-restricted-networks-gcp) for more information.

#### [9.1.5. Adding compute machines to vSphere](#upi-adding-compute-vsphere) Copy linkLink copied to clipboard!

You can use compute machine sets to automate the creation of additional compute machines for your OpenShift Container Platform cluster on vSphere.

See [use compute machine sets](#creating-machineset-vsphere "2.9. Creating a compute machine set on vSphere") for more information.

You can manually add more compute machines to your cluster.

See [Adding compute machines to vSphere manually](#adding-vsphere-compute-user-infra "9.3. Adding compute machines to vSphere manually") for more information.

You can add bare-metal compute machines to your cluster.

See [Adding bare-metal compute machines to a vSphere cluster](#adding-bare-metal-compute-vsphere-user-infra "9.4. Adding bare-metal compute machines to a vSphere cluster") for more information.

Important

Bare-metal nodes on vSphere clusters is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

#### [9.1.6. Adding compute machines to bare metal](#upi-adding-compute-baremetal) Copy linkLink copied to clipboard!

You can add more compute machines to your OpenShift Container Platform cluster on bare metal.

See [Adding compute machines to bare metal](#adding-bare-metal-compute-user-infra "9.5. Adding compute machines to bare metal") for more information.

### [9.2. Adding compute machines to AWS by using CloudFormation templates](#adding-aws-compute-user-infra) Copy linkLink copied to clipboard!

To scale your OpenShift Container Platform cluster on Amazon Web Services (AWS) after user-provisioned installation, you can add compute machines by creating CloudFormation stacks from your installation templates. You can then approve certificate signing requests so the new nodes join the cluster.

#### [9.2.1. Prerequisites](#prerequisites_adding-aws-compute-user-infra) Copy linkLink copied to clipboard!

* You installed your cluster on AWS by using the provided [AWS CloudFormation templates](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-user-infra).
* You have the JSON file and CloudFormation template that you used to create the compute machines during cluster installation. If you do not have these files, you must recreate them by following the instructions in the [installation procedure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_aws/#installing-aws-user-infra).

#### [9.2.2. Adding more compute machines to your AWS cluster by using CloudFormation templates](#machine-adding-aws-compute-cloudformation_adding-aws-compute-user-infra) Copy linkLink copied to clipboard!

To scale your OpenShift Container Platform cluster on Amazon Web Services (AWS), you can add more compute machines by creating additional CloudFormation stacks from the sample templates that you used during installation.

Important

The CloudFormation template creates a stack that represents one compute machine. You must create a stack for each compute machine.

Note

If you do not use the provided CloudFormation template to create your compute nodes, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* You installed an OpenShift Container Platform cluster by using CloudFormation templates and have access to the JSON file and CloudFormation template that you used to create the compute machines during cluster installation.
* You installed the AWS CLI.

**Procedure**

1. Create another compute stack.

   1. Launch the template:

      ```
      $ aws cloudformation create-stack --stack-name <name>
           --template-body file://<template>.yaml
           --parameters file://<parameters>.json
      ```

      * `<name>` is the name for the CloudFormation stack, such as `cluster-workers`. You must provide the name of this stack if you remove the cluster.
      * `<template>` is the relative path to and name of the CloudFormation template YAML file that you saved.
      * `<parameters>` is the relative path to and name of the CloudFormation parameters JSON file.
   2. Confirm that the template components exist:

      ```
      $ aws cloudformation describe-stacks --stack-name <name>
      ```
2. Continue to create compute stacks until you have created enough compute machines for your cluster.

#### [9.2.3. Approving the certificate signing requests for your machines](#installation-approve-csrs_adding-aws-compute-user-infra) Copy linkLink copied to clipboard!

To allow newly added machines to join your OpenShift Container Platform cluster, confirm that the cluster approves pending certificate signing requests (CSRs), or approve them yourself. Approve client requests first, then server requests.

**Prerequisites**

* You added machines to your cluster.

**Procedure**

1. Confirm that the cluster recognizes the machines:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME      STATUS    ROLES   AGE  VERSION
   master-0  Ready     master  63m  v1.35.4
   master-1  Ready     master  63m  v1.35.4
   master-2  Ready     master  64m  v1.35.4
   ```

   The output lists all of the machines that you created.

   Note

   The preceding output might not include the compute nodes until you approve some CSRs.
2. Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:

   ```
   $ oc get csr
   ```

   **Example output**

   ```
   NAME        AGE     REQUESTOR                                                                   CONDITION
   csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
   csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
   ...
   ```

   In this example, two machines are joining the cluster. You might see more approved CSRs in the list.
3. If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:

   Note

   You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates rotate, and more than two certificates are present for each node. You must approve all of these certificates. After you approve the client CSR, the kubelet creates a secondary CSR for the serving certificate, which requires manual approval. The `machine-approver` then automatically approves later serving certificate renewal requests if the kubelet requests a new certificate with the same parameters.

   Note

   For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If you do not approve a request, the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because the API server requires a serving certificate when it connects to the kubelet. Any operation that contacts the kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the `node-bootstrapper` service account in the `system:node` or `system:admin` groups submitted the CSR, and confirm the identity of the node.

   * To approve them individually, run the following command for each valid CSR:

     ```
     $ oc adm certificate approve <csr_name>
     ```

     where:

     `<csr_name>`
     :   Specifies the name of a CSR from the list of current CSRs.
   * To approve all pending CSRs, run the following command:

     ```
     $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
     ```

     Note

     Some Operators might not become available until you approve some CSRs. Each node submits two CSRs, so you might need to run the command to approve CSRs many times.
4. After you approve your client requests, review the server requests for each machine that you added to the cluster:

   ```
   $ oc get csr
   ```

   **Example output**

   ```
   NAME        AGE     REQUESTOR                                                                   CONDITION
   csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
   csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
   ...
   ```
5. If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:

   * To approve them individually, run the following command for each valid CSR:

     ```
     $ oc adm certificate approve <csr_name>
     ```

     where:

     `<csr_name>`
     :   Specifies the name of a CSR from the list of current CSRs.
   * To approve all pending CSRs, run the following command:

     ```
     $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
     ```
6. After you approve all client and server CSRs, the machines have the `Ready` status. Verify this by running the following command:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME      STATUS    ROLES   AGE  VERSION
   master-0  Ready     master  73m  v1.35.4
   master-1  Ready     master  73m  v1.35.4
   master-2  Ready     master  74m  v1.35.4
   worker-0  Ready     worker  11m  v1.35.4
   worker-1  Ready     worker  11m  v1.35.4
   ```

   Note

   You might need to wait a few minutes after approval of the server CSRs for the machines to change to the `Ready` status.

### [9.3. Adding compute machines to vSphere manually](#adding-vsphere-compute-user-infra) Copy linkLink copied to clipboard!

You can add more compute machines to your OpenShift Container Platform cluster on VMware vSphere manually.

#### [9.3.1. Prerequisites](#adding-vsphere-compute-user-infra_adding-vsphere-compute-user-infra) Copy linkLink copied to clipboard!

There are several prerequisites that must be completed before you add more compute machines to your OpenShift Container Platform cluster on VMware vSphere manually.

Note

You can also [use compute machine sets](#creating-machineset-vsphere "2.9. Creating a compute machine set on vSphere") to automate the creation of additional VMware vSphere compute machines for your cluster.

The following prerequisites must be met:

* You [installed a cluster on vSphere](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere).
* You have installation media and Red Hat Enterprise Linux CoreOS (RHCOS) images that you used to create your cluster. If you do not have these files, you must obtain them by following the instructions in the [installation procedure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_vmware_vsphere/#installing-vsphere).

Important

If you do not have access to the Red Hat Enterprise Linux CoreOS (RHCOS) images that were used to create your cluster, you can add more compute machines to your OpenShift Container Platform cluster with newer versions of Red Hat Enterprise Linux CoreOS (RHCOS) images. For instructions, see [Adding new nodes to UPI cluster fails after upgrading to OpenShift 4.6+](https://access.redhat.com/solutions/5514051).

#### [9.3.2. Adding more compute machines to a cluster in vSphere](#machine-vsphere-machines_adding-vsphere-compute-user-infra) Copy linkLink copied to clipboard!

To scale a user-provisioned OpenShift Container Platform cluster on VMware vSphere, you can add more compute machines by cloning the vSphere template into a virtual machine (VM).

**Prerequisites**

* Obtain the base64-encoded Ignition file for your compute machines.
* You have access to the vSphere template that you created for your cluster.

**Procedure**

1. Right-click the template’s name and click **Clone** → **Clone to Virtual Machine**.
2. On the **Select a name and folder** tab, specify a name for the VM. You might include the machine type in the name, such as `compute-1`.

   Note

   Ensure that all virtual machine names across a vSphere installation are unique.
3. On the **Select a name and folder** tab, select the name of the folder that you created for the cluster.
4. On the **Select a compute resource** tab, select the name of a host in your data center.
5. On the **Select storage** tab, select storage for your configuration and disk files.
6. On the **Select clone options** tab, select **Customize this virtual machine’s hardware**.
7. On the **Customize hardware** tab, click **Advanced Parameters**.

   * Add the following configuration parameter names and values by specifying data in the **Attribute** and **Values** fields. Ensure that you select the **Add** button for each parameter that you create.

     + `guestinfo.ignition.config.data`: Paste the contents of the base64-encoded compute Ignition config file for this machine type.
     + `guestinfo.ignition.config.data.encoding`: Specify `base64`.
     + `disk.EnableUUID`: Specify `TRUE`.
8. In the **Virtual Hardware** panel of the **Customize hardware** tab, modify the specified values as required. Ensure that the amount of RAM, CPU, and disk storage meets the minimum requirements for the machine type. If many networks exist, select **Add New Device** > **Network Adapter**, and then enter your network information in the fields provided by the **New Network** menu item.
9. Complete the remaining configuration steps. On clicking the **Finish** button, you have completed the cloning operation.
10. From the **Virtual Machines** tab, right-click on your VM and then select **Power** → **Power On**.

**Next steps**

* Continue to create more compute machines for your cluster.

#### [9.3.3. Approving the certificate signing requests for your machines](#installation-approve-csrs_adding-vsphere-compute-user-infra) Copy linkLink copied to clipboard!

To allow newly added machines to join your OpenShift Container Platform cluster, confirm that the cluster approves pending certificate signing requests (CSRs), or approve them yourself. Approve client requests first, then server requests.

**Prerequisites**

* You added machines to your cluster.

**Procedure**

1. Confirm that the cluster recognizes the machines:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME      STATUS    ROLES   AGE  VERSION
   master-0  Ready     master  63m  v1.35.4
   master-1  Ready     master  63m  v1.35.4
   master-2  Ready     master  64m  v1.35.4
   ```

   The output lists all of the machines that you created.

   Note

   The preceding output might not include the compute nodes until you approve some CSRs.
2. Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:

   ```
   $ oc get csr
   ```

   **Example output**

   ```
   NAME        AGE     REQUESTOR                                                                   CONDITION
   csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
   csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
   ...
   ```

   In this example, two machines are joining the cluster. You might see more approved CSRs in the list.
3. If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:

   Note

   You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates rotate, and more than two certificates are present for each node. You must approve all of these certificates. After you approve the client CSR, the kubelet creates a secondary CSR for the serving certificate, which requires manual approval. The `machine-approver` then automatically approves later serving certificate renewal requests if the kubelet requests a new certificate with the same parameters.

   Note

   For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If you do not approve a request, the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because the API server requires a serving certificate when it connects to the kubelet. Any operation that contacts the kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the `node-bootstrapper` service account in the `system:node` or `system:admin` groups submitted the CSR, and confirm the identity of the node.

   * To approve them individually, run the following command for each valid CSR:

     ```
     $ oc adm certificate approve <csr_name>
     ```

     where:

     `<csr_name>`
     :   Specifies the name of a CSR from the list of current CSRs.
   * To approve all pending CSRs, run the following command:

     ```
     $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
     ```

     Note

     Some Operators might not become available until you approve some CSRs. Each node submits two CSRs, so you might need to run the command to approve CSRs many times.
4. After you approve your client requests, review the server requests for each machine that you added to the cluster:

   ```
   $ oc get csr
   ```

   **Example output**

   ```
   NAME        AGE     REQUESTOR                                                                   CONDITION
   csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
   csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
   ...
   ```
5. If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:

   * To approve them individually, run the following command for each valid CSR:

     ```
     $ oc adm certificate approve <csr_name>
     ```

     where:

     `<csr_name>`
     :   Specifies the name of a CSR from the list of current CSRs.
   * To approve all pending CSRs, run the following command:

     ```
     $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
     ```
6. After you approve all client and server CSRs, the machines have the `Ready` status. Verify this by running the following command:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME      STATUS    ROLES   AGE  VERSION
   master-0  Ready     master  73m  v1.35.4
   master-1  Ready     master  73m  v1.35.4
   master-2  Ready     master  74m  v1.35.4
   worker-0  Ready     worker  11m  v1.35.4
   worker-1  Ready     worker  11m  v1.35.4
   ```

   Note

   You might need to wait a few minutes after approval of the server CSRs for the machines to change to the `Ready` status.

### [9.4. Adding bare-metal compute machines to a vSphere cluster](#adding-bare-metal-compute-vsphere-user-infra) Copy linkLink copied to clipboard!

To support workloads requiring direct hardware access, extend your existing VMware vSphere cluster by adding bare-metal compute machines. This creates a hybrid architecture that combines a virtualized control plane with the performance of physical hardware.

This procedure supports clusters installed using installer-provisioned infrastructure, user-provisioned infrastructure, or the Assisted Installer.

Important

Bare-metal nodes on vSphere clusters is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

Important

Bare-metal compute machines added to a vSphere cluster are unmanaged by the Machine API. You cannot use compute machine sets or the cluster autoscaler to manage these compute machines. Lifecycle tasks such as provisioning and replacement must be performed manually.

#### [9.4.1. Prerequisites](#prerequisites-2) Copy linkLink copied to clipboard!

* You have an existing OpenShift Container Platform cluster installed on vSphere.
* You have bare-metal hardware with network connectivity to the existing cluster’s machine network.
* You have configured the network for the new bare-metal compute machines, including:

  + DHCP: Persistent IP addresses and hostname reservations.
  + DNS: Forward and reverse DNS resolution for the new hostnames.
* You have obtained the Red Hat Enterprise Linux CoreOS (RHCOS) ISO image that matches your cluster version. You can download this from the **Cluster Details** page on the Red Hat Hybrid Cloud Console or extract it from the cluster payload.

Warning

To use this feature, you must explicitly disable the native vSphere Container Storage Interface (CSI) driver for the entire cluster. This means existing vSphere virtual machines will lose the ability to provision or attach vSphere volumes. You must ensure that all workloads (virtual and physical) are migrated to an alternative storage solution before proceeding.

#### [9.4.2. Creating RHCOS machines using an ISO image](#bare-metal-vsphere-iso_adding-bare-metal-compute-vsphere-user-infra) Copy linkLink copied to clipboard!

To add bare-metal compute machines to your VMware vSphere cluster, you must manually provision them using an RHCOS ISO image and the `coreos-installer` utility.

Important

Bare-metal nodes on vSphere clusters is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Prerequisites**

* You have access to the RHCOS ISO image that matches your cluster version.
* You have an HTTP server accessible to the bare-metal machine to host the Ignition config file.
* You have disabled the vSphere CSI driver.
* The OpenShift CLI (`oc`) is installed.

**Procedure**

1. Extract the Ignition config file for the worker node type from the cluster by running the following command:

   ```
   $ oc extract -n openshift-machine-api secret/worker-user-data-managed --keys=userData --to=- > worker.ign
   ```
2. Upload the `worker.ign` Ignition config file to your HTTP server. Record the URL of this file.
3. Validate that the Ignition file is accessible from the network. The following example uses `curl` to verify the file presence:

   ```
   $ curl -I http://<http_server>/worker.ign
   ```
4. Boot the bare-metal machine using the RHCOS ISO image.
5. From the installation console, run the `coreos-installer` command:

   ```
   $ sudo coreos-installer install /dev/sda \
       --ignition-url=http://<http_server>/worker.ign \
       --insecure-ignition \
       --platform=metal
   ```

   where:

   `/dev/sda`
   :   Specifies the target install device for your hardware.

   `<http_server>`
   :   Specifies the address of your web server.
6. Reboot the machine:

   ```
   $ reboot
   ```
7. Monitor the boot process. After the machine reboots, it attempts to join the cluster and generates certificate signing requests (CSRs).

**Verification**

* Verify that the new compute machine has joined the cluster and is in the `Ready` state:

  ```
  $ oc get nodes
  ```

#### [9.4.3. Approving the certificate signing requests for your machines](#installation-approve-csrs_adding-bare-metal-compute-vsphere-user-infra) Copy linkLink copied to clipboard!

To allow newly added machines to join your OpenShift Container Platform cluster, confirm that the cluster approves pending certificate signing requests (CSRs), or approve them yourself. Approve client requests first, then server requests.

**Prerequisites**

* You added machines to your cluster.

**Procedure**

1. Confirm that the cluster recognizes the machines:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME      STATUS    ROLES   AGE  VERSION
   master-0  Ready     master  63m  v1.35.4
   master-1  Ready     master  63m  v1.35.4
   master-2  Ready     master  64m  v1.35.4
   ```

   The output lists all of the machines that you created.

   Note

   The preceding output might not include the compute nodes until you approve some CSRs.
2. Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:

   ```
   $ oc get csr
   ```

   **Example output**

   ```
   NAME        AGE     REQUESTOR                                                                   CONDITION
   csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
   csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
   ...
   ```

   In this example, two machines are joining the cluster. You might see more approved CSRs in the list.
3. If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:

   Note

   You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates rotate, and more than two certificates are present for each node. You must approve all of these certificates. After you approve the client CSR, the kubelet creates a secondary CSR for the serving certificate, which requires manual approval. The `machine-approver` then automatically approves later serving certificate renewal requests if the kubelet requests a new certificate with the same parameters.

   Note

   For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If you do not approve a request, the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because the API server requires a serving certificate when it connects to the kubelet. Any operation that contacts the kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the `node-bootstrapper` service account in the `system:node` or `system:admin` groups submitted the CSR, and confirm the identity of the node.

   * To approve them individually, run the following command for each valid CSR:

     ```
     $ oc adm certificate approve <csr_name>
     ```

     where:

     `<csr_name>`
     :   Specifies the name of a CSR from the list of current CSRs.
   * To approve all pending CSRs, run the following command:

     ```
     $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
     ```

     Note

     Some Operators might not become available until you approve some CSRs. Each node submits two CSRs, so you might need to run the command to approve CSRs many times.
4. After you approve your client requests, review the server requests for each machine that you added to the cluster:

   ```
   $ oc get csr
   ```

   **Example output**

   ```
   NAME        AGE     REQUESTOR                                                                   CONDITION
   csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
   csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
   ...
   ```
5. If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:

   * To approve them individually, run the following command for each valid CSR:

     ```
     $ oc adm certificate approve <csr_name>
     ```

     where:

     `<csr_name>`
     :   Specifies the name of a CSR from the list of current CSRs.
   * To approve all pending CSRs, run the following command:

     ```
     $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
     ```
6. After you approve all client and server CSRs, the machines have the `Ready` status. Verify this by running the following command:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME      STATUS    ROLES   AGE  VERSION
   master-0  Ready     master  73m  v1.35.4
   master-1  Ready     master  73m  v1.35.4
   master-2  Ready     master  74m  v1.35.4
   worker-0  Ready     worker  11m  v1.35.4
   worker-1  Ready     worker  11m  v1.35.4
   ```

   Note

   You might need to wait a few minutes after approval of the server CSRs for the machines to change to the `Ready` status.

#### [9.4.4. Remove the cloud provider uninitialized taint from bare-metal nodes](#bare-metal-vsphere-remove-uninit-taint_adding-bare-metal-compute-vsphere-user-infra) Copy linkLink copied to clipboard!

After a bare-metal node joins a VMware vSphere cluster, the vSphere Cloud Controller Manager (CCM) cannot remove the `node.cloudprovider.kubernetes.io/uninitialized` taint automatically. You must manually remove this taint so that workloads can be scheduled on the node.

The vSphere CCM attempts to initialize each node by searching vCenter for a matching virtual machine. Because a bare-metal node is physical hardware and not a VM in vCenter, the CCM cannot find a match and never removes the taint automatically.

Note

The CCM logs errors similar to `No VM found` for bare-metal nodes. These errors are expected and do not indicate a problem with the node or the cluster.

**Prerequisites**

* The bare-metal node has joined the cluster and its certificate signing requests (CSRs) have been approved.
* You have installed the OpenShift CLI (`oc`).
* You have cluster administrator privileges.

**Procedure**

* Remove the `node.cloudprovider.kubernetes.io/uninitialized` taint from each bare-metal node by running the following command:

  ```
  $ oc adm taint nodes <node_name> node.cloudprovider.kubernetes.io/uninitialized:NoSchedule-
  ```

  Replace `<node_name>` with the name of the bare-metal node as shown in the output of `oc get nodes`.

**Verification**

* Verify that the taint has been removed by running the following command and confirming that `node.cloudprovider.kubernetes.io/uninitialized` does not appear in the output:

  ```
  $ oc describe node <node_name> | grep Taint
  ```

  Replace `<node_name>` with the name of the bare-metal node as shown in the output of `oc get nodes`.

### [9.5. Adding compute machines to bare metal](#adding-bare-metal-compute-user-infra) Copy linkLink copied to clipboard!

To scale your OpenShift Container Platform cluster on bare-metal or platform-agnostic infrastructure, you can add more compute machines. Create RHCOS machines, then approve their certificate signing requests.

#### [9.5.1. Prerequisites](#adding-bare-metal-compute-user-infra-prereqs_adding-bare-metal-compute-user-infra) Copy linkLink copied to clipboard!

There are several prerequisites that must be completed before you add compute machines to your cluster.

The following prerequisites must be met:

* You [installed a cluster on bare metal](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal).
* You [installed a cluster on any platform](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_any_platform/#installing-platform-agnostic).
* You have installation media and Red Hat Enterprise Linux CoreOS (RHCOS) images that you used to create your cluster. If you do not have these files, you must obtain them by following the instructions in the [installation procedure](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#installing-bare-metal).
* If a DHCP server is available for your user-provisioned infrastructure, you have added the details for the additional compute machines to your DHCP server configuration. This includes a persistent IP address, DNS server information, and a hostname for each machine.
* You have updated your DNS configuration to include the record name and IP address of each compute machine that you are adding. You have validated that DNS lookup and reverse DNS lookup resolve correctly.

Important

If you do not have access to the Red Hat Enterprise Linux CoreOS (RHCOS) images that were used to create your cluster, you can add more compute machines to your OpenShift Container Platform cluster with newer versions of Red Hat Enterprise Linux CoreOS (RHCOS) images. For instructions, see [Adding new nodes to UPI cluster fails after upgrading to OpenShift 4.6+](https://access.redhat.com/solutions/5514051).

#### [9.5.2. Creating Red Hat Enterprise Linux CoreOS (RHCOS) machines](#creating-rhcos-machines-bare-metal) Copy linkLink copied to clipboard!

Before you add more compute machines to a cluster that you installed on bare metal infrastructure, you must create RHCOS machines for it to use. You can either use an ISO image or network PXE booting to create the machines.

Note

You must use the same ISO image that you used to install a cluster to deploy all new nodes in a cluster. It is recommended to use the same Ignition config file. The nodes automatically upgrade themselves on the first boot before running the workloads. You can add the nodes before or after the upgrade.

##### [9.5.2.1. Creating RHCOS machines by using an ISO image](#machine-user-infra-machines-iso_adding-bare-metal-compute-user-infra) Copy linkLink copied to clipboard!

To scale your OpenShift Container Platform bare metal cluster, you can create more Red Hat Enterprise Linux CoreOS (RHCOS) compute machines by using an ISO image.

**Prerequisites**

* You have obtained the URL of the Ignition config file for the compute machines for your cluster. You uploaded this file to your HTTP server during installation.
* You must have the OpenShift CLI (`oc`) installed.

**Procedure**

1. Extract the Ignition config file from the cluster by running the following command:

   ```
   $ oc extract -n openshift-machine-api secret/worker-user-data-managed --keys=userData --to=- > worker.ign
   ```
2. Upload the `worker.ign` Ignition config file you exported from your cluster to your HTTP server. Note the URLs of these files.
3. You can validate that the ignition files are available on the URLs. The following example gets the Ignition config files for the compute node:

   ```
   $ curl -k http://<HTTP_server>/worker.ign
   ```
4. You can access the ISO image for booting your new machine by running the following command:

   ```
   RHCOS_VHD_ORIGIN_URL=$(oc -n openshift-machine-config-operator get configmap/coreos-bootimages -o jsonpath='{.data.stream}' | jq -r '.architectures.<architecture>.artifacts.metal.formats.iso.disk.location')
   ```
5. Use the ISO file to install RHCOS on more compute machines. Use the same method that you used when you created machines before you installed the cluster:

   * Burn the ISO image to a disk and boot it directly.
   * Use ISO redirection with a LOM interface.
6. Boot the RHCOS ISO image without specifying any options, or interrupting the live boot sequence. Wait for the installer to boot into a shell prompt in the RHCOS live environment.

   Note

   You can interrupt the RHCOS installation boot process to add kernel arguments. However, for this ISO procedure you must use the `coreos-installer` command as outlined in the following steps, instead of adding kernel arguments.
7. Run the `coreos-installer` command by using `sudo`. The `core` user does not have the root privileges required to perform the installation. Specify the options that meet your installation requirements. At a minimum, you must specify the URL that points to the Ignition config file for the node type, and the device that you are installing to.

   ```
   $ sudo coreos-installer install --ignition-url=http://<HTTP_server>/<node_type>.ign <device> --ignition-hash=sha512-<digest>
   ```

   where:

   `<digest>`
   :   Specifies the Ignition config file SHA512 digest obtained through an HTTP URL to validate the authenticity of the Ignition config file on the cluster node.

       Note

       If you want to provide your Ignition config files through an HTTPS server that uses TLS, you can add the internal certificate authority (CA) to the system trust store before running `coreos-installer`.

       The following example initializes a compute node installation to the `/dev/sda` device. The Ignition config file for the compute node is obtained from an HTTP web server with the IP address 192.168.1.2:

       ```
       $ sudo coreos-installer install --ignition-url=http://192.168.1.2:80/installation_directory/worker.ign /dev/sda --ignition-hash=sha512-a5a2d43879223273c9b60af66b44202a1d1248fc01cf156c46d4a79f552b6bad47bc8cc78ddf0116e80c59d2ea9e32ba53bc807afbca581aa059311def2c3e3b
       ```
8. Monitor the progress of the RHCOS installation on the console of the machine.

   Important

   Ensure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of RHCOS installation issues that might arise.
9. Continue to create more compute machines for your cluster.

##### [9.5.2.2. Creating RHCOS machines by PXE or iPXE booting](#machine-user-infra-machines-pxe_adding-bare-metal-compute-user-infra) Copy linkLink copied to clipboard!

To scale your OpenShift Container Platform bare metal cluster, you can create more Red Hat Enterprise Linux CoreOS (RHCOS) compute machines by using PXE or iPXE booting.

**Prerequisites**

* You have obtained the URL of the Ignition config file for the compute machines for your cluster. You uploaded this file to your HTTP server during installation.
* You have obtained the URLs of the RHCOS ISO image, compressed metal BIOS, `kernel`, and `initramfs` files that you uploaded to your HTTP server during cluster installation.
* You have access to the PXE booting infrastructure that you used to create the machines for your OpenShift Container Platform cluster during installation. The machines must boot from their local disks after RHCOS is installed on them.
* If you use UEFI, you have access to the `grub.conf` file that you modified during OpenShift Container Platform installation.

**Procedure**

1. Confirm that your PXE or iPXE installation for the RHCOS images is correct.

   * For PXE:

     ```
     DEFAULT pxeboot
     TIMEOUT 20
     PROMPT 0
     LABEL pxeboot
         KERNEL http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture>
         APPEND initrd=http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/worker.ign coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img
     ```

     where:

     `KERNEL`
     :   Specifies the location of the live `kernel` file that you uploaded to your HTTP server.

     `APPEND`
     :   Specifies the locations of the RHCOS files that you uploaded to your HTTP server:

     `initrd`
     :   Specifies the location of the live `initramfs` file.

     `coreos.inst.ignition_url`
     :   Specifies the location of the worker Ignition config file. This parameter supports only HTTP and HTTPS.

     `coreos.live.rootfs_url`
     :   Specifies the location of the live `rootfs` file. This parameter supports only HTTP and HTTPS.

         Note

         This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `APPEND` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information on setting up a serial terminal and/or console in RHCOS, see "How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?".
   * For iPXE (`x86_64` + `aarch64`):

     ```
     kernel http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture> initrd=main coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/worker.ign
     initrd --name main http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img
     boot
     ```

     where:

     `kernel`
     :   Specifies the location of the `kernel` file that you uploaded to your HTTP server.

     `initrd=main`
     :   Specifies an argument that is required for booting on UEFI systems.

     `coreos.live.rootfs_url`
     :   Specifies the location of the `rootfs` file that you uploaded to your HTTP server.

     `coreos.inst.ignition_url`
     :   Specifies the location of the worker Ignition config file that you uploaded to your HTTP server.

     `initrd --name main`
     :   Specifies the location of the `initramfs` file that you uploaded to your HTTP server.

         Note

         + If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC named `eno1`, set `ip=eno1:dhcp`.
         + This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `kernel` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information on setting up a serial terminal and/or console in RHCOS, see "How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?" in the Additional resources section and "Enabling the serial console for PXE and ISO installation" in the "Advanced RHCOS installation configuration" section.

         Note

         To network boot the CoreOS `kernel` on `aarch64` architecture, you need to use a version of iPXE build with the `IMAGE_GZIP` option enabled. For more information, see "IMAGE\_GZIP option in iPXE".
   * For PXE (with UEFI and GRUB as second stage) on `aarch64`:

     ```
     menuentry 'Install CoreOS' {
         linux rhcos-<version>-live-kernel-<architecture>  coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/worker.ign
         initrd rhcos-<version>-live-initramfs.<architecture>.img
     }
     ```

     where:

     `linux`
     :   Specifies the location of the live `kernel` file on your TFTP server.

     `coreos.live.rootfs_url`
     :   Specifies the location of the live `rootfs` file.

     `coreos.inst.ignition_url`
     :   Specifies the location of the worker Ignition config file.

     `initrd`
     :   Specifies the location of the live `initramfs` file on your TFTP server.

         Note

         If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC named `eno1`, set `ip=eno1:dhcp`.
2. Use the PXE or iPXE infrastructure to create the required compute machines for your cluster.

#### [9.5.3. Approving the certificate signing requests for your machines](#installation-approve-csrs_adding-bare-metal-compute-user-infra) Copy linkLink copied to clipboard!

To allow newly added machines to join your OpenShift Container Platform cluster, confirm that the cluster approves pending certificate signing requests (CSRs), or approve them yourself. Approve client requests first, then server requests.

**Prerequisites**

* You added machines to your cluster.

**Procedure**

1. Confirm that the cluster recognizes the machines:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME      STATUS    ROLES   AGE  VERSION
   master-0  Ready     master  63m  v1.35.4
   master-1  Ready     master  63m  v1.35.4
   master-2  Ready     master  64m  v1.35.4
   ```

   The output lists all of the machines that you created.

   Note

   The preceding output might not include the compute nodes until you approve some CSRs.
2. Review the pending CSRs and ensure that you see the client requests with the `Pending` or `Approved` status for each machine that you added to the cluster:

   ```
   $ oc get csr
   ```

   **Example output**

   ```
   NAME        AGE     REQUESTOR                                                                   CONDITION
   csr-8b2br   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
   csr-8vnps   15m     system:serviceaccount:openshift-machine-config-operator:node-bootstrapper   Pending
   ...
   ```

   In this example, two machines are joining the cluster. You might see more approved CSRs in the list.
3. If the CSRs were not approved, after all of the pending CSRs for the machines you added are in `Pending` status, approve the CSRs for your cluster machines:

   Note

   You must approve your CSRs within an hour of adding the machines to the cluster. If you do not approve them within an hour, the certificates rotate, and more than two certificates are present for each node. You must approve all of these certificates. After you approve the client CSR, the kubelet creates a secondary CSR for the serving certificate, which requires manual approval. The `machine-approver` then automatically approves later serving certificate renewal requests if the kubelet requests a new certificate with the same parameters.

   Note

   For clusters running on platforms that are not machine API enabled, such as bare metal and other user-provisioned infrastructure, you must implement a method of automatically approving the kubelet serving certificate requests (CSRs). If you do not approve a request, the `oc exec`, `oc rsh`, and `oc logs` commands cannot succeed, because the API server requires a serving certificate when it connects to the kubelet. Any operation that contacts the kubelet endpoint requires this certificate approval to be in place. The method must watch for new CSRs, confirm that the `node-bootstrapper` service account in the `system:node` or `system:admin` groups submitted the CSR, and confirm the identity of the node.

   * To approve them individually, run the following command for each valid CSR:

     ```
     $ oc adm certificate approve <csr_name>
     ```

     where:

     `<csr_name>`
     :   Specifies the name of a CSR from the list of current CSRs.
   * To approve all pending CSRs, run the following command:

     ```
     $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
     ```

     Note

     Some Operators might not become available until you approve some CSRs. Each node submits two CSRs, so you might need to run the command to approve CSRs many times.
4. After you approve your client requests, review the server requests for each machine that you added to the cluster:

   ```
   $ oc get csr
   ```

   **Example output**

   ```
   NAME        AGE     REQUESTOR                                                                   CONDITION
   csr-bfd72   5m26s   system:node:ip-10-0-50-126.us-east-2.compute.internal                       Pending
   csr-c57lv   5m26s   system:node:ip-10-0-95-157.us-east-2.compute.internal                       Pending
   ...
   ```
5. If the remaining CSRs are not approved, and are in the `Pending` status, approve the CSRs for your cluster machines:

   * To approve them individually, run the following command for each valid CSR:

     ```
     $ oc adm certificate approve <csr_name>
     ```

     where:

     `<csr_name>`
     :   Specifies the name of a CSR from the list of current CSRs.
   * To approve all pending CSRs, run the following command:

     ```
     $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs oc adm certificate approve
     ```
6. After you approve all client and server CSRs, the machines have the `Ready` status. Verify this by running the following command:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME      STATUS    ROLES   AGE  VERSION
   master-0  Ready     master  73m  v1.35.4
   master-1  Ready     master  73m  v1.35.4
   master-2  Ready     master  74m  v1.35.4
   worker-0  Ready     worker  11m  v1.35.4
   worker-1  Ready     worker  11m  v1.35.4
   ```

   Note

   You might need to wait a few minutes after approval of the server CSRs for the machines to change to the `Ready` status.

## [Chapter 10. Managing control plane machines](#managing-control-plane-machines) Copy linkLink copied to clipboard!

### [10.1. About control plane machine sets](#cpmso-about) Copy linkLink copied to clipboard!

With control plane machine sets, you can automate management of the control plane machine resources within your OpenShift Container Platform cluster, simplifying upgrades and recovery from degraded control plane machines.

Important

Control plane machine sets cannot manage compute machines, and compute machine sets cannot manage control plane machines.

Control plane machine sets provide for control plane machines similar management capabilities as compute machine sets provide for compute machines. However, these two types of machine sets are separate custom resources defined within the Machine API and have several fundamental differences in their architecture and functionality.

#### [10.1.1. Control Plane Machine Set Operator overview](#cpmso-overview_cpmso-about) Copy linkLink copied to clipboard!

You can use the Control Plane Machine Set Operator to automate management of control plane machines in your OpenShift Container Platform cluster, including automated replacement of degraded machines and rollout of configuration changes.

When the state of the cluster control plane machine set is set to `Active`, the Operator ensures that the cluster has the correct number of control plane machines with the specified configuration. This allows the automated replacement of degraded control plane machines and rollout of changes to the control plane.

A cluster has only one control plane machine set, and the Operator only manages objects in the `openshift-machine-api` namespace.

##### [10.1.1.1. Control Plane Machine Set Operator limitations](#cpmso-limitations_cpmso-about) Copy linkLink copied to clipboard!

Before using the Control Plane Machine Set Operator, review platform support, cluster requirements, and unsupported configurations to ensure compatibility with your environment.

* Only Amazon Web Services (AWS), Google Cloud, IBM Power® Virtual Server, Microsoft Azure, Nutanix, VMware vSphere, and Red Hat OpenStack Platform (RHOSP) clusters are supported.
* Clusters that do not have preexisting machines that represent the control plane nodes cannot use a control plane machine set or enable the use of a control plane machine set after installation. Generally, preexisting control plane machines are only present if the installation program provisioned the cluster infrastructure.

  To check if a cluster has the required preexisting control plane machines, run the following command as a user with administrator privileges:

  ```
  $ oc get machine \
    -n openshift-machine-api \
    -l machine.openshift.io/cluster-api-machine-role=master
  ```

  **Example output showing preexisting control plane machines**

  ```
  NAME                    PHASE     TYPE         REGION      ZONE         AGE
  <infrastructure_id>-master-0   Running   m6i.xlarge   us-west-1   us-west-1a   5h19m
  <infrastructure_id>-master-1   Running   m6i.xlarge   us-west-1   us-west-1b   5h19m
  <infrastructure_id>-master-2   Running   m6i.xlarge   us-west-1   us-west-1a   5h19m
  ```

  **Example output missing preexisting control plane machines**

  ```
  No resources found in openshift-machine-api namespace.
  ```
* The Operator requires the Machine API Operator to be operational and is therefore not supported on clusters with manually provisioned machines. When installing a OpenShift Container Platform cluster with manually provisioned machines for a platform that creates an active generated `ControlPlaneMachineSet` custom resource (CR), you must remove the Kubernetes manifest files that define the control plane machine set as instructed in the installation process.
* Only clusters with three control plane machines are supported.
* Horizontal scaling of the control plane is not supported.
* Deploying Azure control plane machines on Ephemeral operating system disks increases risk for data loss and is not supported.
* Deploying control plane machines as AWS Spot Instances, Google Cloud preemptible VMs, or Azure Spot VMs is not supported.

  Important

  Attempting to deploy control plane machines as AWS Spot Instances, Google Cloud preemptible VMs, or Azure Spot VMs might cause the cluster to lose etcd quorum. A cluster that loses all control plane machines simultaneously is unrecoverable.
* Making changes to the control plane machine set during or before installation is not supported. You must make any changes to the control plane machine set only after installation.

### [10.2. Getting started with control plane machine sets](#cpmso-getting-started) Copy linkLink copied to clipboard!

Set up the control plane machine set to enable automated management, recovery, and configuration updates for control plane machines in your cluster.

The process for getting started with control plane machine sets depends on the state of the `ControlPlaneMachineSet` custom resource (CR) in your cluster.

Clusters with an active generated CR
:   Clusters that have a generated CR with an active state use the control plane machine set by default. No administrator action is required.

Clusters with an inactive generated CR
:   For clusters that include an inactive generated CR, you must review the CR configuration and [activate the CR](#cpmso-activating_cpmso-getting-started "10.2.3. Activating the control plane machine set custom resource").

Clusters without a generated CR
:   For clusters that do not include a generated CR, you must [create and activate a CR](#cpmso-creating-cr_cpmso-getting-started "10.2.4. Creating a control plane machine set custom resource") with the appropriate configuration for your cluster.

If you are uncertain about the state of the `ControlPlaneMachineSet` CR in your cluster, you can [verify the CR status](#cpmso-checking-status_cpmso-getting-started "10.2.2. Checking the control plane machine set custom resource state").

#### [10.2.1. Supported cloud providers](#cpmso-platform-matrix_cpmso-getting-started) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, the control plane machine set is supported for Amazon Web Services (AWS), Google Cloud, Microsoft Azure, Nutanix, and VMware vSphere clusters.

The status of the control plane machine set after installation depends on your cloud provider and the version of OpenShift Container Platform that you installed on your cluster.

Expand

Table 10.1. Control plane machine set implementation for OpenShift Container Platform 4.22

| Cloud provider | Active by default | Generated CR | Manual CR required |
| --- | --- | --- | --- |
| Amazon Web Services (AWS) | X [1] | X |  |
| Google Cloud | X [2] | X |  |
| Microsoft Azure | X [2] | X |  |
| Nutanix | X [3] | X |  |
| Red Hat OpenStack Platform (RHOSP) | X [3] | X |  |
| VMware vSphere | X [4] | X |  |

Show more

1. AWS clusters that are upgraded from version 4.11 or earlier require [CR activation](#cpmso-activating_cpmso-getting-started "10.2.3. Activating the control plane machine set custom resource").
2. Google Cloud and Azure clusters that are upgraded from version 4.12 or earlier require [CR activation](#cpmso-activating_cpmso-getting-started "10.2.3. Activating the control plane machine set custom resource").
3. Nutanix and RHOSP clusters that are upgraded from version 4.13 or earlier require [CR activation](#cpmso-activating_cpmso-getting-started "10.2.3. Activating the control plane machine set custom resource").
4. vSphere clusters that are upgraded from version 4.15 or earlier require [CR activation](#cpmso-activating_cpmso-getting-started "10.2.3. Activating the control plane machine set custom resource").

#### [10.2.2. Checking the control plane machine set custom resource state](#cpmso-checking-status_cpmso-getting-started) Copy linkLink copied to clipboard!

Check the state of the control plane machine set custom resource to determine if it is active, inactive, or missing before making configuration changes.

**Procedure**

* Determine the state of the CR by running the following command:

  ```
  $ oc get controlplanemachineset.machine.openshift.io cluster \
    --namespace openshift-machine-api
  ```

  + A result of `Active` indicates that the `ControlPlaneMachineSet` CR exists and is activated. No administrator action is required.
  + A result of `Inactive` indicates that a `ControlPlaneMachineSet` CR exists but is not activated.
  + A result of `NotFound` indicates that there is no existing `ControlPlaneMachineSet` CR.

**Next steps**

To use the control plane machine set, you must ensure that a `ControlPlaneMachineSet` CR with the correct settings for your cluster exists.

* If your cluster has an existing CR, you must verify that the configuration in the CR is correct for your cluster.
* If your cluster does not have an existing CR, you must create one with the correct configuration for your cluster.

#### [10.2.3. Activating the control plane machine set custom resource](#cpmso-activating_cpmso-getting-started) Copy linkLink copied to clipboard!

To use the control plane machine set, you must ensure that a `ControlPlaneMachineSet` custom resource (CR) with the correct settings for your cluster exists. On a cluster with a generated CR, you must verify that the configuration in the CR is correct for your cluster and activate it.

Note

For more information about the parameters in the CR, see "Control plane machine set configuration".

**Procedure**

1. View the configuration of the CR by running the following command:

   ```
   $ oc --namespace openshift-machine-api edit controlplanemachineset.machine.openshift.io cluster
   ```
2. Change the values of any fields that are incorrect for your cluster configuration.
3. When the configuration is correct, activate the CR by setting the `.spec.state` field to `Active` and saving your changes.

   Important

   To activate the CR, you must change the `.spec.state` field to `Active` in the same `oc edit` session that you use to update the CR configuration. If the CR is saved with the state left as `Inactive`, the control plane machine set generator resets the CR to its original settings.

#### [10.2.4. Creating a control plane machine set custom resource](#cpmso-creating-cr_cpmso-getting-started) Copy linkLink copied to clipboard!

To use the control plane machine set, you must ensure that a `ControlPlaneMachineSet` custom resource (CR) with the correct settings for your cluster exists. On a cluster without a generated CR, you must create the CR manually and activate it.

Note

For more information about the structure and parameters of the CR, see "Control plane machine set configuration".

**Procedure**

1. Create a YAML file using the following template:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   metadata:
     name: cluster
     namespace: openshift-machine-api
   spec:
     replicas: 3
     selector:
       matchLabels:
         machine.openshift.io/cluster-api-cluster: <cluster_id>
         machine.openshift.io/cluster-api-machine-role: master
         machine.openshift.io/cluster-api-machine-type: master
     state: Active
     strategy:
       type: RollingUpdate
     template:
       machineType: machines_v1beta1_machine_openshift_io
       machines_v1beta1_machine_openshift_io:
         failureDomains:
           platform: <platform>
           <platform_failure_domains>
         metadata:
           labels:
             machine.openshift.io/cluster-api-cluster: <cluster_id>
             machine.openshift.io/cluster-api-machine-role: master
             machine.openshift.io/cluster-api-machine-type: master
         spec:
           providerSpec:
             value:
               <platform_provider_spec>
   ```

   where:

   `<cluster_id>`
   :   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You must specify this value when you create a `ControlPlaneMachineSet` CR. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

       ```
       $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
       ```

   `state: Active`
   :   Specifies the state of the Operator. When the state is `Inactive`, the Operator is not operational. You can activate the Operator by setting the value to `Active`.

       Important

       Before you activate the CR, you must ensure that its configuration is correct for your cluster requirements.

   `type: RollingUpdate`
   :   Specifies the update strategy for the cluster. Valid values are `OnDelete` and `RollingUpdate`. The default value is `RollingUpdate`. For more information about update strategies, see "Updating the control plane configuration".

   `platform: <platform>`
   :   Specifies the cloud provider platform name. Valid values are `AWS`, `Azure`, `GCP`, `Nutanix`, `VSphere`, and `OpenStack`.

   `<platform_failure_domains>`
   :   Specifies the failure domains configuration for the cluster. The format and values of this section are provider-specific. For more information, see the sample failure domain configuration for your cloud provider.

   `<platform_provider_spec>`
   :   Specifies the provider spec configuration for the cluster. The format and values of this section are provider-specific. For more information, see the sample provider specification for your cloud provider.
2. Refer to the sample YAML for a control plane machine set CR and populate your file with values that are appropriate for your cluster configuration.
3. Refer to the sample failure domain configuration and sample provider specification for your cloud provider and update those sections of your file with the appropriate values.
4. When the configuration is correct, activate the CR by setting the `.spec.state` field to `Active` and saving your changes.
5. Create the CR from your YAML file by running the following command:

   ```
   $ oc create -f <control_plane_machine_set>.yaml
   ```

   where `<control_plane_machine_set>` specifies the name of the YAML file that contains the CR configuration.

### [10.3. Managing control plane machines with control plane machine sets](#cpmso-managing-machines) Copy linkLink copied to clipboard!

Control plane machine sets automate several essential aspects of control plane management to reduce operational overhead and ensure consistency.

#### [10.3.1. Updating the control plane configuration](#cpmso-feat-config-update_cpmso-managing-machines) Copy linkLink copied to clipboard!

Update the control plane machine set specification to modify control plane machine configuration and trigger automatic or manual replacements.

The Control Plane Machine Set Operator monitors the control plane machines and compares their configuration with the specification in the control plane machine set CR. When there is a discrepancy between the specification in the CR and the configuration of a control plane machine, the Operator marks that control plane machine for replacement.

Note

For more information about the parameters in the CR, see "Control plane machine set configuration".

**Prerequisites**

* Your cluster has an activated and functioning Control Plane Machine Set Operator.

**Procedure**

1. Edit your control plane machine set CR by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster \
     -n openshift-machine-api
   ```
2. Change the values of any fields that you want to update in your cluster configuration.
3. Save your changes.

**Next steps**

* For clusters that use the default `RollingUpdate` update strategy, the control plane machine set propagates changes to your control plane configuration automatically.
* For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

##### [10.3.1.1. Automatic updates to the control plane configuration](#cpmso-feat-auto-update_cpmso-managing-machines) Copy linkLink copied to clipboard!

The `RollingUpdate` update strategy automatically propagates changes to your control plane configuration to minimize manual intervention.

This update strategy is the default configuration for the control plane machine set.

For clusters that use the `RollingUpdate` update strategy, the Operator creates a replacement control plane machine with the configuration that is specified in the CR. When the replacement control plane machine is ready, the Operator deletes the control plane machine that is marked for replacement. The replacement machine then joins the control plane.

If multiple control plane machines are marked for replacement, the Operator protects etcd health during replacement by repeating this replacement process one machine at a time until it has replaced each machine.

##### [10.3.1.2. Manual updates to the control plane configuration](#cpmso-feat-ondelete-update_cpmso-managing-machines) Copy linkLink copied to clipboard!

Use the `OnDelete` update strategy to test configuration changes on individual control plane machines before applying them cluster-wide. Manually replacing machines allows you to test changes to your configuration on a single machine before applying the changes more broadly.

For clusters that are configured to use the `OnDelete` update strategy, the Operator creates a replacement control plane machine when you delete an existing machine. When the replacement control plane machine is ready, the etcd Operator allows the existing machine to be deleted. The replacement machine then joins the control plane.

If multiple control plane machines are deleted, the Operator creates all of the required replacement machines simultaneously. The Operator maintains etcd health by preventing more than one machine being removed from the control plane at once.

#### [10.3.2. Replacing a control plane machine](#cpmso-feat-replace_cpmso-managing-machines) Copy linkLink copied to clipboard!

Replace a control plane machine to apply updated configurations or recover from hardware issues while maintaining cluster stability. The control plane machine set replaces the deleted machine with one using the specification in the control plane machine set custom resource (CR).

**Prerequisites**

* If your cluster runs on Red Hat OpenStack Platform (RHOSP) and you need to evacuate a compute server, such as for an upgrade, you must disable the RHOSP compute node that the machine runs on by running the following command:

  ```
  $ openstack compute service set <target_node_host_name> nova-compute --disable
  ```

  For more information, see [Preparing to migrate](https://docs.redhat.com/en/documentation/red_hat_openstack_platform/17.1/html/configuring_the_compute_service_for_instance_creation/assembly_migrating-virtual-machine-instances-between-compute-nodes_migrating-instances#proc_preparing-to-migrate_migrating-instances) in the RHOSP documentation.

**Procedure**

1. List the control plane machines in your cluster by running the following command:

   ```
   $ oc get machines \
     -l machine.openshift.io/cluster-api-machine-role==master \
     -n openshift-machine-api
   ```
2. Delete a control plane machine by running the following command:

   ```
   $ oc delete machine \
     -n openshift-machine-api \
     <control_plane_machine_name>
   ```

   where `<control_plane_machine_name>` specifies the name of the control plane machine to delete.

   Note

   If you delete multiple control plane machines, the control plane machine set replaces them according to the configured update strategy:

   * For clusters that use the default `RollingUpdate` update strategy, the Operator replaces one machine at a time until each machine is replaced.
   * For clusters that are configured to use the `OnDelete` update strategy, the Operator creates all of the required replacement machines simultaneously.

   Both strategies maintain etcd health during control plane machine replacement.

### [10.4. Control plane machine set configuration](#cpmso-configuration) Copy linkLink copied to clipboard!

Use a control plane machine set to automate management and recovery of control plane machines in your cluster.

#### [10.4.1. Sample YAML for a control plane machine set custom resource](#cpmso-yaml-sample-cr_cpmso-configuration) Copy linkLink copied to clipboard!

Use this sample YAML as a starting point for creating or modifying control plane machine set configurations on any supported platform.

**Sample `ControlPlaneMachineSet` CR YAML file**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
  replicas: 3
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-cluster: <cluster_id>
      machine.openshift.io/cluster-api-machine-role: master
      machine.openshift.io/cluster-api-machine-type: master
  state: Active
  strategy:
    type: RollingUpdate
  template:
    machineType: machines_v1beta1_machine_openshift_io
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        platform: <platform>
        <platform_failure_domains>
      metadata:
        labels:
          machine.openshift.io/cluster-api-cluster: <cluster_id>
          machine.openshift.io/cluster-api-machine-role: master
          machine.openshift.io/cluster-api-machine-type: master
      spec:
        providerSpec:
          value:
            <platform_provider_spec>
```

where:

`name: cluster`
:   Specifies the name of the `ControlPlaneMachineSet` CR, which is `cluster`. Do not change this value.

`replicas: 3`
:   Specifies the number of control plane machines. Only clusters with three control plane machines are supported, so the `replicas` value is `3`. Horizontal scaling is not supported. Do not change this value.

`<cluster_id>`
:   Specifies the infrastructure ID that is based on the cluster ID that you set when you provisioned the cluster. You must specify this value when you create a `ControlPlaneMachineSet` CR. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

`state: Active`
:   Specifies the state of the Operator. When the state is `Inactive`, the Operator is not operational. You can activate the Operator by setting the value to `Active`.

    Important

    Before you activate the Operator, you must ensure that the `ControlPlaneMachineSet` CR configuration is correct for your cluster requirements. For more information about activating the Control Plane Machine Set Operator, see "Getting started with control plane machine sets".

`type: RollingUpdate`
:   Specifies the update strategy for the cluster. The allowed values are `OnDelete` and `RollingUpdate`. The default value is `RollingUpdate`. For more information about update strategies, see "Updating the control plane configuration".

`platform: <platform>`
:   Specifies the cloud provider platform name. Do not change this value.

`<platform_failure_domains>`
:   Specifies the failure domains configuration for the cluster. The format and values of this section are provider-specific. For more information, see the sample failure domain configuration for your cloud provider.

`<platform_provider_spec>`
:   Specifies the provider spec configuration for the cluster. The format and values of this section are provider-specific. For more information, see the sample provider specification for your cloud provider.

#### [10.4.2. Control plane machine set configuration options](#cpmso-config-options-overview_cpmso-configuration) Copy linkLink copied to clipboard!

Customize your control plane machine set to meet specific cluster requirements or naming conventions.

##### [10.4.2.1. Adding a custom prefix to control plane machine names](#cpmso-config-prefix_cpmso-configuration) Copy linkLink copied to clipboard!

Customize the prefix of control plane machine names to distinguish machines across environments or match your naming conventions.

**Procedure**

1. Edit the `ControlPlaneMachineSet` CR by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster \
     -n openshift-machine-api
   ```
2. Edit the `.spec.machineNamePrefix` field of the `ControlPlaneMachineSet` CR:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   metadata:
     name: cluster
     namespace: openshift-machine-api
   spec:
     machineNamePrefix: <machine_prefix>
   # ...
   ```

   where `<machine_prefix>` specifies a prefix name that follows the requirements for a lowercase RFC 1123 subdomain.

   Important

   A lowercase RFC 1123 subdomain must consist of only lowercase alphanumeric characters, hyphens ('-'), and periods ('.'). Each block, separated by periods, must start and end with an alphanumeric character. Hyphens are not allowed at the start or end of a block, and consecutive periods are not permitted.
3. Save your changes.

**Next steps**

* If you changed only the value of the `machineNamePrefix` parameter, clusters that use the default `RollingUpdate` update strategy are not automatically updated. To propagate this change, you must replace your control plane machines manually, regardless of the update strategy for the cluster. For more information, see "Replacing a control plane machine".

#### [10.4.3. Provider-specific configuration options](#cpmso-config-provider-specific_cpmso-configuration) Copy linkLink copied to clipboard!

Configure the provider-specific sections of your control plane machine set manifest for your cloud platform.

The `<platform_provider_spec>` and `<platform_failure_domains>` sections of the control plane machine set manifests are provider specific. For provider-specific configuration options for your cluster, see the documentation for your cloud provider.

### [10.5. Configuration options for control plane machines](#configuration-options-for-control-plane-machines) Copy linkLink copied to clipboard!

#### [10.5.1. Control plane configuration options for Amazon Web Services](#cpmso-config-options-aws) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

The following example YAML snippets show provider specification and failure domain configurations for an AWS cluster.

##### [10.5.1.1. Sample AWS provider specification](#cpmso-yaml-provider-spec-aws_cpmso-config-options-aws) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification.

The following example YAML illustrates a valid configuration for an Amazon Web Services (AWS) cluster.

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates.

You can omit any field that has a value set in the failure domain section of the CR.

In the following example, the `<cluster_id>` string is the infrastructure ID. The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

```
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```

**Sample AWS `providerSpec` values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            ami:
              id: ami-<ami_id_string>
            apiVersion: machine.openshift.io/v1beta1
            blockDevices:
            - ebs:
                encrypted: true
                iops: 0
                kmsKey:
                  arn: ""
                volumeSize: 120
                volumeType: gp3
            credentialsSecret:
              name: aws-cloud-credentials
            deviceIndex: 0
            iamInstanceProfile:
              id: <cluster_id>-master-profile
            instanceType: m6i.xlarge
            kind: AWSMachineProviderConfig
            loadBalancers:
            - name: <cluster_id>-int
              type: network
            - name: <cluster_id>-ext
              type: network
            metadata:
              creationTimestamp: null
            metadataServiceOptions: {}
            placement:
              region: <region>
              availabilityZone: ""
              tenancy:
            securityGroups:
              - filters:
                - name: tag:Name
                  values:
                  - <cluster_id>-node
              - filters:
                - name: tag:Name
                  values:
                  - <cluster_id>-lb
              - filters:
                - name: tag:Name
                  values:
                  - <cluster_id>-controlplane
            subnet: {}
            userDataSecret:
              name: master-user-data
```

where:

`<ami_id_string>`
:   Specifies the Red Hat Enterprise Linux CoreOS (RHCOS) Amazon Machine Images (AMI) ID for the cluster. The AMI must belong to the same region as the cluster. If you want to use an AWS Marketplace image, you must complete the OpenShift Container Platform subscription from the [AWS Marketplace](https://aws.amazon.com/marketplace/fulfillment?productId=59ead7de-2540-4653-a8b0-fa7926d5c845) to obtain an AMI ID for your region.

`spec.template.spec.providerSpec.value.blockDevices.ebs`
:   Specifies the configuration of an encrypted Amazon Elastic Block Store (Amazon EBS) volume.

`spec.template.spec.providerSpec.value.credentialsSecret.name`
:   Specifies the secret name for the cluster. Do not change this value.

`spec.template.spec.providerSpec.value.iamInstanceProfile`
:   Specifies the AWS Identity and Access Management (IAM) instance profile. Do not change this value.

`spec.template.spec.providerSpec.value.instanceType`
:   Specifies the AWS instance type for the control plane.

`spec.template.spec.providerSpec.value.kind`
:   Specifies the cloud provider platform type. Do not change this value.

`spec.template.spec.providerSpec.value.loadBalancers`
:   Specifies the internal (`int`) and external (`ext`) load balancers for the cluster.

    Note

    You can omit the external (`ext`) load balancer parameters on private OpenShift Container Platform clusters.

`spec.template.spec.providerSpec.value.placement`
:   Specifies where to create the control plane instance in AWS. The following keys in this stanza specify additional details:

    `region`
    :   Specifies the AWS region for the cluster.

    `availabilityZone`
    :   This parameter is in the failure domain configuration and has an empty value here.

    If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain.

`tenancy`
:   Specifies the AWS Dedicated Instance configuration for the control plane. For more information, see AWS documentation about [Dedicated Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-instance.html). The following values are valid:

    * `default`: The Dedicated Instance runs on shared hardware.
    * `dedicated`: The Dedicated Instance runs on single-tenant hardware.
    * `host`: The Dedicated Instance runs on a Dedicated Host, which is an isolated server with configurations that you can control.

`spec.template.spec.providerSpec.value.securityGroups`
:   Specifies the control plane machines security group.

`spec.template.spec.providerSpec.value.subnet`
:   This parameter is in the failure domain configuration and has an empty value here.

    If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain.

    Note

    If the failure domain configuration does not specify a value, the control plane machines use the value in the provider specification.

`spec.template.spec.providerSpec.value.userDataSecret`
:   Specifies the control plane user data secret. Do not change this value.

##### [10.5.1.2. Sample AWS failure domain configuration](#cpmso-yaml-failure-domain-aws_cpmso-config-options-aws) Copy linkLink copied to clipboard!

To prevent downtime for your applications due to the failure of a single Amazon Web Services (AWS) region, you can configure failure domains in the control plane machine set by configuring appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` object.

The control plane machine set concept of a failure domain is analogous to the AWS concept of an [*Availability Zone (AZ)*](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones). The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible.

When configuring AWS failure domains in the control plane machine set, you must specify the availability zone name and the subnet to use.

**Sample AWS failure domain values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        aws:
        - placement:
            availabilityZone: <aws_zone_a>
          subnet:
            filters:
            - name: tag:Name
              values:
              - <cluster_id>-subnet-private-<aws_zone_a>
            type: Filters
        - placement:
            availabilityZone: <aws_zone_b>
          subnet:
            filters:
            - name: tag:Name
              values:
              - <cluster_id>-subnet-private-<aws_zone_b>
            type: Filters
        platform: AWS
# ...
```

where:

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.placement.availabilityZone: <aws_zone_a>`
:   Specifies an AWS availability zone for the first failure domain.

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet`
:   Specifies a subnet configuration. In this example, the subnet type is `Filters`, so there is a `filters` stanza.

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet.filters.values: <cluster_id>-subnet-private-<aws_zone_a>`
:   Specifies the subnet name for the first failure domain, using the infrastructure ID and the AWS availability zone.

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet.type`
:   Specifies the subnet type. The following values are valid: `ARN`, `Filters` and `ID`. The default value is `Filters`.

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.placement.availabilityZone: <aws_zone_b>`
:   Specifies an AWS availability zone for an additional failure domain.

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.aws.subnet.filters.values: <cluster_id>-subnet-private-<aws_zone_b>`
:   Specifies the subnet name for the additional failure domain, using the infrastructure ID and the AWS availability zone.

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`
:   Specifies the cloud provider platform name. Do not change this value.

#### [10.5.2. Configuring Amazon Web Services features for control plane machines](#cpmso-supported-features-aws) Copy linkLink copied to clipboard!

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

##### [10.5.2.1. Restricting the API server to private for an Amazon Web Services cluster](#private-clusters-setting-api-private-aws_cpmso-supported-features-aws) Copy linkLink copied to clipboard!

If the security posture of your organization does not allow clusters to use an open API endpoint, you can restrict the API server to use only internal load balancers. To implement this API server restriction, use the Amazon Web Services (AWS) console and OpenShift CLI (`oc`) to delete the external load balancer components.

**Prerequisites**

* You have installed an OpenShift Container Platform cluster on AWS.
* You have access to the AWS console as a user with administrator privileges.
* You have access to the OpenShift CLI (`oc`) as a user with administrator privileges.

**Procedure**

1. Log in to the AWS console as a user with administrator privileges.
2. Delete the external load balancer.

   Note

   The API DNS entry in the private zone already points to the internal load balancer, which uses an identical configuration, so you do not need to modify the internal load balancer.
3. Delete the `api.<cluster_name>.<domain_name>` DNS entry in the public zone.

   where `<cluster_name>` is the name of the cluster and `<domain_name>` is the base domain for the cluster.
4. To remove the external load balancers, log in to the OpenShift CLI (`oc`) as a user with administrator privileges.
5. Edit the `ControlPlaneMachineSet` CR by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster \
     -n openshift-machine-api
   ```
6. Remove the external load balancers by deleting the corresponding lines in the control plane machine set custom resource (CR).

   In the `spec.template.spec.providerSpec.value.loadBalancers` section of the CR, the `name` value for the external load balancer ends in `-ext`. Delete the line with the external load balancer `name` value and the line with the external load balancer `type` value that accompanies it.

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   metadata:
     name: cluster
     namespace: openshift-machine-api
   spec:
   # ...
     template:
   # ...
         spec:
           providerSpec:
             value:
               loadBalancers:
               - name: <cluster_id>-ext
                 type: network
               - name: <cluster_id>-int
                 type: network
   # ...
   ```
7. Save your changes and exit the object specification.

   When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

##### [10.5.2.2. Changing the Amazon Web Services instance type by using a control plane machine set](#cpms-changing-aws-instance-type_cpmso-supported-features-aws) Copy linkLink copied to clipboard!

If you need more resources for your control plane machines, you can change the Amazon Web Services (AWS) instance type that they use. To change the instance type, you update the instance type value in the control plane machine set custom resource (CR).

**Prerequisites**

* You have access to the OpenShift CLI (`oc`) as a user with administrator privileges.
* Your AWS cluster uses a control plane machine set.

**Procedure**

1. Edit your control plane machine set CR by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
   ```
2. Update the CR to implement your configuration changes:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       machines_v1beta1_machine_openshift_io:
         spec:
           providerSpec:
             value:
               instanceType: <compatible_aws_instance_type>
   ```

   where `<compatible_aws_instance_type>` specifies a larger AWS instance type with the same base. For example, you can change this value from `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`.
3. Save your changes and exit the object specification.

   When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

   * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.
   * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

##### [10.5.2.3. Assigning machines to placement groups for Elastic Fabric Adapter instances by using machine sets](#machineset-aws-existing-placement-group_cpmso-supported-features-aws) Copy linkLink copied to clipboard!

You can configure a machine set to deploy machines on Elastic Fabric Adapter (EFA) instances within an existing Amazon Web Services (AWS) placement group.

[EFA](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html) instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA. This example uses both to demonstrate a configuration that can improve network performance for machines within the specified placement group.

**Prerequisites**

* You have access to the OpenShift CLI (`oc`) as a user with administrator privileges.
* You created a placement group in the AWS console.

  Note

  Ensure that the [rules and limitations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/placement-groups.html#limitations-placement-groups) for the type of placement group that you create are compatible with your intended use case. The control plane machine set spreads the control plane machines across multiple failure domains when possible. To use placement groups for the control plane, you must use a placement group type that can span multiple Availability Zones.

**Procedure**

1. Edit your control plane machine set custom resource (CR) by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
   ```
2. Update the CR to implement your configuration changes:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       machines_v1beta1_machine_openshift_io:
         spec:
           providerSpec:
             value:
               instanceType: <supported_instance_type>
               networkInterfaceType: <interface_type>
               placement:
                 availabilityZone: <zone>
                 region: <region>
               placementGroupName: <placement_group>
               placementGroupPartition: <placement_group_partition_number>
   ```

   where:

   `<supported_instance_type>`
   :   Specifies an instance type that [supports EFAs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html#efa-instance-types).

   `<interface_type>`
   :   Specifies the network interface type. To use an EFA, set this value to `EFA`.

   `<zone>`
   :   Specifies the zone; for example, `us-east-1a`.

   `<region>`
   :   Specifies the region; for example, `us-east-1`.

   `<placement_group>`
   :   Specifies the name of the existing AWS placement group to deploy machines in.

   `<placement_group_partition_number>`
   :   Specifies the partition number of the existing AWS placement group to deploy machines in. This parameter is optional.
3. Save your changes and exit the object specification.

   When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

   * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.
   * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

**Verification**

* In the AWS console, find a machine that the machine set created and verify the following in the machine properties:

  + The placement group field has the value that you specified for the `placementGroupName` parameter in the machine set.
  + If you specified a partition number, the partition number field has the value that you specified for the `placementGroupPartition` parameter in the machine set.
  + The interface type field indicates that it uses an EFA.

##### [10.5.2.4. Configuring the AWS EC2 Instance Metadata Service by using machine sets](#machineset-creating-imds-options_cpmso-supported-features-aws) Copy linkLink copied to clipboard!

You can use machine sets to create machines that use the version of the Amazon EC2 Instance Metadata Service (IMDS) that meets the security requirements of your organization.

Machine sets can create machines that allow the use of both IMDSv1 and [IMDSv2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) or machines that require the use of IMDSv2.

You can specify whether to require the use of IMDSv2 by adding or editing the value of `metadataServiceOptions.authentication` in the machine set.

Important

Before configuring a machine set to create machines that require IMDSv2, ensure that any workloads that interact with the AWS metadata service support IMDSv2.

**Prerequisites**

* To use IMDSv2, your AWS cluster must have been created with OpenShift Container Platform version 4.7 or later.

**Procedure**

1. Edit your control plane machine set custom resource (CR) by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
   ```
2. Update the CR to implement your configuration changes:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       machines_v1beta1_machine_openshift_io:
         spec:
           providerSpec:
             value:
               imetadataServiceOptions:
                 authentication: Required
   ```

   To require IMDSv2, set the `metadataServiceOptions.authentication` parameter value to `Required`. To allow the use of both IMDSv1 and IMDSv2, set the parameter value to `Optional`. If you do not specify a value, machines that the machine set creates allow the use of both IMDSv1 and IMDSv2.
3. Save your changes and exit the object specification.

   When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

   * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.
   * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

##### [10.5.2.5. Configuring storage throughput for gp3 drives](#machineset-creating-gp3-throughput_cpmso-supported-features-aws) Copy linkLink copied to clipboard!

You can improve performance for high traffic services by increasing the throughput of gp3 storage volumes in an AWS cluster. You can configure the storage throughput by editing your compute or control plane machine set.

**Prerequisites**

* You use gp3 storage volume(s).

**Procedure**

* Add or edit the following lines under the `providerSpec` field in your compute or control plane machine set:

  ```
  providerSpec:
    value:
      blockDevices:
        - ebs:
            throughputMib: <throughput_value>
  ```

  where:

  `<throughput_value>`
  :   Specifies a value in MiB per second between 125 and 2,000. You can only edit this value on gp3 volumes. The default value is `125`.

##### [10.5.2.6. Creating Dedicated Instances by using machine sets](#machineset-creating-dedicated-instance_cpmso-supported-features-aws) Copy linkLink copied to clipboard!

You can configure a machine set to deploy machines as Dedicated Instances that run in a virtual private cloud (VPC) on hardware that only a single customer can use. To change use Dedicated Instances, you update the placement tenancy value in the machine set custom resource (CR).

Amazon Web Services (AWS) Dedicated Instances are EC2 instances that are physically isolated at the host hardware level. This isolation applies to instances that a single payer account owns even if the instances belong to different AWS accounts.

Public tenancy is the default tenancy. Instances with public tenancy run on shared hardware and can share hardware with Dedicated Instances that belong to the same AWS account.

**Prerequisites**

* You have access to the OpenShift CLI (`oc`) as a user with administrator privileges.

**Procedure**

1. Edit your control plane machine set custom resource (CR) by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
   ```
2. Update the CR to implement your configuration changes:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       machines_v1beta1_machine_openshift_io:
         spec:
           providerSpec:
             value:
               placement:
                 tenancy: dedicated
   ```

   To use Dedicated Instances, set the `placement.tenancy` parameter value to `dedicated`.
3. Save your changes and exit the object specification.

   When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

   * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.
   * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

##### [10.5.2.7. Configuring Capacity Reservations by using machine sets](#machineset-capacity-reservation_cpmso-supported-features-aws) Copy linkLink copied to clipboard!

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define by using Capacity Reservations on Amazon Web Services clusters, including On-Demand Capacity Reservations and Capacity Blocks for ML.

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define.

These parameters specify the instance type, region, and number of instances that you want to reserve. If your Capacity Reservation can accommodate the capacity request, the deployment succeeds.

For more information, including limitations and suggested use cases for this Amazon Web Services offering, see [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) in the AWS documentation.

**Prerequisites**

* You have access to the cluster with `cluster-admin` privileges.
* You installed the OpenShift CLI (`oc`).
* You have purchased an On-Demand Capacity Reservation or Capacity Block for ML. For more information, see [On-Demand Capacity Reservations and Capacity Blocks for ML](https://docs.aws.amazon.com/en_us/AWSEC2/latest/UserGuide/capacity-reservation-overview.html) in the AWS documentation.

**Procedure**

1. Edit your control plane machine set custom resource (CR) by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
   ```
2. Update the CR to implement your configuration changes:

   **Sample configuration**

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       machines_v1beta1_machine_openshift_io:
         spec:
           providerSpec:
             value:
               capacityReservationId: <capacity_reservation>
               marketType: <market_type>
   # ...
   ```

   where:

   `<capacity_reservation>`
   :   Specifies the ID of the Capacity Block for ML or On-Demand Capacity Reservation that you want the machine set to deploy machines on.

   `<market_type>`
   :   Specifies the market type to use. The following values are valid:

       `CapacityBlock`
       :   Use this market type with Capacity Blocks for ML.

       `OnDemand`
       :   Use this market type with On-Demand Capacity Reservations.
3. Save your changes and exit the object specification.

   When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

   * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.
   * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

**Verification**

* To verify machine deployment, list the machines that the machine set created by running the following command:

  ```
  $ oc get machine \
    -n openshift-machine-api \
    -l machine.openshift.io/cluster-api-machine-role=master
  ```

  In the output, verify that the characteristics of the listed machines match the parameters of your Capacity Reservation.

#### [10.5.3. Control plane configuration options for Microsoft Azure](#cpmso-config-options-azure) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

The following example YAML snippets show provider specification and failure domain configurations for an Azure cluster.

##### [10.5.3.1. Sample Azure provider specification](#cpmso-yaml-provider-spec-azure_cpmso-config-options-azure) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification.

The following example YAML illustrates a valid configuration for a Microsoft Azure cluster.

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates.

You can omit any field that has a value set in the failure domain section of the CR.

In the following example, the `<cluster_id>` string is the infrastructure ID. The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

```
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```

**Sample Azure `providerSpec` values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            acceleratedNetworking: true
            apiVersion: machine.openshift.io/v1beta1
            credentialsSecret:
              name: azure-cloud-credential
              namespace: openshift-machine-api
            diagnostics: {}
            image:
              offer: ""
              publisher: ""
              resourceID: /resourceGroups/<cluster_id>-rg/providers/Microsoft.Compute/galleries/gallery_<cluster_id>/images/<cluster_id>-gen2/versions/412.86.20220930
              sku: ""
              version: ""
            internalLoadBalancer: <cluster_id>-internal
            kind: AzureMachineProviderSpec
            location: <region>
            managedIdentity: <cluster_id>-identity
            metadata:
              creationTimestamp: null
              name: <cluster_id>
            networkResourceGroup: <cluster_id>-rg
            osDisk:
              diskSettings: {}
              diskSizeGB: 1024
              managedDisk:
                storageAccountType: Premium_LRS
              osType: Linux
            publicIP: false
            publicLoadBalancer: <cluster_id>
            resourceGroup: <cluster_id>-rg
            subnet: <cluster_id>-master-subnet
            userDataSecret:
              name: master-user-data
            vmSize: Standard_D8s_v3
            vnet: <cluster_id>-vnet
            zone: "1"
```

where:

`spec.template.spec.providerSpec.value.credentialsSecret.name`
:   Specifies the secret name for the cluster. Do not change this value.

`spec.template.spec.providerSpec.value.image`
:   Specifies the image details for your control plane machine set.

`spec.template.spec.providerSpec.value.image.resourceID`
:   Specifies an image that is compatible with your instance type. The Hyper-V generation V2 images created by the installation program have a `-gen2` suffix, while V1 images have the same name without the suffix.

`spec.template.spec.providerSpec.value.internalLoadBalancer`
:   Specifies the internal load balancer for the control plane. The `ControlPlaneMachineSet` and control plane `Machine` CRs require this field. If the field is empty, specify a valid value.

`spec.template.spec.providerSpec.value.kind`
:   Specifies the cloud provider platform type. Do not change this value.

`spec.template.spec.providerSpec.value.location`
:   Specifies the region to place control plane machines on.

`spec.template.spec.providerSpec.value.osDisk`
:   Specifies the disk configuration for the control plane.

`spec.template.spec.providerSpec.value.publicLoadBalancer`
:   Specifies the public load balancer for the control plane.

    Note

    You can omit the `publicLoadBalancer` parameter on private OpenShift Container Platform clusters that have user-defined outbound routing.

`spec.template.spec.providerSpec.value.subnet`
:   Specifies the subnet for the control plane.

`spec.template.spec.providerSpec.value.userDataSecret`
:   Specifies the control plane user data secret. Do not change this value.

`spec.template.spec.providerSpec.value.zone`
:   Specifies the zone configuration for clusters that use a single zone for all failure domains.

    Note

    If the cluster uses a different zone for each failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using different zones for each failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain.

##### [10.5.3.2. Sample Azure failure domain configuration](#cpmso-yaml-failure-domain-azure_cpmso-config-options-azure) Copy linkLink copied to clipboard!

To prevent downtime for your applications due to the failure of a single Microsoft Azure region, you can configure failure domains in the control plane machine set by configuring appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` object.

The control plane machine set concept of a failure domain is analogous to the Azure concept of an [*Azure availability zone*](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/concept-availability-zones). The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible.

When configuring Azure failure domains in the control plane machine set, you must specify the availability zone name. An Azure cluster can use the following configurations:

* One subnet for each availability zone.
* One subnet that spans more than one availability zone.
* More than one subnet in more than one availability zone.

**Sample Azure failure domain values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        azure:
        - zone: "1"
          subnet: <subnet_zone_1>
        - zone: "2"
          subnet: <subnet_zone_2>
        - zone: "3"
          subnet: <subnet_zone_3>
        platform: Azure
# ...
```

where:

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.azure.zone`
:   Each instance of `zone` specifies an Azure availability zone for a failure domain.

    Note

    If the cluster uses a single zone for all failure domains, the `zone` parameter is in the provider specification instead of in the failure domain configuration.

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.azure.subnet`
:   Optional: Specifies the network subnet in which to create the control plane VM. When omitted, the control plane machine set uses the `subnet` value from the machine `providerSpec` template.

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`
:   Specifies the cloud provider platform name. Do not change this value.

#### [10.5.4. Configuring Microsoft Azure features for control plane machines](#cpmso-supported-features-azure) Copy linkLink copied to clipboard!

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

##### [10.5.4.1. Restricting the API server to private for an Microsoft Azure cluster](#private-clusters-setting-api-private-azure_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

If the security posture of your organization does not allow clusters to use an open API endpoint, you can restrict the API server to use only internal load balancers. To implement this API server restriction, use the Microsoft Azure console to delete the external load balancer component.

**Prerequisites**

* You have installed an OpenShift Container Platform cluster on Azure.
* You have access to the Azure console as a user with administrator privileges.

**Procedure**

1. Log in to the Azure console as a user with administrator privileges.
2. Delete the following resources:

   * The `api-v4` rule for the public load balancer.
   * The `frontendIPConfiguration` parameter that is associated with the `api-v4` rule for the public load balancer.
   * The public IP address that is specified in the `frontendIPConfiguration` parameter.
3. Configure the Ingress Controller endpoint publishing scope to `Internal`. For more information, see "Configuring the Ingress Controller endpoint publishing scope to Internal".
4. Delete the `api.<cluster_name>` DNS entry in the public zone.

   where `<cluster_name>` is the name of the cluster.

##### [10.5.4.2. Using the Azure Marketplace offering](#installation-azure-marketplace-subscribe_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

You can create a machine set running on Azure that deploys machines that use the Azure Marketplace offering. To use this offering, you must first obtain the Azure Marketplace image. When obtaining your image, consider the following:

* While the images are the same, the Azure Marketplace publisher is different depending on your region. If you are located in North America, specify `redhat` as the publisher. If you are located in EMEA, specify `redhat-limited` as the publisher.
* The offer includes a `rh-ocp-worker` SKU and a `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker` SKU represents a Hyper-V generation version 2 VM image. The default instance types used in OpenShift Container Platform are version 2 compatible. If you plan to use an instance type that is only version 1 compatible, use the image associated with the `rh-ocp-worker-gen1` SKU. The `rh-ocp-worker-gen1` SKU represents a Hyper-V version 1 VM image.

Important

Installing images with the Azure marketplace is not supported on clusters with 64-bit ARM instances.

You should only modify the RHCOS image for compute machines to use an Azure Marketplace image. Control plane machines and infrastructure nodes do not require an OpenShift Container Platform subscription and use the public RHCOS default image by default, which does not incur subscription costs on your Azure bill. Therefore, you should not modify the cluster default boot image or the control plane boot images. Applying the Azure Marketplace image to them will incur additional licensing costs that cannot be recovered.

**Prerequisites**

* You have installed the Azure CLI client `(az)`.
* Your Azure account is entitled for the offer and you have logged into this account with the Azure CLI client.

**Procedure**

1. Display all of the available OpenShift Container Platform images by running one of the following commands:

   * North America:

     ```
     $  az vm image list --all --offer rh-ocp-worker --publisher redhat -o table
     ```

     **Example output**

     ```
     Offer          Publisher       Sku                 Urn                                                             Version
     -------------  --------------  ------------------  --------------------------------------------------------------  -----------------
     rh-ocp-worker  RedHat          rh-ocp-worker       RedHat:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
     rh-ocp-worker  RedHat          rh-ocp-worker-gen1  RedHat:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
     ```
   * EMEA:

     ```
     $  az vm image list --all --offer rh-ocp-worker --publisher redhat-limited -o table
     ```

     **Example output**

     ```
     Offer          Publisher       Sku                 Urn                                                                     Version
     -------------  --------------  ------------------  --------------------------------------------------------------          -----------------
     rh-ocp-worker  redhat-limited  rh-ocp-worker       redhat-limited:rh-ocp-worker:rh-ocp-worker:4.17.2024100419              4.17.2024100419
     rh-ocp-worker  redhat-limited  rh-ocp-worker-gen1  redhat-limited:rh-ocp-worker:rh-ocp-worker-gen1:4.17.2024100419         4.17.2024100419
     ```

   Note

   Use the latest image that is available for compute and control plane nodes. If required, your VMs are automatically upgraded as part of the installation process.
2. Inspect the image for your offer by running one of the following commands:

   * North America:

     ```
     $ az vm image show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
     ```
   * EMEA:

     ```
     $ az vm image show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
     ```
3. Review the terms of the offer by running one of the following commands:

   * North America:

     ```
     $ az vm image terms show --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
     ```
   * EMEA:

     ```
     $ az vm image terms show --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
     ```
4. Accept the terms of the offering by running one of the following commands:

   * North America:

     ```
     $ az vm image terms accept --urn redhat:rh-ocp-worker:rh-ocp-worker:<version>
     ```
   * EMEA:

     ```
     $ az vm image terms accept --urn redhat-limited:rh-ocp-worker:rh-ocp-worker:<version>
     ```
5. Record the image details of your offer, specifically the values for `publisher`, `offer`, `sku`, and `version`.
6. Add the following parameters to the `providerSpec` section of your machine set YAML file using the image details for your offer:

   **Sample `providerSpec` image values for Azure Marketplace machines**

   ```
   providerSpec:
     value:
       image:
         offer: rh-ocp-worker
         publisher: redhat
         resourceID: ""
         sku: rh-ocp-worker
         type: MarketplaceWithPlan
         version: 413.92.2023101700
   ```

##### [10.5.4.3. Enabling Microsoft Azure boot diagnostics](#machineset-azure-boot-diagnostics_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

You can enable boot diagnostics on Microsoft Azure machines that your machine set creates. Use this to store console logs that you can use to troubleshoot why a node fails to boot.

**Prerequisites**

* Have an existing Azure cluster.

**Procedure**

* Add the `diagnostics` configuration that is applicable to your storage type to the `providerSpec` field in your machine set YAML file:

  + For an Azure Managed storage account:

    ```
    providerSpec:
      value:
        diagnostics:
          boot:
            storageAccountType: <azure_managed>
    ```

    where:

    `<azure_managed>`
    :   Specifies an Azure Managed storage account.
  + For an Azure Unmanaged storage account:

    ```
    providerSpec:
      value:
        diagnostics:
          boot:
            storageAccountType: <customer_managed>
            customerManaged:
              storageAccountURI: <https://<storage_account>.blob.core.windows.net>
    ```

    where:

    `<customer_managed>`
    :   Specifies an Azure Unmanaged storage account.

    `https://<storage_account>.blob.core.windows.net`
    :   Specifies the storage account URL. Replace `<storage_account>` with the name of your storage account.

    Note

    Only the Azure Blob Storage data service is supported.

**Verification**

* On the Azure portal, review the **Boot diagnostics** page for a machine deployed by the machine set, and verify that you can see the serial logs for the machine.

##### [10.5.4.4. Machine sets that deploy machines with ultra disks as data disks](#machineset-azure-ultra-disk_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

You can create a machine set running on Microsoft Azure that deploys machines with ultra disks. Ultra disks are high-performance storage that are intended for use with the most demanding data workloads.

##### [10.5.4.4.1. Creating machines with ultra disks by using machine sets](#machineset-creating-azure-ultra-disk_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

You can deploy machines with ultra disks on Microsoft Azure by editing your machine set YAML file.

**Prerequisites**

* Have an existing Microsoft Azure cluster.

**Procedure**

1. Create a custom secret in the `openshift-machine-api` namespace by using the `master` data secret by running the following command:

   ```
   $ oc -n openshift-machine-api \
   get secret <role>-user-data \
   --template='{{index .data.userData | base64decode}}' | jq > userData.txt
   ```

   where:

   `<role>`
   :   Replace with `master`.

   `userData.txt`
   :   Specifies `userData.txt` as the name of the new custom secret.
2. In a text editor, open the `userData.txt` file and locate the final `}` character in the file.

   1. On the immediately preceding line, add a `,`.
   2. Create a new line after the `,` and add the following configuration details:

      ```
      "storage": {
        "disks": [
          {
            "device": "/dev/disk/azure/scsi1/lun0",
            "partitions": [
              {
                "label": "lun0p1",
                "sizeMiB": 1024,
                "startMiB": 0
              }
            ]
          }
        ],
        "filesystems": [
          {
            "device": "/dev/disk/by-partlabel/lun0p1",
            "format": "xfs",
            "path": "/var/lib/lun0p1"
          }
        ]
      },
      "systemd": {
        "units": [
          {
            "contents": "[Unit]\nBefore=local-fs.target\n[Mount]\nWhere=/var/lib/lun0p1\nWhat=/dev/disk/by-partlabel/lun0p1\nOptions=defaults,pquota\n[Install]\nWantedBy=local-fs.target\n",
            "enabled": true,
            "name": "var-lib-lun0p1.mount"
          }
        ]
      }
      ```

      where:

      `"disks"`
      :   Specifies the configuration details for the disk that you want to attach to a node as an ultra disk.

      `"device"`
      :   Specifies the `lun` value that is defined in the `dataDisks` stanza of the machine set you are using. For example, if the machine set contains `lun: 0`, specify `lun0`. You can initialize multiple data disks by specifying multiple `"disks"` entries in this configuration file. If you specify multiple `"disks"` entries, ensure that the `lun` value for each matches the value in the machine set.

      `"partitions"`
      :   Specifies the configuration details for a new partition on the disk.

      `"label"`
      :   Specifies a label for the partition. You might find it helpful to use hierarchical names, such as `lun0p1` for the first partition of `lun0`.

      `"sizeMiB"`
      :   Specifies the total size in MiB of the partition.

      `"filesystems"`
      :   Specifies the filesystem to use when formatting a partition. Use the partition label to specify the partition.

      `"units"`
      :   Specifies a `systemd` unit to mount the partition at boot. Use the partition label to specify the partition. You can create multiple partitions by specifying multiple `"partitions"` entries in this configuration file. If you specify multiple `"partitions"` entries, you must specify a `systemd` unit for each.

      `"contents"`
      :   Specifies the value of `storage.filesystems.path` for `Where`. Specifies the value of `storage.filesystems.device` for `What`.
3. Extract the disabling template value to a file called `disableTemplating.txt` by running the following command:

   ```
   $ oc -n openshift-machine-api get secret <role>-user-data \
   --template='{{index .data.disableTemplating | base64decode}}' | jq > disableTemplating.txt
   ```

   Replace `<role>` with `master`.
4. Combine the `userData.txt` file and `disableTemplating.txt` file to create a data secret file by running the following command:

   ```
   $ oc -n openshift-machine-api create secret generic <role>-user-data-x5 \
   --from-file=userData=userData.txt \
   --from-file=disableTemplating=disableTemplating.txt
   ```

   For `<role>-user-data-x5`, specify the name of the secret. Replace `<role>` with `master`.
5. Edit your control plane machine set CR by running the following command:

   ```
   $ oc --namespace openshift-machine-api edit controlplanemachineset.machine.openshift.io cluster
   ```
6. Add the following lines in the positions indicated:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: ControlPlaneMachineSet
   spec:
     template:
       spec:
         metadata:
           labels:
             disk: ultrassd
         providerSpec:
           value:
             ultraSSDCapability: Enabled
             dataDisks:
             - nameSuffix: ultrassd
               lun: 0
               diskSizeGB: 4
               deletionPolicy: Delete
               cachingType: None
               managedDisk:
                 storageAccountType: UltraSSD_LRS
             userDataSecret:
               name: <role>-user-data-x5
   ```

   where:

   `spec.template.spec.metadata.labels.disk`
   :   Specifies a label to use to select a node that is created by this machine set. The example uses `disk.ultrassd` for this value.

   `spec.template.spec.providerSpec.value.ultraSSDCapability`
   :   Enables the use of ultra disks. For `dataDisks`, include the entire stanza.

   `spec.template.spec.providerSpec.value.userDataSecret.name`
   :   Specifies the user data secret created earlier. Replace `<role>` with `master`.
7. Save your changes.

   * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.
   * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

**Verification**

1. Validate that the machines are created by running the following command:

   ```
   $ oc get machines
   ```

   The machines should be in the `Running` state.
2. For a machine that is running and has a node attached, validate the partition by running the following command:

   ```
   $ oc debug node/<node_name> -- chroot /host lsblk
   ```

   In this command, `oc debug node/<node_name>` starts a debugging shell on the node `<node_name>` and passes a command with `--`. The passed command `chroot /host` provides access to the underlying host OS binaries, and `lsblk` shows the block devices that are attached to the host OS machine.

**Next steps**

* To use an ultra disk on the control plane, reconfigure your workload to use the control plane’s ultra disk mount point.

##### [10.5.4.4.2. Troubleshooting resources for machine sets that enable ultra disks](#machineset-troubleshooting-azure-ultra-disk_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

You can recover from issues that you might encounter when you enable ultra disks for machine sets. Review fields, such as disk settings, and ensure that the parameters are correctly configured.

###### [10.5.4.4.2.1. Incorrect ultra disk configuration](#ts-mapi-attach-misconfigure_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

If an incorrect configuration of the `ultraSSDCapability` parameter is specified in the machine set, the machine provisioning fails.

For example, if the `ultraSSDCapability` parameter is set to `Disabled`, but an ultra disk is specified in the `dataDisks` parameter, the following error message appears:

```
StorageAccountType UltraSSD_LRS can be used only when additionalCapabilities.ultraSSDEnabled is set.
```

* To resolve this issue, verify that your machine set configuration is correct.

###### [10.5.4.4.2.2. Unsupported disk parameters](#ts-mapi-attach-unsupported_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

If a region, availability zone, or instance size that is not compatible with ultra disks is specified in the machine set, the machine provisioning fails. Check the logs for the following error message:

```
failed to create vm <machine_name>: failure sending request for machine <machine_name>: cannot create vm: compute.VirtualMachinesClient#CreateOrUpdate: Failure sending request: StatusCode=400 -- Original Error: Code="BadRequest" Message="Storage Account type 'UltraSSD_LRS' is not supported <more_information_about_why>."
```

* To resolve this issue, verify that you are using this feature in a supported environment and that your machine set configuration is correct.

###### [10.5.4.4.2.3. Unable to delete disks](#ts-mapi-delete_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

If the deletion of ultra disks as data disks is not working as expected, the machines are deleted and the data disks are orphaned. You must delete the orphaned disks manually if desired.

##### [10.5.4.5. Enabling customer-managed encryption keys for a machine set](#machineset-enabling-customer-managed-encryption-azure_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

To enhance data security, enable customer-managed encryption on Microsoft Azure by adding the disk encryption set ID to your machine set.

You can supply an encryption key to Azure to encrypt data on managed disks at rest. You can enable server-side encryption with customer-managed keys by using the Machine API.

An Azure Key Vault, a disk encryption set, and an encryption key are required to use a customer-managed key. The disk encryption set must be in a resource group where the Cloud Credential Operator (CCO) has granted permissions. If not, an additional reader role is required to be granted on the disk encryption set.

**Prerequisites**

* [You created an Azure Key Vault instance (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#create-an-azure-key-vault-instance).
* [You created an instance of a disk encryption set (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#create-an-instance-of-a-diskencryptionset).
* [You granted the disk encryption set access to key vault (Azure documentation)](https://docs.microsoft.com/en-us/azure/aks/azure-disk-customer-managed-keys#grant-the-diskencryptionset-access-to-key-vault).

**Procedure**

* Configure the disk encryption set under the `providerSpec` field in your machine set YAML file. For example:

  ```
  providerSpec:
    value:
      osDisk:
        diskSizeGB: 128
        managedDisk:
          diskEncryptionSet:
            id: /subscriptions/<subscription_id>/resourceGroups/<resource_group_name>/providers/Microsoft.Compute/diskEncryptionSets/<disk_encryption_set_name>
          storageAccountType: Premium_LRS
  ```

##### [10.5.4.6. Configuring trusted launch for Azure virtual machines by using machine sets](#machineset-azure-trusted-launch_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

By editing the machine set YAML file, you can configure the trusted launch for Microsoft Azure virtual machines (VMs) options that a machine set uses for machines that it deploys.

For example, you can configure these machines to use UEFI security features such as Secure Boot or a dedicated virtual Trusted Platform Module (vTPM) instance.

Note

Some feature combinations result in an invalid configuration.

Expand

Table 10.2. UEFI feature combination compatibility

| Secure Boot[1] | vTPM[2] | Valid configuration |
| --- | --- | --- |
| Enabled | Enabled | Yes |
| Enabled | Disabled | Yes |
| Enabled | Omitted | Yes |
| Disabled | Enabled | Yes |
| Omitted | Enabled | Yes |
| Disabled | Disabled | No |
| Omitted | Disabled | No |
| Omitted | Omitted | No |

Show more

1. Using the `secureBoot` field.
2. Using the `virtualizedTrustedPlatformModule` field.

For more information about related features and functionality, see the Microsoft Azure documentation about [Trusted launch for Azure virtual machines](https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch).

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following section under the `providerSpec` field to provide a valid configuration:

   **Sample valid configuration with UEFI Secure Boot and vTPM enabled**

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       machines_v1beta1_machine_openshift_io:
         spec:
           providerSpec:
             value:
               securityProfile:
                 settings:
                   securityType: TrustedLaunch
                   trustedLaunch:
                     uefiSettings:
                       secureBoot: Enabled
                       virtualizedTrustedPlatformModule: Enabled
   # ...
   ```

   where:

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.securityType`
   :   Enables the use of trusted launch for Azure virtual machines. This value is required for all valid configurations.

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings`
   :   Specifies which UEFI security features to use. This section is required for all valid configurations.

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings.secureBoot`
   :   Enables UEFI Secure Boot.

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.securityProfile.settings.trustedLaunch.uefiSettings.virtualizedTrustedPlatformModule`
   :   Enables the use of a vTPM.

**Verification**

* On the Microsoft Azure portal, review the details for a machine deployed by the machine set and verify that the trusted launch options match the values that you configured.

##### [10.5.4.7. Configuring Azure confidential virtual machines by using machine sets](#machineset-azure-confidential-vms_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

You can enable Microsoft Azure confidential virtual machines (VMs) to use memory encryption to improve data confidentiality.

Note

Confidential VMs are currently not supported on 64-bit ARM architectures.

By editing the machine set YAML file, you can configure the confidential VM options that a machine set uses for machines that it deploys. For example, you can configure these machines to use UEFI security features such as Secure Boot or a dedicated virtual Trusted Platform Module (vTPM) instance.

Warning

Not all instance types support confidential VMs. Do not change the instance type for a control plane machine set that is configured to use confidential VMs to a type that is incompatible. Using an incompatible instance type can cause your cluster to become unstable.

For more information about related features and functionality, see the Microsoft Azure documentation about [Confidential virtual machines](https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview).

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following section under the `providerSpec` field:

   **Sample configuration**

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             osDisk:
               # ...
               managedDisk:
                 securityProfile:
                   securityEncryptionType: VMGuestStateOnly
               # ...
             securityProfile:
               settings:
                   securityType: ConfidentialVM
                   confidentialVM:
                     uefiSettings:
                       secureBoot: Disabled
                       virtualizedTrustedPlatformModule: Enabled
             vmSize: Standard_DC16ads_v5
   # ...
   ```

   where:

   `spec.template.spec.providerSpec.value.osDisk.managedDisk.securityProfile`
   :   Specifies security profile settings for the managed disk when using a confidential VM.

   `spec.template.spec.providerSpec.value.osDisk.managedDisk.securityProfile.securityEncryptionType`
   :   Enables encryption of the Microsoft Azure VM Guest State (VMGS) blob. This setting requires the use of vTPM.

   `spec.template.spec.providerSpec.value.securityProfile`
   :   Specifies security profile settings for the confidential VM.

   `spec.template.spec.providerSpec.value.securityProfile.settings.securityType`
   :   Enables the use of confidential VMs. This value is required for all valid configurations.

   `spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings`
   :   Specifies which UEFI security features to use. This section is required for all valid configurations.

   `spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings.secureBoot`
   :   Disables UEFI Secure Boot.

   `spec.template.spec.providerSpec.value.securityProfile.settings.confidentialVM.uefiSettings.virtualizedTrustedPlatformModule`
   :   Enables the use of a vTPM.

   `spec.template.spec.providerSpec.value.vmSize`
   :   Specifies an instance type that supports confidential VMs.

**Verification**

* On the Microsoft Azure portal, review the details for a machine deployed by the machine set and verify that the confidential VM options match the values that you configured.

##### [10.5.4.8. Configuring Capacity Reservations by using machine sets](#machineset-capacity-reservation_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define by using on-demand Capacity Reservation with Capacity Reservation groups on Microsoft Azure clusters.

You can configure a machine set to deploy machines on any available resources that match the parameters of a capacity request that you define.

These parameters specify the VM size, region, and number of instances that you want to reserve. If your Azure subscription quota can accommodate the capacity request, the deployment succeeds.

For more information, including limitations and suggested use cases for this Microsoft Azure offering, see [On-demand Capacity Reservation](https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-overview) in the Azure documentation.

Note

You cannot change an existing Capacity Reservation configuration for a machine set. To use a different Capacity Reservation group, you must replace the machine set and the machines that the previous machine set deployed.

**Prerequisites**

* You have access to the cluster with `cluster-admin` privileges.
* You installed the OpenShift CLI (`oc`).
* You have created a Capacity Reservation group. For more information, see [Create a Capacity Reservation](https://learn.microsoft.com/en-us/azure/virtual-machines/capacity-reservation-create) in the Microsoft Azure documentation.

**Procedure**

1. Edit your control plane machine set custom resource (CR) by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster --namespace openshift-machine-api
   ```
2. Update the CR to implement your configuration changes:

   **Sample configuration**

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       machines_v1beta1_machine_openshift_io:
         spec:
           providerSpec:
             value:
               capacityReservationGroupID: <capacity_reservation_group>
   # ...
   ```

   where:

   `<capacity_reservation_group>`
   :   Specifies the ID of the Capacity Reservation group that you want the machine set to deploy machines on.
3. Save your changes and exit the object specification.

   When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

   * For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.
   * For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

**Verification**

* To verify machine deployment, list the machines that the machine set created by running the following command:

  ```
  $ oc get machine \
    -n openshift-machine-api \
    -l machine.openshift.io/cluster-api-machine-role=master
  ```

  In the output, verify that the characteristics of the listed machines match the parameters of your Capacity Reservation.

##### [10.5.4.9. Accelerated Networking for Microsoft Azure VMs](#machineset-azure-accelerated-networking_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

You can enable Accelerated Networking, which uses single root I/O virtualization (SR-IOV) to provide Microsoft Azure VMs with a more direct path to the switch, after installation. This enhances network performance.

##### [10.5.4.9.1. Limitations](#machineset-azure-accelerated-networking-limits_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

Consider the following limitations when deciding whether to use Accelerated Networking:

* Accelerated Networking is only supported on clusters where the Machine API is operational.
* Accelerated Networking requires an Azure VM size that includes at least four vCPUs. To satisfy this requirement, you can change the value of `vmSize` in your machine set. For information about Azure VM sizes, see [Microsoft Azure documentation](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes).

##### [10.5.4.9.2. Enabling Accelerated Networking on an existing Microsoft Azure cluster](#machineset-azure-enabling-accelerated-networking-existing_cpmso-supported-features-azure) Copy linkLink copied to clipboard!

You can enable Accelerated Networking on Microsoft Azure by adding `acceleratedNetworking` to your machine set YAML file. Accelerated Networking uses SR-IOV to help improve network performance for new nodes.

**Prerequisites**

* Have an existing Azure cluster where the Machine API is operational.

**Procedure**

* Add the following to the `providerSpec` field:

  ```
  providerSpec:
    value:
      acceleratedNetworking: true
      vmSize: <azure-vm-size>
  ```

  where:

  `providerSpec.value.acceleratedNetworking`
  :   Enables Accelerated Networking.

  `providerSpec.value.vmSize`
  :   Specifies an Azure VM size that includes at least four vCPUs. For information about VM sizes, see the Microsoft Azure documentation [Sizes for virtual machines in Azure](https://docs.microsoft.com/en-us/azure/virtual-machines/sizes).

**Verification**

* On the Microsoft Azure portal, review the **Networking** settings page for a machine provisioned by the machine set, and verify that the `Accelerated networking` field is set to `Enabled`.

#### [10.5.5. Control plane configuration options for Google Cloud](#cpmso-config-options-gcp) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

The following example YAML snippets show provider specification and failure domain configurations for a Google Cloud cluster.

##### [10.5.5.1. Sample Google Cloud provider specification](#cpmso-yaml-provider-spec-gcp_cpmso-config-options-gcp) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification.

The following example YAML illustrates a valid configuration for an Google Cloud cluster.

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates.

You can omit any field that has a value set in the failure domain section of the CR.

In the following example, you can obtain some of the values for your cluster by using the OpenShift CLI (`oc`).

Infrastructure ID
:   The `<cluster_id>` string is the infrastructure ID. The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning. If you have `oc` installed, you can obtain the infrastructure ID by running the following command:

    ```
    $ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
    ```

Image path
:   The `<path_to_image>` string is the path to the source image for the disk. If you have `oc` installed, you can obtain the path to the image by running the following command:

    ```
    $ oc -n openshift-machine-api \
      -o jsonpath='{.spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.disks[0].image}{"\n"}' \
      get ControlPlaneMachineSet/cluster
    ```

**Sample Google Cloud `providerSpec` values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
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
              image: <path_to_image>
              labels: null
              sizeGb: 200
              type: pd-ssd
            kind: GCPMachineProviderSpec
            machineType: e2-standard-4
            metadata:
              creationTimestamp: null
            metadataServiceOptions: {}
            networkInterfaces:
            - network: <cluster_id>-network
              subnetwork: <cluster_id>-master-subnet
            projectID: <project_name>
            region: <region>
            serviceAccounts:
            - email: <cluster_id>-m@<project_name>.iam.gserviceaccount.com
              scopes:
              - https://www.googleapis.com/auth/cloud-platform
            shieldedInstanceConfig: {}
            tags:
            - <cluster_id>-master
            targetPools:
            - <cluster_id>-api
            userDataSecret:
              name: master-user-data
            zone: ""
```

where:

`spec.template.spec.providerSpec.value.credentialsSecret.name`
:   Specifies the secret name for the cluster. Do not change this value.

`spec.template.spec.providerSpec.value.disk.image`
:   Specifies the path to the source image for the disk.

    To use a Google Cloud Marketplace image, specify the offer to use:

    * OpenShift Container Platform: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-ocp-413-x86-64-202305021736`
    * OpenShift Platform Plus: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-opp-413-x86-64-202305021736`
    * OpenShift Kubernetes Engine: `https://www.googleapis.com/compute/v1/projects/redhat-marketplace-public/global/images/redhat-coreos-oke-413-x86-64-202305021736`

`spec.template.spec.providerSpec.value.kind`
:   Specifies the cloud provider platform type. Do not change this value.

`spec.template.spec.providerSpec.value.projectID`
:   Specifies the name of the Google Cloud project that you use for your cluster.

`spec.template.spec.providerSpec.value.projectID.region`
:   Specifies the Google Cloud region for the cluster.

`spec.template.spec.providerSpec.value.serviceAccounts`
:   Specifies a single service account. Specifying more than one service account is not supported.

`spec.template.spec.providerSpec.value.userDataSecret`
:   Specifies the control plane user data secret. Do not change this value.

`spec.template.spec.providerSpec.value.zone`
:   This parameter is in the failure domain configuration and has an empty value here.

    If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain.

##### [10.5.5.2. Sample Google Cloud failure domain configuration](#cpmso-yaml-failure-domain-gcp_cpmso-config-options-gcp) Copy linkLink copied to clipboard!

To prevent downtime for your application due to the failure of a single Google Cloud region, you can configure failure domains in the control plane machine set by configuring appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` object.

The control plane machine set concept of a failure domain is analogous to the existing Google Cloud concept of a [*zone*](https://cloud.google.com/compute/docs/regions-zones). The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible.

When configuring Google Cloud failure domains in the control plane machine set, you must specify the zone name to use.

**Sample Google Cloud failure domain values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        gcp:
        - zone: <gcp_zone_a>
        - zone: <gcp_zone_b>
        - zone: <gcp_zone_c>
        - zone: <gcp_zone_d>
        platform: GCP
# ...
```

where:

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.gcp.zone`
:   Each instance of `zone` specifies a Google Cloud zone for a failure domain.

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`
:   Specifies the cloud provider platform name. Do not change this value.

#### [10.5.6. Configuring Google Cloud features for control plane machines](#cpmso-supported-features-gcp) Copy linkLink copied to clipboard!

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

##### [10.5.6.1. Configuring persistent disk types by using machine sets](#machineset-gcp-pd-disk-types_cpmso-supported-features-gcp) Copy linkLink copied to clipboard!

Configure the persistent disk type for your machine set on Google Cloud to match your workload requirements. Editing the `MachineSet` YAML file allows you to choose between standard, balanced, or SSD persistent disks.

For more information about persistent disk types, compatibility, regional availability, and limitations, see the Google Cloud Compute Engine documentation about [persistent disks](https://cloud.google.com/compute/docs/disks#pdspecs).

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following line under the `providerSpec` field:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             disks:
               type: pd-ssd
   ```

   where:

   `spec.template.spec.providerSpec.value.disks.type`
   :   Uses the `pd-ssd` disk type for control plane nodes. Using the `pd-ssd` disk type is required for control plane nodes.

**Verification**

* Using the Google Cloud console, review the details for a machine deployed by the machine set and verify that the `Type` field matches the configured disk type.

##### [10.5.6.2. Configuring Confidential VM by using machine sets](#machineset-gcp-confidential-vm_cpmso-supported-features-gcp) Copy linkLink copied to clipboard!

You create machine sets to scale clusters on Google Cloud. By editing the machine set YAML file, you can configure the Confidential VM options that a machine set uses for machines that it deploys.

For more information about Confidential VM features, functions, and compatibility, see the Google Cloud Compute Engine documentation about [Confidential VM](https://cloud.google.com/confidential-computing/confidential-vm/docs/about-cvm#confidential-vm).

Note

Confidential VMs are currently not supported on 64-bit ARM architectures. If you use Confidential VM, you must ensure that you select a supported region. For details on supported regions and configurations, see the Google Cloud Compute Engine documentation about [supported zones](https://cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#supported-zones).

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following section under the `providerSpec` field:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
       machines_v1beta1_machine_openshift_io:
         spec:
           providerSpec:
             value:
               confidentialCompute: Enabled
               onHostMaintenance: Terminate
               machineType: n2d-standard-8
   # ...
   ```

   where:

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.confidentialCompute`
   :   Specifies whether Confidential VM is enabled. The following values are valid:

   `Enabled`
   :   Enables Confidential VM with a default selection of Confidential VM technology. The default selection is AMD Secure Encrypted Virtualization (AMD SEV).

       Important

       The `Enabled` value selects Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV), which is deprecated.

   `Disabled`
   :   Disables Confidential VM.

   `AMDEncryptedVirtualizationNestedPaging`
   :   Enables Confidential VM using AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). AMD SEV-SNP supports n2d machines.

   `AMDEncryptedVirtualization`
   :   Enables Confidential VM using AMD SEV. AMD SEV supports c2d, n2d, and c3d machines.

       Important

       The use of Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV) has been deprecated and will be removed in a future release.

   `IntelTrustedDomainExtensions`
   :   Enables Confidential VM using Intel Trusted Domain Extensions (Intel TDX). Intel TDX supports n2d machines.

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.onHostMaintenance`
   :   Specifies the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VM does not support live VM migration.

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.machineType`
   :   Specifies a machine type that supports the Confidential VM option that you specified in the `confidentialCompute` field.

**Verification**

* On the Google Cloud console, review the details for a machine deployed by the machine set and verify that the Confidential VM options match the values that you configured.

##### [10.5.6.3. Configuring Shielded VM options by using machine sets](#machineset-gcp-shielded-vms_cpmso-supported-features-gcp) Copy linkLink copied to clipboard!

To help secure your cluster instances, you can configure Shielded Virtual Machine (VM) options for your machine sets on Google Cloud by editing the `MachineSet` YAML file.

For more information about Shielded VM features and functionality, see the Google Cloud Compute Engine documentation about [Shielded VM](https://cloud.google.com/compute/shielded-vm/docs/shielded-vm).

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following section under the `providerSpec` field:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             shieldedInstanceConfig:
               integrityMonitoring: Enabled
               secureBoot: Disabled
               virtualizedTrustedPlatformModule: Enabled
   # ...
   ```

   where:

   `spec.template.spec.providerSpec.value.shieldedInstanceConfig`
   :   Specifies the Shielded VM configuration.

   `spec.template.spec.providerSpec.value.shieldedInstanceConfig.integrityMonitoring`
   :   Specifies whether integrity monitoring is enabled. Valid values are `Disabled` or `Enabled`.

       Note

       When integrity monitoring is enabled, you must not disable virtual trusted platform module (vTPM).

   `spec.template.spec.providerSpec.value.shieldedInstanceConfig.secureBoot`
   :   Specifies whether UEFI Secure Boot is enabled. Valid values are `Disabled` or `Enabled`.

   `spec.template.spec.providerSpec.value.shieldedInstanceConfig.virtualizedTrustedPlatformModule`
   :   Specifies whether vTPM is enabled. Valid values are `Disabled` or `Enabled`.

**Verification**

* Using the Google Cloud console, review the details for a machine deployed by the machine set and verify that the Shielded VM options match the values that you configured.

##### [10.5.6.4. Enabling customer-managed encryption keys for a machine set](#machineset-gcp-enabling-customer-managed-encryption_cpmso-supported-features-gcp) Copy linkLink copied to clipboard!

Use Google Cloud Compute Engine to supply an encryption key to encrypt data on disks at rest. The key is used to encrypt the data encryption key, not to encrypt the customer’s data. By default, Compute Engine encrypts this data by using Compute Engine keys.

You can enable encryption with a customer-managed key in clusters that use the Machine API. You must first [create a KMS key](https://cloud.google.com/compute/docs/disks/customer-managed-encryption#before_you_begin) and assign the correct permissions to a service account. The KMS key name, key ring name, and location are required to allow a service account to use your key.

Note

If you do not want to use a dedicated service account for the KMS encryption, the Compute Engine default service account is used instead. You must grant the default service account permission to access the keys if you do not use a dedicated service account. The Compute Engine default service account name follows the `service-<project_number>@compute-system.iam.gserviceaccount.com` pattern.

**Procedure**

1. To allow a specific service account to use your KMS key and to grant the service account the correct IAM role, run the following command with your KMS key name, key ring name, and location:

   ```
   $ gcloud kms keys add-iam-policy-binding <key_name> \
     --keyring <key_ring_name> \
     --location <key_ring_location> \
     --member "serviceAccount:service-<project_number>@compute-system.iam.gserviceaccount.com” \
     --role roles/cloudkms.cryptoKeyEncrypterDecrypter
   ```
2. Configure the encryption key under the `providerSpec` field in your machine set YAML file. For example:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             disks:
             - type:
               encryptionKey:
                 kmsKey:
                   name: machine-encryption-key
                   keyRing: openshift-encryption-ring
                   location: global
                   projectID: openshift-gcp-project
                 kmsKeyServiceAccount: openshift-service-account@openshift-gcp-project.iam.gserviceaccount.com
   ```

   where:

   `spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.name`
   :   Specifies the name of the customer-managed encryption key that is used for the disk encryption.

   `spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.keyRing`
   :   Specifies the name of the KMS key ring that the KMS key belongs to.

   `spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.location`
   :   Specifies the Google Cloud location in which the KMS key ring exists.

   `spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKey.projectID`
   :   Optional: Specifies the ID of the project in which the KMS key ring exists. If a project ID is not set, the machine set `projectID` in which the machine set was created is used.

   `spec.template.spec.providerSpec.value.disks.type.encryptionKey.kmsKeyServiceAccount`
   :   Optional: Specifies the service account that is used for the encryption request for the given KMS key. If a service account is not set, the Compute Engine default service account is used.

       When a new machine is created by using the updated `providerSpec` object configuration, the disk encryption key is encrypted with the KMS key.

#### [10.5.7. Control plane configuration options for Nutanix](#cpmso-config-options-nutanix) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

The following example YAML snippets show provider specification and failure domain configurations for a Nutanix cluster.

##### [10.5.7.1. Sample Nutanix provider specification](#cpmso-yaml-provider-spec-nutanix_cpmso-config-options-nutanix) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification.

The following example YAML illustrates a valid configuration for a Nutanix cluster.

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates.

In the following example, the `<cluster_id>` string is the infrastructure ID. The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

```
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```

**Sample Nutanix `providerSpec` values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            apiVersion: machine.openshift.io/v1
            bootType: ""
            categories:
            - key: <category_name>
              value: <category_value>
            cluster:
              type: uuid
              uuid: <cluster_uuid>
            credentialsSecret:
              name: nutanix-credentials
            image:
              name: <cluster_id>-rhcos
              type: name
            kind: NutanixMachineProviderConfig
            memorySize: 16Gi
            metadata:
              creationTimestamp: null
            project:
              type: name
              name: <project_name>
            subnets:
            - type: uuid
              uuid: <subnet_uuid>
            systemDiskSize: 120Gi
            userDataSecret:
              name: master-user-data
            vcpuSockets: 8
            vcpusPerSocket: 1
```

where:

`spec.template.spec.providerSpec.value.bootType`
:   Specifies the boot type that the control plane machines use. For more information about boot types, see [Understanding UEFI, Secure Boot, and TPM in the Virtualized Environment (Nutanix documentation)](https://portal.nutanix.com/page/documents/kbs/details?targetId=kA07V000000H3K9SAK).

    Valid values are `Legacy`, `SecureBoot`, or `UEFI`. The default is `Legacy`.

    Note

    You must use the `Legacy` boot type in OpenShift Container Platform 4.22.

`spec.template.spec.providerSpec.value.categories`
:   Specifies one or more Nutanix Prism categories to apply to control plane machines. This stanza requires `key` and `value` parameters for a category key-value pair that exists in Prism Central. For more information about categories, see [Category management](https://portal.nutanix.com/page/documents/details?targetId=Prism-Central-Guide-vpc_2022_6:ssp-ssp-categories-manage-pc-c.html).

`spec.template.spec.providerSpec.value.cluster`
:   Specifies a Nutanix Prism Element cluster configuration. In this example, the cluster type is `uuid`, so there is a `uuid` stanza.

    Note

    If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain.

`spec.template.spec.providerSpec.value.credentialsSecret`
:   Specifies the secret name for the cluster. Do not change this value.

`spec.template.spec.providerSpec.value.image`
:   Specifies the path to the source image for the disk.

`spec.template.spec.providerSpec.value.kind`
:   Specifies the cloud provider platform type. Do not change this value.

`spec.template.spec.providerSpec.value.memorySize`
:   Specifies the memory allocated for the control plane machines.

`spec.template.spec.providerSpec.value.project`
:   Specifies the Nutanix project that you use for your cluster. In this example, the project type is `name`, so there is a `name` stanza.

`spec.template.spec.providerSpec.value.subnets`
:   Specify one or more Prism Element subnet objects. In this example, the subnet type is `uuid`, so there is a `uuid` stanza. A maximum of 32 subnets for each Prism Element failure domain in the cluster is supported.

    Important

    Do not remove the original subnet, which hosts the API server and ingress server, from the cluster.

    The CIDR IP address prefix for one of the specified subnets must contain the virtual IP addresses that the OpenShift Container Platform cluster uses. All subnet UUID values must be unique.

    Note

    If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain.

`spec.template.spec.providerSpec.value.systemDiskSize`
:   Specifies the VM disk size for the control plane machines.

`spec.template.spec.providerSpec.value.userDataSecret`
:   Specifies the control plane user data secret. Do not change this value.

`spec.template.spec.providerSpec.value.vcpuSockets`
:   Specifies the number of vCPU sockets allocated for the control plane machines.

`spec.template.spec.providerSpec.value.vcpusPerSocket`
:   Specifies the number of vCPUs for each control plane vCPU socket.

##### [10.5.7.2. Failure domains for Nutanix clusters](#mapi-failure-domain-nutanix_cpmso-config-options-nutanix) Copy linkLink copied to clipboard!

To modify failure domain configurations on a Nutanix cluster, you must modify the cluster infrastructure, control plane machine set, and compute machine set custom resources (CRs) to apply the new configuration.

To add or update the failure domain configuration on a Nutanix cluster, you must make coordinated changes to several resources. The following actions are required:

1. Modify the cluster infrastructure custom resource (CR).
2. Modify the cluster control plane machine set CR.
3. Modify or replace the compute machine set CRs.

For more information, see "Adding failure domains to an existing Nutanix cluster".

##### [10.5.7.3. Improving reliability for multiple subnet configurations on Nutanix](#cpmso-ts-nutanix-multiple-subnet_cpmso-config-options-nutanix) Copy linkLink copied to clipboard!

To improve reliability and avoid common networking problems with multiple subnet configurations on Nutanix, adhere to the configuration practices that minimize networking conflicts.

The following networking configuration and management practices can help your multiple subnet configuration perform more reliably:

* To avoid overlapping IP address assignments, use predefined static IP addresses in the `cloud-init` metadata.
* Tag all VMs, disks, and networks with a unique cluster ID.
* Avoid IP address conflicts by using dedicated subnets for each OpenShift Container Platform cluster:

  Nutanix uses Nutanix Acropolis Hypervisor (AHV) and Nutanix Prism networking to assign IP addresses to virtual machines (VMs). If a single subnet provides IP addresses for more than one OpenShift Container Platform cluster, AHV or Prism might assign the same IP address to a VM or pod in more than one cluster.

  To avoid this issue, use dedicated subnets for each OpenShift Container Platform cluster, even when you have more than one cluster on a single Prism Central instance. You can use the Prism UI or automation tools, such as Terraform or Ansible, to create separate IP address pools for each OpenShift Container Platform cluster.
* Ensure that each OpenShift Container Platform cluster uses distinct DNS zones and virtual IP address ranges.
* Avoid DHCP conflicts by maintaining DHCP allocations:

  If you use Nutanix to manage DHCP allocation, objects in your cluster might have duplicate leases. Duplicate leases can cause DHCP conflicts when you apply changes to the control plane machine set custom resource (CR) specification.

  To avoid this issue, regularly remove stale DHCP leases.
* Use automation tools, such as Terraform or Ansible, to isolate the infrastructure for each OpenShift Container Platform cluster.

#### [10.5.8. Control plane configuration options for Red Hat OpenStack Platform (RHOSP)](#cpmso-config-options-openstack) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

The following example YAML snippets show provider specification and failure domain configurations for an RHOSP cluster.

##### [10.5.8.1. Sample RHOSP provider specification](#cpmso-yaml-provider-spec-openstack_cpmso-config-options-openstack) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification.

The following example YAML illustrates a valid configuration for an Red Hat OpenStack Platform (RHOSP) cluster.

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates.

You can omit any field that has a value set in the failure domain section of the CR.

In the following example, the `<cluster_id>` string is the infrastructure ID. The infrastructure ID matches the cluster ID that the installation program used during cluster provisioning. If you have the OpenShift CLI (`oc`) installed, you can obtain the infrastructure ID by running the following command:

```
$ oc get -o jsonpath='{.status.infrastructureName}{"\n"}' infrastructure cluster
```

**Sample OpenStack `providerSpec` values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            apiVersion: machine.openshift.io/v1alpha1
            cloudName: openstack
            cloudsSecret:
              name: openstack-cloud-credentials
              namespace: openshift-machine-api
            flavor: m1.xlarge
            image: <cluster_id>-rhcos
            kind: OpenstackProviderSpec
            metadata:
              creationTimestamp: null
            networks:
            - filter: {}
              subnets:
              - filter:
                  name: <cluster_id>-nodes
                  tags: openshiftClusterID=<cluster_id>
            securityGroups:
            - filter: {}
              name: <cluster_id>-master
            serverGroupName: <cluster_id>-master
            serverMetadata:
              Name: <cluster_id>-master
              openshiftClusterID: <cluster_id>
            tags:
            - openshiftClusterID=<cluster_id>
            trunk: true
            userDataSecret:
              name: master-user-data
```

where:

`spec.template.spec.providerSpec.value.cloudsSecret.name`
:   Specifies the secret name for the cluster. Do not change this value.

`spec.template.spec.providerSpec.value.flavor`
:   Specifies the RHOSP flavor type for the control plane.

`spec.template.spec.providerSpec.value.kind`
:   Specifies the cloud provider platform type. Do not change this value.

`spec.template.spec.providerSpec.value.securityGroups`
:   Specifies the control plane machines security group.

##### [10.5.8.2. Sample RHOSP failure domain configuration](#cpmso-yaml-failure-domain-openstack_cpmso-config-options-openstack) Copy linkLink copied to clipboard!

To prevent downtime for your applications due to the failure of a single Red Hat OpenStack Platform (RHOSP) region, you can configure failure domains in the control plane machine set by configuring appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` object.

The control plane machine set concept of a failure domain is analogous to the existing RHOSP concept of an [availability zone](https://docs.openstack.org/nova/latest/admin/availability-zones.html). The `ControlPlaneMachineSet` CR spreads control plane machines across more than one failure domain when possible.

**Sample OpenStack failure domain values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        openstack:
        - availabilityZone: nova-az0
          rootVolume:
            availabilityZone: cinder-az0
        - availabilityZone: nova-az1
          rootVolume:
            availabilityZone: cinder-az1
        - availabilityZone: nova-az2
          rootVolume:
            availabilityZone: cinder-az2
        platform: OpenStack
# ...
```

where:

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.openstack`
:   Specifies the availability zones for the failure domains. This example demonstrates the use of more than one Nova availability zone and corresponding Cinder availability zones.

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`
:   Specifies the cloud provider platform name. Do not change this value.

#### [10.5.9. Configuring Red Hat OpenStack Platform (RHOSP) features for control plane machines](#cpmso-supported-features-openstack) Copy linkLink copied to clipboard!

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

##### [10.5.9.1. Changing the RHOSP compute flavor by using a control plane machine set](#cpms-changing-openstack-flavor-type_cpmso-supported-features-openstack) Copy linkLink copied to clipboard!

You can change the Red Hat OpenStack Platform (RHOSP) compute service (Nova) flavor that your control plane machines use by updating the specification in the control plane machine set custom resource.

In RHOSP, flavors define the compute, memory, and storage capacity of computing instances. By increasing or decreasing the flavor size, you can scale your control plane vertically.

**Prerequisites**

* Your RHOSP cluster uses a control plane machine set.

**Procedure**

1. Edit the following line under the `providerSpec` field:

   ```
   providerSpec:
     value:
   # ...
       flavor: m1.xlarge
   ```

   where:

   providerSpec.value.flavor
   :   Specify a RHOSP flavor type that has the same base as the existing selection. For example, you can change `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`. You can choose larger or smaller flavors depending on your vertical scaling needs.
2. Save your changes.

   After you save your changes, machines are replaced with ones that use the flavor you chose.

#### [10.5.10. Control plane configuration options for VMware vSphere](#cpmso-config-options-vsphere) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your infrastructure or environment by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

The following example YAML snippets show provider specification and failure domain configurations for a vSphere cluster.

##### [10.5.10.1. Sample vSphere provider specification](#cpmso-yaml-provider-spec-vsphere_cpmso-config-options-vsphere) Copy linkLink copied to clipboard!

You can update your control plane machines to reflect changes in your underlying infrastructure by editing values in the control plane machine set provider specification.

The following example YAML illustrates a valid configuration for a VMware vSphere cluster.

Note

When you create a control plane machine set for an existing cluster, the provider specification must match the `providerSpec` configuration in the control plane machine custom resource (CR) that the installation program creates.

You can omit any field that has a value set in the failure domain section of the CR.

**Sample vSphere `providerSpec` values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
      spec:
        providerSpec:
          value:
            apiVersion: machine.openshift.io/v1beta1
            credentialsSecret:
              name: vsphere-cloud-credentials
            dataDisks:
            - name: "<disk_name>"
              provisioningMode: "<mode>"
              sizeGiB: 20
            diskGiB: 120
            kind: VSphereMachineProviderSpec
            memoryMiB: 16384
            metadata:
              creationTimestamp: null
            network:
              devices:
              - networkName: <vm_network_name>
            numCPUs: 4
            numCoresPerSocket: 4
            snapshot: ""
            template: <vm_template_name>
            userDataSecret:
              name: master-user-data
            workspace:
              datacenter: <vcenter_data_center_name>
              datastore: <vcenter_datastore_name>
              folder: <path_to_vcenter_vm_folder>
              resourcePool: <vsphere_resource_pool>
              server: <vcenter_server_ip>
```

where:

`spec.template.spec.providerSpec.value.credentialsSecret`
:   Specifies the secret name for the cluster. Do not change this value.

`spec.template.spec.providerSpec.value.dataDisks`
:   Specifies one or more data disk definitions. For more information, see "Configuring data disks by using machine sets".

`spec.template.spec.providerSpec.value.diskGiB`
:   Specifies the VM disk size for the control plane machines.

`spec.template.spec.providerSpec.value.kind`
:   Specifies the cloud provider platform type. Do not change this value.

`spec.template.spec.providerSpec.value.memoryMiB`
:   Specifies the memory allocated for the control plane machines.

`spec.template.spec.providerSpec.value.network`
:   Specifies the network on which to deploy the control plane.

    Note

    If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain.

`spec.template.spec.providerSpec.value.numCPUs`
:   Specifies the number of CPUs allocated for the control plane machines.

`spec.template.spec.providerSpec.value.numCoresPerSocket`
:   Specifies the number of cores for each control plane CPU.

`spec.template.spec.providerSpec.value.template`
:   Specifies the vSphere VM template to use, such as `user-5ddjd-rhcos`.

    Note

    If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain.

`spec.template.spec.providerSpec.value.userDataSecret`
:   Specifies the control plane user data secret. Do not change this value.

`spec.template.spec.providerSpec.value.workspace`
:   Specifies the workspace details for the control plane.

    Note

    If the cluster uses a failure domain, configure this parameter in the failure domain. If you specify this value in the provider specification when using a failure domain, the Control Plane Machine Set Operator ignores it and uses the value in the failure domain.

    The following keys in this stanza specify additional details:

    `datacenter`
    :   Specifies the vCenter datacenter for the control plane.

    `datastore`
    :   Specifies the vCenter datastore for the control plane.

    `folder`
    :   Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`.

    `resourcePool`
    :   Specifies the vSphere resource pool for your VMs.

    `server`
    :   Specifies the vCenter server IP or fully qualified domain name.

##### [10.5.10.2. Sample VMware vSphere failure domain configuration](#cpmso-yaml-failure-domain-vsphere_cpmso-config-options-vsphere) Copy linkLink copied to clipboard!

To prevent downtime for your applications due to the failure of a single VMware vSphere region, you can configure failure domains in the control plane machine set by configuring appropriate values in the `failureDomains` section of the `ControlPlaneMachineSet` object.

On vSphere infrastructure, the cluster-wide infrastructure custom resource definition (CRD), `infrastructures.config.openshift.io`, defines failure domains for your cluster. A failure domain is an infrastructure resource made up of a control plane machine set, a vCenter data center, vCenter datastore, and a network. The `providerSpec` in the `ControlPlaneMachineSet` custom resource (CR) specifies names for failure domains that the control plane machine set uses to ensure control plane nodes deploy on the appropriate failure domain.

By using a failure domain resource, you can use a control plane machine set to deploy control plane machines on separate clusters or data centers. A control plane machine set also balances control plane machines across defined failure domains to improve fault tolerance capabilities for your infrastructure.

Note

If you change the `ProviderSpec` configuration in the `ControlPlaneMachineSet` CR, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy.

**Sample VMware vSphere failure domain values**

```
apiVersion: machine.openshift.io/v1
kind: ControlPlaneMachineSet
metadata:
  name: cluster
  namespace: openshift-machine-api
spec:
# ...
  template:
# ...
    machines_v1beta1_machine_openshift_io:
      failureDomains:
        vsphere:
        - name: <failure_domain_name_1>
        - name: <failure_domain_name_2>
        platform: VSphere
# ...
```

where:

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.vsphere.name`
:   Each instance of `name` specifies a failure domain.

    Important

    Each `name` field value in the stanza must match the corresponding value in the `failureDomains.name` field of the cluster-wide infrastructure CRD. You can find the value of the `failureDomains.name` field by running the following command:

    ```
    $ oc get infrastructure cluster -o=jsonpath={.spec.platformSpec.vsphere.failureDomains[0].name}
    ```

    The `name` field is the only supported failure domain field that you can specify in the `ControlPlaneMachineSet` CR.

    For an example of a cluster-wide infrastructure CRD that defines resources for each failure domain, see "Specifying multiple regions and zones for your cluster on vSphere."

`spec.template.machines_v1beta1_machine_openshift_io.failureDomains.platform`
:   Specifies the cloud provider platform name. Do not change this value.

#### [10.5.11. Configuring VMware vSphere features for control plane machines](#cpmso-supported-features-vsphere) Copy linkLink copied to clipboard!

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

##### [10.5.11.1. Adding tags to machines by using machine sets](#machine-api-vmw-add-tags_cpmso-supported-features-vsphere) Copy linkLink copied to clipboard!

To ensure that your cluster remains scalable and resilient, you can use a `MachineSet` object and machine health checks to automate the provisioning and repair of nodes.

OpenShift Container Platform adds a cluster-specific tag to each virtual machine (VM) that it creates. The installation program uses these tags to select the VMs to delete when uninstalling a cluster.

In addition to the cluster-specific tags assigned to VMs, you can configure a machine set to add up to 10 additional vSphere tags to the VMs it provisions.

**Prerequisites**

* You have access to an OpenShift Container Platform cluster installed on vSphere using an account with `cluster-admin` permissions.
* You have access to the VMware vCenter console associated with your cluster.
* You have created a tag in the vCenter console.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Use the vCenter console to find the tag ID for any tag that you want to add to your machines:

   1. Log in to the vCenter console.
   2. From the **Home** menu, click **Tags & Custom Attributes**.
   3. Select a tag that you want to add to your machines.
   4. Use the browser URL for the tag that you select to identify the tag ID.

      **Example tag URL**

      ```
      https://vcenter.example.com/ui/app/tags/tag/urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL/permissions
      ```

      **Example tag ID**

      ```
      urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL
      ```
2. In a text editor, open the YAML file for an existing machine set or create a new one.
3. Edit the following lines under the `providerSpec` field:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       spec:
         providerSpec:
           value:
             tagIDs:
             - <tag_id_value>
   # ...
   ```

   where

   `spec.template.spec.providerSpec.value.tagIDs`
   :   Specifies a list of up to 10 tags to add to the machines that this machine set provisions. Replace `<tag_id_value>` with the tag that you want to add to your machines. For example, `urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL`.

##### [10.5.11.2. Configuring data disks by using machine sets](#machineset-vsphere-data-disks_cpmso-supported-features-vsphere) Copy linkLink copied to clipboard!

To provide persistent storage beyond the root volume for specialized application workloads, define a `dataDisks` array in the `MachineSet` YAML file to specify disk size and storage policy.

OpenShift Container Platform clusters on VMware vSphere support adding up to 29 disks to the virtual machine (VM) controller.

Important

Configuring vSphere data disks is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

By configuring data disks, you can attach disks to VMs and use them to store data for etcd, container images, and other uses. Separating data can help avoid filling the primary disk so that important activities such as upgrades have the resources that they require.

Note

Adding data disks attaches them to the VM and mounts them to the location that RHCOS designates.

**Prerequisites**

* You have administrator access to OpenShift CLI (`oc`) for an OpenShift Container Platform cluster on vSphere.

**Procedure**

1. In a text editor, open the YAML file for an existing machine set or create a new one.
2. Edit the following lines under the `providerSpec` field:

   ```
   apiVersion: machine.openshift.io/v1
   kind: ControlPlaneMachineSet
   # ...
   spec:
     template:
       machines_v1beta1_machine_openshift_io:
         spec:
           providerSpec:
             value:
               dataDisks:
               - name: "<disk_name>"
                 provisioningMode: "<mode>"
                 sizeGiB: 20
               - name: "<disk_name>"
                 provisioningMode: "<mode>"
                 sizeGiB: 20
   # ...
   ```

   where

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks`
   :   Specifies a collection of 1-29 data disk definitions. This sample configuration shows the formatting to include two data disk definitions.

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks.name`
   :   Specifies the name of the data disk. The name must meet the following requirements:

       * Start and end with an alphanumeric character
       * Consist only of alphanumeric characters, hyphens (`-`), and underscores (`_`)
       * Have a maximum length of 80 characters

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks.provisioningMode`
   :   Specifies the data disk provisioning method. This value defaults to the vSphere default storage policy if not set. Valid values are `Thin`, `Thick`, and `EagerlyZeroed`.

   `spec.template.machines_v1beta1_machine_openshift_io.spec.providerSpec.value.dataDisks.sizeGiB`
   :   Specifies the size of the data disk in GiB. The maximum size is 16,384 GiB.

### [10.6. Control plane resiliency and recovery](#cpmso-resiliency) Copy linkLink copied to clipboard!

You can use the control plane machine set to improve the resiliency of the control plane for your OpenShift Container Platform cluster.

#### [10.6.1. High availability and fault tolerance with failure domains](#cpmso-failure-domains_cpmso-resiliency) Copy linkLink copied to clipboard!

When possible, the control plane machine set spreads the control plane machines across multiple failure domains. This configuration provides high availability and fault tolerance within the control plane. This strategy can help protect the control plane when issues arise within the infrastructure provider.

##### [10.6.1.1. Failure domain platform support and configuration](#cpmso-failure-domains-provider_cpmso-resiliency) Copy linkLink copied to clipboard!

Review failure domain support for your cloud provider to determine how to configure high availability for your control plane.

Expand

Table 10.3. Failure domain support matrix

| Cloud provider | Support for failure domains | Provider nomenclature |
| --- | --- | --- |
| Amazon Web Services (AWS) | X | [Availability Zone (AZ)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#concepts-availability-zones) |
| Google Cloud | X | [zone](https://cloud.google.com/compute/docs/regions-zones) |
| Microsoft Azure | X | [Azure availability zone](https://learn.microsoft.com/en-us/azure/azure-web-pubsub/concept-availability-zones) |
| Nutanix | X | [failure domain](https://portal.nutanix.com/page/documents/solutions/details?targetId=RA-2147-Nutanix-for-Enterprise-Edge:failure-domain-considerations.html) |
| Red Hat OpenStack Platform (RHOSP) | X | [OpenStack Nova availability zones](https://docs.openstack.org/nova/2023.2/admin/availability-zones.html) and [OpenStack Cinder availability zones](https://docs.openstack.org/cinder/2023.2/admin/availability-zone-type.html) |
| VMware vSphere | X | failure domain mapped to a vSphere Zone [1] |

Show more

1. For more information, see "Regions and zones for a VMware vCenter".

The failure domain configuration in the control plane machine set custom resource (CR) is platform-specific. For more information about failure domain parameters in the CR, see the sample failure domain configuration for your provider.

##### [10.6.1.2. Balancing control plane machines](#cpmso-failure-domains-balancing_cpmso-resiliency) Copy linkLink copied to clipboard!

The control plane machine set balances control plane machines across failure domains to ensure fault tolerance and high availability.

When possible, the control plane machine set uses each failure domain equally to ensure appropriate fault tolerance. If there are fewer failure domains than control plane machines, failure domains are selected for reuse alphabetically by name. For clusters with no failure domains specified, all control plane machines are placed within a single failure domain.

Some changes to the failure domain configuration cause the control plane machine set to rebalance the control plane machines. For example, if you add failure domains to a cluster with fewer failure domains than control plane machines, the control plane machine set rebalances the machines across all available failure domains.

#### [10.6.2. Recovery of failed control plane machines](#cpmso-control-plane-recovery_cpmso-resiliency) Copy linkLink copied to clipboard!

The Control Plane Machine Set Operator automates the recovery of control plane machines to maintain cluster availability without manual intervention.

When a control plane machine is deleted, the Operator creates a replacement with the configuration that is specified in the `ControlPlaneMachineSet` custom resource (CR).

For clusters that use control plane machine sets, you can configure a machine health check. The machine health check deletes unhealthy control plane machines so that they are replaced.

Important

If you configure a `MachineHealthCheck` resource for the control plane, set the value of `maxUnhealthy` to `1`.

This configuration ensures that the machine health check takes no action when multiple control plane machines appear to be unhealthy. Multiple unhealthy control plane machines can indicate that the etcd cluster is degraded or that a scaling operation to replace a failed machine is in progress.

If the etcd cluster is degraded, manual intervention might be required. If a scaling operation is in progress, the machine health check should allow it to finish.

#### [10.6.3. Quorum protection with machine lifecycle hooks](#machine-lifecycle-hook-deletion-etcd_cpmso-resiliency) Copy linkLink copied to clipboard!

To protect etcd quorum on OpenShift Container Platform clusters that use the Machine API Operator, the etcd Operator uses lifecycle hooks for the machine deletion phase to implement a quorum protection mechanism.

By using a `preDrain` lifecycle hook, the etcd Operator can control when the pods on a control plane machine are drained and removed. To protect etcd quorum, the etcd Operator prevents the removal of an etcd member until it migrates that member onto a new node within the cluster.

This mechanism allows the etcd Operator precise control over the members of the etcd quorum and allows the Machine API Operator to safely create and remove control plane machines without specific operational knowledge of the etcd cluster.

##### [10.6.3.1. Control plane deletion with quorum protection processing order](#machine-lifecycle-hook-deletion-etcd-order_cpmso-resiliency) Copy linkLink copied to clipboard!

When a control plane machine is replaced on a cluster that uses a control plane machine set, the cluster temporarily has four control plane machines. When the fourth control plane node joins the cluster, the etcd Operator starts a new etcd member on the replacement node. When the etcd Operator observes that the old control plane machine is marked for deletion, it stops the etcd member on the old node and promotes the replacement etcd member to join the quorum of the cluster.

The control plane machine `Deleting` phase proceeds in the following order:

1. A control plane machine is slated for deletion.
2. The control plane machine enters the `Deleting` phase.
3. To satisfy the `preDrain` lifecycle hook, the etcd Operator takes the following actions:

   1. The etcd Operator waits until a fourth control plane machine is added to the cluster as an etcd member. This new etcd member has a state of `Running` but not `ready` until it receives the full database update from the etcd leader.
   2. When the new etcd member receives the full database update, the etcd Operator promotes the new etcd member to a voting member and removes the old etcd member from the cluster.

   After this transition is complete, it is safe for the old etcd pod and its data to be removed, so the `preDrain` lifecycle hook is removed.
4. The control plane machine status condition `Drainable` is set to `True`.
5. The machine controller attempts to drain the node that is backed by the control plane machine.

   * If draining fails, `Drained` is set to `False` and the machine controller attempts to drain the node again.
   * If draining succeeds, `Drained` is set to `True`.
6. The control plane machine status condition `Drained` is set to `True`.
7. If no other Operators have added a `preTerminate` lifecycle hook, the control plane machine status condition `Terminable` is set to `True`.
8. The machine controller removes the instance from the infrastructure provider.
9. The machine controller deletes the `Node` object.

**YAML snippet demonstrating the etcd quorum protection `preDrain` lifecycle hook**

```
apiVersion: machine.openshift.io/v1beta1
kind: Machine
metadata:
  ...
spec:
  lifecycleHooks:
    preDrain:
    - name: EtcdQuorumOperator
      owner: clusteroperator/etcd
  ...
```

where:

`spec.lifecycleHooks.preDrain.name`
:   Specifies the name of the `preDrain` lifecycle hook.

`spec.lifecycleHooks.preDrain.owner`
:   Specifies the hook-implementing controller that manages the `preDrain` lifecycle hook.

### [10.7. Troubleshooting the control plane machine set](#cpmso-troubleshooting) Copy linkLink copied to clipboard!

Use the following information to understand and recover from issues you might encounter.

#### [10.7.1. Checking the control plane machine set custom resource state](#cpmso-checking-status_cpmso-troubleshooting) Copy linkLink copied to clipboard!

Check the state of the control plane machine set custom resource to determine if it is active, inactive, or missing before making configuration changes.

**Procedure**

* Determine the state of the CR by running the following command:

  ```
  $ oc get controlplanemachineset.machine.openshift.io cluster \
    --namespace openshift-machine-api
  ```

  + A result of `Active` indicates that the `ControlPlaneMachineSet` CR exists and is activated. No administrator action is required.
  + A result of `Inactive` indicates that a `ControlPlaneMachineSet` CR exists but is not activated.
  + A result of `NotFound` indicates that there is no existing `ControlPlaneMachineSet` CR.

**Next steps**

To use the control plane machine set, you must ensure that a `ControlPlaneMachineSet` CR with the correct settings for your cluster exists.

* If your cluster has an existing CR, you must verify that the configuration in the CR is correct for your cluster.
* If your cluster does not have an existing CR, you must create one with the correct configuration for your cluster.

#### [10.7.2. Adding a missing Azure internal load balancer](#cpmso-ts-ilb-missing_cpmso-troubleshooting) Copy linkLink copied to clipboard!

Add the required `internalLoadBalancer` parameter to Azure control plane resources to ensure proper load balancing configuration.

For more information about where this parameter is located in the Azure provider specification, see the sample Azure provider specification. The placement in the control plane `Machine` CR is similar.

**Procedure**

1. List the control plane machines in your cluster by running the following command:

   ```
   $ oc get machines \
     -l machine.openshift.io/cluster-api-machine-role==master \
     -n openshift-machine-api
   ```
2. For each control plane machine, edit the CR by running the following command:

   ```
   $ oc edit machine <control_plane_machine_name>
   ```
3. Add the `internalLoadBalancer` parameter with the correct details for your cluster and save your changes.
4. Edit your control plane machine set CR by running the following command:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io cluster \
     -n openshift-machine-api
   ```
5. Add the `internalLoadBalancer` parameter with the correct details for your cluster and save your changes.

**Next steps**

* For clusters that use the default `RollingUpdate` update strategy, the Operator automatically propagates the changes to your control plane configuration.
* For clusters that are configured to use the `OnDelete` update strategy, you must replace your control plane machines manually.

#### [10.7.3. Recovering a degraded etcd Operator](#cpmso-ts-etcd-degraded_cpmso-troubleshooting) Copy linkLink copied to clipboard!

Recover a degraded etcd Operator by removing failed members to restore cluster state after machine health check operations.

For example, while performing remediation, the machine health check might delete a control plane machine that is hosting etcd. If the etcd member is not reachable at that time, the etcd Operator becomes degraded.

When the etcd Operator is degraded, manual intervention is required to force the Operator to remove the failed member and restore the cluster state.

**Procedure**

1. List the control plane machines in your cluster by running the following command:

   ```
   $ oc get machines \
     -l machine.openshift.io/cluster-api-machine-role==master \
     -n openshift-machine-api \
     -o wide
   ```

   Any of the following conditions might indicate a failed control plane machine:

   * The `STATE` value is `stopped`.
   * The `PHASE` value is `Failed`.
   * The `PHASE` value is `Deleting` for more than ten minutes.

   Important

   Before continuing, ensure that your cluster has two healthy control plane machines. Performing the actions in this procedure on more than one control plane machine risks losing etcd quorum and can cause data loss.

   If you have lost the majority of your control plane hosts, leading to etcd quorum loss, then you must follow the disaster recovery procedure "Restoring to an earlier cluster state" instead of this procedure.
2. Edit the machine CR for the failed control plane machine by running the following command:

   ```
   $ oc edit machine <control_plane_machine_name>
   ```
3. Remove the contents of the `lifecycleHooks` parameter from the failed control plane machine and save your changes.

   The etcd Operator removes the failed machine from the cluster and can then safely add new etcd members.

#### [10.7.4. Upgrading clusters that run on RHOSP](#cpmso-ts-openstack-upgrade_cpmso-troubleshooting) Copy linkLink copied to clipboard!

Review post-upgrade requirements for clusters running on Red Hat OpenStack Platform (RHOSP) to ensure control plane machine sets function correctly.

For clusters that run on RHOSP that were created with OpenShift Container Platform 4.13 or earlier, you might have to perform post-upgrade tasks before you can use control plane machine sets.

##### [10.7.4.1. Configuring RHOSP clusters that have machines with root volume availability zones after an upgrade](#cpmso-openstack-ts-root-volume-azs_cpmso-troubleshooting) Copy linkLink copied to clipboard!

For some clusters that run on Red Hat OpenStack Platform (RHOSP) that you upgrade, you must manually update machine resources before you can use control plane machine sets if the following configurations are true:

* The upgraded cluster was created with OpenShift Container Platform 4.13 or earlier.
* The cluster infrastructure is installer-provisioned.
* Machines were distributed across multiple availability zones.
* Machines were configured to use root volumes for which block storage availability zones were not defined.

To understand why this procedure is necessary, see [Solution #7024383](https://access.redhat.com/solutions/7013893).

**Procedure**

1. For all control plane machines, edit the provider spec for all control plane machines that match the environment. For example, to edit the machine `master-0`, enter the following command:

   ```
   $ oc edit machine/<cluster_id>-master-0 -n openshift-machine-api
   ```

   where:

   `<cluster_id>`
   :   Specifies the ID of the upgraded cluster.
2. In the provider spec, set the value of the property `rootVolume.availabilityZone` to the volume of the availability zone you want to use.

   **An example RHOSP provider spec**

   ```
   providerSpec:
     value:
       apiVersion: machine.openshift.io/v1alpha1
       availabilityZone: az0
         cloudName: openstack
       cloudsSecret:
         name: openstack-cloud-credentials
         namespace: openshift-machine-api
       flavor: m1.xlarge
       image: rhcos-4.14
       kind: OpenstackProviderSpec
       metadata:
         creationTimestamp: null
       networks:
       - filter: {}
         subnets:
         - filter:
             name: refarch-lv7q9-nodes
             tags: openshiftClusterID=refarch-lv7q9
       rootVolume:
           availabilityZone: nova
           diskSize: 30
           sourceUUID: rhcos-4.12
           volumeType: fast-0
       securityGroups:
       - filter: {}
         name: refarch-lv7q9-master
       serverGroupName: refarch-lv7q9-master
       serverMetadata:
         Name: refarch-lv7q9-master
         openshiftClusterID: refarch-lv7q9
       tags:
       - openshiftClusterID=refarch-lv7q9
       trunk: true
       userDataSecret:
         name: master-user-data
   ```

   where:

   `availabilityZone: nova`
   :   Specifies the zone name for the root volume.

       Note

       If you edited or recreated machine resources after your initial cluster deployment, you might have to adapt these steps for your configuration.

       In your RHOSP cluster, find the availability zone of the root volumes for your machines and use that as the value.
3. Run the following command to retrieve information about the control plane machine set resource:

   ```
   $ oc describe controlplanemachineset.machine.openshift.io/cluster --namespace openshift-machine-api
   ```
4. Run the following command to edit the resource:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io/cluster --namespace openshift-machine-api
   ```
5. For that resource, set the value of the `spec.state` property to `Active` to activate control plane machine sets for your cluster.

   The control plane is now ready to be managed by the Cluster Control Plane Machine Set Operator.

##### [10.7.4.2. Configuring RHOSP clusters that have control plane machines with availability zones after an upgrade](#cpmso-openstack-with-az-config_cpmso-troubleshooting) Copy linkLink copied to clipboard!

For some clusters that run on Red Hat OpenStack Platform (RHOSP) that you upgrade, you must manually update machine resources before you can use control plane machine sets if the following configurations are true:

* The upgraded cluster was created with OpenShift Container Platform 4.13 or earlier.
* The cluster infrastructure is installer-provisioned.
* Control plane machines were distributed across multiple compute availability zones.

To understand why this procedure is necessary, see [Solution #7013893](https://access.redhat.com/solutions/7013893).

**Procedure**

1. For the `master-1` and `master-2` control plane machines, open the provider specs for editing. For example, to edit the first machine, enter the following command:

   ```
   $ oc edit machine/<cluster_id>-master-1 -n openshift-machine-api
   ```

   where:

   `<cluster_id>`
   :   Specifies the ID of the upgraded cluster.
2. For the `master-1` and `master-2` control plane machines, edit the value of the `serverGroupName` property in their provider specs to match that of the machine `master-0`.

   **An example RHOSP provider spec**

   ```
   providerSpec:
     value:
       apiVersion: machine.openshift.io/v1alpha1
       availabilityZone: az0
         cloudName: openstack
       cloudsSecret:
         name: openstack-cloud-credentials
         namespace: openshift-machine-api
       flavor: m1.xlarge
       image: rhcos-4.22
       kind: OpenstackProviderSpec
       metadata:
         creationTimestamp: null
       networks:
       - filter: {}
         subnets:
         - filter:
             name: refarch-lv7q9-nodes
             tags: openshiftClusterID=refarch-lv7q9
       securityGroups:
       - filter: {}
         name: refarch-lv7q9-master
       serverGroupName: refarch-lv7q9-master-az0
       serverMetadata:
         Name: refarch-lv7q9-master
         openshiftClusterID: refarch-lv7q9
       tags:
       - openshiftClusterID=refarch-lv7q9
       trunk: true
       userDataSecret:
         name: master-user-data
   ```

   where:

   `serverGroupName`
   :   Specifies the server group name. This value must match for machines `master-0`, `master-1`, and `master-2`.

       Note

       If you edited or recreated machine resources after your initial cluster deployment, you might have to adapt these steps for your configuration.

       In your RHOSP cluster, find the server group that your control plane instances are in and use that as the value.
3. Run the following command to retrieve information about the control plane machine set resource:

   ```
   $ oc describe controlplanemachineset.machine.openshift.io/cluster --namespace openshift-machine-api
   ```
4. Run the following command to edit the resource:

   ```
   $ oc edit controlplanemachineset.machine.openshift.io/cluster --namespace openshift-machine-api
   ```
5. For that resource, set the value of the `spec.state` property to `Active` to activate control plane machine sets for your cluster.

   The control plane is now ready to be managed by the Cluster Control Plane Machine Set Operator.

#### [10.7.5. Improving reliability for multiple subnet configurations on Nutanix](#cpmso-ts-nutanix-multiple-subnet_cpmso-troubleshooting) Copy linkLink copied to clipboard!

To improve reliability and avoid common networking problems with multiple subnet configurations on Nutanix, adhere to the configuration practices that minimize networking conflicts.

The following networking configuration and management practices can help your multiple subnet configuration perform more reliably:

* To avoid overlapping IP address assignments, use predefined static IP addresses in the `cloud-init` metadata.
* Tag all VMs, disks, and networks with a unique cluster ID.
* Avoid IP address conflicts by using dedicated subnets for each OpenShift Container Platform cluster:

  Nutanix uses Nutanix Acropolis Hypervisor (AHV) and Nutanix Prism networking to assign IP addresses to virtual machines (VMs). If a single subnet provides IP addresses for more than one OpenShift Container Platform cluster, AHV or Prism might assign the same IP address to a VM or pod in more than one cluster.

  To avoid this issue, use dedicated subnets for each OpenShift Container Platform cluster, even when you have more than one cluster on a single Prism Central instance. You can use the Prism UI or automation tools, such as Terraform or Ansible, to create separate IP address pools for each OpenShift Container Platform cluster.
* Ensure that each OpenShift Container Platform cluster uses distinct DNS zones and virtual IP address ranges.
* Avoid DHCP conflicts by maintaining DHCP allocations:

  If you use Nutanix to manage DHCP allocation, objects in your cluster might have duplicate leases. Duplicate leases can cause DHCP conflicts when you apply changes to the control plane machine set custom resource (CR) specification.

  To avoid this issue, regularly remove stale DHCP leases.
* Use automation tools, such as Terraform or Ansible, to isolate the infrastructure for each OpenShift Container Platform cluster.

### [10.8. Disabling the control plane machine set](#cpmso-disabling) Copy linkLink copied to clipboard!

Disable the control plane machine set if you need to manually manage control plane machines or troubleshoot Operator behavior.

The `.spec.state` field in an activated `ControlPlaneMachineSet` custom resource (CR) cannot be changed from `Active` to `Inactive`. To disable the control plane machine set, you must delete the CR so that it is removed from the cluster.

When you delete the CR, the Control Plane Machine Set Operator performs cleanup operations and disables the control plane machine set. The Operator then removes the CR from the cluster and creates an inactive control plane machine set with default settings.

#### [10.8.1. Deleting the control plane machine set](#cpmso-deleting_cpmso-disabling) Copy linkLink copied to clipboard!

To stop managing control plane machines with the control plane machine set on your cluster, you must delete the `ControlPlaneMachineSet` custom resource (CR).

**Procedure**

* Delete the control plane machine set CR by running the following command:

  ```
  $ oc delete controlplanemachineset.machine.openshift.io cluster \
    -n openshift-machine-api
  ```

**Verification**

* Check the control plane machine set custom resource state. A result of `Inactive` indicates that the removal and replacement process is successful. A `ControlPlaneMachineSet` CR exists but is not activated.

#### [10.8.2. Checking the control plane machine set custom resource state](#cpmso-checking-status_cpmso-disabling) Copy linkLink copied to clipboard!

Check the state of the control plane machine set custom resource to determine if it is active, inactive, or missing before making configuration changes.

**Procedure**

* Determine the state of the CR by running the following command:

  ```
  $ oc get controlplanemachineset.machine.openshift.io cluster \
    --namespace openshift-machine-api
  ```

  + A result of `Active` indicates that the `ControlPlaneMachineSet` CR exists and is activated. No administrator action is required.
  + A result of `Inactive` indicates that a `ControlPlaneMachineSet` CR exists but is not activated.
  + A result of `NotFound` indicates that there is no existing `ControlPlaneMachineSet` CR.

#### [10.8.3. Re-enabling the control plane machine set](#cpmso-reenabling_cpmso-disabling) Copy linkLink copied to clipboard!

Restore automated control plane management after previously disabling the control plane machine set.

To re-enable the control plane machine set, you must ensure that the configuration in the CR is correct for your cluster and activate it.

For more information, see "Activating the control plane machine set custom resource".

### [10.9. Manually scaling control plane machines](#cpmso-manually-scaling-control-planes) Copy linkLink copied to clipboard!

Manually scale to 4 or 5 control plane nodes on bare-metal infrastructure to recover from a degraded state, perform deep-level debugging, or ensure control plane stability in complex scenarios.

Important

Red Hat supports a cluster that has 4 or 5 control plane nodes only on bare-metal infrastructure.

#### [10.9.1. Adding a control plane node to your cluster](#creating-control-plane-node_cpmso-manually-scaling-control-planes) Copy linkLink copied to clipboard!

Add a control plane node to recover from a degraded state, perform deep-level debugging, or ensure stability and security of the control plane in complex bare metal scenarios.

**Prerequisites**

* You have installed a healthy cluster with at least three control plane nodes.
* You have created a single control plane node that you intend to add to your cluster as a postinstalltion task.

**Procedure**

1. Retrieve pending Certificate Signing Requests (CSRs) for the new control plane node by entering the following command:

   ```
   $ oc get csr | grep Pending
   ```
2. Approve all pending CSRs for the control plane node by entering the following command:

   ```
   $ oc get csr -o go-template='{{range .items}}{{if not .status}}{{.metadata.name}}{{"\n"}}{{end}}{{end}}' | xargs --no-run-if-empty oc adm certificate approve
   ```

   Important

   You must approve the CSRs to complete the installation.
3. Confirm that the control plane node is in the `Ready` status by entering the following command:

   ```
   $ oc get nodes
   ```

   Note

   On installer-provisioned infrastructure, the etcd Operator relies on the Machine API to manage the control plane and ensure etcd quorum. The Machine API then uses `Machine` CRs to represent and manage the underlying control plane nodes.
4. Create the `BareMetalHost` and `Machine` CRs and link them to the `Node` CR of the control plane node.

   1. Create the `BareMetalHost` CR with a unique `.metadata.name` value as demonstrated in the following example:

      ```
      apiVersion: metal3.io/v1alpha1
      kind: BareMetalHost
      metadata:
        name: node-5
        namespace: openshift-machine-api
      spec:
        automatedCleaningMode: metadata
        bootMACAddress: 00:00:00:00:00:02
        bootMode: UEFI
        customDeploy:
          method: install_coreos
        externallyProvisioned: true
        online: true
        userData:
          name: master-user-data-managed
          namespace: openshift-machine-api
      # ...
      ```
   2. Apply the `BareMetalHost` CR by entering the following command:

      ```
      $ oc apply -f <filename>
      ```

      where `<filename>` specifies the name of the `BareMetalHost` CR.
   3. Create the `Machine` CR by using the unique `.metadata.name` value as demonstrated in the following example:

      ```
      apiVersion: machine.openshift.io/v1beta1
      kind: Machine
      metadata:
        annotations:
          machine.openshift.io/instance-state: externally provisioned
          metal3.io/BareMetalHost: openshift-machine-api/node-5
        finalizers:
        - machine.machine.openshift.io
        labels:
          machine.openshift.io/cluster-api-cluster: <cluster_name>
          machine.openshift.io/cluster-api-machine-role: master
          machine.openshift.io/cluster-api-machine-type: master
        name: node-5
        namespace: openshift-machine-api
      spec:
        metadata: {}
        providerSpec:
          value:
            apiVersion: baremetal.cluster.k8s.io/v1alpha1
            customDeploy:
              method: install_coreos
            hostSelector: {}
            image:
              checksum: ""
              url: ""
            kind: BareMetalMachineProviderSpec
            metadata:
              creationTimestamp: null
            userData:
              name: master-user-data-managed
      # ...
      ```

      where `<cluster_name>` specifies the name of the specific cluster, for example, `test-day2-1-6qv96`.
   4. Get the cluster name by running the following command:

      ```
      $ oc get infrastructure cluster -o=jsonpath='{.status.infrastructureName}{"\n"}'
      ```
   5. Apply the `Machine` CR by entering the following command:

      ```
      $ oc apply -f <filename>
      ```

      where `<filename>` specifies the name of the `Machine` CR.
   6. Link `BareMetalHost`, `Machine`, and `Node` objects by running the `link-machine-and-node.sh` script:

      1. Copy the following `link-machine-and-node.sh` script to a local machine:

         ```
         #!/bin/bash

         # Credit goes to
         # https://bugzilla.redhat.com/show_bug.cgi?id=1801238.
         # This script will link Machine object
         # and Node object. This is needed
         # in order to have IP address of
         # the Node present in the status of the Machine.

         set -e

         machine="$1"
         node="$2"

         if [ -z "$machine" ] || [ -z "$node" ]; then
             echo "Usage: $0 MACHINE NODE"
             exit 1
         fi

         node_name=$(echo "${node}" | cut -f2 -d':')

         oc proxy &
         proxy_pid=$!
         function kill_proxy {
             kill $proxy_pid
         }
         trap kill_proxy EXIT SIGINT

         HOST_PROXY_API_PATH="http://localhost:8001/apis/metal3.io/v1alpha1/namespaces/openshift-machine-api/baremetalhosts"

         function print_nics() {
             local ips
             local eob
             declare -a ips

             readarray -t ips < <(echo "${1}" \
                                  | jq '.[] | select(. | .type == "InternalIP") | .address' \
                                  | sed 's/"//g')

             eob=','
             for (( i=0; i<${#ips[@]}; i++ )); do
                 if [ $((i+1)) -eq ${#ips[@]} ]; then
                     eob=""
                 fi
                 cat <<- EOF
                   {
                     "ip": "${ips[$i]}",
                     "mac": "00:00:00:00:00:00",
                     "model": "unknown",
                     "speedGbps": 10,
                     "vlanId": 0,
                     "pxe": true,
                     "name": "eth1"
                   }${eob}
         EOF
             done
         }

         function wait_for_json() {
             local name
             local url
             local curl_opts
             local timeout

             local start_time
             local curr_time
             local time_diff

             name="$1"
             url="$2"
             timeout="$3"
             shift 3
             curl_opts="$@"
             echo -n "Waiting for $name to respond"
             start_time=$(date +%s)
             until curl -g -X GET "$url" "${curl_opts[@]}" 2> /dev/null | jq '.' 2> /dev/null > /dev/null; do
                 echo -n "."
                 curr_time=$(date +%s)
                 time_diff=$((curr_time - start_time))
                 if [[ $time_diff -gt $timeout ]]; then
                     printf '\nTimed out waiting for %s' "${name}"
                     return 1
                 fi
                 sleep 5
             done
             echo " Success!"
             return 0
         }
         wait_for_json oc_proxy "${HOST_PROXY_API_PATH}" 10 -H "Accept: application/json" -H "Content-Type: application/json"

         addresses=$(oc get node -n openshift-machine-api "${node_name}" -o json | jq -c '.status.addresses')

         machine_data=$(oc get machines.machine.openshift.io -n openshift-machine-api -o json "${machine}")
         host=$(echo "$machine_data" | jq '.metadata.annotations["metal3.io/BareMetalHost"]' | cut -f2 -d/ | sed 's/"//g')

         if [ -z "$host" ]; then
             echo "Machine $machine is not linked to a host yet." 1>&2
             exit 1
         fi

         # The address structure on the host doesn't match the node, so extract
         # the values we want into separate variables so we can build the patch
         # we need.
         hostname=$(echo "${addresses}" | jq '.[] | select(. | .type == "Hostname") | .address' | sed 's/"//g')

         set +e
         read -r -d '' host_patch << EOF
         {
           "status": {
             "hardware": {
               "hostname": "${hostname}",
               "nics": [
         $(print_nics "${addresses}")
               ],
               "systemVendor": {
                 "manufacturer": "Red Hat",
                 "productName": "product name",
                 "serialNumber": ""
               },
               "firmware": {
                 "bios": {
                   "date": "04/01/2014",
                   "vendor": "SeaBIOS",
                   "version": "1.11.0-2.el7"
                 }
               },
               "ramMebibytes": 0,
               "storage": [],
               "cpu": {
                 "arch": "x86_64",
                 "model": "Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",
                 "clockMegahertz": 2199.998,
                 "count": 4,
                 "flags": []
               }
             }
           }
         }
         EOF
         set -e

         echo "PATCHING HOST"
         echo "${host_patch}" | jq .

         curl -s \
              -X PATCH \
              "${HOST_PROXY_API_PATH}/${host}/status" \
              -H "Content-type: application/merge-patch+json" \
              -d "${host_patch}"

         oc get baremetalhost -n openshift-machine-api -o yaml "${host}"
         ```
      2. Make the script executable by entering the following command:

         ```
         $ chmod +x link-machine-and-node.sh
         ```
      3. Run the script by entering the following command:

         ```
         $ bash link-machine-and-node.sh node-5 node-5
         ```

         Note

         The first `node-5` instance represents the machine, and the second instance represents the node.

**Verification**

1. Confirm members of etcd by executing into one of the pre-existing control plane nodes:

   1. Open a remote shell session to the control plane node by entering the following command:

      ```
      $ oc rsh -n openshift-etcd etcd-node-0
      ```
   2. List etcd members:

      ```
      # etcdctl member list -w table
      ```
2. Check the etcd Operator configuration process until completion by entering the following command. Expected output shows `False` under the `PROGRESSING` column.

   ```
   $ oc get clusteroperator etcd
   ```
3. Confirm etcd health by running the following commands:

   1. Open a remote shell session to the control plane node:

      ```
      $ oc rsh -n openshift-etcd etcd-node-0
      ```
   2. Check endpoint health. Expected output shows `is healthy` for the endpoint.

      ```
      # etcdctl endpoint health
      ```
4. Verify that all nodes are ready by entering the following command. The expected output shows the `Ready` status beside each node entry.

   ```
   $ oc get nodes
   ```
5. Verify that the cluster Operators are all available by entering the following command. Expected output lists each Operator and shows the available status as `True` beside each listed Operator.

   ```
   $ oc get ClusterOperators
   ```
6. Verify that the cluster version is correct by entering the following command:

   ```
   $ oc get ClusterVersion
   ```

   **Example output**

   ```
   NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
   version   OpenShift Container Platform.5    True        False         5h57m   Cluster version is OpenShift Container Platform.5
   ```

## [Chapter 11. Managing machines with the Cluster API](#managing-machines-with-the-cluster-api) Copy linkLink copied to clipboard!

### [11.1. About the Cluster API](#cluster-api-about) Copy linkLink copied to clipboard!

You can use the Cluster API to create and manage compute machine sets and compute machines in your OpenShift Container Platform cluster.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The Cluster API is an upstream project that is integrated into OpenShift Container Platform as a Technology Preview for Amazon Web Services (AWS), Google Cloud, Microsoft Azure, Red Hat OpenStack Platform (RHOSP), VMware vSphere, and bare-metal platforms.

#### [11.1.1. Cluster API overview](#cluster-api-overview_cluster-api-about) Copy linkLink copied to clipboard!

You can use the Cluster API to create and manage compute machine sets and compute machines in your OpenShift Container Platform cluster. You can use the Cluster API alongside or instead of managing machines with the Machine API.

For OpenShift Container Platform 4.22 clusters, you can use the Cluster API to perform node host provisioning management actions after the cluster installation finishes. This system enables an elastic, dynamic provisioning method on top of public or private cloud infrastructure.

With the Cluster API Technology Preview, you can create compute machines and compute machine sets on OpenShift Container Platform clusters for supported providers. You can also explore the features that are enabled by this implementation that might not be available with the Machine API.

##### [11.1.1.1. Cluster API benefits](#cluster-api-benefits_cluster-api-about) Copy linkLink copied to clipboard!

With the Cluster API, you can use Kubernetes tools for infrastructure management to perform advanced machine management and scaling.

By using the Cluster API, OpenShift Container Platform users and developers can gain the following advantages:

* The option to use upstream community Cluster API infrastructure providers that might not be supported by the Machine API.
* The opportunity to collaborate with third parties who maintain machine controllers for infrastructure providers.
* The ability to use the same set of Kubernetes tools for infrastructure management in OpenShift Container Platform.
* The ability to create compute machine sets by using the Cluster API that support features that are not available with the Machine API.

##### [11.1.1.2. Cluster API limitations](#capi-tech-preview-limitations_cluster-api-about) Copy linkLink copied to clipboard!

Using the Cluster API to manage machines is a Technology Preview feature and has specific limitations.

These limitiations are listed as follows:

* To use this feature, you must enable the `TechPreviewNoUpgrade` feature set.

  Important

  Enabling this feature set cannot be undone and prevents minor version updates.
* Only Amazon Web Services (AWS), Google Cloud, Microsoft Azure, Red Hat OpenStack Platform (RHOSP), VMware vSphere, and bare-metal clusters can use the Cluster API.
* You must manually create some of the primary resources that the Cluster API requires. For more information, see "Getting started with the Cluster API".
* You cannot use the Cluster API to manage control plane machines.
* Migration of existing compute machine sets created by the Machine API to Cluster API compute machine sets is not supported.
* Full feature parity with the Machine API is not available.
* For clusters that use the Cluster API, OpenShift CLI (`oc`) commands prioritize Cluster API objects over Machine API objects. This behavior impacts any `oc` command that acts upon any object that is represented in both the Cluster API and the Machine API.

  For more information and a workaround for this issue, see "Referencing the intended objects when using the CLI" in the troubleshooting content.

##### [11.1.1.3. The Cluster CAPI Operator](#capi-arch-operator_cluster-api-about) Copy linkLink copied to clipboard!

The OpenShift Container Platform integration of the upstream Cluster API is implemented and managed by the Cluster CAPI Operator.

The Cluster CAPI Operator and its operands are provisioned in the `openshift-cluster-api` namespace, in contrast to the Machine API, which uses the `openshift-machine-api` namespace.

The Cluster CAPI Operator is an OpenShift Container Platform Operator that maintains the lifecycle of Cluster API resources. This Operator is responsible for all administrative tasks related to deploying the Cluster API project within an OpenShift Container Platform cluster.

If a cluster is configured correctly to allow the use of the Cluster API, the Cluster CAPI Operator installs the Cluster API components on the cluster. For more information, see the "Cluster CAPI Operator" entry in the *Cluster Operators reference* content.

##### [11.1.1.4. Cluster API primary resources](#capi-arch-resources_cluster-api-about) Copy linkLink copied to clipboard!

The Cluster API consists of the following primary resources. For the Technology Preview of this feature, you must create some of these resources manually in the `openshift-cluster-api` namespace.

Cluster
:   A fundamental unit that represents a cluster that is managed by the Cluster API.

Infrastructure cluster
:   A provider-specific resource that defines properties that all of the compute machine sets in the cluster share, such as the region and subnets.

Machine template
:   A provider-specific template that defines the properties of the machines that a compute machine set creates.

Machine set
:   A group of machines.

    Compute machine sets are to machines as replica sets are to pods. To add machines or scale them down, change the `replicas` field on the compute machine set custom resource to meet your compute needs.

    With the Cluster API, a compute machine set references a `Cluster` object and a provider-specific machine template.

Machine
:   A fundamental unit that describes the host for a node.

    The Cluster API creates machines based on the configuration in the machine template.

### [11.2. Getting started with the Cluster API](#cluster-api-getting-started) Copy linkLink copied to clipboard!

The Machine API and Cluster API are distinct API groups that have similar resources. You can use these API groups to automate the management of infrastructure resources on your OpenShift Container Platform cluster.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

When you install a standard OpenShift Container Platform cluster that has three control plane nodes, three compute nodes, and uses the default configuration options, the installation program provisions the following infrastructure resources in the `openshift-machine-api` namespace

* One control plane machine set that manages three control plane machines.
* One or more compute machine sets that manage three compute machines.
* One machine health check that manages spot instances.

When you install a cluster that supports managing infrastructure resources with the Cluster API, the installation program provisions the following resources in the `openshift-cluster-api` namespace:

* One cluster resource.
* One provider-specific infrastructure cluster resource.

On clusters that support migrating Machine API resources to Cluster API resources, a two-way synchronization controller creates these primary resources automatically. For more information, see "Machine API to Cluster API resource migration".

#### [11.2.1. Creating the Cluster API primary resources](#creating-primary-resources_cluster-api-getting-started) Copy linkLink copied to clipboard!

For clusters that do not support migrating Machine API resources to Cluster API resources, you must manually create the following Cluster API resources in the `openshift-cluster-api` namespace:

* One or more machine templates that correspond to compute machine sets.
* One or more compute machine sets that manage three compute machines.

##### [11.2.1.1. Creating a Cluster API machine template](#capi-creating-machine-template_cluster-api-getting-started) Copy linkLink copied to clipboard!

You can create a provider-specific machine template resource by creating a YAML manifest file and applying it with the OpenShift CLI (`oc`).

**Prerequisites**

* You have deployed an OpenShift Container Platform cluster.
* You have enabled the use of the Cluster API.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Create a YAML file similar to the following example. This procedure uses `<machine_template_resource_file>.yaml` as an example file name.

   ```
   apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
   kind: <machine_template_kind>
   metadata:
     name: <template_name>
     namespace: openshift-cluster-api
   spec:
     template:
       spec:
   ```

   where:

   `kind`
   :   Specifies the machine template kind. This value must match the value for your platform.

   The following values are valid:

   Expand

   | Cluster infrastructure provider | Value |
   | --- | --- |
   | Amazon Web Services (AWS) | `AWSMachineTemplate` |
   | Google Cloud | `GCPMachineTemplate` |
   | Microsoft Azure | `AzureMachineTemplate` |
   | Red Hat OpenStack Platform (RHOSP) | `OpenStackMachineTemplate` |
   | VMware vSphere | `VSphereMachineTemplate` |
   | Bare metal | `Metal3MachineTemplate` |

   Show more

   `metadata.name`
   :   Specifies a name for the machine template.

   `spec.template.spec`
   :   Specifies the details for your environment. These parameters are provider specific. For more information, see the sample Cluster API machine template YAML for your provider.
2. Create the machine template CR by running the following command:

   ```
   $ oc create -f <machine_template_resource_file>.yaml
   ```

**Verification**

* Confirm that the machine template CR is created by running the following command:

  ```
  $ oc get <machine_template_kind> -n openshift-cluster-api
  ```

  Replace `<machine_template_kind>` with the value that corresponds to your platform.

  **Example output**

  ```
  NAME              AGE
  <template_name>   77m
  ```

##### [11.2.1.2. Creating a Cluster API compute machine set](#capi-creating-machine-set_cluster-api-getting-started) Copy linkLink copied to clipboard!

You can create compute machine sets that use the Cluster API to dynamically manage the machine compute resources for specific workloads of your choice.

**Prerequisites**

* You have deployed an OpenShift Container Platform cluster.
* You have enabled the use of the Cluster API.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).
* You have created the machine template resource.

**Procedure**

1. Create a YAML file similar to the following. This procedure uses `<machine_set_resource_file>.yaml` as an example file name.

   ```
   apiVersion: cluster.x-k8s.io/v1beta1
   kind: MachineSet
   metadata:
     name: <machine_set_name>
     namespace: openshift-cluster-api
   spec:
     clusterName: <cluster_name>
     replicas: 1
     selector:
       matchLabels:
         test: example
     template:
       metadata:
         labels:
           test: example
       spec:
   # ...
   ```

   where:

   `metadata.name`
   :   Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.

   `spec.clusterName`
   :   Specifies the name of the cluster. Obtain the value of the cluster ID by running the following command:

   ```
   $  oc get infrastructure cluster \
      -o jsonpath='{.status.infrastructureName}'
   ```

   `spec.template.spec`
   :   Specifies the details for your environment. These parameters are provider specific. For more information, see the sample Cluster API compute machine set YAML for your provider.
2. Create the compute machine set CR by running the following command:

   ```
   $ oc create -f <machine_set_resource_file>.yaml
   ```
3. Confirm that the compute machine set CR is created by running the following command:

   ```
   $ oc get machineset.cluster.x-k8s.io -n openshift-cluster-api
   ```

   **Example output**

   ```
   NAME                 CLUSTER          REPLICAS   READY   AVAILABLE   AGE   VERSION
   <machine_set_name>   <cluster_name>   1          1       1           17m
   ```

   When the new compute machine set is available, the `REPLICAS` and `AVAILABLE` values match. If the compute machine set is not available, wait a few minutes and run the command again.

**Verification**

* To verify that the compute machine set is creating machines according to your required configuration, review the lists of machines and nodes in the cluster by running the following commands:

  + View the list of Cluster API machines:

    ```
    $ oc get machine.cluster.x-k8s.io -n openshift-cluster-api
    ```

    **Example output**

    ```
    NAME                             CLUSTER          NODENAME                                 PROVIDERID      PHASE     AGE     VERSION
    <machine_set_name>-<string_id>   <cluster_name>   <ip_address>.<region>.compute.internal   <provider_id>   Running   8m23s
    ```
  + View the list of nodes:

    ```
    $ oc get node
    ```

    **Example output**

    ```
    NAME                                       STATUS   ROLES    AGE     VERSION
    <ip_address_1>.<region>.compute.internal   Ready    worker   5h14m   v1.28.5
    <ip_address_2>.<region>.compute.internal   Ready    master   5h19m   v1.28.5
    <ip_address_3>.<region>.compute.internal   Ready    worker   7m      v1.28.5
    ```

#### [11.2.2. Machine API to Cluster API resource migration](#mapi-to-capi-migration-overview_cluster-api-getting-started) Copy linkLink copied to clipboard!

On clusters that support migrating Machine API resources to Cluster API resources, a two-way synchronization controller creates the Cluster API resources in the `openshift-cluster-api` namespace.

These Cluster API resources are listed as follows:

* One or more machine templates that correspond to compute machine sets.
* One or more compute machine sets that manage three compute machines.
* One or more Cluster API compute machines that correspond to each Machine API compute machine.

Note

The two-way synchronization controller only operates on clusters with the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set enabled.

These Cluster API resources correspond to the resources that the installation program provisions in the `openshift-machine-api` namespace for a cluster that uses the default configuration options. The Cluster API resources have the same names as their Machine API counterparts and appear in the output of commands, such as `oc get`, that list resources. The synchronization controller creates the Cluster API resources in an unprovisioned (`Paused`) state to prevent unintended reconciliation.

For supported configurations, you can migrate a Machine API resource to the equivalent Cluster API resource by changing which API it considers authoritative. When you migrate a Machine API resources to the Cluster API, you transfer management of the resource to the Cluster API.

By migrating a Machine API resource to use the Cluster API, you can verify that everything works as expected before deciding to use the Cluster API in production clusters. After migrating a Machine API resource to an equivalent Cluster API resource, you can examine the new resource to verify that the features and configuration match the original Machine API resource.

When you change the authoritative API for a compute machine set, any existing compute machines that the compute machine set manages retain their original authoritative API. As a result, a compute machine set that manages machines that use different authoritative APIs is a valid and expected occurrence in clusters that support migrating between these API types.

When you change the authoritative API for a compute machine, the instance on the underlying infrastructure that backs the machine is not recreated or reprovisioned. In-place changes, such as modifying labels, tags, taints, or annotations, are the only changes that the API group can make to the underlying instance that backs the machine.

Note

You can only migrate some resources on supported infrastructure types.

Expand

Table 11.1. Supported resource conversions

| Infrastructure | Compute machine | Compute machine set | Machine health check | Control plane machine set | Cluster autoscaler |
| --- | --- | --- | --- | --- | --- |
| AWS | Technology Preview | Technology Preview | Not Available | Not Available | Not Available |
| All other infrastructure types | Not Available | Not Available | Not Available | Not Available | Not Available |

Show more

##### [11.2.2.1. Authoritative API types of compute machines](#machine-set-authoritative-api-machines_cluster-api-getting-started) Copy linkLink copied to clipboard!

The values of the `.spec.authoritativeAPI` and `.spec.template.spec.authoritativeAPI` fields in a Machine API compute machine set determine the authoritative API of the compute machines.

Expand

Table 11.2. Interaction of authoritativeAPI fields when creating compute machines

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **`.spec.authoritativeAPI` value** | `ClusterAPI` | `ClusterAPI` | `MachineAPI` | `MachineAPI` |
| **`.spec.template.spec.authoritativeAPI` value** | `ClusterAPI` | `MachineAPI` | `MachineAPI` | `ClusterAPI` |
| **`authoritativeAPI` value for new compute machines** | `ClusterAPI` | `ClusterAPI` | `MachineAPI` | `ClusterAPI` |

Show more

Note

When the `.spec.authoritativeAPI` value is `ClusterAPI`, the Machine API machine set is not authoritative and the `.spec.template.spec.authoritativeAPI` value is not used. As a result, the only combination that creates a compute machine with the Machine API as authoritative is where the `.spec.authoritativeAPI` and `.spec.template.spec.authoritativeAPI` values are `MachineAPI`.

##### [11.2.2.2. Migrating a Machine API resource to use the Cluster API](#migrating-between-capi-mapi_cluster-api-getting-started) Copy linkLink copied to clipboard!

You can migrate individual Machine API objects to equivalent Cluster API objects.

Important

Migrating a Machine API resource to use the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Prerequisites**

* You have deployed an OpenShift Container Platform cluster on a supported infrastructure type.
* You have enabled the use of the Cluster API.
* You have enabled the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Identify the Machine API resource that you want to migrate to a Cluster API resource by running the following command:

   ```
   $ oc get <resource_kind> -n openshift-machine-api
   ```

   where `<resource_kind>` is one of the following values:

   `machine.machine.openshift.io`
   :   The fully qualified name of the resource kind for a compute or control plane machine.

   `machineset.machine.openshift.io`
   :   The fully qualified name of the resource kind for a compute machine set.
2. Edit the resource specification by running the following command:

   ```
   $ oc edit <resource_kind>/<resource_name> -n openshift-machine-api
   ```

   where:

   `<resource_kind>`
   :   Specifies a compute machine with `machine.machine.openshift.io` or compute machine set with `machineset.machine.openshift.io`.

   `<resource_name>`
   :   Specifies the name of the Machine API resource that you want to migrate to a Cluster API resource.
3. In the resource specification, update the value of the `spec.authoritativeAPI` field:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: <resource_kind>
   metadata:
     name: <resource_name>
     [...]
   spec:
     authoritativeAPI: ClusterAPI
     [...]
   status:
     authoritativeAPI: MachineAPI
     [...]
   ```

   where:

   `kind`
   :   Specifies the resource kind of the resource that you want to migrate. For example, the resource kind for a compute machine set is `MachineSet` and the resource kind for a compute machine is `Machine`.

   `metadata.name`
   :   Specifies the name of the resource that you want to migrate.

   `spec.authoritativeAPI`
   :   Specifies the authoritative API that you want this resource to use. For example, to start migrating a Machine API resource to the Cluster API, specify `ClusterAPI`.

   `status.authoritativeAPI`
   :   Specifies the value for the current authoritative API. This value indicates which API currently manages this resource. Do not change the value in this part of the specification.

   Important

   Do not change other values when you update the value of the `spec.authoritativeAPI` field. Because other controllers might process updates to other values before the synchronization controller processes the `spec.authoritativeAPI` field update, changing other values can cause unexpected behavior.

   For more information, see "Unexpected behavior when changing resource configurations".

**Verification**

* Check the status of the conversion by running the following command:

  ```
  $ oc -n openshift-machine-api get <resource_kind>/<resource_name> -o json | jq .status.authoritativeAPI
  ```

  where:

  `<resource_kind>`
  :   Specifies a compute machine with `machine.machine.openshift.io` or compute machine set with `machineset.machine.openshift.io`.

  `<resource_name>`
  :   Specifies the name of the Machine API resource that you want to migrate to a Cluster API resource.

  + While the conversion progresses, this command returns a value of `Migrating`. If this value persists for a long time, check the logs for the `cluster-capi-operator` deployment in the `openshift-cluster-api` namespace for more information and to identify potential issues.
  + When the conversion is complete, this command returns a value of `ClusterAPI`.

##### [11.2.2.3. Deploying Cluster API compute machines by using a Machine API compute machine set](#deploying-capi-machines-via-mapi-machine-sets_cluster-api-getting-started) Copy linkLink copied to clipboard!

You can configure a Machine API compute machine set to deploy Cluster API compute machines. With this process, you can test the Cluster API compute machine creation workflow without creating and scaling a Cluster API compute machine set.

A Machine API compute machine set with this configuration creates nonauthoritative Machine API compute machines that use the Cluster API as authoritative. The two-way synchronization controller then creates corresponding authoritative Cluster API machines that provision on the underlying infrastructure.

Important

Deploying Cluster API compute machines by using a Machine API compute machine set is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Prerequisites**

* You have deployed an OpenShift Container Platform cluster on a supported infrastructure type.
* You have enabled the use of the Cluster API.
* You have enabled the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. List the Machine API compute machine sets in your cluster by running the following command:

   ```
   $ oc get machineset.machine.openshift.io -n openshift-machine-api
   ```
2. Edit the resource specification by running the following command:

   ```
   $ oc edit machineset.machine.openshift.io <machine_set_name> \
     -n openshift-machine-api
   ```

   Replace `<machine_set_name>` with the name of the Machine API compute machine set that you want to configure to deploy Cluster API compute machines.
3. In the resource specification, update the value of the `spec.template.spec.authoritativeAPI` field:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   metadata:
     [...]
     name: <machine_set_name>
     [...]
   spec:
     authoritativeAPI: MachineAPI
     [...]
     template:
       [...]
       spec:
         authoritativeAPI: ClusterAPI
   status:
     authoritativeAPI: MachineAPI
     [...]
   ```

   where:

   `spec.authoritativeAPI`
   :   Specifies the unconverted value for the Machine API compute machine set. Do not change the value in this part of the specification.

   `spec.template.spec.authoritativeAPI`
   :   Specifies the authoritative API for the machine set. To configure the compute machine set to deploy Cluster API compute machines, set this value to `ClusterAPI`.

   `status.authoritativeAPI`
   :   Specifies the current value for the Machine API compute machine set. Do not change the value in this part of the specification.

**Verification**

1. List the machines that are managed by the updated compute machine set by running the following command:

   ```
   $ oc get machines.machine.openshift.io \
     -n openshift-machine-api \
     -l machine.openshift.io/cluster-api-machineset=<machine_set_name>
   ```
2. To verify that a machine created by the updated machine set has the correct configuration, examine the `status.authoritativeAPI` field in the CR for one of the new machines by running the following command:

   ```
   $ oc describe machines.machine.openshift.io <machine_name> \
     -n openshift-machine-api
   ```

   For a Cluster API compute machine, the value of the field is `ClusterAPI`.

### [11.3. Managing machines with the Cluster API](#cluster-api-managing-machines) Copy linkLink copied to clipboard!

You can manage machines with the Cluster API by modifying a Cluster API machine template or a compute machine set by using the CLI.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

#### [11.3.1. Modifying a Cluster API machine template](#capi-modifying-machine-template_cluster-api-managing-machines) Copy linkLink copied to clipboard!

You can update the machine template resource for your cluster by modifying the YAML manifest file and applying it with the OpenShift CLI (`oc`).

**Prerequisites**

* You have deployed an OpenShift Container Platform cluster that uses the Cluster API.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. List the machine template resource for your cluster by running the following command:

   ```
   $ oc get <machine_template_kind>
   ```

   Replace `<machine_template_kind>` with the value that corresponds to your platform. The following values are valid:

   Expand

   | Cluster infrastructure provider | Value |
   | --- | --- |
   | Amazon Web Services | `AWSMachineTemplate` |
   | Google Cloud | `GCPMachineTemplate` |
   | Microsoft Azure | `AzureMachineTemplate` |
   | RHOSP | `OpenStackMachineTemplate` |
   | VMware vSphere | `VSphereMachineTemplate` |
   | Bare metal | `Metal3MachineTemplate` |

   Show more

   **Example output**

   ```
   NAME              AGE
   <template_name>   77m
   ```
2. Write the machine template resource for your cluster to a file that you can edit by running the following command:

   ```
   $ oc get <machine_template_kind> <template_name> -o yaml > <template_name>.yaml
   ```

   Replace `<template_name>` with the name of the machine template resource for your cluster.
3. Make a copy of the `<template_name>.yaml` file with a different name. This procedure uses `<modified_template_name>.yaml` as an example file name.
4. Use a text editor to make changes to the `<modified_template_name>.yaml` file that defines the updated machine template resource for your cluster. When editing the machine template resource, observe the following:

   * The parameters in the `spec` stanza are provider specific. For more information, see the sample Cluster API machine template YAML for your provider.
   * You must use a value for the `metadata.name` parameter that differs from any existing values.

     Important

     For any Cluster API compute machine sets that reference this template, you must update the `spec.template.spec.infrastructureRef.name` parameter to match the `metadata.name` value in the new machine template resource.
5. Apply the machine template CR by running the following command:

   ```
   $ oc apply -f <modified_template_name>.yaml
   ```

   For `<modified_template_name>`, use the edited YAML file with a new name.

**Next steps**

* For any Cluster API compute machine sets that reference this template, update the `spec.template.spec.infrastructureRef.name` parameter to match the `metadata.name` value in the new machine template resource. For more information, see "Modifying a compute machine set by using the CLI."

#### [11.3.2. Modifying a compute machine set by using the CLI](#machineset-modifying_cluster-api-managing-machines) Copy linkLink copied to clipboard!

To enable features or change the properties of machines, you can modify the configuration of a compute machine set using the CLI. You can then propagate the changes to the machines in your cluster.

When you modify a compute machine set, your changes only apply to compute machines that are created after you save the updated `MachineSet` custom resource (CR). The changes do not affect existing machines.

Note

Changes made in the underlying cloud provider are not reflected in the `Machine` or `MachineSet` CRs. To adjust instance configuration in cluster-managed infrastructure, use the cluster-side resources.

You can replace the existing machines with new ones that reflect the updated configuration by scaling the compute machine set to create twice the number of replicas and then scaling it down to the original number of replicas.

If you need to scale a compute machine set without making other changes, you do not need to delete the machines.

Note

By default, the OpenShift Container Platform router pods are deployed on compute machines. Because the router is required to access some cluster resources, including the web console, do not scale the compute machine set to `0` unless you first relocate the router pods.

The output examples in this procedure use the values for an AWS cluster.

**Prerequisites**

* Your OpenShift Container Platform cluster uses the Cluster API.
* You are logged in to the cluster as an administrator by using the OpenShift CLI (`oc`).

**Procedure**

1. List the compute machine sets in your cluster by running the following command:

   ```
   $ oc get machinesets.cluster.x-k8s.io -n openshift-cluster-api
   ```

   **Example output**

   ```
   NAME                          CLUSTER             REPLICAS   READY   AVAILABLE   AGE   VERSION
   <compute_machine_set_name_1>  <cluster_name>      1          1       1           26m
   <compute_machine_set_name_2>  <cluster_name>      1          1       1           26m
   ```
2. Edit a compute machine set by running the following command:

   ```
   $ oc edit machinesets.cluster.x-k8s.io <machine_set_name> \
     -n openshift-cluster-api
   ```
3. Note the value of the `spec.replicas` field, because you need it when scaling the machine set to apply the changes.

   ```
   apiVersion: cluster.x-k8s.io/v1beta1
   kind: MachineSet
   metadata:
     name: <machine_set_name>
     namespace: openshift-cluster-api
   spec:
     replicas: 2
   # ...
   ```

   The examples in this procedure show a compute machine set that has a `replicas` value of `2`.
4. Update the compute machine set CR with the configuration options that you want and save your changes.
5. List the machines that are managed by the updated compute machine set by running the following command:

   ```
   $ oc get machines.cluster.x-k8s.io \
     -n openshift-cluster-api \
     -l cluster.x-k8s.io/set-name=<machine_set_name>
   ```

   **Example output for an AWS cluster**

   ```
   NAME                        CLUSTER          NODENAME                                    PROVIDERID                              PHASE           AGE     VERSION
   <machine_name_original_1>   <cluster_name>   <original_1_ip>.<region>.compute.internal   aws:///us-east-2a/i-04e7b2cbd61fd2075   Running         4h
   <machine_name_original_2>   <cluster_name>   <original_2_ip>.<region>.compute.internal   aws:///us-east-2a/i-04e7b2cbd61fd2075   Running         4h
   ```
6. For each machine that is managed by the updated compute machine set, set the `delete` annotation by running the following command:

   ```
   $ oc annotate machines.cluster.x-k8s.io/<machine_name_original_1> \
     -n openshift-cluster-api \
     cluster.x-k8s.io/delete-machine="true"
   ```
7. To create replacement machines with the new configuration, scale the compute machine set to twice the number of replicas by running the following command:

   ```
   $ oc scale --replicas=4 \
     machinesets.cluster.x-k8s.io <machine_set_name> \
     -n openshift-cluster-api
   ```

   The original example value of `2` is doubled to `4`.
8. List the machines that are managed by the updated compute machine set by running the following command:

   ```
   $ oc get machines.cluster.x-k8s.io \
     -n openshift-cluster-api \
     -l cluster.x-k8s.io/set-name=<machine_set_name>
   ```

   **Example output for an AWS cluster**

   ```
   NAME                        CLUSTER          NODENAME                                    PROVIDERID                              PHASE           AGE     VERSION
   <machine_name_original_1>   <cluster_name>   <original_1_ip>.<region>.compute.internal   aws:///us-east-2a/i-04e7b2cbd61fd2075   Running         4h
   <machine_name_original_2>   <cluster_name>   <original_2_ip>.<region>.compute.internal   aws:///us-east-2a/i-04e7b2cbd61fd2075   Running         4h
   <machine_name_updated_1>    <cluster_name>   <updated_1_ip>.<region>.compute.internal    aws:///us-east-2a/i-04e7b2cbd61fd2075   Provisioned     55s
   <machine_name_updated_2>    <cluster_name>   <updated_2_ip>.<region>.compute.internal    aws:///us-east-2a/i-04e7b2cbd61fd2075   Provisioning    55s
   ```

   When the new machines are in the `Running` phase, you can scale the compute machine set to the original number of replicas.
9. To remove the machines that were created with the old configuration, scale the compute machine set to the original number of replicas by running the following command:

   ```
   $ oc scale --replicas=2 \
     machinesets.cluster.x-k8s.io <machine_set_name> \
     -n openshift-cluster-api
   ```

   The `replicas` parameter is set to the original example value of `2`.

**Verification**

* To verify that a machine created by the updated machine set has the correct configuration, examine the relevant fields in the CR for one of the new machines by running the following command:

  ```
  $ oc describe machines.cluster.x-k8s.io <machine_name_updated_1> \
    -n openshift-cluster-api
  ```
* To verify that the compute machines without the updated configuration are deleted, list the machines that are managed by the updated compute machine set by running the following command:

  ```
  $ oc get machines.cluster.x-k8s.io \
    -n openshift-cluster-api \
    cluster.x-k8s.io/set-name=<machine_set_name>
  ```

  **Example output while deletion is in progress for an AWS cluster**

  ```
  NAME                        CLUSTER          NODENAME                                    PROVIDERID                              PHASE      AGE     VERSION
  <machine_name_original_1>   <cluster_name>   <original_1_ip>.<region>.compute.internal   aws:///us-east-2a/i-04e7b2cbd61fd2075   Running    18m
  <machine_name_original_2>   <cluster_name>   <original_2_ip>.<region>.compute.internal   aws:///us-east-2a/i-04e7b2cbd61fd2075   Running    18m
  <machine_name_updated_1>    <cluster_name>   <updated_1_ip>.<region>.compute.internal    aws:///us-east-2a/i-04e7b2cbd61fd2075   Running    18m
  <machine_name_updated_2>    <cluster_name>   <updated_2_ip>.<region>.compute.internal    aws:///us-east-2a/i-04e7b2cbd61fd2075   Running    18m
  ```

  **Example output when deletion is complete for an AWS cluster**

  ```
  NAME                        CLUSTER          NODENAME                                    PROVIDERID                              PHASE      AGE     VERSION
  <machine_name_updated_1>    <cluster_name>   <updated_1_ip>.<region>.compute.internal    aws:///us-east-2a/i-04e7b2cbd61fd2075   Running    18m
  <machine_name_updated_2>    <cluster_name>   <updated_2_ip>.<region>.compute.internal    aws:///us-east-2a/i-04e7b2cbd61fd2075   Running    18m
  ```

### [11.4. Configuration options for Cluster API machines](#configuration-options-for-cluster-api-machines) Copy linkLink copied to clipboard!

#### [11.4.1. Cluster API configuration options for Amazon Web Services](#cluster-api-config-options-aws) Copy linkLink copied to clipboard!

You can change the configuration of your Amazon Web Services (AWS) Cluster API machines by updating values in the Cluster API custom resource manifests.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The YAML file examples show configurations for an Amazon Web Services cluster.

You can enable features by updating values in the Cluster API custom resource manifests.

##### [11.4.1.1. Sample YAML for a Cluster API machine template resource on Amazon Web Services](#capi-yaml-machine-template-aws_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines.

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      iamInstanceProfile: # ...
      instanceType: m5.large
      ignition:
        storageType: UnencryptedUserData
        version: "3.4"
      ami:
        id: # ...
      subnet:
        filters:
        - name: tag:Name
          values:
          - # ...
      additionalSecurityGroups:
      - filters:
        - name: tag:Name
          values:
          - # ...
```

where:

`kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`metadata.name`
:   Specifies a name for the machine template.

`spec.template.spec`
:   Specifies the details for your environment. The values here are examples.

##### [11.4.1.2. Sample YAML for a Cluster API compute machine set resource on Amazon Web Services](#capi-yaml-machine-set-aws_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

The compute machine set resource defines additional properties of the machines that the resource creates. The compute machine set also references the cluster resource and machine template when creating machines.

```
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: AWSMachineTemplate
        name: <template_name>
```

where:

`metadata.name`
:   Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.

`metadata.labels.cluster.x-k8s.io/cluster-name`
:   Specifies the cluster ID as the name of the cluster.

`spec.clusterName`
:   Specifies the cluster ID as the name of the cluster.

`spec.template.spec.infrastructureRef.kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`spec.template.spec.infrastructureRef.name`
:   Specifies the machine template name.

##### [11.4.1.2.1. Elastic Fabric Adapter instances and placement group options](#machine-feature-aws-existing-placement-group_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

You can deploy compute machines on Elastic Fabric Adapter (EFA) instances within an existing AWS placement group.

EFA instances do not require placement groups, and you can use placement groups for purposes other than configuring an EFA. The following example uses an EFA and placement group together to demonstrate a configuration that can improve network performance for machines within the specified placement group.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

**Sample EFA instance and placement group configuration**

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceType: <supported_instance_type>
      networkInterfaceType: efa
      placementGroupName: <placement_group>
      placementGroupPartition: <placement_group_partition_number>
# ...
```

where:

`spec.template.spec.instanceType`
:   Specifies an instance type that supports EFAs. For more information, see "Supported instance types".

`spec.template.spec.networkInterfaceType`
:   Specifies the `efa` network interface type.

`spec.template.spec.placementGroupName`
:   Specifies the name of the existing AWS placement group to deploy machines in.

`spec.template.spec.placementGroupPartition`
:   Specifies the partition number of the existing AWS placement group where you want your machines deployed. Setting a value for the parameter is optional.

Note

Ensure that the rules and limitations for the type of placement group that you create are compatible with your intended use case. For more information, see "Placement groups for your Amazon EC2 instances".

##### [11.4.1.2.2. Amazon EC2 Instance Metadata Service configuration options](#machine-feature-aws-imds-options_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

You can restrict the version of the Amazon EC2 Instance Metadata Service (IMDS) that machines on Amazon Web Services (AWS) clusters use. Machines can require the use of IMDSv2, or allow the use of IMDSv1 in addition to IMDSv2.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

Important

Before creating machines that require IMDSv2, ensure that any workloads that interact with the IMDS support IMDSv2.

**Sample IMDS configuration**

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceMetadataOptions:
        httpEndpoint: enabled
        httpPutResponseHopLimit: 1
        httpTokens: optional
        instanceMetadataTags: disabled
# ...
```

where:

`spec.template.spec.instanceMetadataOptions.httpPutResponseHopLimit`
:   Specifies the number of network hops allowed for IMDSv2 calls. If no value is specified, this parameter is set to `1` by default.

`spec.template.spec.instanceMetadataOptions.httpTokens`
:   Specifies whether to require the use of IMDSv2. If no value is specified, this parameter is set to `optional` by default. The following values are valid:

    * `optional`: Allow the use of both IMDSv1 and IMDSv2.
    * `required`: Require IMDSv2.

Note

The Machine API does not support the `httpEndpoint`, `httpPutResponseHopLimit`, and `instanceMetadataTags` fields. If you migrate a Cluster API machine template that uses this feature to a Machine API compute machine set, any Machine API machines that it creates will not have these fields and the underlying instances will not use these settings. Any existing machines that the migrated machine set manages will retain these fields and the underlying instances will continue to use these settings.

Requiring the use of IMDSv2 might cause timeouts. For more information, including mitigation strategies, see "Instance metadata access considerations".

##### [11.4.1.2.3. Dedicated Instance configuration options](#machine-feature-aws-dedicated-instances_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

You can deploy machines that are backed by Dedicated Instances on Amazon Web Services (AWS) clusters.

Dedicated Instances run in a virtual private cloud (VPC) on hardware that is dedicated to a single customer. These Amazon EC2 instances are physically isolated at the host hardware level. The isolation of Dedicated Instances occurs even if the instances belong to different AWS accounts that are linked to a single payer account. However, other instances that are not dedicated can share hardware with Dedicated Instances if they belong to the same AWS account.

OpenShift Container Platform supports instances with public or dedicated tenancy.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

**Sample Dedicated Instances configuration**

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      tenancy: dedicated
# ...
```

The `tenancy` field specifies using instances with dedicated tenancy that run on single-tenant hardware. If you do not specify the `dedicated` value, instances with public tenancy that run on shared hardware are used by default.

##### [11.4.1.2.4. Place machines on Dedicated Hosts by using machine templates](#machine-feature-aws-dedicated-hosts_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

You can configure a machine template to place machines on Amazon Web Services (AWS) Dedicated Hosts. With dynamic host allocation, the Cluster API requests a Dedicated Host from AWS and applies the specified tags to the Dedicated Host.

Important

AWS Dedicated Host support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

**Procedure**

* Configure the following fields in your `AWSMachineTemplate` resource:

  ```
  apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
  kind: AWSMachineTemplate
  # ...
  spec:
    template:
      spec:
        tenancy: host
        hostAffinity: host
        dynamicHostAllocation:
          tags:
            <tag_name>: <tag_value>
  # ...
  ```

  where:

  `spec.template.spec.dynamicHostAllocation.tags`
  :   Optional parameter. Specifies tags to apply to the dynamically allocated Dedicated Host. If you specify tags, you must specify both a key and a value. For `<tag_name>`, specify the tag key, for example `Environment`. For `<tag_value>`, specify the tag value, for example `production`.

##### [11.4.1.2.5. Place machines on a specific Dedicated Host by using machine templates](#machine-feature-aws-dedicated-hosts-byo-template_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

You can configure a machine template to place machines on a specific Amazon Web Services (AWS) Dedicated Host by specifying the host ID.

Important

AWS Dedicated Host support is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

**Procedure**

* Configure the following fields in your `AWSMachineTemplate` resource:

  ```
  apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
  kind: AWSMachineTemplate
  # ...
  spec:
    template:
      spec:
        tenancy: host
        hostAffinity: host
        hostID: <dedicated_host_id>
  # ...
  ```

  where:

  `<dedicated_host_id>`
  :   Specifies the ID of the AWS Dedicated Host on which to place the machine, for example `h-0123456789abcdef0`.

##### [11.4.1.2.6. Non-guaranteed Spot Instances and hourly cost limits](#machine-feature-agnostic-nonguaranteed-instances_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

You can deploy machines as non-guaranteed Spot Instances on Amazon Web Services (AWS). Spot Instances use spare AWS EC2 capacity and are less expensive than On-Demand Instances. You can use Spot Instances for workloads that can tolerate interruptions, such as batch or stateless, horizontally scalable workloads.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

Important

AWS EC2 can reclaim the capacity for a Spot Instance at any time.

**Sample Spot Instance configuration**

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      spotMarketOptions:
        maxPrice: <price_per_hour>
# ...
```

where:

`spec.template.spec.spotMarketOptions`
:   Specifies the use of Spot Instances.

`spec.template.spec.spotMarketOptions.maxPrice`
:   Optional parameter. Specifies an hourly cost limit in US dollars for the Spot Instance. For example, setting the `<price_per_hour>` value to `2.50` limits the cost of the Spot Instance to USD 2.50 per hour. When this value is not set, the maximum price charges up to the On-Demand Instance price.

    Warning

    Setting a specific `maxPrice: <price_per_hour>` value might increase the frequency of interruptions compared to using the default On-Demand Instance price. Red Hat recommends to use the default On-Demand Instance price and to not set the maximum price for Spot Instances.

Interruptions can occur when using Spot Instances for the following reasons:

* The instance price exceeds your maximum price
* The demand for Spot Instances increases
* The supply of Spot Instances decreases

AWS gives a two-minute warning to the user when an interruption occurs. OpenShift Container Platform begins to remove the workloads from the affected instances when AWS issues the termination warning.

When AWS terminates an instance, a termination handler running on the Spot Instance node deletes the machine resource. To satisfy the compute machine set `replicas` quantity, the compute machine set creates a machine that requests a Spot Instance.

##### [11.4.1.2.7. Configuring storage throughput for gp3 drives](#machine-feature-aws-throughput-capi_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

You can improve performance for high traffic services by increasing the throughput of gp3 storage volumes in an AWS cluster. You can configure the storage throughput for the root volume, non root volumes, or both.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

**Prerequisites**

* You use gp3 storage volume(s).

**Procedure**

* On the machine template in which you want to configure throughput, add the `throughput` parameter:

  ```
  apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
  kind: AWSMachineTemplate
  # ...
  spec:
    template:
      spec:
        nonRootVolumes:
        - throughput: <throughput_value>
        rootVolume:
          throughput: <throughput_value>
  # ...
  ```

  where:

  `<throughput_value>`
  :   Specifies a value in MiB per second between 125 and 2,000. You can only edit this value on gp3 volumes. The default value is `125`.

##### [11.4.1.2.8. Capacity Reservation configuration options](#machine-feature-agnostic-capacity-reservation_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

OpenShift Container Platform version 4.22 and later supports Capacity Reservations on Amazon Web Services clusters, including On-Demand Capacity Reservations and Capacity Blocks for ML.

You can deploy machines on any available resources that match the parameters of a capacity request that you define. These parameters specify the instance type, region, and number of instances that you want to reserve. If your Capacity Reservation can accommodate the capacity request, the deployment succeeds.

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file. Then, configure a machine set YAML file to reference the machine template when it deploys machines.

**Sample Capacity Reservation configuration**

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      capacityReservationId: <capacity_reservation>
      capacityReservationPreference: <reservation_preference>
      marketType: <market_type>
# ...
```

where:

`spec.template.spec.capacityReservationId`
:   Specifies the ID of the Capacity Block for ML or On-Demand Capacity Reservation that you want to deploy machines on.

`spec.template.spec.capacityReservationPreference`
:   Specifies your preferred capacity reservation behavior. The following values are valid:

    `CapacityReservationsOnly`
    :   Use this option to require a matching capacity reservation. If no matching capacity reservation is available, the instance fails to launch.

    `Open`
    :   Use this option to allow using an open capacity reservation that matches the availability zone and instance type.

    `None`
    :   Use this option to prohibit using a capacity reservation. You might use this option to help keep capacity reservations available for workloads that you want to use them.

`spec.template.spec.marketType`
:   Specifies the market type to use. The following values are valid:

    `CapacityBlock`
    :   Use this market type with Capacity Blocks for ML.

    `OnDemand`
    :   Use this market type with On-Demand Capacity Reservations.

    `Spot`
    :   Use this market type with Spot Instances. This option is not compatible with Capacity Reservations.

    For more information, including limitations and suggested use cases for this offering, see On-Demand Capacity Reservations and Capacity Blocks for ML (AWS documentation).

##### [11.4.1.2.9. GPU-enabled machine options](#machine-feature-aws-add-nvidia-gpu-node_cluster-api-config-options-aws) Copy linkLink copied to clipboard!

You can deploy GPU-enabled compute machines on Amazon Web Services (AWS).

The following sample configuration uses an AWS G4dn instance type, which includes an NVIDIA Tesla T4 Tensor Core GPU, as an example.

For more information about supported instance types, see the following pages in the NVIDIA documentation:

* NVIDIA GPU Operator Community support matrix
* NVIDIA AI Enterprise support matrix

To deploy compute machines with your configuration, configure the appropriate values in a machine template YAML file and a machine set YAML file that references the machine template when it deploys machines.

**Sample GPU-enabled machine template configuration**

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta2
kind: AWSMachineTemplate
# ...
spec:
  template:
    spec:
      instanceType: g4dn.xlarge
# ...
```

* The `spec.template.spec.instanceType` field specifies a G4dn instance type.

**Sample GPU-enabled machine set configuration**

```
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <cluster_name>-gpu-<region>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <cluster_name>-gpu-<region>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <cluster_name>-gpu-<region>
        node-role.kubernetes.io/<role>: ""
# ...
```

where:

`metadate.name`
:   Specifies a name that includes the `gpu` role. The name includes the cluster ID as a prefix and the region as a suffix.

`spec.selector.matchLabels.cluster.x-k8s.io/set-name`
:   Specifies a selector label that matches the machine set name.

`spec.template.metadata.labels.cluster.x-k8s.io/set-name`
:   Specifies a template label that matches the machine set name.

#### [11.4.2. Cluster API configuration options for Google Cloud](#cluster-api-config-options-gcp) Copy linkLink copied to clipboard!

You can change the configuration of your Google Cloud Cluster API machines by updating values in the Cluster API custom resource manifests.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

##### [11.4.2.1. Sample YAML for configuring Google Cloud clusters](#cluster-api-sample-yaml-gcp_cluster-api-config-options-gcp) Copy linkLink copied to clipboard!

The following example YAML files show configurations for a Google Cloud cluster.

##### [11.4.2.1.1. Sample YAML for a Cluster API machine template resource on Google Cloud](#capi-yaml-machine-template-gcp_cluster-api-config-options-gcp) Copy linkLink copied to clipboard!

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines.

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: GCPMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      rootDeviceType: pd-ssd
      rootDeviceSize: 128
      instanceType: n1-standard-4
      image: projects/rhcos-cloud/global/images/rhcos-411-85-202203181601-0-gcp-x86-64
      subnet: <cluster_name>-worker-subnet
      serviceAccounts:
        email: <service_account_email_address>
        scopes:
          - https://www.googleapis.com/auth/cloud-platform
      additionalLabels:
        kubernetes-io-cluster-<cluster_name>: owned
      additionalNetworkTags:
        - <cluster_name>-worker
      ipForwarding: Disabled
```

where:

`kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`metadata.name`
:   Specifies a name for the machine template.

`spec.template.spec`
:   Specifies the details for your environment. The values here are examples.

##### [11.4.2.1.2. Sample YAML for a Cluster API compute machine set resource on Google Cloud](#capi-yaml-machine-set-gcp_cluster-api-config-options-gcp) Copy linkLink copied to clipboard!

The compute machine set resource defines additional properties of the machines that it creates. The compute machine set also references the cluster resource and machine template when creating machines.

```
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: GCPMachineTemplate
        name: <template_name>
      failureDomain: <failure_domain>
```

where:

`metadata.name`
:   Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.

`metadata.labels.cluster.x-k8s.io/cluster-name`
:   Specifies the cluster ID as the name of the cluster.

`spec.clusterName`
:   Specifies the cluster ID as the name of the cluster.

`spec.template.spec.infrastructureRef.kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`spec.template.spec.infrastructureRef.name`
:   Specifies the machine template name.

`spec.template.spec.failureDomain`
:   Specifies the failure domain within the Google Cloud region.

#### [11.4.3. Cluster API configuration options for Microsoft Azure](#cluster-api-config-options-azure) Copy linkLink copied to clipboard!

You can change the configuration of your Microsoft Azure Cluster API machines by updating values in the Cluster API custom resource manifests.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The following example YAML files show configurations for an Azure cluster.

##### [11.4.3.1. Sample YAML for a Cluster API machine template resource on Microsoft Azure](#capi-yaml-machine-template-azure_cluster-api-config-options-azure) Copy linkLink copied to clipboard!

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines.

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: AzureMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      disableExtensionOperations: true
      identity: UserAssigned
      image:
        id: /subscriptions/<subscription_id>/resourceGroups/<cluster_name>-rg/providers/Microsoft.Compute/galleries/gallery_<compliant_cluster_name>/images/<cluster_name>-gen2/versions/latest
      networkInterfaces:
        - acceleratedNetworking: true
          privateIPConfigs: 1
          subnetName: <cluster_name>-worker-subnet
      osDisk:
        diskSizeGB: 128
        managedDisk:
          storageAccountType: Premium_LRS
        osType: Linux
      sshPublicKey: <ssh_key_value>
      userAssignedIdentities:
        - providerID: 'azure:///subscriptions/<subscription_id>/resourcegroups/<cluster_name>-rg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/<cluster_name>-identity'
      vmSize: Standard_D4s_v3
```

where:

`kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`metadata.name`
:   Specifies a name for the machine template.

`spec.template.spec`
:   Specifies the details for your environment. The values here are examples.

`spec.template.spec.image.id`
:   Specifies an image that is compatible with your instance type. The Hyper-V generation V2 images created by the installation program have a `-gen2` suffix, while V1 images have the same name without the suffix.

Note

Default OpenShift Container Platform cluster names contain hyphens (`-`), which are not compatible with Azure gallery name requirements. The value of `<compliant_cluster_name>` in this configuration must use underscores (`_`) instead of hyphens to comply with these requirements. Other instances of `<cluster_name>` do not change.

For example, a cluster name of `jdoe-test-2m2np` transforms to `jdoe_test_2m2np`. The full string for `gallery_<compliant_cluster_name>` in this example is `gallery_jdoe_test_2m2np`, not `gallery_jdoe-test-2m2np`. The complete value of `spec.template.spec.image.id` for this example value is `/subscriptions/<subscription_id>/resourceGroups/jdoe-test-2m2np-rg/providers/Microsoft.Compute/galleries/gallery_jdoe_test_2m2np/images/jdoe-test-2m2np-gen2/versions/latest`.

##### [11.4.3.2. Sample YAML for a Cluster API compute machine set resource on Microsoft Azure](#capi-yaml-machine-set-azure_cluster-api-config-options-azure) Copy linkLink copied to clipboard!

The compute machine set resource defines additional properties of the machines that it creates. The compute machine set also references the cluster resource and machine template when creating machines.

```
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
        dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: AzureMachineTemplate
        name: <template_name>
```

where:

`metadata.name`
:   Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.

`metadata.labels.cluster.x-k8s.io/cluster-name`
:   Specifies the cluster ID as the name of the cluster.

`spec.template.spec.infrastructureRef.kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`spec.template.spec.infrastructureRef.name`
:   Specifies the machine template name.

#### [11.4.4. Cluster API configuration options for Red Hat OpenStack Platform](#cluster-api-config-options-rhosp) Copy linkLink copied to clipboard!

You can change the configuration of your Red Hat OpenStack Platform (RHOSP) Cluster API machines by updating values in the Cluster API custom resource manifests.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

##### [11.4.4.1. Sample YAML for configuring RHOSP clusters](#cluster-api-sample-yaml-rhosp_cluster-api-config-options-rhosp) Copy linkLink copied to clipboard!

The following example YAML files show configurations for a RHOSP cluster.

##### [11.4.4.1.1. Sample YAML for a Cluster API machine template resource on RHOSP](#capi-yaml-machine-template-rhosp_cluster-api-config-options-rhosp) Copy linkLink copied to clipboard!

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines.

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: OpenStackMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      flavor: <openstack_node_machine_flavor>
      image:
        filter:
          name: <openstack_image>
```

where:

`kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`metadata.name`
:   Specifies a name for the machine template.

`spec.template.spec`
:   Specifies the details for your environment. The values here are examples.

`spec.template.spec.flavor`
:   Specifies the RHOSP flavor to use. For more information, see "Creating flavors for launching instances".

`spec.template.spec.image.filter.name`
:   Specifies the image to use.

##### [11.4.4.1.2. Sample YAML for a Cluster API compute machine set resource on RHOSP](#capi-yaml-machine-set-rhosp_cluster-api-config-options-rhosp) Copy linkLink copied to clipboard!

The compute machine set resource defines additional properties of the machines that the resource creates. The compute machine set also references the infrastructure resource and machine template when creating machines.

```
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: OpenStackMachineTemplate
        name: <template_name>
      failureDomain: <nova_availability_zone>
```

where:

`metadata.name`
:   Specifies a name for the compute machine set.

`spec.clusterName`
:   Specifies the cluster ID as the name of the cluster.

`spec.template.spec.bootstrap.dataSecretName`
:   For the Cluster API Technology Preview, the Operator can use the worker user data secret from the `openshift-machine-api` namespace.

`spec.template.spec.infrastructureRef.kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`spec.template.spec.infrastructureRef.name`
:   Specifies the machine template name.

`spec.template.spec.failureDomain`
:   Optional parameter. Specifies the name of the Nova availability zone for the machine set to create machines in. If you do not specify a value, machines are not restricted to a specific availability zone.

#### [11.4.5. Cluster API configuration options for VMware vSphere](#cluster-api-config-options-vsphere) Copy linkLink copied to clipboard!

You can change the configuration of your VMware vSphere Cluster API machines by updating values in the Cluster API custom resource manifests.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

##### [11.4.5.1. Sample YAML for configuring VMware vSphere clusters](#cluster-api-sample-yaml-vsphere_cluster-api-config-options-vsphere) Copy linkLink copied to clipboard!

The following example YAML files show configurations for a VMware vSphere cluster.

##### [11.4.5.1.1. Sample YAML for a Cluster API machine template resource on VMware vSphere](#capi-yaml-machine-template-vsphere_cluster-api-config-options-vsphere) Copy linkLink copied to clipboard!

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines.

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: VSphereMachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      template: <vm_template_name>
      server: <vcenter_server_ip>
      diskGiB: 128
      cloneMode: linkedClone
      datacenter: <vcenter_data_center_name>
      datastore: <vcenter_datastore_name>
      folder: <vcenter_vm_folder_path>
      resourcePool: <vsphere_resource_pool>
      numCPUs: 4
      memoryMiB: 16384
      network:
        devices:
        - dhcp4: true
          networkName: "<vm_network_name>"
```

where:

`kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`metadata.name`
:   Specifies a name for the machine template.

`spec.template.spec`
:   Specifies the details for your environment. The values here are examples.

`spec.template.spec.template`
:   Specifies the vSphere VM template to use, such as `user-5ddjd-rhcos`.

`spec.template.spec.server`
:   Specifies the vCenter server IP or fully qualified domain name.

`spec.template.spec.cloneMode`
:   Specifies the type of VM clone to use. The following values are valid:

    * `fullClone`
    * `linkedClone`

    When using the `linkedClone` type, the disk size matches the clone source instead of using the `diskGiB` value. For more information, see the vSphere documentation about VM clone types.

`spec.template.spec.datacenter`
:   Specifies the vCenter data center to deploy the compute machine set on.

`spec.template.spec.datastore`
:   Specifies the vCenter datastore to deploy the compute machine set on.

`spec.template.spec.folder`
:   Specifies the path to the vSphere VM folder in vCenter, such as `/dc1/vm/user-inst-5ddjd`.

`spec.template.spec.resourcePool`
:   Specifies the vSphere resource pool for your VMs.

`spec.template.spec.network.devices.networkName`
:   Specifies the vSphere VM network to deploy the compute machine set to. This VM network must be where other compute machines reside in the cluster.

##### [11.4.5.1.2. Sample YAML for a Cluster API compute machine set resource on VMware vSphere](#capi-yaml-machine-set-vsphere_cluster-api-config-options-vsphere) Copy linkLink copied to clipboard!

The compute machine set resource defines additional properties of the machines that the resource creates. The compute machine set also references the cluster resource and machine template when creating machines.

```
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/<role>: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: VSphereMachineTemplate
        name: <template_name>
      failureDomain:
        - name: <failure_domain_name>
          region: <region_a>
          zone: <zone_a>
          server: <vcenter_server_name>
          topology:
            datacenter: <region_a_data_center>
            computeCluster: "</region_a_data_center/host/zone_a_cluster>"
            resourcePool: "</region_a_data_center/host/zone_a_cluster/Resources/resource_pool>"
            datastore: "</region_a_data_center/datastore/datastore_a>"
            networks:
            - port-group
```

where:

`metadata.name`
:   Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.

`metadata.labels.cluster.x-k8s.io/cluster-name`
:   Specifies the cluster ID as the name of the cluster.

`spec.clusterName`
:   Specifies the cluster ID as the name of the cluster.

`spec.template.spec.infrastructureRef.kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`spec.template.spec.infrastructureRef.name`
:   Specifies the machine template name.

`spec.template.spec.failureDomain`
:   Specifies the failure domain configuration details.

Note

Using multiple regions and zones on a vSphere cluster that uses the Cluster API is not a validated configuration.

#### [11.4.6. Cluster API configuration options for bare metal](#cluster-api-config-options-bare-metal) Copy linkLink copied to clipboard!

You can change the configuration of your bare metal Cluster API machines by updating values in the Cluster API custom resource manifests.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

##### [11.4.6.1. Sample YAML for configuring bare metal clusters](#cluster-api-sample-yaml-bare-metal_cluster-api-config-options-bare-metal) Copy linkLink copied to clipboard!

The following example YAML files show configurations for a bare metal cluster.

##### [11.4.6.1.1. Sample YAML for a Cluster API machine template resource on bare metal](#capi-yaml-machine-template-bare-metal_cluster-api-config-options-bare-metal) Copy linkLink copied to clipboard!

The machine template resource is provider-specific and defines the basic properties of the machines that a compute machine set creates. The compute machine set references this template when creating machines.

```
apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
kind: Metal3MachineTemplate
metadata:
  name: <template_name>
  namespace: openshift-cluster-api
spec:
  template:
    spec:
      customDeploy: install_coreos
      userData:
        name: worker-user-data-managed
```

where:

`kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`metadata.name`
:   Specifies a name for the machine template.

`spec.template.spec`
:   Specifies the details for your environment. The values here are examples.

`spec.template.spec.userData.name`
:   Specifies the Ignition configuration, which the Machine API Operator generates during installation. You must apply the `openshift-cluster-api` namespace to ensure the cluster can access the secret by running the following command:

```
$ oc get secret worker-user-data-managed \
  -n openshift-machine-api -o yaml | \
  sed 's/namespace: .*/namespace: openshift-cluster-api/' | oc apply -f -
```

##### [11.4.6.1.2. Sample YAML for a Cluster API compute machine set resource on bare metal](#capi-yaml-machine-set-bare-metal_cluster-api-config-options-bare-metal) Copy linkLink copied to clipboard!

The compute machine set resource defines additional properties of the machines that it creates. The compute machine set also references the cluster resource and machine template when creating machines.

```
apiVersion: cluster.x-k8s.io/v1beta1
kind: MachineSet
metadata:
  name: <machine_set_name>
  namespace: openshift-cluster-api
  labels:
    cluster.x-k8s.io/cluster-name: <cluster_name>
spec:
  clusterName: <cluster_name>
  replicas: 1
  selector:
    matchLabels:
      test: example
      cluster.x-k8s.io/cluster-name: <cluster_name>
      cluster.x-k8s.io/set-name: <machine_set_name>
  template:
    metadata:
      labels:
        test: example
        cluster.x-k8s.io/cluster-name: <cluster_name>
        cluster.x-k8s.io/set-name: <machine_set_name>
        node-role.kubernetes.io/worker: ""
    spec:
      bootstrap:
         dataSecretName: worker-user-data-managed
      clusterName: <cluster_name>
      infrastructureRef:
        apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
        kind: Metal3MachineTemplate
        name: <template_name>
```

where:

`metadata.name`
:   Specifies a name for the compute machine set. The cluster ID, machine role, and region form a typical pattern for this value in the following format: `<cluster_name>-<role>-<region>`.

`metadata.labels.cluster.x-k8s.io/cluster-name`
:   Specifies the cluster ID as the name of the cluster.

`spec.template.spec.infrastructureRef.kind`
:   Specifies the machine template kind. This value must match the value for your platform.

`spec.template.spec.infrastructureRef.name`
:   Specifies the machine template name.

### [11.5. Troubleshooting clusters that use the Cluster API](#cluster-api-troubleshooting) Copy linkLink copied to clipboard!

To help avoid or recover from issues in a cluster that supports migrating resources to use a different authoritative API, you can learn how to recognize these issues. Generally, troubleshooting steps for problems with the Cluster API are similar to those steps for problems with the Machine API.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

The Cluster CAPI Operator and its operands are provisioned in the `openshift-cluster-api` namespace, whereas the Machine API uses the `openshift-machine-api` namespace. When using `oc` commands that reference a namespace, be sure to reference the correct one.

#### [11.5.1. Referencing the intended objects when using the CLI](#ts-capi-cli-reference-intended-objects_cluster-api-troubleshooting) Copy linkLink copied to clipboard!

For clusters that use the Cluster API, OpenShift CLI (`oc`) commands prioritize Cluster API objects over Machine API objects.

This behavior impacts any `oc` command that acts upon any object that is represented in both the Cluster API and the Machine API. This explanation uses the `oc delete machine` command, which deletes a machine, as an example.

Cause
:   When you run an `oc` command, `oc` communicates with the Kube API server to determine which objects to act upon. The Kube API server uses the first installed custom resource definition (CRD) it encounters alphabetically when an `oc` command is run.

    CRDs for Cluster API objects are in the `cluster.x-k8s.io` group, while CRDs for Machine API objects are in the `machine.openshift.io` group. Because the letter `c` precedes the letter `m` alphabetically, the Kube API server matches on the Cluster API object CRD. As a result, the `oc` command acts upon Cluster API objects.

Consequence
:   Because of this behavior, the following unintended outcomes can occur on a cluster that uses the Cluster API:

    * For namespaces that contain both types of objects, commands such as `oc get machine` return only Cluster API objects.
    * For namespaces that contain only Machine API objects, commands such as `oc get machine` return no results.

Workaround
:   You can ensure that `oc` commands act on the type of objects you intend by using the corresponding fully qualified name.

**Prerequisites**

* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

* To delete a Machine API machine, use the fully qualified name `machine.machine.openshift.io` when running the `oc delete machine` command:

  ```
  $ oc delete machine.machine.openshift.io <machine_name>
  ```
* To delete a Cluster API machine, use the fully qualified name `machine.cluster.x-k8s.io` when running the `oc delete machine` command:

  ```
  $ oc delete machine.cluster.x-k8s.io <machine_name>
  ```

#### [11.5.2. Duplicated machine set and machine resources](#ts-capi-sync-list-duplicate-resources_cluster-api-troubleshooting) Copy linkLink copied to clipboard!

On clusters that support migrating Machine API resources to Cluster API resources, some resources seem to have duplicate instances in the output of OpenShift CLI (`oc`) commands that list resources and in the OpenShift Container Platform web console.

Cause
:   When you install an OpenShift Container Platform cluster that uses the default configuration options, the installation program provisions the following infrastructure resources in the `openshift-machine-api` namespace:

    * One control plane machine set that manages three control plane machines.
    * One or more compute machine sets that manage three compute machines.
    * One machine health check that manages spot instances.
    * Compute machines that are created according to the compute machine set specifications.

    On clusters that support migrating Machine API resources to Cluster API resources, a two-way synchronization controller creates the following Cluster API resources in the `openshift-cluster-api` namespace:

    * One cluster resource.
    * One provider-specific infrastructure cluster resource.
    * One or more machine templates that correspond to compute machine sets.
    * One or more compute machine sets that manage three compute machines.
    * Compute machines that are created according to the machine template and compute machine set specifications.
    * Infrastructure machines that correspond to compute machines.

    These Cluster API resources have the same names as their counterparts in the `openshift-machine-api` namespace.

Consequence
:   Because of this behavior, instances of machine set and machine resources that seem to be duplicates appear in the output of `oc` commands that list resources and in the OpenShift Container Platform web console.

Workaround
:   Although the resources have the same names as their counterparts in the other namespace, only the resources that use the current authoritative API are active. The synchronization controller creates and maintains the corresponding resources that do not use the current authoritative API in an unprovisioned (`Paused`) state to prevent unintended reconciliation.

Result
:   Only one of each resource that seems to be a duplicate is active at a time. The inactive nonauthoritative resources do not impact functionality.

    Important

    Do not delete any nonauthoritative resource that does not use the current authoritative API unless you want to delete the corresponding resource that does use the current authoritative API.

    When you delete a nonauthoritative resource that does not use the current authoritative API, the synchronization controller deletes the corresponding resource that does use the current authoritative API. For more information, see "Unexpected resource deletion behavior".

#### [11.5.3. Unexpected behavior when changing resource configurations](#ts-capi-migrate-unexpected-behavior_cluster-api-troubleshooting) Copy linkLink copied to clipboard!

On clusters that support migrating resources between the Machine API and the Cluster API, users might experience unexpected resource behavior when updating the authoritative API.

Cause
:   In addition to the two-way synchronization controller that manages changes related to migrating between authoritative APIs, other controllers can act on Machine API and Cluster API resources.

    If you make other changes while updating the value of the `spec.authoritativeAPI` field, the synchronization controller might not be the first controller to act on the resource when you save the resource specification.

Consequence
:   Because other controllers might process updates to other values before the synchronization controller processes the `spec.authoritativeAPI` field update, changing other values can cause unexpected behavior.

    For example, if you increase the number of replicas in a machine set specification while updating the value of the `spec.authoritativeAPI` field, the machine set might create machines with the unintended authoritative API.

Workaround
:   Do not change other values when you update the value of the `spec.authoritativeAPI` field. For more information, see [OCPBUGS-74638](https://issues.redhat.com/browse/OCPBUGS-74638).

#### [11.5.4. Unexpected resource deletion behavior](#ts-capi-migrate-unexpected-deletion-behavior_cluster-api-troubleshooting) Copy linkLink copied to clipboard!

On clusters that support migrating resources between the Machine API and the Cluster API, users might experience unexpected behavior when deleting Cluster API resources on a cluster where the Machine API is authoritative.

Cause
:   For any resource that uses the authoritative API, the two-way synchronization controller creates and maintains corresponding resources that do not use the current authoritative API.

    The deletion behavior for resources that do not use the current authoritative API depends on which API is authoritative.

    * When you delete a Cluster API resource on a cluster where the Machine API is authoritative, the synchronization controller deletes the corresponding Machine API resource.
    * When you delete a Machine API resource on a cluster where the Cluster API is authoritative, the synchronization controller does not delete the corresponding Cluster API resource. This difference in behavior supports migration from using the Machine API to using the Cluster API.

    This behavior occurs when deleting resources directly and when performing scale-down operations.

Consequence
:   This different behavior depending on which API is authoritative has the following consequences:

    * For clusters on which the Cluster API is authoritative, you can remove Machine API resources with no impact to the corresponding Cluster API resources.
    * For clusters on which the Machine API is authoritative, you cannot remove Cluster API resources without also deleting the corresponding Machine API resources.

Workaround
:   For clusters on which the Machine API is authoritative, do not delete any Cluster API resource unless you want to delete the corresponding Machine API resource.

#### [11.5.5. Troubleshooting resource migration](#ts-capi-resource-migration_cluster-api-troubleshooting) Copy linkLink copied to clipboard!

To help avoid or recover from issues when you migrate a resource to use a different authoritative API, you can learn how to recognize these issues. To understand unexpected behavior in your cluster, you can learn about differences between the Cluster API and the Machine API.

##### [11.5.5.1. Authoritative API types of compute machines](#machine-set-authoritative-api-machines_cluster-api-troubleshooting) Copy linkLink copied to clipboard!

The values of the `.spec.authoritativeAPI` and `.spec.template.spec.authoritativeAPI` fields in a Machine API compute machine set determine the authoritative API of the compute machines.

Expand

Table 11.3. Interaction of authoritativeAPI fields when creating compute machines

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **`.spec.authoritativeAPI` value** | `ClusterAPI` | `ClusterAPI` | `MachineAPI` | `MachineAPI` |
| **`.spec.template.spec.authoritativeAPI` value** | `ClusterAPI` | `MachineAPI` | `MachineAPI` | `ClusterAPI` |
| **`authoritativeAPI` value for new compute machines** | `ClusterAPI` | `ClusterAPI` | `MachineAPI` | `ClusterAPI` |

Show more

Note

When the `.spec.authoritativeAPI` value is `ClusterAPI`, the Machine API machine set is not authoritative and the `.spec.template.spec.authoritativeAPI` value is not used. As a result, the only combination that creates a compute machine with the Machine API as authoritative is where the `.spec.authoritativeAPI` and `.spec.template.spec.authoritativeAPI` values are `MachineAPI`.

##### [11.5.5.2. Incomplete synchronization of labels and annotations](#ts-capi-migrate-sync-label-annotation_cluster-api-troubleshooting) Copy linkLink copied to clipboard!

The label and annotation synchronization behavior differs between the Machine API and the Cluster API. In some cases, these differences cause the two-way synchronization controller to overwrite labels on a Cluster API machine during migration.

Cause
:   With the Machine API, changes to machine set labels and annotations do not propagate to existing machines and nodes. These changes only apply to machines deployed after the update.

    With the Cluster API, changes to machine set labels and annotations propagate to existing machines and nodes. When the authoritative API for a machine set changes from Machine API to Cluster API, the labels propagate to the Cluster API machines that the authoritative API manages. The propagation happens before the Cluster API machine is marked as authoritative.

Consequence
:   The two-way synchronization controller overwrites any propagated labels and annotations with the earlier value, leading to an inconsistency. This outcome only occurs when removing a label or annotation. Updates and additional labels or annotations do not cause this inconsistency.

Workaround
:   There is no workaround for this issue. For more information, see [OCPBUGS-54333](https://issues.redhat.com/browse/OCPBUGS-54333).

##### [11.5.5.3. Unsupported configuration options](#ts-capi-migrate-unsupported-features_cluster-api-troubleshooting) Copy linkLink copied to clipboard!

To understand whether the Cluster API meets your requirements, you can learn about unsupported configuration options.

The Machine API does not support all configuration options for the Cluster API. Some Machine API configurations cannot migrate to the Cluster API. Additional configuration options might be supported in a future release.

Attempting to use unsupported configurations might cause a migration to fail or result in errors.

Note

This list might not be exhaustive.

##### [11.5.5.3.1. General limitations](#ts-capi-migrate-unsupported-features-general_cluster-api-troubleshooting) Copy linkLink copied to clipboard!

The following limitations apply to all clusters:

* Machine API compute machines cannot migrate to the Cluster API unless the `NodeDeletionTimeout` field uses the Cluster API default value of `10s`.
* OpenShift Container Platform does not support using the following Cluster API fields in the `spec.template.spec` stanza of a machine set or the `spec` stanza of a machine:

  + `version`
  + `readinessGates`
* The Machine API does not support using the following Cluster API drain configuration options:

  + `nodeDrainTimeout`
  + `nodeVolumeDetachTimeout`
  + `nodeDeletionTimeout`

##### [11.5.5.3.2. Amazon Web Services (AWS) limitations](#ts-capi-migrate-unsupported-features-aws_cluster-api-troubleshooting) Copy linkLink copied to clipboard!

The following limitations apply to AWS clusters:

* The Machine API does not support using the following Amazon EC2 Instance Metadata Service (IMDS) configuration options:

  + `httpEndpoint`
  + `httpPutResponseHopLimit`
  + `instanceMetadataTags`

  If you migrate a Cluster API machine template that uses IMDS configuration options to a Machine API compute machine set, expect the following behaviors:

  + Any machines that the migrated Machine API machine set creates will not have these fields. The underlying instances will not use these settings.
  + Any existing machines that the migrated machine set manages will retain these fields. The underlying instances will continue to use these settings.
* OpenShift Container Platform does not support using the following AWS machine template fields:

  + `spec.ami.eksLookupType`
  + `spec.cloudInit`
  + `spec.ignition.proxy`
  + `spec.ignition.tls`
  + `spec.imageLookupBaseOS`
  + `spec.imageLookupFormat`
  + `spec.imageLookupOrg`
  + `spec.networkInterfaces`
  + `spec.privateDNSName`
  + `spec.securityGroupOverrides`
  + `spec.uncompressedUserData`
* The Cluster API does not support orphaning a nonroot Amazon Elastic Block Store (Amazon EBS) volume when its underlying AWS EC2 instance is removed. When an instance is terminated, the Cluster API removes all dependent volumes.

### [11.6. Disabling the Cluster API](#cluster-api-disabling) Copy linkLink copied to clipboard!

To stop using the Cluster API to automate the management of infrastructure resources on your OpenShift Container Platform cluster, convert any Cluster API resources on your cluster to equivalent Machine API resources.

Important

Managing machines with the Cluster API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

#### [11.6.1. Cluster API resources migration to Machine API resources](#capi-to-mapi-migration-overview_cluster-api-disabling) Copy linkLink copied to clipboard!

On clusters that support migrating between the Cluster API and Machine API resources, the two-way synchronization controller supports converting a Cluster API resource to a Machine API resource.

Note

The two-way synchronization controller only operates on clusters with the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set enabled.

You can migrate resources that you originally migrated from the Machine API to the Cluster API, or resources that you created as Cluster API resources initially. Migrating an original Machine API resource to a Cluster API resource and then migrating it back provides an opportunity to verify that the migration process works as expected.

Note

You can only migrate some resources on supported infrastructure types.

Expand

Table 11.4. Supported resource conversions

| Infrastructure | Compute machine | Compute machine set | Machine health check | Control plane machine set | Cluster autoscaler |
| --- | --- | --- | --- | --- | --- |
| AWS | Technology Preview | Technology Preview | Not Available | Not Available | Not Available |
| All other infrastructure types | Not Available | Not Available | Not Available | Not Available | Not Available |

Show more

##### [11.6.1.1. Migrating a Cluster API resource to use the Machine API](#migrating-between-capi-mapi_cluster-api-disabling) Copy linkLink copied to clipboard!

You can migrate individual Cluster API objects to equivalent Machine API objects.

Important

Migrating a Cluster API resource to use the Machine API is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Prerequisites**

* You have deployed an OpenShift Container Platform cluster on a supported infrastructure type.
* You have enabled the `MachineAPIMigration` feature gate in the `TechPreviewNoUpgrade` feature set.
* You have access to the cluster using an account with `cluster-admin` permissions.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Identify the Cluster API resource that you want to migrate to a Machine API resource by running the following command:

   ```
   $ oc get <resource_kind> -n openshift-cluster-api
   ```

   where `<resource_kind>` is one of the following values:

   `machine.cluster.x-k8s.io`
   :   The fully qualified name of the resource kind for a compute or control plane machine.

   `machineset.cluster.x-k8s.io`
   :   The fully qualified name of the resource kind for a compute machine set.
2. Edit the resource specification by running the following command:

   ```
   $ oc edit <resource_kind>/<resource_name> -n openshift-machine-api
   ```

   where:

   `<resource_kind>`
   :   Specifies a compute machine with `machine.machine.openshift.io` or compute machine set with `machineset.machine.openshift.io`.

   `<resource_name>`
   :   Specifies the name of the Machine API resource that corresponds to the Cluster API resource that you want to migrate to the Machine API.
3. In the resource specification, update the value of the `spec.authoritativeAPI` field:

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: <resource_kind>
   metadata:
     name: <resource_name>
     [...]
   spec:
     authoritativeAPI: MachineAPI
     [...]
   status:
     authoritativeAPI: ClusterAPI
     [...]
   ```

   where:

   `kind`
   :   Specifies the resource kind of the resource that you want to migrate. For example, the resource kind for a compute machine set is `MachineSet` and the resource kind for a compute machine is `Machine`.

   `metadata.name`
   :   Specifies the name of the resource that you want to migrate.

   `spec.authoritativeAPI`
   :   Specifies the authoritative API that you want this resource to use. For example, to start migrating a Cluster API resource to the Machine API, specify `MachineAPI`.

   `status.authoritativeAPI`
   :   Specifies the value for the current authoritative API. This value indicates which API currently manages this resource. Do not change the value in this part of the specification.

   Important

   Do not change other values when you update the value of the `spec.authoritativeAPI` field. Because other controllers might process updates to other values before the synchronization controller processes the `spec.authoritativeAPI` field update, changing other values can cause unexpected behavior.

   For more information, see "Unexpected behavior when changing resource configurations".

**Verification**

* Check the status of the conversion by running the following command:

  ```
  $ oc -n openshift-machine-api get <resource_kind>/<resource_name> -o json | jq .status.authoritativeAPI
  ```

  where:

  `<resource_kind>`
  :   Specifies a compute machine with `machine.machine.openshift.io` or compute machine set with `machineset.machine.openshift.io`.

  `<resource_name>`
  :   Specifies the name of the Machine API resource that corresponds to the Cluster API resource that you want to migrate to the Machine API.

  + While the conversion progresses, this command returns a value of `Migrating`. If this value persists for a long time, check the logs for the `cluster-capi-operator` deployment in the `openshift-cluster-api` namespace for more information and to identify potential issues.
  + When the conversion is complete, this command returns a value of `MachineAPI`.

  Important

  Do not delete any nonauthoritative resource that does not use the current authoritative API unless you want to delete the corresponding resource that does use the current authoritative API.

  When you delete a nonauthoritative resource that does not use the current authoritative API, the synchronization controller deletes the corresponding resource that does use the current authoritative API. For more information, see "Unexpected resource deletion behavior" in the *Troubleshooting resource migration* content.

##### [11.6.1.2. Authoritative API types of compute machines](#machine-set-authoritative-api-machines_cluster-api-disabling) Copy linkLink copied to clipboard!

The values of the `.spec.authoritativeAPI` and `.spec.template.spec.authoritativeAPI` fields in a Machine API compute machine set determine the authoritative API of the compute machines.

Expand

Table 11.5. Interaction of authoritativeAPI fields when creating compute machines

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **`.spec.authoritativeAPI` value** | `ClusterAPI` | `ClusterAPI` | `MachineAPI` | `MachineAPI` |
| **`.spec.template.spec.authoritativeAPI` value** | `ClusterAPI` | `MachineAPI` | `MachineAPI` | `ClusterAPI` |
| **`authoritativeAPI` value for new compute machines** | `ClusterAPI` | `ClusterAPI` | `MachineAPI` | `ClusterAPI` |

Show more

Note

When the `.spec.authoritativeAPI` value is `ClusterAPI`, the Machine API machine set is not authoritative and the `.spec.template.spec.authoritativeAPI` value is not used. As a result, the only combination that creates a compute machine with the Machine API as authoritative is where the `.spec.authoritativeAPI` and `.spec.template.spec.authoritativeAPI` values are `MachineAPI`.

## [Chapter 12. Deploying machine health checks](#deploying-machine-health-checks) Copy linkLink copied to clipboard!

You can configure and deploy a machine health check to automatically repair damaged machines in a machine pool.

Important

You can use the advanced machine management and scaling capabilities only in clusters where the Machine API is operational. Clusters with user-provisioned infrastructure require additional validation and configuration to use the Machine API.

Clusters with the infrastructure platform type `none` cannot use the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that supports the feature. This parameter cannot be changed after installation.

To view the platform type for your cluster, run the following command:

```
$ oc get infrastructure cluster -o jsonpath='{.status.platform}'
```

### [12.1. About machine health checks](#machine-health-checks-about_deploying-machine-health-checks) Copy linkLink copied to clipboard!

You can use machine health checks to detect and remediate unhealthy machines automatically, limiting disruption to the targeted machine pool.

Note

You can only apply a machine health check to machines that are managed by compute machine sets or control plane machine sets.

To monitor machine health, create a resource to define the configuration for a controller. Set a condition to check, such as staying in the `NotReady` status for five minutes or displaying a permanent condition in the node-problem-detector, and a label for the set of machines to monitor.

The controller that observes a `MachineHealthCheck` resource checks for the defined condition. If a machine fails the health check, the machine is automatically deleted and one is created to take its place. When a machine is deleted, you see a `machine deleted` event.

To limit disruptive impact of the machine deletion, the controller drains and deletes only one node at a time. If there are more unhealthy machines than the `maxUnhealthy` threshold allows for in the targeted pool of machines, remediation stops and therefore enables manual intervention.

Note

Consider the timeouts carefully, accounting for workloads and requirements.

* Long timeouts can result in long periods of downtime for the workload on the unhealthy machine.
* Too short timeouts can result in a remediation loop. For example, the timeout for checking the `NotReady` status must be long enough to allow the machine to complete the startup process.

To stop the check, remove the resource.

#### [12.1.1. Limitations when deploying machine health checks](#machine-health-checks-limitations_deploying-machine-health-checks) Copy linkLink copied to clipboard!

There are limitations to consider before deploying a machine health check:

* Only machines owned by a machine set are remediated by a machine health check.
* If the node for a machine is removed from the cluster, a machine health check considers the machine to be unhealthy and remediates it immediately.
* If the corresponding node for a machine does not join the cluster after the `nodeStartupTimeout`, the machine is remediated.
* A machine is remediated immediately if the `Machine` resource phase is `Failed`.

### [12.2. About the MachineHealthCheck custom resource](#machine-health-checks-resource_deploying-machine-health-checks) Copy linkLink copied to clipboard!

You control how a machine health check remediates unhealthy machines by using a `MachineHealthCheck` custom resource (CR) to configure health criteria, remediation limits, and startup timeouts for machines in a targeted pool.

The `MachineHealthCheck` resource for all cloud-based installation types, and other than bare metal, resembles the following YAML file:

```
apiVersion: machine.openshift.io/v1beta1
kind: MachineHealthCheck
metadata:
  name: example
  namespace: openshift-machine-api
spec:
  selector:
    matchLabels:
      machine.openshift.io/cluster-api-machine-role: <role>
      machine.openshift.io/cluster-api-machine-type: <role>
      machine.openshift.io/cluster-api-machineset: <cluster_name>-<label>-<zone>
  unhealthyConditions:
  - type:    "Ready"
    timeout: "300s"
    status: "False"
  - type:    "Ready"
    timeout: "300s"
    status: "Unknown"
  maxUnhealthy: "40%"
  nodeStartupTimeout: "10m"
```

where:

`metadata.name`
:   Specifies the name of the machine health check to deploy.

`spec.selector.matchLabels`
:   Specifies the machine pool and machine set to check by adding labels:

    * `machine.openshift.io/cluster-api-machine-role`: Specifies a label for the machine pool that you want to check.
    * `machine.openshift.io/cluster-api-machine-type`: Specifies a label for the machine pool that you want to check.
    * `machine.openshift.io/cluster-api-machineset`: Specifies the machine set to track in the `<cluster_name>-<label>-<zone>` format. For example, `prod-node-us-east-1a`.

`spec.unhealthyConditions.timeout`
:   Specifies the timeout duration for a node condition. If a condition is met for the duration of the timeout, the machine will be remediated. Long timeouts can result in long periods of downtime for a workload on an unhealthy machine.

`spec.maxUnhealthy`
:   Specifies the amount of machines allowed to be concurrently remediated in the targeted pool. This can be set as a percentage or an integer. If the number of unhealthy machines exceeds the limit set by `maxUnhealthy`, remediation is not performed.

`spec.nodeStartupTimeout`
:   Specifies the timeout duration that a machine health check must wait for a node to join the cluster before a machine is determined to be unhealthy.

Note

The `matchLabels` are examples only; you must map your machine groups based on your specific needs.

#### [12.2.1. About short-circuiting machine health check remediation](#machine-health-checks-short-circuiting_deploying-machine-health-checks) Copy linkLink copied to clipboard!

You can use machine health check short-circuiting to ensure that machine health checks remediate machines only when the cluster is healthy, by configuring the `maxUnhealthy` field in the `MachineHealthCheck` resource.

If you define a value for the `maxUnhealthy` field, before remediating any machines, the `MachineHealthCheck` compares the value of `maxUnhealthy` with the number of machines within its target pool that it has determined to be unhealthy. Remediation is not performed if the number of unhealthy machines exceeds the `maxUnhealthy` limit.

Important

If `maxUnhealthy` is not set, the value defaults to `100%` and the machines are remediated regardless of the state of the cluster.

The appropriate `maxUnhealthy` value depends on the scale of the cluster you deploy and how many machines the `MachineHealthCheck` covers. For example, you can use the `maxUnhealthy` value to cover multiple compute machine sets across multiple availability zones so that if you lose an entire zone, your `maxUnhealthy` setting prevents further remediation within the cluster. In global Azure regions that do not have multiple availability zones, you can use availability sets to ensure high availability.

Important

If you configure a `MachineHealthCheck` resource for the control plane, set the value of `maxUnhealthy` to `1`.

This configuration ensures that the machine health check takes no action when multiple control plane machines appear to be unhealthy. Multiple unhealthy control plane machines can indicate that the etcd cluster is degraded or that a scaling operation to replace a failed machine is in progress.

If the etcd cluster is degraded, manual intervention might be required. If a scaling operation is in progress, the machine health check should allow it to finish.

The `maxUnhealthy` field can be set as either an integer or percentage. There are different remediation implementations depending on the `maxUnhealthy` value.

Setting maxUnhealthy by using an absolute value
:   If `maxUnhealthy` is set to `2`:

    * Remediation will be performed if 2 or fewer nodes are unhealthy
    * Remediation will not be performed if 3 or more nodes are unhealthy

    These values are independent of how many machines are being checked by the machine health check.

Setting maxUnhealthy by using percentages
:   If `maxUnhealthy` is set to `40%` and there are 25 machines being checked:

    * Remediation will be performed if 10 or fewer nodes are unhealthy
    * Remediation will not be performed if 11 or more nodes are unhealthy

    If `maxUnhealthy` is set to `40%` and there are 6 machines being checked:

    * Remediation will be performed if 2 or fewer nodes are unhealthy
    * Remediation will not be performed if 3 or more nodes are unhealthy

    Note

    The allowed number of machines is rounded down when the percentage of `maxUnhealthy` machines that are checked is not a whole number.

### [12.3. Creating a machine health check resource](#machine-health-checks-creating_deploying-machine-health-checks) Copy linkLink copied to clipboard!

You can create a `MachineHealthCheck` resource to monitor and automatically remediate unhealthy machines in a machine set.

Note

You can only apply a machine health check to machines that are managed by compute machine sets or control plane machine sets.

**Prerequisites**

* Install the `oc` command-line interface.

**Procedure**

1. Create a `healthcheck.yml` file that contains the definition of your machine health check.
2. Apply the `healthcheck.yml` file to your cluster:

   ```
   $ oc apply -f healthcheck.yml
   ```

### [12.4. About power-based remediation of bare metal](#mgmt-power-remediation-baremetal-about_deploying-machine-health-checks) Copy linkLink copied to clipboard!

You can configure and deploy a machine health check to detect and repair unhealthy bare-metal nodes, which is critical to ensuring the overall health of the cluster.

Physically remediating a cluster can be challenging and any delay in putting the machine into a safe or an operational state increases the time the cluster remains in a degraded state, and the risk that subsequent failures might bring the cluster offline. Power-based remediation helps counter such challenges.

Instead of reprovisioning the nodes, power-based remediation uses a power controller to power off an inoperable node. This type of remediation is also called power fencing.

OpenShift Container Platform uses the `MachineHealthCheck` controller to detect faulty bare metal nodes. Power-based remediation is fast and reboots faulty nodes instead of removing them from the cluster.

Power-based remediation provides the following capabilities:

* Allows the recovery of control plane nodes
* Reduces the risk of data loss in hyperconverged environments
* Reduces the downtime associated with recovering physical machines

#### [12.4.1. About machine health checks on bare metal](#mgmt-power-remediation-baremetal-about-health-checks_deploying-machine-health-checks) Copy linkLink copied to clipboard!

Machine deletion on bare metal cluster triggers reprovisioning of a bare metal host. Usually bare metal reprovisioning is a lengthy process, during which the cluster is missing compute resources and applications might be interrupted.

There are two ways to change the default remediation process from machine deletion to host power-cycle:

1. Annotate the `MachineHealthCheck` resource with the `machine.openshift.io/remediation-strategy: external-baremetal` annotation.
2. Create a `Metal3RemediationTemplate` resource, and refer to it in the `spec.remediationTemplate` of the `MachineHealthCheck`.

After using one of these methods, unhealthy machines are power-cycled by using Baseboard Management Controller (BMC) credentials.

About the annotation-based remediation process
:   The annotation-based remediation process performs the following steps:

    1. The MachineHealthCheck (MHC) controller detects that a node is unhealthy.
    2. The MHC notifies the bare metal machine controller which requests to power-off the unhealthy node.
    3. After the power is off, the node is deleted, which allows the cluster to reschedule the affected workload on other nodes.
    4. The bare metal machine controller requests to power on the node.
    5. After the node is up, the node re-registers itself with the cluster, resulting in the creation of a new node.
    6. After the node is recreated, the bare metal machine controller restores the annotations and labels that existed on the unhealthy node before its deletion.

    Note

    If the power operations did not complete, the bare metal machine controller triggers the reprovisioning of the unhealthy node unless this is a control plane node or a node that was provisioned externally.

About the metal3-based remediation process
:   The metal3-based remediation process performs the following steps:

    1. The MachineHealthCheck (MHC) controller detects that a node is unhealthy.
    2. The MHC creates a metal3 remediation custom resource for the metal3 remediation controller, which requests to power-off the unhealthy node.
    3. After the power is off, the node is deleted, which allows the cluster to reschedule the affected workload on other nodes.
    4. The metal3 remediation controller requests to power on the node.
    5. After the node is up, the node re-registers itself with the cluster, resulting in the creation of a new node.
    6. After the node is recreated, the metal3 remediation controller restores the annotations and labels that existed on the unhealthy node before its deletion.

    Note

    If the power operations did not complete, the metal3 remediation controller triggers the reprovisioning of the unhealthy node unless this is a control plane node or a node that was provisioned externally.

#### [12.4.2. Creating a MachineHealthCheck resource for bare metal](#mgmt-power-remediation-baremetal-about-creating-mhc-baremetal_deploying-machine-health-checks) Copy linkLink copied to clipboard!

You control how a machine health check remediates unhealthy machines by using a `MachineHealthCheck` resource to configure health criteria, remediation limits, and startup timeouts for machines in a targeted pool.

**Prerequisites**

* The OpenShift Container Platform is installed using installer-provisioned infrastructure.
* Access to Baseboard Management Controller (BMC) credentials or BMC access to each node.
* Network access to the BMC interface of the unhealthy node.
* For a metal3-based remediation, a `Metal3RemediationTemplate` resource must exist.

  **Sample `Metal3RemediationTemplate` resource for bare metal, metal3-based remediation**

  ```
  apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
  kind: Metal3RemediationTemplate
  metadata:
    name: metal3-remediation-template
    namespace: openshift-machine-api
  spec:
    template:
      spec:
        strategy:
          type: Reboot
          retryLimit: 1
          timeout: 5m0s
  ```

**Procedure**

1. Create a `healthcheck.yaml` file that contains the definition of your machine health check.

   **Sample `MachineHealthCheck` resource for bare metal, annotation-based remediation**

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineHealthCheck
   metadata:
     name: example
     namespace: openshift-machine-api
     annotations:
       machine.openshift.io/remediation-strategy: external-baremetal
   spec:
     selector:
       matchLabels:
         machine.openshift.io/cluster-api-machine-role: <role>
         machine.openshift.io/cluster-api-machine-type: <role>
         machine.openshift.io/cluster-api-machineset: <cluster_name>-<label>-<zone>
     unhealthyConditions:
     - type:    "Ready"
       timeout: "300s"
       status: "False"
     - type:    "Ready"
       timeout: "300s"
       status: "Unknown"
     maxUnhealthy: "40%"
     nodeStartupTimeout: "10m"
   ```

   where

   `metadata.name`
   :   Specify the name of the machine health check to deploy.

   `metadata.annotations`
   :   Specify the required annotation for the annotation-based remediation process.

       Important

       You must include the `machine.openshift.io/remediation-strategy: external-baremetal` annotation in the `annotations` section to enable annotation-based remediation. With this remediation strategy, unhealthy hosts are rebooted instead of removed from the cluster.

   `spec.selector.matchLabels`
   :   Specify the machine pool and machine set to check by adding labels:

       * `machine.openshift.io/cluster-api-machine-role`: Specify a label for the machine pool that you want to check.
       * `machine.openshift.io/cluster-api-machine-type`: Specify a label for the machine pool that you want to check.
       * `machine.openshift.io/cluster-api-machineset`: Specify the machine set to track in the `<cluster_name>-<label>-<zone>` format. For example, `prod-node-us-east-1a`.

   `spec.unhealthyConditions.timeout`
   :   Specify the timeout duration for a node condition. If a condition is met for the duration of the timeout, the machine will be remediated. Long timeouts can result in long periods of downtime for a workload on an unhealthy machine.

   `spec.maxUnhealthy`
   :   Specify the amount of machines allowed to be concurrently remediated in the targeted pool. This can be set as a percentage or an integer. If the number of unhealthy machines exceeds the limit set by `maxUnhealthy`, remediation is not performed.

   `spec.nodeStartupTimeout`
   :   Specify the timeout duration that a machine health check must wait for a node to join the cluster before a machine is determined to be unhealthy.

   **Sample `MachineHealthCheck` resource for bare metal, metal3-based remediation**

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineHealthCheck
   metadata:
     name: example
     namespace: openshift-machine-api
   spec:
     selector:
       matchLabels:
         machine.openshift.io/cluster-api-machine-role: <role>
         machine.openshift.io/cluster-api-machine-type: <role>
         machine.openshift.io/cluster-api-machineset: <cluster_name>-<label>-<zone>
     remediationTemplate:
       apiVersion: infrastructure.cluster.x-k8s.io/v1beta1
       kind: Metal3RemediationTemplate
       name: metal3-remediation-template
       namespace: openshift-machine-api
     unhealthyConditions:
     - type:    "Ready"
       timeout: "300s"
   ```

   where:

   `metadata.name`
   :   Specify the name of the machine health check to deploy.

   `spec.selector.matchLabels`
   :   Specify the machine pool and machine set to check by adding labels:

       * `machine.openshift.io/cluster-api-machine-role`: Specify a label for the machine pool that you want to check.
       * `machine.openshift.io/cluster-api-machine-type`: Specify a label for the machine pool that you want to check.
       * `machine.openshift.io/cluster-api-machineset`: Specify the machine set to track in the `<cluster_name>-<label>-<zone>` format. For example, `prod-node-us-east-1a`.

   `spec.remediationTemplate`
   :   Specify the metal3 remediation template to use. Provide the following information:

       * `apiVersion`. Specify the API version as `infrastructure.cluster.x-k8s.io/v1beta1`.
       * `kind`. Specify `Metal3RemediationTemplate`.
       * `name`. Specify the name of the template.
       * `namespace`. Specify the namespace of the template.

   `spec.unhealthyConditions.timeout`
   :   Specify the timeout duration for a node condition. If a condition is met for the duration of the timeout, the machine will be remediated. Long timeouts can result in long periods of downtime for a workload on an unhealthy machine.

   Note

   The `matchLabels` are examples only; you must map your machine groups based on your specific needs.
2. Apply the `healthcheck.yaml` file to your cluster using the following command:

   ```
   $ oc apply -f healthcheck.yaml
   ```

#### [12.4.3. Troubleshooting issues with power-based remediation](#mgmt-power-remediation-baremetal-about-troubleshooting_deploying-machine-health-checks) Copy linkLink copied to clipboard!

To troubleshoot issues you are having with power-based remediation, check the connection to the Baseboard Management Controller (BMC).

**Procedure**

* Verify the following conditions:

  + You have access to the BMC.
  + The BMC is connected to the control plane node that is responsible for running the remediation task.

## [Legal Notice](#idm140199739129536) Copy linkLink copied to clipboard!

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
