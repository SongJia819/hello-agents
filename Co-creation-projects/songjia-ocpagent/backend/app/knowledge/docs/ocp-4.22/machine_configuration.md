---
title: "Machine configuration"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/machine_configuration/index
retrieved_at: 2026-09-05T05:42:12.660035+00:00
---

# Machine configuration

---

OpenShift Container Platform 4.22

## Managing and applying configuration and updates of the base operating system and container runtimes in OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140329130314368)

**Abstract**

This document provides instructions for managing changes to systemd, CRI-O, Kubelet, the kernel, and other system features by using MachineConfig, KubeletConfig, and ContainerRuntimeConfig objects. In addition, image layering allows you to easily customize the underlying node operating system by layering additional images onto the base image of any of your cluster worker nodes.

---

## [Chapter 1. Machine configuration overview](#machine-config-index) Copy linkLink copied to clipboard!

You can make changes to the operating systems on OpenShift Container Platform nodes by creating `MachineConfig` objects, which are managed by the Machine Config Operator. For example, you can use the Machine Config Operator (MCO) and machine configs to manage systemd, CRI-O and kubelet, the kernel, Network Manager, and other system features.

Tasks in this section describe how to use features of the Machine Config Operator to configure operating system features on OpenShift Container Platform nodes.

Important

NetworkManager stores new network configurations to `/etc/NetworkManager/system-connections/` in a key file format.

Previously, NetworkManager stored new network configurations to `/etc/sysconfig/network-scripts/` in the `ifcfg` format. Starting with RHEL 9.0, RHEL stores new network configurations at `/etc/NetworkManager/system-connections/` in a key file format. The connections configurations stored to `/etc/sysconfig/network-scripts/` in the old format still work uninterrupted. Modifications in existing profiles continue updating the older files.

### [1.1. About the Machine Config Operator](#about-machine-config-operator_machine-config-overview) Copy linkLink copied to clipboard!

The Machine Config Operator (MCO) manages the lifecycle of your cluster nodes by coordinating operating system updates and configuration changes. You can use the MCO to simplify node upgrades and ensures consistent host environments across your cluster.

OpenShift Container Platform 4.22 integrates both operating system and cluster management. Because the cluster manages its own updates, including updates to Red Hat Enterprise Linux CoreOS (RHCOS) on cluster nodes, OpenShift Container Platform provides an opinionated lifecycle management experience that simplifies the orchestration of node upgrades.

OpenShift Container Platform employs three daemon sets and controllers to simplify node management. These daemon sets orchestrate operating system updates and configuration changes to the hosts by using standard Kubernetes-style constructs. They include:

* The `machine-config-controller`, which coordinates machine upgrades from the control plane. It monitors all of the cluster nodes and orchestrates their configuration updates.
* The `machine-config-daemon` daemon set, which runs on each node in the cluster and updates a machine to configuration as defined by machine config and as instructed by the MachineConfigController. When the node detects a change, it drains off its pods, applies the update, and reboots. These changes come in the form of Ignition configuration files that apply the specified machine configuration and control kubelet configuration. The update itself is delivered in a container. This process is key to the success of managing OpenShift Container Platform and RHCOS updates together.
* The `machine-config-server` daemon set, which provides the Ignition config files to control plane nodes as they join the cluster.

The machine configuration is a subset of the Ignition configuration. The `machine-config-daemon` reads the machine configuration to see if it needs to do an OSTree update or if it must apply a series of systemd kubelet file changes, configuration changes, or other changes to the operating system or OpenShift Container Platform configuration.

When you perform node management operations, you create or modify a `KubeletConfig` custom resource (CR).

Important

When changes are made to a machine configuration, the Machine Config Operator (MCO) automatically reboots all corresponding nodes in order for the changes to take effect.

You can mitigate the disruption caused by some machine config changes by using a node disruption policy. See *Understanding node restart behaviors after machine config changes*.

Alternatively, you can prevent the nodes from automatically rebooting after machine configuration changes before making the changes. Pause the autoreboot process by setting the `spec.paused` field to `true` in the corresponding machine config pool. When paused, machine configuration changes are not applied until you set the `spec.paused` field to `false` and the nodes have rebooted into the new configuration.

* When the MCO detects any of the following changes, it applies the update without draining or rebooting the node:

  + Changes to the SSH key in the `spec.config.passwd.users.sshAuthorizedKeys` parameter of a machine config.
  + Changes to the global pull secret or pull secret in the `openshift-config` namespace.
  + Automatic rotation of the `/etc/kubernetes/kubelet-ca.crt` certificate authority (CA) by the Kubernetes API Server Operator.
* When the MCO detects changes to the `/etc/containers/registries.conf` file, such as editing an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object, it drains the corresponding nodes, applies the changes, and uncordons the nodes. The node drain does not happen for the following changes:

  + The addition of a registry with the `pull-from-mirror = "digest-only"` parameter set for each mirror.
  + The addition of a mirror with the `pull-from-mirror = "digest-only"` parameter set in a registry.
  + The addition of items to the `unqualified-search-registries` list.

There might be situations where the configuration on a node does not fully match what the currently-applied machine config specifies. This state is called *configuration drift*. The Machine Config Daemon (MCD) regularly checks the nodes for configuration drift. If the MCD detects configuration drift, the MCO marks the node `degraded` until an administrator corrects the node configuration. A degraded node is online and operational, but, it cannot be updated.

### [1.2. Machine config overview](#machine-config-overview_machine-config-overview) Copy linkLink copied to clipboard!

You should understand what the Machine Config Operator (MCO) does and how it interacts with other components before making advanced, system-level changes to an OpenShift Container Platform cluster.

The Machine Config Operator (MCO) manages updates to systemd, CRI-O and Kubelet, the kernel, Network Manager, and other system features. It also offers a `MachineConfig` CRD that can write configuration files onto the host.

You should know the following details about the MCO, machine configs, and how they are used:

* A machine config can make a specific change to a file or service on the operating system of each system representing a pool of OpenShift Container Platform nodes.
* MCO applies changes to operating systems in pools of machines. All OpenShift Container Platform clusters start with worker and control plane node pools. By adding more role labels, you can configure custom pools of nodes. For example, you can set up a custom pool of worker nodes that includes particular hardware features needed by an application. However, examples in this section focus on changes to the default pool types.

  Important

  A node can have multiple labels applied that indicate its type, such as `master` or `worker`, however it can be a member of only a **single** machine config pool.
* Machine configs are processed alphabetically, in lexicographically increasing order, by their name. The render controller uses the first machine config in the list as the base and appends the rest to the base machine config into a rendered machine config, which is then applied to the appropriate nodes.
* When you create a machine config for the worker nodes, the changes are also applied to the nodes in all custom pools.

  However, as of OpenShift Container Platform 4.15, any machine configs that target custom pools always override worker machine configs if the worker machine configs contain definitions for the same fields.
* After a machine config change, the MCO updates the affected nodes alphabetically by zone, based on the `topology.kubernetes.io/zone` label. If a zone has more than one node, the oldest nodes are updated first. For nodes that do not use zones, such as in bare metal deployments, the nodes are upgraded by age, with the oldest nodes updated first. The MCO updates the number of nodes as specified by the `maxUnavailable` field on the machine configuration pool at a time.
* Some machine configuration must be in place before OpenShift Container Platform is installed to disk. In most cases, this can be accomplished by creating a machine config that is injected directly into the OpenShift Container Platform installer process, instead of running as a postinstallation machine config. In other cases, you might need to do bare metal installation where you pass kernel arguments at OpenShift Container Platform installer startup, to do such things as setting per-node individual IP addresses or advanced disk partitioning.
* MCO manages items that are set in machine configs. Manual changes you do to your systems will not be overwritten by MCO, unless MCO is explicitly told to manage a conflicting file. In other words, MCO only makes specific updates you request, it does not claim control over the whole node.
* Manual changes to nodes are strongly discouraged. If you need to decommission a node and start a new one, those direct changes would be lost.
* MCO is only supported for writing to files in `/etc` and `/var` directories, although there are symbolic links to some directories that can be writeable by being symbolically linked to one of those areas. The `/opt` and `/usr/local` directories are examples.
* Ignition is the configuration format used in MachineConfigs. For details, see "Configuration Specification v3.5.0 (Ignition documentation)".
* Although Ignition config settings can be delivered directly at OpenShift Container Platform installation time, and are formatted in the same way that MCO delivers Ignition configs, MCO has no way of seeing what those original Ignition configs are. Therefore, you should wrap Ignition config settings into a machine config before deploying them.
* When a file managed by MCO changes outside of MCO, the Machine Config Daemon (MCD) sets the node as `degraded`. It will not overwrite the offending file, however, and should continue to operate in a `degraded` state.
* A key reason for using a machine config is that it will be applied when you spin up new nodes for a pool in your OpenShift Container Platform cluster. The `machine-api-operator` provisions a new machine and MCO configures it.

MCO uses Ignition as the configuration format. OpenShift Container Platform 4.6 moved from Ignition config specification version 2 to version 3. For more information, see the "Configuration Specification v3.5.0 (Ignition documentation)" in the *Additional resources* section.

#### [1.2.1. What can you change with machine configs?](#what-can-you-change-with-machine-configs) Copy linkLink copied to clipboard!

The kinds of components that MCO can change include:

* **config**: Create Ignition config objects to do things like modify files, systemd services, and other features on OpenShift Container Platform machines, including:

  + **Configuration files**: Create or overwrite files in the `/var` or `/etc` directory.
  + **systemd units**: Create and set the status of a systemd service or add to an existing systemd service by dropping in additional settings.
  + **users and groups**: Change SSH keys in the passwd section postinstallation.

    Important

    - Changing SSH keys by using a machine config is supported only for the `core` user.
    - Adding new users by using a machine config is not supported.
* **kernelArguments**: Add arguments to the kernel command line when OpenShift Container Platform nodes boot.
* **kernelType**: Optionally identify a non-standard kernel to use instead of the standard kernel. Use `realtime` to use the RT kernel (for RAN). This is only supported on select platforms. Use the `64k-pages` parameter to enable the 64k page size kernel. This setting is exclusive to machines with 64-bit ARM architectures.
* **fips**: Enable FIPS mode. FIPS should be set at installation-time setting and not a postinstallation procedure. For more information, see "Using system-wide cryptographic policies".

  Important

  To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening).

  When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86\_64, ppc64le, and s390x architectures.
* **extensions**: Extend RHCOS features by adding selected pre-packaged software. For this feature, available extensions include usbguard and kernel modules. For more information, see "Protecting systems against intrusive USB devices" in the *Additional resources* section.
* **Custom resources (for `ContainerRuntime` and `Kubelet`)**: Outside of machine configs, MCO manages two special custom resources for modifying CRI-O container runtime settings (`ContainerRuntime` CR) and the Kubelet service (`Kubelet` CR).

The MCO is not the only Operator that can change operating system components on OpenShift Container Platform nodes. Other Operators can modify operating system-level features as well. One example is the Node Tuning Operator, which allows you to do node-level tuning through Tuned daemon profiles.

Tasks for the MCO configuration that can be done after installation are included in the following procedures. See descriptions of RHCOS bare metal installation for system configuration tasks that must be done during or before OpenShift Container Platform installation. By default, many of the changes you make with the MCO require a reboot.

* When the MCO detects any of the following changes, it applies the update without draining or rebooting the node:

  + Changes to the SSH key in the `spec.config.passwd.users.sshAuthorizedKeys` parameter of a machine config.
  + Changes to the global pull secret or pull secret in the `openshift-config` namespace.
  + Automatic rotation of the `/etc/kubernetes/kubelet-ca.crt` certificate authority (CA) by the Kubernetes API Server Operator.
* When the MCO detects changes to the `/etc/containers/registries.conf` file, such as editing an `ImageDigestMirrorSet`, `ImageTagMirrorSet`, or `ImageContentSourcePolicy` object, it drains the corresponding nodes, applies the changes, and uncordons the nodes. The node drain does not happen for the following changes:

  + The addition of a registry with the `pull-from-mirror = "digest-only"` parameter set for each mirror.
  + The addition of a mirror with the `pull-from-mirror = "digest-only"` parameter set in a registry.
  + The addition of items to the `unqualified-search-registries` list.

In other cases, you can mitigate the disruption to your workload when the MCO makes changes by using *node disruption policies*. For information, see *Understanding node restart behaviors after machine config changes*.

There might be situations where the configuration on a node does not fully match what the currently-applied machine config specifies. This state is called *configuration drift*. The Machine Config Daemon (MCD) regularly checks the nodes for configuration drift. If the MCD detects configuration drift, the MCO marks the node `degraded` until an administrator corrects the node configuration. A degraded node is online and operational, but, it cannot be updated. For more information on configuration drift, see *Understanding configuration drift detection*.

#### [1.2.2. Node configuration management with machine config pools](#architecture-machine-config-pools_machine-config-overview) Copy linkLink copied to clipboard!

When making changes to nodes, you can modify groups of nodes by applying the changes to all of the nodes in the same machine config pool (MCP).

Machines that run control plane components or user workloads are divided into groups based on the types of resources they handle. These groups of machines are called machine config pools (MCP). Each MCP manages a set of nodes and its corresponding machine configs. The role of the node determines which MCP it belongs to; the MCP governs nodes based on its assigned node role label. Nodes in an MCP have the same configuration; this means nodes can be scaled up and torn down in response to increased or decreased workloads.

By default, there are two MCPs created by the cluster when it is installed: `master` and `worker`. Each default MCP has a defined configuration applied by the Machine Config Operator (MCO), which is responsible for managing MCPs and facilitating MCP updates.

For worker nodes, you can create additional MCPs, or custom pools, to manage nodes with custom use cases that extend outside of the default node types. Custom MCPs for the control plane nodes are not supported.

Custom pools are pools that inherit their configurations from the worker pool. They use any machine config targeted for the worker pool, but add the ability to deploy changes only targeted at the custom pool. Since a custom pool inherits its configuration from the worker pool, any change to the worker pool is applied to the custom pool as well. Custom pools that do not inherit their configurations from the worker pool are not supported by the MCO.

Note

A node can only be included in one MCP. If a node has multiple labels that correspond to several MCPs, like `worker,infra`, it is managed by the infra custom pool, not the worker pool. Custom pools take priority on selecting nodes to manage based on node labels; nodes that do not belong to a custom pool are managed by the worker pool.

It is recommended to have a custom pool for every node role you want to manage in your cluster. For example, if you create infra nodes to handle infra workloads, it is recommended to create a custom infra MCP to group those nodes together. If you apply an `infra` role label to a worker node so it has the `worker,infra` dual label, but do not have a custom infra MCP, the MCO considers it a worker node. If you remove the `worker` label from a node and apply the `infra` label without grouping it in a custom pool, the node is not recognized by the MCO and is unmanaged by the cluster.

Important

Any node labeled with the `infra` role that is only running infra workloads is not counted toward the total number of subscriptions. The MCP managing an infra node is mutually exclusive from how the cluster determines subscription charges; tagging a node with the appropriate `infra` role and using taints to prevent user workloads from being scheduled on that node are the only requirements for avoiding subscription charges for infra workloads.

The MCO applies updates for pools independently; for example, if there is an update that affects all pools, nodes from each pool update in parallel with each other. If you add a custom pool, nodes from that pool also attempt to update concurrently with the master and worker nodes.

There might be situations where the configuration on a node does not fully match what the currently-applied machine config specifies. This state is called *configuration drift*. The Machine Config Daemon (MCD) regularly checks the nodes for configuration drift. If the MCD detects configuration drift, the MCO marks the node `degraded` until an administrator corrects the node configuration. A degraded node is online and operational, but, it cannot be updated.

### [1.3. Understanding the Machine Config Operator node drain behavior](#machine-config-node-drain_machine-config-overview) Copy linkLink copied to clipboard!

When you use a machine config to change a system feature, such as adding new config files, modifying systemd units or kernel arguments, or updating SSH keys, the Machine Config Operator (MCO) applies those changes and ensures that each node is in the desired configuration state.

After you make the changes, the MCO generates a new rendered machine config. In the majority of cases, when applying the new rendered machine config, the Operator performs the following steps on each affected node until all of the affected nodes have the updated configuration:

1. Cordon. The MCO marks the node as not schedulable for additional workloads.
2. Drain. The MCO terminates all running workloads on the node, causing the workloads to be rescheduled onto other nodes.
3. Apply. The MCO writes the new configuration to the nodes as needed.
4. Reboot. The MCO restarts the node.
5. Uncordon. The MCO marks the node as schedulable for workloads.

Throughout this process, the MCO maintains the required number of pods based on the `MaxUnavailable` value set in the machine config pool.

Note

There are conditions which can prevent the MCO from draining a node. If the MCO fails to drain a node, the Operator will be unable to reboot the node, preventing any changes made to the node through a machine config. For more information and mitigation steps, see the "MCCDrainError" runbook.

If the MCO drains pods on the master node, note the following conditions:

* In single-node OpenShift clusters, the MCO skips the drain operation.
* The MCO does not drain static pods in order to prevent interference with services, such as etcd.

Note

In certain cases the nodes are not drained. For more information, see "About the Machine Config Operator."

There are ways to mitigate the disruption caused by drain and reboot cycles by using node disruption policies or disabling control plane reboots. For more information, see "Understanding node restart behaviors after machine config changes" and "Disabling the Machine Config Operator from automatically rebooting".

### [1.4. Understanding configuration drift detection](#machine-config-drift-detection_machine-config-overview) Copy linkLink copied to clipboard!

The Machine Config Operator (MCO) uses the Machine Config Daemon (MCD) to check nodes for configuration drift on a regular basis. If detected, the MCO sets the node and the machine config pool (MCP) to `Degraded` and reports the error. A degraded node is online and operational, but, it cannot be updated.

There might be situations when the on-disk state of a node differs from what is configured in the machine config. This is known as *configuration drift*. For example, a cluster admin might manually modify a file, a systemd unit file, or a file permission that was configured through a machine config. This causes configuration drift. Configuration drift can cause problems between nodes in a Machine Config Pool or when the machine configs are updated.

The MCD performs configuration drift detection upon each of the following conditions:

* When a node boots.
* After any of the files (Ignition files and systemd drop-in units) specified in the machine config are modified outside of the machine config.
* Before a new machine config is applied.

  Note

  If you apply a new machine config to the nodes, the MCD temporarily shuts down configuration drift detection. This shutdown is needed because the new machine config necessarily differs from the machine config on the nodes. After the new machine config is applied, the MCD restarts detecting configuration drift using the new machine config.

When performing configuration drift detection, the MCD validates that the file contents and permissions fully match what the currently-applied machine config specifies. Typically, the MCD detects configuration drift in less than a second after the detection is triggered.

If the MCD detects configuration drift, the MCD performs the following tasks:

* Emits an error to the console logs
* Emits a Kubernetes event
* Stops further detection on the node
* Sets the node and MCP to `degraded`

You can check if you have a degraded node by listing the MCPs:

```
$ oc get mcp worker
```

If you have a degraded MCP, the `DEGRADEDMACHINECOUNT` field is non-zero, similar to the following output:

**Example output**

```
NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
worker   rendered-worker-404caf3180818d8ac1f50c32f14b57c3   False     True       True       2              1                   1                     1                      5h51m
```

You can determine if the problem is caused by configuration drift by examining the machine config pool:

```
$ oc describe mcp worker
```

**Example output**

```
 ...
    Last Transition Time:  2021-12-20T18:54:00Z
    Message:               Node ci-ln-j4h8nkb-72292-pxqxz-worker-a-fjks4 is reporting: "content mismatch for file \"/etc/mco-test-file\""
    Reason:                1 nodes are reporting degraded status on sync
    Status:                True
    Type:                  NodeDegraded
 ...
```

In this example, the text in the `Message` field shows that a node’s `/etc/mco-test-file` file, which was added by the machine config, has changed outside of the machine config. In response, the `Type` field show that state of the node is `NodeDegraded`.

Or, if you know which node is degraded, examine that node:

```
$ oc describe node/ci-ln-j4h8nkb-72292-pxqxz-worker-a-fjks4
```

**Example output**

```
 ...

Annotations:        cloud.network.openshift.io/egress-ipconfig: [{"interface":"nic0","ifaddr":{"ipv4":"10.0.128.0/17"},"capacity":{"ip":10}}]
                    csi.volume.kubernetes.io/nodeid:
                      {"pd.csi.storage.gke.io":"projects/openshift-gce-devel-ci/zones/us-central1-a/instances/ci-ln-j4h8nkb-72292-pxqxz-worker-a-fjks4"}
                    machine.openshift.io/machine: openshift-machine-api/ci-ln-j4h8nkb-72292-pxqxz-worker-a-fjks4
                    machineconfiguration.openshift.io/controlPlaneTopology: HighlyAvailable
                    machineconfiguration.openshift.io/currentConfig: rendered-worker-67bd55d0b02b0f659aef33680693a9f9
                    machineconfiguration.openshift.io/desiredConfig: rendered-worker-67bd55d0b02b0f659aef33680693a9f9
                    machineconfiguration.openshift.io/reason: content mismatch for file "/etc/mco-test-file"
                    machineconfiguration.openshift.io/state: Degraded
 ...
```

The `content mismatch for file` error message indicates that configuration drift was detected between the node and the listed machine config. Here the error message indicates that the contents of the `/etc/mco-test-file`, which was added by the machine config, has changed outside of the machine config. As a result, the state of the node is `Degraded`.

You can correct configuration drift and return the node to the `Ready` state by performing one of the following remediations:

* Ensure that the contents and file permissions of the files on the node match what is configured in the machine config. You can manually rewrite the file contents or change the file permissions.
* Generate a force file on the degraded node. The force file causes the MCD to bypass the usual configuration drift detection and reapplies the current machine config. For more information, see "How to skip validation of failing / stuck MachineConfig in OCP 4?".

  Note

  Generating a force file on a node causes that node to reboot.

### [1.5. Checking machine config pool status](#checking-mco-status_machine-config-overview) Copy linkLink copied to clipboard!

You can see the status of the Machine Config Operator (MCO), its sub-components, and the resources it manages, by using the `oc` commands.

**Procedure**

1. To see the number of MCO-managed nodes available on your cluster for each machine config pool (MCP), run the following command:

   ```
   $ oc get machineconfigpool
   ```

   **Example output**

   ```
   NAME      CONFIG                    UPDATED  UPDATING   DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT  AGE
   master    rendered-master-06c9c4…   True     False      False     3             3                  3                   0                     4h42m
   worker    rendered-worker-f4b64…    False    True       False     3             2                  2                   0                     4h42m
   ```

   where:

   UPDATED
   :   The `True` status indicates that the MCO has applied the current machine config to the nodes in that MCP. The current machine config is specified in the `STATUS` field in the `oc get mcp` output. The `False` status indicates a node in the MCP is updating.

   UPDATING
   :   The `True` status indicates that the MCO is applying the desired machine config, as specified in the `MachineConfigPool` custom resource, to at least one of the nodes in that MCP. The desired machine config is the new, edited machine config. Nodes that are updating might not be available for scheduling. The `False` status indicates that all nodes in the MCP are updated.

   DEGRADED
   :   A `True` status indicates the MCO is blocked from applying the current or desired machine config to at least one of the nodes in that MCP, or the configuration is failing. Nodes that are degraded might not be available for scheduling. A `False` status indicates that all nodes in the MCP are ready.

   MACHINECOUNT
   :   Indicates the total number of machines in that MCP.

   READYMACHINECOUNT
   :   Indicates the number of machines that are both running the current machine config and are ready for scheduling. This count is always less than or equal to the `UPDATEDMACHINECOUNT` number.

   UPDATEDMACHINECOUNT
   :   Indicates the total number of machines in that MCP that have the current machine config.

   DEGRADEDMACHINECOUNT
   :   Indicates the total number of machines in that MCP that are marked as degraded or unreconcilable.

   In the previous output, there are three control plane (master) nodes and three worker nodes. The control plane MCP and the associated nodes are updated to the current machine config. The nodes in the worker MCP are being updated to the desired machine config. Two of the nodes in the worker MCP are updated and one is still updating, as indicated by the `UPDATEDMACHINECOUNT` being `2`. There are no issues, as indicated by the `DEGRADEDMACHINECOUNT` being `0` and `DEGRADED` being `False`.

   While the nodes in the MCP are updating, the machine config listed under `CONFIG` is the current machine config, which the MCP is being updated from. When the update is complete, the listed machine config is the desired machine config, which the MCP was updated to.

   Note

   If a node is being cordoned, that node is not included in the `READYMACHINECOUNT`, but is included in the `MACHINECOUNT`. Also, the MCP status is set to `UPDATING`. Because the node has the current machine config, it is counted in the `UPDATEDMACHINECOUNT` total:

   **Example output**

   ```
   NAME      CONFIG                    UPDATED  UPDATING   DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT  AGE
   master    rendered-master-06c9c4…   True     False      False     3             3                  3                   0                     4h42m
   worker    rendered-worker-c1b41a…   False    True       False     3             2                  3                   0                     4h42m
   ```
2. To check the status of the nodes in an MCP by examining the `MachineConfigPool` custom resource, run the following command: :

   ```
   $ oc describe mcp worker
   ```

   **Example output**

   ```
   ...
     Degraded Machine Count:     0
     Machine Count:              3
     Observed Generation:        2
     Ready Machine Count:        3
     Unavailable Machine Count:  0
     Updated Machine Count:      3
   Events:                       <none>
   ```

   Note

   If a node is being cordoned, the node is not included in the `Ready Machine Count`. It is included in the `Unavailable Machine Count`:

   **Example output**

   ```
   ...
     Degraded Machine Count:     0
     Machine Count:              3
     Observed Generation:        2
     Ready Machine Count:        2
     Unavailable Machine Count:  1
     Updated Machine Count:      3
   ```
3. To see each existing `MachineConfig` object, run the following command:

   ```
   $ oc get machineconfigs
   ```

   **Example output**

   ```
   NAME                             GENERATEDBYCONTROLLER          IGNITIONVERSION  AGE
   00-master                        2c9371fbb673b97a6fe8b1c52...   3.5.0            5h18m
   00-worker                        2c9371fbb673b97a6fe8b1c52...   3.5.0            5h18m
   01-master-container-runtime      2c9371fbb673b97a6fe8b1c52...   3.5.0            5h18m
   01-master-kubelet                2c9371fbb673b97a6fe8b1c52…     3.5.0            5h18m
   ...
   rendered-master-dde...           2c9371fbb673b97a6fe8b1c52...   3.5.0            5h18m
   rendered-worker-fde...           2c9371fbb673b97a6fe8b1c52...   3.5.0            5h18m
   ```

   Note that the `MachineConfig` objects listed as `rendered` are not meant to be changed or deleted.
4. To view the contents of a particular machine config (in this case, `01-master-kubelet`), run the following command:

   ```
   $ oc describe machineconfigs 01-master-kubelet
   ```

   The output from the command shows that this `MachineConfig` object contains both configuration files (`cloud.conf` and `kubelet.conf`) and a systemd service (Kubernetes Kubelet):

   **Example output**

   ```
   Name:         01-master-kubelet
   ...
   Spec:
     Config:
       Ignition:
         Version:  3.5.0
       Storage:
         Files:
           Contents:
             Source:   data:,
           Mode:       420
           Overwrite:  true
           Path:       /etc/kubernetes/cloud.conf
           Contents:
             Source:   data:,kind%3A%20KubeletConfiguration%0AapiVersion%3A%20kubelet.config.k8s.io%2Fv1beta1%0Aauthentication%3A%0A%20%20x509%3A%0A%20%20%20%20clientCAFile%3A%20%2Fetc%2Fkubernetes%2Fkubelet-ca.crt%0A%20%20anonymous...
           Mode:       420
           Overwrite:  true
           Path:       /etc/kubernetes/kubelet.conf
       Systemd:
         Units:
           Contents:  [Unit]
   Description=Kubernetes Kubelet
   Wants=rpc-statd.service network-online.target crio.service
   After=network-online.target crio.service

   ExecStart=/usr/bin/hyperkube \
       kubelet \
         --config=/etc/kubernetes/kubelet.conf \ ...
   ```
5. If something goes wrong with a machine config that you apply, you can always back out that change. For example, if you had run `oc create -f ./myconfig.yaml` to apply a machine config, you could remove that machine config by running the following command:

   ```
   $ oc delete -f ./myconfig.yaml
   ```

   If that was the only problem, the nodes in the affected pool should return to a non-degraded state. This actually causes the rendered configuration to roll back to its previously rendered state.

   If you add your own machine configs to your cluster, you can use the commands shown in the previous example to check their status and the related status of the pool to which they are applied.

### [1.6. About node status during updates](#checking-mco-node-status_machine-config-overview) Copy linkLink copied to clipboard!

If you make changes to a machine config pool (MCP) that results in a new machine config, for example by using a `MachineConfig` or `KubeletConfig` object, you can get detailed information about the progress of the node updates by using the machine config nodes custom resource. This information can be helpful if issues arise during the update and you need to troubleshoot a node.

The `MachineConfigNode` custom resource allows you to monitor the progress of individual node updates as they move through the update phases. This information can be helpful with troubleshooting if one of the nodes has an issue during the update. The custom resource reports where in the update process the node is at the moment, the phases that have completed, and the phases that are remaining.

The node update process consists of the following phases and subphases that are tracked by the machine config node custom resource, explained with more detail later in this section:

* **Update Prepared**. The MCO stops the configuration drift monitoring process and verifies that the newly-created machine config can be applied to a node.
* **Update Executed**. The MCO cordons and drains the node and applies the new machine config to the node files and operating system, as needed. It contains the following sub-phases:

  + **Cordoned**. The MCO cordoned the node.
  + **Drained**. The MCO drained the node.
  + **AppliedFilesAndOS**. The MCO has updated the node files and operating system.
  + **AppliedFiles**. The MCO has updated the node files.
  + **AppliedOSImage**. The MCO has updated the operating system.

    In order to see **AppliedFiles** and **AppliedOSImage** in the output, you must enable the `TechPreviewNoUpgrade` feature set on the cluster. These conditions replace **AppliedFilesAndOS**. For more information, see "Enabling features using feature gates".

    Note

    Enabling the `TechPreviewNoUpgrade` feature set cannot be undone and prevents minor version updates. These feature sets are not recommended on production clusters.

    Important

    The `AppliedFiles` and `AppliedOSImage` condition is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

    For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).
* **PinnedImageSetsProgressing** The MCO is performing the steps needed to pin and pre-load container images.
* **PinnedImageSetsDegraded** The pinned image process failed. You can view the reason for the failure by using the `oc describe machineconfignode` command, as described later in this section.
* **NodeDegraded** The node update failed. You can view the reason for the failure by using the `oc describe machineconfignode` command, as described later in this section.
* **Update Post update action** The MCO is reloading CRI-O, as needed.
* **Rebooted Node** The MCO is rebooting the node, as needed.
* **Update Complete**. The MCO is uncordoning the node, updating the node state to the cluster, and resumes producing node metrics. It contains the following sub-phase:

  + **Uncordoned**
* **Updated** The MCO completed a node update and the current config version of the node is equal to the desired updated version.
* **Resumed**. The MCO restarted the config drift monitor process and the node returns to operational state.
* **ImagePulledFromRegistry**. The MCO has pulled the desired custom layered image. This condition applies only to nodes on which on-cluster image mode has been configured.

  In order to see **ImagePulledFromRegistry** in the output, you must enable the `TechPreviewNoUpgrade` feature set on the cluster. For more information, see "Enabling features using feature gates".

  Note

  Enabling the `TechPreviewNoUpgrade` feature set cannot be undone and prevents minor version updates. These feature sets are not recommended on production clusters.

  Important

  The `ImagePulledFromRegistry` condition is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

  For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

As the update moves through these phases, you can query the `MachineConfigNode` custom resource, which reports one of the following conditions for each phase:

* `True`. The phase is complete on that node.
* `False`. The phase has not yet started or will not be executed on that node.
* `Unknown`. The phase is either being executed on that node or has an error. If the phase has an error, you can use the `oc describe machineconfignodes` command for more information, as described later in this section.

For example, consider a cluster with a newly-created machine config:

```
$ oc get machineconfig
```

**Example output**

```
NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
# ...
rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   c00e2c941bc6e236b50e0bf3988e6c790cf2bbb2   3.5.0             6d15h
rendered-master-a386c2d1550b927d274054124f58be68   c00e2c941bc6e236b50e0bf3988e6c790cf2bbb2   3.5.0             7m26s
# ...
rendered-worker-01f27f752eb84eba917450e43636b210   c00e2c941bc6e236b50e0bf3988e6c790cf2bbb2   3.5.0             6d15h
rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   c00e2c941bc6e236b50e0bf3988e6c790cf2bbb2   3.5.0             7m26s
# ...
```

In this example, the current machine config for the worker nodes is listed before the newly-created machine config, which is being applied to the worker nodes.

You can watch as the nodes are updated with the new machine config:

```
$ oc get machineconfignodes
```

**Example output**

```
NAME                                       POOLNAME      DESIREDCONFIG                                      CURRENTCONFIG                                      UPDATED   AGE
ci-ln-ds73n5t-72292-9xsm9-master-0         master        rendered-master-a386c2d1550b927d274054124f58be68   rendered-master-a386c2d1550b927d274054124f58be68   True      27M
ci-ln-ds73n5t-72292-9xsm9-master-1         master        rendered-master-a386c2d1550b927d274054124f58be68   rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   False     27M
ci-ln-ds73n5t-72292-9xsm9-master-2         master        rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   True      27M
ci-ln-ds73n5t-72292-9xsm9-worker-a-2d8tz   worker-cnf    rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   True      20M
ci-ln-ds73n5t-72292-9xsm9-worker-b-gw5sd   worker        rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   rendered-worker-01f27f752eb84eba917450e43636b210   False     20M
ci-ln-ds73n5t-72292-9xsm9-worker-c-t227w   worker        rendered-worker-01f27f752eb84eba917450e43636b210   rendered-worker-01f27f752eb84eba917450e43636b210   True      19M
```

In this example, the `ci-ln-ds73n5t-72292-9xsm9-worker-a-2d8tz` node has been updated. The new machine config, `rendered-worker-f351f6947f15cd0380514f4b1c89f8f2`, is shown as the desired and current machine configs.

The `ci-ln-ds73n5t-72292-9xsm9-worker-b-gw5sd` node is currently being updated to the new machine config. The previous and new machine configs are shown as the desired and current machine configs, respectively.

The `ci-ln-ds73n5t-72292-9xsm9-worker-c-t227w` node has not yet been updated to the new machine config. The previous machine config is shown as the desired and current machine configs.

Expand

Table 1.1. Basic machine config node fields

| Field | Meaning |
| --- | --- |
| `NAME` | The name of the node. |
| `POOLNAME` | The name of the machine config pool associated with that node. |
| `DESIREDCONFIG` | The name of the new machine config that the node updates to. |
| `CURRENTCONFIG` | The name of the current machine configuration on that node. |
| `UPDATED` | Indicates if the node has been updated by using one of the following conditions:  * If `False`, the node is being updated to the new machine configuration shown in the `DESIREDCONFIG` field. * If `True`, and the `CURRENTCONFIG` matches the new machine configuration shown in the `DESIREDCONFIG` field, the node has been updated. * If `True`, and the `CURRENTCONFIG` matches the old machine configuration shown in the `DESIREDCONFIG` field, that node has not been updated yet. |
| `AGE` | The age of the machine configuration node from when it was created. The age is not changed if the associated node is updated. |

Show more

You can use the `-o wide` flag to display additional information about the updates:

```
$ oc get machineconfignodes -o wide
```

**Example output**

```
NAME                                       POOLNAME    DESIREDCONFIG                                      CURRENTCONFIG                                         UPDATED   AGE   UPDATEPREPARED   UPDATEEXECUTED   UPDATEPOSTACTIONCOMPLETE   UPDATECOMPLETE   RESUMED   UPDATEDFILESANDOS   CORDONEDNODE   DRAINEDNODE   REBOOTEDNODE   UNCORDONEDNODE
ci-ln-ds73n5t-72292-9xsm9-master-0         master      rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   rendered-master-23cf200e4ee97daa6e39fdce24c9fb67      True      27M   False            False            False                      False            False     False               False          False         False          False
ci-ln-ds73n5t-72292-9xsm9-master-1         master      rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   rendered-master-23cf200e4ee97daa6e39fdce24c9fb67      True      27M   False            False            False                      False            False     False               False          False         False          False
ci-ln-ds73n5t-72292-9xsm9-master-2         master      rendered-master-23cf200e4ee97daa6e39fdce24c9fb67   rendered-master-23cf200e4ee97daa6e39fdce24c9fb67      True      27M   False            False            False                      False            False     False               False          False         False          False
ci-ln-ds73n5t-72292-9xsm9-worker-a-2d8tz   worker-cnf  rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   rendered-worker-f351f6947f15cd0380514f4b1c89f8f2      True      20M   False            False            False                      False            False     False               False          False         False          False
ci-ln-ds73n5t-72292-9xsm9-worker-b-gw5sd   worker      rendered-worker-f351f6947f15cd0380514f4b1c89f8f2   rendered-worker-01f27f752eb84eba917450e43636b210      False     20M   True             True             Unknown                    False            False     True                True           True          Unknown        False
ci-ln-ds73n5t-72292-9xsm9-worker-c-t227w   worker      rendered-worker-01f27f752eb84eba917450e43636b210   rendered-worker-01f27f752eb84eba917450e43636b210      True      19M   False            False            False                      False            False     False               False          False         False          False
```

In addition to the fields defined in the previous table, the `-o wide` output displays the following fields:

Expand

Table 1.2. Machine config node fields in the -o wide output

| Phase Name | Definition |
| --- | --- |
| `UPDATEPREPARED` | Indicates if the MCO is preparing to update the node. |
| `UPDATEEXECUTED` | Indicates if the MCO has completed the body of the update on the node. |
| `UPDATEPOSTACTIONCOMPLETE` | Indicates if the MCO has executed the post-update actions on the node. |
| `UPDATECOMPLETE` | Indicates if the MCO has completed the update on the node. |
| `RESUMED` | Indicates if the node has resumed normal processes. |
| `UPDATEDFILESANDOS` | Indicates if the MCO has updated the node files and operating system. |
| `CORDONEDNODE` | Indicates if the MCO has marked the node as not schedulable. |
| `DRAINEDNODE` | Indicates if the MCO has drained the node. |
| `REBOOTEDNODE` | Indicates if the MCO has restarted the node. |
| `UNCORDONEDNODE` | Indicates if the MCO has marked the node as schedulable. |

Show more

For more details on the update status, you can use the `oc describe machineconfignode` command:

```
$ oc describe machineconfignode/<machine_config_node_name>
```

**Example output**

```
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigNode
metadata:
  creationTimestamp: "2025-04-28T18:40:29Z"
  generation: 3
  name: <machine_config_node_name>
# ...
spec:
  configVersion:
    desired: rendered-master-34f96af2e41acb615410b97ce1c819e6
  node:
    name: ci-ln-921r7qk-72292-kxv95-master-0
  pool:
    name: master
status:
  conditions:
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: All pinned image sets complete
    reason: AsExpected
    status: "False"
    type: PinnedImageSetsProgressing
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the UpdatePrepared phase
    reason: NotYetOccurred
    status: "False"
    type: UpdatePrepared
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the UpdateExecuted phase
    reason: NotYetOccurred
    status: "False"
    type: UpdateExecuted
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the UpdatePostActionComplete phase
    reason: NotYetOccurred
    status: "False"
    type: UpdatePostActionComplete
  - lastTransitionTime: "2025-04-28T18:42:08Z"
    message: 'Action during update to rendered-master-34f96af2e41acb615410b97ce1c819e6:
      Uncordoned Node as part of completing upgrade phase'
    reason: Uncordoned
    status: "False"
    type: UpdateComplete
  - lastTransitionTime: "2025-04-28T18:42:08Z"
    message: 'Action during update to rendered-master-34f96af2e41acb615410b97ce1c819e6:
      In desired config . Resumed normal operations.'
    reason: Resumed
    status: "False"
    type: Resumed
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the Drained phase
    reason: NotYetOccurred
    status: "False"
    type: Drained
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the AppliedFilesAndOS phase
    reason: NotYetOccurred
    status: "False"
    type: AppliedFilesAndOS
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the Cordoned phase
    reason: NotYetOccurred
    status: "False"
    type: Cordoned
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the RebootedNode phase
    reason: NotYetOccurred
    status: "False"
    type: RebootedNode
  - lastTransitionTime: "2025-04-28T18:42:08Z"
    message: Node ci-ln-921r7qk-72292-kxv95-master-0 Updated
    reason: Updated
    status: "True"
    type: Updated
  - lastTransitionTime: "2025-04-28T18:42:08Z"
    message: 'Action during update to rendered-master-34f96af2e41acb615410b97ce1c819e6:
      UnCordoned node. The node is reporting Unschedulable = false'
    reason: UpdateCompleteUncordoned
    status: "False"
    type: Uncordoned
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: This node has not yet entered the NodeDegraded phase
    reason: NotYetOccurred
    status: "False"
    type: NodeDegraded
  - lastTransitionTime: "2025-04-28T18:41:09Z"
    message: All is good
    reason: AsExpected
    status: "False"
    type: PinnedImageSetsDegraded
  configVersion:
    current: rendered-master-34f96af2e41acb615410b97ce1c819e6
    desired: rendered-master-34f96af2e41acb615410b97ce1c819e6
  observedGeneration: 4
```

where:

`metadata.name`
:   Specifies the `MachineConfigNode` object name.

`spec.configVersion.desired`
:   Specifies the new machine configuration. This field updates after the MCO validates the machine config in the `UPDATEPREPARED` phase, and then the status adds the new configuration.

`status.configVersion.current`
:   Specifies the current machine config on the node.

For clusters configured with on-cluster image mode, the machine config node output also includes the name of the custom layered image that was applied to affected nodes.

**Example machine config node output**

```
Name:         ip-10-0-14-86.us-west-1.compute.internal
API Version:  machineconfiguration.openshift.io/v1
Kind:         MachineConfigNode
# ...
Spec:
  Config Image:
    Desired Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
  Config Version:
    Desired:  rendered-worker-d63c7736923b60b8b82492ae9a1eef40
  Node:
    Name:  ip-10-0-14-86.us-west-1.compute.internal
  Pool:
    Name:  worker
# ...
Status:
  Conditions:
# ...
    Message:               Action during update to image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3: Successfully pulled OS image image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3 from registry
    Reason:                ImagePulledFromRegistry
    Status:                False
    Type:                  ImagePulledFromRegistry
# ...
  Config Image:
    Current Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
    Desired Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
# ...
```

The digested image pull spec for the new custom layered image is in the `Spec.Config Image.Desired Image` parameter.

In order to see the custom layered image in the output, you must enable the `TechPreviewNoUpgrade` feature set on the cluster. For more information, see "Enabling features using feature gates".

Note

Enabling the `TechPreviewNoUpgrade` feature set cannot be undone and prevents minor version updates. These feature sets are not recommended on production clusters.

Important

The custom layered image output is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

#### [1.6.1. Checking node status during updates](#checking-mco-node-status-configuring_machine-config-overview) Copy linkLink copied to clipboard!

During the update of a machine config pool (MCP), you can monitor the progress of all of the nodes in your cluster by using the `oc get machineconfignodes` and `oc describe machineconfignodes` commands. These commands provide information that can be helpful if issues arise during the update and you need to troubleshoot a node.

For more information on the meaning of these fields, see "About checking machine config node status."

**Prerequisites**

* In order to see specific machine config node output, as described in "About checking machine config node status", you must enable the `TechPreviewNoUpgrade` feature set on the cluster. For more information, see "Enabling features using feature gates".

  Note

  Enabling the `TechPreviewNoUpgrade` feature set cannot be undone and prevents minor version updates. These feature sets are not recommended on production clusters.

  Important

  The custom layered image output is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

  For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Procedure**

* View the update status of all nodes in the cluster, including the current and desired machine configurations, by running the following command:

  ```
  $ oc get machineconfignodes
  ```

  **Example output**

  ```
  NAME                                       POOLNAME   DESIREDCONFIG                                      CURRENTCONFIG                                      UPDATED   AGE
  ci-ln-mdb23yt-72292-kzdsg-master-0         master     rendered-master-f21b093d20f68a7c06f922ed3ea5fbc8   rendered-master-1abc053eec29e6c945670f39d6dc8afa   False     27M
  ci-ln-mdb23yt-72292-kzdsg-master-1         master     rendered-master-1abc053eec29e6c945670f39d6dc8afa   rendered-master-1abc053eec29e6c945670f39d6dc8afa   True      27M
  ci-ln-mdb23yt-72292-kzdsg-master-2         master     rendered-master-1abc053eec29e6c945670f39d6dc8afa   rendered-master-1abc053eec29e6c945670f39d6dc8afa   True      27M
  ci-ln-mdb23yt-72292-kzdsg-worker-a-gfqjr   worker     rendered-worker-d0130cd74e9e576d7ba78ce166272bfb   rendered-worker-8f61bf839898a4487c3b5263a430e94a   False     20M
  ci-ln-mdb23yt-72292-kzdsg-worker-b-gknq4   worker     rendered-worker-8f61bf839898a4487c3b5263a430e94a   rendered-worker-8f61bf839898a4487c3b5263a430e94a   True      20M
  ci-ln-mdb23yt-72292-kzdsg-worker-c-mffrx   worker     rendered-worker-8f61bf839898a4487c3b5263a430e94a   rendered-worker-8f61bf839898a4487c3b5263a430e94a   True      19M
  ```
* View of all machine config node status fields for the nodes in your cluster by running the following command:

  ```
  $ oc get machineconfignodes -o wide
  ```

  **Example output**

  ```
  NAME                                       POOLNAME   DESIREDCONFIG                                      CURRENTCONFIG                                      UPDATED   AGE   UPDATEPREPARED   UPDATEEXECUTED   UPDATEPOSTACTIONCOMPLETE   UPDATECOMPLETE   RESUMED   UPDATEDFILESANDOS   CORDONEDNODE   DRAINEDNODE   REBOOTEDNODE   UNCORDONEDNODE
  ci-ln-g6dr34b-72292-g9btv-master-0         master     rendered-master-d4e122320b351cdbe1df59ddb63ddcfc   rendered-master-6f2064fcb36d2a914de5b0c660dc49ff   False     27M   True             Unknown          False                      False            False     Unknown             False          False         False          False
  ci-ln-g6dr34b-72292-g9btv-master-1         master     rendered-master-6f2064fcb36d2a914de5b0c660dc49ff   rendered-master-6f2064fcb36d2a914de5b0c660dc49ff   True      27M   False            False            False                      False            False     False               False          False         False          False
  ci-ln-g6dr34b-72292-g9btv-master-2         master     rendered-master-6f2064fcb36d2a914de5b0c660dc49ff   rendered-master-6f2064fcb36d2a914de5b0c660dc49ff   True      27M   False            False            False                      False            False     False               False          False         False          False
  ci-ln-g6dr34b-72292-g9btv-worker-a-sjh5r   worker     rendered-worker-671b88c8c569fa3f60dc1a27cf9c91f2   rendered-worker-d5534cb730e5e108905fc285c2a42b6c   False     20M   True             Unknown          False                      False            False     Unknown             False          False         False          False
  ci-ln-g6dr34b-72292-g9btv-worker-b-xthbz   worker     rendered-worker-d5534cb730e5e108905fc285c2a42b6c   rendered-worker-d5534cb730e5e108905fc285c2a42b6c   True      20M   False            False            False                      False            False     False               False          False         False          False
  ci-ln-g6dr34b-72292-g9btv-worker-c-gnpd6   worker     rendered-worker-d5534cb730e5e108905fc285c2a42b6c   rendered-worker-d5534cb730e5e108905fc285c2a42b6c   True      19M   False            False            False                      False            False     False               False          False         False          False
  ```
* Check the update status of nodes in a specific machine config pool by running the following command:

  ```
  $ oc get machineconfignodes $(oc get machineconfignodes -o json | jq -r '.items[]|select(.spec.pool.name=="<pool_name>")|.metadata.name')
  ```

  1

  where:

  `<pool_name>`
  :   Specifies the name of the machine config pool.

      **Example output**

      ```
      NAME                                       POOLNAME   DESIREDCONFIG                                      CURRENTCONFIG                                      UPDATED   AGE
      ci-ln-g6dr34b-72292-g9btv-worker-a-sjh5r   worker     rendered-worker-d5534cb730e5e108905fc285c2a42b6c   rendered-worker-d5534cb730e5e108905fc285c2a42b6c   True      20M
      ci-ln-g6dr34b-72292-g9btv-worker-b-xthbz   worker     rendered-worker-d5534cb730e5e108905fc285c2a42b6c   rendered-worker-faf6b50218a8bbce21f1370866283de5   False     20M
      ci-ln-g6dr34b-72292-g9btv-worker-c-gnpd6   worker     rendered-worker-faf6b50218a8bbce21f1370866283de5   rendered-worker-faf6b50218a8bbce21f1370866283de5   True      19M
      ```
* Check the update status of an individual node by running the following command:

  ```
  $ oc describe machineconfignode/<node_name>
  ```

  **Example output**

  ```
  apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineConfigNode
  metadata:
    creationTimestamp: "2025-04-28T18:52:16Z"
    generation: 3
    name: ci-ln-921r7qk-72292-kxv95-worker-a-zmxrr
    ownerReferences:
    - apiVersion: v1
      kind: Node
      name: ci-ln-921r7qk-72292-kxv95-worker-a-zmxrr
      uid: e548a8d1-4f16-42cd-9234-87ac5aede6c1
    resourceVersion: "62331"
    uid: 11d96e07-582d-4569-a84a-9d8c5229a551
  spec:
    configVersion:
      desired: rendered-worker-1930ca7433b7f0153286a3f04e4cb57b
    node:
      name: ci-ln-921r7qk-72292-kxv95-worker-a-zmxrr
    pool:
      name: worker
  status:
    conditions:
  # ...
      lastTransitionTime: 2025-04-23T14:55:31Z
      message: Update Compatible. Post Cfg Actions: [] Drain Required: true
      reason: UpdatePrepared
      status: True
      type: UpdatePrepared
  # ...
      lastTransitionTime: 2025-04-23T14:55:31Z
      message: Draining node. The drain will not be complete until desired drainer drain-rendered-worker-1930ca7433b7f0153286a3f04e4cb57b
        matches current drainer uncordon-rendered-worker-a9673968884f1ea42c26edcd914af907
      reason: UpdateExecutedDrained
      status: True
      type: Drained
  # ...
      lastTransitionTime: 2025-04-23T14:55:31Z
      message: Cordoned node. The node is reporting Unschedulable = true
      reason: UpdateExecutedCordoned
      status: True
      type: Cordoned
  # ...
    - lastTransitionTime: "2025-04-28T18:52:16Z"
      message: This node has not yet entered the NodeDegraded phase
      reason: NotYetOccurred
      status: "False"
      type: NodeDegraded
  # ...
    configversion:
      current: rendered-worker-8110974a5cea69dff5b263237b58abd8
      desired: rendered-worker-1930ca7433b7f0153286a3f04e4cb57b
    observedgeneration:  4
    pinnedImageSets:
    - desiredGeneration: 1
      name: worker-pinned-images
  # ...
  ```

### [1.7. Viewing and interacting with certificates](#checking-mco-status-certs_machine-config-overview) Copy linkLink copied to clipboard!

You can secure connections between Red Hat Enterprise Linux CoreOS (RHCOS) nodes and the Machine Config Server by viewing, interacting with, and extracting detailed information from Machine Config Operator and image registry certificates.

For more information, see "Machine Config Operator certificates".

The following certificates are handled in the cluster by the Machine Config Controller (MCC) and can be found in the `ControllerConfig` resource:

* `/etc/kubernetes/kubelet-ca.crt`
* `/etc/kubernetes/static-pod-resources/configmaps/cloud-config/ca-bundle.pem`
* `/etc/pki/ca-trust/source/anchors/openshift-config-user-ca-bundle.crt`

The MCC also handles the image registry certificates and its associated user bundle certificate.

You can get information about the listed certificates, including the underyling bundle the certificate comes from, and the signing and subject data.

**Prerequisites**

* This procedure contains optional steps that require that the `python-yq` RPM package is installed.

**Procedure**

* Get detailed certificate information by running the following command:

  ```
  $ oc get controllerconfig/machine-config-controller -o yaml | yq -y '.status.controllerCertificates'
  ```

  **Example output**

  ```
  - bundleFile: KubeAPIServerServingCAData
    notAfter: '2034-10-23T13:13:02Z'
    notBefore: '2024-10-25T13:13:02Z'
    signer: CN=admin-kubeconfig-signer,OU=openshift
    subject: CN=admin-kubeconfig-signer,OU=openshift
  - bundleFile: KubeAPIServerServingCAData
    notAfter: '2024-10-26T13:13:05Z'
    notBefore: '2024-10-25T13:27:14Z'
    signer: CN=kubelet-signer,OU=openshift
    subject: CN=kube-csr-signer_@1729862835
  - bundleFile: KubeAPIServerServingCAData
    notAfter: '2024-10-26T13:13:05Z'
    notBefore: '2024-10-25T13:13:05Z'
    signer: CN=kubelet-signer,OU=openshift
    subject: CN=kubelet-signer,OU=openshift
  # ...
  ```
* Get a simpler version of the information found in the `ControllerConfig` resource by checking the machine config pool status using the following command:

  ```
  $ oc get mcp master -o yaml | yq -y '.status.certExpirys'
  ```

  **Example output**

  ```
  - bundle: KubeAPIServerServingCAData
    expiry: '2034-10-23T13:13:02Z'
    subject: CN=admin-kubeconfig-signer,OU=openshift
  - bundle: KubeAPIServerServingCAData
    expiry: '2024-10-26T13:13:05Z'
    subject: CN=kube-csr-signer_@1729862835
  - bundle: KubeAPIServerServingCAData
    expiry: '2024-10-26T13:13:05Z'
    subject: CN=kubelet-signer,OU=openshift
  - bundle: KubeAPIServerServingCAData
    expiry: '2025-10-25T13:13:05Z'
    subject: CN=kube-apiserver-to-kubelet-signer,OU=openshift
  # ...
  ```

  This method is meant for OpenShift Container Platform applications that already consume machine config pool information.
* Check which image registry certificates are on the nodes:

  1. Log in to a node:

     ```
     $ oc debug node/<node_name>
     ```
  2. Set `/host` as the root directory within the debug shell:

     ```
     sh-5.1# chroot /host
     ```
  3. Look at the contents of the `/etc/docker/cert.d` directory:

     ```
     sh-5.1# ls /etc/docker/certs.d
     ```

     **Example output**

     ```
     image-registry.openshift-image-registry.svc.cluster.local:5000
     image-registry.openshift-image-registry.svc:5000
     ```

## [Chapter 2. Using machine config objects to configure nodes](#machine-configs-configure) Copy linkLink copied to clipboard!

You can create `MachineConfig` custom resources (CR) that modify files, systemd unit files, and other operating system features running on OpenShift Container Platform nodes. By using `MachineConfig` objects, you can perform tasks such as disabling chronyd, adding kernel arguments, enabling multipathing, and adding RHCOS extensions.

For more ideas on working with machine configs, see "How to update ssh keys after installation in OpenShift 4?", "Container image signatures", "Enabling SCTP in Openshift Container Platform 4", and "How to provide custom iSCSI initiatornames for nodes".

OpenShift Container Platform supports Ignition specification version 3.5. For more information, see "Configuration Specification v3.5.0 (Ignition documentation)". You should base all new machine configs you create going forward on Ignition specification version 3.5. If you are upgrading your OpenShift Container Platform cluster, any existing machine configs with a previous Ignition specification will be translated automatically to specification version 3.5.

There might be situations where the configuration on a node does not fully match what the currently-applied machine config specifies. This state is called *configuration drift*. The Machine Config Daemon (MCD) regularly checks the nodes for configuration drift. If the MCD detects configuration drift, the MCO marks the node `degraded` until an administrator corrects the node configuration. A degraded node is online and operational, but, it cannot be updated. For more information on configuration drift, see "Understanding configuration drift detection".

Tip

Use the following "Configuring chrony time service" procedure as a model for how to go about adding other configuration files to OpenShift Container Platform nodes.

### [2.1. Configuring chrony time service](#installation-special-config-chrony_machine-configs-configure) Copy linkLink copied to clipboard!

You can set the time server and related settings used by the chrony time service (`chronyd`) by modifying the contents of the `chrony.conf` file and passing those contents to your nodes as a machine config.

For more information on chrony best practices, see the following resources:

* [Configuring chrony (Red Hat Knowledgebase article)](https://access.redhat.com/solutions/3073261)
* [Best practices for NTP (Red Hat Knowledgebase article)](https://access.redhat.com/solutions/778603)
* [Basic chrony NTP troubleshooting (Red Hat Ceph Storage documentation)](https://docs.redhat.com/en/documentation/red_hat_ceph_storage/8/html-single/troubleshooting_guide/basic-chrony-NTP-troubleshooting_diag#basic-chrony-NTP-troubleshooting_diag)

**Procedure**

1. Create a Butane config including the contents of the `chrony.conf` file. For example, to configure chrony on worker nodes, create a `99-worker-chrony.bu` file.

   Note

   The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane.

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     name: 99-worker-chrony
     labels:
       machineconfiguration.openshift.io/role: worker
   storage:
     files:
     - path: /etc/chrony.conf
       mode: 0644
       overwrite: true
       contents:
         inline: |
           pool 0.rhel.pool.ntp.org iburst
           driftfile /var/lib/chrony/drift
           makestep 1.0 3
           rtcsync
           logdir /var/log/chrony
   ```

   * `name: 99-worker-chrony` - Specify a name for the machine config file. On control plane nodes, substitute `master` for `worker`.
   * `machineconfiguration.openshift.io/role: worker` - On control plane nodes, substitute `master` for `worker`.
   * `mode: 0644` - Specify an octal value mode for the `mode` field in the machine config file. After creating the file and applying the changes, the `mode` is converted to a decimal value. You can check the YAML file with the command `oc get mc <mc-name> -o yaml`.
   * `pool 0.rhel.pool.ntp.org iburst` - Specify any valid, reachable time source, such as the one provided by your DHCP server.

   Note

   For all-machine to all-machine communication, the Network Time Protocol (NTP) on UDP is port `123`. If an external NTP time server is configured, you must open UDP port `123`.

   Alternatively, you can specify any of the following NTP servers: `1.rhel.pool.ntp.org`, `2.rhel.pool.ntp.org`, or `3.rhel.pool.ntp.org`. When you use NTP with your DHCP server, you must set the `sourcedir /run/chrony-dhcp` parameter in the `chrony.conf` file.
2. Use Butane to generate a `MachineConfig` object file, `99-worker-chrony.yaml`, containing the configuration to be delivered to the nodes:

   ```
   $ butane 99-worker-chrony.bu -o 99-worker-chrony.yaml
   ```
3. Apply the configurations in one of two ways:

   * If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster.
   * If the cluster is already running, apply the file:

     ```
     $ oc apply -f ./99-worker-chrony.yaml
     ```

### [2.2. Disabling the chrony time service](#cnf-disable-chronyd_machine-configs-configure) Copy linkLink copied to clipboard!

You can disable the chrony time service (`chronyd`) for nodes with a specific role by using a `MachineConfig` custom resource (CR).

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

**Procedure**

1. Create the `MachineConfig` CR that disables `chronyd` for the specified node role.

   1. Save the following YAML in the `disable-chronyd.yaml` file:

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfig
      metadata:
        labels:
          machineconfiguration.openshift.io/role: <node_role>
        name: disable-chronyd
      spec:
        config:
          ignition:
            version: 3.5.0
          systemd:
            units:
              - contents: |
                  [Unit]
                  Description=NTP client/server
                  Documentation=man:chronyd(8) man:chrony.conf(5)
                  After=ntpdate.service sntp.service ntpd.service
                  Conflicts=ntpd.service systemd-timesyncd.service
                  ConditionCapability=CAP_SYS_TIME
                  [Service]
                  Type=forking
                  PIDFile=/run/chrony/chronyd.pid
                  EnvironmentFile=-/etc/sysconfig/chronyd
                  ExecStart=/usr/sbin/chronyd $OPTIONS
                  ExecStartPost=/usr/libexec/chrony-helper update-daemon
                  PrivateTmp=yes
                  ProtectHome=yes
                  ProtectSystem=full
                  [Install]
                  WantedBy=multi-user.target
                enabled: false
                name: "chronyd.service"
              - name: "kubelet-dependencies.target"
                contents: |
                  [Unit]
                  Description=Dependencies necessary to run kubelet
                  Documentation=https://github.com/openshift/machine-config-operator/
                  Requires=basic.target network-online.target
                  Wants=NetworkManager-wait-online.service crio-wipe.service
                  Wants=rpc-statd.service
      ```

      where:

      `metadata.labels`
      :   Specifies the node role where you want to disable `chronyd`, for example, `master`.
   2. Create the `MachineConfig` CR by running the following command:

      ```
      $ oc create -f disable-chronyd.yaml
      ```

### [2.3. Adding kernel arguments to nodes](#nodes-nodes-kernel-arguments_machine-configs-configure) Copy linkLink copied to clipboard!

In some special cases, you can add kernel arguments to a set of nodes in your cluster to customize the kernel behavior to meet specific needs you might have.

You should add kernel arguments with caution and a clear understanding of the implications of the arguments you set.

Warning

Improper use of kernel arguments can result in your systems becoming unbootable.

Examples of kernel arguments you could set include:

* **nosmt**: Disables symmetric multithreading (SMT) in the kernel. Multithreading allows multiple logical threads for each CPU. You could consider `nosmt` in multi-tenant environments to reduce risks from potential cross-thread attacks. By disabling SMT, you essentially choose security over performance.
* **enforcing=0**: Configures Security Enhanced Linux (SELinux) to run in permissive mode. In permissive mode, the system acts as if SELinux is enforcing the loaded security policy, including labeling objects and emitting access denial entries in the logs, but it does not actually deny any operations. While not supported for production systems, permissive mode can be helpful for debugging.

  Warning

  Disabling SELinux on RHCOS in production is not supported. After SELinux has been disabled on a node, it must be re-provisioned before re-inclusion in a production cluster.

See [Kernel.org kernel parameters](https://www.kernel.org/doc/Documentation/admin-guide/kernel-parameters.txt) for a list and descriptions of kernel arguments.

In the following procedure, you create a `MachineConfig` object that identifies:

* A set of machines to which you want to add the kernel argument. In this case, machines with a worker role.
* Kernel arguments that are appended to the end of the existing kernel arguments.
* A label that indicates where in the list of machine configs the change is applied.

**Prerequisites**

* You have `cluster-admin` privileges.
* Your cluster is running.

**Procedure**

1. List existing `MachineConfig` objects for your OpenShift Container Platform cluster to determine how to label your machine config:

   ```
   $ oc get MachineConfig
   ```

   **Example output**

   ```
   NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
   00-master                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   00-worker                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-master-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-master-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-worker-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-worker-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   99-master-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   99-master-ssh                                                                                 3.2.0             40m
   99-worker-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   99-worker-ssh                                                                                 3.2.0             40m
   rendered-master-23e785de7587df95a4b517e0647e5ab7   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   rendered-worker-5d596d9293ca3ea80c896a1191735bb1   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   ```
2. Create a `MachineConfig` object file that identifies the kernel argument (for example, `05-worker-kernelarg-selinuxpermissive.yaml`)

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfig
   metadata:
     labels:
       machineconfiguration.openshift.io/role: worker
     name: 05-worker-kernelarg-selinuxpermissive
   spec:
     kernelArguments:
       - enforcing=0
   ```

   where:

   `machineconfiguration.openshift.io/role`
   :   Specifies a label to apply changes to specific nodes.

   `name`
   :   Specifies a name to identify where it fits among the machine configs (05) and what it does (adds a kernel argument to configure SELinux permissive mode).

   `kernelArguments`
   :   Specifies the exact kernel argument as `enforcing=0`.
3. Create the new machine config:

   ```
   $ oc create -f 05-worker-kernelarg-selinuxpermissive.yaml
   ```
4. Check the machine configs to see that the new one was added:

   ```
   $ oc get MachineConfig
   ```

   **Example output**

   ```
   NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
   00-master                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   00-worker                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-master-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-master-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-worker-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-worker-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   05-worker-kernelarg-selinuxpermissive                                                         3.5.0             105s
   99-master-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   99-master-ssh                                                                                 3.2.0             40m
   99-worker-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   99-worker-ssh                                                                                 3.2.0             40m
   rendered-master-23e785de7587df95a4b517e0647e5ab7   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   rendered-worker-5d596d9293ca3ea80c896a1191735bb1   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   ```
5. Check the nodes:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                           STATUS                     ROLES    AGE   VERSION
   ip-10-0-136-161.ec2.internal   Ready                      worker   28m   v1.35.4
   ip-10-0-136-243.ec2.internal   Ready                      master   34m   v1.35.4
   ip-10-0-141-105.ec2.internal   Ready,SchedulingDisabled   worker   28m   v1.35.4
   ip-10-0-142-249.ec2.internal   Ready                      master   34m   v1.35.4
   ip-10-0-153-11.ec2.internal    Ready                      worker   28m   v1.35.4
   ip-10-0-153-150.ec2.internal   Ready                      master   34m   v1.35.4
   ```

   You can see that scheduling on each worker node is disabled as the change is being applied.
6. Check that the kernel argument worked by going to one of the worker nodes and listing the kernel command-line arguments (in `/proc/cmdline` on the host):

   ```
   $ oc debug node/ip-10-0-141-105.ec2.internal
   ```

   **Example output**

   ```
   Starting pod/ip-10-0-141-105ec2internal-debug ...
   To use host binaries, run `chroot /host`

   sh-4.2# cat /host/proc/cmdline
   BOOT_IMAGE=/ostree/rhcos-... console=tty0 console=ttyS0,115200n8
   rootflags=defaults,prjquota rw root=UUID=fd0... ostree=/ostree/boot.0/rhcos/16...
   coreos.oem.id=qemu coreos.oem.id=ec2 ignition.platform.id=ec2 enforcing=0

   sh-4.2# exit
   ```

   You should see the `enforcing=0` argument added to the other kernel arguments.

### [2.4. Enabling multipathing with kernel arguments on RHCOS](#rhcos-enabling-multipath-day-2_machine-configs-configure) Copy linkLink copied to clipboard!

You can achieve higher host availability by enabling multipathing on the primary disk, which allows stronger resilience to hardware failure, by using a `MachineConfig` object.

Important

Enabling multipathing during installation is supported and recommended for nodes provisioned in OpenShift Container Platform. In setups where any I/O to non-optimized paths results in I/O system errors, you must enable multipathing at installation time. For more information about enabling multipathing during installation time, see "Enabling multipathing post installation" in the *Installing on bare metal* documentation.

Important

On IBM Z® and IBM® LinuxONE, you can enable multipathing only if you configured your cluster for it during installation. For more information, see "Installing RHCOS and starting the OpenShift Container Platform bootstrap process" in *Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE*.

Important

When an OpenShift Container Platform cluster is installed or configured as a postinstallation activity on a single VIOS host with "vSCSI" storage on IBM Power® with multipath configured, the CoreOS nodes with multipath enabled fail to boot. This behavior is expected, as only one path is available to the node.

**Prerequisites**

* You have a running OpenShift Container Platform cluster.
* You are logged in to the cluster as a user with administrative privileges.
* You have confirmed that the disk is enabled for multipathing. Multipathing is only supported on hosts that are connected to a SAN via an HBA adapter.

**Procedure**

1. To enable multipathing postinstallation on control plane nodes:

   * Create a machine config file, such as `99-master-kargs-mpath.yaml`, that instructs the cluster to add the `master` label and that identifies the multipath kernel argument, for example:

     ```
     apiVersion: machineconfiguration.openshift.io/v1
     kind: MachineConfig
     metadata:
       labels:
         machineconfiguration.openshift.io/role: "master"
       name: 99-master-kargs-mpath
     spec:
       kernelArguments:
         - 'rd.multipath=default'
         - 'root=/dev/disk/by-label/dm-mpath-root'
     ```
2. To enable multipathing postinstallation on worker nodes:

   * Create a machine config file, such as `99-worker-kargs-mpath.yaml`, that instructs the cluster to add the `worker` label and that identifies the multipath kernel argument, for example:

     ```
     apiVersion: machineconfiguration.openshift.io/v1
     kind: MachineConfig
     metadata:
       labels:
         machineconfiguration.openshift.io/role: "worker"
       name: 99-worker-kargs-mpath
     spec:
       kernelArguments:
         - 'rd.multipath=default'
         - 'root=/dev/disk/by-label/dm-mpath-root'
     ```
3. Create the new machine config by using either the master or worker YAML file you previously created:

   ```
   $ oc create -f ./99-worker-kargs-mpath.yaml
   ```
4. Check the machine configs to see that the new one was added:

   ```
   $ oc get MachineConfig
   ```

   **Example output**

   ```
   NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
   00-master                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   00-worker                                          52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-master-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-master-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-worker-container-runtime                        52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   01-worker-kubelet                                  52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   99-master-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   99-master-ssh                                                                                 3.2.0             40m
   99-worker-generated-registries                     52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   99-worker-kargs-mpath                              52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             105s
   99-worker-ssh                                                                                 3.2.0             40m
   rendered-master-23e785de7587df95a4b517e0647e5ab7   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   rendered-worker-5d596d9293ca3ea80c896a1191735bb1   52dd3ba6a9a527fc3ab42afac8d12b693534c8c9   3.5.0             33m
   ```
5. Check the nodes:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                           STATUS                     ROLES    AGE   VERSION
   ip-10-0-136-161.ec2.internal   Ready                      worker   28m   v1.35.4
   ip-10-0-136-243.ec2.internal   Ready                      master   34m   v1.35.4
   ip-10-0-141-105.ec2.internal   Ready,SchedulingDisabled   worker   28m   v1.35.4
   ip-10-0-142-249.ec2.internal   Ready                      master   34m   v1.35.4
   ip-10-0-153-11.ec2.internal    Ready                      worker   28m   v1.35.4
   ip-10-0-153-150.ec2.internal   Ready                      master   34m   v1.35.4
   ```

   You can see that scheduling on each worker node is disabled as the change is being applied.
6. Check that the kernel argument worked by going to one of the worker nodes and listing the kernel command-line arguments (in `/proc/cmdline` on the host):

   ```
   $ oc debug node/ip-10-0-141-105.ec2.internal
   ```

   **Example output**

   ```
   Starting pod/ip-10-0-141-105ec2internal-debug ...
   To use host binaries, run `chroot /host`

   sh-4.2# cat /host/proc/cmdline
   ...
   rd.multipath=default root=/dev/disk/by-label/dm-mpath-root
   ...

   sh-4.2# exit
   ```

   You should see the added kernel arguments.

### [2.5. Adding a real-time kernel to nodes](#nodes-nodes-rtkernel-arguments_machine-configs-configure) Copy linkLink copied to clipboard!

If your OpenShift Container Platform workloads require real-time operating system characteristics, you can switch your machines to the Linux real-time kernel. Switching to the real-time kernel provides a higher degree of determinism for your OpenShift Container Platform workloads.

Even though Linux is not a real-time operating system, the Linux real-time kernel includes a preemptive scheduler that provides the operating system with real-time characteristics. For OpenShift Container Platform, 4.22 you can make the switch to real-time kernel by using a `MachineConfig` object.

Although making the change is as simple as changing a machine config `kernelType` setting to `realtime`, there are a few other considerations before making the change:

* Currently, real-time kernel is supported only on worker nodes, and only for radio access network (RAN) use.
* The following procedure is fully supported with bare metal installations that use systems that are certified for Red Hat Enterprise Linux for Real Time 8.
* Real-time support in OpenShift Container Platform is limited to specific subscriptions.
* The following procedure is also supported for use with Google Cloud.

**Prerequisites**

* Have a running OpenShift Container Platform cluster (version 4.4 or later).
* Log in to the cluster as a user with administrative privileges.

**Procedure**

1. Create a machine config for the real-time kernel: Create a YAML file (for example, `99-worker-realtime.yaml`) that contains a `MachineConfig` object for the `realtime` kernel type. This example tells the cluster to use a real-time kernel for all worker nodes:

   ```
   $ cat << EOF > 99-worker-realtime.yaml
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfig
   metadata:
     labels:
       machineconfiguration.openshift.io/role: "worker"
     name: 99-worker-realtime
   spec:
     kernelType: realtime
   EOF
   ```
2. Add the machine config to the cluster. Type the following to add the machine config to the cluster:

   ```
   $ oc create -f 99-worker-realtime.yaml
   ```
3. Check the real-time kernel: Once each impacted node reboots, log in to the cluster and run the following commands to make sure that the real-time kernel has replaced the regular kernel for the set of nodes you configured:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                                        STATUS  ROLES    AGE   VERSION
   ip-10-0-143-147.us-east-2.compute.internal  Ready   worker   103m  v1.35.4
   ip-10-0-146-92.us-east-2.compute.internal   Ready   worker   101m  v1.35.4
   ip-10-0-169-2.us-east-2.compute.internal    Ready   worker   102m  v1.35.4
   ```

   ```
   $ oc debug node/ip-10-0-143-147.us-east-2.compute.internal
   ```

   **Example output**

   ```
   Starting pod/ip-10-0-143-147us-east-2computeinternal-debug ...
   To use host binaries, run `chroot /host`

   sh-4.4# uname -a
   Linux <worker_node> 4.18.0-147.3.1.rt24.96.el8_1.x86_64 #1 SMP PREEMPT RT
           Wed Nov 27 18:29:55 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
   ```

   The kernel name contains `rt` and text “PREEMPT RT” indicates that this is a real-time kernel.
4. To go back to the regular kernel, delete the `MachineConfig` object:

   ```
   $ oc delete -f 99-worker-realtime.yaml
   ```

### [2.6. Configuring journald settings](#machineconfig-modify-journald_machine-configs-configure) Copy linkLink copied to clipboard!

To configure settings for the `journald` service on OpenShift Container Platform nodes, you can modify the appropriate configuration file and pass the file to the appropriate pool of nodes as a machine config.

This procedure describes how to modify `journald` rate limiting settings in the `/etc/systemd/journald.conf` file and apply them to worker nodes. See the `journald.conf` man page for information on how to use that file.

**Prerequisites**

* Have a running OpenShift Container Platform cluster.
* Log in to the cluster as a user with administrative privileges.

**Procedure**

1. Create a Butane config file, `40-worker-custom-journald.bu`, that includes an `/etc/systemd/journald.conf` file with the required settings.

   Note

   The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane.

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     name: 40-worker-custom-journald
     labels:
       machineconfiguration.openshift.io/role: worker
   storage:
     files:
     - path: /etc/systemd/journald.conf
       mode: 0644
       overwrite: true
       contents:
         inline: |
           # Disable rate limiting
           RateLimitInterval=1s
           RateLimitBurst=10000
           Storage=volatile
           Compress=no
           MaxRetentionSec=30s
   ```
2. Use Butane to generate a `MachineConfig` object file, `40-worker-custom-journald.yaml`, containing the configuration to be delivered to the worker nodes:

   ```
   $ butane 40-worker-custom-journald.bu -o 40-worker-custom-journald.yaml
   ```
3. Apply the machine config to the pool:

   ```
   $ oc apply -f 40-worker-custom-journald.yaml
   ```
4. Check that the new machine config is applied and that the nodes are not in a degraded state. It might take a few minutes. The worker pool will show the updates in progress, as each node successfully has the new machine config applied:

   ```
   $ oc get machineconfigpool
   ```

   **Example output**

   ```
   NAME   CONFIG             UPDATED UPDATING DEGRADED MACHINECOUNT READYMACHINECOUNT UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE
   master rendered-master-35 True    False    False    3            3                 3                   0                    34m
   worker rendered-worker-d8 False   True     False    3            1                 1                   0                    34m
   ```
5. To check that the change was applied, you can log in to a worker node:

   ```
   $ oc get node | grep worker
   ```

   **Example output**

   ```
   ip-10-0-0-1.us-east-2.compute.internal   Ready    worker   39m   v0.0.0-master+$Format:%h$
   ```

   ```
   $ oc debug node/ip-10-0-0-1.us-east-2.compute.internal
   ```

   **Example output**

   ```
   Starting pod/ip-10-0-141-142us-east-2computeinternal-debug ...
   ...
   sh-4.2# chroot /host
   sh-4.4# cat /etc/systemd/journald.conf
   # Disable rate limiting
   RateLimitInterval=1s
   RateLimitBurst=10000
   Storage=volatile
   Compress=no
   MaxRetentionSec=30s
   sh-4.4# exit
   ```

### [2.7. Adding extensions to RHCOS](#rhcos-add-extensions_machine-configs-configure) Copy linkLink copied to clipboard!

You can add software packages to Red Hat Enterprise Linux CoreOS (RHCOS) systems by using extension packages to add a minimal set of features to specific nodes.

RHCOS is a minimal container-oriented op-system-base-full operating system, designed to provide a common set of capabilities to OpenShift Container Platform clusters across all platforms. Although adding software packages to RHCOS systems is generally discouraged, you can add any of the following extensions to extend RHCOS:

* **usbguard**: The `usbguard` extension protects RHCOS systems from attacks by intrusive USB devices. For `usbguard`, you must create additional `MachineConfig` objects to start and enable the services as described in the following procedure. For more information, see [USBGuard](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/security_hardening/index#usbguard_protecting-systems-against-intrusive-usb-devices).
* **kerberos**: The `kerberos` extension provides a mechanism that allows both users and machines to identify themselves to the network to receive defined, limited access to the areas and services that an administrator has configured. For more information, see [Using Kerberos](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/system-level_authentication_guide/using_kerberos), including how to set up a Kerberos client and mount a Kerberized NFS share.
* **sandboxed-containers**: The `sandboxed-containers` extension contains RPMs for Kata, QEMU, and its dependencies. For more information, see [OpenShift Sandboxed Containers](https://docs.redhat.com/en/documentation/openshift_sandboxed_containers/latest).
* **ipsec**: The `ipsec` extension contains RPMs for libreswan and NetworkManager-libreswan.
* **wasm**: The `wasm` extension enables Developer Preview functionality in OpenShift Container Platform for users who want to use WASM-supported workloads.
* **sysstat**: Adding the `sysstat` extension provides additional performance monitoring for OpenShift Container Platform nodes, including the system activity reporter (`sar`) command for collecting and reporting information.
* **kernel-devel**: The `kernel-devel` extension provides kernel headers and makefiles sufficient to build modules against the kernel package.

The following procedure describes how to use a machine config to add one or more extensions to your RHCOS nodes.

**Prerequisites**

* Have a running OpenShift Container Platform cluster (version 4.6 or later).
* Log in to the cluster as a user with administrative privileges.

**Procedure**

1. Create a Butane configuration file named `80-worker-usbguard.bu` to add the extension, manage the configuration files, and enable the service.

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     name: 80-worker-usbguard
     labels:
       machineconfiguration.openshift.io/role: worker
   extensions:
     - usbguard
   storage:
     files:
       - path: /etc/usbguard/usbguard-daemon.conf
         mode: 0600
         overwrite: true
         contents:
           inline: |
             RuleFile=/etc/usbguard/rules.conf
             PresentDevicePolicy=apply-policy
             IPCAllowedGroups=wheel
       - path: /etc/usbguard/rules.conf
         mode: 0600
         overwrite: false
         contents:
           inline: |
             allow id 1d6b:0002 serial "0000:00:14.0" name "EHCI Host Controller"
   systemd:
     units:
       - name: usbguard.service
         enabled: true
   ```
2. Convert the Butane configuration into a `MachineConfig` manifest by entering the following command:

   ```
   $ butane 80-worker-usbguard.bu -o 80-worker-usbguard.yaml
   ```
3. Apply the `MachineConfig` to the cluster by entering the following command:

   ```
   $ oc apply -f 80-worker-usbguard.yaml
   ```

   This sets all compute nodes to install the `usbguard` RPM package, write the required configuration files, and enable the systemd daemon within a single node rollout cycle.

**Verification**

1. Check that the new machine config was successfully created by entering the following command:

   ```
   $ oc get machineconfig 80-worker-usbguard
   ```

   **Example output**

   ```
   NAME                GENERATEDBYCONTROLLER IGNITIONVERSION AGE
   80-worker-usbguard                        3.5.0           57s
   ```
2. Check that the machine config is now applied and that the nodes are not in a degraded state. This operation might take a few minutes. The worker pool will show the updates in progress, as each machine successfully has the new machine config applied:

   ```
   $ oc get machineconfigpool
   ```

   **Example output**

   ```
   NAME   CONFIG             UPDATED UPDATING DEGRADED MACHINECOUNT READYMACHINECOUNT UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE
   master rendered-master-35 True    False    False    3            3                 3                   0                    34m
   worker rendered-worker-d8 False   True     False    3            1                 1                   0                    34m
   ```
3. After the pool reports `UPDATED` as `True`, verify that the extension package was installed and that the service is running normally by debugging a compute node. You can complete these tasks by running the following commands:

   ```
   $ oc get node | grep worker
   ```

   **Example output**

   ```
   NAME                                        STATUS  ROLES    AGE   VERSION
   ip-10-0-169-2.us-east-2.compute.internal    Ready   worker   102m  v1.35.4
   ```

   ```
   $ oc debug node/ip-10-0-169-2.us-east-2.compute.internal
   ```

   **Example output**

   ```
   ...
   To use host binaries, run `chroot /host`
   sh-4.4# chroot /host
   sh-4.4# rpm -q usbguard
   usbguard-0.7.4-4.el8.x86_64.rpm
   ...
   sh-4.4# systemctl status usbguard.service
   usbguard.service - USBGuard daemon
           Loaded: loaded (/usr/lib/systemd/system/usbguard.service; enabled; preset: disabled)
           Active: active (running)
   ```

### [2.8. Loading custom firmware blobs in the machine config manifest](#rhcos-load-firmware-blobs_machine-configs-configure) Copy linkLink copied to clipboard!

You can load local firmware blobs that are not managed by RHCOS into the machine config manifest by updating the search path with a machine config.

By default, the location for firmware blobs in `/usr/lib` is read-only.

**Procedure**

1. Create a Butane config file, `98-worker-firmware-blob.bu`, that updates the search path so that it is root-owned and writable to local storage. The following example places the custom blob file from your local workstation onto nodes under `/var/lib/firmware`.

   Note

   The [Butane version](https://coreos.github.io/butane/specs/) you specify in the config file should match the OpenShift Container Platform version and always ends in `0`. For example, `4.22.0`. See "Creating machine configs with Butane" for information about Butane.

   **Butane config file for custom firmware blob**

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     labels:
       machineconfiguration.openshift.io/role: worker
     name: 98-worker-firmware-blob
   storage:
     files:
     - path: /var/lib/firmware/<package_name>
       contents:
         local: <package_name>
       mode: 0644
   openshift:
     kernel_arguments:
       - 'firmware_class.path=/var/lib/firmware'
   ```

   where:

   `storage.files.path`
   :   Specifies the path on the node where the firmware package is copied to.

   `storage.files.contents.local`
   :   Specifies a file with contents that are read from a local file directory on the system running Butane. The path of the local file is relative to a `files-dir` directory, which must be specified by using the `--files-dir` option with Butane in a subsequent step.

   `storage.files.mode`
   :   Specifies the permissions for the file on the RHCOS node. Red Hat recommends setting `0644` permissions.

   `openshift.kernel_arguments`
   :   Specifies the kernel search path of where to look for the custom firmware blob that was copied from your local workstation onto the root file system of the node. This example uses `/var/lib/firmware` as the customized path.
2. Run Butane to generate a `MachineConfig` object file that uses a copy of the firmware blob on your local workstation named `98-worker-firmware-blob.yaml`. The firmware blob contains the configuration to be delivered to the nodes. The following example uses the `--files-dir` option to specify the directory on your workstation where the local file or files are located:

   ```
   $ butane 98-worker-firmware-blob.bu -o 98-worker-firmware-blob.yaml --files-dir <directory_including_package_name>
   ```
3. Apply the configurations to the nodes in one of two ways:

   * If the cluster is not running yet, after you generate manifest files, add the `MachineConfig` object file to the `<installation_directory>/openshift` directory, and then continue to create the cluster.
   * If the cluster is already running, apply the file:

     ```
     $ oc apply -f 98-worker-firmware-blob.yaml
     ```

     A `MachineConfig` object YAML file is created for you to finish configuring your machines.
4. Save the Butane config in case you need to update the `MachineConfig` object in the future.

### [2.9. Changing the core user password for node access](#core-user-password_machine-configs-configure) Copy linkLink copied to clipboard!

You can use the default `core` user to access a node through a cloud provider serial console or a bare metal baseboard controller manager (BMC) if a node is down and you cannot access that node by using SSH or the `oc debug node` command.

By default, Red Hat Enterprise Linux CoreOS (RHCOS) creates a user named `core` on the nodes in your cluster. However, there is no password for this user. As such, you cannot log in with this user without creating a password by using a machine config. The Machine Config Operator (MCO) assigns the password and injects the password into the `/etc/shadow` file, allowing you to log in with the `core` user. The MCO does not examine the password hash. As such, the MCO cannot report if there is a problem with the password.

Note

* The password works only through a cloud provider serial console or a BMC. It does not work with SSH.
* If you have a machine config that includes an `/etc/shadow` file or a systemd unit that sets a password, it takes precedence over the password hash.

You can change the password, if needed, by editing the machine config you used to create the password. Also, you can remove the password by deleting the machine config. Deleting the machine config does not remove the user account.

**Procedure**

1. Using a tool that is supported by your operating system, create a hashed password. For example, create a hashed password using `mkpasswd` by running the following command:

   ```
   $ mkpasswd -m SHA-512 testpass
   ```

   **Example output**

   ```
   $ $6$CBZwA6s6AVFOtiZe$aUKDWpthhJEyR3nnhM02NM1sKCpHn9XN.NPrJNQ3HYewioaorpwL3mKGLxvW0AOb4pJxqoqP4nFX77y0p00.8.
   ```
2. Create a machine config file that contains the `core` username and the hashed password:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfig
   metadata:
     labels:
       machineconfiguration.openshift.io/role: worker
     name: set-core-user-password
   spec:
     config:
       ignition:
         version: 3.5.0
       passwd:
         users:
         - name: core
           passwordHash: <password>
   ```

   where:

   `spec.config.passwd.users.name`
   :   Specifies the user name. This must be `core`.

   `spec.config.passwd.users.passwordHash`
   :   Specifies the hashed password to use with the `core` account.
3. Create the machine config by running the following command:

   ```
   $ oc create -f <file-name>.yaml
   ```

   The nodes do not reboot and should become available in a few moments. You can use the `oc get mcp` to watch for the machine config pools to be updated, as shown in the following example:

   ```
   NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   master   rendered-master-d686a3ffc8fdec47280afec446fce8dd   True      False      False      3              3                   3                     0                      64m
   worker   rendered-worker-4605605a5b1f9de1d061e9d350f251e5   False     True       False      3              0                   0                     0                      64m
   ```

**Verification**

1. After the nodes return to the `UPDATED=True` state, start a debug session for a node by running the following command:

   ```
   $ oc debug node/<node_name>
   ```
2. Set `/host` as the root directory within the debug shell by running the following command:

   ```
   sh-4.4# chroot /host
   ```
3. Check the contents of the `/etc/shadow` file:

   **Example output**

   ```
   ...
   core:$6$2sE/010goDuRSxxv$o18K52wor.wIwZp:19418:0:99999:7:::
   ...
   ```

   The hashed password is assigned to the `core` user.

### [2.10. Overriding storage or partition setup](#machine-config-install-time-configs_machine-configs-configure) Copy linkLink copied to clipboard!

You can use a `MachineConfig` object to change the disk partition schema, file systems, and RAID configurations that were established during the cluster installation. This allows you to make specific configuration changes that are different from the initial cluster state.

If you specified storage and partition configuration upon cluster installation by using a Butane config, Ignition config, or machine config, those configurations become defaults within your cluster. If you create new nodes, those nodes automatically use those default configurations.

You cannot change these components directly. By default, the Machine Config Operator (MCO) reviews changes in `MachineConfig` objects for specific fields and blocks some changes for security reasons. However, you can override this restriction for disk partition schema, file systems, and RAID configurations by adding the `irreconcilableValidationOverrides` parameter to the `MachineConfiguration` object. Then, you can create a new machine config to make the necessary changes for new nodes.

Note

Configuration changes made through this process apply to new nodes only.

For example, you might want to override your default storage configuration to add new hardware that uses a different storage partitioning schema or storage file system to your cluster. In this case, you can modify the storage configuration for any new nodes in your cluster.

Or, if you used Ignition to modify the storage configuration as a post-installation task, your cluster might be reporting an `irreconcilableChanges` status in the `MachineConfigNode` object status fields. This messaging can alert you to these differences, so that you can determine if you want new hardware with the new configurations.

Important

Overriding irreconcilable fields is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

**Prerequisites**

* You enabled the required Technology Preview features for your cluster by adding the `TechPreviewNoUpgrade` feature set to the `FeatureGate` CR named `cluster`. For information about enabling Feature Gates, see *Enabling features using feature gates*.

  Warning

  Enabling the `TechPreviewNoUpgrade` feature set on your cluster cannot be undone and prevents minor version updates. This feature set allows you to enable these Technology Preview features on test clusters, where you can fully test them. Do not enable this feature set on production clusters.

**Procedure**

1. Edit the `MachineConfiguration` object by using the following command:

   ```
   $ oc edit machineconfiguration
   ```
2. Add the `irreconcilableValidationOverrides` stanza to the `MachineConfiguration` object.

   ```
   apiVersion: operator.openshift.io/v1
   kind: MachineConfiguration
   # ...
   spec:
     irreconcilableValidationOverrides:
       storage:
       - Disks
       - Raid
       - FileSystems
   # ...
   ```

   where:

   `spec.irreconcilableValidationOverrides.storage.Disks`
   :   Allows you to modify the installed storage disk configuration to be used with new nodes. This field is optional.

   `spec.irreconcilableValidationOverrides.storage.Raid`
   :   Allows you to modify the installed RAID configuration to be used with new nodes. This field is optional.

   `spec.irreconcilableValidationOverrides.storage.FileSystems`
   :   Allows you to modify the installed file system configuration to be used with new nodes. This field is optional.
3. Create a YAML file for a `MachineConfig` object with the changes that you need, similar to the following:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfig
   metadata:
     labels:
       machineconfiguration.openshift.io/role: worker
     name: extra-disks
   spec:
     config:
       ignition:
         version: "3.5.0"
       storage:
         disks:
         - device: "/dev/sdb"
           wipeTable: true
           partitions:
           - label: raid.1.1
             number: 1
             sizeMiB: 1024
             startMiB: 0
         - device: "/dev/sdc"
           wipeTable: true
           partitions:
           - label: raid.1.2
             number: 1
             sizeMiB: 1024
             startMiB: 0
         raid:
         - devices:
           - "/dev/disk/by-partlabel/raid.1.1"
           - "/dev/disk/by-partlabel/raid.1.2"
           level: stripe
           name: data
         filesystems:
         - device: "/dev/md/data"
           path: "/var/lib/data"
           format: ext4
           label: DATA
   ```

   where:

   `spec.config.storage.disks`
   :   Specifies changes to the installed storage disk configuration in Ignition format. This field is optional.

   `spec.config.storage.raid`
   :   Specifies changes to the installed RAID configuration in Ignition format. This field is optional.

   `spec.config.storage.filesystems`
   :   Specifies changes to the installed file system configuration in Ignition format. This field is optional.
4. Create the `MachineConfig` object by using a command similar to the following:

   ```
   $ oc create -f <file_name>.yaml
   ```

   When you create a new node from a machine set with the associated label, the new configurations are applied to the node.

## [Chapter 3. Using node disruption policies to minimize disruption from machine config changes](#machine-config-node-disruption_machine-configs-configure) Copy linkLink copied to clipboard!

You can create a *node disruption policy* to define the configuration changes that cause a disruption to your cluster, and which changes do not.

Note

Node disruption policies are not supported for on-cluster custom layered images.

By default, when you make certain changes to the Ignition config objects fields by using a `MachineConfig` object, the Machine Config Operator (MCO) drains and reboots the nodes associated with that machine config.

By using a node disruption policy, you can define the configuration changes that require actions such as node reboots, node drains, or service restarts, and which changes do not. This reduces node downtime when making small machine configuration changes in your cluster. To configure the policy, you modify the `MachineConfiguration` object, which is in the `openshift-machine-config-operator` namespace. See the example node disruption policies in the `MachineConfiguration` objects in "Example node disruption policies".

Note

There are machine configuration changes that always require a reboot, regardless of any node disruption policies. For more information, see *About the Machine Config Operator*.

After you create the node disruption policy, the MCO validates the policy to search for potential issues in the file, such as problems with formatting. The MCO then merges the policy with the cluster defaults and populates the `status.nodeDisruptionPolicyStatus` fields in the machine config with the actions to be performed upon future changes to the machine config. The configurations in your policy always overwrite the cluster defaults.

Important

The MCO does not validate whether a change can be successfully applied by your node disruption policy. Therefore, you are responsible to ensure the accuracy of your node disruption policies.

For example, you can configure a node disruption policy so that sudo configurations do not require a node drain and reboot. Or, you can configure your cluster so that updates to `sshd` are applied with only a reload of that one service.

You can control the behavior of the MCO when making the changes to the following Ignition configuration objects:

* **configuration files**: You add to or update the files in the `/var` or `/etc` directory. You can configure a policy for a specific file anywhere in the directory or for a path to a specific directory. For a path, a change or addition to any file in that directory triggers the policy.

  Note

  If a file is included in more than one policy, only the policy with the best match to that file is applied.

  For example, if you have a policy for the `/etc/` directory and a policy for the `/etc/pki/` directory, a change to the `/etc/pki/tls/certs/ca-bundle.crt` file would apply the `etc/pki` policy.
* **systemd units**: You create and set the status of a systemd service or modify a systemd service.
* **users and groups**: You change SSH keys in the `passwd` section postinstallation.
* **ICSP**, **ITMS**, **IDMS** objects: You can remove mirroring rules from an `ImageContentSourcePolicy` (ICSP), `ImageTagMirrorSet` (ITMS), and `ImageDigestMirrorSet` (IDMS) object.

When you make any of these changes, the node disruption policy determines which of the following actions are required when the MCO implements the changes:

* **Reboot**: The MCO drains and reboots the nodes. This is the default behavior.
* **None**: The MCO does not drain or reboot the nodes. The MCO applies the changes with no further action.
* **Drain**: The MCO cordons and drains the nodes of their workloads. The workloads restart with the new configurations.
* **Reload**: For services, the MCO reloads the specified services without restarting the service.
* **Restart**: For services, the MCO fully restarts the specified services.
* **DaemonReload**: The MCO reloads the systemd manager configuration.
* **Special**: This is an internal MCO-only action and cannot be set by the user.

Note

* The `Reboot` and `None` actions cannot be used with any other actions, as the `Reboot` and `None` actions override the others.
* Actions are applied in the order that they are set in the node disruption policy list.
* If you make other machine config changes that do require a reboot or other disruption to the nodes, that reboot supercedes the node disruption policy actions.

### [3.1. Example node disruption policies](#machine-config-node-disruption-example_machine-configs-configure) Copy linkLink copied to clipboard!

The following example `MachineConfiguration` objects contain a node disruption policy.

Tip

A `MachineConfiguration` object and a `MachineConfig` object are different objects. A `MachineConfiguration` object is a singleton object in the MCO namespace that contains configuration parameters for the MCO operator. A `MachineConfig` object defines changes that are applied to a machine config pool.

The following example `MachineConfiguration` object shows no user defined policies. The default node disruption policy values are shown in the `status` stanza.

**Default node disruption policy**

```
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
spec:
  logLevel: Normal
  managementState: Managed
  operatorLogLevel: Normal
status:
  nodeDisruptionPolicyStatus:
    clusterPolicies:
      files:
      - actions:
        - type: None
        path: /etc/mco/internal-registry-pull-secret.json
      - actions:
        - type: None
        path: /var/lib/kubelet/config.json
      - actions:
        - reload:
            serviceName: crio.service
          type: Reload
        path: /etc/machine-config-daemon/no-reboot/containers-gpg.pub
      - actions:
        - reload:
            serviceName: crio.service
          type: Reload
        path: /etc/containers/policy.json
      - actions:
        - type: Special
        path: /etc/containers/registries.conf
      - actions:
        - reload:
            serviceName: crio.service
          type: Reload
        path: /etc/containers/registries.d
      - actions:
        - type: None
        path: /etc/nmstate/openshift
      - actions:
        - restart:
            serviceName: coreos-update-ca-trust.service
          type: Restart
        - restart:
            serviceName: crio.service
          type: Restart
        path: /etc/pki/ca-trust/source/anchors/openshift-config-user-ca-bundle.crt
      sshkey:
        actions:
        - type: None
  observedGeneration: 9
```

The default node disruption policy does not contain a policy for changes to the `/etc/containers/registries.conf.d` file. This is because both OpenShift Container Platform and Red Hat Enterprise Linux (RHEL) use the `registries.conf.d` file to specify aliases for image short names. It is recommended that you always pull an image by its fully-qualified name. This is particularly important with public registries, because the image might not deploy if the public registry requires authentication. You can create a user-defined policy to use with the `/etc/containers/registries.conf.d` file, if you need to use image short names.

In the following example, when changes are made to the SSH keys, the MCO drains the cluster nodes, reloads the `crio.service`, reloads the systemd configuration, and restarts the `crio-service`.

**Example node disruption policy for an SSH key change**

```
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  nodeDisruptionPolicy:
    sshkey:
      actions:
      - type: Drain
      - reload:
          serviceName: crio.service
        type: Reload
      - type: DaemonReload
      - restart:
          serviceName: crio.service
        type: Restart
# ...
```

In the following example, when changes are made to the `/etc/chrony.conf` file, the MCO restarts the `chronyd.service` on the cluster nodes. If files are added to or modified in the `/var/run` directory, the MCO applies the changes with no further action.

**Example node disruption policy for a configuration file change**

```
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  nodeDisruptionPolicy:
    files:
    - actions:
      - restart:
          serviceName: chronyd.service
        type: Restart
      path: /etc/chrony.conf
    - actions:
      - type: None
      path: /var/run
```

In the following example, when changes are made to the `auditd.service` systemd unit, the MCO drains the cluster nodes, reloads the `crio.service`, reloads the systemd manager configuration, and restarts the `crio.service`.

**Example node disruption policy for a systemd unit change**

```
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  nodeDisruptionPolicy:
    units:
      - name: auditd.service
        actions:
          - type: Drain
          - type: Reload
            reload:
              serviceName: crio.service
          - type: DaemonReload
          - type: Restart
            restart:
              serviceName: crio.service
```

In the following example, when changes are made to the `registries.conf` file, such as by editing an `ImageContentSourcePolicy` (ICSP) object, the MCO does not drain or reboot the nodes and applies the changes with no further action.

**Example node disruption policy for a registries.conf file change**

```
apiVersion: operator.openshift.io/v1
kind: MachineConfiguration
metadata:
  name: cluster
# ...
spec:
  nodeDisruptionPolicy:
    files:
      - actions:
        - type: None
        path: /etc/containers/registries.conf
```

### [3.2. Configuring node restart behaviors upon machine config changes](#machine-config-node-disruption-config_machine-configs-configure) Copy linkLink copied to clipboard!

You can create a node disruption policy to define the machine configuration changes that cause a disruption to your cluster, and which changes do not.

You can control how your nodes respond to changes in the files in the `/var` or `/etc` directory, the systemd units, the SSH keys, and the `registries.conf` file.

When you make any of these changes, the node disruption policy determines which of the following actions are required when the MCO implements the changes:

* **Reboot**: The MCO drains and reboots the nodes. This is the default behavior.
* **None**: The MCO does not drain or reboot the nodes. The MCO applies the changes with no further action.
* **Drain**: The MCO cordons and drains the nodes of their workloads. The workloads restart with the new configurations.
* **Reload**: For services, the MCO reloads the specified services without restarting the service.
* **Restart**: For services, the MCO fully restarts the specified services.
* **DaemonReload**: The MCO reloads the systemd manager configuration.
* **Special**: This is an internal MCO-only action and cannot be set by the user.

Note

* The `Reboot` and `None` actions cannot be used with any other actions, as the `Reboot` and `None` actions override the others.
* Actions are applied in the order that they are set in the node disruption policy list.
* If you make other machine config changes that do require a reboot or other disruption to the nodes, that reboot supercedes the node disruption policy actions.

**Procedure**

1. Edit the `machineconfigurations.operator.openshift.io` object to define the node disruption policy:

   ```
   $ oc edit MachineConfiguration cluster -n openshift-machine-config-operator
   ```
2. Add a node disruption policy similar to the following:

   ```
   apiVersion: operator.openshift.io/v1
   kind: MachineConfiguration
   metadata:
     name: cluster
   # ...
   spec:
     nodeDisruptionPolicy:
       files:
       - actions:
         - restart:
             serviceName: chronyd.service
           type: Restart
         path: /etc/chrony.conf
       sshkey:
         actions:
         - type: Drain
         - reload:
             serviceName: crio.service
           type: Reload
         - type: DaemonReload
         - restart:
             serviceName: crio.service
           type: Restart
       units:
       - actions:
         - type: Drain
         - reload:
             serviceName: crio.service
           type: Reload
         - type: DaemonReload
         - restart:
             serviceName: crio.service
           type: Restart
         name: test.service
   ```

   where:

   `spec.nodeDisruptionPolicy`
   :   Specifies the node disruption policy.

   `spec.nodeDisruptionPolicy.files`
   :   Specifies a list of machine config file definitions and actions to take to changes on those paths. This list supports a maximum of 50 entries.

   `spec.nodeDisruptionPolicy.files.actions`
   :   Specifies the series of actions to be executed upon changes to the specified files. Actions are applied in the order that they are set in this list. This list supports a maximum of 10 entries. Specify the following parameters:

       `restart`. Specifies that the listed service is to be reloaded upon changes to the specified files. `restart.serviceName`. Specifies the full name of the service to be acted upon.

   `spec.nodeDisruptionPolicy.files.path`
   :   Specifies the location of a file that is managed by a machine config. The actions in the policy apply when changes are made to the file in `path`.

   `spec.nodeDisruptionPolicy.sshkey`
   :   Specifies a list of service names and actions to take upon changes to the SSH keys in the cluster.

   `spec.nodeDisruptionPolicy.units`
   :   Specifies a list of systemd unit names and actions to take upon changes to those units.

**Verification**

* View the `MachineConfiguration` object file that you created:

  ```
  $ oc get MachineConfiguration/cluster -o yaml
  ```

  **Example output**

  ```
  apiVersion: operator.openshift.io/v1
  kind: MachineConfiguration
  metadata:
    labels:
      machineconfiguration.openshift.io/role: worker
    name: cluster
  # ...
  status:
    nodeDisruptionPolicyStatus:
      clusterPolicies:
        files:
  # ...
        - actions:
          - restart:
              serviceName: chronyd.service
            type: Restart
          path: /etc/chrony.conf
        sshkey:
          actions:
          - type: Drain
          - reload:
              serviceName: crio.service
            type: Reload
          - type: DaemonReload
          - restart:
              serviceName: crio.service
            type: Restart
        units:
        - actions:
          - type: Drain
          - reload:
              serviceName: crio.service
            type: Reload
          - type: DaemonReload
          - restart:
              serviceName: crio.service
            type: Restart
          name: test.se
  # ...
  ```

  The `nodeDisruptionPolicyStatus` parameter specifies the current cluster-validated policies.

## [Chapter 4. Configuring MCO-related custom resources](#machine-configs-custom) Copy linkLink copied to clipboard!

In addition to `MachineConfig` objects, you can use `KubeletConfig` or `ContainerRuntimeConfig` custom resources to change node-level settings that impact how the kubelet and CRI-O container runtime services behave.

The kubelet configuration is currently serialized as an Ignition configuration, so it can be directly edited. However, there is also a new `kubelet-config-controller` added to the Machine Config Controller (MCC). This lets you use a `KubeletConfig` custom resource (CR) to edit the kubelet parameters.

### [4.1. Creating a KubeletConfig CR to edit kubelet parameters](#create-a-kubeletconfig-crd-to-edit-kubelet-parameters_machine-configs-custom) Copy linkLink copied to clipboard!

You can use a `KubeletConfig` custom resource (CR) to edit a kubelet parameters without modifing the kubelet configuration directly.

Note

As the fields in the `kubeletConfig` object are passed directly to the kubelet from upstream Kubernetes, the kubelet validates those values directly. Invalid values in the `kubeletConfig` object might cause cluster nodes to become unavailable. For valid values, see the [Kubernetes documentation](https://kubernetes.io/docs/reference/config-api/kubelet-config.v1beta1/).

Consider the following guidance:

* Edit an existing `KubeletConfig` CR to modify existing settings or add new settings, instead of creating a CR for each change. It is recommended that you create a CR only to modify a different machine config pool, or for changes that are intended to be temporary, so that you can revert the changes.
* Create one `KubeletConfig` CR for each machine config pool with all the config changes you want for that pool.
* As needed, create multiple `KubeletConfig` CRs with a limit of 10 per cluster. For the first `KubeletConfig` CR, the Machine Config Operator (MCO) creates a machine config appended with `kubelet`. With each subsequent CR, the controller creates another `kubelet` machine config with a numeric suffix. For example, if you have a `kubelet` machine config with a `-2` suffix, the next `kubelet` machine config is appended with `-3`.

Note

If you are applying a kubelet or container runtime config to a custom machine config pool, the custom role in the `machineConfigSelector` must match the name of the custom machine config pool.

For example, because the following custom machine config pool is named `infra`, the custom role must also be `infra`:

```
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfigPool
metadata:
  name: infra
spec:
  machineConfigSelector:
    matchExpressions:
      - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,infra]}
# ...
```

If you want to delete the machine configs, delete them in reverse order to avoid exceeding the limit. For example, you delete the `kubelet-3` machine config before deleting the `kubelet-2` machine config.

Note

If you have a machine config with a `kubelet-9` suffix, and you create another `KubeletConfig` CR, a new machine config is not created, even if there are fewer than 10 `kubelet` machine configs.

The following example command and output show a `KubeletConfig` CR:

```
$ oc get kubeletconfig
```

```
NAME                      AGE
set-kubelet-config        15m
```

The following example command and output show a `KubeletConfig` machine config:

```
$ oc get mc | grep kubelet
```

```
...
99-worker-generated-kubelet-1                  b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             26m
...
```

The following procedure is an example to show how to configure the maximum number of pods per node, the maximum PIDs per node, and the maximum container log size size on the worker nodes.

**Prerequisites**

1. Obtain the label associated with the static `MachineConfigPool` CR for the type of node you want to configure. Perform one of the following steps:

   1. View the machine config pool:

      ```
      $ oc describe machineconfigpool <name>
      ```

      For example:

      ```
      $ oc describe machineconfigpool worker
      ```

      **Example output**

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfigPool
      metadata:
        creationTimestamp: 2019-02-08T14:52:39Z
        generation: 1
        labels:
          custom-kubelet: set-kubelet-config
      ```

      The `metadata.labels` parameter specifies labels you can use with a `KubeletConfig` CR.
   2. If the label is not present, add a key/value pair:

      ```
      $ oc label machineconfigpool worker custom-kubelet=set-kubelet-config
      ```

**Procedure**

1. View the available machine configuration objects that you can select:

   ```
   $ oc get machineconfig
   ```

   By default, the two kubelet-related configs are `01-master-kubelet` and `01-worker-kubelet`.
2. Check the current value for the maximum pods per node:

   ```
   $ oc describe node <node_name>
   ```

   For example:

   ```
   $ oc describe node ci-ln-5grqprb-f76d1-ncnqq-worker-a-mdv94
   ```

   Look for `value: pods: <value>` in the `Allocatable` stanza:

   **Example output**

   ```
   Allocatable:
    attachable-volumes-aws-ebs:  25
    cpu:                         3500m
    hugepages-1Gi:               0
    hugepages-2Mi:               0
    memory:                      15341844Ki
    pods:                        250
   ```
3. Configure the worker nodes as needed:

   1. Create a YAML file similar to the following that contains the kubelet configuration:

      Important

      Kubelet configurations that target a specific machine config pool also affect any dependent pools. For example, creating a kubelet configuration for the pool containing worker nodes will also apply to any subset pools, including the pool containing infrastructure nodes. To avoid this, you must create a new machine config pool with a selection expression that only includes worker nodes, and have your kubelet configuration target this new pool.

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: KubeletConfig
      metadata:
        name: set-kubelet-config
      spec:
        machineConfigPoolSelector:
          matchLabels:
            custom-kubelet: set-kubelet-config
        kubeletConfig:
            podPidsLimit: 8192
            containerLogMaxSize: 50Mi
            maxPods: 500
      ```

      where:

      `spec.machineConfigPoolSelector.matchLabels`
      :   Specifies the label from the machine config pool.

      `spec.kubeletConfig`
      :   Specifies the kubelet configuration. For example:

          * Use `podPidsLimit` to set the maximum number of PIDs in any pod.
          * Use `containerLogMaxSize` to set the maximum size of the container log file before it is rotated.
          * Use `maxPods` to set the maximum pods per node.

            Note

            The rate at which the kubelet talks to the API server depends on queries per second (QPS) and burst values. The default values, `50` for `kubeAPIQPS` and `100` for `kubeAPIBurst`, are sufficient if there are limited pods running on each node. It is recommended to update the kubelet QPS and burst rates if there are enough CPU and memory resources on the node.

            ```
            apiVersion: machineconfiguration.openshift.io/v1
            kind: KubeletConfig
            metadata:
              name: set-kubelet-config
            spec:
              machineConfigPoolSelector:
                matchLabels:
                  custom-kubelet: set-kubelet-config
              kubeletConfig:
                maxPods: <pod_count>
                kubeAPIBurst: <burst_rate>
                kubeAPIQPS: <QPS>
            ```
   2. Update the machine config pool for workers with the label:

      ```
      $ oc label machineconfigpool worker custom-kubelet=set-kubelet-config
      ```
   3. Create the `KubeletConfig` object:

      ```
      $ oc create -f change-maxPods-cr.yaml
      ```

**Verification**

1. Verify that the `KubeletConfig` object is created:

   ```
   $ oc get kubeletconfig
   ```

   **Example output**

   ```
   NAME                      AGE
   set-kubelet-config        15m
   ```

   Depending on the number of worker nodes in the cluster, wait for the worker nodes to be rebooted one by one. For a cluster with 3 worker nodes, this could take about 10 to 15 minutes.
2. Verify that the changes are applied to the node:

   1. Check on a worker node that the `maxPods` value changed:

      ```
      $ oc describe node <node_name>
      ```
   2. Locate the `Allocatable` stanza:

      ```
       ...
      Allocatable:
        attachable-volumes-gce-pd:  127
        cpu:                        3500m
        ephemeral-storage:          123201474766
        hugepages-1Gi:              0
        hugepages-2Mi:              0
        memory:                     14225400Ki
        pods:                       500
       ...
      ```

      In this example, the `pods` parameter should report the value you set in the `KubeletConfig` object.
3. Verify the change in the `KubeletConfig` object:

   ```
   $ oc get kubeletconfigs set-kubelet-config -o yaml
   ```

   This should show a status of `True` and `type:Success`, as shown in the following example:

   ```
   spec:
     kubeletConfig:
       containerLogMaxSize: 50Mi
       maxPods: 500
       podPidsLimit: 8192
     machineConfigPoolSelector:
       matchLabels:
         custom-kubelet: set-kubelet-config
   status:
     conditions:
     - lastTransitionTime: "2021-06-30T17:04:07Z"
       message: Success
       status: "True"
       type: Success
   ```

### [4.2. Creating a ContainerRuntimeConfig CR to edit CRI-O parameters](#create-a-containerruntimeconfig_machine-configs-custom) Copy linkLink copied to clipboard!

You can change some of the settings associated with the OpenShift Container Platform CRI-O runtime for the nodes associated with a specific machine config pool (MCP) by using a `ContainerRuntimeConfig` custom resource (CR).

With a `ContainerRuntimeConfig` CR, you set the configuration values and add a label to match the MCP. The MCO then rebuilds the `crio.conf` and `storage.conf` configuration files on the associated nodes with the updated values.

Note

To revert the changes implemented by using a `ContainerRuntimeConfig` CR, you must delete the CR. Removing the label from the machine config pool does not revert the changes.

You can modify the following settings by using a `ContainerRuntimeConfig` CR:

* **Log level**: The `logLevel` parameter sets the CRI-O `log_level` parameter, which is the level of verbosity for log messages. The default is `info` (`log_level = info`). Other options include `fatal`, `panic`, `error`, `warn`, `debug`, and `trace`.
* **Overlay size**: The `overlaySize` parameter sets the CRI-O Overlay storage driver `size` parameter, which is the maximum size of a container image.
* **Container runtime**: The `defaultRuntime` parameter sets the container runtime to either `crun` or `runc`. The default is `crun`.

You should have one `ContainerRuntimeConfig` CR for each machine config pool with all the config changes you want for that pool. If you are applying the same content to all the pools, you only need one `ContainerRuntimeConfig` CR for all the pools.

You should edit an existing `ContainerRuntimeConfig` CR to modify existing settings or add new settings instead of creating a new CR for each change. It is recommended to create a new `ContainerRuntimeConfig` CR only to modify a different machine config pool, or for changes that are intended to be temporary so that you can revert the changes.

You can create multiple `ContainerRuntimeConfig` CRs, as needed, with a limit of 10 per cluster. For the first `ContainerRuntimeConfig` CR, the MCO creates a machine config appended with `containerruntime`. With each subsequent CR, the controller creates a new `containerruntime` machine config with a numeric suffix. For example, if you have a `containerruntime` machine config with a `-2` suffix, the next `containerruntime` machine config is appended with `-3`.

If you want to delete the machine configs, you should delete them in reverse order to avoid exceeding the limit. For example, you should delete the `containerruntime-3` machine config before deleting the `containerruntime-2` machine config.

Note

If you have a machine config with a `containerruntime-9` suffix, and you create another `ContainerRuntimeConfig` CR, a new machine config is not created, even if there are fewer than 10 `containerruntime` machine configs.

The following example command and output show multiple `ContainerRuntimeConfig` CRs:

```
$ oc get ctrcfg
```

```
NAME         AGE
ctr-overlay  15m
ctr-level    5m45s
```

The following example command and output show multiple `containerruntime` machine configs:

```
$ oc get mc | grep container
```

```
...
01-master-container-runtime                        b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             57m
...
01-worker-container-runtime                        b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             57m
...
99-worker-generated-containerruntime               b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             26m
99-worker-generated-containerruntime-1             b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             17m
99-worker-generated-containerruntime-2             b5c5119de007945b6fe6fb215db3b8e2ceb12511   3.5.0             7m26s
...
```

The following example sets the `log_level` field to `debug`, sets the overlay size to 8 GB, and configures runC as the container runtime:

```
apiVersion: machineconfiguration.openshift.io/v1
kind: ContainerRuntimeConfig
metadata:
 name: overlay-size
spec:
 machineConfigPoolSelector:
   matchLabels:
     pools.operator.machineconfiguration.openshift.io/worker: ''
 containerRuntimeConfig:
   logLevel: debug
   overlaySize: 8G
   defaultRuntime: "runc"
```

where:

`spec.machineConfigPoolSelector.matchLabels`
:   Specifies the machine config pool label. For a container runtime config, the role must match the name of the associated machine config pool.

`spec.containerRuntimeConfig.logLevel`
:   Specifies the level of verbosity for log messages. This parameter is optional.

`spec.containerRuntimeConfig.overlaySize`
:   Specifies the maximum size of a container image. This parameter is optional.

`spec.containerRuntimeConfig.defaultRuntime`
:   Specifies the container runtime to deploy to new containers, either `crun` or `runc`. The default value is `crun`. This parameter is optional.

The following procedure shows how to change CRI-O settings by using a `ContainerRuntimeConfig` CR.

**Procedure**

1. Create a YAML file for the `ContainerRuntimeConfig` CR:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: ContainerRuntimeConfig
   metadata:
    name: overlay-size
   spec:
    machineConfigPoolSelector:
      matchLabels:
        pools.operator.machineconfiguration.openshift.io/worker: ''
    containerRuntimeConfig:
      logLevel: debug
      overlaySize: 8G
      defaultRuntime: "runc"
   ```

   where:

   `spec.machineConfigPoolSelector.matchLabels`
   :   Set a label for the machine config pool that you want you want to modify.

   `spec.containerRuntimeConfig`
   :   Set the parameters as needed.
2. Create the `ContainerRuntimeConfig` CR:

   ```
   $ oc create -f <file_name>.yaml
   ```
3. Verify that the CR is created:

   ```
   $ oc get ContainerRuntimeConfig
   ```

   **Example output**

   ```
   NAME           AGE
   overlay-size   3m19s
   ```
4. Check that a new `containerruntime` machine config is created:

   ```
   $ oc get machineconfigs | grep containerrun
   ```

   **Example output**

   ```
   99-worker-generated-containerruntime   2c9371fbb673b97a6fe8b1c52691999ed3a1bfc2  3.5.0  31s
   ```
5. Monitor the machine config pool until all are shown as ready:

   ```
   $ oc get mcp worker
   ```

   **Example output**

   ```
   NAME    CONFIG               UPDATED  UPDATING  DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT  DEGRADEDMACHINECOUNT  AGE
   worker  rendered-worker-169  False    True      False     3             1                  1                    0                     9h
   ```
6. Verify that the settings were applied in CRI-O:

   1. Open an `oc debug` session to a node in the machine config pool and run `chroot /host`.

      ```
      $ oc debug node/<node_name>
      ```

      ```
      sh-4.4# chroot /host
      ```
   2. Verify the changes in the `crio.conf` file:

      ```
      sh-4.4# crio config | grep 'log_level'
      ```

      **Example output**

      ```
      log_level = "debug"
      ```
   3. Verify the changes in the `storage.conf` file:

      ```
      sh-4.4# head -n 7 /etc/containers/storage.conf
      ```

      **Example output**

      ```
      [storage]
        driver = "overlay"
        runroot = "/var/run/containers/storage"
        graphroot = "/var/lib/containers/storage"
        [storage.options]
          additionalimagestores = []
          size = "8G"
      ```
   4. Verify the changes in the `crio/crio.conf.d/01-ctrcfg-defaultRuntime` file:

      ```
      sh-5.1# cat /etc/crio/crio.conf.d/01-ctrcfg-defaultRuntime
      ```

      **Example output**

      ```
      [crio]
        [crio.runtime]
          default_runtime = "runc"
      ```

### [4.3. Configuring the container runtime](#config-container-runtime_machine-configs-custom) Copy linkLink copied to clipboard!

You can configure the container runtime used with new workloads on your nodes, based on which runtime you or your organization prefers. You can use either crun, which is considered a faster and more lightweight runtime, or runC, which is more widely used than crun.

For information on crun and runC, see "About the container engine and container runtime".

Warning

Starting in OpenShift Container Platform 4.22, the runC container runtime is deprecated.

Starting in OpenShift Container Platform 4.18, crun is the default container runtime for new installations. You can change between the runtimes by using a `ContainerRuntimeConfig` object, as described in the following procedure. Changing the container runtime affects new workloads only. Existing workloads continue to use their existing container runtime.

If you updated your cluster from OpenShift Container Platform 4.17, the runC container runtime remains unchanged as the default. During the upgrade, two `MachineConfig` objects, one for the control plane nodes and one for the worker nodes, were created to override the new default runtime. You can migrate the container runtime to crun, on a schedule of your choosing, by removing either or both of the `MachineConfig` objects.

**Procedure**

* If your cluster is updated from OpenShift Container Platform 4.17, you can use the crun container runtime by deleting the following `MachineConfig` objects:

  + Migrate your worker nodes to crun by running the following command:

    ```
    $ oc delete machineconfig 00-override-worker-generated-crio-default-container-runtime
    ```
  + Migrate your control plane nodes to crun by running the following command:

    ```
    $ oc delete machineconfig 00-override-master-generated-crio-default-container-runtime
    ```
* For any OpenShift Container Platform 4.18 or greater cluster, you can configure crun or runC as the container runtime for specific nodes by creating a container runtime configuration:

  1. Create a YAML file for the `ContainerRuntimeConfig` CR:

     ```
     apiVersion: machineconfiguration.openshift.io/v1
     kind: ContainerRuntimeConfig
     metadata:
      name: configure-runc
     spec:
      machineConfigPoolSelector:
        matchLabels:
          pools.operator.machineconfiguration.openshift.io/worker: ''
      containerRuntimeConfig:
        defaultRuntime: "runc"
     ```

     where:

     + `spec.machineConfigPoolSelector.matchLabels`:: Specifies a label for the machine config pool that you want you want to modify.
     + `spec.containerRuntimeConfig.defaultRuntime`:: Specifies the container runtime to use with new workloads on the nodes in the specified machine config pool, either `crun` or `runc`.
  2. Create the `ContainerRuntimeConfig` CR:

     ```
     $ oc create -f <file_name>.yaml
     ```

**Verification**

1. After the nodes return to a ready state, open an `oc debug` session to a node by running the following command:

   ```
   $ oc debug node/<node_name>
   ```
2. Set `/host` as the root directory within the debug shell by running the following command:

   ```
   sh-5.1# chroot /host
   ```
3. Check the container runtime by using the following command:

   ```
   sh-5.1# crio status config | grep default_runtime
   ```

   **Example output**

   ```
   INFO[2026-01-27 23:09:18.413462914Z] Starting CRI-O, version: 1.30.14-6.rhaos4.17.gitfa27f6f.el9, git: unknown(clean)
       default_runtime = "runc"
   ```

   The `default_runtime` parameter specifies the container runtime that OpenShift Container Platform uses for new workloads on this node, either `crun` or `runc`, depending on what you have configured.

### [4.4. Setting the default maximum container root partition size for Overlay with CRI-O](#set-the-default-max-container-root-partition-size-for-overlay-with-crio_machine-configs-custom) Copy linkLink copied to clipboard!

You can use a `ContainerRuntimeConfig` custom resource (CR) to set a maximum partition size for the root disk of all containers.

The root partition of each container shows all of the available disk space of the underlying host.

To configure the maximum Overlay size, as well as other CRI-O options like the log level, you can create the following `ContainerRuntimeConfig` custom resource definition (CRD):

```
apiVersion: machineconfiguration.openshift.io/v1
kind: ContainerRuntimeConfig
metadata:
 name: overlay-size
spec:
 machineConfigPoolSelector:
   matchLabels:
     custom-crio: overlay-size
 containerRuntimeConfig:
   logLevel: debug
   overlaySize: 8G
```

**Procedure**

1. Create the configuration object:

   ```
   $ oc apply -f overlaysize.yml
   ```
2. To apply the new CRI-O configuration to your worker nodes, edit the worker machine config pool:

   ```
   $ oc edit machineconfigpool worker
   ```
3. Add the `custom-crio` label based on the `matchLabels` name you set in the `ContainerRuntimeConfig` CRD:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfigPool
   metadata:
     creationTimestamp: "2020-07-09T15:46:34Z"
     generation: 3
     labels:
       custom-crio: overlay-size
       machineconfiguration.openshift.io/mco-built-in: ""
   ```
4. Save the changes, then view the machine configs:

   ```
   $ oc get machineconfigs
   ```

   New `99-worker-generated-containerruntime` and `rendered-worker-xyz` objects are created:

   **Example output**

   ```
   99-worker-generated-containerruntime  4173030d89fbf4a7a0976d1665491a4d9a6e54f1   3.5.0             7m42s
   rendered-worker-xyz                   4173030d89fbf4a7a0976d1665491a4d9a6e54f1   3.5.0             7m36s
   ```
5. After those objects are created, monitor the machine config pool for the changes to be applied:

   ```
   $ oc get mcp worker
   ```

   The worker nodes show `UPDATING` as `True`, as well as the number of machines, the number updated, and other details:

   **Example output**

   ```
   NAME   CONFIG              UPDATED   UPDATING   DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   worker rendered-worker-xyz False True False     3             2                   2                    0                      20h
   ```

   When complete, the worker nodes transition back to `UPDATING` as `False`, and the `UPDATEDMACHINECOUNT` number matches the `MACHINECOUNT`:

   **Example output**

   ```
   NAME   CONFIG              UPDATED   UPDATING   DEGRADED  MACHINECOUNT  READYMACHINECOUNT  UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   worker   rendered-worker-xyz   True      False      False      3         3            3             0           20h
   ```

   Looking at a worker machine, you see that the new 8 GB max size configuration is applied to all of the workers:

   **Example output**

   ```
   head -n 7 /etc/containers/storage.conf
   [storage]
     driver = "overlay"
     runroot = "/var/run/containers/storage"
     graphroot = "/var/lib/containers/storage"
     [storage.options]
       additionalimagestores = []
       size = "8G"
   ```

   Looking inside a container, you see that the root partition is now 8 GB:

   **Example output**

   ```
   ~ $ df -h
   Filesystem                Size      Used Available Use% Mounted on
   overlay                   8.0G      8.0K      8.0G   0% /
   ```

### [4.5. Creating a drop-in file for the default CRI-O capabilities](#create-crio-default-capabilities_machine-configs-custom) Copy linkLink copied to clipboard!

You can change some of the settings associated with the OpenShift Container Platform CRI-O runtime for the nodes associated with a specific machine config pool (MCP) by using a controller custom resource (CR).

You set the configuration values and add a label to match the MCP in a `ContainerRuntimeConfig` CR. The Machine Config Operator (MCO) then rebuilds the `crio.conf` and `default.conf` configuration files on the associated nodes with the updated values.

Earlier versions of OpenShift Container Platform included specific machine configs by default. If you updated to a later version of OpenShift Container Platform, those machine configs were retained to ensure that clusters running on the same OpenShift Container Platform version have the same machine configs.

You can create multiple `ContainerRuntimeConfig` CRs, as needed, with a limit of 10 per cluster. For the first `ContainerRuntimeConfig` CR, the MCO creates a machine config appended with `containerruntime`. With each subsequent CR, the controller creates a `containerruntime` machine config with a numeric suffix. For example, if you have a `containerruntime` machine config with a `-2` suffix, the next `containerruntime` machine config is appended with `-3`.

If you want to delete the machine configs, delete them in reverse order to avoid exceeding the limit. For example, delete the `containerruntime-3` machine config before you delete the `containerruntime-2` machine config.

Note

If you have a machine config with a `containerruntime-9` suffix and you create another `ContainerRuntimeConfig` CR, a new machine config is not created, even if there are fewer than 10 `containerruntime` machine configs.

**Example of multiple ContainerRuntimeConfig CRs**

```
$ oc get ctrcfg
```

**Example output**

```
NAME         AGE
ctr-overlay  15m
ctr-level    5m45s
```

**Example showing multiple containerruntime related system configs**

```
$ cat /proc/1/status | grep Cap
```

```
$ capsh --decode=<decode_CapBnd_value>
```

Replace `<decode_CapBnd_value>` with the specific value you want to decode.

## [Chapter 5. Pinning images to nodes](#machine-config-pin-preload-images-about) Copy linkLink copied to clipboard!

You can prevent a slow, unreliable connection to an image registry from interfering with operations that require pulled images by pulling those images in advance and *pinning* those images to a specific machine config pool (MCP) before they are actually needed.

This problem can affect clusters that have low bandwidth, clusters with unreliable internet connectivity, or clusters in a disconnected environment. For example, a cluster update might require pulling more than one hundred images. Failure to pull those images could cause retries that can interfere with the update process and might cause the update to fail.

By pinning images, you can ensure that the images are available to your nodes when needed for operations such as updating a cluster or deploying an application. You can provide a more consistent update, which is important when scheduling updates into maintenance windows. When deploying applications, you can pin images to ensure that the images are available, so that you can deploy in a more reliable manner.

You can pin images to specific nodes by using a `PinnedImageSet` custom resource (CR), as described in *Pinning images*. Pinned images are stored on the nodes in the `/etc/crio/crio.conf.d/50-pinned-images` file on those nodes. The contents of the file appear similar to the following example:

```
[crio]
  [crio.image]
    pinned_images = ["quay.io/openshift-release-dev/ocp-release@sha256:4198606580b69c8335ad7ae531c3a74e51aee25db5faaf368234e8c8dae5cbea", "quay.io/openshift-release-dev/ocp-release@sha256:513cf1028aa1a021fa73d0601427a0fbcf6d212b88aaf9d76d4e4841a061e44e", "quay.io/openshift-release-dev/ocp-release@sha256:61eae2d261e54d1b8a0e05f6b5326228b00468364563745eed88460af04f909b"]
```

Another benefit to pinned images is that image garbage collection does not remove the pinned images.

Before pulling the images, the Machine Config Operator (MCO) verifies that there is enough storage space available on each affected node. If the node has sufficient space, the MCO creates the pinned image file, pulls the images, and reloads CRI-O. If there is not sufficient space, the MCO does not pull the images and presents an error message.

### [5.1. Pinning images](#machine-config-pin-preload-images_machine-config-operator) Copy linkLink copied to clipboard!

You can pin images to your nodes by using a `PinnedImageSet` custom resource (CR) making the images available to your nodes when needed for operations such as updating a cluster or deploying an application.

The pinned image set defines the list of images to pre-load and the machine config pool to which the images should be pinned.

The images are stored in the `/etc/crio/crio.conf.d/50-pinned-images` file on the nodes.

Note

Only images that you can successfully inspect with the `podman manifest inspect <IMAGE_URL>` command can be used with a pinned image set. Image inspections could fail due to unsupported manifest formats, registry authorization issues, invalid schemas, network connectivity issues, or other issues.

**Procedure**

1. Create a YAML file that defines the `PinnedImageSet` object, similar to the following example:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: PinnedImageSet
   metadata:
     labels:
       machineconfiguration.openshift.io/role: worker
     name: worker-pinned-images
   spec:
     pinnedImages:
      - name: quay.io/openshift-release-dev/ocp-release@sha256:513cf1028aa1a021fa73d0601427a0fbcf6d212b88aaf9d76d4e4841a061e44e
      - name: quay.io/openshift-release-dev/ocp-release@sha256:61eae2d261e54d1b8a0e05f6b5326228b00468364563745eed88460af04f909b
   ```

   where:

   `metadata.labels`
   :   Specifies an optional node selector to specify the machine config pool to pin the images to. If not specified, the images are pinned to all nodes in the cluster.

   `spec.pinnedImages`
   :   Specifies a list of one or more images to pre-load.
2. Create the `PinnedImageSet` object by running the following command:

   ```
   $ oc create -f <file_name>.yaml
   ```

**Verification**

* Check that the pinned image set is reported in the machine config node object for the affected machine config pool by running the following command:

  ```
  $ oc describe machineconfignode <machine_config_node_name>
  ```

  **Example command**

  ```
  $ oc describe machineconfignode ci-ln-25hlkvt-72292-jrs48-worker-a-2bdj
  ```

  **Example output for a successful image pull and pin**

  ```
  apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineConfigNode
  metadata:
    creationTimestamp: "2025-04-28T18:40:29Z"
    generation: 3
    name: <machine_config_node_name>
  # ...
  status
    pinnedImageSets:
    - currentGeneration: 1
      desiredGeneration: 1
      name: worker-pinned-images
  ```

  where:

  `status.pinnedImageSets`
  :   Specifies that the `PinnedImageSet` object you created is associated with the machine config node.

  Any failures or error messages would appear in the `MachineConfigNode` object status fields, as shown in the following example:

  **Example output for a failed image pull and pin**

  ```
  apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineConfigNode
  metadata:
    creationTimestamp: "2025-04-28T18:40:29Z"
    generation: 3
    name: <machine_config_node_name>
  # ...
    - lastTransitionTime: "2025-04-29T19:37:23Z"
      message: One or more PinnedImageSet is experiencing an error. See PinnedImageSet
        list for more details.
      reason: PrefetchFailed
      status: "True"
      type: PinnedImageSetsDegraded
    configVersion:
      current: rendered-worker-cef1b52c532e19a20add12e369261fba
      desired: rendered-worker-cef1b52c532e19a20add12e369261fba
    observedGeneration: 3
    pinnedImageSets:
    - desiredGeneration: 1
      lastFailedGeneration: 1
      lastFailedGenerationError: 'failed to execute podman manifest inspect for "quay.io/rh-ee/machine-config-operator@sha256:65d3a308767b1773b6e3499dde6ef085753d7e20e685f78841079":
        exit status 125'
      name: worker-pinned-images
  ```
* Check that the pinned image file is created and contains the correct images.

  1. Start a debug session for a node by running the following command:

     ```
     $ oc debug node/<node_name>
     ```
  2. Set `/host` as the root directory within the debug shell by running the following command:

     ```
     sh-5.1# chroot /host
     ```
  3. Verify the contents of the pinned image file by running the following command:

     ```
     $ cat /etc/crio/crio.conf.d/50-pinned-images
     ```

     **Example output**

     ```
     [crio]
       [crio.image]
         pinned_images = ["quay.io/openshift-release-dev/ocp-release@sha256:4198606580b69c8335ad7ae531c3a74e51aee25db5faaf368234e8c8dae5cbea", "quay.io/openshift-release-dev/ocp-release@sha256:513cf1028aa1a021fa73d0601427a0fbcf6d212b88aaf9d76d4e4841a061e44e", "quay.io/openshift-release-dev/ocp-release@sha256:61eae2d261e54d1b8a0e05f6b5326228b00468364563745eed88460af04f909b"]
     ```

     where:

     `pinnedImages`
     :   Specifies the images that have been pulled and pinned for the affected machine config pool.

## [Chapter 6. Boot image management](#mco-update-boot-images) Copy linkLink copied to clipboard!

For supported platforms, the Machine Config Operator (MCO) can manage and update the boot image on each node to ensure the Red Hat Enterprise Linux CoreOS (RHCOS) version of the boot image matches the Red Hat Enterprise Linux CoreOS (RHCOS) version appropriate for your cluster.

The following table lists the platforms on which boot image management is available:

Expand

| Platform | Worker machine sets | Control plane machine sets |
| --- | --- | --- |
| Google Cloud | Enabled by default | Disabled by default |
| Amazon Web Services (AWS) | Enabled by default | Disabled by default |
| Microsoft Azure | Enabled by default | Disabled by default |
| VMware vSphere | Enabled by default | Not supported |

Show more

For all other platforms, the MCO does not automatically update the boot image with each cluster update. Images from the Google Cloud Marketplace or AWS Marketplace are not automatically updated.

For clusters where automatic updates are disabled or not supported, you can manually update the boot image on your cluster. See "Manually updating the boot image" for information. The method to update or specify the image varies by platform.

### [6.1. About boot image management](#mco-update-boot-images_machine-configs-configure) Copy linkLink copied to clipboard!

With boot image management enabled, the Machine Config Operator (MCO) manages and updates the Red Hat Enterprise Linux CoreOS (RHCOS) version of the boot image in the machine sets for your control plane or worker nodes. This means that the MCO updates the boot image whenever you update your cluster. Without boot image management enabled, if your cluster was originally created with an older OpenShift Container Platform version, the boot image that the MCO would use to create new nodes is an older Red Hat Enterprise Linux CoreOS (RHCOS) version, even if your cluster is at a later OpenShift Container Platform version.

New nodes created after enabling the feature use the updated boot image. This feature has no effect on existing nodes.

Note

The following table lists the platforms on which boot image management is available:

Expand

| Platform | Worker machine sets | Control plane machine sets |
| --- | --- | --- |
| Google Cloud | Enabled by default | Disabled by default |
| Amazon Web Services (AWS) | Enabled by default | Disabled by default |
| Microsoft Azure | Enabled by default | Disabled by default |
| VMware vSphere | Enabled by default | Not supported |

Show more

For all other platforms, the MCO does not automatically update the boot image with each cluster update. Images from the Google Cloud Marketplace or AWS Marketplace are not automatically updated.

For clusters where automatic updates are disabled or not supported, you can manually update the boot image on your cluster. See "Manually updating the boot image" for information. The method to update or specify the image varies by platform.

For example, with the feature disabled, if your cluster was originally created with OpenShift Container Platform 4.16, the boot image that the MCO would use to create new nodes is the same RHCOS version that was installed for the cluster, even if your cluster is currently at a later OpenShift Container Platform version.

Using an older boot image could cause the following issues:

* Extra time to start nodes
* Certificate expiration issues
* Version skew issues

You can disable the boot image management feature, if needed. When the feature is disabled, the boot image version no longer updates with the cluster. For example, you could disable the boot image management feature in order to use a custom boot image that you do not want changed. For information on how to disable this feature, see "Disabling boot image management". If you disable this feature, you can re-enable the feature at any time. For information, see "Enabling boot image management".

How the cluster behaves after disabling or re-enabling the feature, depends upon when you made the change, including the following scenarios:

* If you disable the feature before updating to a new OpenShift Container Platform version:

  + The boot image version used by the machine sets remains the same OpenShift Container Platform version as when the feature was disabled.
  + When you scale up nodes, the new nodes use that same OpenShift Container Platform version.
* If you disable the feature after updating to a new OpenShift Container Platform version:

  + The boot image version used by the machine sets is updated to match the updated OpenShift Container Platform version.
  + When you scale up nodes, the new nodes use the updated OpenShift Container Platform version.
  + If you update to a later OpenShift Container Platform version, the boot image version in the machine sets remains at the current version and is not updated with the cluster.
* If you enable the feature after disabling:

  + The boot image version used by the machine sets is updated to the current OpenShift Container Platform version, if different.
  + When you scale up nodes, the new nodes use the current OpenShift Container Platform version in the cluster.

Note

Because a boot image is used only when a node is scaled up, this feature has no effect on existing nodes.

To view the current Red Hat Enterprise Linux CoreOS (RHCOS) boot image version used in your cluster, you can view the `/sysroot/.coreos-aleph-version.json` file on that node.

**Example coreos-aleph-version.json file with an older boot image**

```
{
# ...
    "ref": "docker://ostree-image-signed:oci-archive:/rhcos-418.94.202511191518-0-ostree.x86_64.ociarchive",
    "version": "418.94.202511191518-0"
}
```

where:

`<version>`
:   Specifies the Red Hat Enterprise Linux CoreOS (RHCOS) boot image version. In this example, the boot image is from the originally-installed OpenShift Container Platform 4.18 version, regardless of the current version of the cluster.

Important

If any of the machine sets for which you want to enable boot image management use a `*-user-data` secret that is based on Ignition version 2.2.0, the Machine Config Operator converts the Ignition version to 3.4.0 when you enable the feature. OpenShift Container Platform versions 4.5 and lower use Ignition version 2.2.0. If this conversion fails, the MCO or your cluster could degrade. An error message that includes *err: converting ignition stub failed: failed to parse Ignition config* is added to the output of the `oc get ClusterOperator machine-config` command. You can use the following general steps to correct the problem:

1. Disable the boot image management feature. For information, see "Disabling boot image management".
2. Manually update the `*-user-data` secret to use Ignition version to 3.2.0.
3. Enable the boot image management feature. For information, see "Enabling boot image management".

### [6.2. Enabling boot image management](#mco-update-boot-images-configuring_machine-configs-configure) Copy linkLink copied to clipboard!

For supported platforms, the Machine Config Operator (MCO) can manage and update the boot image on each node to ensure the Red Hat Enterprise Linux CoreOS (RHCOS) version of the boot image matches the Red Hat Enterprise Linux CoreOS (RHCOS) version appropriate for your cluster.

Note

The following table lists the platforms on which boot image management is available:

Expand

| Platform | Worker machine sets | Control plane machine sets |
| --- | --- | --- |
| Google Cloud | Enabled by default | Disabled by default |
| Amazon Web Services (AWS) | Enabled by default | Disabled by default |
| Microsoft Azure | Enabled by default | Disabled by default |
| VMware vSphere | Enabled by default | Not supported |

Show more

For all other platforms, the MCO does not automatically update the boot image with each cluster update. Images from the Google Cloud Marketplace or AWS Marketplace are not automatically updated.

For clusters where automatic updates are disabled or not supported, you can manually update the boot image on your cluster. See "Manually updating the boot image" for information. The method to update or specify the image varies by platform.

To enable the boot image management feature for control plane machine sets or to re-enable the boot image management feature for worker machine sets where it was disabled, edit the `MachineConfiguration` object. You can enable the feature for all of the machine sets in the cluster or specific machine sets.

Note

Because the boot image management feature for worker nodes is default for the Google Cloud and AWS platforms, the `managedBootImages` configuration does not appear in the machine configuration object. To enable the feature for control plane machine sets without disabling the feature for worker machine sets, you must expressly add the configuration for both the control plane and worker machine sets, as shown in the following procedure. If you add only the configuration for control plane machine sets, due to default behavior, the Machine Config Operator (MCO) overwrites the configuration for the worker machine sets.

Enabling the feature updates the boot image to the Red Hat Enterprise Linux CoreOS (RHCOS) boot image version appropriate for your cluster. If the cluster is again updated to a new OpenShift Container Platform version in the future, the boot image is updated again. New nodes created after enabling the feature use the updated boot image. This feature has no effect on existing nodes.

When boot image management is enabled, the MCO automatically enables boot image skew enforcement to ensure that the boot image version is compliant for your cluster. For more information, see "Boot image skew enforcement".

**Procedure**

1. Edit the `MachineConfiguration` object, named `cluster`, by using the following command:

   ```
   $ oc edit MachineConfiguration cluster
   ```
2. Enable the boot image management feature for some or all of your machine sets:

   * Enable the boot image management feature for all machine sets:

     ```
     apiVersion: operator.openshift.io/v1
     kind: MachineConfiguration
     metadata:
       name: cluster
     spec:
     # ...
       managedBootImages:
         machineManagers:
         - apiGroup: machine.openshift.io
           resource: controlplanemachinesets
           selection:
             mode: All
         - apiGroup: machine.openshift.io
           resource: machinesets
           selection:
             mode: All
     ```

     where:

     `spec.managedBootImages`
     :   Configures the boot image management feature.

     `spec.managedBootImages.machineManagers.apiGroup`
     :   Specifies the API group. This must be `machine.openshift.io`.

     `spec.managedBootImages.machineManagers.resource`
     :   Specifies the resource within the specified API group to apply the change. Use one or both of the following parameters. You must add the full stanza, as shown, if you want to enable the feature for control plane and worker machine sets.

         + `controlplanemachinesets`: Enables boot image management for control plane machine sets.
         + `machinesets`: Enables boot image management for worker machine sets.

     `spec.managedBootImages.machineManagers.selection.mode`
     :   Specifies that the feature is enabled for all machine sets in the cluster.
   * Enable the boot image management feature for specific worker machine sets:

     ```
     apiVersion: operator.openshift.io/v1
     kind: MachineConfiguration
     metadata:
       name: cluster
     spec:
     # ...
       managedBootImages:
         machineManagers:
         - apiGroup: machine.openshift.io
           resource: machinesets
           selection:
             mode: Partial
             partial:
               machineResourceSelector:
                 matchLabels:
                   region: "east"
     ```

     where:

     `spec.managedBootImages`
     :   Configures the boot image management feature.

     `spec.managedBootImages.machineManagers.apiGroup`
     :   Specifies the API group. This must be `machine.openshift.io`.

     `spec.managedBootImages.machineManagers.resource`
     :   Specifies the resource within the specified API group to apply the change. This must be `machinesets`. Partial boot image management for control plane machine sets is not supported.

     `spec.managedBootImages.machineManagers.selection.mode`
     :   Specifies that the feature is enabled for specific machine sets in the cluster. This must be `Partial`.

     `spec.managedBootImages.machineManagers.selection.partial`
     :   Specifies that the feature is enabled for machine sets with the specified label in their `MachineSet` object.

**Verification**

1. View the current state of the boot image management feature by using the following command to view the machine configuration object:

   ```
   $ oc get machineconfiguration cluster -o yaml
   ```

   **Example machine set with the boot image reference**

   ```
   kind: MachineConfiguration
   metadata:
     name: cluster
   # ...
   status:
     conditions:
     - lastTransitionTime: "2025-05-01T20:11:49Z"
       message: Reconciled 2 of 4 MAPI MachineSets | Reconciled 0 of 0 CAPI MachineSets
         | Reconciled 0 of 0 CAPI MachineDeployments
       reason: BootImageUpdateConfigurationUpdated
       status: "True"
       type: BootImageUpdateProgressing
     - lastTransitionTime: "2025-05-01T19:30:13Z"
       message: 0 Degraded MAPI MachineSets | 0 Degraded CAPI MachineSets | 0 CAPI MachineDeployments
       reason: BootImageUpdateConfigurationUpdated
       status: "False"
       type: BootImageUpdateDegraded
     managedBootImagesStatus:
       machineManagers:
       - apiGroup: machine.openshift.io
         resource: controlplanemachinesets
         selection:
           mode: All
       - apiGroup: machine.openshift.io
         resource: machinesets
         selection:
           mode: All
   ```

   where:

   `status.managedBootImagesStatus.machineManagers.selection.mode`
   :   Specifies that the boot image management feature is enabled when set to `All`.
2. Scale a machine set to create a new node by using a command similar to the following. The boot image is updated only for new nodes.

   ```
   $ oc scale --replicas=2 machinesets.machine.openshift.io <machineset> -n openshift-machine-api
   ```
3. If your cluster was using an older boot image version, you can see the new boot image version when the new node reaches the `READY` state. View the Red Hat Enterprise Linux CoreOS (RHCOS) version on a nodes:

   1. Log in to the node by using a command similar to the following:

      ```
      $ oc debug node/<node_name>
      ```
   2. Set `/host` as the root directory within the debug shell by using the following command:

      ```
      sh-5.1# chroot /host
      ```
   3. View the `/sysroot/.coreos-aleph-version.json` file by using a command similar to the following:

      ```
      sh-5.1# cat /sysroot/.coreos-aleph-version.json
      ```

      **Example output**

      ```
      {
      # ...
          "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251015-1-ostree.x86_64.ociarchive",
          "version": "9.6.20251015-1"
      }
      ```

      where:

      `<version>`
      :   Specifies the boot image version.

### [6.3. Disabling boot image management](#mco-update-boot-images-disable_machine-configs-configure) Copy linkLink copied to clipboard!

You can disable the boot image management feature so that the Machine Config Operator (MCO) no longer manages or updates the boot image in the affected machine sets. For example, you could disable this feature for the worker nodes in order to use a custom boot image that you do not want changed.

Note

If you are updating an Microsoft Azure or VMware vSphere cluster from OpenShift Container Platform 4.21 to 4.22, and you have not configured the `managedBootImages` parameter, the update is blocked with the message: `This cluster is Azure or vSphere but lacks a boot image configuration`. The update is intentionally blocked on Azure or vSphere clusters in order to alert you that the default boot image management behavior is changing between version 4.21 and 4.22 in order to enable boot images management by default on those platforms.

To allow the update, perform one of the following tasks:

* If you want to allow the feature to be enabled, acknowledge that you are aware of the change in the default behavior by patching the `admin-acks` config map by running the following command:

  ```
  $ oc -n openshift-config patch cm admin-acks --patch '{"data":{"ack-4.21-boot-image-opt-out-in-4.22":"true"}}' --type=merge
  ```
* If you do not want the boot image management feature enabled, explicitly disable the feature for worker machine sets by using the following procedure.

You disable the boot image management feature for the control plane or worker machine sets in your cluster by editing the `MachineConfiguration` object.

Note

The following table lists the platforms on which boot image management is available:

Expand

| Platform | Worker machine sets | Control plane machine sets |
| --- | --- | --- |
| Google Cloud | Enabled by default | Disabled by default |
| Amazon Web Services (AWS) | Enabled by default | Disabled by default |
| Microsoft Azure | Enabled by default | Disabled by default |
| VMware vSphere | Enabled by default | Not supported |

Show more

For all other platforms, the MCO does not automatically update the boot image with each cluster update. Images from the Google Cloud Marketplace or AWS Marketplace are not automatically updated.

For clusters where automatic updates are disabled or not supported, you can manually update the boot image on your cluster. See "Manually updating the boot image" for information. The method to update or specify the image varies by platform.

Disabling this feature does not rollback the nodes or machine sets to the originally-installed boot image. The machine sets retain the boot image version that was present when the feature was disabled and is not updated if the cluster is upgraded to a new OpenShift Container Platform version in the future. This feature has no effect on existing nodes.

If boot image management is disabled, you must update the boot image version that is used by the boot image skew enforcement feature to ensure that the boot image is current for your cluster. For more information, see "Boot image skew enforcement".

After disabling the feature, you can re-enable the feature at any time. For more information, see "Enabling updated boot images".

**Procedure**

1. Edit the `MachineConfiguration` object, named `cluster`, by using the following command::

   ```
   $ oc edit MachineConfiguration cluster
   ```
2. Disable the feature for some or all of your machine sets by making one or both of the following changes:

   * Disable the feature for nodes in the worker machine sets by adding the following parameters:

     ```
     apiVersion: operator.openshift.io/v1
     kind: MachineConfiguration
     metadata:
       name: cluster
     spec:
     # ...
       managedBootImages:
         machineManagers:
         - apiGroup: machine.openshift.io
           resource: machinesets
           selection:
             mode: None
     ```

     where:

     `spec.managedBootImages`
     :   Specifies the parameters for the boot image management feature.

     `spec.managedBootImages.machineManagers.apiGroup`
     :   Specifies the API group. This must be `machine.openshift.io`.

     `spec.managedBootImages.machineManagers.resource`
     :   Specifies that the `selection.mode` parameter applies to worker nodes when a value of `machinesets` is set.

     `spec.managedBootImages.machineManagers.selection.mode`
     :   When `None`, specifies that the feature is disabled for the specified machine sets.
   * Disable the feature for nodes in the control plane machine sets by adding the following parameters:

     ```
     apiVersion: operator.openshift.io/v1
     kind: MachineConfiguration
     metadata:
       name: cluster
     spec:
     # ...
       managedBootImages:
         machineManagers:
         - apiGroup: machine.openshift.io
           resource: controlplanemachinesets
           selection:
             mode: None
     ```

     where:

     `spec.managedBootImages`
     :   Specifies the parameters for the boot image management feature.

     `spec.managedBootImages.machineManagers.apiGroup`
     :   Specifies the API group. This must be `machine.openshift.io`.

     `spec.managedBootImages.machineManagers.resource`
     :   Specifies that the `selection.mode` parameter applies to control plane nodes when a value of `controlplanemachinesets` is set.

     `spec.managedBootImages.machineManagers.selection.mode`
     :   When `None`, specifies that the feature is disabled for the specified machine sets.

**Verification**

* View the current state of the boot image management feature by using the following command to view the machine configuration object:

  ```
  $ oc get machineconfiguration cluster -o yaml
  ```

  **Example machine set with the boot image reference**

  ```
  kind: MachineConfiguration
  metadata:
    name: cluster
  # ...
  status:
    conditions:
    - lastTransitionTime: "2025-05-01T20:11:49Z"
      message: Reconciled 2 of 4 MAPI MachineSets | Reconciled 0 of 0 CAPI MachineSets
        | Reconciled 0 of 0 CAPI MachineDeployments
      reason: BootImageUpdateConfigurationUpdated
      status: "True"
      type: BootImageUpdateProgressing
    - lastTransitionTime: "2025-05-01T19:30:13Z"
      message: 0 Degraded MAPI MachineSets | 0 Degraded CAPI MachineSets | 0 CAPI MachineDeployments
      reason: BootImageUpdateConfigurationUpdated
      status: "False"
      type: BootImageUpdateDegraded
    managedBootImagesStatus:
      machineManagers:
      - apiGroup: machine.openshift.io
        resource: controlplanemachinesets
        selection:
          mode: None
      - apiGroup: machine.openshift.io
        resource: machinesets
        selection:
          mode: All
  ```

  where:

  `status.managedBootImagesStatus.machineManagers.selection.mode`
  :   Specifies that the boot image management feature is disabled when set to `None`. In this example, the boot image management feature is disabled for control plane machine sets and enabled for worker machine sets.

## [Chapter 7. Boot image skew enforcement](#mco-update-boot-skew-mgmt) Copy linkLink copied to clipboard!

You can use boot image skew enforcement to help ensure that the boot images in a cluster are up-to-date with the OpenShift Container Platform and RHCOS version being used in the cluster. Using an older boot image could cause issues when scaling new nodes. If the images are older than a predetermined version, the MCO disables cluster upgrades until it deems the boot images to be compliant.

Note

Boot image skew enforcement is not supported for single-node OpenShift clusters.

### [7.1. About boot image skew enforcement](#mco-update-boot-skew-mgmt-about_mco-update-boot-skew-mgmt) Copy linkLink copied to clipboard!

Using boot image skew enforcement, you can ensure that the boot images in a cluster are up-to-date with the OpenShift Container Platform and RHCOS version being used in the cluster. Making sure that your boot images are current can help you avoid the problems associated with running older images.

When boot image skew enforcement is active in a cluster, the Machine Config Operator (MCO) examines the boot image version reported in the `MachineConfiguration` object to determine if that boot image is appropriate for the cluster. If the boot image version is too old, the Operator reports that *boot image version skew* is detected and blocks cluster updates until you manually update the boot image or disable boot image skew enforcement by setting the `None` mode, as described in this section.

The limit for boot image version skew is set within the MCO and cannot be modified.

For information on manually configuring the boot image in your cluster, see "Manually updating the boot image".

#### [7.1.1. About boot image skew enforcement modes](#mco-update-boot-skew-mgmt-about-modes_mco-update-boot-skew-mgmt) Copy linkLink copied to clipboard!

Review the following information to learn about the boot image skew enforcement modes. Use the information to determine the best method for your cluster.

Boot image skew enforcement operates in one of the following modes:

Automatic
:   When set to `Automatic`, with boot image management also enabled, if the cluster is updated from one OpenShift Container Platform version to the next, the MCO automatically updates the boot image version in the `MachineConfiguration` object and tests the boot image version for skew.

    Note

    In OpenShift Container Platform 4.22, the automatic mode is available only for AWS, Google Cloud, Azure, and vSphere clusters and is the default for these platforms.

    The MCO automatically configures this mode when the following conditions are met:

    * Boot image management is available for the platform that your cluster uses. Currently boot image management is available for only AWS, Google Cloud, Azure, and vSphere clusters.
    * You have enabled boot image management for compute machine sets.
    * You have not set skew enforcement to the manual or none mode.

    For information on boot image management, see "Boot image management".

    **Example `MachineConfiguration` object with automatic skew enforcement**

    ```
    apiVersion: operator.openshift.io/v1
    kind: MachineConfiguration
    metadata:
      name: cluster
    status:
    # ...
      bootImageSkewEnforcementStatus:
        automatic:
          ocpVersion: 4.22.0
        mode: Automatic
    ```

    The MCO examines the boot image reported in the `ocpVersion` parameter to determine if the cluster is violating the boot image version skew limits.

Manual
:   When set to `Manual`, if the boot image version is updated, a cluster administrator is responsible for manually updating the `MachineConfiguration` object with the RHCOS version of the new boot image or the OpenShift Container Platform version associated with the new boot image. The MCO then tests the boot image version for skew.

    **Example `MachineConfiguration` object with skew enforcement based on an RHCOS version**

    ```
    apiVersion: operator.openshift.io/v1
    kind: MachineConfiguration
    metadata:
      name: cluster
    # ...
    spec:
      bootImageSkewEnforcement:
        mode: Manual
        manual:
          mode: RHCOSVersion
          rhcosVersion: 9.2.20251023-0
    # ...
    status:
      bootImageSkewEnforcementStatus:
        manual:
          mode: RHCOSVersion
          rhcosVersion: 9.2.20251023-0
        mode: Manual
    ```

    **Example `MachineConfiguration` object with skew enforcement based on an OpenShift Container Platform version**

    ```
    apiVersion: operator.openshift.io/v1
    kind: MachineConfiguration
    metadata:
      name: cluster
    # ...
    spec:
      bootImageSkewEnforcement:
        manual:
          mode: OCPVersion
          ocpVersion: 4.22.0
        mode: Manual
    # ...
    status:
      bootImageSkewEnforcementStatus:
        manual:
          mode: OCPVersion
          ocpVersion: 4.22.0
        mode: Manual
    ```

    The MCO examines the boot image reported in the `rhcosVersion` or `ocpVersion` parameter to determine if the cluster is violating the boot image version skew limits.

None
:   When set to `None`, boot image skew enforcement is disabled. When disabled, the MCO does not monitor for boot image skew and does not report if new nodes are provisioned with older boot images, which could introduce issues when scaling new nodes.

    **Example `MachineConfiguration` object with skew enforcement disabled**

    ```
    apiVersion: operator.openshift.io/v1
    kind: MachineConfiguration
    metadata:
      name: cluster
    # ...
    spec:
      bootImageSkewEnforcement:
        mode: None
    # ...
    status:
      bootImageSkewEnforcementStatus:
        mode: None
    ```

    When in the none mode, the MCO reports a Prometheus alert that skew enforcement is disabled and that scale-up might run into issues due to old boot images. The alert does not cause any functional issues for the cluster.

    Single-node OpenShift clusters default to the none mode regardless of platform, because they do not scale. The skew enforcement Prometheus alert is not reported for single-node OpenShift clusters.

    Bare-metal clusters running OpenShift Container Platform version 4.10 and later do not use the MCO to keep their boot images up-to-date. Skew enforcement defaults to the none mode and the skew enforcement Prometheus alert mentioned is not reported. For bare-metal clusters running OpenShift Container Platform version 4.9 and earlier, you need to perform a one-time action to migrate to the 4.10 system, this is explained further in the bare metal boot image update docs. For information, see "Manually updating the boot image".

### [7.2. Configuring boot image skew enforcement](#mco-update-boot-skew-mgmt-configuring_mco-update-boot-skew-mgmt) Copy linkLink copied to clipboard!

You can configure the current boot image skew enforcement mode that the Machine Config Operator (MCO) uses. By configuring the boot image skew enforcement mode, you can determine if the boot image version in the `MachineConfiguration` object is updated automatically or manually.

Alternatively, you can disable boot image skew enforcement by setting the `mode` to `None`. When disabled, the MCO does not monitor for boot image skew, and older boot images could be used, possibly introducing issues when scaling new nodes.

In OpenShift Container Platform 4.22, the automatic mode is available only for AWS, Google Cloud, Azure, and vSphere clusters and is the default for these platforms. If you modify a cluster from the automatic mode to the manual or none mode, you can revert a cluster back to automatic mode only by removing the `bootImageSkewEnforcement` stanza from the `MachineConfiguration` object.

All other platforms default to manual mode with the OpenShift Container Platform version set as the boot image version in the `MachineConfiguration` object. In manual mode, you are expected to manually update the `MachineConfiguration` object with new boot image version whenever you update the boot image.

**Procedure**

1. For manual mode, you can obtain the current boot image on a node by using the following command:

   ```
   $ oc debug node/<new-node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
   ```

   **Example output**

   ```
   # ...
       "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251023-0-ostree.x86_64.ociarchive",
       "version": "9.6.20251023-0"
   ```

   You should use the newest node on the cluster, because the boot image might have been updated after the older nodes were created. Ideally, test the newest node from each machine set and use the oldest boot image among them.
2. Specify the boot image skew enforcement mode and set the boot image version as needed:

   ```
   apiVersion: operator.openshift.io/v1
   kind: MachineConfiguration
   metadata:
     name: cluster
   spec:
   # ...
     bootImageSkewEnforcement:
       mode: Manual
       manual:
         mode: RHCOSVersion
         rhcosVersion: 9.6.20251023-0
   # ...
   ```

   where:

   `spec.bootImageSkewEnforcement.mode`
   :   Specifies the boot image enforcement mode, one of the following values:

       * `Manual`. Specifies that boot image skew management is in manual mode. You must specify the `spec.bootImageSkewEnforcement.manual` parameters.
       * `None`. Specifies that boot image skew management is disabled. You do not need to specify the `spec.bootImageSkewEnforcement.manual` parameters.

   `spec.bootImageSkewEnforcement.manual.mode`
   :   Specifies the version you want to represent the current boot image, either `OCPVersion` or `RHCOSVersion`. You must include one of the following parameters:

       * For `RHCOSVersion`, use `spec.bootImageSkewEnforcement.manual.rhcosVersion` to specify the RHCOS version that is being used as a boot image in the `[major].[minor].[datestamp(YYYYMMDD)]-[buildnumber]` or `[major].[minor].[timestamp(YYYYMMDDHHmm)]-[buildnumber]` format. This field must be between 14 and 21 characters.
       * For `OCPVersion`, use `spec.bootImageSkewEnforcement.manual.ocpVersion` to specify the OpenShift Container Platform version associated with the boot image that is being used in the `x.y.z` format. This field must be between 5 and 10 characters.

### [7.3. Updating the boot image skew enforcement version](#mco-update-boot-skew-mgmt-updating.adoc_mco-update-boot-skew-mgmt) Copy linkLink copied to clipboard!

If you are running boot image skew enforcement in the manual mode, you must manually update the boot image version in the `MachineConfiguration` object each time you update the boot image in your cluster. With the boot image updated in the `MachineConfiguration` object, the Machine Config Operator (MCO) can properly perform boot image skew enforcement to ensure that your nodes are up-to-date.

**Procedure**

1. If necessary, obtain the RHCOS or OpenShift Container Platform version of the current boot image on an updated node by using one of the following commands:

   * Obtain the RHCOS version by running the following command:

     ```
     $ oc debug node/<new-node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
     ```

     **Example output**

     ```
     # ...
         "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251023-0-ostree.x86_64.ociarchive",
         "version": "9.6.20251023-0"
     ```
   * Obtain the OpenShift Container Platform version by running the following command:

     ```
     $ openshift-install version
     ```

     Ensure that you use the same `openshift-install` binary that you used when updating the boot image.

     **Example output**

     ```
     openshift-install 4.22.0
     ```
2. Specify the boot image version in the `MachineConfiguration` object with either the RHCOS or OpenShift Container Platform version:

   * Update the `MachineConfiguration` object with the RHCOS version:

     ```
     apiVersion: operator.openshift.io/v1
     kind: MachineConfiguration
     metadata:
       name: cluster
     # ...
     spec:
       bootImageSkewEnforcement:
         mode: Manual
         manual:
           mode: RHCOSVersion
           rhcosVersion: 9.2.20251023-0
     # ...
     ```

     If the `spec.bootImageSkewEnforcement.manual.mode` is `RHCOSVersion`, specify the RHCOS version of the boot image with the `rhcosVersion` parameter, as shown in the example.
   * Update the `MachineConfiguration` object with the OpenShift Container Platform version

     ```
     apiVersion: operator.openshift.io/v1
     kind: MachineConfiguration
     metadata:
       name: cluster
     # ...
     spec:
       bootImageSkewEnforcement:
         mode: Manual
         manual:
           mode: OCPVersion
           ocpVersion: 4.22.0
     # ...
     ```

     If the `spec.bootImageSkewEnforcement.manual.mode` is `OCPVersion`, specify the OpenShift Container Platform version of the boot image with the `ocpVersion` parameter, as shown in the example.

## [Chapter 8. Manually updating the boot image](#mco-update-boot-images-manual) Copy linkLink copied to clipboard!

For OpenShift Container Platform platforms that do not support automatic boot image updating or for clusters configured with the boot image management feature disabled, you can manually update the boot image used by the compute nodes in your cluster. By updating the boot image, you can ensure that newly scaled up nodes are able to successfully use the latest Red Hat Enterprise Linux CoreOS (RHCOS) version and join the cluster.

Note

Red Hat does not support manually updating the boot image in control plane nodes.

### [8.1. Manually updating the boot image on an Azure cluster](#mco-update-boot-images-azure_mco-update-boot-images-manual) Copy linkLink copied to clipboard!

You can manually update the boot image for your Microsoft Azure cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly.

Note

Boot image updates are not supported for Azure confidential virtual machines and Azure Stack Hub clusters. Contact Red Hat Support for these cases.

Use the following procedure to create environment variables that facilitate running the required commands, identify the correct boot image to use as the new boot image, and modify your compute machine sets to use that image.

The process requires you to determine the product variant and Hyper-V generation of your Azure boot image. The following procedure helps determine both values, which you need in order to look up the target image.

Note

For clusters that use a default Red Hat Enterprise Linux CoreOS (RHCOS), Azure Red Hat OpenShift (ARO), or Azure Marketplace image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement".

**Prerequisites**

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2).
* You have installed the OpenShift CLI (`oc`).
* You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement".
* You have disabled boot image management for the cluster. For more information, see "Disabling boot image management".
* You have downloaded the latest version of the OpenShift Container Platform installation program from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program."
* You have installed the [`jq`](https://stedolan.github.io/jq/) program.

**Procedure**

1. Set an environment variable with your cluster architecture by running the following command:

   ```
   $ export ARCH=<architecture_type>
   ```

   Replace `<architecture_type>` with one of the following values:

   * Use `aarch64` for the AArch64 or ARM64 architecture.
   * Use `x86_64` for the x86\_64 or AMD64 architecture.

   You can find the architecture as a label in any `MachineSet` object.

   **Example machine set with an architecture label**

   ```
   apiVersion: machine.openshift.io/v1beta1
   kind: MachineSet
   metadata:
     annotations:
       capacity.cluster-autoscaler.kubernetes.io/labels: kubernetes.io/arch=amd64
   # ...
   ```
2. Determine your Azure image variant and Hyper-V generation:

   1. Obtain the required values from your machine set by running the following command:

      ```
      $ oc get machineset <machineset-name> -n openshift-machine-api \
        -o jsonpath='{.spec.template.spec.providerSpec.value.image}'
      ```

      **Example output**

      ```
      {"offer":"rh-ocp-worker","publisher":"redhat","resourceID":"","sku":"rh-ocp-worker","type":"MarketplaceWithPlan","version":"4.16.20231023"}
      ```
   2. Determine your image variant by comparing the output to the entries in the following table:

      Expand

      | Output parmeters | Variant |
      | --- | --- |
      | `resourceID` is non-empty | `no-purchase-plan` |
      | `publisher` is `azureopenshift` | `no-purchase-plan` |
      | `publisher` is `redhat` and `offer` is `rh-ocp-worker` | `ocp` |
      | `publisher` is `redhat` and `offer` is `rh-opp-worker` | `opp` |
      | `publisher` is `redhat` and `offer` is `rh-oke-worker` | `oke` |
      | `publisher` is `redhat-limited` and `offer` is `rh-ocp-worker` | `ocp-emea` |
      | `publisher` is `redhat-limited` and `offer` is `rh-ocp-worker` | `opp-emea` |
      | `publisher` is `redhat-limited` and `offer` is `rh-ocp-worker` | `oke-emea` |

      Show more

      Make note of the variant for later use.
   3. Determine your image Hyper-V generation by comparing the output to the entries in the following table:

      Expand

      | Output | Image type | Hyper-V generation |
      | --- | --- | --- |
      | `resourceID` is non-empty | Legacy uploaded | * `hyperVGen2` if the `resourceID` value contains `gen2` * `hyperVGen1` if the `resourceID` value does not contain `gen2` |
      | `publisher` is `azureopenshift` | Unpaid marketplace | * `hyperVGen2` if `sku` contains `v2` or the cluster architecture is AArch64 or ARM64 * `hyperVGen1` for all other images |
      | `publisher` is `redhat` or `redhat-limited`. | Paid marketplace | * `hyperVGen1` if `sku` contains `-gen1` * `hyperVGen2` for all other images |

      Show more

      Make note of the generation for later use.
   4. Optional: You can compare the output of the `version` parameter against the output of the following command to determine if your boot image needs updating.

      ```
      $ openshift-install coreos print-stream-json | jq '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"'
      ```

      `ARCH` is the environment variable you created in a previous step.

      In the output of the command, locate your variant and generation as shown in the following example:

      **Example output**

      ```
        "ocp": {
      # ...
          "hyperVGen2": {
            "publisher": "redhat",
            "offer": "rh-ocp-worker",
            "sku": "rh-ocp-worker",
            "version": "4.18.2025031114"
      ```

      If the boot image referenced in the `version` parameter of your machine set matches or is later than the version in this output, no further action on your part is required to update the boot image. If not, continue with this procedure.
3. Obtain the values needed to identify the new boot image and set the values as environment variables:

   1. Obtain the values required for the new boot image by running the following command:

      ```
      $ openshift-install coreos print-stream-json | jq '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"'
      ```

      `ARCH` is the environment variable you created in a previous step.
   2. In the output of the command, locate your variant and generation as shown in the following example:

      **Example output**

      ```
        "ocp": {
        # ...
          "hyperVGen2": {
            "publisher": "redhat",
            "offer": "rh-ocp-worker",
            "sku": "rh-ocp-worker",
            "version": "9.6.20251015"
      ```
   3. Set an environment variable with your image variant by running the following command:

      ```
      $ export VARIANT=<variant>
      ```

      Replace `<variant>` with the variant of your image, one of the following vales: `no-purchase-plan`, `ocp`, `opp`, `oke`, `ocp-emea`, `opp-emea`, or `oke-emea`.
   4. Set an environment variable with your image generation by running the following command:

      ```
      $ export GEN=<generation>
      ```

      Replace `<generation>` with the generation of your image, one of the following vales: `hyperVGen1` or `hyperVGen2`.
   5. Set environment variables for the `publisher`, `offer`, `sku`, and `version` fields based on the `openshift-install` output for your variant and generation by running the following commands:

      ```
      $ export PUBLISHER=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".publisher')
      ```

      `ARCH`, `VARIANT`, and `GEN` are environment variables you created in a previous step.

      ```
      $ export OFFER=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".offer')
      ```

      ```
      $ export SKU=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".sku')
      ```

      ```
      $ export VERSION=$(openshift-install coreos print-stream-json | jq -r '.architectures."'"${ARCH}"'"."rhel-coreos-extensions"."marketplace"."azure"."'"${VARIANT}"'"."'"${GEN}"'".version')
      ```
   6. Obtain the RHCOS version by running the following command:

      ```
      $ echo $VERSION
      ```

      **Example output**

      ```
      9.6.20251015
      ```

      Make note of the RHCOS version for later use.
   7. Set an environment variable with the type of your image by running the following command:

      ```
      $ export IMAGE_TYPE=<image_type>
      ```

      Replace `<image_type>` with one of the following values based on the variant of your image:

      * For the `no-purchase-plan` variant, use `MarketplaceNoPlan`.
      * For all other variants, use `MarketplaceWithPlan`.
4. Update each of your compute machine sets to include the new boot image:

   1. Obtain the name of your machine sets for use in the following step by running the following command:

      ```
      $ oc get machineset -n openshift-machine-api
      ```

      **Example output**

      ```
      NAME                                        DESIRED   CURRENT   READY   AVAILABLE   AGE
      ci-ln-lbf9h9k-1d09d-fwh4l-worker-eastus21   1         1         1       1           135m
      ci-ln-lbf9h9k-1d09d-fwh4l-worker-eastus22   1         1         1       1           135m
      ci-ln-lbf9h9k-1d09d-fwh4l-worker-eastus23   1         1         1       1           135m
      ```
   2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:

      ```
      $ oc patch machineset <machineset-name> -n openshift-machine-api --type merge \
        -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":{"publisher":"'${PUBLISHER}'","offer":"'${OFFER}'","sku":"'${SKU}'","version":"'${VERSION}'","resourceID":"","type":"'${IMAGE_TYPE}'"}}}}}}}'
      ```

      `PUBLISHER`, `OFFER`, `SKU`, `VERSION`, and `IMAGE_TYPE` are environment variables you created in previous steps.
5. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

**Verification**

1. Scale up a machine set to check that the new node is using the new boot image:

   1. Increase the machine set replicas by one to trigger a new machine by running the following command:

      ```
      $ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
      ```

      where:

      `<count>`
      :   Specifies the total number of replicas, including any existing replicas, that you want for this machine set.

      `<machineset_name>`
      :   Specifies the name of the machine set to scale.
   2. Optional: View the status of the machine set as it provisions by running the following command:

      ```
      $ oc get machines.machine.openshift.io -n openshift-machine-api -w
      ```

      It can take several minutes for the machine set to achieve the `Running` state.
   3. Verify that the new node has been created and is in the `Ready` state by running the following command:

      ```
      $ oc get nodes
      ```
2. Verify that the new node is using the new boot image by running the following command:

   ```
   $ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
   ```

   Replace `<new_node>` with the name of your new node.

   **Example output**

   ```
   {
   # ...
       "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251015-ostree.x86_64.ociarchive",
       "version": "9.6.20251015"
   }
   ```

   where:

   `version`
   :   Specifies the boot image version.
3. Verify that the boot image is the same the RHCOS version as the image you noted in a previous step by running the following command:

   ```
   $ echo $VERSION
   ```

   **Example output**

   ```
   9.6.20251015
   ```

### [8.2. Manually updating the boot image on an AWS cluster](#mco-update-boot-images-aws_mco-update-boot-images-manual) Copy linkLink copied to clipboard!

You can manually update the boot image for your Amazon Web Services (AWS) cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly.

Use the following procedure to create environment variables that facilitate running the required commands, identify the correct Amazon Machine Image (AMI) to use as the new boot image, and modify your compute machine sets to use that image.

The process differs for clusters that use a default Red Hat Enterprise Linux CoreOS (RHCOS) image and clusters that use a custom RHCOS image from the AWS Marketplace. The following procedure helps determine which type of image you use.

Note

For clusters that use a default RHCOS image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement".

**Prerequisites**

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2).
* You have installed the OpenShift CLI (`oc`).
* You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement".
* You have disabled boot image management for the cluster. For more information, see "Disabling boot image management".
* You have installed the [AWS CLI](https://aws.amazon.com/cli/).
* You configured an AWS account to host the cluster. For information, see "Configuring an AWS account".
* For a cluster that uses a default RHCOS image, ensure you have met the following additional prerequisites:

  + You have downloaded the latest version of the OpenShift Container Platform installation program from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program."
  + For a cluster that uses a default RHCOS image, you have installed the [`jq`](https://jqlang.org/) program.

**Procedure**

1. Determine if your cluster uses a default RHCOS image or a custom RHCOS image from the AWS Marketplace image:

   1. Obtain the current AWS region where the cluster is installed and set the value in an environment variable by running the following command:

      ```
      $ export REGION=$(oc get infrastructure cluster -o jsonpath='{.status.platformStatus.aws.region}')
      ```
   2. Obtain the current Amazon Machine Image (AMI) ID for your region and set the value in an environment variable by running the following command:

      ```
      $ export CURRENT_AMI=$(oc get machineset -n openshift-machine-api -o jsonpath='{.items[0].spec.template.spec.providerSpec.value.ami.id}')
      ```
   3. Obtain the product ID for your AMI and set the value in an environment variable by running the following command:

      ```
      $ export PRODUCT_ID=$(aws ec2 describe-images --image-ids "$CURRENT_AMI" --region "$REGION" \
        --query 'Images[0].Name' --output text | \
        grep -oE '[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}')
      ```

      `CURRENT_AMI` and `REGION` are environment variables you created in previous steps.
   4. Display the contents of the `PRODUCT_ID` environment variable by running the following command:

      ```
      $ echo $PRODUCT_ID
      ```

      * If the output for the `PRODUCT_ID` environment variable is empty, as shown in the following example, your cluster uses a standard OpenShift Container Platform image.

        **Example with empty output**
      * If the output for the `PRODUCT_ID` environment variable is not empty, as shown in the following example, your cluster uses an AWS Marketplace image.

        **Example with non-empty output**

        ```
        59ead7de-2540-4653-a8b0-fa7926d5c845
        ```
      * If the command returns an error, and you are unable to determine your cluster variant, contact Red Hat Support. If Red Hat Support determines that your cluster uses an AWS Marketplace image, you can set the `PRODUCT_ID` environment variable with the appropriate product ID from the following table.

        ```
        $ export PRODUCT_ID=<Product_ID_from_table>
        ```

        Expand

        | Variant | Product ID |
        | --- | --- |
        | [OpenShift Container Platform on x86 - NA](https://aws.amazon.com/marketplace/procurement/?productId=59ead7de-2540-4653-a8b0-fa7926d5c845) | `59ead7de-2540-4653-a8b0-fa7926d5c845` |
        | [OpenShift Kubernetes Engine on x86 - NA](https://aws.amazon.com/marketplace/procurement?productId=963b36c3-de6f-48ed-b802-2b38b2a2cdeb) | `963b36c3-de6f-48ed-b802-2b38b2a2cdeb` |
        | [OpenShift Platform Plus on x86 - NA](https://aws.amazon.com/marketplace/procurement?productId=f5da01a6-d046-487c-9072-42fe53b1cad4) | `f5da01a6-d046-487c-9072-42fe53b1cad4` |
        | [OpenShift Container Platform on ARM - NA](https://aws.amazon.com/marketplace/procurement?productId=abc249f8-7440-45f7-a4b1-c026baff64c1) | `abc249f8-7440-45f7-a4b1-c026baff64c1` |
        | [OpenShift Kubernetes Engine on ARM - NA](https://aws.amazon.com/marketplace/procurement?productId=d2d3ebcd-c1ca-43d8-bf0a-530433200f35) | `d2d3ebcd-c1ca-43d8-bf0a-530433200f35` |
        | [OpenShift Platform Plus on ARM - NA](https://aws.amazon.com/marketplace/procurement?productId=be6d3e94-c8dc-4a3e-9218-4b449b11f06f) | `be6d3e94-c8dc-4a3e-9218-4b449b11f06f` |
        | [OpenShift Container Platform on x86 - EU, ME and Africa](https://aws.amazon.com/marketplace/procurement?productId=962791c7-3ae5-46d1-ba62-c7a5ebac54fd) | `962791c7-3ae5-46d1-ba62-c7a5ebac54fd` |
        | [OpenShift Kubernetes Engine on x86 - EU, ME and Africa](https://aws.amazon.com/marketplace/procurement?productId=7026c8d7-392c-4010-b93c-f93f7bc5495f) | `7026c8d7-392c-4010-b93c-f93f7bc5495f` |
        | [OpenShift Platform Plus on x86 - EU, ME and Africa](https://aws.amazon.com/marketplace/procurement?productId=628c9df3-0254-4f91-bc1f-8619d1b8eaa8) | `628c9df3-0254-4f91-bc1f-8619d1b8eaa8` |

        Show more
2. Determine the AMI for the new boot image by using one of the following steps, depending upon the type of image used in your cluster:

   * For a cluster that uses a default RHCOS image, perform the following steps:

     1. Set an environment variable with your cluster architecture by running the following command:

        ```
        $ export ARCH=<architecture_type>
        ```

        Replace `<architecture_type>` with one of the following values:

        + Specify `aarch64` for the AArch64 or ARM64 architecture.
        + Specify `ppc64le` for the IBM Power® (ppc64le) architecture.
        + Specify `s390x` for the IBM Z® and IBM® LinuxONE (s390x) architecture.
        + Specify `x86_64` for the x86\_64 or AMD64 architecture.

        You can find the architecture as a label in any `MachineSet` object.

        **Example machine set with an architecture label**

        ```
        apiVersion: machine.openshift.io/v1beta1
        kind: MachineSet
        metadata:
          annotations:
            capacity.cluster-autoscaler.kubernetes.io/labels: kubernetes.io/arch=amd64
        # ...
        ```
     2. Obtain the AMI for the new boot image and set an environment variable with the AMI by running the following command:

        ```
        $ export AMI_ID=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.aws.regions.\"${REGION}\".image")
        ```

        `ARCH` and `REGION` are environment variables you created in previous steps.
     3. View the RHCOS version of the new boot image by running the following command:

        ```
        $ openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.aws.regions.\"${REGION}\".release"
        ```

        **Example output**

        ```
        9.6.20251212-1
        ```

        Make note of the RHCOS version for later use.
   * For a cluster that uses a custom RHCOS image, perform the following steps:

     1. Obtain a list of valid AMI images by running the following command:

        ```
        $ aws ec2 describe-images --region "${REGION}" --filters "Name=name,Values=*${PRODUCT_ID}*" \
          --query 'reverse(sort_by(Images, &CreationDate))[].[CreationDate,ImageId,Name]' --output table
        ```

        `REGION` and `PRODUCT_ID` are environment variables you created in previous steps.

        This command returns the AMIs ordered by creation date, with the latest images first. The RHCOS version of each AMI is contained in the AMI name. Choose the latest image version available.

        Make note of the Red Hat Enterprise Linux CoreOS (RHCOS) version for later use.
     2. Set an environment variable with the AMI of the new boot image by running the following command:

        ```
        $ export AMI_ID=<ami-value>
        ```
3. Update each of your compute machine sets to include the new boot image:

   1. Obtain the name of your machine sets for use in the following step by running the following command:

      ```
      $ oc get machineset -n openshift-machine-api
      ```

      **Example output**

      ```
      NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
      rhhdrbk-b5564-4pcm9-worker-0         3         3         3       3           123m
      ci-ln-xj96skb-72292-48nm5-worker-d   1         1         1       1           27m
      ```
   2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:

      ```
      $ oc patch machineset <machineset_name> -n openshift-machine-api --type merge -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"ami":{"id":"'${AMI_ID}'"}}}}}}}'
      ```

      Replace `<machineset_name>` with the name of your machine set.

      `AMI_ID` is the environment variable you created in a previous step.
4. If boot image skew enforcement in your cluster is set to the manual mode, update the boot image version in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version."

**Verification**

1. Scale up a machine set to check that the new node is using the new boot image:

   1. Increase the machine set replicas by one to trigger a new machine by running the following command:

      ```
      $ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
      ```

      where:

      `<count>`
      :   Specifies the total number of replicas, including any existing replicas, that you want for this machine set.

      `<machineset_name>`
      :   Specifies the name of the machine set to scale.
   2. Optional: View the status of the machine set as it provisions by running the following command:

      ```
      $ oc get machines.machine.openshift.io -n openshift-machine-api -w
      ```

      It can take several minutes for the machine set to achieve the `Running` state.
   3. Verify that the new node has been created and is in the `Ready` state by running the following command:

      ```
      $ oc get nodes
      ```
2. Verify that the new node is using the new boot image by running the following command:

   ```
   $ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
   ```

   Replace `<new_node>` with the name of your new node.

   **Example output**

   ```
   {
   # ...
       "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
       "version": "9.6.20251212-1"
   }
   ```

   where:

   `version`
   :   Specifies the boot image version.

### [8.3. Manually updating the boot image on an Google Cloud cluster](#mco-update-boot-images-gcp_mco-update-boot-images-manual) Copy linkLink copied to clipboard!

You can manually update the boot image for your Google Cloud cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly.

Use the following procedure to create environment variables that facilitate running the required commands, identify the correct boot image to use as the new boot image, and modify your machine sets to use that image.

The process differs for clusters that use a default Red Hat Enterprise Linux CoreOS (RHCOS) image, clusters that use a custom Red Hat Enterprise Linux CoreOS (RHCOS) image from the Google Cloud Marketplace, and user-provisioned infrastructure clusters. The following procedure helps determine which type of cluster you have.

For user-provisioned infrastructure Google Cloud clusters, which typically have no Machine API compute machine sets, you can provision new nodes based on the new boot image by updating the underlying Google Cloud infrastructure with the new boot image, such as instance templates, Deployment Manager templates, or Terraform configuration. For more information, see "Creating additional worker machines in Google Cloud".

Note

For clusters that use a default Red Hat Enterprise Linux CoreOS (RHCOS) image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement".

**Prerequisites**

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2).
* You have installed the OpenShift CLI (`oc`).
* You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement".
* You have disabled boot image management for the cluster. For more information, see "Disabling boot image management".
* For a cluster that uses a default RHCOS image, ensure that your cluster meets the following additional prerequisites:

  + You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program."
  + You have installed the [`jq`](https://jqlang.github.io/jq/) program.
* For a user-provisioned infrastructure cluster, ensure that your cluster meets the following additional prerequisites:

  + You have downloaded the latest version of the OpenShift Container Platform installation program from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program."
  + You have installed the [Google Cloud CLI](https://cloud.google.com/sdk/docs/install).
  + You have created a Google Cloud service account.

**Procedure**

1. Determine which image in the machine set is the boot image and set the value in an environment variable:

   1. Set the boot image value in an environment variable by running the following command:

      ```
      $ export BOOT_DISK_INDEX=$(oc get machineset -n openshift-machine-api -o json | \
        jq '.items[0].spec.template.spec.providerSpec.value.disks | map(.boot == true) | index(true)')
      ```
   2. Display the contents of the `BOOT_DISK_INDEX` environment variable by running the following command:

      ```
      $ echo $BOOT_DISK_INDEX
      ```

      **Example output**

      ```
      0
      ```

      If the output for the `BOOT_DISK_INDEX` environment variable is `null`, none of the disks in the machine set has the `boot` field explicitly set. In this case, the boot disk is typically the first disk.

      **Example null output**

      ```
      null
      ```
   3. If the `BOOT_DISK_INDEX` output is `null`, set the boot image to the first image by running the following command:

      ```
      $ export BOOT_DISK_INDEX=0
      ```
2. Determine if your cluster uses a default RHCOS image or a GCP Marketplace RHCOS image from the Google Cloud Marketplace, or is a user-provisioned infrastructure cluster:

   1. Obtain the name of the current boot image and set the name as an environment variable by running the following command:

      ```
      $ export CURRENT_IMAGE=$(oc get machineset -n openshift-machine-api -o json | \
        jq -r ".items[0].spec.template.spec.providerSpec.value.disks[${BOOT_DISK_INDEX}].image")
      ```

      `BOOT_DISK_INDEX` is the environment variable you created in a previous step.
   2. View the name of the image by running the following command:

      ```
      $ echo $CURRENT_IMAGE
      ```

      **Example output**

      ```
      projects/rhcos-cloud/global/images/rhcos-416-94-202510081640-0-gcp-x86-64
      ```
   3. Compare the prefix of the image name to the entries in the following table:

      Expand

      | Current image prefix | Variant |
      | --- | --- |
      | `projects/rhcos-cloud/global/images/` | Default |
      | `projects/redhat-marketplace-public/global/images/` | GCP Marketplace RHCOS image |
      | No machine set present/custom prefix | User-provisioned infrastructure |

      Show more

      Default RHCOS clusters use images from the `rhcos-cloud` project in the `rhcos-<version>-<platform>-<arch>` format.

      GCP Marketplace RHCOS clusters use images from the `redhat-marketplace-public` project in the `redhat-coreos-<offering>-<version>-<arch>-<date>` format.

      Note

      The following images are the latest Google Cloud Marketplace images for the OpenShift Container Platform:

      OpenShift Container Platform
      :   `redhat-coreos-ocp-413-x86-64-202305021736`

      OpenShift Platform Plus
      :   `redhat-coreos-opp-413-x86-64-202305021736`

      OpenShift Kubernetes Engine
      :   `redhat-coreos-oke-413-x86-64-202305021736`

      Red Hat has not published Marketplace images for OpenShift Container Platform later than these OpenShift Container Platform 4.13 images. If the current boot image in your cluster matches one of the listed images, no further action is necessary.
3. Obtain the name of the new boot image by using one of the following steps, depending upon your cluster:

   * For a cluster that uses a default RHCOS image, perform the following steps:

     1. Set an environment variable with your cluster architecture by running the following command:

        ```
        $ export ARCH=<architecture_type>
        ```

        Replace `<architecture_type>` with one of the following values:

        + Specify `aarch64` for the AArch64 or ARM64 architecture.
        + Specify `ppc64le` for the IBM Power® (ppc64le) architecture.
        + Specify `s390x` for the IBM Z® and IBM® LinuxONE (s390x) architecture.
        + Specify `x86_64` for the x86\_64 or AMD64 architecture.

        You can find the architecture as a label in any `MachineSet` object.

        **Example machine set with an architecture label**

        ```
        apiVersion: machine.openshift.io/v1beta1
        kind: MachineSet
        metadata:
          annotations:
            capacity.cluster-autoscaler.kubernetes.io/labels: kubernetes.io/arch=amd64
        # ...
        ```
     2. Set an environment variable with the name of the new boot image by running the following command:

        ```
        $ export GCP_IMAGE=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.name")
        ```

        `ARCH` is the environment variable you created in a previous step.
     3. Set an environment variable with the Google Cloud project of the new boot image by running the following command:

        ```
        $ export GCP_PROJECT=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.project")
        ```

        `ARCH` is the environment variable you created in a previous step.
     4. View the Red Hat Enterprise Linux CoreOS (RHCOS) version of the new boot image by running the following command:

        ```
        $ openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.release"
        ```

        **Example output**

        ```
        9.6.20251212-1
        ```

        Make note of the RHCOS version for later use.
   * For a cluster that uses a GCP Marketplace RHCOS image that is earlier than the 4.13 images listed above, perform the following steps:

     1. Set an environment variable with the name of the new boot image by running the following command:

        ```
        $ export GCP_IMAGE=<image_name>
        ```

        Replace `<image_name>` with one of the following values:

        + Specify `redhat-coreos-ocp-413-x86-64-202305021736` for an OpenShift Container Platform cluster.
        + Specify `redhat-coreos-opp-413-x86-64-202305021736` for an OpenShift Platform Plus cluster.
        + Specify `redhat-coreos-oke-413-x86-64-202305021736` for an OpenShift Kubernetes Engine cluster.
     2. Set an environment variable with the Google Cloud project of the new boot image by running the following command:

        ```
        $ export GCP_PROJECT=redhat-marketplace-public
        ```
   * For a user-provisioned infrastructure cluster, perform the following steps:

     1. Set an environment variable with your cluster architecture by running the following command:

        ```
        $ export ARCH=<architecture_type>
        ```

        Replace `<architecture_type>` with one of the following values:

        + Specify `aarch64` for the AArch64 or ARM64 architecture.
        + Specify `ppc64le` for the IBM Power® (ppc64le) architecture.
        + Specify `s390x` for the IBM Z® and IBM® LinuxONE (s390x) architecture.
        + Specify `x86_64` for the x86\_64 or AMD64 architecture.
     2. Set an environment variable with the name of the new boot image by running the following command:

        ```
        $ export GCP_IMAGE=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.name")
        ```

        `ARCH` is the environment variable you created in a previous step.
     3. Set an environment variable with the Google Cloud project of the new boot image in your cluster by running the following command:

        ```
        $ export GCP_PROJECT=$(openshift-install coreos print-stream-json | jq -r ".architectures.\"${ARCH}\".images.gcp.project")
        ```

        `ARCH` is the environment variable you created in a previous step.

        If the default RHCOS image is not accessible in your environment, for example in a restricted or disconnected environment, you could download the new boot image tar file and upload the file as a custom image to your own Google Cloud project before updating your Google Cloud instance templates.

        Update your Google Cloud instance template(s) to reference the new image, then create new instances from the updated template. The exact steps depend on how your infrastructure was provisioned. For more information, see "Creating additional worker machines in Google Cloud".

        After creating the new instances, you can proceed to the verification steps, unless your user-provisioned infrastructure cluster has any Machine API machine sets, such as for Day-2 scaling. You can update those machine sets as described in the following steps.
4. Update each of your compute machine sets to include the new boot image:

   1. Obtain the name of your machine sets for use in the following step by running the following command:

      ```
      $ oc get machineset -n openshift-machine-api
      ```

      **Example output**

      ```
      NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
      ci-ln-xw7zmyt-72292-x7nqv-worker-a   1         1         1       1           53m
      ci-ln-xw7zmyt-72292-x7nqv-worker-b   1         1         1       1           53m
      ci-ln-xw7zmyt-72292-x7nqv-worker-c   1         1         1       1           53m
      ```
   2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:

      ```
      $ oc patch machineset <machineset-name> -n openshift-machine-api --type json \
        -p '[{"op": "replace", "path": "/spec/template/spec/providerSpec/value/disks/'${BOOT_DISK_INDEX}'/image", "value": "projects/'${GCP_PROJECT}'/global/images/'${GCP_IMAGE}'"}]'
      ```

      Replace `<machineset_name>` with the name of your machine set.

      `BOOT_DISK_INDEX`, `GCP_PROJECT`, and `GCP_IMAGE` are environment variables you created in previous steps.
5. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

**Verification**

1. Scale up a machine set to check that the new node is using the new boot image:

   1. Increase the machine set replicas by one to trigger a new machine by running the following command:

      ```
      $ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
      ```

      where:

      `<count>`
      :   Specifies the total number of replicas, including any existing replicas, that you want for this machine set.

      `<machineset_name>`
      :   Specifies the name of the machine set to scale.
   2. Optional: View the status of the machine set as it provisions by running the following command:

      ```
      $ oc get machines.machine.openshift.io -n openshift-machine-api -w
      ```

      It can take several minutes for the machine set to achieve the `Running` state.
   3. Verify that the new node has been created and is in the `Ready` state by running the following command:

      ```
      $ oc get nodes
      ```
2. Verify that the new node is using the new boot image by running the following command:

   ```
   $ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
   ```

   Replace `<new_node>` with the name of your new node.

   **Example output**

   ```
   {
   # ...
       "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
       "version": "9.6.20251212-1"
   }
   ```

   where:

   `version`
   :   Specifies the boot image version.
3. Verify that the boot image is the same the RHCOS version as the image you noted in a previous step by running the following command:

   ```
   $ echo $GCP_IMAGE
   ```

   `RHCOS_URL` is the environment variable you created in a previous step.

   **Example output**

   ```
   https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-9.6/builds/9.6.20251212-1/x86_64/rhcos-9.6.20251212-1-nutanix.x86_64.qcow2
   ```

### [8.4. Manually updating the boot image on a bare-metal cluster](#mco-update-boot-images-ibm-bare-metal_mco-update-boot-images-manual) Copy linkLink copied to clipboard!

For a bare-metal cluster that was installed with OpenShift Container Platform version 4.9 or earlier, you need to change how the cluster provisions new nodes in order to update the boot image used with those nodes. Using an up-to-date boot image ensures that any new nodes can scale up properly.

Note

The standard boot image management feature is not supported for bare-metal clusters.

If your bare-metal cluster was installed with OpenShift Container Platform version 4.10 or later, boot images are kept current by the Cluster Version Operator (CVO) and are not at risk of boot image skew. Skew enforcement is disabled for the cluster by default. No further action on your part is required to maintain the boot image versioning.

If your bare-metal cluster was installed with OpenShift Container Platform version 4.9 or earlier, the cluster is using the legacy qcow2-based provisioning method. Boot images in these clusters are not managed by the CVO and could be significantly out of date. Follow the steps below to migrate the cluster to use the `machine-os-images` provisioning method, which was introduced in OpenShift Container Platform 4.10. This migration ensures that the cluster always uses the release version as the boot image when a scale-up is taking place.

Use the following procedure to enable the `install_coreos` deployment method and disable the qcow2 image cache. With these changes, the Cluster Baremetal Operator (CBO) will use the `machine-os-images` container from the release payload for new node provisioning. The cluster will have no skew risk, the same as a cluster at version 4.10 or later. Skew enforcement is automatically disabled after the migration is complete.

Note

Boot image updates are not required for Agent-based Installer clusters. The boot image for Agent-based Installer nodes is generated from the current release payload through the `oc adm node-image create` command and does not have skew issues.

**Prerequisites**

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2).
* You have the OpenShift CLI (`oc`) installed.
* A new physical host must be registered and in the `available` state and an associated `BareMetalHost` object must be present in the `openshift-machine-api` namespace so that you can scale a new machine to verify the procedure.

**Procedure**

1. Check whether your cluster is using the legacy boot image provisioning path by running the following command:

   ```
   $ oc get provisioning provisioning-configuration \
     -o jsonpath='{.spec.provisioningOSDownloadURL}'
   ```

   * If the output is non-empty, your cluster was installed with OpenShift Container Platform version 4.9 or earlier. Boot images are not managed by the Cluster Version Operator (CVO) and could be significantly out of date. Follow the steps in this procedure to migrate to the current provisioning path.
   * If the output is empty, your cluster was installed with OpenShift Container Platform version 4.10 or later. Boot images are kept current by the Cluster Version Operator (CVO) and are not at risk of skew. Skew enforcement is disabled for this cluster. No further action on your part is required to maintain the boot image versioning.
2. Clear the legacy image fields and enable the `install_coreos` deployment method:

   1. Migrate each machine set to the `machine-os-images` provisioning path by running the following command:

      ```
      $ oc patch machineset <machineset_name> -n openshift-machine-api --type merge \
        -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"customDeploy":{"method":"install_coreos"},"image":{"url":"","checksum":""}}}}}}}'
      ```

      Replace `<machineset_name>` with the name of your machine set.
   2. Clear the legacy download URL by running the following command:

      ```
      $ oc patch provisioning provisioning-configuration --type=merge -p '{"spec":{"provisioningOSDownloadURL":""}}'
      ```

      This process migrates the cluster to the `machine-os-images` provisioning method, which ensures that the latest boot image is used for scaling nodes.

**Verification**

1. Scale up a machine set to check that the new node is using the new boot image:

   1. Increase the machine set replicas by one to trigger a new machine by running the following command:

      ```
      $ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
      ```

      where:

      `<count>`
      :   Specifies the total number of replicas, including any existing replicas, that you want for this machine set.

      `<machineset_name>`
      :   Specifies the name of the machine set to scale.
   2. Optional: View the status of the machine set as it provisions by running the following command:

      ```
      $ oc get machines.machine.openshift.io -n openshift-machine-api -w
      ```

      It can take several minutes for the machine set to achieve the `Running` state.
   3. Verify that the new node has been created and is in the `Ready` state by running the following command:

      ```
      $ oc get nodes
      ```
2. Verify that the new node is using the new boot image by running the following command:

   ```
   $ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
   ```

   Replace `<new_node>` with the name of your new node.

   **Example output**

   ```
   {
   # ...
       "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
       "version": "9.6.20251212-1"
   }
   ```

   where:

   `version`
   :   Specifies the boot image version.

### [8.5. Manually updating the boot image on an IBM Cloud(R) cluster](#mco-update-boot-images-ibm-cloud_mco-update-boot-images-manual) Copy linkLink copied to clipboard!

For an IBM Cloud cluster, you can manually update the boot image for the compute nodes in your cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to help ensure any new nodes can scale up properly.

Note

The standard boot image management feature is not supported for IBM Cloud clusters.

The following procedure, which includes steps to create environment variables that facilitate running the required commands, shows how to obtain IBM Cloud authentication credentials, download a boot image, upload that image to the IBM Cloud image service, and modify your compute machine sets to use the new boot image.

This procedure uses the default IBM Cloud Cloud Object Storage (COS) bucket in your cluster, which was created during cluster installation. Each COS bucket has a specific Cloud Resource Name (CRN), which the IBM Cloud CLI uses the to select the correct COS bucket. The following procedure shows how to obtain the CRN for the default COS bucket. For more information on the CRN, see [Cloud Resource Names in the IBM Cloud documentation](https://cloud.ibm.com/docs/account?topic=account-crn).

**Prerequisites**

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2).
* You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program."
* You have the OpenShift CLI (`oc`) installed.
* You have the [IBM Cloud CLI](https://cloud.ibm.com/docs/cli?topic=cli-getting-started) installed.
* You have installed the IBM Cloud Virtual Private Cloud (VPC) CLI plugin.
* You have installed the IBM Cloud Object Storage plugin.

**Procedure**

1. Obtain the resource group and region from the `infrastructure` object and set the values in an environment variable by running the following commands:

   ```
   $ export RESOURCE_GROUP=$(oc get infrastructure cluster -o jsonpath='{.status.infrastructureName}')
   ```

   ```
   $ export REGION=$(oc get infrastructure cluster -o jsonpath='{.status.platformStatus.ibmcloud.location}')
   ```
2. Generate an IBM Cloud API key and log in to your IBM Cloud:

   1. Follow the instructions in [Creating your IBM Cloud API key in the IBM Cloud](https://www.ibm.com/docs/en/masv-and-l/cd?topic=cli-creating-your-cloud-api-key) documentation to generate the API key.

      To ensure that the key has the appropriate permissions, you must use the same IBM Cloud account used to create the OpenShift Container Platform cluster when generating the key.
   2. Set the API key in an environment variable by running the following command:

      ```
      $ export IBM_API_KEY=<Your_IBM_Cloud_API_Key>
      ```
   3. Log in to your IBM Cloud by running the following command:

      ```
      $ ibmcloud login --apikey ${IBM_API_KEY} -r ${REGION} -g ${RESOURCE_GROUP}
      ```

      `IBM_API_KEY`, `REGION`, and `RESOURCE_GROUP` are environment variables you created in previous steps.

      **Example output**

      ```
      API endpoint: https://cloud.ibm.com
      Authenticating...
      Retrieving API key token...
      OK

      Targeted account OpenShift-QE (xxxxxxxxxxxxxxxx) <-> xxxxxx

      Targeted resource group xxxxxxx-ibm3h-9pbgg

      Targeted region eu-gb

      API endpoint:     https://cloud.ibm.com
      Region:           eu-gb
      User:             xxxxx
      Account:          xxxxx
      Resource group:   xxxxx
      ```
3. Obtain the URL of the RHCOS image to use as the boot image and set the location in an environment variable by running one of the following commands, based on your cluster architecture:

   * Linux (x86\_64, amd64):

     ```
     $ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.artifacts.ibmcloud.formats["qcow2.gz"].disk.location')
     ```
   * Linux on IBM Z® and IBM® LinuxONE (s390x):

     ```
     export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.s390x.artifacts.ibmcloud.formats["qcow2.gz"].disk.location')
     ```
4. Obtain the boot image:

   1. Download the image by using the following command:

      ```
      $ curl -L -o /tmp/rhcos-new.qcow2.gz "${RHCOS_URL}"
      ```

      `RHCOS_URL` is the environment variable you created in a previous step.
   2. Decompress the downloaded image by running the following command:

      ```
      $ gunzip /tmp/rhcos-new.qcow2.gz
      ```
5. Upload the boot image to the default IBM Cloud Cloud Object Storage (COS) bucket:

   1. Obtain the CRN for your COS bucket and set the CRN in an environment variable by running the following command:

      ```
      $ export COS_CRN=$(ibmcloud resource service-instance "${RESOURCE_GROUP}-cos" --output json | jq -r '.[0].crn')
      ```
   2. Optional: Check that the CRN is correct by running the following command:

      ```
      $ echo ${COS_CRN}
      ```
   3. Configure the default COS bucket with the CRN by running the following command:

      ```
      $ ibmcloud cos config crn --crn "${COS_CRN}"
      ```

      `COS_CRN` is the environment variable you created in a previous step.
   4. Upload the boot image to the COS bucket by running the following command:

      ```
      $ ibmcloud cos object-put --bucket "${RESOURCE_GROUP}-vsi-image" --key "rhcos-new.qcow2" --body /tmp/rhcos-new.qcow2 --region "${REGION}"
      ```

      `RESOURCE_GROUP` and `REGION` are environment variables you created in previous steps.
   5. Optional: Check that image was uploaded to the COS bucket by running the following command:

      ```
      $ ibmcloud cos objects --bucket "${RESOURCE_GROUP}-vsi-image" --region "${REGION}"
      ```

      `RESOURCE_GROUP` and `REGION` are environment variables you created in previous steps.

      **Example output**

      ```
      OK
      Found 2 objects in bucket 'xxxxxx-ibm3h-9pbgg-vsi-image':
      ```
   6. Set an environment variable to create a descriptive name for your boot image:

      ```
      $ export IMAGE_NAME="<descriptive_image_name>"
      ```

      Setting a descriptive name for your boot image, such as using the Red Hat Enterprise Linux CoreOS (RHCOS) version number in the image name, makes it easier to track which version is currently deployed if you update the cluster in the future.
   7. Create a custom image for your IBM Cloud Virtual Private Cloud (VPC) from the uploaded boot image by running one of the following commands, based on your cluster architecture:

      * Linux (x86\_64, amd64):

        ```
        $ ibmcloud is image-create "${RESOURCE_GROUP}-${IMAGE_NAME}" --file "cos://${REGION}/${RESOURCE_GROUP}-vsi-image/rhcos-new.qcow2" --os-name rhel-coreos-stable-amd64 --resource-group-name "${RESOURCE_GROUP}"
        ```

        You must set the `--os-name` argument to `rhel-coreos-stable-amd64` as shown. This parameter configures several Red Hat Enterprise Linux CoreOS (RHCOS) default values that are required.

        `RESOURCE_GROUP`, `IMAGE_NAME`, and `REGION` are environment variables you created in previous steps.
      * Linux on IBM Z® and IBM® LinuxONE (s390x):

        ```
        $ ibmcloud is image-create "${RESOURCE_GROUP}-${IMAGE_NAME}" --file "cos://${REGION}/${RESOURCE_GROUP}-vsi-image/rhcos-new.qcow2" --os-name red-8-s390x-byol --resource-group-name "${RESOURCE_GROUP}"
        ```

        You must set the `--os-name` argument to `red-8-s390x-byol` as shown. This parameter configures several Red Hat Enterprise Linux CoreOS (RHCOS) default values that are required.

        `RESOURCE_GROUP`, `IMAGE_NAME`, and `REGION` are environment variables you created in previous steps.
   8. Optional: Observe the new image being uploaded until its status changes from `pending` to `available`.

      ```
      $ watch ibmcloud is image "${RESOURCE_GROUP}-${IMAGE_NAME}"
      ```

      `RESOURCE_GROUP` and `IMAGE_NAME` are environment variables you created in previous steps.
6. Update each of your compute machine sets to include the new boot image:

   1. Obtain the name of your machine sets for use in the following step by running the following command:

      ```
      $ oc get machineset -n openshift-machine-api
      ```

      **Example output**

      ```
      NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
      rhhdrbk-b5564-4pcm9-worker-0         3         3         3       3           123m
      ci-ln-xj96skb-72292-48nm5-worker-d   1         1         1       1           27m
      ```
   2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:

      ```
      $ oc patch machineset <machineset-name> -n openshift-machine-api --type merge \
        -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":"'${RESOURCE_GROUP}'-'${IMAGE_NAME}'"}}}}}}'
      ```

      Replace `<machineset_name>` with the name of your machine set.

      `IMAGE_NAME` is the environment variable you created in a previous step.
7. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

**Verification**

1. Scale up a machine set to check that the new node is using the new boot image:

   1. Increase the machine set replicas by one to trigger a new machine by running the following command:

      ```
      $ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
      ```

      where:

      `<count>`
      :   Specifies the total number of replicas, including any existing replicas, that you want for this machine set.

      `<machineset_name>`
      :   Specifies the name of the machine set to scale.
   2. Optional: View the status of the machine set as it provisions by running the following command:

      ```
      $ oc get machines.machine.openshift.io -n openshift-machine-api -w
      ```

      It can take several minutes for the machine set to achieve the `Running` state.
   3. Verify that the new node has been created and is in the `Ready` state by running the following command.

      ```
      $ oc get nodes
      ```
   4. Verify that the new node is using the new boot image by running the following command:

      ```
      $ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
      ```

      Replace `<new_node>` with the name of your new node.

      **Example output**

      ```
      {
      # ...
          "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
          "version": "9.6.20251212-1"
      }
      ```

      where:

      `<version>`
      :   Specifies the boot image version.

   After you migrate all machine sets to the new boot image, the old boot image is no longer needed. You can remove the old boot image from your COS bucket.

### [8.6. Manually updating the boot image on a Nutanix cluster](#mco-update-boot-images-nutanix_mco-update-boot-images-manual) Copy linkLink copied to clipboard!

You can manually update the boot image for your Nutanix cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly.

Note

The standard boot image management feature is not supported for Nutanix clusters.

The following procedure, which includes steps to create environment variables that facilitate running the required commands, shows how to obtain Nutanix authentication credentials, download a boot image, upload that image to the Nutanix Prism Central, and modify your compute machine sets to use the new boot image.

This procedure requires Nutanix authentication credentials, which you need to access Prism Central. If you need to recover your credentials, you can get them from an OpenShift Container Platform secret, the name of which you can find in the default compute machine set. You can decrypt this secret and export the credentials to create the `clouds.yaml` file, as described in the following procedure.

**Prerequisites**

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2).
* You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program."
* You have installed the OpenShift CLI (`oc`).
* You have installed the [`jq`](https://stedolan.github.io/jq/) program.

**Procedure**

1. If you need to recover your Nutanix authentication credentials, perform the following steps:

   1. Obtain the name of the secret that contains your credentials by running the following command:

      ```
      $ oc get machineset -n openshift-machine-api -o yaml | grep credentialsSecret -A 1
      ```

      **Example output**

      ```
          credentialsSecret:
            name: nutanix-credentials
      ```
   2. Decrypt the secret by running the following command:

      ```
      $ oc get secret <secret_name> -n openshift-machine-api -o jsonpath='{.data.credentials}' | base64 -d
      ```

      Replace `<secret_name>` with the name of the secret, which you obtained in the previous step.

      **Example output**

      ```
      [{"type":"basic_auth","data":{"prismCentral":{"username":"","password":""},"prismElements":null}}]
      ```
2. Set an environment variable for the Nutanix username by running the following command:

   ```
   $ export USER="<username>"
   ```
3. Set an environment variable for the Nutanix password by running the following command:

   ```
   $ export PASS="<password>"
   ```
4. If you need to recover your IP address for Prism Central, run the following command:

   ```
   $ oc get configmap cloud-provider-config -n openshift-config -o jsonpath='{.data.config}' | grep prismCentral -A 8
   ```

   **Example output**

   ```
       "prismCentral": {
           "address": "",
           "port": 9440,
           "credentialRef": {
               "kind": "Secret",
               "name": "nutanix-credentials",
               "namespace": "openshift-cloud-controller-manager"
           }
       },
   ```

   where:

   `prismCentral.address`
   :   Specifies the Prism Central IP address.
5. Set an environment variables for the Prism Central IP address by running the following command:

   ```
   $ export PC_IP="<prism_central_ip_address>"
   ```
6. Obtain the boot image and upload the image to Prism Central:

   1. Obtain the URL of the RHCOS image you want to use as the boot image and set the location in an environment variable by running the following command:

      ```
      $ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.artifacts.nutanix.formats.qcow2.disk.location')
      ```
   2. Set an environment variable to create a descriptive name for your boot image in Prism Central by running the following command:

      ```
      $ export IMAGE_NAME="<descriptive_image_name>"
      ```

      Setting a descriptive name for your boot image in Prism Central, such as using the Red Hat Enterprise Linux CoreOS (RHCOS) version number in the image name, makes it easier to track which version is currently deployed if you update the cluster in the future.

      **Example command**

      ```
      $ export IMAGE_NAME="rhcos-9.6-boot-image"
      ```
   3. Upload the image to Prism Central by running the following command:

      ```
      $ curl -k -u "$USER:$PASS" \
        -X POST "https://$PC_IP:9440/api/nutanix/v3/images" \
        -H "Content-Type: application/json" \
        -d '{
          "spec": {
            "name": "'"$IMAGE_NAME"'",
            "resources": {
              "image_type": "DISK_IMAGE",
              "source_uri": "'"$RHCOS_URL"'"
            }
          },
          "metadata": {
            "kind": "image"
          }
        }'
      ```

      `USER`,`PASS`, `IMAGE_NAME`, and `RHCOS_URL` are environment variables you created in previous steps.
   4. Optional: Verify that the image is uploaded by running the following command:

      ```
      $ curl -k -u "$USER:$PASS" \
        -X POST "https://$PC_IP:9440/api/nutanix/v3/images/list" \
        -H "Content-Type: application/json" \
        -d '{
          "kind": "image",
          "filter": "name=='"$IMAGE_NAME"'"
        }'
      ```

      **Example output**

      ```
      {
        "name": "<image-name>",
        "state": "COMPLETE"
      }
      ```
7. Update each of your compute machine sets to include the new boot image:

   1. Obtain the name of your machine sets for use in the following step by running the following command:

      ```
      $ oc get machineset -n openshift-machine-api
      ```

      **Example output**

      ```
      NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
      rhhdrbk-b5564-4pcm9-worker-0         3         3         3       3           123m
      ci-ln-xj96skb-72292-48nm5-worker-d   1         1         1       1           27m
      ```
   2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:

      ```
      $ oc patch machineset <machineset_name> -n openshift-machine-api --type merge -p '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":{"type":"name","name":"'${IMAGE_NAME}'"}}}}}}}'
      ```

      Replace `<machineset_name>` with the name of your machine set.
8. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

**Verification**

1. Scale up a machine set to check that the new node is using the new boot image:

   1. Increase the machine set replicas by one to trigger a new machine by running the following command:

      ```
      $ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
      ```

      where:

      `<count>`
      :   Specifies the total number of replicas, including any existing replicas, that you want for this machine set.

      `<machineset_name>`
      :   Specifies the name of the machine set to scale.
   2. Optional: View the status of the machine set as it provisions by running the following command:

      ```
      $ oc get machines.machine.openshift.io -n openshift-machine-api -w
      ```

      It can take several minutes for the machine set to achieve the `Running` state.
   3. Verify that the new node has been created and is in the `Ready` state by running the following command:

      ```
      $ oc get nodes
      ```
2. Verify that the new node is using the new boot image by running the following command:

   ```
   $ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
   ```

   Replace `<new_node>` with the name of your new node.

   **Example output**

   ```
   {
   # ...
       "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
       "version": "9.6.20251212-1"
   }
   ```

   where:

   `version`
   :   Specifies the boot image version.
3. Verify that the boot image is the same version as the image you uploaded in a previous step by running the following command:

   ```
   $ echo ${RHCOS_URL}
   ```

   **Example output**

   ```
   https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-9.6/builds/9.6.20251212-1/x86_64/rhcos-9.6.20251212-1-nutanix.x86_64.qcow2
   ```

   After you migrate all machine sets to the new boot image, you can remove the old boot image from Prism Central.

### [8.7. Manually updating the boot image on an RHOSP cluster](#mco-update-boot-images-openstack_mco-update-boot-images-manual) Copy linkLink copied to clipboard!

For a Red Hat OpenStack Platform (RHOSP) cluster, you can manually update the boot image for your cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to help ensure any new nodes can scale up properly.

Note

The standard boot image management feature is not supported for RHOSP clusters.

The following procedure, which includes steps to create environment variables that facilitate running the required commands, shows how to obtain RHOSP authentication credentials, download a boot image, upload that image to the RHOSP image service (Glance), and modify your worker machine sets to use the new boot image.

This procedure requires the `clouds.yaml` file, which is needed by the OpenStackClient CLI to connect to your RHOSP cloud. If you need to re-create this file, you can get the RHOSP credentials from an OpenShift Container Platform secret, the name of which you can find in the default compute machine set. You can decrypt this secret and export the credentials to create the `clouds.yaml` file, as described in the following procedure.

Note

Updating control plane machine sets is not supported in RHOSP.

**Prerequisites**

* You have completed the general boot image prerequisites as described in the Prerequisites section of [OpenShift Container Platform Boot Image Updates](https://access.redhat.com/articles/7053165#prerequisites-2).
* You have downloaded the latest version of the OpenShift Container Platform installation program, openshift-install, from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program."
* You have installed the OpenShift CLI (`oc`) installed.
* You have installed the [OpenStackClient (RHCOS documentation)](https://docs.openstack.org/python-openstackclient/latest/).
* You have installed the [`jq`](https://stedolan.github.io/jq/) program.

**Procedure**

1. If you need to re-create the `clouds.yaml` file, perform the following steps:

   1. Obtain the name of the secret that contains your credentials by running the following command:

      ```
      $ oc get machineset -n openshift-machine-api -o yaml | grep cloudsSecret -A 1
      ```

      **Example output**

      ```
      cloudsSecret:
        name: openstack-cloud-credentials
      ```
   2. Decrypt the secret and add the contents to the `clouds.yaml` file by running the following command:

      ```
      $ oc get secret <secret_name> -n openshift-machine-api -o jsonpath='{.data.clouds\.yaml}' | base64 -d > <file_path>/clouds.yaml
      ```

      Replace `<secret_name>` with the name of the secret, which you obtained in the previous step, and `<file_path>` with the path to the `clouds.yaml` file.
   3. Optional: Verify the contents of the `clouds.yaml` file by running the following command:

      ```
      $ cat <file_path>/clouds.yaml
      ```

      Replace `<file_path>` with the path to the `clouds.yaml` file.

      **Example output**

      ```
      clouds:
        openstack:
          auth:
            auth_url: https://your-openstack-url:13000
            username: "your-username"
            password: "your-password"
            project_name: "your-project"
            user_domain_name: "Default"
            project_domain_name: "Default"
      ```
2. Set an environment variable for the location of the `clouds.yaml` file by running the following command:

   ```
   $ export OS_CLIENT_CONFIG_FILE=<file_path>/clouds.yaml
   ```

   Replace `<file_path>` with the path to the `clouds.yaml` file.

   The OpenStackClient CLI uses this environment variable to locate the `clouds.yaml` file.
3. Obtain the name of your RHOSP cloud from the default compute machine set and set the name in an environment variable by running the following command:

   ```
   $ export CLOUD_NAME=$(oc get machineset -n openshift-machine-api -o jsonpath='{.items[0].spec.template.spec.providerSpec.value.cloudName}')
   ```
4. Obtain the URL of the RHCOS image you want to use as the boot image and set the location in an environment variable by running one of the following commands, based on cluster architecture:

   * Linux (x86\_64, amd64):

     ```
     $ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r \
       '.architectures.x86_64.artifacts.openstack.formats."qcow2.gz".disk.location')
     ```
   * Linux on IBM Z® and IBM® LinuxONE (s390x):

     ```
     $ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r \
       '.architectures.s390x.artifacts.openstack.formats."qcow2.gz".disk.location')
     ```
   * Linux on ARM (aarch64, arm64)

     ```
     $ export RHCOS_URL=$(openshift-install coreos print-stream-json | jq -r \
       '.architectures.aarch64.artifacts.openstack.formats."qcow2.gz".disk.location')
     ```
5. Obtain the boot image and upload the image to the RHOSP image service (Glance):

   1. Download the image by using the following command:

      ```
      $ curl -L -o /tmp/rhcos-new.qcow2.gz "${RHCOS_URL}"
      ```

      `RHCOS_URL` is the URL environment variables you created in a previous step.
   2. Decompress the downloaded image by using the following command:

      ```
      $ gunzip <file_path>/rhcos-new.qcow2.gz
      ```

      Replace `<file_path>` with the path to the location for the image.
   3. Set an environment variable to create a descriptive name for your boot image in Glance by running the following command:

      ```
      $ export IMAGE_NAME="<descriptive_image_name>"
      ```

      Setting a descriptive name for your boot image, such as using the Red Hat Enterprise Linux CoreOS (RHCOS) version number in the image name, makes it easier to track which version is currently deployed if you update the cluster in the future.

      **Example command**

      ```
      $ export IMAGE_NAME="rhcos 9.6 boot image"
      ```
   4. Upload the image to Glance by using the following command:

      ```
      $ openstack --os-cloud "${CLOUD_NAME}" image create "${IMAGE_NAME}" \
        --disk-format qcow2 \
        --container-format bare \
        --file <file_path>/rhcos-new.qcow2 \
        --property os_type=linux \
        --property os_distro=rhcos
      ```

      Replace `<file_path>` with the path to the location for the image.

      `CLOUD_NAME` and `IMAGE_NAME` are environment variables you created in previous steps.

      It might take several minutes for the image to upload. When the upload is complete, details on the image displays, similar to the following example:

      **Example output**

      ```
      +------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Field            | Value                                                                                                                                                                               |
      +------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | checksum         | 469fa549f706617ff15b41bd2a919679                                                                                                                                                    |
      # ...                                                                                                                                                         |
      | disk_format      | qcow2                                                                                                                                                                               |
      # ...
      | name             | rhcos 9.6 boot image
      ```
   5. Optional: Verify that the image has uploaded and is in active state by running the following command:

      ```
      $ openstack --os-cloud "${CLOUD_NAME}" image show "${IMAGE_NAME}" -f json | jq '{name: .name, status: .status}'
      ```

      **Example output**

      ```
      {
        "name": "rhcos 9.6 boot image",
        "status": "active"
      }
      ```
6. Update each of your compute machine sets to include the new boot image:

   1. Obtain the name of your machine sets for use in the following step by running the following command:

      ```
      $ oc get machineset -n openshift-machine-api
      ```

      **Example output**

      ```
      NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
      rhhdrbk-b5564-4pcm9-worker-0         3         3         3       3           123m
      ci-ln-xj96skb-72292-48nm5-worker-d   1         1         1       1           27m
      ```
   2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:

      ```
      $ oc patch machineset <machineset_name> -n openshift-machine-api --type merge -p \
        '{"spec":{"template":{"spec":{"providerSpec":{"value":{"image":"'${IMAGE_NAME}'"}}}}}}'
      ```

      Replace `<machineset_name>` with the name of your machine set.

      `IMAGE_NAME` is the environment variable you created in a previous step.
7. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

**Verification**

1. Scale up a machine set to check that the new node is using the new boot image:

   1. Increase the machine set replicas by one to trigger a new machine by running the following command:

      ```
      $ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
      ```

      where:

      `<count>`
      :   Specifies the total number of replicas, including any existing replicas, that you want for this machine set.

      `<machineset_name>`
      :   Specifies the name of the machine set to scale.
   2. Optional: View the status of the machine set as it provisions by running the following command:

      ```
      $ oc get machines.machine.openshift.io -n openshift-machine-api -w
      ```

      It can take several minutes for the machine set to achieve the `Running` state.
   3. Verify that the new node has been created and is in the `Ready` state by running the following command:

      ```
      $ oc get nodes
      ```
2. Verify that the new node is using the new boot image by running the following command:

   ```
   $ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
   ```

   Replace `<new_node>` with the name of your new node.

   **Example output**

   ```
   {
   # ...
       "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
       "version": "9.6.20251212-1"
   }
   ```

   where:

   `version`
   :   Specifies the boot image version.

   After you migrate all machine sets to the new boot image, you can remove the old boot image from Glance.

### [8.8. Manually updating the boot image on a vSphere cluster](#mco-update-boot-images-vsphere_mco-update-boot-images-manual) Copy linkLink copied to clipboard!

You can manually update the boot image for your VMware vSphere cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to ensure that new nodes can scale up properly.

vSphere boot images use a template that you create by uploading a Red Hat Enterprise Linux CoreOS (RHCOS) OVA image to the vSphere vCenter. The template image is used by all machine sets as the boot image. Use the following procedure to identify the correct boot image to use as the new boot image, create the template from the image in vCenter, and modify your compute machine sets to use that template image.

Note

For clusters that use a default RHCOS image, you can configure the cluster to automatically update the boot image each time the cluster is updated. If you are using the following procedure, ensure that automatic boot image updates are disabled and skew enforcement is in manual mode. For more information, see "Boot image management" and "Boot image skew enforcement".

**Prerequisites**

* You have completed the general boot image prerequisites as described in the "Prerequisites" section of the [OpenShift Container Platform Boot Image Updates knowledgebase article](https://access.redhat.com/articles/7053165#prerequisites-2).
* You have installed the OpenShift CLI (`oc`).
* You have set boot image skew enforcement to the manual or none mode. For more information, see "Configuring boot image skew enforcement".
* You have disabled boot image management for the cluster. For more information, see "Disabling boot image management".
* You have downloaded the latest version of the OpenShift Container Platform installation program from the [OpenShift Cluster Manager](https://console.redhat.com/openshift). For more information, see "Obtaining the installation program."

**Procedure**

1. Obtain the latest boot image to use as the new boot image:

   1. Obtain the name of the new boot image by running the following command:

      ```
      $ openshift-install coreos print-stream-json | jq '.architectures.x86_64.artifacts.vmware'
      ```

      **Example output**

      ```
      {
        "release": "9.6.20251023-0",
        "formats": {
          "ova": {
            "disk": {
              "location": "https://rhcos.mirror.openshift.com/art/storage/prod/streams/rhel-9.6/builds/9.6.20251023-0/x86_64/rhcos-9.6.20251023-0-vmware.x86_64.ova",
              "sha256": "14fa549bb83b2e730de22312419b503bc1ce85adf72269582f0af60e366d87ff"
            }
          }
        }
      }
      ```
   2. Use the URL in the `location` field to download the image.
2. In the vSphere Client, create a template for the OVA image:

   1. From the **Hosts and Clusters** tab, right-click your cluster name and select **Deploy OVF Template**.
   2. On the **Select an OVF** tab, specify the name of the RHCOS OVA file that you downloaded.
   3. On the **Select a name and folder** tab, set a **Virtual machine name** for your template, such as using the RHCOS version number in the image name. Click the name of your vSphere cluster and select the folder.
   4. On the **Select a compute resource** tab, click the name of your vSphere cluster.
   5. On the **Select storage** tab, configure the storage options for your VM.

      * Select **Thin Provision** or **Thick Provision**, based on your storage preferences.
      * Select the data store that you specified in your `install-config.yaml` file.
      * If you want to encrypt your virtual machines, select **Encrypt this virtual machine**. See "Requirements for encrypting virtual machines" for more information.
   6. On the **Select network** tab, specify the network that you configured for the cluster, if available.
   7. When creating the OVF template, do not specify values on the **Customize template** tab or configure the template any further.
   8. On the **Ready to complete** tab, verify your settings and click **Finish**.

      The vSphere Client uploads the boot image to create the OVF template. This can take a few minutes depending on network speeds. You can keep track of this process in the task tab under *Deploy OVF template*.
   9. After the upload is complete, click the new virtual machine and click **Template** → **Convert to template** → **Yes**.

      You now have a VM template based on the new boot image, which you can use to update the machine set objects.
3. Update each of your compute machine sets to include the new boot image:

   1. Obtain the name of your machine sets for use in the following step by running the following command:

      ```
      $ oc get machineset -n openshift-machine-api
      ```

      **Example output**

      ```
      NAME                                 DESIRED   CURRENT   READY   AVAILABLE   AGE
      ci-ln-xw7zmyt-72292-x7nqv-worker-a   1         1         1       1           53m
      ```
   2. Edit a machine set to update the `image` field in the `providerSpec` stanza to add your boot image by running the following command:

      ```
      $ oc patch machineset <machineset-name> -n openshift-machine-api --type json \
        -p '[{"op": "replace", "path": "/spec/template/spec/providerSpec/value/template", "value": "ci-ln-6vjqx8t-c1627-bwxkr-rhcos-generated-region-generated-zone"}]'
      ```

      Replace `<machineset_name>` with the name of your machine set.
4. If boot image skew enforcement in your cluster is set to the manual mode, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

**Verification**

1. Scale up a machine set to check that the new node is using the new boot image:

   1. Increase the machine set replicas by one to trigger a new machine by running the following command:

      ```
      $ oc scale --replicas=<count> machineset <machineset_name> -n openshift-machine-api
      ```

      where:

      `<count>`
      :   Specifies the total number of replicas, including any existing replicas, that you want for this machine set.

      `<machineset_name>`
      :   Specifies the name of the machine set to scale.
   2. Optional: View the status of the machine set as it provisions by running the following command:

      ```
      $ oc get machines.machine.openshift.io -n openshift-machine-api -w
      ```

      It can take several minutes for the machine set to achieve the `Running` state.
   3. Verify that the new node has been created and is in the `Ready` state by running the following command:

      ```
      $ oc get nodes
      ```
2. Verify that the new node is using the new boot image by running the following command:

   ```
   $ oc debug node/<new_node> -- chroot /host cat /sysroot/.coreos-aleph-version.json
   ```

   Replace `<new_node>` with the name of your new node.

   **Example output**

   ```
   {
   # ...
       "ref": "docker://ostree-image-signed:oci-archive:/rhcos-9.6.20251212-1-ostree.x86_64.ociarchive",
       "version": "9.6.20251212-1"
   }
   ```

   where:

   `version`
   :   Specifies the boot image version.

### [8.9. Manually updating the boot image on a platform none or external cluster](#mco-update-boot-images-plat-none_mco-update-boot-images-manual) Copy linkLink copied to clipboard!

For `platform: None` and `platform: External` clusters, you can manually update the boot image for your cluster by configuring your machine sets to use the latest OpenShift Container Platform image as the boot image to help ensure any new nodes can scale up properly.

For these clusters, OpenShift Container Platform does not manage node provisioning or Red Hat Enterprise Linux CoreOS (RHCOS) boot images. These clusters do not use Machine API machine sets.

Note

The standard boot image management feature is not supported for `platform: None` or `platform: External` clusters.

The method for updating boot images depends on how nodes are added to your cluster as a day-2 operation.

Expand

| Method | Description |
| --- | --- |
| User-provisioned infrastructure clusters | Nodes are provisioned manually by a user-managed infrastructure. |
| Red Hat Advanced Cluster Management (RHACM)-managed clusters | Nodes are added by using a discovery ISO managed by an `InfraEnv` object on the hub cluster. |
| External provider clusters | Nodes are provisioned by using provider-specific tooling with a user-uploaded RHCOS image. |

Show more

User-provisioned infrastructure
:   For user-provisioned infrastructure clusters, you manage boot images as part of your infrastructure. To update the boot image, download the latest RHCOS image for your architecture from [mirror.openshift.com](https://mirror.openshift.com/pub/openshift-v4/dependencies/rhcos/) and update your infrastructure to serve the new image.

    For the full procedure, see the section for your platform in "Adding compute machines to clusters with user-provisioned infrastructure manually".

RHACM-managed clusters
:   For clusters managed by RHACM, the boot image used to generate the discovery ISO image is controlled by the `spec.osImageVersion` parameter in the `InfraEnv` object on the hub cluster. After an OpenShift Container Platform upgrade, you need to update the existing `InfraEnv` object to add or update `spec.osImageVersion` field, specifying the OpenShift Container Platform version of the new boot image.

External provider clusters
:   For clusters managed by an external infrastructure provider, such as Oracle Cloud Infrastructure (OCI), you must upload the new boot image to the provider’s image store and update your node provisioning configuration to reference the new image when creating new nodes. The exact steps are provider-specific.

If boot image skew enforcement in your cluster is set to the manual mode, after updating the boot image, update the version of the new boot image in the `MachineConfiguration` object as described in "Updating the boot image skew enforcement version".

## [Chapter 9. Creating custom machine config pools](#machine-config-creating-custom-mcp) Copy linkLink copied to clipboard!

You can create custom machine config pools (MCP) to manage compute nodes for custom use cases that extend outside of the default node types. By using a custom machine config pool, you can deploy changes targeted only at nodes in the custom pool.

Custom machine config pools inherit their configurations from the `worker` machine config pool. Changes made to the `worker` machine config pool apply to nodes in the custom pool. However, changes made to the custom machine config pool apply only to the nodes in the custom pool. For more information on custom machine config pools, see "Node configuration management with machine config pools".

Note

Custom machine config pools for the control plane nodes are not supported.

For example, you could use a custom machine config pool to create an *infrastructure* node. Components that you move to an infrastructure node do not need to be accounted for during sizing. For more information on infrastructure nodes, see "Creating infrastructure machine sets".

After you create the custom machine config pool, you can boot new nodes directly to the pool by creating a new machine set. Or, you can add existing nodes to the custom pool by using labels.

### [9.1. Creating a custom machine config pool with a new node](#machine-config-custom-mcp-automatic_machine-config-creating-custom-mcp) Copy linkLink copied to clipboard!

You can create a custom machine config pool (MCP) and launch a new node directly into that pool. By launching the node directly into the new pool, you save a node reboot cycle that would be required when moving the nodes from the worker machine config pool to the custom pool.

Use the `userDataSecret` parameter in the machine set to instruct the Machine Config Operator (MCO) to add the node to a specific machine config pool. The secret contains the endpoint of the custom machine config pool. You must prefix the name of this new secret with the name of the custom machine config pool.

The following procedure shows you how to create a new custom machine config pool and launch a new node into that pool.

**Procedure**

1. Create a custom machine config pool:

   1. Create a YAML file similar to the following:

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfigPool
      metadata:
        name: custom
      spec:
        machineConfigSelector:
          matchExpressions:
            - {key: machineconfiguration.openshift.io/role, operator: In, values: [custom,worker]}
        nodeSelector:
          matchLabels:
            node-role.kubernetes.io/custom: ""
      ```

      where:

      `metadata.name`
      :   Specifies a name for the custom machine config pool.

      `spec.machineConfigSelector.matchExpressions`
      :   Specifies the node roles for the new node. This must include the `worker` role and the custom role.

      `spec.nodeSelector.matchLabels`
      :   Specifies a node selector to use when adding nodes to this pool.
   2. Create the machine config pool by running the following command:

      ```
      $ oc create -f <file_name>.yaml
      ```
2. Create a new machine set that creates a new node in the new custom machine config pool:

   1. Create a YAML file, for example by making a copy of an existing compute machine set YAML and making the following changes:

      ```
      apiVersion: machine.openshift.io/v1beta1
      kind: MachineSet
      metadata:
      # ...
        name: <machineset_name>
        namespace: openshift-machine-api
      # ...
      spec:
      # ...
        template:
      # ...
          spec:
      # ...
            providerSpec:
      # ...
              value:
      # ...
                userDataSecret:
                  name: <mcp_name>-user-data-managed
      # ...
      ```

      where:

      `metadata.name`
      :   Specifies a name for the machine set.

      `metadata.namespace`
      :   Specifies a namespace for the machine set. This must be `openshift-machine-api`.

      `spec.template.spec.providerSpec.value.userDataSecret`
      :   Specifies a name for the user data secret that is created. The name of the secret must start with the name of the custom machine config pool and end with `-user-data-managed`. For example `custom-user-data-managed`.

      These are the minimum changes required to create the new machine set. For more configuration options or to configure an all-new machine set, see "Creating infrastructure machine sets" for your platform.

      Note

      When creating a new machine set, you should specify the latest image to use for the boot image. For more information about configuring the boot image on your cluster, see "Manually updating the boot image" for your platform. The method to specify the image varies by provider.
   2. Create the machine set by running the following command:

      ```
      $ oc create -f <file_name>.yaml
      ```

      The MCO creates a new node in the new custom machine config pool.

**Verification**

1. Check to see that the MCO created the new machine config pool by running the following command:

   ```
   $ oc get mcp
   ```

   **Example output**

   ```
   NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   custom    rendered-custom-72be15c95699b6d39f70fce525f51bb2    True      False      False      1              1                   1                     0                      12s
   master    rendered-master-9e25b616b551d6c77f490191f45161d7    True      False      False      3              3                   3                     0                      32m
   worker    rendered-worker-72be15c95699b6d39f70fce525f51bb2    True      False      False      2              2                   2                     0                      32m
   ```

   In this example, `custom` is the new machine config pool.
2. Check to see that the MCO created the new machine set by running the following command:

   ```
   $ oc get machineset -n openshift-machine-api
   ```

   **Example output**

   ```
   NAME                                  DESIRED   CURRENT   READY   AVAILABLE   AGE
   ci-ln-7x179fk-72292-tc5qz-custom-a    1         1         1       1           62s
   ci-ln-7x179fk-72292-tc5qz-worker-a    1         1         1       1           91m
   ci-ln-7x179fk-72292-tc5qz-worker-b    1         1         1       1           91m
   ci-ln-7x179fk-72292-tc5qz-worker-f    1         1         1       1           91m
   ```

   In this example, `ci-ln-7x179fk-72292-tc5qz-custom-a` is the new machine set.
3. Check that the MCO created the required secret by running the following command:

   ```
   $ oc get secrets -n openshift-machine-api
   ```

   **Example output**

   ```
   NAME                                                  TYPE                      DATA   AGE
   # ...
   custom-user-data-managed                              Opaque                    2      9m
   # ...
   ```
4. Check to see that the node is in the new custom machine config pool by running the following command:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                                        STATUS   ROLES                    AGE   VERSION
   ci-ln-i61xqwb-72292-hz2mw-custom-9r496      Ready    custom,worker             9m   v1.35.3
   ci-ln-i61xqwb-72292-ftjn8-master-0          Ready    control-plane,master     42m   v1.35.3
   ci-ln-i61xqwb-72292-ftjn8-master-1          Ready    control-plane,master     44m   v1.35.3
   ci-ln-i61xqwb-72292-ftjn8-master-2          Ready    control-plane,master     43m   v1.35.3
   ci-ln-i61xqwb-72292-ftjn8-worker-c-2lhcl    Ready    worker                   36m   v1.35.3
   ci-ln-i61xqwb-72292-ftjn8-worker-f-qgdb7    Ready    worker                   36m   v1.35.3
   ```

   In this example, the `ci-ln-i61xqwb-72292—​hz2mw-custom-9r496` is a new node that was added to the `custom` machine config pool.

### [9.2. Creating a custom machine config pool for an existing node](#machine-config-custom-mcp-existing_machine-config-creating-custom-mcp) Copy linkLink copied to clipboard!

You can create custom machine config pools (MCP) and manually add an existing node into that pool. With custom machine config pools, you can deploy changes targeted at the nodes in the custom pool.

The following procedure shows you how to create a new custom machine config pool and add an existing node into that pool.

**Procedure**

1. Create a custom machine config pool:

   1. Create a YAML file similar to the following:

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfigPool
      metadata:
        name: custom
      spec:
        machineConfigSelector:
          matchExpressions:
            - {key: machineconfiguration.openshift.io/role, operator: In, values: [custom,worker]}
        nodeSelector:
          matchLabels:
            node-role.kubernetes.io/custom: ""
      ```

      where:

      `metadata.name`
      :   Specifies a name for the machine config pool.

      `spec.machineConfigSelector.matchExpressions`
      :   Specifies the node roles for the new node. This must include the `worker` role and the custom role.

      `spec.nodeSelector.matchLabels`
      :   Specifies a node selector to use when adding nodes to this pool.
   2. Create the machine config pool by running the following command:

      ```
      $ oc create -f <file_name>.yaml
      ```
2. Add a label to the worker nodes that you want to move to the new custom pool by running the following command:

   ```
   $ oc label node <node_name> <node_selector>
   ```

   Replace `<node_name>` with the name of the node that you want to move and replace `<node-selector>` with the node selector you added to the machine config pool.

   **Example command**

   ```
   $ oc label node ci-ln-g5tpp5k-72292-hz2mw-worker-b-ps8xh node-role.kubernetes.io/custom=""
   ```

**Verification**

1. Check to see that the MCO created the new machine config pool by running the following command:

   ```
   $ oc get mcp
   ```

   **Example output**

   ```
   NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   custom    rendered-custom-72be15c95699b6d39f70fce525f51bb2    True      False      False      1              1                   1                     0                      12s
   master    rendered-master-9e25b616b551d6c77f490191f45161d7    True      False      False      3              3                   3                     0                      32m
   worker    rendered-worker-72be15c95699b6d39f70fce525f51bb2    True      False      False      2              2                   2                     0                      32m
   ```

   In this example, `custom` is the new machine config pool.
2. Check to see if the node is in that pool by running the following command:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                                       STATUS   ROLES                  AGE   VERSION
   ci-ln-i61xqwb-72292-ftjn8-master-0         Ready    control-plane,master   42m   v1.35.3
   ci-ln-i61xqwb-72292-ftjn8-master-1         Ready    control-plane,master   44m   v1.35.3
   ci-ln-i61xqwb-72292-ftjn8-master-2         Ready    control-plane,master   43m   v1.35.3
   ci-ln-g5tpp5k-72292-hz2mw-worker-b-ps8xh   Ready    custom,worker          36m   v1.35.3
   ci-ln-i61xqwb-72292-ftjn8-worker-c-2lhcl   Ready    worker                 36m   v1.35.3
   ci-ln-i61xqwb-72292-ftjn8-worker-f-qgdb7   Ready    worker                 36m   v1.35.3
   ```

   In this example, the `ci-ln-g5tpp5k-72292-hz2mw-worker-b-ps8xh` node is an existing node that was moved to the `custom` machine config pool.

## [Chapter 10. Managing unused rendered machine configs](#machine-configs-garbage-collection) Copy linkLink copied to clipboard!

You can remove old, unused rendered machine configs by using the `oc adm prune renderedmachineconfigs` command. By removing these objects, you can free up disk space and reduce performance issues.

The Machine Config Operator (MCO) does not perform any garbage collection activities. This means that all rendered machine configs remain in the cluster. Each time a user or controller applies a new machine config, the MCO creates new rendered configs for each affected machine config pool. Over time, this can lead to a large number of rendered machine configs, which can make working with machine configs confusing. Having too many rendered machine configs can also contribute to disk space issues and performance issues with etcd.

By using the `oc adm prune renderedmachineconfigs` command with the `--confirm` flag, you can remove all unused rendered machine configs or only those in a specific machine config pool. You can also remove a specific number of unused rendered machine configs, keeping some older machine configs in case you want to check older configurations.

You can use the `oc adm prune renderedmachineconfigs` command without the `--confirm` flag to see which rendered machine configs would be removed.

Use the `list` subcommand to display all the rendered machine configs in the cluster or a specific machine config pool.

Note

The `oc adm prune renderedmachineconfigs` command deletes only rendered machine configs that are not in use. If a rendered machine configs are in use by a machine config pool, the rendered machine config is not deleted. In this case, the command output specifies the reason that the rendered machine config was not deleted.

### [10.1. Viewing rendered machine configs](#machineconfig-garbage-collect-viewing_machine-configs-garbage-collection) Copy linkLink copied to clipboard!

You can view a list of rendered machine configs by using the `oc adm prune renderedmachineconfigs` command with the `list` subcommand to determine which objects you can remove.

For example, the command in the following procedure would list all rendered machine configs for the `worker` machine config pool.

**Procedure**

* Optional: List the rendered machine configs by using the following command:

  ```
  $ oc adm prune renderedmachineconfigs list --in-use=false --pool-name=worker
  ```

  where:

  list
  :   Displays a list of rendered machine configs in your cluster.

  `--in-use`
  :   Optional: Specifies whether to display only the used machine configs or all machine configs from the specified pool. If `true`, the output lists the rendered machine configs that are being used by a machine config pool. If `false`, the output lists all rendered machine configs in the cluster. The default value is `false`.

  `--pool-name`
  :   Optional: Specifies the machine config pool from which to display the machine configs.

  **Example output**

  ```
  worker

  rendered-worker-f38bf61ced3c920cf5a29a200ed43243 -- 2025-01-21 13:45:01 +0000 UTC (Currently in use: false)
  rendered-worker-fc94397dc7c43808c7014683c208956e-- 2025-01-30 17:20:53 +0000 UTC (Currently in use: false)
  rendered-worker-708c652868f7597eaa1e2622edc366ef -- 2025-01-31 18:01:16 +0000 UTC (Currently in use: true)
  ```
* List the rendered machine configs that you can remove automatically by running the following command. Any rendered machine config marked with the `as it’s currently in use` message in the command output cannot be removed.

  ```
  $ oc adm prune renderedmachineconfigs --pool-name=worker
  ```

  The command runs in dry-run mode, and no machine configs are removed.

  where:

  `--pool-name`
  :   Optional: Displays the machine configs in the specified machine config pool.

  **Example output**

  ```
  Dry run enabled - no modifications will be made. Add --confirm to remove rendered machine configs.
  dry-run deleting rendered MachineConfig rendered-worker-f38bf61ced3c920cf5a29a200ed43243
  dry-run deleting MachineConfig rendered-worker-fc94397dc7c43808c7014683c208956e
  Skip dry-run deleting rendered MachineConfig rendered-worker-708c652868f7597eaa1e2622edc366ef as it's currently in use
  ```

### [10.2. Removing unused rendered machine configs](#machineconfig-garbage-collect-removing_machine-configs-garbage-collection) Copy linkLink copied to clipboard!

You can remove unused rendered machine configs by using the `oc adm prune renderedmachineconfigs` command with the `--confirm` command, reducing disk space and performance issues.

If any rendered machine config is not deleted, the command output indicates which was not deleted and lists the reason for skipping the deletion.

**Procedure**

1. Optional: List the rendered machine configs that you can remove automatically by running the following command. Any rendered machine config marked with the `as it’s currently in use` message in the command output cannot be removed.

   ```
   $ oc adm prune renderedmachineconfigs --pool-name=worker
   ```

   **Example output**

   ```
   Dry run enabled - no modifications will be made. Add --confirm to remove rendered machine configs.
   dry-run deleting rendered MachineConfig rendered-worker-f38bf61ced3c920cf5a29a200ed43243
   dry-run deleting MachineConfig rendered-worker-fc94397dc7c43808c7014683c208956e
   Skip dry-run deleting rendered MachineConfig rendered-worker-708c652868f7597eaa1e2622edc366ef as it's currently in use
   ```

   where:

   pool-name
   :   Optional: Specifies the machine config pool where you want to delete the machine configs from.
2. Remove the unused rendered machine configs by running the following command. The command in the following procedure would delete the two oldest unused rendered machine configs in the `worker` machine config pool.

   ```
   $ oc adm prune renderedmachineconfigs --pool-name=worker --count=2 --confirm
   ```

   where:

   `--count`
   :   Optional: Specifies the maximum number of unused rendered machine configs you want to delete, starting with the oldest.

   `--confirm`
   :   Indicates that pruning should occur, instead of performing a dry-run.

   `--pool-name`
   :   Optional: Specifies the machine config pool from which you want to delete the machine. If not specified, all the pools are evaluated.

   **Example output**

   ```
   deleting rendered MachineConfig rendered-worker-f38bf61ced3c920cf5a29a200ed43243
   deleting rendered MachineConfig rendered-worker-fc94397dc7c43808c7014683c208956e
   Skip deleting rendered MachineConfig rendered-worker-708c652868f7597eaa1e2622edc366ef as it's currently in use
   ```

## [Chapter 11. Image mode for OpenShift](#mco-coreos-layering) Copy linkLink copied to clipboard!

You can extend the functionality of your base RHCOS image by layering additional images onto the base image without modifying the base RHCOS image.

This layering creates a *custom layered image* that includes all RHCOS functionality and adds additional functionality to specific nodes in the cluster.

Image mode is a cloud-native approach to operating system management that treats your OS like a container image. You define your operating system configuration as code, build it as a unified image, and deploy it consistently across your entire fleet.

### [11.1. About image mode for OpenShift](#coreos-layering-about_mco-coreos-layering) Copy linkLink copied to clipboard!

Image mode for OpenShift allows you to customize the underlying node operating system on any of your cluster nodes. This helps keep everything up-to-date, including the node operating system and any added customizations such as specialized software.

You create a custom layered image by using a Containerfile and applying it to nodes by using a custom object. At any time, you can remove the custom layered image by deleting that custom object.

With image mode for OpenShift, you can install RPMs into your base image, and your custom content will be booted alongside RHCOS. The Machine Config Operator (MCO) can roll out these custom layered images and monitor these custom containers in the same way it does for the default RHCOS image. Image mode for OpenShift gives you greater flexibility in how you manage your RHCOS nodes.

Important

Installing realtime kernel and extensions RPMs as custom layered content is not recommended. This is because these RPMs can conflict with RPMs installed by using a machine config. If there is a conflict, the MCO enters a `degraded` state when it tries to install the machine config RPM. You need to remove the conflicting extension from your machine config before proceeding.

When you apply the custom layered image to your cluster, you assume the responsibility for the package you applied with the custom layered image and any issues that might arise with the package.

There are three methods for deploying a custom layered image onto your nodes:

On-cluster image mode
:   With on-cluster image mode, you create a `MachineOSConfig` object where you include the Containerfile and other parameters. The build is performed on your cluster and the resulting custom layered image is automatically pushed to your repository and applied to the machine config pool that you specified in the `MachineOSConfig` object. The entire process is performed completely within your cluster.

Out-of-cluster image mode
:   With out-of-cluster image mode, you create a Containerfile that references an OpenShift Container Platform image and the RPM that you want to apply, build the layered image in your own environment, and push the image to your repository. Then, in your cluster, create a `MachineConfig` object for the targeted node pool that points to the new image. The Machine Config Operator overrides the base RHCOS image, as specified by the `osImageURL` value in the associated machine config, and boots the new image.

During OpenShift Container Platform installation
:   You can apply a pre-built custom layered image to specific nodes during OpenShift Container Platform installation.

Important

For these methods, use the same base RHCOS image installed on the rest of your cluster. Use the `oc adm release info --image-for rhel-coreos` command to obtain the base image used in your cluster.

### [11.2. Example Containerfiles](#coreos-layering-examples_mco-coreos-layering) Copy linkLink copied to clipboard!

Image mode for OpenShift allows you to use the following types of images to create custom layered images:

* **OpenShift Container Platform Hotfixes**. You can work with Customer Experience and Engagement (CEE) to obtain and apply Hotfix packages on top of your RHCOS image. In some instances, you might want a bug fix or enhancement before it is included in an official OpenShift Container Platform release. Image mode for OpenShift allows you to easily add the Hotfix before it is officially released and remove the Hotfix when the underlying RHCOS image incorporates the fix.

  Important

  Some Hotfixes require a Red Hat Support Exception and are outside of the normal scope of OpenShift Container Platform support coverage or life cycle policies.

  Hotfixes are provided to you based on Red Hat Hotfix policy. Apply it on top of the base image and test that new custom layered image in a non-production environment. When you are satisfied that the custom layered image is safe to use in production, you can roll it out on your own schedule to specific node pools. For any reason, you can easily roll back the custom layered image and return to using the default RHCOS.

  **Example on-cluster Containerfile to apply a Hotfix**

  ```
  containerfileArch: noarch
  content: |-
    FROM configs AS final
    #Install hotfix package
    RUN dnf update -y https://example.com/files/systemd-252-46.el9_4.x86_64.rpm \
                      https://example.com/files/systemd-journal-remote-252-46.el9_4.x86_64.rpm \
                      https://example.com/files/systemd-libs-252-46.el9_4.x86_64.rpm  \
                      https://example.com/files/systemd-pam-252-46.el9_4.x86_64.rpm \
                      https://example.com/files/systemd-udev-252-46.el9_4.x86_64.rpm \
                      https://example.com/files/systemd-rpm-macros-252-46.el9_4.noarch.rpm && \
        dnf clean all && \
        bootc container lint
  ```

  **Example out-of-cluster Containerfile to apply a Hotfix**

  ```
  FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...
  #Install hotfix package
  RUN dnf update -y https://example.com/files/systemd-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-journal-remote-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-libs-252-46.el9_4.x86_64.rpm  \
                    https://example.com/files/systemd-pam-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-udev-252-46.el9_4.x86_64.rpm \
                    https://example.com/files/systemd-rpm-macros-252-46.el9_4.noarch.rpm && \
      dnf clean all && \
      bootc container lint
  ```
* **RHEL packages**. You can download Red Hat Enterprise Linux (RHEL) packages from the Red Hat Customer Portal, such as chrony, firewalld, and iputils.

  **Example out-of-cluster Containerfile to apply the rsyslog utility**

  ```
  # Using a 4.18.0 image
  FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...
  # Install rsyslog package
  RUN dnf install -y rsyslog && \
      bootc container lint
  # Copy your custom configuration in
  ADD remote.conf /etc/rsyslog.d/remote.conf
  ```
* **Third-party packages**. You can download and install RPMs from third-party organizations, such as the following types of packages:

  + Bleeding edge drivers and kernel enhancements to improve performance or add capabilities.
  + Forensic client tools to investigate possible and actual break-ins.
  + Security agents.
  + Inventory agents that provide a coherent view of the entire cluster.
  + SSH Key management packages.

  **Example on-cluster Containerfile to apply a third-party package from EPEL**

  ```
  FROM configs AS final

  #Enable EPEL (more info at https://docs.fedoraproject.org/en-US/epel/ ) and install htop
  RUN dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm && \
      dnf install -y htop && \
      dnf clean all && \
      bootc container lint
  ```

  **Example out-of-cluster Containerfile to apply a third-party package from EPEL**

  ```
  # Get RHCOS base image of target cluster `oc adm release info --image-for rhel-coreos`
  FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...

  #Enable EPEL (more info at https://docs.fedoraproject.org/en-US/epel/ ) and install htop
  RUN dnf install -y https://dl.fedoraproject.org/pub/epel/epel-release-latest-9.noarch.rpm && \
      dnf install -y htop && \
      dnf clean all && \
      bootc container lint
  ```

  This Containerfile installs the RHEL fish program. Because fish requires additional RHEL packages, the image must be built on an entitled RHEL host. For RHEL entitlements to work, you must copy the `etc-pki-entitlement` secret into the `openshift-machine-config-operator` namespace.

  **Example on-cluster Containerfile to apply a third-party package that has RHEL dependencies**

  ```
  FROM configs AS final

  # RHEL entitled host is needed here to access RHEL packages
  # Install fish as third party package from EPEL
  RUN dnf install -y https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/Packages/f/fish-3.3.1-3.el9.x86_64.rpm && \
      dnf clean all && \
      bootc container lint
  ```

  **Example out-of-cluster Containerfile to apply a third-party package that has RHEL dependencies**

  ```
  # Get RHCOS base image of target cluster `oc adm release info --image-for rhel-coreos`
  FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...

  # RHEL entitled host is needed here to access RHEL packages
  # Install fish as third party package from EPEL
  RUN dnf install -y https://dl.fedoraproject.org/pub/epel/9/Everything/x86_64/Packages/f/fish-3.3.1-3.el9.x86_64.rpm && \
      dnf clean all && \
      bootc container lint
  ```

After you create the machine config, the Machine Config Operator (MCO) performs the following steps:

1. Renders a new machine config for the specified pool or pools.
2. Performs cordon and drain operations on the nodes in the pool or pools.
3. Writes the rest of the machine config parameters onto the nodes.
4. Applies the custom layered image to the node.
5. Reboots the node using the new image.

Important

It is strongly recommended that you test your images outside of your production environment before rolling out to your cluster.

### [11.3. About on-cluster image mode](#coreos-layering-configuring-on_mco-coreos-layering) Copy linkLink copied to clipboard!

You can use the image mode for OpenShift on-cluster build process to apply a custom layered image to your nodes by creating a `MachineOSConfig` custom resource (CR).

When you create the object, the Machine Config Operator (MCO) creates a `MachineOSBuild` object and a builder pod. The process also creates transient objects, such as config maps, which are cleaned up after the build is complete. The `MachineOSBuild` object and the associated `builder-*` pod use the same naming scheme, `<MachineOSConfig_CR_name>-<hash>`, for example:

**Example `MachineOSBuild` object**

```
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED
layered-image-c8765e26ebc87e1e17a7d6e0a78e8bae   False      False      True        False         False
```

**Example builder pod**

```
NAME                                                      READY   STATUS      RESTARTS        AGE
build-layered-image-c8765e26ebc87e1e17a7d6e0a78e8bae      2/2     Running     0               11m
```

You should not need to interact with these new objects or the `machine-os-builder` pod. However, you can use all of these resources for troubleshooting, if necessary.

When the build is complete, the MCO pushes the new custom layered image to your repository and rolls the image out to the nodes in the associated machine config pool. You can see the digested image pull spec for the new custom layered image in the `MachineOSConfig` object. This is now the active image pull spec for this `MachineOSConfig`.

**Example digested image pull spec**

```
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineOSConfig
metadata:
  annotations:
    machineconfiguration.openshift.io/current-machine-os-build: layered-9a8f89455246fa0c42ecee6ff1fa1a45
  labels:
    machineconfiguration.openshift.io/createdByOnClusterBuildsHelper: ""
  name: layered-image
# ...
status:
  currentImagePullSpec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-image@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
```

Tip

You can test a `MachineOSBuild` object to make sure it builds correctly without rolling out the custom layered image to active nodes by using a custom machine config pool that contains non-production nodes. Alternatively, you can use a custom machine config pool that has no nodes. The `MachineOSBuild` object builds even if there are no nodes for the MCO to deploy the custom layered image onto.

You can apply a custom layered image to any machine config pool in your cluster, including the control plane, worker, or custom pools.

Note

For single-node OpenShift clusters, you can apply a custom layered image to the control plane node only.

Making certain changes to a `MachineOSConfig` object triggers an automatic rebuild of the associated custom layered image. You can mitigate the effects of the rebuild by pausing the machine config pool where the custom layered image is applied as described in "Pausing the machine config pools". While the pools are paused, the MCO does not roll out the newly built image to the nodes after the build is complete. However, the build runs regardless of whether the pool is paused or not. For example, if you want to remove and replace a `MachineOSCOnfig` object, pausing the machine config pools before making the change prevents the MCO from reverting the associated nodes to the base image, reducing the number of reboots needed.

When a machine config pool is paused, the `oc get machineconfigpools` reports the following status:

**Example output**

```
NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master    rendered-master-a0b404d061a6183cc36d302363422aba    True      False      False      3              3                   3                     0                      4h14m
worker    rendered-worker-221507009cbcdec0eec8ab3ccd789d18    False     False      False      2              2                   2                     0                      4h14m
```

The `worker` machine config pool is paused, as indicated by the three `False` statuses and the `READYMACHINECOUNT` at `0`.

After the changes have been rolled out, you can unpause the machine config pool.

In the case of a build failure, for example due to network issues or an invalid secret, the MCO retries the build three additional times before the job fails. The MCO creates a different build pod for each build attempt. Note that the MCO automatically removes these build pods after a short period of time. Also, the affected machine config pool reports a build failure through the `ImageBuildDegraded` status condition. You can use the build pod logs to troubleshoot any build failures.

**Example failed `MachineOSBuild` object**

```
NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
layered-image-c8765e26ebc87e1e17a7d6e0a78e8bae   False      False      False        False        True     12m
```

You can manually rebuild your custom layered image by either modifying your `MachineOSConfig` object or applying an annotation to the `MachineOSConfig` object. For more information, see "Rebuilding an on-cluster custom layered image".

If you used a custom machine config pool to apply an on-cluster layered image to a node, you can remove the custom layered image from the node and revert to the base image. For more information, see "Reverting an on-cluster layered node".

You can modify an on-custom layered image as needed, to install additional packages, remove existing packages, change repositories, update secrets, or other similar changes, by editing the MachineOSConfig object. For more information, see "Modifying a custom layered image".

#### [11.3.1. On-cluster image mode known limitations](#coreos-layering-configuring-on-limitations_mco-coreos-layering) Copy linkLink copied to clipboard!

Note the following limitations when working with the on-cluster layering feature:

* On-cluster image mode is not supported on multi-architecture compute machines.
* Using multiple `MachineOSConfig` objects on the same machine config pool is not supported. You need a separate `MachineOSConfig` CR for each machine config pool where you want to use a distinct custom layered image.
* If you scale up a machine set that uses a custom layered image, the nodes reboot two times. The first, when the node is initially created with the base image and a second time when the custom layered image is applied.
* Node disruption policies are not supported on nodes with a custom layered image. However, the following machine configuration changes do not cause a new image build or the reboot of a node with an on-cluster custom layered image:

  + Modifying the configuration files in the `/var` or `/etc` directory
  + Adding or modifying a systemd service
  + Changing SSH keys
  + Removing mirroring rules from `ICSP`, `ITMS`, and `IDMS` objects
  + Changing the trusted CA, by updating the `user-ca-bundle` configmap in the `openshift-config` namespace
* The following machine configuration changes do cause a new image build and a node reboot:

  + Changing the kernel arguments
  + Changing the `OSImageURL` parameter
  + Adding or removing extensions
* The images used in creating custom layered images take up space in your push registry. Always be aware of the free space in your registry and prune the images as needed. You can automatically remove an on-cluster custom layered image from the repository by deleting the `MachineOSBuild` object that created the image. Note that the credentials provided by the registry push secret must also grant permission to delete an image from the registry. For more information, see "Removing an on-cluster custom layered image".

#### [11.3.2. Using the on-cluster image mode to apply a custom layered image](#coreos-layering-configuring-on-proc_mco-coreos-layering) Copy linkLink copied to clipboard!

You can use the on-cluster build process to apply a custom layered image to your cluster by creating a `MachineOSConfig` custom resource (CR).

The `MachineOSConfig` CR specifies the following parameters:

* the Containerfile to build
* the machine config pool to associate the build
* where the final image should be pushed and pulled from
* the push and pull secrets to use

You can create only one `MachineOSConfig` CR for each machine config pool.

**Prerequisites**

* You have the pull secret in the `openshift-machine-config-operator` namespace that the Machine Config Operator (MCO) needs in order to pull the base operating system image from your repository. By default, the MCO uses the cluster global pull secret, which it synchronizes into the `openshift-machine-config-operator` namespace. You can add your pull secret to the OpenShift Container Platform global pull secret or you can use a different pull secret. For information on modifying the global pull secret, see "Updating the global cluster pull secret".
* You have the push secret of the registry that the MCO needs to push the new custom layered image to. The credentials provided by the secret must also grant permission to delete an image from the registry.

  Note

  In a disconnected environment, ensure that the disconnected cluster can access the registry where you want to push the image. Image mirroring applies only to pulling images.
* You have the pull secret that your nodes need to pull the new custom layered image from your registry. This should be a different secret than the one used to push the image to the repository.
* You are familiar with how to configure a Containerfile. Instructions on how to create a Containerfile are beyond the scope of this documentation.
* Optional: You have a separate machine config pool for the nodes where you want to apply the custom layered image. One benefit to having a custom machine config pool for the nodes it that you can easily revert to the base image, if needed. For more information, see "Reverting an on-cluster layered node".

**Procedure**

1. Create a `MachineOSconfig` object:

   1. Create a YAML file similar to the following:

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineOSConfig
      metadata:
        name: layered-image
      spec:
        machineConfigPool:
          name: layered-image
        containerFile:
        - containerfileArch: NoArch
          content: |-
            FROM configs AS final
            RUN dnf install -y cowsay && \
              dnf clean all && \
              bootc container lint
        imageBuilder:
          imageBuilderType: Job
        baseImagePullSecret:
          name: global-pull-secret-copy
        renderedImagePushSpec: image-registry.openshift-image-registry.svc:5000/openshift/os-image:latest
        renderedImagePushSecret:
          name: builder-dockercfg-mtcl23
      ```

      where:

      `apiVersion`
      :   Specifies the `machineconfiguration.openshift.io/v1` API that is required for `MachineConfig` CRs.

      `metadata.name`
      :   Specifies a name for the `MachineOSConfig` object. The name must match the name of the associated machine config pool. This name is used with other on-cluster image mode resources. The examples in this documentation use the name `layered-image`.

      `spec.machineConfigPool.name`
      :   Specifies the name of the machine config pool associated with the nodes where you want to deploy the custom layered image. The examples in this documentation use the `layered-image` machine config pool.

      `spec.containerFile`
      :   Specifies the Containerfile to configure the custom layered image.

      `spec.containerFile.containerfileArch`
      :   Specifies the architecture this containerfile is to be built for: `ARM64`, `AMD64`, `PPC64LE`, `S390X`, or `NoArch`. The default is `NoArch`, which defines a Containerfile that can be applied to any architecture.

      `spec.imageBuilder`
      :   Specifies the name of the image builder to use. This must be `Job`, which is a reference to the `job` object that is managing the image build.

      `spec.baseImagePullSecret`
      :   Specifies the name of the pull secret that the MCO needs to pull the base operating system image from the registry. By default, the global pull secret is used. This parameter is optional.

      `spec.renderedImagePushSpec`
      :   Specifies the image registry to push the newly-built custom layered image to. This can be any registry that your cluster has access to in the `host[:port][/namespace]/name` or `svc_name.namespace.svc[:port]/repository/name:<tag>` format. This example uses the internal OpenShift Container Platform registry. You can specify a mirror registry if you cluster is properly configured to use a mirror registry.

      `spec.renderedImagePushSecret`
      :   Specifies the name of the push secret that the MCO needs to push the newly-built custom layered image to that registry.
   2. Create the `MachineOSConfig` object:

      ```
      $ oc create -f <filename>.yaml
      ```
2. If necessary, when the `MachineOSBuild` object has been created and is in the `READY` state, modify the node spec for the nodes where you want to use the new custom layered image:

   1. Check that the `MachineOSBuild` object is ready, by running the following command:

      ```
      $ oc get machineosbuild
      ```

      When the `SUCCEEDED` value is `True`, the build is complete:

      **Example output showing that the `MachineOSBuild` object is ready**

      ```
      NAME                                                     PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
      layered-image-ad5a3cad36303c363cf458ab0524e7c0-builder   False      False      True        False         False    43s
      ```
   2. Edit the nodes where you want to deploy the custom layered image by adding a label for the machine config pool you specified in the `MachineOSConfig` object:

      ```
      $ oc label node <node_name> 'node-role.kubernetes.io/<mcp_name>='
      ```

      where:

      node-role.kubernetes.io/<mcp\_name>=
      :   Specifies a node selector that identifies the nodes to deploy the custom layered image.

      When you save the changes, the MCO drains, cordons, and reboots the nodes. After the reboot, the node uses the new custom layered image.

**Verification**

1. Verify that the new pods are ready by running the following command:

   ```
   $ oc get pods -n openshift-machine-config-operator
   ```

   **Example output**

   ```
   NAME                                                                    READY   STATUS    RESTARTS   AGE
   build-layered-image-ad5a3cad36303c363cf458ab0524e7c0-hxrws              2/2     Running   0          2m40s
   # ...
   machine-os-builder-6fb66cfb99-zcpvq                                     1/1     Running   0          2m42s
   ```

   The build pod where the custom layered image is building is named in the `build-<MachineOSConfig_CR_name>-<hash>` format. The `machine-os-builder-*` pod can be used for troubleshooting.
2. Verify the custom layered image build by running a command similar to the following:

   ```
   $ oc get machineconfigpool <mcp_name> -o yaml
   ```

   **Example output**

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfigPool
   metadata:
     labels:
       machineconfiguration.openshift.io/mco-built-in: ""
       pools.operator.machineconfiguration.openshift.io/layered: ""
     name: layered
   # ...
   status:
   # ...
     conditions
   # ...
     - lastTransitionTime: "2025-09-09T13:43:35Z"
       message: 'Failed to build OS image for pool worker (MachineOSBuild: worker-2d03dc921ff0c242c5892a3ef1ed1608):
         Failed: Build Failed'
       reason: BuildFailed
       status: "True"
       type: ImageBuildDegraded
   ```

   The `reason: BuildFailed` status indicates whether the custom layered image build failed. If `False`, the build succeeded. If `True`, the build failed. You can use the build pod logs to troubleshoot any build failures.
3. Verify the current stage of your layered build by running the following command:

   ```
   $ oc get machineosbuilds
   ```

   **Example output**

   ```
   NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
   layered-image-ad5a3cad36303c363cf458ab0524e7c0   False      True       False       False         False    12m
   ```

   The `MachineOSBuild` object is named in the `<MachineOSConfig_CR_name>-<hash>` format.

   The build is complete when `BUILDING` is `False` and `SUCCEEDED` is `True`.
4. When the build is complete, verify that the image has been applied to the nodes in the affected pool by running a command similar to the following:

   ```
   $ oc describe machineconfignode/<machine_config_node_name>
   ```

   **Example machine config node output**

   ```
   Name:         ip-10-0-14-86.us-west-1.compute.internal
   API Version:  machineconfiguration.openshift.io/v1
   Kind:         MachineConfigNode
   # ...
   Spec:
     Config Image:
       Desired Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
     Config Version:
       Desired:  rendered-worker-d63c7736923b60b8b82492ae9a1eef40
     Node:
       Name:  ip-10-0-14-86.us-west-1.compute.internal
     Pool:
       Name:  worker
   # ...
   Status:
     Conditions:
   # ...
       Message:               Action during update to image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3: Successfully pulled OS image image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3 from registry
       Reason:                ImagePulledFromRegistry
       Status:                False
       Type:                  ImagePulledFromRegistry
   # ...
     Config Image:
       Current Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
       Desired Image:  image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/ocb-image@sha256:b485378fd8f7963ed74f14ce64f4f1e511e1601d49302b3046b1b78a83f539e3
   # ...
   ```

   The digested image pull spec for the new custom layered image is in the `Spec.Config Image.Desired Image` parameter.

   Important

   The `ImagePulledFromRegistry` condition is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

   For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).
5. Verify that the `MachineOSConfig` object contains a reference to the new custom layered image by running the following command:

   ```
   $ oc describe machineosconfig <object_name>
   ```

   **Example digested image pull spec**

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineOSConfig
   metadata:
     annotations:
       machineconfiguration.openshift.io/current-machine-os-build: layered-9a8f89455246fa0c42ecee6ff1fa1a45
     labels:
       machineconfiguration.openshift.io/createdByOnClusterBuildsHelper: ""
     name: layered-image
   # ...
   status:
     currentImagePullSpec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-image@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
   ```

   where:

   `status.currentImagePullSpec`
   :   Specifies the digested image pull spec for the new custom layered image.
6. Verify that the appropriate nodes are using the new custom layered image:

   1. Start a debug session as root for a control plane node by running the following command:

      ```
      $ oc debug node/<node_name>
      ```
   2. Set `/host` as the root directory within the debug shell:

      ```
      sh-4.4# chroot /host
      ```
   3. Run the `rpm-ostree status` command to view that the custom layered image is in use:

      ```
      sh-5.1# rpm-ostree status
      ```

      **Example output**

      ```
      # ...
      Deployments:
      * ostree-unverified-registry:image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-images@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
                         Digest: sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
                        Version: 419.94.202502100215-0 (2025-02-12T19:20:44Z)
      ```

      The `Deployments` stanza includes the digested image pull spec for the new custom layered image.

#### [11.3.3. Modifying an on-cluster custom layered image](#coreos-layering-configuring-on-modifying_mco-coreos-layering) Copy linkLink copied to clipboard!

You can modify an on-cluster custom layered image, as needed, to install additional packages, remove existing packages, change the pull or push repositories, update secrets, or other similar changes.

You can edit the `MachineOSConfig` object, apply changes to the YAML file that created the `MachineOSConfig` object, or create a new YAML file for that purpose.

If you modify and apply the `MachineOSConfig` object YAML or create a new YAML file, the YAML overwrites any changes you made directly to the `MachineOSConfig` object itself.

Making certain changes to a `MachineOSConfig` object triggers an automatic rebuild of the associated custom layered image. You can mitigate the effects of the rebuild by pausing the machine config pool where the custom layered image is applied as described in "Pausing the machine config pools". While the pools are paused, the MCO does not roll out the newly built image to the nodes after the build is complete. However, the build runs regardless of whether the pool is paused or not. For example, if you want to remove and replace a `MachineOSCOnfig` object, pausing the machine config pools before making the change prevents the MCO from reverting the associated nodes to the base image, reducing the number of reboots needed.

When a machine config pool is paused, the `oc get machineconfigpools` reports the following status:

**Example output**

```
NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
master    rendered-master-a0b404d061a6183cc36d302363422aba    True      False      False      3              3                   3                     0                      4h14m
worker    rendered-worker-221507009cbcdec0eec8ab3ccd789d18    False     False      False      2              2                   2                     0                      4h14m
```

The `worker` machine config pool is paused, as indicated by the three `False` statuses and the `READYMACHINECOUNT` at `0`.

After the changes have been rolled out, you can unpause the machine config pool.

**Prerequisites**

* You have opted in to on-cluster image mode by creating a `MachineOSConfig` object.

**Procedure**

* Modify an object to update the associated custom layered image:

  1. Edit the `MachineOSConfig` object to modify the custom layered image. The following example adds the `rngd` daemon to nodes that already have the tree package that was installed using a custom layered image.

     ```
     apiVersion: machineconfiguration.openshift.io/v1
     kind: MachineOSConfig
     metadata:
       name: layered-image
     spec:
       machineConfigPool:
         name: layered-image
       containerFile:
       - containerfileArch: noarch
         content: |-
           FROM configs AS final

           RUN rpm-ostree install rng-tools && \
               systemctl enable rngd && \
               rpm-ostree cleanup -m && \
               bootc container lint

           RUN rpm-ostree install tree && \
               bootc container lint
       imageBuilder:
         imageBuilderType: PodImageBuilder
       baseImagePullSecret:
         name: global-pull-secret-copy
       renderedImagePushspec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/os-images:latest
       renderedImagePushSecret:
         name: new-secret-name
     ```

     where:

     `spec:containerFile.content`
     :   Modify the Containerfile, for example to add or remove packages. This parameter is optional.

     `spec.baseImagePullSecret`
     :   Update the secret needed to pull the base operating system image from the registry. This parameter is optional.

     `spec.renderedImagePushspec`
     :   Modify the image registry to push the newly built custom layered image to. This parameter is optional.

     `spec.renderedImagePushSecret`
     :   Update the secret needed to push the newly built custom layered image to the registry. This parameter is optional.

     When you save the changes, the MCO drains, cordons, and reboots the nodes. After the reboot, the node uses the cluster base Red Hat Enterprise Linux CoreOS (RHCOS) image. If your changes modify a secret only, no new build is triggered and no reboot is performed.

**Verification**

1. Verify that the new `MachineOSBuild` object was created by using the following command:

   ```
   $ oc get machineosbuild
   ```

   **Example output**

   ```
   NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
   layered-image-a5457b883f5239cdcb71b57e1a30b6ef   False      False      True        False         False    4d17h
   layered-image-f91f0f5593dd337d89bf4d38c877590b   False      True       False       False         False    2m41s
   ```

   The value `True` in the `BUILDING` column indicates that the `MachineOSBuild` object is building. When the `SUCCEEDED` column reports `True`, the build is complete.
2. You can watch as the new machine config is rolled out to the nodes by using the following command:

   ```
   $ oc get machineconfigpools
   ```

   **Example output**

   ```
   NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   master    rendered-master-a0b404d061a6183cc36d302363422aba    True      False      False      3              3                   3                     0                      3h38m
   worker    rendered-worker-221507009cbcdec0eec8ab3ccd789d18    False     True       False      2              2                   2                     0                      3h38m
   ```

   The value `FALSE` in the `UPDATED` column indicates that the `MachineOSBuild` object is building. When the `UPDATED` column reports `FALSE`, the new custom layered image has rolled out to the nodes.
3. When the node is back in the `Ready` state, check that the changes were applied:

   1. Open an `oc debug` session to the node by running the following command:

      ```
      $ oc debug node/<node_name>
      ```
   2. Set `/host` as the root directory within the debug shell by running the following command:

      ```
      sh-5.1# chroot /host
      ```
   3. Use an appropriate command to verify that change was applied. The following examples shows that the `rngd` daemon was installed:

      ```
      sh-5.1# rpm -qa |grep rng-tools
      ```

      **Example output**

      ```
      rng-tools-6.17-3.fc41.x86_64
      ```

      ```
      sh-5.1# rngd -v
      ```

      **Example output**

      ```
      rngd 6.16
      ```

#### [11.3.4. Rebuilding an on-cluster custom layered image](#coreos-layering-configuring-on-rebuild_mco-coreos-layering) Copy linkLink copied to clipboard!

You can rebuild an on-cluster custom layered image by either modifying your `MachineOSConfig` object or adding an annotation to the `MachineOSConfig` object. Both of these actions trigger an automatic rebuild of the object.

For example, you could perform a rebuild if the you change the Containerfile or need to update the `osimageurl` location in a machine config.

After you add the annotation, the Machine Config Operator (MCO) deletes the current `MachineOSBuild` object and creates a new one in its place. When the build process is complete, the MCO automatically removes the annotation.

**Prerequisites**

* You have opted-in to on-cluster image mode by creating a `MachineOSConfig` object.

**Procedure**

* Edit the `MachineOSConfig` object to add the `machineconfiguration.openshift.io/rebuild` annotation by using the following command:

  ```
  $ oc edit MachineOSConfig <object_name>
  ```

  **Example `MachineOSConfig` object**

  ```
  apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineOSConfig
  metadata:
    annotations:
      machineconfiguration.openshift.io/current-machine-os-build: layering-c26d4a003432df70ee66c83981144cfa
      machineconfiguration.openshift.io/rebuild: ""
  # ...
    name: layered-image
  # ...
  ```

  Add the `machineconfiguration.openshift.io/rebuild: ""` annotation to trigger a rebuild of the custom layered image.

**Verification**

* Check that the `MachineOSBuild` object is building by using the following command:

  ```
  $ oc get machineosbuild
  ```

  **Example output**

  ```
  NAME                                             PREPARED   BUILDING   SUCCEEDED   INTERRUPTED   FAILED   AGE
  layered-image-d6b929a29c6dbfa8e4007c8069a2fd08   False      True       False       False         False    2m41s
  ```

  The value `True` in the `BUILDING` column indicates that the `MachineOSBuild` object is building.
* Edit the `MachineOSConfig` object to verify that the MCO removed the `machineconfiguration.openshift.io/rebuild` annotation by using the following command:

  ```
  $ oc edit MachineOSConfig <object_name>
  ```

  **Example `MachineOSConfig` object**

  ```
  apiVersion: machineconfiguration.openshift.io/v1
  kind: MachineOSConfig
  metadata:
    annotations:
      machineconfiguration.openshift.io/current-machine-os-build: layering-c26d4a003432df70ee66c83981144cfa
  # ...
    name: layered-image
  # ...
  ```

#### [11.3.5. Reverting an on-cluster custom layered image](#coreos-layering-configuring-on-revert_mco-coreos-layering) Copy linkLink copied to clipboard!

If you applied an on-cluster layered image to a node in a custom machine config pool (MCP), you can remove the custom layered image from the node and revert to the base image.

To revert the node, remove the node from the custom MCP by removing the custom machine config pool label from the node. After you remove the label, the Machine Config Operator (MCO) reboots the node with the cluster base Red Hat Enterprise Linux CoreOS (RHCOS) image, overriding the custom layered image.

Important

Before you remove the label, make sure the node is associated with another MCP.

**Prerequisites**

* You have opted-in to On-cluster image mode by creating a `MachineOSConfig` object.
* You have applied a `MachineOSConfig` object to a node in a custom machine config pool.

**Procedure**

* Remove the label from the node by using the following command:

  ```
  $ oc label node/<node_name> node-role.kubernetes.io/<mcp_name>-
  ```

  When you save the changes, the MCO drains, cordons, and reboots the nodes. After the reboot, the node uses the cluster base Red Hat Enterprise Linux CoreOS (RHCOS) image.

**Verification**

* Verify that the custom layered image is removed by performing any of the following checks:

  + Check that the worker machine config pool is updating with the previous machine config:

    ```
    $ oc get mcp
    ```

    **Sample output**

    ```
    NAME      CONFIG                                              UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
    layered   rendered-layered-e8c8bc1de69777325003e80bc0c04b82   True      False      False      0              0                   0                     0                      4h20m
    master    rendered-master-50d7bc27ee8b9ca2250383f0647ade7f    True      False      False      3              3                   3                     0                      5h39m
    worker    rendered-worker-e8c8bc1de69777325003e80bc0c04b82    True      False      False      3              3                   3                     0                      5h39m
    ```

    The custom machine config pool, named `layered`, no longer has any nodes. When the `UPDATING` field is `True`, the machine config pool is updating with the previous machine config. When the field becomes `False`, the worker machine config pool has rolled out to the previous machine config.
  + Check the nodes to see that scheduling on the nodes is disabled. This indicates that the change is being applied:

    ```
    $ oc get nodes
    ```

    **Example output**

    ```
    NAME                                         STATUS                     ROLES                  AGE   VERSION
    ip-10-0-148-79.us-west-1.compute.internal    Ready                      worker                 32m   v1.35.4
    ip-10-0-155-125.us-west-1.compute.internal   Ready,SchedulingDisabled   worker                 35m   v1.35.4
    ip-10-0-170-47.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
    ip-10-0-174-77.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
    ip-10-0-211-49.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
    ip-10-0-218-151.us-west-1.compute.internal   Ready                      worker                 31m   v1.35.4
    ```
  + When the node is back in the `Ready` state, check that the node is using the base image:

    1. Open an `oc debug` session to the node. For example:

       ```
       $ oc debug node/ip-10-0-155-125.us-west-1.compute.internal
       ```
    2. Set `/host` as the root directory within the debug shell:

       ```
       sh-4.4# chroot /host
       ```
    3. Run the `rpm-ostree status` command to view that the base image is in use:

       ```
       sh-4.4# rpm-ostree status
       ```

       **Example output**

       ```
       State: idle
       Deployments:
       * ostree-unverified-registry:registry.build05.ci.openshift.org/ci-ln-qd0hmqk/stable@sha256:a8bd32573f787f6d1c23e1d669abbefd1e31339826d06e750c0ca632ad6c414f
                          Digest: sha256:a8bd32573f787f6d1c23e1d669abbefd1e31339826d06e750c0ca632ad6c414f
                         Version: 419.96.202501202201-0 (2025-01-20T22:06:13Z)
       ```

#### [11.3.6. Removal of an on-cluster custom layered image](#coreos-layering-configuring-on-remove_mco-coreos-layering) Copy linkLink copied to clipboard!

You can remove an on-cluster custom layered image from the repository by deleting the `MachineOSBuild` object that created the image. Removing unneeded custom layered images prevents the images from taking up excessive space in your registry.

The credentials provided by the registry push secret that you added to the `MachineOSBuild` object must grant the permission for deleting an image from the registry. If the delete permission is not provided, the image is not removed when you delete the `MachineOSBuild` object.

The custom layered image is not deleted if the image is either currently in use on a node or is desired by the nodes, as indicated by the `machineconfiguration.openshift.io/currentImage` or `machineconfiguration.openshift.io/desiredImage` annotations on the node, which are added to the node when you create the `MachineOSConfig` object.

### [11.4. Using Out-of-cluster image mode to apply a custom layered image](#coreos-layering-configuring_mco-coreos-layering) Copy linkLink copied to clipboard!

You can use the image mode for OpenShift out-of-cluster build process to apply a custom layered image to your nodes by creating a `MachineOSConfig` custom resource (CR).

When you create the object, the Machine Config Operator (MCO) reboots those nodes with the new custom layered image, overriding the base Red Hat Enterprise Linux CoreOS (RHCOS) image.

To apply a custom layered image to your cluster, you must have the custom layered image in a repository that your cluster can access. Then, create a `MachineConfig` object that points to the custom layered image. You need a separate `MachineConfig` object for each machine config pool that you want to configure.

Important

As soon as you apply an out-of-cluster custom image to your cluster, you effectively *take ownership* of your custom layered images and those nodes. OpenShift Container Platform no longer automatically updates any node that uses the custom layered image. You become responsible for maintaining and updating your nodes as appropriate. If you roll back the custom layer, OpenShift Container Platform resumes automatically updating the node. See the "Updating with a RHCOS custom layered image" for important information about updating nodes that use a custom layered image.

**Prerequisites**

* You must create a custom layered image that is based on an OpenShift Container Platform image digest, not a tag.

  Note

  You should use the same base RHCOS image that is installed on the rest of your cluster. Use the `oc adm release info --image-for rhel-coreos` command to obtain the base image being used in your cluster.

  For example, the following Containerfile creates a custom layered image from an OpenShift Container Platform 4.22 image and overrides the kernel package with one from CentOS 9 Stream:

  **Example Containerfile for a custom layer image**

  ```
  # Using a 4.22.0 image
  FROM quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256...
  #Install hotfix rpm
  RUN rpm-ostree override replace http://mirror.stream.centos.org/9-stream/BaseOS/x86_64/os/Packages/kernel-{,core-,modules-,modules-core-,modules-extra-}5.14.0-295.el9.x86_64.rpm && \
      rpm-ostree cleanup -m && \
      bootc container lint
  ```

  where:

  `FROM`
  :   Specifies the RHCOS base image of your cluster.

  `RUN`
  :   Replaces the kernel packages.

  Note

  Instructions on how to create a Containerfile are beyond the scope of this documentation.
* Because the process for building a custom layered image is performed outside of the cluster, you must use the `--authfile /path/to/pull-secret` option with Podman or Buildah. Alternatively, to have the pull secret read by these tools automatically, you can add it to one of the default file locations: `~/.docker/config.json`, `$XDG_RUNTIME_DIR/containers/auth.json`, `~/.docker/config.json`, or `~/.dockercfg`. Refer to the `containers-auth.json` man page for more information.
* You must push the custom layered image to a repository that your cluster can access.

**Procedure**

1. Create a machine config file.

   1. Create a YAML file similar to the following:

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfig
      metadata:
        labels:
          machineconfiguration.openshift.io/role: worker
        name: os-layer-custom
      spec:
        osImageURL: quay.io/my-registry/custom-image@sha256...
      ```

      where:

      `metadata.labels`
      :   Specifies the machine config pool to deploy the custom layered image.

      `spec.osImageURL`
      :   Specifies the path to the custom layered image in the repository.
   2. Create the `MachineConfig` object:

      ```
      $ oc create -f <file_name>.yaml
      ```

      Important

      It is strongly recommended that you test your images outside of your production environment before rolling out to your cluster.

**Verification**

You can verify that the custom layered image is applied by performing any of the following checks:

1. Check that the worker machine config pool has rolled out with the new machine config:

   1. Check that the new machine config is created:

      ```
      $ oc get mc
      ```

      **Sample output**

      ```
      NAME                                               GENERATEDBYCONTROLLER                      IGNITIONVERSION   AGE
      00-master                                          5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
      00-worker                                          5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
      01-master-container-runtime                        5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
      01-master-kubelet                                  5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
      01-worker-container-runtime                        5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
      01-worker-kubelet                                  5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
      99-master-generated-registries                     5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
      99-master-ssh                                                                                 3.2.0             98m
      99-worker-generated-registries                     5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
      99-worker-ssh                                                                                 3.2.0             98m
      os-layer-custom                                                                                                 10s
      rendered-master-15961f1da260f7be141006404d17d39b   5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
      rendered-worker-5aff604cb1381a4fe07feaf1595a797e   5bdb57489b720096ef912f738b46330a8f577803   3.5.0             95m
      rendered-worker-5de4837625b1cbc237de6b22bc0bc873   5bdb57489b720096ef912f738b46330a8f577803   3.5.0             4s
      ```

      The `os-layer-custom` object is the newly created machine config. The `rendered-worker-5de4837625b1cbc237de6b22bc0bc873` object is the newly created rendered machine config.
   2. Check that the `osImageURL` value in the new machine config points to the expected image:

      ```
      $ oc describe mc rendered-worker-5de4837625b1cbc237de6b22bc0bc873
      ```

      **Example output**

      ```
      Name:         rendered-worker-5de4837625b1cbc237de6b22bc0bc873
      Namespace:
      Labels:       <none>
      Annotations:  machineconfiguration.openshift.io/generated-by-controller-version: 5bdb57489b720096ef912f738b46330a8f577803
                    machineconfiguration.openshift.io/release-image-version: 4.22.0-ec.3
      API Version:  machineconfiguration.openshift.io/v1
      Kind:         MachineConfig
      ...
        Os Image URL: quay.io/my-registry/custom-image@sha256...
      ```
   3. Check that the associated machine config pool is updated with the new machine config:

      ```
      $ oc get mcp
      ```

      **Sample output**

      ```
      NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
      master   rendered-master-15961f1da260f7be141006404d17d39b   True      False      False      3              3                   3                     0                      39m
      worker   rendered-worker-5de4837625b1cbc237de6b22bc0bc873   True      False      False      3              0                   0                     0                      39m
      ```

      When the `UPDATING` field is `True`, the machine config pool is updating with the new machine config. In this case, you will not see the new machine config listed in the output. When the field becomes `False`, the worker machine config pool has rolled out to the new machine config.
   4. Check the nodes to see that scheduling on the nodes is disabled. This indicates that the change is being applied:

      ```
      $ oc get nodes
      ```

      **Example output**

      ```
      NAME                                         STATUS                     ROLES                  AGE   VERSION
      ip-10-0-148-79.us-west-1.compute.internal    Ready                      worker                 32m   v1.35.4
      ip-10-0-155-125.us-west-1.compute.internal   Ready,SchedulingDisabled   worker                 35m   v1.35.4
      ip-10-0-170-47.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
      ip-10-0-174-77.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
      ip-10-0-211-49.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
      ip-10-0-218-151.us-west-1.compute.internal   Ready                      worker                 31m   v1.35.4
      ```
2. When the node is back in the `Ready` state, check that the node is using the custom layered image:

   1. Open an `oc debug` session to the node. For example:

      ```
      $ oc debug node/ip-10-0-155-125.us-west-1.compute.internal
      ```
   2. Set `/host` as the root directory within the debug shell:

      ```
      sh-4.4# chroot /host
      ```
   3. Run the `rpm-ostree status` command to view that the custom layered image is in use:

      ```
      sh-4.4# sudo rpm-ostree status
      ```

      **Example output**

      ```
      State: idle
      Deployments:
      * ostree-unverified-registry:quay.io/my-registry/...
                         Digest: sha256:...
      ```

#### [11.4.1. Reverting an out-of-cluster node](#coreos-layering-removing_mco-coreos-layering) Copy linkLink copied to clipboard!

You can revert an out-of-cluster custom layered image from the nodes in specific machine config pools. The Machine Config Operator (MCO) reboots those nodes with the cluster base Red Hat Enterprise Linux CoreOS (RHCOS) image, overriding the custom layered image.

To remove a Red Hat Enterprise Linux CoreOS (RHCOS) custom layered image from your cluster, you need to delete the machine config that applied the image.

**Procedure**

* Delete the machine config that applied the custom layered image.

  ```
  $ oc delete mc os-layer-custom
  ```

  After deleting the machine config, the nodes reboot.

**Verification**

You can verify that the custom layered image is removed by performing any of the following checks:

1. Check that the worker machine config pool is updating with the previous machine config:

   ```
   $ oc get mcp
   ```

   **Sample output**

   ```
   NAME     CONFIG                                             UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
   master   rendered-master-6faecdfa1b25c114a58cf178fbaa45e2   True      False      False      3              3                   3                     0                      39m
   worker   rendered-worker-6b000dbc31aaee63c6a2d56d04cd4c1b   False     True       False      3              0                   0                     0                      39m
   ```

   When the `UPDATING` field is `True`, the machine config pool is updating with the previous machine config. When the field becomes `False`, the worker machine config pool has rolled out to the previous machine config.
2. Check the nodes to see that scheduling on the nodes is disabled. This indicates that the change is being applied:

   ```
   $ oc get nodes
   ```

   **Example output**

   ```
   NAME                                         STATUS                     ROLES                  AGE   VERSION
   ip-10-0-148-79.us-west-1.compute.internal    Ready                      worker                 32m   v1.35.4
   ip-10-0-155-125.us-west-1.compute.internal   Ready,SchedulingDisabled   worker                 35m   v1.35.4
   ip-10-0-170-47.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
   ip-10-0-174-77.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
   ip-10-0-211-49.us-west-1.compute.internal    Ready                      control-plane,master   42m   v1.35.4
   ip-10-0-218-151.us-west-1.compute.internal   Ready                      worker                 31m   v1.35.4
   ```
3. When the node is back in the `Ready` state, check that the node is using the base image:

   1. Open an `oc debug` session to the node by running the following command:

      ```
      $ oc debug node/<node_name>
      ```
   2. Set `/host` as the root directory within the debug shell by running the following command:

      ```
      sh-5.1# chroot /host
      ```
   3. Run the `rpm-ostree status` command to view that the custom layered image is in use:

      ```
      sh-5.1# sudo rpm-ostree status
      ```

      **Example output**

      ```
      State: idle
      Deployments:
      * ostree-unverified-registry:podman pull quay.io/openshift-release-dev/ocp-release@sha256:e2044c3cfebe0ff3a99fc207ac5efe6e07878ad59fd4ad5e41f88cb016dacd73
                         Digest: sha256:e2044c3cfebe0ff3a99fc207ac5efe6e07878ad59fd4ad5e41f88cb016dacd73
      ```

### [11.5. Applying a custom layered image during OpenShift Container Platform installation](#coreos-layering-install-time_mco-coreos-layering) Copy linkLink copied to clipboard!

You can use the standard OpenShift Container Platform installation process to apply a custom layered image to your nodes by adding a `MachineOSConfig` custom resource (CR) YAML and a push secret YAML to the `<installation_directory>/manifests/` directory. This allows you to use image mode for OpenShift to apply additional functionality to specific nodes upon cluster installation.

After the installation, if you modify a machine config pool or update the OpenShift Container Platform version, the Machine Config Operator (MCO) builds and applies a new custom layered image, and pushes the updated image to your repository.

**Prerequisites**

* You have a custom layered image in a repository that your cluster can access.

  **Example containerFile for a custom layered image**

  ```
  FROM quay.io/centos/centos:stream9 AS centos
  RUN dnf install -y epel-release

  FROM [rhel-coreos image] AS configs
  COPY --from=centos /etc/yum.repos.d /etc/yum.repos.d
  COPY --from=centos /etc/pki/rpm-gpg/RPM-GPG-KEY-* /etc/pki/rpm-gpg/
  RUN sed -i 's/\$stream/9-stream/g' /etc/yum.repos.d/centos*.repo && \
      rpm-ostree install cowsay && \
      ostree container commit
  ```
* You have a repository and any needed secret where the MCO can push any updated custom layered images.

**Procedure**

1. Create a YAML file for the `MachineOSConfig` object similar to the following:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineOSConfig
   metadata:
     name: worker
     annotations:
       machineconfiguration.openshift.io/pre-built-image: "quay.io/myorg/custom-rhcos@sha256:abc123..."
   spec:
     machineConfigPool:
       name: worker
     imageBuilder:
       imageBuilderType: Job
     renderedImagePushSpec: quay.io/your-registry/layered-rhcos:latest
     renderedImagePushSecret:
       name: push-secret
     containerFile:
     - containerfileArch: NoArch
       content: |
         FROM configs AS final
         RUN rpm-ostree install cowsay && \
           ostree container commit
   ```

   where:

   `metadata.name`
   :   Specifies a name for the `MachineOSConfig` object. The name must match the name of the associated machine config pool.

   `metadata.annotations.machineconfiguration.openshift.io/pre-built-image`
   :   Specifies the digested image pull spec of your custom layered image.

   `spec.machineConfigPool`
   :   Specifies the name of the machine config pool associated with the nodes where you want to deploy the custom layered image.

   `spec.imageBuilder.imageBuilderType`
   :   Specifies the name of the image builder to use. This must be `Job`, which is a reference to the `job` object that is managing the image build.

   `spec.renderedImagePushSpec`
   :   Specifies an image registry to push any updated custom layered images to, if needed, after the installation process is complete. This can be any registry that your cluster has access to in the `host[:port][/namespace]/name` or `svc_name.namespace.svc[:port]/repository/name:<tag>` format. You can specify a mirror registry if you cluster is properly configured to use a mirror registry.

   `spec.renderedImagePushSecret.name`
   :   Specifies the name of the push secret needed by the MCO to push the updated custom layered image to that registry.

   `spec.containerFile`
   :   Specifies the containerFile that you used to create the custom layered image.
2. Create a YAML file for the push secret similar to the following:

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: push-secret
     namespace: openshift-machine-config-operator
   data:
     .dockerconfigjson: secret
   type: kubernetes.io/dockerconfigjson
   ```
3. When the `manifests` directory is available, add the `MachineOSConfig` YAML to the directory by using a command similar to the following:

   ```
   $ cp <file-name>.yaml manifests/
   ```

   where:

   `file-name`
   :   Specifies the YAML file for the `MachineOSConfig` object.
4. Add the push secret YAML to the `manifests` directory by using a command similar to the following:

   ```
   $ cp <file-name>.yaml manifests/
   ```

   where:

   `file-name`
   :   Specifies the YAML file for the push secret.
5. Continue with the installation process as usual.

**Verification**

* After the installation is complete, check that the `MachineOSConfig` object displays the `PreBuiltImageSeeded` status as `True` and contains a reference to the custom layered image by using the following command:

  ```
  $ oc get machineosconfigs.machineconfiguration.openshift.io -o yaml
  ```

  **Example output**

  ```
  apiVersion: v1
  items:
  - apiVersion: machineconfiguration.openshift.io/v1
    kind: MachineOSConfig
    metadata:
      annotations:
        machineconfiguration.openshift.io/current-machine-os-build: worker-4cedbc10da849ae7019288febc3a2d17
  # ...
    status:
      conditions:
      - lastTransitionTime: "2025-11-19T13:32:17Z"
        message: MachineOSConfig seeded with pre-built image "quay.io/myorg/custom-rhcos@sha256:abc123..."
        reason: PreBuiltImageSeeded
        status: "True"
        type: Seeded
      currentImagePullSpec: image-registry.openshift-image-registry.svc:5000/openshift-machine-config-operator/layered-rhcos@sha256:3c8fc667adcb432ce0c83581f16086afec08a961dd28fed69bb6bad6db0a0754
  ```

  where:

  `items.status.conditions.reason.PreBuiltImageSeeded.True`
  :   Specifies that the associated nodes were created using your custom layered image.

  `items.status.currentImagePullSpec`
  :   Specifies the digested image pull spec for the new custom layered image.

### [11.6. Updating with a RHCOS custom layered image](#coreos-layering-updating_mco-coreos-layering) Copy linkLink copied to clipboard!

When you configure image mode for OpenShift, OpenShift Container Platform no longer automatically updates the node pool that uses the custom layered image. You become responsible to manually update your nodes as appropriate.

Updating a node with a custom layered image is not required. However, if that node gets too far behind the current OpenShift Container Platform version, you could experience unexpected results.

To update a node that uses a custom layered image, follow these general steps:

1. The cluster automatically upgrades to version x.y.z+1, except for the nodes that use the custom layered image.
2. You could then create a new Containerfile that references the updated OpenShift Container Platform image and the RPM that you had previously applied.
3. Create a new machine config that points to the updated custom layered image.

## [Chapter 12. Setting the RHCOS version in a cluster](#mco-image-streams) Copy linkLink copied to clipboard!

You can create an OpenShift Container Platform cluster that uses Red Hat Enterprise Linux CoreOS (RHCOS) 10.x or update an existing cluster to RHCOS 10.x, which is available as a Technology Preview feature in OpenShift Container Platform 4.21.2 and greater. By running Red Hat Enterprise Linux CoreOS (RHCOS) 10.x as a Technology Preview feature, you can test how the operating system works with your cluster and your hardware, anticipate changes, and report bugs to Red Hat.

By default, RHCOS 9.x is installed on OpenShift Container Platform clusters starting with 4.13.

At any time, you can revert the cluster back to RHCOS 9.x, if needed.

Important

Using RHCOS 10.x in an OpenShift Container Platform cluster is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

RHCOS is a purpose-designed operating system for use with containers that is deployed by default on all OpenShift Container Platform nodes. Each version of RHCOS is based on a specific version of Red Hat Enterprise Linux (RHEL). For OpenShift Container Platform 4.13 and greater, the RHCOS version is based on RHEL 9.x.

Running a cluster with RHCOS 10.x is for **testing purposes only** on test clusters, and should not be used on production clusters. For example, by testing your cluster with RHCOS 10.x, you can ensure that any existing hardware operates as expected with the new operating system.

You can use one of the following methods to run the nodes in a cluster on RHCOS 10.x:

* Upgrading an existing 4.21.2 or later cluster to RHCOS 10.x. For more information, see "Updating the nodes in an existing cluster from RHCOS 9 to RHCOS 10".
* Deploying RHCOS 10.x on a new OpenShift Container Platform cluster. For more information, see "Installation configuration parameters".

### [12.1. Updating the nodes in an existing cluster from RHCOS 9 to RHCOS 10](#mco-image-streams-updating_mco-image-streams) Copy linkLink copied to clipboard!

For an existing OpenShift Container Platform 4.21.2 or later cluster, you can move the nodes in your machine config pool to Red Hat Enterprise Linux CoreOS (RHCOS) 10.x. By running Red Hat Enterprise Linux CoreOS (RHCOS) 10.x as a Technology Preview feature, you can test how the operating system works with your cluster and your hardware, anticipate changes, and report bugs to Red Hat.

Use the following procedure for an OpenShift Container Platform 4.22.x cluster. For an OpenShift Container Platform 4.21.x cluster that is 4.21.2 or later, see the [How to deploy a RHCOS 10 OpenShift Container Platform cluster knowledgebase article](https://access.redhat.com/articles/7138399).

Important

Running a cluster with a mixture of RHCOS 9.x and 10.x nodes is not supported. You must move all of your nodes to RHCOS 10.x.

**Prerequisites**

* You have updated the boot image in your cluster to at least RHCOS 9.x. Note that the boot image on each node remains at RHCOS 9.x after installing or upgrading to RHCOS 10.x. After you configure RHCOS 10.x in your cluster, new nodes boot using RHCOS 9.x initially and automatically upgrade to RHCOS 10.x. For more information, see "Manually updating the boot image".
* You have enabled the `TechPreviewNoUpgrade` feature set in your cluster’s `FeatureGate` custom resource (CR). For more information, see "Enabling features using feature gates".

**Procedure**

1. Confirm that your cluster has the RHCOS 10.x stream available by running the following command:

   ```
   $ oc get osImageStreams/cluster -o yaml | grep rhel-10
   ```

   **Example output**

   ```
     - name: rhel-10
   ```

   It can take several minutes for the `osImageStream` object to become available after you enable the `TechPreviewNoUpgrade` feature set.
2. Update the nodes by using one of the following procedures:

   * Update all of the nodes in your cluster to RHCOS 10:

     1. Edit the `OSImageStream` custom resource by running the following command:

        ```
        $ oc edit osimagestream cluster
        ```
     2. Add or edit the `defaultStream` parameter to specify `rhel-10`:

        ```
        apiVersion: machineconfiguration.openshift.io/v1alpha1
        kind: OSImageStream
        metadata:
          annotations:
            machineconfiguration.openshift.io/release-image-version: c4a08067821f304642e731fdcca0c8c6a6b19484
          creationTimestamp: "2026-04-13T17:27:41Z"
          generation: 1
          name: cluster
          resourceVersion: "36503"
          uid: f2ef4c15-4c1b-4117-850e-ae6adf408c4f
        spec:
          defaultStream: rhel-10
        status:
          availableStreams:
          - name: rhel-10
            osExtensionsImage: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:34baf90f333d89690a2f99b3ab746f8a43fee99b1218a8a058f75231f7c7ab53
            osImage: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:b208f0f861d009008b43a103e64d087f6da59e480bb0292d401895e041095da7
          - name: rhel-9
            osExtensionsImage: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:4aa864da633b1ce0a3612992a75849ff2b7d289699fa9b9b400522371a77d3ea
            osImage: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:cb34964bd5d957a1226e9fb082a591b650eca339ebd4aad15343d02fc21130dd
          defaultStream: rhel-9
        ```

        The `spec.defaultStream: rhel-10` parameter directs the Machine Config Operator (MCO) to update the nodes to the image referenced in `status.availableStreams.osImage` value under `name: rhel-10`.
   * Update all machine config pools to RHCOS 10:

     1. Update the worker machine config pool to RHCOS 10 by using the following command:

        ```
        $ oc patch mcp worker --type merge -p '{"spec":{"osImageStream":{"name":"rhel-10"}}}'
        ```
     2. Update the control plane machine config pool to RHCOS 10 by using the following command:

        ```
        $ oc patch mcp master --type merge -p '{"spec":{"osImageStream":{"name":"rhel-10"}}}'
        ```
     3. Update all custom machine config pools to RHCOS 10 by using the following command with the name of the machine config pool to update:

        ```
        $ oc patch mcp <mcp_name> --type merge -p '{"spec":{"osImageStream":{"name":"rhel-10"}}}'
        ```

        Replace `<mcp_name>` with the names of the custom machine config pools to update.

     Important

     Running a cluster with a mixture of RHCOS 9.x and 10.x nodes is not supported. You must move all of your nodes to RHCOS 10.x.

     Wait for the pools to finish rolling out the update.

**Verification**

1. After the nodes have returned to the READY state, examine the `/etc/redhat-release` file to see the current RHCOS version on the nodes:

   1. Log in to a node by using the following command:

      ```
      $ oc debug node/<node_name>
      ```

      Replace `<node_name>` with the name of the node.
   2. Set `/host` as the root directory within the debug shell by using the following command:

      ```
      $ chroot /host
      ```
   3. Look at the contents of the `/etc/redhat-release` file by using the following command:

      ```
      $ cat /etc/redhat-release
      ```

      The output should appear similar to the following example:

      **Example output**

      ```
      Red Hat Enterprise Linux release 10.2 (Coughlan)
      ```

## [Chapter 13. Machine Config Daemon metrics overview](#machine-config-daemon-metrics) Copy linkLink copied to clipboard!

The Machine Config Daemon, part of the Machine Config Operator, runs on every node in the cluster to manage configuration changes and updates on each of the nodes.

### [13.1. Understanding Machine Config Daemon metrics](#machine-config-daemon-metrics-understanding_machine-config-operator) Copy linkLink copied to clipboard!

You can access the metrics provided by the Machine Config Daemon by using the Prometheus Cluster Monitoring stack.

The following table describes this set of metrics. Some entries contain commands for getting specific logs. However, the most comprehensive set of logs is available using the `oc adm must-gather` command.

Note

Metrics marked with `*` in the **Name** and **Description** columns represent serious errors that might cause performance problems. Such problems might prevent updates and upgrades from proceeding.

Expand

Table 13.1. MCO metrics

| Name | Format | Description | Notes |
| --- | --- | --- | --- |
| `mcd_host_os_and_version` | `[]string{"os", "version"}` | Shows the OS that MCD is running on, such as RHCOS or RHEL. In case of RHCOS, the version is provided. |  |
| `mcd_drain_err*` |  | Logs errors received during failed drain. \* | While drains might need multiple tries to succeed, terminal failed drains prevent updates from proceeding. The `drain_time` metric, which shows how much time the drain took, might help with troubleshooting.  For further investigation, see the logs by running:  `$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-<hash> -c machine-config-daemon` |
| `mcd_pivot_err*` | `[]string{"err", "node", "pivot_target"}` | Logs errors encountered during pivot. \* | Pivot errors might prevent OS upgrades from proceeding.  For further investigation, run this command to see the logs from the `machine-config-daemon` container:  `$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-<hash> -c machine-config-daemon` |
| `mcd_state` | `[]string{"state", "reason"}` | State of Machine Config Daemon for the indicated node. Possible states are "Done", "Working", and "Degraded". In case of "Degraded", the reason is included. | For further investigation, see the logs by running:  `$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-<hash> -c machine-config-daemon` |
| `mcd_kubelet_state*` |  | Logs kubelet health failures. \* | This is expected to be empty, with failure count of 0. If failure count exceeds 2, the error indicating threshold is exceeded. This indicates a possible issue with the health of the kubelet.  For further investigation, run this command to access the node and see all its logs:  `$ oc debug node/<node> — chroot /host journalctl -u kubelet` |
| `mcd_reboot_err*` | `[]string{"message", "err", "node"}` | Logs the failed reboots and the corresponding errors. \* | This is expected to be empty, which indicates a successful reboot.  For further investigation, see the logs by running:  `$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-<hash> -c machine-config-daemon` |
| `mcd_update_state` | `[]string{"config", "err"}` | Logs success or failure of configuration updates and the corresponding errors. | The expected value is `rendered-master/rendered-worker-XXXX`. If the update fails, an error is present.  For further investigation, see the logs by running:  `$ oc logs -f -n openshift-machine-config-operator machine-config-daemon-<hash> -c machine-config-daemon` |

Show more

## [Legal Notice](#idm140329130314368) Copy linkLink copied to clipboard!

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
