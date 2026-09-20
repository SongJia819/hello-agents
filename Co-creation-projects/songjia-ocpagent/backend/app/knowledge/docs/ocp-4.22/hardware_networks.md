---
title: "Hardware networks"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/index
retrieved_at: 2026-09-05T05:41:49.289070+00:00
---

# Hardware networks

---

OpenShift Container Platform 4.22

## Configuring hardware-specific networking features in OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140583325988416)

**Abstract**

This document covers configuring Single Root I/O Virtualization (SR-IOV) and other hardware-specific network optimizations in OpenShift Container Platform.

---

## [Chapter 1. About Single Root I/O Virtualization (SR-IOV) hardware networks](#about-sriov) Copy linkLink copied to clipboard!

To share a single physical device with multiple pods, implement the Single Root I/O Virtualization (SR-IOV) specification. This standard enables flexible PCI device assignment, allowing a device to show as multiple separate physical devices for efficient resource allocation.

Note

As of OpenShift Container Platform 4.21, the SR-IOV Operator can support ARM hardware.

You can configure a Single Root I/O Virtualization (SR-IOV) device in your cluster by using the [SR-IOV Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

SR-IOV can segment a compliant network device, recognized on the host node as a physical function (PF), into multiple virtual functions (VFs). The VF is used like any other network device. The SR-IOV network device driver for the device determines how the VF is exposed in the container:

* `netdevice` driver: A regular kernel network device in the `netns` of the container
* `vfio-pci` driver: A character device mounted in the container

You can use SR-IOV network devices with additional networks on your OpenShift Container Platform cluster installed on bare metal or Red Hat OpenStack Platform (RHOSP) infrastructure for applications that require high bandwidth or low latency.

The SR-IOV Network Operator is supported on the following platforms:

* Bare metal
* Red Hat OpenStack Platform (RHOSP)

Note

For a list of devices, such as network interface controllers (NICs) that OpenShift Container Platform supports, see [Red Hat certified hardware](https://catalog.redhat.com/en/hardware) on the Red Hat Ecosystem Catalog. The following example, finds the Intel X710 network adapter:

1. From the Red Hat certified hardware webpage, click **Explore** from the **Components** tile.
2. From the **Provider** drop-down menu, click the **Intel Corporation** checkbox.
3. From the **Platform** drop-down menu, click the **Red Hat OpenShift Container Platform** checkbox.
4. Find the **Intel® Ethernet Server Adapter X710** network adapter from the list and then click on its tile. A new webpage opens that shows information for the network adapter.

You can configure multi-network policies for SR-IOV networks. The support for this is technology preview and SR-IOV additional networks are only supported with kernel NICs. They are not supported for Data Plane Development Kit (DPDK) applications.

Note

Creating multi-network policies on SR-IOV networks might not deliver the same performance to applications compared to SR-IOV networks without a multi-network policy configured.

Important

Multi-network policies for SR-IOV network is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

You can enable SR-IOV on a node by using the following command:

```
$ oc label node <node_name> feature.node.kubernetes.io/network-sriov.capable="true"
```

### [1.2. Components that manage SR-IOV network devices](#components-sr-iov-network-devices) Copy linkLink copied to clipboard!

The SR-IOV Network Operator creates and manages the components of the SR-IOV stack. The Operator performs the following functions:

* Orchestrates discovery and management of SR-IOV network devices
* Generates `NetworkAttachmentDefinition` custom resources for the SR-IOV Container Network Interface (CNI)
* Creates and updates the configuration of the SR-IOV network device plugin
* Creates node specific `SriovNetworkNodeState` custom resources
* Updates the `spec.interfaces` field in each `SriovNetworkNodeState` custom resource

The Operator provisions the following components:

SR-IOV network configuration daemon
:   A daemon set that is deployed on worker nodes when the SR-IOV Network Operator starts. The daemon is responsible for discovering and initializing SR-IOV network devices in the cluster.

SR-IOV Network Operator webhook
:   A dynamic admission controller webhook that validates the Operator custom resource and sets appropriate default values for unset fields.

SR-IOV Network resources injector
:   A dynamic admission controller webhook that provides functionality for patching Kubernetes pod specifications with requests and limits for custom network resources such as SR-IOV VFs. The SR-IOV network resources injector adds the `resource` field to only the first container in a pod automatically.

SR-IOV network device plugin
:   A device plugin that discovers, advertises, and allocates SR-IOV network virtual function (VF) resources. Device plugins are used in Kubernetes to enable the use of limited resources, typically in physical devices. Device plugins give the Kubernetes scheduler awareness of resource availability, so that the scheduler can schedule pods on nodes with sufficient resources.

SR-IOV CNI plugin
:   A CNI plugin that attaches VF interfaces allocated from the SR-IOV network device plugin directly into a pod.

SR-IOV InfiniBand CNI plugin
:   A CNI plugin that attaches InfiniBand (IB) VF interfaces allocated from the SR-IOV network device plugin directly into a pod.

Note

The SR-IOV Network resources injector and SR-IOV Network Operator webhook are enabled by default and can be disabled by editing the `default` `SriovOperatorConfig` CR. Use caution when disabling the SR-IOV Network Operator Admission Controller webhook. You can disable the webhook under specific circumstances, such as troubleshooting, or if you want to use unsupported devices.

### [1.4. Next steps](#about-sriov-next-steps) Copy linkLink copied to clipboard!

* [Configuring the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#configuring-sriov-operator)
* [Configuring an SR-IOV network device](#configuring-sriov-device "Chapter 2. Configuring an SR-IOV network device")
* If you use OpenShift Virtualization: [Connecting a virtual machine to an SR-IOV network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/virtualization/#virt-connecting-vm-to-sriov)
* [Configuring an SR-IOV network attachment](#configuring-sriov-net-attach "Chapter 3. Configuring an SR-IOV Ethernet network attachment")
* [Ethernet network attachement: Adding a pod to an SR-IOV additional network](#configuring-sriov-net-attach "Chapter 3. Configuring an SR-IOV Ethernet network attachment")
* [InfiniBand network attachement: Adding a pod to an SR-IOV additional network](#configuring-sriov-ib-attach "Chapter 4. Configuring an SR-IOV InfiniBand network attachment")

## [Chapter 2. Configuring an SR-IOV network device](#configuring-sriov-device) Copy linkLink copied to clipboard!

You can configure a Single Root I/O Virtualization (SR-IOV) device in your cluster.

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

### [2.1. SR-IOV network node configuration object](#nw-sriov-networknodepolicy-object_configuring-sriov-device) Copy linkLink copied to clipboard!

You specify the SR-IOV network device configuration for a node by creating an SR-IOV network node policy. The API object for the policy is part of the `sriovnetwork.openshift.io` API group.

The following YAML describes an SR-IOV network node policy:

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: <name>
  namespace: openshift-sriov-network-operator
spec:
  resourceName: <sriov_resource_name>
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
  priority: <priority>
  mtu: <mtu>
  needVhostNet: false
  numVfs: <num>
  externallyManaged: false
  nicSelector:
    vendor: "<vendor_code>"
    deviceID: "<device_id>"
    pfNames: ["<pf_name>", ...]
    rootDevices: ["<pci_bus_id>", ...]
    netFilter: "<filter_string>"
  deviceType: <device_type>
  isRdma: false
  linkType: <link_type>
  eSwitchMode: "switchdev"
  excludeTopology: false
```

where:

`metadata.name`
:   Specifies the name for the custom resource object.

`metadata.namespace`
:   Specifies the namespace where the SR-IOV Network Operator is installed.

`spec.resourceName`
:   Specifies the resource name of the SR-IOV network device plugin. You can create multiple SR-IOV network node policies for a resource name. When specifying a name, be sure to use the accepted syntax expression `^[a-zA-Z0-9_]+$`.

`spec.nodeSelector`
:   Specifies the nodes to configure. Only SR-IOV network devices on the selected nodes are configured. The SR-IOV Container Network Interface (CNI) plugin and device plugin are deployed on selected nodes only.

    Important

    The SR-IOV Network Operator applies node network configuration policies to nodes in sequence. Before applying node network configuration policies, the SR-IOV Network Operator checks if the machine config pool (MCP) for a node is in an unhealthy state such as `Degraded` or `Updating`. If a node is in an unhealthy MCP, the process of applying node network configuration policies to all targeted nodes in the cluster pauses until the MCP returns to a healthy state.

    To avoid a node in an unhealthy MCP from blocking the application of node network configuration policies to other nodes, including nodes in other MCPs, you must create a separate node network configuration policy for each MCP.

`spec.priority`
:   Optional: Specifies the priority as an integer value between `0` and `99`. A smaller value receives higher priority. For example, a priority of `10` is a higher priority than `99`. The default value is `99`.

`spec.mtu`
:   Optional: Specifies the maximum transmission unit (MTU) of the physical function and all its virtual functions. The maximum MTU value can vary for different network interface controller (NIC) models.

    Important

    If you want to create virtual function on the default network interface, ensure that the MTU is set to a value that matches the cluster MTU.

    If you want to modify the MTU of a single virtual function while the function is assigned to a pod, leave the MTU value blank in the SR-IOV network node policy. Otherwise, the SR-IOV Network Operator reverts the MTU of the virtual function to the MTU value defined in the SR-IOV network node policy, which might trigger a node drain.

`spec.needVhostNet`
:   Optional: Set to `true` to mount the `/dev/vhost-net` device in the pod. Use the mounted `/dev/vhost-net` device with Data Plane Development Kit (DPDK) to forward traffic to the kernel network stack.

`spec.numVfs`
:   Specifies the number of the virtual functions (VF) to create for the SR-IOV physical network device. For an Intel network interface controller (NIC), the number of VFs cannot be larger than the total VFs supported by the device. For a Mellanox NIC, the number of VFs cannot be larger than `127`.

`spec.externallyManaged`
:   Indicates whether the SR-IOV Network Operator manages all, or only a subset of virtual functions (VFs). With the value set to `false` the SR-IOV Network Operator manages and configures all VFs on the PF.

    Note

    When `externallyManaged` is set to `true`, you must manually create the Virtual Functions (VFs) on the physical function (PF) before applying the `SriovNetworkNodePolicy` resource. If the VFs are not pre-created, the SR-IOV Network Operator’s webhook will block the policy request.

    When `externallyManaged` is set to `false`, the SR-IOV Network Operator automatically creates and manages the VFs, including resetting them if necessary.

    To use VFs on the host system, you must create them through NMState, and set `externallyManaged` to `true`. In this mode, the SR-IOV Network Operator does not modify the PF or the manually managed VFs, except for those explicitly defined in the `nicSelector` field of your policy. However, the SR-IOV Network Operator continues to manage VFs that are used as pod secondary interfaces.

`spec.nicSelector`
:   Identifies the device to which this resource applies. You do not have to specify values for all the parameters. It is recommended to identify the network device with enough precision to avoid selecting a device unintentionally.

    If you specify `rootDevices`, you must also specify a value for `vendor`, `deviceID`, or `pfNames`. If you specify both `pfNames` and `rootDevices` at the same time, ensure that they refer to the same device. If you specify a value for `netFilter`, then you do not need to specify any other parameter because a network ID is unique.

`spec.nicSelector.vendor`
:   Optional: Specifies the vendor hexadecimal identifier of the SR-IOV network device. The only allowed values are `8086` (Intel) and `15b3` (Mellanox).

`spec.nicSelector.deviceID`
:   Optional: Specifies the device hexadecimal identifier of the SR-IOV network device. For example, `101b` is the device ID for a Mellanox ConnectX-6 device.

`spec.nicSelector.pfNames`
:   Optional: Specifies an array of one or more physical function (PF) names the resource must apply to. You can specify either the kernel-assigned interface name or an alternative name configured through the Kubernetes NMState Operator.

`spec.nicSelector.rootDevices`
:   Optional: Specifies an array of one or more PCI bus addresses the resource must apply to. For example `0000:02:00.1`.

`spec.nicSelector.netFilter`
:   Optional: Specifies the platform-specific network filter. The only supported platform is Red Hat OpenStack Platform (RHOSP). Acceptable values use the following format: `openstack/NetworkID:xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`. Replace `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx` with the value from the `/var/config/openstack/latest/network_data.json` metadata file. This filter ensures that VFs are associated with a specific OpenStack network. The operator uses this filter to map the VFs to the appropriate network based on metadata provided by the OpenStack platform.

`spec.deviceType`
:   Optional: Specifies the driver to configure for the VFs created from this resource. The only allowed values are `netdevice` and `vfio-pci`. The default value is `netdevice`.

    For a Mellanox NIC to work in DPDK mode on bare-metal nodes, use the `netdevice` driver type and set `isRdma` to `true`.

`spec.isRdma`
:   Optional: Configures whether to enable remote direct memory access (RDMA) mode. The default value is `false`.

    If the `isRdma` parameter is set to `true`, you can continue to use the RDMA-enabled VF as a normal network device. A device can be used in either mode.

    Set `isRdma` to `true` and additionally set `needVhostNet` to `true` to configure a Mellanox NIC for use with Fast data path DPDK applications.

    Note

    You cannot set the `isRdma` parameter to `true` for Intel NICs.

`spec.linkType`
:   Optional: Specifies the link type for the VFs. The default value is `eth` for Ethernet. Change this value to 'ib' for InfiniBand.

    When `linkType` is set to `ib`, `isRdma` is automatically set to `true` by the SR-IOV Network Operator webhook. When `linkType` is set to `ib`, `deviceType` should not be set to `vfio-pci`.

    Do not set `linkType` to `eth` for `SriovNetworkNodePolicy`, because this can lead to an incorrect number of available devices reported by the device plugin.

`spec.eSwitchMode`
:   Optional: Set to `"switchdev"` to enable hardware offloading. For more information about hardware offloading, see "Configuring hardware offloading".

`spec.excludeTopology`
:   Optional: Set to `true` to exclude advertising an SR-IOV network resource’s NUMA node to the Topology Manager. The default value is `false`.

#### [2.1.1. SR-IOV network node configuration examples](#nw-sr-iov-network-node-configuration-examples_configuring-sriov-device) Copy linkLink copied to clipboard!

The following example describes the configuration for an InfiniBand device:

**Example configuration for an InfiniBand device**

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: <name>
  namespace: openshift-sriov-network-operator
spec:
  resourceName: <sriov_resource_name>
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
  numVfs: <num>
  nicSelector:
    vendor: "<vendor_code>"
    deviceID: "<device_id>"
    rootDevices:
      - "<pci_bus_id>"
  linkType: <link_type>
  isRdma: true
# ...
```

The following example describes the configuration for an SR-IOV network device in a RHOSP virtual machine:

**Example configuration for an SR-IOV device in a virtual machine**

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: <name>
  namespace: openshift-sriov-network-operator
spec:
  resourceName: <sriov_resource_name>
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
  numVfs: 1
  nicSelector:
    vendor: "<vendor_code>"
    deviceID: "<device_id>"
    netFilter: "openstack/NetworkID:ea24bd04-8674-4f69-b0ee-fa0b3bd20509"
# ...
```

* When configuring the node network policy for a virtual machine, the `numVfs` parameter is always set to `1`.
* When the virtual machine is deployed on RHOSP, the `netFilter` parameter must refer to a network ID. Valid values for `netFilter` are available from an `SriovNetworkNodeState` object.

#### [2.1.2. Automated discovery of SR-IOV network devices](#discover-sr-iov-devices_configuring-sriov-device) Copy linkLink copied to clipboard!

The SR-IOV Network Operator searches your cluster for SR-IOV capable network devices on worker nodes. The Operator creates and updates a `SriovNetworkNodeState` custom resource (CR) for each worker node that provides a compatible SR-IOV network device.

The CR is assigned the same name as the worker node. The `status.interfaces` list provides information about the network devices on a node.

Important

Do not modify a `SriovNetworkNodeState` object. The Operator creates and manages these resources automatically.

The following YAML is an example of a `SriovNetworkNodeState` object created by the SR-IOV Network Operator:

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodeState
metadata:
  name: node-25
  namespace: openshift-sriov-network-operator
  ownerReferences:
  - apiVersion: sriovnetwork.openshift.io/v1
    blockOwnerDeletion: true
    controller: true
    kind: SriovNetworkNodePolicy
    name: default
spec:
  dpConfigVersion: "39824"
status:
  interfaces:
  - deviceID: "1017"
    driver: mlx5_core
    mtu: 1500
    name: ens785f0
    altNames:
    - production-nic
    pciAddress: "0000:18:00.0"
    totalvfs: 8
    vendor: 15b3
  - deviceID: "1017"
    driver: mlx5_core
    mtu: 1500
    name: ens785f1
    pciAddress: "0000:18:00.1"
    totalvfs: 8
    vendor: 15b3
  - deviceID: 158b
    driver: i40e
    mtu: 1500
    name: ens817f0
    pciAddress: 0000:81:00.0
    totalvfs: 64
    vendor: "8086"
  - deviceID: 158b
    driver: i40e
    mtu: 1500
    name: ens817f1
    pciAddress: 0000:81:00.1
    totalvfs: 64
    vendor: "8086"
  - deviceID: 158b
    driver: i40e
    mtu: 1500
    name: ens803f0
    pciAddress: 0000:86:00.0
    totalvfs: 64
    vendor: "8086"
  syncStatus: Succeeded
```

* The value of the `name` field is the same as the name of the worker node.
* The `interfaces` stanza includes a list of all of the SR-IOV devices discovered by the Operator on the worker node.
* The `altNames` field lists any alternative interface names configured through the Kubernetes NMState Operator. You can use these names in the `nicSelector.pfNames` field of a `SriovNetworkNodePolicy` CR.

#### [2.1.3. Configuring the SR-IOV Network Operator on Mellanox cards when Secure Boot is enabled](#nw-sriov-nic-mlx-secure-boot_configuring-sriov-device) Copy linkLink copied to clipboard!

The SR-IOV Network Operator supports an option to skip the firmware configuration for Mellanox devices. This option allows you to create virtual functions by using the SR-IOV Network Operator when the system has secure boot enabled. You must manually configure and allocate the number of virtual functions in the firmware before switching the system to secure boot.

Note

The number of virtual functions in the firmware is the maximum number of virtual functions that you can request in the policy.

**Procedure**

1. Configure the virtual functions (VFs) by running the following command when the system is without a secure boot when using the sriov-config daemon:

   ```
   $ mstconfig -d -0001:b1:00.1 set SRIOV_EN=1 NUM_OF_VFS=16
   ```

   * `SRIOV_EN=1` enables the SR-IOV Network Operator support on the Mellanox card.
   * `NUM_OF_VFS=16` specifies the number of virtual functions to enable in the firmware.
2. Configure the SR-IOV Network Operator by disabling the Mellanox plugin. See the following `SriovOperatorConfig` example configuration:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovOperatorConfig
   metadata:
     name: default
     namespace: openshift-sriov-network-operator
   spec:
     configDaemonNodeSelector: {}
     configurationMode: daemon
     disableDrain: false
     disablePlugins:
     - mellanox
     enableInjector: true
     enableOperatorWebhook: true
     logLevel: 2
   ```
3. Reboot the system to enable the virtual functions and the configuration settings.
4. Check the virtual functions (VFs) after rebooting the system by running the following command:

   ```
   $ oc -n openshift-sriov-network-operator get sriovnetworknodestate.sriovnetwork.openshift.io worker-0 -oyaml
   ```

   The following is example output:

   ```
   - deviceID: 101d
       driver: mlx5_core
       eSwitchMode: legacy
       linkSpeed: -1 Mb/s
       linkType: ETH
       mac: 08:c0:eb:96:31:25
       mtu: 1500
       name: ens3f1np1
       pciAddress: 0000:b1:00.1
       totalvfs: 16
       vendor: 15b3
   ```

   * The `totalvfs` value is the same number used in the `mstconfig` command earlier in the procedure.
5. Enable secure boot to prevent unauthorized operating systems and malicious software from loading during the device’s boot process.

   1. Enable secure boot by using the BIOS (Basic Input/Output System) to set values for the following parameters:

      * `Secure Boot: Enabled`
      * `Secure Boot Policy: Standard`
      * `Secure Boot Mode: Mode Deployed`
   2. Reboot the system.

#### [2.1.4. Virtual function (VF) partitioning for SR-IOV devices](#nw-sriov-nic-partitioning_configuring-sriov-device) Copy linkLink copied to clipboard!

In some cases, you might want to split virtual functions (VFs) from the same physical function (PF) into many resource pools. For example, you might want some of the VFs to load with the default driver and the remaining VFs load with the `vfio-pci` driver.

For example, the following YAML shows the selector for an interface named `netpf0` with VF `2` through `7`:

```
pfNames: ["netpf0#2-7"]
```

where:

`netpf0`
:   The name of the PF interface name.

`2`
:   The first VF index (0-based) that gets included in the range.

`7`
:   The last VF index (0-based) that gets included in the range.

You can select VFs from the same PF by using different policy CRs provided that you meet the following requirements:

* The `numVfs` value must be similar for policies that select the same PF.
* The VF index must be in the range of `0` to `<numVfs>-1`. For example, if you have a policy with `numVfs` set to `8`, then the `<first_vf>` value must not be smaller than `0`, and the `<last_vf>` must not be larger than `7`.
* The VFs ranges in different policies must not overlap.
* The `<first_vf>` must not be larger than the `<last_vf>`.

The following example illustrates NIC partitioning for an SR-IOV device.

The policy `policy-net-1` defines a resource pool `net-1` that includes the VF `0` of PF `netpf0` with the default VF driver. The policy `policy-net-1-dpdk` defines a resource pool `net-1-dpdk` that includes the VF `8` to `15` of PF `netpf0` with the `vfio` VF driver.

Policy `policy-net-1`:

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: policy-net-1
  namespace: openshift-sriov-network-operator
spec:
  resourceName: net1
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
  numVfs: 16
  nicSelector:
    pfNames: ["netpf0#0-0"]
  deviceType: netdevice
```

Policy `policy-net-1-dpdk`:

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: policy-net-1-dpdk
  namespace: openshift-sriov-network-operator
spec:
  resourceName: net1dpdk
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: "true"
  numVfs: 16
  nicSelector:
    pfNames: ["netpf0#8-15"]
  deviceType: vfio-pci
```

##### [2.1.4.1. Verifying that the interface is successfully partitioned](#verifying-that-the-interface-is-successfully-partitioned) Copy linkLink copied to clipboard!

Confirm that the interface partitioned to virtual functions (VFs) for the SR-IOV device by running the following command:

```
$ ip link show <interface>
```

`<interface>` specifies the interface that you specified when partitioning to VFs for the SR-IOV device, for example, `ens3f1`.

The following is example output:

```
5: ens3f1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
link/ether 3c:fd:fe:d1:bc:01 brd ff:ff:ff:ff:ff:ff

vf 0     link/ether 5a:e7:88:25:ea:a0 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
vf 1     link/ether 3e:1d:36:d7:3d:49 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
vf 2     link/ether ce:09:56:97:df:f9 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
vf 3     link/ether 5e:91:cf:88:d1:38 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
vf 4     link/ether e6:06:a1:96:2f:de brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
```

#### [2.1.5. A test pod template for clusters that use SR-IOV on OpenStack](#nw-openstack-ovs-sr-iov-testpmd-pod_configuring-sriov-device) Copy linkLink copied to clipboard!

The following `testpmd` pod demonstrates container creation with huge pages, reserved CPUs, and the SR-IOV port.

**An example `testpmd` pod**

```
apiVersion: v1
kind: Pod
metadata:
  name: testpmd-sriov
  namespace: mynamespace
  annotations:
    cpu-load-balancing.crio.io: "disable"
    cpu-quota.crio.io: "disable"
# ...
spec:
  containers:
  - name: testpmd
    command: ["sleep", "99999"]
    image: registry.redhat.io/openshift4/dpdk-base-rhel8:v4.9
    securityContext:
      capabilities:
        add: ["IPC_LOCK","SYS_ADMIN"]
      privileged: true
      runAsUser: 0
    resources:
      requests:
        memory: 1000Mi
        hugepages-1Gi: 1Gi
        cpu: '2'
        openshift.io/sriov1: 1
      limits:
        hugepages-1Gi: 1Gi
        cpu: '2'
        memory: 1000Mi
        openshift.io/sriov1: 1
    volumeMounts:
      - mountPath: /dev/hugepages
        name: hugepage
        readOnly: False
  runtimeClassName: performance-cnf-performanceprofile
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
```

* This example assumes that the name of the performance profile is `cnf-performance profile`.

#### [2.1.6. A test pod template for clusters that use OVS hardware offloading on OpenStack](#nw-openstack-hw-offload-testpmd-pod_configuring-sriov-device) Copy linkLink copied to clipboard!

The following `testpmd` pod demonstrates Open vSwitch (OVS) hardware offloading on Red Hat OpenStack Platform (RHOSP).

**An example `testpmd` pod**

```
apiVersion: v1
kind: Pod
metadata:
  name: testpmd-sriov
  namespace: mynamespace
  annotations:
    k8s.v1.cni.cncf.io/networks: hwoffload1
spec:
  runtimeClassName: performance-cnf-performanceprofile
  containers:
  - name: testpmd
    command: ["sleep", "99999"]
    image: registry.redhat.io/openshift4/dpdk-base-rhel8:v4.9
    securityContext:
      capabilities:
        add: ["IPC_LOCK","SYS_ADMIN"]
      privileged: true
      runAsUser: 0
    resources:
      requests:
        memory: 1000Mi
        hugepages-1Gi: 1Gi
        cpu: '2'
      limits:
        hugepages-1Gi: 1Gi
        cpu: '2'
        memory: 1000Mi
    volumeMounts:
      - mountPath: /mnt/huge
        name: hugepage
        readOnly: False
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
```

* If your performance profile is not named `cnf-performance profile`, replace that string with the correct performance profile name.

#### [2.1.7. Huge pages resource injection for Downward API](#nw-sriov-hugepages_configuring-sriov-device) Copy linkLink copied to clipboard!

When a pod specification includes a resource request or limit for huge pages, the Network Resources Injector automatically adds Downward API fields to the pod specification to provide the huge pages information to the container.

The Network Resources Injector adds a volume that is named `podnetinfo` and is mounted at `/etc/podnetinfo` for each container in the pod. The volume uses the Downward API and includes a file for huge pages requests and limits. The file naming convention is as follows:

* `/etc/podnetinfo/hugepages_1G_request_<container-name>`
* `/etc/podnetinfo/hugepages_1G_limit_<container-name>`
* `/etc/podnetinfo/hugepages_2M_request_<container-name>`
* `/etc/podnetinfo/hugepages_2M_limit_<container-name>`

The paths specified in the previous list are compatible with the `app-netutil` library. By default, the library is configured to search for resource information in the `/etc/podnetinfo` directory. If you choose to specify the Downward API path items yourself manually, the `app-netutil` library searches for the following paths in addition to the paths in the previous list.

* `/etc/podnetinfo/hugepages_request`
* `/etc/podnetinfo/hugepages_limit`
* `/etc/podnetinfo/hugepages_1G_request`
* `/etc/podnetinfo/hugepages_1G_limit`
* `/etc/podnetinfo/hugepages_2M_request`
* `/etc/podnetinfo/hugepages_2M_limit`

As with the paths that the Network Resources Injector can create, the paths in the preceding list can optionally end with a `_<container-name>` suffix.

### [2.2. Configuring SR-IOV network devices](#nw-sriov-configuring-device_configuring-sriov-device) Copy linkLink copied to clipboard!

The SR-IOV Network Operator adds the `SriovNetworkNodePolicy.sriovnetwork.openshift.io` custom resource definition (CRD) to OpenShift Container Platform. You can configure an SR-IOV network device by creating a `SriovNetworkNodePolicy` custom resource (CR).

Note

When applying the configuration specified in a `SriovNetworkNodePolicy` CR, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes. Reboot only happens in the following cases:

* With Mellanox NICs (`mlx5` driver) a node reboot happens every time the number of virtual functions (VFs) increase on a physical function (PF).
* With Intel NICs, a reboot only happens if the kernel parameters do not include `intel_iommu=on` and `iommu=pt`.

It might take several minutes for a configuration change to apply.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the SR-IOV Network Operator.
* You have enough available nodes in your cluster to handle the evicted workload from drained nodes.
* You have not selected any control plane nodes for SR-IOV network device configuration.

**Procedure**

1. Create an `SriovNetworkNodePolicy` object, and then save the YAML in the `<name>-sriov-node-network.yaml` file. Replace `<name>` with the name for this configuration.
2. Optional: Label the SR-IOV capable cluster nodes with `SriovNetworkNodePolicy.Spec.NodeSelector` if they are not already labeled. For more information about labeling nodes, see "Understanding how to update labels on nodes".
3. Create the `SriovNetworkNodePolicy` object. When running the following command, replace `<name>` with the name for this configuration:

   ```
   $ oc create -f <name>-sriov-node-network.yaml
   ```

   After applying the configuration update, all the pods in the `sriov-network-operator` namespace change to the `Running` status.
4. To verify your SR-IOV network device configuration, enter the following command and replace `<node_name>` with the name of the node where you configured the device.

   ```
   $ oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name> -o jsonpath='{.status.syncStatus}'
   ```

### [2.3. Creating a non-uniform memory access (NUMA) aligned SR-IOV pod](#nw-sriov-topology-manager_configuring-sriov-device) Copy linkLink copied to clipboard!

You can create a NUMA aligned SR-IOV pod by restricting SR-IOV and the CPU resources allocated from the same NUMA node with `restricted` or `single-numa-node` Topology Manager policies.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have configured the CPU Manager policy to `static`. For more information on CPU Manager, see the "Additional resources" section.
* You have configured the Topology Manager policy to `single-numa-node`.

  Note

  When `single-numa-node` is unable to satisfy the request, you can configure the Topology Manager policy to `restricted`. For more flexible SR-IOV network resource scheduling, see *Excluding SR-IOV network topology during NUMA-aware scheduling* in the *Additional resources* section.

**Procedure**

1. Create the following SR-IOV pod spec, and then save the YAML in the `<name>-sriov-pod.yaml` file. Replace `<name>` with a name for this pod.

   The following example shows an SR-IOV pod spec:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: sample-pod
     annotations:
       k8s.v1.cni.cncf.io/networks: <name>
   spec:
     containers:
     - name: sample-container
       image: <image>
       command: ["sleep", "infinity"]
       resources:
         limits:
           memory: "1Gi"
           cpu: "2"
         requests:
           memory: "1Gi"
           cpu: "2"
   ```

   * `<name>` specifies the name of the SR-IOV network attachment definition CR.
   * `<image>` specifies the name of the `sample-pod` image.
   * To create the SR-IOV pod with guaranteed QoS, set `memory limits` equal to `memory requests`.
   * To create the SR-IOV pod with guaranteed QoS, set `cpu limits` equal to `cpu requests`.
2. Create the sample SR-IOV pod by running the following command:

   ```
   $ oc create -f <filename>
   ```

   * `<filename>` specifies the name of the file you created in the earlier step.
3. Confirm that the `sample-pod` is configured with guaranteed QoS.

   ```
   $ oc describe pod sample-pod
   ```
4. Confirm that the `sample-pod` is allocated with exclusive CPUs.

   ```
   $ oc exec sample-pod -- cat /sys/fs/cgroup/cpuset/cpuset.cpus
   ```
5. Confirm that the SR-IOV device and CPUs that are allocated for the `sample-pod` are on the same NUMA node.

   ```
   $ oc exec sample-pod -- cat /sys/fs/cgroup/cpuset/cpuset.cpus
   ```

### [2.4. Exclude the SR-IOV network topology for NUMA-aware scheduling](#nw-sriov-exclude-topology-manager_configuring-sriov-device) Copy linkLink copied to clipboard!

You can exclude advertising the Non-Uniform Memory Access (NUMA) node for the SR-IOV network to the Topology Manager for more flexible SR-IOV network deployments during NUMA-aware pod scheduling.

In some scenarios, it is a priority to maximize CPU and memory resources for a pod on a single NUMA node. By not providing a hint to the Topology Manager about the NUMA node for the pod’s SR-IOV network resource, the Topology Manager can deploy the SR-IOV network resource and the pod CPU and memory resources to different NUMA nodes. This can add to network latency because of the data transfer between NUMA nodes. However, it is acceptable in scenarios when workloads require optimal CPU and memory performance.

For example, consider a compute node, `compute-1`, that features two NUMA nodes: `numa0` and `numa1`. The SR-IOV-enabled NIC is present on `numa0`. The CPUs available for pod scheduling are present on `numa1` only. By setting the `excludeTopology` specification to `true`, the Topology Manager can assign CPU and memory resources for the pod to `numa1` and can assign the SR-IOV network resource for the same pod to `numa0`. This is only possible when you set the `excludeTopology` specification to `true`. Otherwise, the Topology Manager attempts to place all resources on the same NUMA node.

### [2.5. Troubleshooting SR-IOV configuration](#nw-sriov-troubleshooting_configuring-sriov-device) Copy linkLink copied to clipboard!

After following the procedure to configure an SR-IOV network device, the following sections address some error conditions.

**Procedure**

* To display the state of nodes, run the following command:

  ```
  $ oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name>
  ```

  `<node_name>` specifies the name of a node with an SR-IOV network device.

  If the output from the command indicates "cannot allocate memory", check the following items:

  + Confirm that global SR-IOV settings are enabled in the BIOS for the node.
  + Confirm that VT-d is enabled in the BIOS for the node.

## [Chapter 3. Configuring an SR-IOV Ethernet network attachment](#configuring-sriov-net-attach) Copy linkLink copied to clipboard!

You can configure an Ethernet network attachment for an Single Root I/O Virtualization (SR-IOV) device in the cluster.

Before you perform any tasks in the following documentation, ensure that you installed the SR-IOV Network Operator.

### [3.1. Ethernet device configuration object](#nw-sriov-network-object_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

You can configure an Ethernet network device by defining an `SriovNetwork` object.

The following YAML describes an `SriovNetwork` object:

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: <name>
  namespace: openshift-sriov-network-operator
spec:
  resourceName: <sriov_resource_name>
  networkNamespace: <target_namespace>
  vlan: <vlan>
  spoofChk: "<spoof_check>"
  ipam: |-
    {}
  linkState: <link_state>
  maxTxRate: <max_tx_rate>
  minTxRate: <min_tx_rate>
  vlanQoS: <vlan_qos>
  trust: "<trust_vf>"
  capabilities: <capabilities>
```

`metadata.name`
:   Specifies a name for the object. The SR-IOV Network Operator creates a `NetworkAttachmentDefinition` object with same name.

`metadata.namespace`
:   Specifies the namespace where the SR-IOV Network Operator is installed. You can also install the SR-IOV Network Operator in any namespace.

`spec.resourceName`
:   Specifies the value for the `spec.resourceName` parameter from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network.

`spec.networkNamespace`
:   Specifies the target namespace for the `SriovNetwork` object. Only pods in the target namespace can attach to the additional network. When installing the SR-IOV Network Operator in a namespace other than `openshift-sriov-network-operator`, you must not configure this field.

`spec.vlan`
:   Optional: Specifies the VLAN ID to assign to an additional network. The default value of `0` means that an additional network has no VLAN ID tag. Supported VLAN ID values range from `1` to `4094`.

`spec.spoofChk`
:   Optional: Specifies the spoof check mode of the VF. The allowed values are the strings `"on"` and `"off"`.

    Important

    You must enclose the value you specify in quotes or the object is rejected by the SR-IOV Network Operator.

`spec.ipam`
:   Specifies a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.

`spec.linkState`
:   Optional: Specifies the link state of virtual function (VF). Allowed values are `enable`, `disable`, and `auto`.

`spec.maxTxRate`
:   Optional: Specifies a maximum transmission rate, in Mbps, for the VF.

`spec.minTxRate`
:   Optional: Specifies a minimum transmission rate, in Mbps, for the VF. This value must be less than or equal to the maximum transmission rate.

    Note

    Intel NICs do not support the `minTxRate` parameter. For more information, see [BZ#1772847](https://bugzilla.redhat.com/show_bug.cgi?id=1772847).

`spec.vlanQoS`
:   Optional: Specifies an IEEE 802.1p priority level for the VF. The default value is `0`.

`spec.trust`
:   Optional: Specifies the trust mode of the VF. The allowed values are the strings `"on"` and `"off"`.

    Important

    You must enclose the value that you specify in quotes, or the SR-IOV Network Operator rejects the object.

`spec.capabilities`
:   Optional: Specifies the capabilities to configure for this additional network. You can specify `'{ "ips": true }'` to enable IP address support or `'{ "mac": true }'` to enable MAC address support.

#### [3.1.1. Creating a configuration for assignment of dual-stack IP addresses dynamically](#nw-multus-configure-dualstack-ip-address_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

You can dynamically assign dual-stack IP addresses to a secondary network so that pods can communicate over both IPv4 and IPv6 addresses.

You can configure the following IP address assignment types in the `ipRanges` parameter:

* IPv4 addresses
* IPv6 addresses
* multiple IP address assignment

**Procedure**

1. Set `type` to `whereabouts`.
2. Use `ipRanges` to allocate IP addresses as shown in the following example:

   ```
   cniVersion: operator.openshift.io/v1
   kind: Network
   metadata:
     name: cluster
   spec:
     additionalNetworks:
     - name: whereabouts-shim
       namespace: default
       type: Raw
       rawCNIConfig: |-
         {
          "name": "whereabouts-dual-stack",
          "cniVersion": "0.3.1,
          "type": "bridge",
          "ipam": {
            "type": "whereabouts",
            "ipRanges": [
                     {"range": "192.168.10.0/24"},
                     {"range": "2001:db8::/64"}
                 ]
          }
         }
   ```
3. Attach the secondary network to a pod. For more information, see "Adding a pod to a secondary network".

**Verification**

* Verify that all IP addresses got assigned to the network interfaces within the network namespace of a pod by entering the following command:

  ```
  $ oc exec -it <pod_name> -- ip a
  ```

  where:

  `<pod_name>`
  :   The name of the pod.

#### [3.1.2. Configuration of IP address assignment for a network attachment](#nw-multus-ipam-object_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

For secondary networks, you can assign IP addresses by using an IP Address Management (IPAM) CNI plugin, which supports various assignment methods, including Dynamic Host Configuration Protocol (DHCP) and static assignment.

The DHCP IPAM CNI plugin responsible for dynamic assignment of IP addresses operates with two distinct components:

* CNI Plugin: Responsible for integrating with the Kubernetes networking stack to request and release IP addresses.
* DHCP IPAM CNI Daemon: A listener for DHCP events that coordinates with existing DHCP servers in the environment to handle IP address assignment requests. This daemon is not a DHCP server itself.

For networks requiring `type: dhcp` in their IPAM configuration, ensure the DHCP server meets the following conditions:

* A DHCP server is available and running in the environment.
* The DHCP server is external to the cluster and you expect the server to form part of the existing network infrastructure for the customer.
* The DHCP server is appropriately configured to serve IP addresses to the nodes.

In cases where a DHCP server is unavailable in the environment, consider using the Whereabouts IPAM CNI plugin. The Whereabouts CNI provides similar IP address management capabilities without the need for an external DHCP server.

Note

Use the Whereabouts CNI plugin when no external DHCP server exists or where static IP address management is preferred. The Whereabouts plugin includes a reconciler daemon to manage stale IP address allocations.

Ensure the periodic renewal of a DHCP lease throughout the lifetime of a container by including a separate daemon, the DHCP IPAM CNI Daemon. To deploy the DHCP IPAM CNI daemon, change the Cluster Network Operator (CNO) configuration to trigger the deployment of this daemon as part of the secondary network setup.

##### [3.1.2.1. Static IP address assignment configuration](#nw-multus-static_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

The following table describes the configuration for static IP address assignment:

Expand

Table 3.1. ipam static configuration object

| Field | Type | Description |
| --- | --- | --- |
| `type` | `string` | The IPAM address type. The value `static` is required. |
| `addresses` | `array` | An array of objects specifying IP addresses to assign to the virtual interface. Both IPv4 and IPv6 IP addresses are supported. |
| `routes` | `array` | An array of objects specifying routes to configure inside the pod. |
| `dns` | `array` | Optional: An array of objects specifying the DNS configuration. |

Show more

The `addresses` array requires objects with the following fields:

Expand

Table 3.2. ipam.addresses[] array

| Field | Type | Description |
| --- | --- | --- |
| `address` | `string` | An IP address and network prefix that you specify. For example, if you specify `10.10.21.10/24`, the secondary network gets assigned an IP address of `10.10.21.10` and the subnet mask of `255.255.255.0`. |
| `gateway` | `string` | The default gateway to route egress network traffic to. |

Show more

Expand

Table 3.3. ipam.routes[] array

| Field | Type | Description |
| --- | --- | --- |
| `dst` | `string` | The IP address range in CIDR format, such as `192.168.17.0/24` or `0.0.0.0/0` for the default route. |
| `gw` | `string` | The gateway that routes network traffic. |

Show more

Expand

Table 3.4. ipam.dns object

| Field | Type | Description |
| --- | --- | --- |
| `nameservers` | `array` | An array of one or more IP addresses where DNS queries get sent. |
| `domain` | `array` | The default domain to append to a hostname. For example, if the domain is set to `example.com`, a DNS lookup query for `example-host` is rewritten as `example-host.example.com`. |
| `search` | `array` | An array of domain names to append to an unqualified hostname, such as `example-host`, during a DNS lookup query. |

Show more

**Static IP address assignment configuration example**

```
{
  "ipam": {
    "type": "static",
      "addresses": [
        {
          "address": "191.168.1.7/24"
        }
      ]
  }
}
```

##### [3.1.2.2. Dynamic IP address (DHCP) assignment configuration](#nw-multus-dhcp_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

A pod obtains its original DHCP lease when the pod gets created. The lease must be periodically renewed by a minimal DHCP server deployment running on the cluster.

Important

For an Ethernet network attachment, the SR-IOV Network Operator does not create a DHCP server deployment; the Cluster Network Operator is responsible for creating the minimal DHCP server deployment.

To trigger the deployment of the DHCP server, you must create a shim network attachment by editing the Cluster Network Operator configuration, as in the following example:

**Example shim network attachment definition**

```
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  additionalNetworks:
  - name: dhcp-shim
    namespace: default
    type: Raw
    rawCNIConfig: |-
      {
        "name": "dhcp-shim",
        "cniVersion": "0.3.1",
        "type": "bridge",
        "ipam": {
          "type": "dhcp"
        }
      }
  # ...
```

where:

`type`
:   Specifies dynamic IP address assignment for the cluster.

#### [3.1.3. Dynamic IP address assignment configuration with Whereabouts](#nw-multus-whereabouts_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

The Whereabouts CNI plugin helps the dynamic assignment of an IP address to a secondary network without the use of a DHCP server.

The Whereabouts CNI plugin also supports overlapping IP address ranges and configuration of the same CIDR range multiple times within separate `NetworkAttachmentDefinition` CRDs. This provides greater flexibility and management capabilities in multitenant environments.

##### [3.1.3.1. Dynamic IP address configuration parameters](#dynamic-ip-address-assignment-objects_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

The following table describes the configuration objects for dynamic IP address assignment with Whereabouts:

Expand

Table 3.5. ipam whereabouts configuration parameters

| Field | Type | Description |
| --- | --- | --- |
| `type` | `string` | The IPAM address type. The value `whereabouts` is required. |
| `range` | `string` | An IP address and range in CIDR notation. IP addresses are assigned from within this range of addresses. |
| `exclude` | `array` | Optional: A list of zero or more IP addresses and ranges in CIDR notation. IP addresses within an excluded address range are not assigned. |
| `network_name` | `string` | Optional: Helps ensure that each group or domain of pods gets its own set of IP addresses, even if they share the same range of IP addresses. Setting this field is important for keeping networks separate and organized, notably in multitenant environments. |

Show more

##### [3.1.3.2. Dynamic IP address assignment configuration with Whereabouts that excludes IP address ranges](#dynamic-ip-address-assignment-whereabouts_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

The following example shows a dynamic address assignment configuration in a NAD file that uses Whereabouts:

**Whereabouts dynamic IP address assignment that excludes specific IP address ranges**

```
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/27",
    "exclude": [
       "192.0.2.192/30",
       "192.0.2.196/32"
    ]
  }
}
```

##### [3.1.3.3. Dynamic IP address assignment that uses Whereabouts with overlapping IP address ranges](#dynamic-ip-address-assignment-whereabouts-overlapping-ip-ranges_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

The following example shows a dynamic IP address assignment that uses overlapping IP address ranges for multitenant networks.

**NetworkAttachmentDefinition 1**

```
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/29",
    "network_name": "example_net_common",
  }
}
```

where:

`network_name`
:   Optional parameter. If set, must match the `network_name` of `NetworkAttachmentDefinition 2`.

**NetworkAttachmentDefinition 2**

```
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/24",
    "network_name": "example_net_common",
  }
}
```

where:

`network_name`
:   Optional parameter. If set, must match the `network_name` of `NetworkAttachmentDefinition 1`.

### [3.2. Configuring SR-IOV additional network](#nw-sriov-network-attachment_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

You can configure an additional network that uses SR-IOV hardware by creating an `SriovNetwork` object. When you create an `SriovNetwork` object, the SR-IOV Network Operator automatically creates a `NetworkAttachmentDefinition` object.

Note

Do not modify or delete an `SriovNetwork` object if it is attached to any pods in a `running` state.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

**Procedure**

1. Create a `SriovNetwork` object, and then save the YAML in the `<name>.yaml` file, where `<name>` is a name for this additional network. The object specification might resemble the following example:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: attach1
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: net1
     networkNamespace: project2
     ipam: |-
       {
         "type": "host-local",
         "subnet": "10.56.217.0/24",
         "rangeStart": "10.56.217.171",
         "rangeEnd": "10.56.217.181",
         "gateway": "10.56.217.1"
       }
   ```
2. To create the object, enter the following command:

   ```
   $ oc create -f <name>.yaml
   ```

   where:

   `<name>`
   :   Specifies the name of the additional network.
3. Optional: To confirm that the `NetworkAttachmentDefinition` object that is associated with the `SriovNetwork` object that you created in the previous step exists, enter the following command. Replace `<namespace>` with the `networkNamespace` value you specified in the `SriovNetwork` object.

   ```
   $ oc get net-attach-def -n <namespace>
   ```

### [3.3. Assigning an SR-IOV network to a VRF](#cnf-assigning-a-sriov-network-to-a-vrf_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

As a cluster administrator, you can assign an SR-IOV network interface to your VRF domain by using the CNI VRF plugin.

To do this, add the VRF configuration to the optional `metaPlugins` parameter of the `SriovNetwork` resource.

Note

Applications that use VRF instances need to bind to a specific device. The common usage is to use the `SO_BINDTODEVICE` option for a socket. `SO_BINDTODEVICE` binds the socket to a device that is specified in the passed interface name, for example, `eth1`. To use `SO_BINDTODEVICE`, the application must have `CAP_NET_RAW` capabilities.

Using a VRF through the `ip vrf exec` command is not supported in OpenShift Container Platform pods. To use VRF, bind applications directly to the VRF interface.

#### [3.3.1. Creating an additional SR-IOV network attachment with the CNI VRF plugin](#cnf-creating-an-additional-sriov-network-with-vrf-plug-in_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

The SR-IOV Network Operator manages additional network definitions. When you specify an additional SR-IOV network to create, the SR-IOV Network Operator creates the `NetworkAttachmentDefinition` custom resource (CR) automatically.

Note

Do not edit `NetworkAttachmentDefinition` custom resources that the SR-IOV Network Operator manages. Doing so might disrupt network traffic on your additional network.

To create an additional SR-IOV network attachment with the CNI virtual routing and forwarding (VRF) plugin, perform the following procedure.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in to the OpenShift Container Platform cluster as a user with cluster-admin privileges.

**Procedure**

1. Create the `SriovNetwork` custom resource (CR) for the additional SR-IOV network attachment and insert the `metaPlugins` configuration, as in the following example CR. Save the YAML as the file `sriov-network-attachment.yaml`.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: example-network
     namespace: additional-sriov-network-1
   spec:
     ipam: |
       {
         "type": "host-local",
         "subnet": "10.56.217.0/24",
         "rangeStart": "10.56.217.171",
         "rangeEnd": "10.56.217.181",
         "routes": [{
           "dst": "0.0.0.0/0"
         }],
         "gateway": "10.56.217.1"
       }
     vlan: 0
     resourceName: intelnics
     metaPlugins : |
       {
         "type": "vrf",
   ```

   1

   ```
         "vrfname": "example-vrf-name"
       }
   ```

   where:

   `metaPlugins.type`
   :   Set the `type` parameter to `vrf`.

   `metaPlugins.vrfname`
   :   Specify a name for the VRF in the `vrfname` parameter. An interface gets assigned to the VRF. If you do not specify a name for the VRF in a pod, the SR-IOV Network Operator automatically generates a name for the VRF.
2. Create the `SriovNetwork` resource:

   ```
   $ oc create -f sriov-network-attachment.yaml
   ```

**Verification**

1. Confirm that the SR-IOV Network Operator created the `NetworkAttachmentDefinition` CR by running the following command. The expected output shows the name of the NAD CR and the creation age in minutes.

   ```
   $ oc get network-attachment-definitions -n <namespace>
   ```

   * `<namespace>`: Replace `<namespace>` with the namespace that you specified when configuring the network attachment, for example, `additional-sriov-network-1`.

     Note

     There might be a delay before the SR-IOV Network Operator creates the CR.
2. To verify that the VRF CNI is correctly configured and that the additional SR-IOV network attachment is attached, do the following:

   1. Create an SR-IOV network that uses the VRF CNI.
   2. Assign the network to a pod.
   3. Verify that the pod network attachment connects to the SR-IOV additional network. Ensure that you remote shell login into the pod and run the following command. The expected output shows the name of the VRF interface and its unique ID in the routing table.

      ```
      $ ip vrf show
      ```
   4. Confirm that the VRF interface is `master` for the secondary interface by running the following command. Example output shows `5: net1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc noqueue master red state UP mode`.

      ```
      $ ip link
      ```

### [3.4. Runtime configuration for an Ethernet-based SR-IOV attachment](#nw-sriov-runtime-config-ethernet_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

When attaching a pod to an additional network, you can specify a runtime configuration to make specific customizations for the pod. For example, you can request a specific MAC hardware address.

You specify the runtime configuration by setting an annotation in the pod specification. The annotation key is `k8s.v1.cni.cncf.io/networks`, and it accepts a JSON object that describes the runtime configuration.

**Example runtime configuration for an Ethernet-based SR-IOV network attachment**

```
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
  annotations:
    k8s.v1.cni.cncf.io/networks: |-
      [
        {
          "name": "<network_attachment>",
          "mac": "<mac_address>",
          "ips": ["<cidr_range>"]
        }
      ]
spec:
  containers:
  - name: sample-container
    image: <image>
    imagePullPolicy: IfNotPresent
    command: ["sleep", "infinity"]
```

where:

`k8s.v1.cni.cncf.io/networks.name`
:   The name of the SR-IOV network attachment definition CR. Example value is `ibl`.

`k8s.v1.cni.cncf.io/networks.mac`
:   Optional parameter. The MAC address for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. To use this feature, you also must specify `{ "mac": true }` in the `SriovNetwork` object. Example value is `c2:11:22:33:44:55:66:77`.

`k8s.v1.cni.cncf.io/networks.ips`
:   Optional parameter. IP addresses for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this feature, you also must specify `{ "ips": true }` in the `SriovNetwork` object. Example value is `192.168.10.1/24", "2001::1/64`.

### [3.5. Adding a pod to a secondary network](#nw-multus-add-pod_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

To enable a pod to use additional network interfaces in OpenShift Container Platform, you can attach the pod to a secondary network. The pod continues to send normal cluster-related network traffic over the default network.

When a pod is created, a secondary network is attached to the pod. However, if a pod already exists, you cannot attach a secondary network to it.

The pod must be in the same namespace as the secondary network.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in to the cluster.

**Procedure**

1. Add an annotation to the `Pod` object. Only one of the following annotation formats can be used:

   1. To attach a secondary network without any customization, add an annotation with the following format:

      ```
      metadata:
        annotations:
          k8s.v1.cni.cncf.io/networks: <network>[,<network>,...]
      ```

      where:

      `k8s.v1.cni.cncf.io/networks`
      :   Specifies the name of the secondary network to associate with the pod. To specify more than one secondary network, separate each network with a comma. Do not include whitespace between the comma. If you specify the same secondary network multiple times, that pod will have multiple network interfaces attached to that network.
   2. To attach a secondary network with customizations, add an annotation with the following format:

      ```
      metadata:
        annotations:
          k8s.v1.cni.cncf.io/networks: |-
            [
              {
                "name": "<network>",
                "namespace": "<namespace>",
                "default-route": ["<default_route>"]
              }
            ]
      ```

      where:

      `<network>`
      :   Specifies the name of the secondary network defined by a `NetworkAttachmentDefinition` object.

      `<namespace>`
      :   Specifies the namespace where the `NetworkAttachmentDefinition` object is defined.

      `<default-route>`
      :   Optional parameter. Specifies an override for the default route, such as `192.168.17.1`.
2. Create the pod by entering the following command.

   ```
   $ oc create -f <name>.yaml
   ```

   Replace `<name>` with the name of the pod.
3. Optional: Confirm that the annotation exists in the `pod` CR by entering the following command. Replace `<name>` with the name of the pod.

   ```
   $ oc get pod <name> -o yaml
   ```

   In the following example, the `example-pod` pod is attached to the `net1` secondary network:

   ```
   $ oc get pod example-pod -o yaml
   apiVersion: v1
   kind: Pod
   metadata:
     annotations:
       k8s.v1.cni.cncf.io/networks: macvlan-bridge
       k8s.v1.cni.cncf.io/network-status: |-
         [{
             "name": "ovn-kubernetes",
             "interface": "eth0",
             "ips": [
                 "10.128.2.14"
             ],
             "default": true,
             "dns": {}
         },{
             "name": "macvlan-bridge",
             "interface": "net1",
             "ips": [
                 "20.2.2.100"
             ],
             "mac": "22:2f:60:a5:f8:00",
             "dns": {}
         }]
     name: example-pod
     namespace: default
   spec:
     ...
   status:
     ...
   ```

   where:

   `k8s.v1.cni.cncf.io/network-status`
   :   Specifies a JSON array of objects. Each object describes the status of a secondary network attached to the pod. The annotation value is stored as a plain text value.

#### [3.5.1. Exposing MTU for vfio-pci SR-IOV devices to pod](#nw-sriov-expose-mtu_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

After adding a pod to an additional network, you can check that the MTU is available for the SR-IOV network.

**Procedure**

1. Check that the pod annotation includes MTU by running the following command:

   ```
   $ oc describe pod example-pod
   ```

   The following example shows the sample output:

   ```
   "mac": "20:04:0f:f1:88:01",
          "mtu": 1500,
          "dns": {},
          "device-info": {
            "type": "pci",
            "version": "1.1.0",
            "pci": {
              "pci-address": "0000:86:01.3"
       }
     }
   ```
2. Verify that the MTU is available in `/etc/podnetinfo/` inside the pod by running the following command:

   ```
   $ oc exec example-pod -n sriov-tests -- cat /etc/podnetinfo/annotations | grep mtu
   ```

   The following example shows the sample output:

   ```
   k8s.v1.cni.cncf.io/network-status="[{
       \"name\": \"ovn-kubernetes\",
       \"interface\": \"eth0\",
       \"ips\": [
           \"10.131.0.67\"
       ],
       \"mac\": \"0a:58:0a:83:00:43\",
       \"default\": true,
       \"dns\": {}
       },{
       \"name\": \"sriov-tests/sriov-nic-1\",
       \"interface\": \"net1\",
       \"ips\": [
           \"192.168.10.1\"
       ],
       \"mac\": \"20:04:0f:f1:88:01\",
       \"mtu\": 1500,
       \"dns\": {},
       \"device-info\": {
           \"type\": \"pci\",
           \"version\": \"1.1.0\",
           \"pci\": {
               \"pci-address\": \"0000:86:01.3\"
           }
       }
       }]"
   ```

#### [3.5.2. Change the MTU value of a virtual function for a running pod](#nw-sriov-change-vf-mtu-running-pod_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

You can change the maximum transmission unit (MTU) of a virtual function (VF) for a running pod by omitting the `mtu` field from the `SriovNetworkNodePolicy` custom resource (CR) and configuring the physical function (PF) MTU by using the Kubernetes NMState Operator.

When the `mtu` field is set in the `SriovNetworkNodePolicy` CR, the SR-IOV Network Operator continuously enforces that MTU value on the VF. This reverts any application-level MTU changes and can trigger a node drain. To avoid this conflict, use the following approach:

* Omit the `mtu` field from the `SriovNetworkNodePolicy` CR. This allows the SR-IOV Network Operator to provision VFs without managing their MTU.
* Use the Kubernetes NMState Operator to set the MTU of the PF to the required value. A VF cannot have a higher MTU than its parent PF, so you must set the PF MTU first.

With these configurations in place, a pod that has the `NET_ADMIN` Linux capability can safely set its own VF MTU without interference from the SR-IOV Network Operator.

Important

If you already configured a value for the `mtu` field in your `SriovNetworkNodePolicy` CR, removing it might trigger a node drain. Perform this change during a scheduled maintenance window.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You logged in as a user with `cluster-admin` privileges.
* You installed the SR-IOV Network Operator.
* You installed the Kubernetes NMState Operator.

**Procedure**

1. Verify that the `mtu` field is not present in your `SriovNetworkNodePolicy` CR by running the following command:

   ```
   $ oc get sriovnetworknodepolicy <policy_name> -n openshift-sriov-network-operator -o jsonpath='{.spec.mtu}'
   ```

   where:

   `<policy_name>`
   :   Specifies the name of the `SriovNetworkNodePolicy` CR.

       If the command returns a value, remove the `mtu` field from the CR by running the following command:

       ```
       $ oc patch sriovnetworknodepolicy <policy_name> -n openshift-sriov-network-operator \
         --type=json -p='[{"op": "remove", "path": "/spec/mtu"}]'
       ```

       The SR-IOV Network Operator reconciles and creates the VFs with the default MTU of 1500.
2. Verify that the VFs are created with the default MTU by running the following commands:

   ```
   $ oc debug node/<node_name>
   ```

   ```
   # chroot /host
   # ip link show <vf_interface>
   ```

   where:

   `<node_name>`
   :   Specifies the name of the node where the PF is located.

   `<vf_interface>`
   :   Specifies the VF interface name, for example `ens3f0v0`.

       **Example output**

       ```
       4: ens3f0v0: <BROADCAST,MULTICAST> mtu 1500 qdisc noop state DOWN mode DEFAULT group default qlen 1000
           link/ether aa:bb:cc:dd:ee:01 brd ff:ff:ff:ff:ff:ff
       ```
3. Create a `NodeNetworkConfigurationPolicy` CR to set the MTU of the PF:

   1. Create a file named `nncp-set-pf-mtu.yaml` with the following content:

      ```
      apiVersion: nmstate.io/v1
      kind: NodeNetworkConfigurationPolicy
      metadata:
        name: set-pf-mtu
      spec:
        nodeSelector:
          kubernetes.io/hostname: <node_name>
        desiredState:
          interfaces:
            - name: <pf_interface>
              type: ethernet
              state: up
              mtu: <mtu_value>
      ```

      where:

      `<node_name>`
      :   Specifies the name of the node where the PF is located.

      `<pf_interface>`
      :   Specifies the name of the PF interface, for example `ens3f0`.

      `<mtu_value>`
      :   Specifies the required MTU value for the PF, for example `9000`. This value must be greater than or equal to the MTU that the application sets on the VF.
   2. Apply the CR by running the following command:

      ```
      $ oc apply -f nncp-set-pf-mtu.yaml
      ```
4. Verify that the NMState policy has been applied successfully by running the following command:

   ```
   $ oc get nodenetworkconfigurationpolicy set-pf-mtu
   ```

   **Example output**

   ```
   NAME          STATUS      REASON
   set-pf-mtu    Available   SuccessfullyConfigured
   ```

   Wait until the `STATUS` column shows `Available` before proceeding.
5. Verify that the PF MTU has been updated on the node by running the following commands:

   ```
   $ oc debug node/<node_name>
   ```

   ```
   # chroot /host
   # ip link show <pf_interface>
   ```

   where:

   `<node_name>`
   :   Specifies the name of the node where the PF is located.

   `<pf_interface>`
   :   Specifies the name of the PF interface, for example `ens3f0`.

       **Example output**

       ```
       2: ens3f0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc mq state UP mode DEFAULT group default qlen 1000
           link/ether aa:bb:cc:dd:ee:ff brd ff:ff:ff:ff:ff:ff
       ```

       The VFs retain their default MTU of 1500 at this stage.
6. Deploy or update the application pod to set the VF MTU at container startup:

   1. Create or update the pod spec with a startup command that sets the VF MTU before the application starts:

      ```
      apiVersion: v1
      kind: Pod
      metadata:
        name: <pod_name>
        namespace: <namespace>
        annotations:
          k8s.v1.cni.cncf.io/networks: <sriov_network_name>
      spec:
        containers:
          - name: <container_name>
            image: <image>
            command: ["/bin/sh"]
            args:
              - "-c"
              - "ip link set mtu <mtu_value> dev <vf_interface>; <application_command>"
            securityContext:
              capabilities:
                add: ["NET_ADMIN"]
            resources:
              requests:
                <sriov_resource_name>: "1"
              limits:
                <sriov_resource_name>: "1"
      ```

      where:

      `command` and `args`
      :   Sets the VF MTU to the specified value before running the application command.

      `NET_ADMIN`
      :   The `NET_ADMIN` Linux capability is required for the container to change network interface settings.

      `<pod_name>`
      :   Specifies the name of the pod.

      `<namespace>`
      :   Specifies the namespace where the pod runs.

      `<sriov_network_name>`
      :   Specifies the name of the `SriovNetwork` CR that provides the VF to the pod.

      `<container_name>`
      :   Specifies the name of the container.

      `<image>`
      :   Specifies the container image to use.

      `<mtu_value>`
      :   Specifies the required MTU value, for example `9000`.

      `<vf_interface>`
      :   Specifies the VF interface name as it is displayed inside the pod, typically `net1`.

      `<application_command>`
      :   Specifies the main application command to run after the MTU is set.

      `<sriov_resource_name>`
      :   Specifies the SR-IOV resource name defined in the `spec.resourceName` field of the `SriovNetworkNodePolicy` CR.
   2. Apply the pod spec by running the following command:

      ```
      $ oc apply -f <pod_spec_file>.yaml
      ```

      where:

      `<pod_spec_file>`
      :   Specifies the name of the file containing the pod specification.

**Verification**

1. Verify that the VF MTU inside the pod has been set to the expected value by running the following command:

   ```
   $ oc exec <pod_name> -n <namespace> -- ip link show <vf_interface>
   ```

   where:

   `<pod_name>`
   :   Specifies the name of the pod.

   `<namespace>`
   :   Specifies the namespace where the pod is running.

   `<vf_interface>`
   :   Specifies the VF interface name inside the pod, for example `net1`.

       **Example output**

       ```
       3: net1: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 9000 qdisc mq state UP mode DEFAULT group default qlen 1000
           link/ether 00:00:5E:00:53:01 brd ff:ff:ff:ff:ff:ff
       ```

       The example output confirms that the VF MTU matches the value set by the pod startup command. The SR-IOV Network Operator preserves this value because the `SriovNetworkNodePolicy` CR delegates MTU management to the pod.

### [3.6. Configuring parallel node draining during SR-IOV network policy updates](#configure-sr-iov-operator-parallel-nodes_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

By default, the SR-IOV Network Operator drains workloads from a node before every policy change. The Operator performs this action, one node at a time, to ensure that the reconfiguration does not impact workloads.

In large clusters, draining nodes sequentially can be time-consuming, taking hours or even days. In time-sensitive environments, you can enable parallel node draining in an `SriovNetworkPoolConfig` custom resource (CR) for faster rollouts of SR-IOV network configurations.

To configure parallel draining, use the `SriovNetworkPoolConfig` CR to create a node pool. You can then add nodes to the pool and define the maximum number of nodes in the pool that the Operator can drain in parallel. With this approach, you can enable parallel draining for faster reconfiguration while ensuring you still have enough nodes remaining in the pool to handle any running workloads.

Note

A node can only belong to one SR-IOV network pool configuration. If a node is not part of a pool, the node gets added to a virtual, default, pool that with a configuration for draining one node at a time only.

The node might restart during the draining process.

The procedure requires that you create SR-IOV resources and then parallel drain the nodes.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.
* Install the SR-IOV Network Operator.
* Nodes have hardware that support SR-IOV.

**Procedure**

1. Create a YAML file that defines the `SriovNetworkPoolConfig` resource:

   **Example `sriov-nw-pool.yaml` file**

   ```
   apiVersion: v1
   kind: SriovNetworkPoolConfig
   metadata:
     name: pool-1
     namespace: openshift-sriov-network-operator
   spec:
     maxUnavailable: 2
     nodeSelector:
       matchLabels:
         node-role.kubernetes.io/worker: ""
   ```

   where:

   `name`
   :   Specify the name of the `SriovNetworkPoolConfig` object.

   `namespace`
   :   Specify namespace where the SR-IOV Network Operator is installed.

   `maxUnavailable`
   :   Specify an integer number, or percentage value, for nodes that can be unavailable in the pool during an update. For example, if you have 10 nodes and you set the maximum unavailable to 2, then only 2 nodes can be drained in parallel at any time, leaving 8 nodes for handling workloads.

   `nodeSelector`
   :   Specify the nodes to add the pool by using the node selector. This example adds all nodes with the `worker` role to the pool.
2. Create the `SriovNetworkPoolConfig` resource by running the following command:

   ```
   $ oc create -f sriov-nw-pool.yaml
   ```
3. Create the `sriov-test` namespace by running the following command:

   ```
   $ oc create namespace sriov-test
   ```
4. Create a YAML file that defines the `SriovNetworkNodePolicy` resource, as demonstrated in the following example YAML file:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: sriov-nic-1
     namespace: openshift-sriov-network-operator
   spec:
     deviceType: netdevice
     nicSelector:
       pfNames: ["ens1"]
     nodeSelector:
       node-role.kubernetes.io/worker: ""
     numVfs: 5
     priority: 99
     resourceName: sriov_nic_1
   ```
5. Create the `SriovNetworkNodePolicy` resource by running the following command:

   ```
   $ oc create -f sriov-node-policy.yaml
   ```
6. Create a YAML file that defines the `SriovNetwork` resource:

   **Example `sriov-network.yaml` file**

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: sriov-nic-1
     namespace: openshift-sriov-network-operator
   spec:
     linkState: auto
     networkNamespace: sriov-test
     resourceName: sriov_nic_1
     capabilities: '{ "mac": true, "ips": true }'
     ipam: '{ "type": "static" }'
   ```
7. Create the `SriovNetwork` resource by running the following command:

   ```
   $ oc create -f sriov-network.yaml
   ```
8. View the node pool you created by running the following command:

   ```
   $ oc get sriovNetworkpoolConfig -n openshift-sriov-network-operator
   ```

   Expected output shows the name of the node pool, such as `pool-1`, that includes all the node that have the `worker` role and the age of the node pool in seconds, such as `67s`.
9. Update the number of virtual functions in the `SriovNetworkNodePolicy` resource to trigger workload draining in the cluster:

   ```
   $ oc patch SriovNetworkNodePolicy sriov-nic-1 -n openshift-sriov-network-operator --type merge -p '{"spec": {"numVfs": 4}}'
   ```
10. Check the draining status on the target cluster by running the following command:

    ```
    $ oc get sriovNetworkNodeState -n openshift-sriov-network-operator
    ```

    **Example output**

    ```
    NAMESPACE                          NAME       SYNC STATUS   DESIRED SYNC STATE   CURRENT SYNC STATE   AGE
    openshift-sriov-network-operator   worker-0   InProgress    Drain_Required       DrainComplete        3d10h
    openshift-sriov-network-operator   worker-1   InProgress    Drain_Required       DrainComplete        3d10h
    ```

    When the draining process completes, the `SYNC STATUS` changes to `Succeeded`, and the `DESIRED SYNC STATE` and `CURRENT SYNC STATE` values return to `IDLE`.

### [3.7. Excluding the SR-IOV network topology for NUMA-aware scheduling](#nw-sriov-configure-exclude-topology-manager_configuring-sriov-net-attach) Copy linkLink copied to clipboard!

To exclude advertising the SR-IOV network resource’s Non-Uniform Memory Access (NUMA) node to the Topology Manager, you can configure the `excludeTopology` specification in the `SriovNetworkNodePolicy` custom resource. Use this configuration for more flexible SR-IOV network deployments during NUMA-aware pod scheduling.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have configured the CPU Manager policy to `static`. For more information about CPU Manager, see the *Additional resources* section.
* You have configured the Topology Manager policy to `single-numa-node`.
* You have installed the SR-IOV Network Operator.

**Procedure**

1. Create the `SriovNetworkNodePolicy` CR:

   1. Save the following YAML in the `sriov-network-node-policy.yaml` file, replacing values in the YAML to match your environment:

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetworkNodePolicy
      metadata:
        name: <policy_name>
        namespace: openshift-sriov-network-operator
      spec:
        resourceName: sriovnuma0
        nodeSelector:
          kubernetes.io/hostname: <node_name>
        numVfs: <number_of_Vfs>
        nicSelector:
          vendor: "<vendor_ID>"
          deviceID: "<device_ID>"
        deviceType: netdevice
        excludeTopology: true
      ```

      `spec.resourceName`
      :   Specifies the resource name of the SR-IOV network device plugin. This YAML uses a sample `resourceName` value.

      `spec.nicSelector`
      :   Identifies the device for the Operator to configure by using the network interface controller (NIC selector).

      `spec.excludeTopology`
      :   Excludes advertising the NUMA node for the SR-IOV network resource to the Topology Manager. Set the value to `true`. The default value is `false`.

      Note

      If many `SriovNetworkNodePolicy` resources target the same SR-IOV network resource, the `SriovNetworkNodePolicy` resources must have the same value as the `excludeTopology` specification. Otherwise, the conflicting policy is rejected.
   2. Create the `SriovNetworkNodePolicy` resource by running the following command. Successful output lists the name of the `SriovNetworkNodePolicy` resource and the `created` status.

      ```
      $ oc create -f sriov-network-node-policy.yaml
      ```
2. Create the `SriovNetwork` CR:

   1. Save the following YAML in the `sriov-network.yaml` file, replacing values in the YAML to match your environment:

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetwork
      metadata:
        name: <sriov_network_name>
        namespace: openshift-sriov-network-operator
      spec:
        resourceName: sriovnuma0
        networkNamespace: <namespace>
        ipam: |-
          {
            "type": "<ipam_type>",
          }
      ```

      `metadata.name`
      :   Specifies the name for the SR-IOV network resource.

      `spec.resourceName`
      :   Specifies the resource name for the `SriovNetworkNodePolicy` CR from the earlier step. This YAML uses a sample `resourceName` value.

      `spec.networkNamespace`
      :   Specifies the namespace for your SR-IOV network resource.

      `spec.ipam`
      :   Specifies the IP address management configuration for the SR-IOV network.
   2. Create the `SriovNetwork` resource by running the following command. Successful output lists the name of the `SriovNetwork` resource and the `created` status.

      ```
      $ oc create -f sriov-network.yaml
      ```
3. Create a pod and assign the SR-IOV network resource from the previous step:

   1. Save the following YAML in the `sriov-network-pod.yaml` file, replacing values in the YAML to match your environment:

      ```
      apiVersion: v1
      kind: Pod
      metadata:
        name: <pod_name>
        annotations:
          k8s.v1.cni.cncf.io/networks: |-
            [
              {
                "name": "<sriov_network_name>",
              }
            ]
      spec:
        containers:
        - name: <container_name>
          image: <image>
          imagePullPolicy: IfNotPresent
          command: ["sleep", "infinity"]
      ```

      `metadata.annotations."k8s.v1.cni.cncf.io/networks"`
      :   Specifies the name of the `SriovNetwork` resource that uses the `SriovNetworkNodePolicy` resource.
   2. Create the `Pod` resource by running the following command. The expected output shows the name of the `Pod` resource and the `created` status.

      ```
      $ oc create -f sriov-network-pod.yaml
      ```

**Verification**

1. Verify the status of the pod by running the following command, replacing `<pod_name>` with the name of the pod:

   ```
   $ oc get pod <pod_name>
   ```

   The following is example output:

   ```
   NAME                                     READY   STATUS    RESTARTS   AGE
   test-deployment-sriov-76cbbf4756-k9v72   1/1     Running   0          45h
   ```
2. Open a debug session with the target pod to verify that the SR-IOV network resources are deployed to a different node than the memory and CPU resources.

   1. Open a debug session with the pod by running the following command, replacing <pod\_name> with the target pod name.

      ```
      $ oc debug pod/<pod_name>
      ```
   2. Set `/host` as the root directory within the debug shell. The debug pod mounts the root file system from the host in `/host` within the pod. By changing the root directory to `/host`, you can run binaries from the host file system:

      ```
      $ chroot /host
      ```
   3. View information about the CPU allocation by running the following commands:

      ```
      $ lscpu | grep NUMA
      ```

      The following is example output:

      ```
      NUMA node(s):                    2
      NUMA node0 CPU(s):     0,2,4,6,8,10,12,14,16,18,...
      NUMA node1 CPU(s):     1,3,5,7,9,11,13,15,17,19,...
      ```

      ```
      $ cat /proc/self/status | grep Cpus
      ```

      The following is example output:

      ```
      Cpus_allowed:	ffff
      Cpus_allowed_list:	1,3,5,7
      ```

      The expected output shows the CPUs (1, 3, 5, and 7) that get allocated to a `NUMA` node, such as `NUMA node1`. The SR-IOV network resource can use the NIC from another `NUMA` node, such as `NUMA node0`. Note that the `ffff` hexadecimal value represents the CPU cores that run a process.

      ```
      $ cat  /sys/class/net/net1/device/numa_node
      ```

      Expected output shows the number for the `NUMA` node, such as `0`.

      Note

      If you set the `excludeTopology` specification to `True`, the required resources might exist in the same NUMA node.

## [Chapter 4. Configuring an SR-IOV InfiniBand network attachment](#configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

You can configure an InfiniBand (IB) network attachment for an Single Root I/O Virtualization (SR-IOV) device in the cluster.

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

### [4.1. InfiniBand device configuration object](#nw-sriov-ibnetwork-object_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

You can configure an InfiniBand (IB) network device by defining an `SriovIBNetwork` object.

The following YAML describes an `SriovIBNetwork` object:

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovIBNetwork
metadata:
  name: <name>
  namespace: openshift-sriov-network-operator
spec:
  resourceName: <sriov_resource_name>
  networkNamespace: <target_namespace>
  ipam: |-
    {}
  linkState: <link_state>
  capabilities: <capabilities>
```

where:

`name`
:   A name for the object. The SR-IOV Network Operator creates a `NetworkAttachmentDefinition` object with same name.

`namespace`
:   The namespace where the SR-IOV Operator is installed.

`resourceName`
:   The value for the `spec.resourceName` parameter from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network.

`networkNamespace`
:   The target namespace for the `SriovIBNetwork` object. Only pods in the target namespace can attach to the network device.

`ipam`
:   Optional parameter. A configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.

`linkState`
:   Optional parameter. The link state of virtual function (VF). Allowed values are `enable`, `disable` and `auto`.

`capabilities`
:   Optional parameter. The capabilities to configure for this network. You can specify `'{ "ips": true }'` to enable IP address support or `'{ "infinibandGUID": true }'` to enable IB Global Unique Identifier (GUID) support.

#### [4.1.1. Creating a configuration for assignment of dual-stack IP addresses dynamically](#nw-multus-configure-dualstack-ip-address_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

You can dynamically assign dual-stack IP addresses to a secondary network so that pods can communicate over both IPv4 and IPv6 addresses.

You can configure the following IP address assignment types in the `ipRanges` parameter:

* IPv4 addresses
* IPv6 addresses
* multiple IP address assignment

**Procedure**

1. Set `type` to `whereabouts`.
2. Use `ipRanges` to allocate IP addresses as shown in the following example:

   ```
   cniVersion: operator.openshift.io/v1
   kind: Network
   metadata:
     name: cluster
   spec:
     additionalNetworks:
     - name: whereabouts-shim
       namespace: default
       type: Raw
       rawCNIConfig: |-
         {
          "name": "whereabouts-dual-stack",
          "cniVersion": "0.3.1,
          "type": "bridge",
          "ipam": {
            "type": "whereabouts",
            "ipRanges": [
                     {"range": "192.168.10.0/24"},
                     {"range": "2001:db8::/64"}
                 ]
          }
         }
   ```
3. Attach the secondary network to a pod. For more information, see "Adding a pod to a secondary network".

**Verification**

* Verify that all IP addresses got assigned to the network interfaces within the network namespace of a pod by entering the following command:

  ```
  $ oc exec -it <pod_name> -- ip a
  ```

  where:

  `<pod_name>`
  :   The name of the pod.

#### [4.1.2. Configuration of IP address assignment for a network attachment](#nw-multus-ipam-object_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

For secondary networks, you can assign IP addresses by using an IP Address Management (IPAM) CNI plugin, which supports various assignment methods, including Dynamic Host Configuration Protocol (DHCP) and static assignment.

The DHCP IPAM CNI plugin responsible for dynamic assignment of IP addresses operates with two distinct components:

* CNI Plugin: Responsible for integrating with the Kubernetes networking stack to request and release IP addresses.
* DHCP IPAM CNI Daemon: A listener for DHCP events that coordinates with existing DHCP servers in the environment to handle IP address assignment requests. This daemon is not a DHCP server itself.

For networks requiring `type: dhcp` in their IPAM configuration, ensure the DHCP server meets the following conditions:

* A DHCP server is available and running in the environment.
* The DHCP server is external to the cluster and you expect the server to form part of the existing network infrastructure for the customer.
* The DHCP server is appropriately configured to serve IP addresses to the nodes.

In cases where a DHCP server is unavailable in the environment, consider using the Whereabouts IPAM CNI plugin. The Whereabouts CNI provides similar IP address management capabilities without the need for an external DHCP server.

Note

Use the Whereabouts CNI plugin when no external DHCP server exists or where static IP address management is preferred. The Whereabouts plugin includes a reconciler daemon to manage stale IP address allocations.

Ensure the periodic renewal of a DHCP lease throughout the lifetime of a container by including a separate daemon, the DHCP IPAM CNI Daemon. To deploy the DHCP IPAM CNI daemon, change the Cluster Network Operator (CNO) configuration to trigger the deployment of this daemon as part of the secondary network setup.

##### [4.1.2.1. Static IP address assignment configuration](#nw-multus-static_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

The following table describes the configuration for static IP address assignment:

Expand

Table 4.1. ipam static configuration object

| Field | Type | Description |
| --- | --- | --- |
| `type` | `string` | The IPAM address type. The value `static` is required. |
| `addresses` | `array` | An array of objects specifying IP addresses to assign to the virtual interface. Both IPv4 and IPv6 IP addresses are supported. |
| `routes` | `array` | An array of objects specifying routes to configure inside the pod. |
| `dns` | `array` | Optional: An array of objects specifying the DNS configuration. |

Show more

The `addresses` array requires objects with the following fields:

Expand

Table 4.2. ipam.addresses[] array

| Field | Type | Description |
| --- | --- | --- |
| `address` | `string` | An IP address and network prefix that you specify. For example, if you specify `10.10.21.10/24`, the secondary network gets assigned an IP address of `10.10.21.10` and the subnet mask of `255.255.255.0`. |
| `gateway` | `string` | The default gateway to route egress network traffic to. |

Show more

Expand

Table 4.3. ipam.routes[] array

| Field | Type | Description |
| --- | --- | --- |
| `dst` | `string` | The IP address range in CIDR format, such as `192.168.17.0/24` or `0.0.0.0/0` for the default route. |
| `gw` | `string` | The gateway that routes network traffic. |

Show more

Expand

Table 4.4. ipam.dns object

| Field | Type | Description |
| --- | --- | --- |
| `nameservers` | `array` | An array of one or more IP addresses where DNS queries get sent. |
| `domain` | `array` | The default domain to append to a hostname. For example, if the domain is set to `example.com`, a DNS lookup query for `example-host` is rewritten as `example-host.example.com`. |
| `search` | `array` | An array of domain names to append to an unqualified hostname, such as `example-host`, during a DNS lookup query. |

Show more

**Static IP address assignment configuration example**

```
{
  "ipam": {
    "type": "static",
      "addresses": [
        {
          "address": "191.168.1.7/24"
        }
      ]
  }
}
```

##### [4.1.2.2. Dynamic IP address (DHCP) assignment configuration](#nw-multus-dhcp_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

A pod obtains its original DHCP lease when the pod gets created. The lease must be periodically renewed by a minimal DHCP server deployment running on the cluster.

Important

For an Ethernet network attachment, the SR-IOV Network Operator does not create a DHCP server deployment; the Cluster Network Operator is responsible for creating the minimal DHCP server deployment.

To trigger the deployment of the DHCP server, you must create a shim network attachment by editing the Cluster Network Operator configuration, as in the following example:

**Example shim network attachment definition**

```
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  additionalNetworks:
  - name: dhcp-shim
    namespace: default
    type: Raw
    rawCNIConfig: |-
      {
        "name": "dhcp-shim",
        "cniVersion": "0.3.1",
        "type": "bridge",
        "ipam": {
          "type": "dhcp"
        }
      }
  # ...
```

where:

`type`
:   Specifies dynamic IP address assignment for the cluster.

#### [4.1.3. Dynamic IP address assignment configuration with Whereabouts](#nw-multus-whereabouts_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

The Whereabouts CNI plugin helps the dynamic assignment of an IP address to a secondary network without the use of a DHCP server.

The Whereabouts CNI plugin also supports overlapping IP address ranges and configuration of the same CIDR range multiple times within separate `NetworkAttachmentDefinition` CRDs. This provides greater flexibility and management capabilities in multitenant environments.

##### [4.1.3.1. Dynamic IP address configuration parameters](#dynamic-ip-address-assignment-objects_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

The following table describes the configuration objects for dynamic IP address assignment with Whereabouts:

Expand

Table 4.5. ipam whereabouts configuration parameters

| Field | Type | Description |
| --- | --- | --- |
| `type` | `string` | The IPAM address type. The value `whereabouts` is required. |
| `range` | `string` | An IP address and range in CIDR notation. IP addresses are assigned from within this range of addresses. |
| `exclude` | `array` | Optional: A list of zero or more IP addresses and ranges in CIDR notation. IP addresses within an excluded address range are not assigned. |
| `network_name` | `string` | Optional: Helps ensure that each group or domain of pods gets its own set of IP addresses, even if they share the same range of IP addresses. Setting this field is important for keeping networks separate and organized, notably in multitenant environments. |

Show more

##### [4.1.3.2. Dynamic IP address assignment configuration with Whereabouts that excludes IP address ranges](#dynamic-ip-address-assignment-whereabouts_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

The following example shows a dynamic address assignment configuration in a NAD file that uses Whereabouts:

**Whereabouts dynamic IP address assignment that excludes specific IP address ranges**

```
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/27",
    "exclude": [
       "192.0.2.192/30",
       "192.0.2.196/32"
    ]
  }
}
```

##### [4.1.3.3. Dynamic IP address assignment that uses Whereabouts with overlapping IP address ranges](#dynamic-ip-address-assignment-whereabouts-overlapping-ip-ranges_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

The following example shows a dynamic IP address assignment that uses overlapping IP address ranges for multitenant networks.

**NetworkAttachmentDefinition 1**

```
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/29",
    "network_name": "example_net_common",
  }
}
```

where:

`network_name`
:   Optional parameter. If set, must match the `network_name` of `NetworkAttachmentDefinition 2`.

**NetworkAttachmentDefinition 2**

```
{
  "ipam": {
    "type": "whereabouts",
    "range": "192.0.2.192/24",
    "network_name": "example_net_common",
  }
}
```

where:

`network_name`
:   Optional parameter. If set, must match the `network_name` of `NetworkAttachmentDefinition 1`.

### [4.2. Configuring SR-IOV additional network](#nw-sriov-network-attachment_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

You can configure an additional network that uses SR-IOV hardware by creating an `SriovIBNetwork` object. When you create an `SriovIBNetwork` object, the SR-IOV Network Operator automatically creates a `NetworkAttachmentDefinition` object.

Note

Do not modify or delete an `SriovIBNetwork` object if it is attached to any pods in a `running` state.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.

**Procedure**

1. Create a `SriovIBNetwork` object, and then save the YAML in the `<name>.yaml` file, where `<name>` is a name for this additional network. The object specification might resemble the following example:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovIBNetwork
   metadata:
     name: attach1
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: net1
     networkNamespace: project2
     ipam: |-
       {
         "type": "host-local",
         "subnet": "10.56.217.0/24",
         "rangeStart": "10.56.217.171",
         "rangeEnd": "10.56.217.181",
         "gateway": "10.56.217.1"
       }
   ```
2. To create the object, enter the following command:

   ```
   $ oc create -f <name>.yaml
   ```

   where:

   `<name>`
   :   Specifies the name of the additional network.
3. Optional: To confirm that the `NetworkAttachmentDefinition` object that is associated with the `SriovIBNetwork` object that you created in the previous step exists, enter the following command. Replace `<namespace>` with the `networkNamespace` value you specified in the `SriovIBNetwork` object.

   ```
   $ oc get net-attach-def -n <namespace>
   ```

### [4.3. Runtime configuration for an InfiniBand-based SR-IOV attachment](#nw-sriov-runtime-config-sriov-ib_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

When attaching a pod to an additional network, you can specify a runtime configuration to make specific customizations for the pod. For example, you can request a specific MAC hardware address.

You specify the runtime configuration by setting an annotation in the pod specification. The annotation key is `k8s.v1.cni.cncf.io/networks`, and it accepts a JSON object that describes the runtime configuration.

The following JSON describes the runtime configuration options for an InfiniBand-based SR-IOV network attachment.

```
[
  {
    "name": "<network_attachment>",
    "infiniband-guid": "<guid>",
    "ips": ["<cidr_range>"]
  }
]
```

where:

`name`
:   The name of the SR-IOV network attachment definition CR.

`infiniband-guid`
:   The InfiniBand GUID for the SR-IOV device. To use this feature, you also must specify `{ "infinibandGUID": true }` in the `SriovIBNetwork` object.

`ips`
:   The IP addresses for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this feature, you also must specify `{ "ips": true }` in the `SriovIBNetwork` object.

```
apiVersion: v1
kind: Pod
metadata:
  name: sample-pod
  annotations:
    k8s.v1.cni.cncf.io/networks: |-
      [
        {
          "name": "ib1",
          "infiniband-guid": "c2:11:22:33:44:55:66:77",
          "ips": ["192.168.10.1/24", "2001::1/64"]
        }
      ]
spec:
  containers:
  - name: sample-container
    image: <image>
    imagePullPolicy: IfNotPresent
    command: ["sleep", "infinity"]
```

### [4.4. Adding a pod to a secondary network](#nw-multus-add-pod_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

To enable a pod to use additional network interfaces in OpenShift Container Platform, you can attach the pod to a secondary network. The pod continues to send normal cluster-related network traffic over the default network.

When a pod is created, a secondary network is attached to the pod. However, if a pod already exists, you cannot attach a secondary network to it.

The pod must be in the same namespace as the secondary network.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in to the cluster.

**Procedure**

1. Add an annotation to the `Pod` object. Only one of the following annotation formats can be used:

   1. To attach a secondary network without any customization, add an annotation with the following format:

      ```
      metadata:
        annotations:
          k8s.v1.cni.cncf.io/networks: <network>[,<network>,...]
      ```

      where:

      `k8s.v1.cni.cncf.io/networks`
      :   Specifies the name of the secondary network to associate with the pod. To specify more than one secondary network, separate each network with a comma. Do not include whitespace between the comma. If you specify the same secondary network multiple times, that pod will have multiple network interfaces attached to that network.
   2. To attach a secondary network with customizations, add an annotation with the following format:

      ```
      metadata:
        annotations:
          k8s.v1.cni.cncf.io/networks: |-
            [
              {
                "name": "<network>",
                "namespace": "<namespace>",
                "default-route": ["<default_route>"]
              }
            ]
      ```

      where:

      `<network>`
      :   Specifies the name of the secondary network defined by a `NetworkAttachmentDefinition` object.

      `<namespace>`
      :   Specifies the namespace where the `NetworkAttachmentDefinition` object is defined.

      `<default-route>`
      :   Optional parameter. Specifies an override for the default route, such as `192.168.17.1`.
2. Create the pod by entering the following command.

   ```
   $ oc create -f <name>.yaml
   ```

   Replace `<name>` with the name of the pod.
3. Optional: Confirm that the annotation exists in the `pod` CR by entering the following command. Replace `<name>` with the name of the pod.

   ```
   $ oc get pod <name> -o yaml
   ```

   In the following example, the `example-pod` pod is attached to the `net1` secondary network:

   ```
   $ oc get pod example-pod -o yaml
   apiVersion: v1
   kind: Pod
   metadata:
     annotations:
       k8s.v1.cni.cncf.io/networks: macvlan-bridge
       k8s.v1.cni.cncf.io/network-status: |-
         [{
             "name": "ovn-kubernetes",
             "interface": "eth0",
             "ips": [
                 "10.128.2.14"
             ],
             "default": true,
             "dns": {}
         },{
             "name": "macvlan-bridge",
             "interface": "net1",
             "ips": [
                 "20.2.2.100"
             ],
             "mac": "22:2f:60:a5:f8:00",
             "dns": {}
         }]
     name: example-pod
     namespace: default
   spec:
     ...
   status:
     ...
   ```

   where:

   `k8s.v1.cni.cncf.io/network-status`
   :   Specifies a JSON array of objects. Each object describes the status of a secondary network attached to the pod. The annotation value is stored as a plain text value.

#### [4.4.1. Exposing MTU for vfio-pci SR-IOV devices to pod](#nw-sriov-expose-mtu_configuring-sriov-ib-attach) Copy linkLink copied to clipboard!

After adding a pod to an additional network, you can check that the MTU is available for the SR-IOV network.

**Procedure**

1. Check that the pod annotation includes MTU by running the following command:

   ```
   $ oc describe pod example-pod
   ```

   The following example shows the sample output:

   ```
   "mac": "20:04:0f:f1:88:01",
          "mtu": 1500,
          "dns": {},
          "device-info": {
            "type": "pci",
            "version": "1.1.0",
            "pci": {
              "pci-address": "0000:86:01.3"
       }
     }
   ```
2. Verify that the MTU is available in `/etc/podnetinfo/` inside the pod by running the following command:

   ```
   $ oc exec example-pod -n sriov-tests -- cat /etc/podnetinfo/annotations | grep mtu
   ```

   The following example shows the sample output:

   ```
   k8s.v1.cni.cncf.io/network-status="[{
       \"name\": \"ovn-kubernetes\",
       \"interface\": \"eth0\",
       \"ips\": [
           \"10.131.0.67\"
       ],
       \"mac\": \"0a:58:0a:83:00:43\",
       \"default\": true,
       \"dns\": {}
       },{
       \"name\": \"sriov-tests/sriov-nic-1\",
       \"interface\": \"net1\",
       \"ips\": [
           \"192.168.10.1\"
       ],
       \"mac\": \"20:04:0f:f1:88:01\",
       \"mtu\": 1500,
       \"dns\": {},
       \"device-info\": {
           \"type\": \"pci\",
           \"version\": \"1.1.0\",
           \"pci\": {
               \"pci-address\": \"0000:86:01.3\"
           }
       }
       }]"
   ```

## [Chapter 5. Configuring namespaced SR-IOV resources](#configuring-namespaced-sriov-resources) Copy linkLink copied to clipboard!

Namespaced SriovNetwork Resources allow application owners to create and manage their own SriovNetwork resources directly within their namespaces, rather than relying on a cluster administrator to do it in a shared operator namespace. This method simplifies permissions, improves security, and provides better separation between applications.

### [5.1. An introduction to namespaced SriovNetwork resources](#introduction-to-namespaced-sriovnetwork-resources_configuring-namespaced-sriov-resources) Copy linkLink copied to clipboard!

SR-IOV networks can be created and managed directly within application namespaces. This capability provides application owners with fine-grained control over network configurations, simplifying their workflow.

This approach offers several key advantages that enhance the user experience:

* Increased Autonomy and Control: Application owners gain direct control over their network configurations, eliminating the need for a cluster administrator to create `SriovNetwork` objects on their behalf.
* Enhanced Security: By allowing users to manage resources within their own namespaces, the feature improves security and provides better separation between applications. This also helps avoid the unintentional incorrect configuration of other applications' NetworkAttachmentDefinition objects.
* Simplified Permissions: Managing `SriovNetwork` resources directly in their own namespaces simplifies user permissions. This streamlines the workflow and reduces the operational burden for developers.

#### [5.1.1. Configuring SriovNetwork in application namespaces](#nw-configuring-sriov-in-app-namespace_configuring-namespaced-sriov-resources) Copy linkLink copied to clipboard!

When an SriovNetwork custom resource (CR) is deployed in an application namespace, do not define or populate the `spec.networkNamespace` field. In this scenario, the NetworkAttachmentDefinition will be created in the same namespace as the SriovNetwork CR.

The SR-IOV Network Operator webhook rejects the creation of an `SriovNetwork` resource in an application namespace if the `spec.networkNamespace` field is defined.

Follow this procedure to create an `SriovNetwork` resource in an application namespace and attach a pod to the additional network.

**Prerequisites**

The following steps must be completed by a cluster administrator before an application owner can configure a namespaced SriovNetwork resource:

* The SR-IOV Network Operator is installed in the `openshift-sriov-network-operator` namespace.
* Nodes with SR-IOV hardware are labeled for the operator to identify the nodes.

As an application owner you need to have administrator privileges on the application namespace.

**Procedure**

1. Specify the SR-IOV network device configuration for a node by creating an SR-IOV network node policy. The `SriovNetworkNodePolicy` object is created in the `openshift-sriov-network-operator` namespace to define the SR-IOV network device configuration for nodes. Example configuration for Intel DPK is as follows:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: intel-dpdk-node-policy
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: intelnics
     nodeSelector:
       feature.node.kubernetes.io/network-sriov.capable: "true"
     priority: 10
     numVfs: 4
     nicSelector:
       vendor: "8086"
       deviceID: "158b"
       pfNames: [""]
     deviceType: netdevice
   ```
2. Create an application namespace. For example, create a namespace named `sriov-app` by running the following command:

   ```
   $ cat <<EOF | oc create -f -
   apiVersion: v1
   kind: Namespace
   metadata:
       name: sriov-app
   EOF
   ```
3. Create a YAML file, for example, `sriovnetwork.yaml`, to define the `SriovNetwork` object in the application namespace.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: test-network
     namespace: sriov-app
   spec:
     resourceName: intelnics
     ipam:
       type: host-local
       subnet: "10.0.0.0/24"
       routes:
         - dst: "0.0.0.0/0"
           gw: "10.0.0.1"
     vlan: 10
   ```

   * `namespace`: The value must match the name of the application namespace, for example, `sriov-app`.
   * `resourceName`: This value must match the `spec.resourceName` defined in the `SriovNetworkNodePolicy` created by the cluster administrator, which in the example is `intelnics`.
4. Apply the YAML file to create the `SriovNetwork` object in the application namespace.

   ```
   $ oc create -f sriovnetwork.yaml
   ```

   After an application owner has created the SriovNetwork resource, they can create a pod that uses the newly defined network. You attach a pod to the additional network by adding a specific annotation to the pod’s YAML manifest.
5. Create a YAML file, for example, `test-pod.yaml`, to define a pod that uses the new network attachment:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: test-pod
     namespace: sriov-app
     annotations:
       k8s.v1.cni.cncf.io/networks: test-network
   spec:
     containers:
     - name: test-pod-container
       image: centos/tools
       command: ["/bin/bash", "-c", "sleep 3600"]
   ```

   * `namespace`: The namespace where the pod is created. This must be the same namespace where the `SriovNetwork` object is created.
   * `annotations`: `k8s.v1.cni.cncf.io/networks` specifies the additional network that the pod connects to. The value must match the `metadata.name` of the `SriovNetwork` object.
6. Apply the YAML file to create the pod in the application namespace by running the following command:

   ```
   $ oc create -f test-pod.yaml
   ```

**Verification**

1. Verify that the NetworkAttachmentDefinition has been created in the same namespace by running the following command:

   ```
   $ oc get net-attach-def -n sriov-app
   ```

   Where `sriov-app` is the application namespace where the `SriovNetwork` object is created.

   The following is example output:

   ```
   NAME           AGE
   test-network   2m
   ```
2. Verify the pod is running and get its network status by describing the pod with the following command:

   ```
   $ oc describe pod test-pod -n sriov-app
   ```

   Where `sriov-app` is the application namespace where the pod is created.

   In the output, look for the `k8s.v1.cni.cncf.io/network-status` annotation. This shows the name of the network and the IP assigned to the pod on that interface.
3. Check that the pod has the additional network interface by running the following command:

   ```
   $ oc exec -it test-pod -n sriov-app -- ip a
   ```

   Look for a secondary network interface, for example `net1` or `eth1`, in addition to the default eth0 interface. The `net1` interface should have an IP address from the subnet you defined in the SriovNetwork object, for example `10.0.0.0/24`. This confirms the pod is using the new network attachment definition.

## [Chapter 6. Configuring an RDMA subsystem for SR-IOV](#configuring-sriov-rdma-cni) Copy linkLink copied to clipboard!

Remote Direct Memory Access (RDMA) allows direct memory access between two systems without involving the operating system of either system. You can configure an RDMA Container Network Interface (CNI) on Single Root I/O Virtualization (SR-IOV) to enable high-performance, low-latency communication between containers. When you combine RDMA with SR-IOV, you provide a mechanism to expose hardware counters of Mellanox Ethernet devices for use inside Data Plane Development Kit (DPDK) applications.

### [6.1. Configuring SR-IOV RDMA CNI](#nw-sriov-configuring-sriov-rdma-cni_configuring-sriov-rdma-cni) Copy linkLink copied to clipboard!

Configure an RDMA CNI on SR-IOV.

Note

This procedure applies only to Mellanox devices.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the SR-IOV Network Operator.

**Procedure**

1. Create an `SriovNetworkPoolConfig` CR and save it as `sriov-nw-pool.yaml`, as shown in the following example:

   **Example `SriovNetworkPoolConfig` CR**

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkPoolConfig
   metadata:
     name: worker
     namespace: openshift-sriov-network-operator
   spec:
     maxUnavailable: 1
     nodeSelector:
       matchLabels:
         node-role.kubernetes.io/worker: ""
     rdmaMode: <rdma_mode>
   ```

   `spec.rdmaMode`
   :   Specifies the RDMA network namespace mode. Set to `exclusive`.
2. Create the `SriovNetworkPoolConfig` resource by running the following command:

   ```
   $ oc create -f sriov-nw-pool.yaml
   ```
3. Create an `SriovNetworkNodePolicy` CR and save it as `sriov-node-policy.yaml`, as shown in the following example:

   **Example `SriovNetworkNodePolicy` CR**

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: sriov-nic-pf1
     namespace: openshift-sriov-network-operator
   spec:
     deviceType: netdevice
     isRdma: <is_rdma>
     nicSelector:
       pfNames: ["ens3f0np0"]
     nodeSelector:
       node-role.kubernetes.io/worker: ""
     numVfs: 4
     priority: 99
     resourceName: sriov_nic_pf1
   ```

   `spec.isRdma`
   :   Specifies whether to activate RDMA mode. Set to `true`.
4. Create the `SriovNetworkNodePolicy` resource by running the following command:

   ```
   $ oc create -f sriov-node-policy.yaml
   ```
5. Create an `SriovNetwork` CR and save it as `sriov-network.yaml`, as shown in the following example:

   **Example `SriovNetwork` CR**

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: sriov-nic-pf1
     namespace: openshift-sriov-network-operator
   spec:
     networkNamespace: sriov-tests
     resourceName: sriov_nic_pf1
       ipam: |-
     metaPlugins: |
       {
         "type": "<plugin_type>"
       }
   ```

   `spec.metaPlugins.type`
   :   Specifies the type of meta plugin. Set to `rdma` to create the RDMA plugin.
6. Create the `SriovNetwork` resource by running the following command:

   ```
   $ oc create -f sriov-network.yaml
   ```

**Verification**

1. Create a `Pod` CR and save it as `sriov-test-pod.yaml`, as shown in the following example:

   **Example runtime configuration**

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: sample-pod
     annotations:
       k8s.v1.cni.cncf.io/networks: |-
         [
           {
             "name": "net1",
             "mac": "20:04:0f:f1:88:01",
             "ips": ["192.168.10.1/24", "2001::1/64"]
           }
         ]
   spec:
     containers:
     - name: sample-container
       image: <image>
       imagePullPolicy: IfNotPresent
       command: ["sleep", "infinity"]
   ```
2. Create the test pod by running the following command:

   ```
   $ oc create -f sriov-test-pod.yaml
   ```
3. Log in to the test pod by running the following command:

   ```
   $ oc rsh testpod1 -n sriov-tests
   ```
4. Verify that the path to the `hw-counters` directory exists by running the following command:

   ```
   $ ls /sys/bus/pci/devices/${PCIDEVICE_OPENSHIFT_IO_SRIOV_NIC_PF1}/infiniband/*/ports/1/hw_counters/
   ```

   **Example output**

   ```
   duplicate_request       out_of_buffer req_cqe_flush_error           resp_cqe_flush_error        roce_adp_retrans        roce_slow_restart_trans
   implied_nak_seq_err     out_of_sequence req_remote_access_errors    resp_local_length_error     roce_adp_retrans_to     rx_atomic_requests
   lifespan                packet_seq_err req_remote_invalid_request   resp_remote_access_errors   roce_slow_restart       rx_read_requests
   local_ack_timeout_err  req_cqe_error resp_cqe_error                 rnr_nak_retry_err           roce_slow_restart_cnps  rx_write_requests
   ```

## [Chapter 7. Configuring interface-level network sysctl settings and all-multicast mode for SR-IOV networks](#configuring-interface-level-sysctl-settings-sriov-device) Copy linkLink copied to clipboard!

As a cluster administrator, you can change interface-level network sysctls and several interface attributes such as promiscuous mode, all-multicast mode, MTU, and MAC address by using the tuning Container Network Interface (CNI) meta plugin for a pod connected to a SR-IOV network device.

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

### [7.1. Labeling nodes with an SR-IOV enabled NIC](#nw-labeling-sriov-enabled-nodes_configuring-sysctl-interface-sriov-device) Copy linkLink copied to clipboard!

If you want to enable SR-IOV on only SR-IOV capable nodes there are a couple of ways to do this.

**Procedure**

1. Install the Node Feature Discovery (NFD) Operator. NFD detects the presence of SR-IOV enabled NICs and labels the nodes with `node.alpha.kubernetes-incubator.io/nfd-network-sriov.capable = true`.
2. Examine the `SriovNetworkNodeState` CR for each node. The `interfaces` stanza includes a list of all of the SR-IOV devices discovered by the SR-IOV Network Operator on the worker node. Label each node with `feature.node.kubernetes.io/network-sriov.capable: "true"` by using the following command:

   ```
   $ oc label node <node_name> feature.node.kubernetes.io/network-sriov.capable="true"
   ```

   Note

   You can label the nodes with whatever name you want.

### [7.2. Setting one sysctl flag](#nw-setting-one-sysctl-flag_configuring-sysctl-interface-sriov-device) Copy linkLink copied to clipboard!

You can set interface-level network `sysctl` settings for a pod connected to a SR-IOV network device.

In this example, `net.ipv4.conf.IFNAME.accept_redirects` is set to `1` on the created virtual interfaces.

The `sysctl-tuning-test` is a namespace used in this example.

* Use the following command to create the `sysctl-tuning-test` namespace:

  ```
  $ oc create namespace sysctl-tuning-test
  ```

#### [7.2.1. Setting one sysctl flag on nodes with SR-IOV network devices](#nw-basic-example-setting-one-sysctl-flag-node-policy_configuring-sysctl-interface-sriov-device) Copy linkLink copied to clipboard!

The SR-IOV Network Operator adds the `SriovNetworkNodePolicy.sriovnetwork.openshift.io` custom resource definition (CRD) to OpenShift Container Platform. You can configure an SR-IOV network device by creating a `SriovNetworkNodePolicy` custom resource (CR).

Note

When applying the configuration specified in a `SriovNetworkNodePolicy` object, the SR-IOV Operator might drain and reboot the nodes.

It can take several minutes for a configuration change to apply.

Follow this procedure to create a `SriovNetworkNodePolicy` custom resource (CR).

**Procedure**

1. Create an `SriovNetworkNodePolicy` custom resource (CR). For example, save the following YAML as the file `policyoneflag-sriov-node-network.yaml`:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: policyoneflag
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: policyoneflag
     nodeSelector:
       feature.node.kubernetes.io/network-sriov.capable="true"
     priority: 10
     numVfs: 5
     nicSelector:
       pfNames: ["ens5"]
     deviceType: "netdevice"
     isRdma: false
   ```

   * `<name>` specifies the name for the custom resource object.
   * `<namespace>` specifies the namespace where the SR-IOV Network Operator is installed.
   * `<resourceName>` specifies the resource name of the SR-IOV network device plugin. You can create multiple SR-IOV network node policies for a resource name.
   * `<nodeSelector>` specifies the node selector for the nodes to configure. Only SR-IOV network devices on the selected nodes are configured. The SR-IOV Container Network Interface (CNI) plugin and device plugin are deployed on selected nodes only.
   * `<priority>` is optional. The priority is an integer value between `0` and `99`. A smaller value receives higher priority. For example, a priority of `10` is a higher priority than `99`. The default value is `99`.
   * `<numVfs>` specifies the number of the virtual functions (VFs) to create for the SR-IOV physical network device. For an Intel network interface controller (NIC), the number of VFs cannot be larger than the total VFs supported by the device. For a Mellanox NIC, the number of VFs cannot be larger than `127`.
   * `<nicSelector>` identifies the device for the Operator to configure. You do not have to specify values for all the parameters. It is recommended to identify the network device with enough precision to avoid selecting a device unintentionally. If you specify `rootDevices`, you must also specify a value for `vendor`, `deviceID`, or `pfNames`. If you specify both `pfNames` and `rootDevices` at the same time, ensure that they refer to the same device. If you specify a value for `netFilter`, then you do not need to specify any other parameter because a network ID is unique.
   * `<pfNames>` is optional. An array of one or more physical function (PF) names for the device.
   * `<deviceType>` is optional. The driver type for the virtual functions. The only allowed value is `netdevice`. For a Mellanox NIC to work in DPDK mode on bare-metal nodes, set `isRdma` to `true`.
   * `<isRdma>` is optional. Configures whether to enable remote direct memory access (RDMA) mode. The default value is `false`. If the `isRdma` parameter is set to `true`, you can continue to use the RDMA-enabled VF as a normal network device. A device can be used in either mode. Set `isRdma` to `true` and additionally set `needVhostNet` to `true` to configure a Mellanox NIC for use with Fast Data Path DPDK applications.

   Note

   The `vfio-pci` driver type is not supported.
2. Create the `SriovNetworkNodePolicy` object:

   ```
   $ oc create -f policyoneflag-sriov-node-network.yaml
   ```

   After applying the configuration update, all the pods in `sriov-network-operator` namespace change to the `Running` status.
3. To verify that the SR-IOV network device is configured, enter the following command. Replace `<node_name>` with the name of a node with the SR-IOV network device that you just configured. Expected output shows `Succeeded`.

   ```
   $ oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name> -o jsonpath='{.status.syncStatus}'
   ```

#### [7.2.2. Configuring sysctl on a SR-IOV network](#configuring-sysctl-on-sriov-network_configuring-sysctl-interface-sriov-device) Copy linkLink copied to clipboard!

You can set interface specific `sysctl` settings on virtual interfaces created by SR-IOV by adding the tuning configuration to the optional `metaPlugins` parameter of the `SriovNetwork` resource.

The SR-IOV Network Operator manages additional network definitions. When you specify an additional SR-IOV network to create, the SR-IOV Network Operator creates the `NetworkAttachmentDefinition` custom resource (CR) automatically.

Note

Do not edit `NetworkAttachmentDefinition` custom resources that the SR-IOV Network Operator manages. Doing so might disrupt network traffic on your additional network.

To change the interface-level network `net.ipv4.conf.IFNAME.accept_redirects` `sysctl` settings, create an additional SR-IOV network with the Container Network Interface (CNI) tuning plugin.

**Prerequisites**

* Install the OpenShift Container Platform CLI (oc).
* Log in to the OpenShift Container Platform cluster as a user with cluster-admin privileges.

**Procedure**

1. Create the `SriovNetwork` custom resource (CR) for the additional SR-IOV network attachment and insert the `metaPlugins` configuration, as in the following example CR. Save the YAML as the file `sriov-network-interface-sysctl.yaml`.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: onevalidflag
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: policyoneflag
     networkNamespace: sysctl-tuning-test
     ipam: '{ "type": "static" }'
     capabilities: '{ "mac": true, "ips": true }'
     metaPlugins : |
       {
         "type": "tuning",
         "capabilities":{
           "mac":true
         },
         "sysctl":{
            "net.ipv4.conf.IFNAME.accept_redirects": "1"
         }
       }
   ```

   * `<name>` specifies a name for the object. The SR-IOV Network Operator creates a NetworkAttachmentDefinition object with same name.
   * `<namespace>` specifies the namespace where the SR-IOV Network Operator is installed.
   * `<resourceName>` specifies the value for the `spec.resourceName` parameter from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network.
   * `<networkNamespace>` specifies the target namespace for the `SriovNetwork` object. Only pods in the target namespace can attach to the additional network.
   * `<ipam>` specifies a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.
   * `<capabilities>` specifies optional capabilities for the additional network. You can specify `"{ "ips": true }"` to enable IP address support or `"{ "mac": true }"` to enable MAC address support.
   * `<metaPlugins>` specifies optional additional capabilities for the device. In this use case set the `type` field to `tuning`. Specify the interface-level network `sysctl` you want to set in the `sysctl` field.
2. Create the `SriovNetwork` resource:

   ```
   $ oc create -f sriov-network-interface-sysctl.yaml
   ```

**Verification**

* Confirm that the SR-IOV Network Operator created the `NetworkAttachmentDefinition` CR by running the following command:

  ```
  $ oc get network-attachment-definitions -n <namespace>
  ```

  + Replace `<namespace>` with the value for `networkNamespace` that you specified in the `SriovNetwork` object. For example, `sysctl-tuning-test`. The expected output shows the name of the NAD CRD and the creation age in minutes.

  Note

  There might be a delay before the SR-IOV Network Operator creates the CR.

  1. Create a `Pod` CR. Save the following YAML as the file `examplepod.yaml`:

     ```
     apiVersion: v1
     kind: Pod
     metadata:
       name: tunepod
       namespace: sysctl-tuning-test
       annotations:
         k8s.v1.cni.cncf.io/networks: |-
           [
             {
               "name": "onevalidflag",
               "mac": "0a:56:0a:83:04:0c",
               "ips": ["10.100.100.200/24"]
            }
           ]
     spec:
       containers:
       - name: podexample
         image: centos
         command: ["/bin/bash", "-c", "sleep INF"]
         securityContext:
           runAsUser: 2000
           runAsGroup: 3000
           allowPrivilegeEscalation: false
           capabilities:
             drop: ["ALL"]
       securityContext:
         runAsNonRoot: true
         seccompProfile:
           type: RuntimeDefault
     ```

     + `<name>` specifies the name of the SR-IOV network attachment definition CR.
     + `<mac>` is optional. The MAC address for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. To use this feature, you also must specify `{ "mac": true }` in the SriovNetwork object.
     + `<ips>` is optional. IP addresses for the SR-IOV device that are allocated from the resource type defined in the SR-IOV network attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this feature, you also must specify `{ "ips": true }` in the `SriovNetwork` object.
  2. Create the `Pod` CR:

     ```
     $ oc apply -f examplepod.yaml
     ```
  3. Verify that the pod is created by running the following command:

     ```
     $ oc get pod -n sysctl-tuning-test
     ```

     The following is example output:

     ```
     NAME      READY   STATUS    RESTARTS   AGE
     tunepod   1/1     Running   0          47s
     ```
  4. Log in to the pod by running the following command:

     ```
     $ oc rsh -n sysctl-tuning-test tunepod
     ```
  5. Verify the values of the configured sysctl flag. Find the value `net.ipv4.conf.IFNAME.accept_redirects` by running the following command:

     ```
     $ sysctl net.ipv4.conf.net1.accept_redirects
     ```

### [7.3. Configuring sysctl settings for pods associated with bonded SR-IOV interface flag](#nw-configure-sysctl-settings-flag-bonded_configuring-sysctl-interface-sriov-device) Copy linkLink copied to clipboard!

You can set interface-level network `sysctl` settings for a pod connected to a bonded SR-IOV network device.

In this example, the specific network interface-level `sysctl` settings that can be configured are set on the bonded interface.

The `sysctl-tuning-test` is a namespace used in this example.

* Use the following command to create the `sysctl-tuning-test` namespace:

  ```
  $ oc create namespace sysctl-tuning-test
  ```

#### [7.3.1. Setting all sysctl flag on nodes with bonded SR-IOV network devices](#nw-setting-all-sysctls-flag-node-policy-bonded_configuring-sysctl-interface-sriov-device) Copy linkLink copied to clipboard!

The SR-IOV Network Operator adds the `SriovNetworkNodePolicy.sriovnetwork.openshift.io` custom resource definition (CRD) to OpenShift Container Platform. You can configure an SR-IOV network device by creating a `SriovNetworkNodePolicy` custom resource (CR).

Note

When applying the configuration specified in a SriovNetworkNodePolicy object, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes.

It might take several minutes for a configuration change to apply.

Follow this procedure to create a `SriovNetworkNodePolicy` custom resource (CR).

**Procedure**

1. Create an `SriovNetworkNodePolicy` custom resource (CR). Save the following YAML as the file `policyallflags-sriov-node-network.yaml`. Replace `policyallflags` with the name for the configuration.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: policyallflags
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: policyallflags
     nodeSelector:
       node.alpha.kubernetes-incubator.io/nfd-network-sriov.capable = `true`
     priority: 10
     numVfs: 5
     nicSelector:
       pfNames: ["ens1f0"]
     deviceType: "netdevice"
     isRdma: false
   ```

   * `<name>` specifies the name for the custom resource object.
   * `<namespace>` specifies the namespace where the SR-IOV Network Operator is installed.
   * `<resourceName>` specifies the resource name of the SR-IOV network device plugin. You can create multiple SR-IOV network node policies for a resource name.
   * `<nodeSelector>` specifies the node selector for the nodes to configure. Only SR-IOV network devices on the selected nodes are configured. The SR-IOV Container Network Interface (CNI) plugin and device plugin are deployed on selected nodes only.
   * `<priority>` is optional. The priority is an integer value between `0` and `99`. A smaller value receives higher priority. For example, a priority of `10` is a higher priority than `99`. The default value is `99`.
   * `<numVfs>` specifies the number of virtual functions (VFs) to create for the SR-IOV physical network device. For an Intel network interface controller (NIC), the number of VFs cannot be larger than the total VFs supported by the device. For a Mellanox NIC, the number of VFs cannot be larger than `127`.
   * `<nicSelector>` identifies the device for the Operator to configure. You do not have to specify values for all the parameters. It is recommended to identify the network device with enough precision to avoid selecting a device unintentionally. If you specify `rootDevices`, you must also specify a value for `vendor`, `deviceID`, or `pfNames`. If you specify both `pfNames` and `rootDevices` at the same time, ensure that they refer to the same device. If you specify a value for `netFilter`, then you do not need to specify any other parameter because a network ID is unique.
   * `<pfNames>` is optional. An array of one or more physical function (PF) names for the device.
   * `<deviceType>` is optional. The driver type for the virtual functions. The only allowed value is `netdevice`. For a Mellanox NIC to work in DPDK mode on bare-metal nodes, set `isRdma` to `true`.
   * `<isRdma>` is optional. Configures whether to enable remote direct memory access (RDMA) mode. The default value is `false`. If the `isRdma` parameter is set to `true`, you can continue to use the RDMA-enabled VF as a normal network device. A device can be used in either mode. Set `isRdma` to `true` and additionally set `needVhostNet` to `true` to configure a Mellanox NIC for use with Fast Data Path DPDK applications.

   Note

   The `vfio-pci` driver type is not supported.
2. Create the `SriovNetworkNodePolicy` object:

   ```
   $ oc create -f policyallflags-sriov-node-network.yaml
   ```

   After applying the configuration update, all the pods in sriov-network-operator namespace change to the `Running` status.
3. To verify that the SR-IOV network device is configured, enter the following command. Replace `<node_name>` with the name of a node with the SR-IOV network device that you just configured. Expected output shows `Succeeded`

   ```
   $ oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name> -o jsonpath='{.status.syncStatus}'
   ```

#### [7.3.2. Configuring sysctl on a bonded SR-IOV network](#configuring-sysctl-on-bonded-sriov-network_configuring-sysctl-interface-sriov-device) Copy linkLink copied to clipboard!

You can set interface specific `sysctl` settings on a bonded interface created from two SR-IOV interfaces. Do this by adding the tuning configuration to the optional `Plugins` parameter of the bond network attachment definition.

Note

Do not edit `NetworkAttachmentDefinition` custom resources that the SR-IOV Network Operator manages. Doing so might disrupt network traffic on your additional network.

To change specific interface-level network `sysctl` settings create the `SriovNetwork` custom resource (CR) with the Container Network Interface (CNI) tuning plugin by using the following procedure.

**Prerequisites**

* Install the OpenShift Container Platform CLI (oc).
* Log in to the OpenShift Container Platform cluster as a user with cluster-admin privileges.

**Procedure**

1. Create the `SriovNetwork` custom resource (CR) for the bonded interface as in the following example CR. Save the YAML as the file `sriov-network-attachment.yaml`.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: allvalidflags
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: policyallflags
     networkNamespace: sysctl-tuning-test
     capabilities: '{ "mac": true, "ips": true }'
   ```

   * `<name>`: A name for the object. The SR-IOV Network Operator creates a NetworkAttachmentDefinition object with same name.
   * `<namespace>`: The namespace where the SR-IOV Network Operator is installed.
   * `<resourceName>`: The value for the `spec.resourceName` parameter from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network.
   * `<networkNamespace>`: The target namespace for the `SriovNetwork` object. Only pods in the target namespace can attach to the additional network.
   * `<capabilities>`: Optional: The capabilities to configure for this additional network. You can specify `"{ "ips": true }"` to enable IP address support or `"{ "mac": true }"` to enable MAC address support.
2. Create the `SriovNetwork` resource:

   ```
   $ oc create -f sriov-network-attachment.yaml
   ```
3. Create a bond network attachment definition as in the following example CR. Save the YAML as the file `sriov-bond-network-interface.yaml`.

   ```
   apiVersion: "k8s.cni.cncf.io/v1"
   kind: NetworkAttachmentDefinition
   metadata:
     name: bond-sysctl-network
     namespace: sysctl-tuning-test
   spec:
     config: '{
     "cniVersion":"0.4.0",
     "name":"bound-net",
     "plugins":[
       {
         "type":"bond",
         "mode": "active-backup",
         "failOverMac": 1,
         "linksInContainer": true,
         "miimon": "100",
         "links": [
           {"name": "net1"},
           {"name": "net2"}
         ],
         "ipam":{
           "type":"static"
         }
       },
       {
         "type":"tuning",
         "capabilities":{
           "mac":true
         },
         "sysctl":{
           "net.ipv4.conf.IFNAME.accept_redirects": "0",
           "net.ipv4.conf.IFNAME.accept_source_route": "0",
           "net.ipv4.conf.IFNAME.disable_policy": "1",
           "net.ipv4.conf.IFNAME.secure_redirects": "0",
           "net.ipv4.conf.IFNAME.send_redirects": "0",
           "net.ipv6.conf.IFNAME.accept_redirects": "0",
           "net.ipv6.conf.IFNAME.accept_source_route": "1",
           "net.ipv6.neigh.IFNAME.base_reachable_time_ms": "20000",
           "net.ipv6.neigh.IFNAME.retrans_time_ms": "2000"
         }
       }
     ]
   }'
   ```

   * `<type>`: The type is `bond`.
   * `<mode>`: The `mode` attribute specifies the bonding mode. The bonding modes supported are `balance-rr` - 0, `active-backup` - 1, and `balance-xor` - 2. For `balance-rr` or `balance-xor` modes, you must set the `trust` mode to `on` for the SR-IOV virtual function.
   * `<failOverMac>`: The `failover` attribute is mandatory for active-backup mode.
   * `<linksInContainer>`: The `linksInContainer=true` flag informs the Bond CNI that the required interfaces are to be found inside the container. By default, Bond CNI looks for these interfaces on the host which does not work for integration with SRIOV and Multus.
   * `<links>`: The `links` section defines which interfaces will be used to create the bond. By default, Multus names the attached interfaces as: "net", plus a consecutive number, starting with one.
   * `<ipam>`: A configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition. In this pod example IP addresses are configured manually, so in this case,`ipam` is set to static.
   * `<tuning>`: Add additional capabilities to the device. For example, set the `type` field to `tuning`. Specify the interface-level network `sysctl` you want to set in the sysctl field. This example sets all interface-level network `sysctl` settings that can be set.
4. Create the bond network attachment resource:

   ```
   $ oc create -f sriov-bond-network-interface.yaml
   ```

**Verification**

1. Confirm that the SR-IOV Network Operator created the `NetworkAttachmentDefinition` CR by running the following command:

   ```
   $ oc get network-attachment-definitions -n <namespace>
   ```

   * `<namespace>`: Replace with the networkNamespace that you specified when configuring the network attachment, for example, `sysctl-tuning-test`. Expected output shows the names of the NAD CRDs and the creation age in minutes.

   Note

   There might be a delay before the SR-IOV Network Operator creates the CR.
2. Create a `Pod` CR. For example, save the following YAML as the file `examplepod.yaml`:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: tunepod
     namespace: sysctl-tuning-test
     annotations:
       k8s.v1.cni.cncf.io/networks: |-
         [
           {"name": "allvalidflags"},
           {"name": "allvalidflags"},
           {
             "name": "bond-sysctl-network",
             "interface": "bond0",
             "mac": "0a:56:0a:83:04:0c",
             "ips": ["10.100.100.200/24"]
          }
         ]
   spec:
     containers:
     - name: podexample
       image: centos
       command: ["/bin/bash", "-c", "sleep INF"]
       securityContext:
         runAsUser: 2000
         runAsGroup: 3000
         allowPrivilegeEscalation: false
         capabilities:
           drop: ["ALL"]
     securityContext:
       runAsNonRoot: true
       seccompProfile:
         type: RuntimeDefault
   ```

   * `<allvalidflags>`: The name of the SR-IOV network attachment definition CR.
   * `<mac>`: Optional: The MAC address for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. To use this feature, you also must specify `{ "mac": true }` in the SriovNetwork object.
   * `<ips>`: Optional: IP addresses for the SR-IOV device that are allocated from the resource type defined in the SR-IOV network attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this feature, you also must specify `{ "ips": true }` in the `SriovNetwork` object.
3. Apply the YAML:

   ```
   $ oc apply -f examplepod.yaml
   ```
4. Verify that the pod is created by running the following command:

   ```
   $ oc get pod -n sysctl-tuning-test
   ```

   The following is example output:

   ```
   NAME      READY   STATUS    RESTARTS   AGE
   tunepod   1/1     Running   0          47s
   ```
5. Log in to the pod by running the following command:

   ```
   $ oc rsh -n sysctl-tuning-test tunepod
   ```
6. Verify the values of the configured `sysctl` flag. Find the value `net.ipv6.neigh.IFNAME.base_reachable_time_ms` by running the following command:

   ```
   $ sysctl net.ipv6.neigh.bond0.base_reachable_time_ms
   ```

### [7.4. About all-multicast mode](#nw-about-all-multi-cast-mode_configuring-sysctl-interface-sriov-device) Copy linkLink copied to clipboard!

Enabling all-multicast mode, particularly in the context of rootless applications, is critical. If you do not enable this mode, you would be required to grant the `NET_ADMIN` capability to the pod’s Security Context Constraints (SCC). If you were to allow the `NET_ADMIN` capability to grant the pod privileges to make changes that extend beyond its specific requirements, you could potentially expose security vulnerabilities.

The tuning CNI plugin supports changing several interface attributes, including all-multicast mode. By enabling this mode, you can allow applications running on Virtual Functions (VFs) that are configured on a SR-IOV network device to receive multicast traffic from applications on other VFs, whether attached to the same or different physical functions.

#### [7.4.1. Enabling the all-multicast mode on an SR-IOV network](#enabling-all-multicast-sriov-network_configuring-sysctl-interface-sriov-device) Copy linkLink copied to clipboard!

You can enable the all-multicast mode on an SR-IOV interface by:

* Adding the tuning configuration to the `metaPlugins` parameter of the `SriovNetwork` resource
* Setting the `allmulti` field to `true` in the tuning configuration

  Note

  Ensure that you create the virtual function (VF) with trust enabled.

The SR-IOV Network Operator manages additional network definitions. When you specify an additional SR-IOV network to create, the SR-IOV Network Operator creates the `NetworkAttachmentDefinition` custom resource (CR) automatically.

Note

Do not edit `NetworkAttachmentDefinition` custom resources that the SR-IOV Network Operator manages. Doing so might disrupt network traffic on your additional network.

Enable the all-multicast mode on a SR-IOV network by following this guidance.

**Prerequisites**

* You have installed the OpenShift Container Platform CLI (oc).
* You are logged in to the OpenShift Container Platform cluster as a user with `cluster-admin` privileges.
* You have installed the SR-IOV Network Operator.
* You have configured an appropriate `SriovNetworkNodePolicy` object.

**Procedure**

1. Create a YAML file with the following settings that defines a `SriovNetworkNodePolicy` object for a Mellanox ConnectX-5 device. Save the YAML file as `sriovnetpolicy-mlx.yaml`.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: sriovnetpolicy-mlx
     namespace: openshift-sriov-network-operator
   spec:
     deviceType: netdevice
     nicSelector:
       deviceID: "1017"
       pfNames:
         - ens8f0np0#0-9
       rootDevices:
         - 0000:d8:00.0
       vendor: "15b3"
     nodeSelector:
       feature.node.kubernetes.io/network-sriov.capable: "true"
     numVfs: 10
     priority: 99
     resourceName: resourcemlx
   ```
2. Optional: If the SR-IOV capable cluster nodes are not already labeled, add the `SriovNetworkNodePolicy.Spec.NodeSelector` label. For more information about labeling nodes, see "Understanding how to update labels on nodes".
3. Create the `SriovNetworkNodePolicy` object by running the following command:

   ```
   $ oc create -f sriovnetpolicy-mlx.yaml
   ```

   After applying the configuration update, all the pods in the `sriov-network-operator` namespace automatically move to a `Running` status.
4. Create the `enable-allmulti-test` namespace by running the following command:

   ```
   $ oc create namespace enable-allmulti-test
   ```
5. Create the `SriovNetwork` custom resource (CR) for the additional SR-IOV network attachment and insert the `metaPlugins` configuration, as in the following example CR YAML, and save the file as `sriov-enable-all-multicast.yaml`.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: enableallmulti
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: enableallmulti
     networkNamespace: enable-allmulti-test
     ipam: '{ "type": "static" }'
     capabilities: '{ "mac": true, "ips": true }'
     trust: "on"
     metaPlugins : |
       {
         "type": "tuning",
         "capabilities":{
           "mac":true
         },
         "allmulti": true
         }
       }
   ```

   * Replace `<name>` with a name for the object. The SR-IOV Network Operator creates a `NetworkAttachmentDefinition` object with the same name.
   * Replace `<namespace>` with the namespace where the SR-IOV Network Operator is installed.
   * Replace `<resourceName>` with a value for the `spec.resourceName` parameter from the `SriovNetworkNodePolicy` object that defines the SR-IOV hardware for this additional network.
   * Replace `<networkNamespace>` with the target namespace for the `SriovNetwork` object. Only pods in the target namespace can attach to the additional network.
   * Replace `<ipam>` with a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.
   * Optional: Set capabilities for the additional network. You can specify `"{ "ips": true }"` to enable IP address support or `"{ "mac": true }"` to enable MAC address support.
   * Specify the trust mode of the virtual function. This must be set to "on".
   * Add more capabilities to the device by using the `metaPlugins` parameter. In this use case, set the `type` field to `tuning`, and add the `allmulti` field and set it to `true`.
6. Create the `SriovNetwork` resource by running the following command:

   ```
   $ oc create -f sriov-enable-all-multicast.yaml
   ```

**Verification**

* Confirm that the SR-IOV Network Operator created the `NetworkAttachmentDefinition` CR by running the following command:

  ```
  $ oc get network-attachment-definitions -n <namespace>
  ```

  + Replace `<namespace>` with the value for `networkNamespace` that you specified in the `SriovNetwork` object. For this example, that is `enable-allmulti-test`. The expected output shows the name of the NAD CR and the creation age in minutes.

  Note

  There might be a delay before the SR-IOV Network Operator creates the CR.
* Display information about the SR-IOV network resources by running the following command:

  ```
  $ oc get sriovnetwork -n openshift-sriov-network-operator
  ```

  1. To verify that the tuning CNI is correctly configured and that the additional SR-IOV network attachment is attached, create a `Pod` CR. Save the following sample YAML in a file named `examplepod.yaml`:

     ```
     apiVersion: v1
     kind: Pod
     metadata:
       name: samplepod
       namespace: enable-allmulti-test
       annotations:
         k8s.v1.cni.cncf.io/networks: |-
           [
             {
               "name": "enableallmulti",
               "mac": "0a:56:0a:83:04:0c",
               "ips": ["10.100.100.200/24"]
            }
           ]
     spec:
       containers:
       - name: podexample
         image: centos
         command: ["/bin/bash", "-c", "sleep INF"]
         securityContext:
           runAsUser: 2000
           runAsGroup: 3000
           allowPrivilegeEscalation: false
           capabilities:
             drop: ["ALL"]
       securityContext:
         runAsNonRoot: true
         seccompProfile:
           type: RuntimeDefault
     ```

     + Replace `<name>` with the name of the SR-IOV network attachment definition CR.
     + Optional: Specify the MAC address for the SR-IOV device that is allocated from the resource type defined in the SR-IOV network attachment definition CR. To use this feature, you also must specify `{"mac": true}` in the SriovNetwork object.
     + Optional: Specify the IP addresses for the SR-IOV device that are allocated from the resource type defined in the SR-IOV network attachment definition CR. Both IPv4 and IPv6 addresses are supported. To use this feature, you also must specify `{ "ips": true }` in the `SriovNetwork` object.
  2. Create the `Pod` CR by running the following command:

     ```
     $ oc apply -f examplepod.yaml
     ```
  3. Verify that the pod is created by running the following command:

     ```
     $ oc get pod -n enable-allmulti-test
     ```

     The following is example output:

     ```
     NAME       READY   STATUS    RESTARTS   AGE
     samplepod  1/1     Running   0          47s
     ```
  4. Log in to the pod by running the following command:

     ```
     $ oc rsh -n enable-allmulti-test samplepod
     ```
  5. List all the interfaces associated with the pod by running the following command:

     ```
     sh-4.4# ip link
     ```

     The following is example output:

     ```
     1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN mode DEFAULT group default qlen 1000
         link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
     2: eth0@if22: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 8901 qdisc noqueue state UP mode DEFAULT group default
         link/ether 0a:58:0a:83:00:10 brd ff:ff:ff:ff:ff:ff link-netnsid 0
     3: net1@if24: <BROADCAST,MULTICAST,ALLMULTI,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP mode DEFAULT group default
         link/ether ee:9b:66:a4:ec:1d brd ff:ff:ff:ff:ff:ff link-netnsid 0
     ```

     + `eth0@if22` is the primary interface.
     + `net1@if24` is the secondary interface configured with the network-attachment-definition that supports the all-multicast mode (`ALLMULTI` flag).

## [Chapter 8. Configuring QinQ support for SR-IOV enabled workloads](#configuring-qinq-support) Copy linkLink copied to clipboard!

QinQ, formally known as 802.1Q-in-802.1Q, is a networking technique defined by IEEE 802.1ad. IEEE 802.1ad extends the IEEE 802.1Q-1998 standard and enriches VLAN capabilities by introducing an additional 802.1Q tag to packets already tagged with 802.1Q. This method is also referred to as VLAN stacking or double VLAN.

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

### [8.1. About 802.1Q-in-802.1Q support](#nw-about-qinq-support_configuring-qinq-support) Copy linkLink copied to clipboard!

In traditional VLAN setups, frames typically contain a single VLAN tag, such as VLAN-100, as well as other metadata such as Quality of Service (QoS) bits and protocol information. QinQ introduces a second VLAN tag, where the service provider designates the outer tag for their use, offering them flexibility, while the inner tag remains dedicated to the customer’s VLAN.

QinQ facilitates the creation of nested VLANs by using double VLAN tagging, enabling finer segmentation and isolation of traffic within a network environment. This approach is particularly valuable in service provider networks where you need to deliver VLAN-based services to multiple customers over a common infrastructure, while ensuring separation and isolation of traffic.

The following diagram illustrates how OpenShift Container Platform can use SR-IOV and QinQ to achieve advanced network segmentation and isolation for containerized workloads.

The diagram shows how double VLAN tagging (QinQ) works in a worker node with SR-IOV support. The SR-IOV virtual function (VF) located in the pod namespace, `ext0` is configured by the SR-IOV Container Network Interface (CNI) with a VLAN ID and VLAN protocol. This corresponds to the S-tag. Inside the pod, the VLAN CNI creates a subinterface using the primary interface `ext0`. This subinterface adds an internal VLAN ID using the 802.1Q protocol, which corresponds to the C-tag.

This demonstrates how QinQ enables finer traffic segmentation and isolation within the network. The Ethernet frame structure is detailed on the right, highlighting the inclusion of both VLAN tags, EtherType, IP, TCP, and Payload sections. QinQ facilitates the delivery of VLAN-based services to multiple customers over a shared infrastructure while ensuring traffic separation and isolation.

The OpenShift Container Platform SR-IOV solution already supports setting the VLAN protocol on the `SriovNetwork` custom resource (CR). The virtual function (VF) can use this protocol to set the VLAN tag, also known as the outer tag. Pods can then use the VLAN CNI plugin to configure the inner tag.

### [8.2. Configuring QinQ support for SR-IOV enabled workloads](#nw-configuring-qinq-sriov-proc_configuring-qinq-support) Copy linkLink copied to clipboard!

Configure QinQ support for SR-IOV enabled workloads to enable double VLAN tagging on your cluster.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have access to the cluster as a user with the `cluster-admin` role.
* You have installed the SR-IOV Network Operator.

**Procedure**

1. Create a file named `sriovnetpolicy-810-sriov-node-network.yaml` by using the following content:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: sriovnetpolicy-810
     namespace: openshift-sriov-network-operator
   spec:
     deviceType: netdevice
     nicSelector:
       pfNames:
         - ens5f0#0-9
     nodeSelector:
       node-role.kubernetes.io/worker-cnf: ""
     numVfs: 10
     priority: 99
     resourceName: resource810
   ```
2. Create the `SriovNetworkNodePolicy` object by running the following command:

   ```
   $ oc create -f sriovnetpolicy-810-sriov-node-network.yaml
   ```
3. Open a separate terminal window and monitor the synchronization status of the SR-IOV network node state for the node specified in the `openshift-sriov-network-operator` namespace by running the following command:

   ```
   $ watch -n 1 'oc get sriovnetworknodestates -n openshift-sriov-network-operator <node_name> -o jsonpath="{.status.syncStatus}"'
   ```

   The synchronization status indicates a change from `InProgress` to `Succeeded`.
4. Create a `SriovNetwork` object, and set the outer VLAN called the S-tag, or `Service Tag`, as it belongs to the infrastructure.

   Important

   You must configure the VLAN on the trunk interface of the switch. In addition, you might need to further configure some switches to support QinQ tagging.

   1. Create a file named `nad-sriovnetwork-1ad-810.yaml` by using the following content:

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetwork
      metadata:
        name: sriovnetwork-1ad-810
        namespace: openshift-sriov-network-operator
      spec:
        ipam: '{}'
        vlan: <vlan_id>
        vlanProto: <vlan_protocol>
        networkNamespace: default
        resourceName: resource810
      ```

      * `<vlan_id>` specifies the S-tag VLAN tag, for example `171`.
      * `<vlan_protocol>` specifies the VLAN protocol to assign to the virtual function (VF). Supported values are `802.1ad` and `802.1q`. The default value is `802.1q`.
   2. Create the object by running the following command:

      ```
      $ oc create -f nad-sriovnetwork-1ad-810.yaml
      ```
5. Create a `NetworkAttachmentDefinition` object with an inner VLAN. The inner VLAN is often referred to as the C-tag, or `Customer Tag`, as it belongs to the Network Function:

   1. Create a file named `nad-cvlan100.yaml` by using the following content:

      ```
      apiVersion: k8s.cni.cncf.io/v1
      kind: NetworkAttachmentDefinition
      metadata:
        name: nad-cvlan100
        namespace: default
      spec:
        config: '{
          "name": "vlan-100",
          "cniVersion": "0.3.1",
          "type": "vlan",
          "linkInContainer": true,
          "master": "<vf_interface>",
          "vlanId": 100,
          "ipam": {"type": "static"}
        }'
      ```

      * `<vf_interface>` specifies the VF interface inside the pod. The default name is `net1` because the name is not set in the pod annotation.
   2. Apply the YAML file by running the following command:

      ```
      $ oc apply -f nad-cvlan100.yaml
      ```

**Verification**

* Verify QinQ is active on the node by following this procedure:

  1. Create a file named `test-qinq-pod.yaml` by using the following content:

     ```
     apiVersion: v1
     kind: Pod
     metadata:
       name: test-pod
       annotations:
         k8s.v1.cni.cncf.io/networks: sriovnetwork-1ad-810, nad-cvlan100
     spec:
       containers:
         - name: test-container
           image: quay.io/ocp-edge-qe/cnf-gotests-client:v4.10
           imagePullPolicy: Always
           securityContext:
             privileged: true
     ```
  2. Create the test pod by running the following command:

     ```
     $ oc create -f test-qinq-pod.yaml
     ```
  3. Enter into a debug session on the target node where the pod is present and display information about the network interface `ens5f0` by running the following command:

     ```
     $ oc debug node/my-cluster-node -- bash -c "ip link show ens5f0"
     ```

     **Example output**

     ```
     6: ens5f0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
     link/ether b4:96:91:a5:22:10 brd ff:ff:ff:ff:ff:ff
     vf 0 link/ether a2:81:ba:d0:6f:f3 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
     vf 1 link/ether 8a:bb:0a:36:f2:ed brd ff:ff:ff:ff:ff:ff, vlan 171, vlan protocol 802.1ad, spoof checking on, link-state auto, trust off
     vf 2 link/ether ca:0e:e1:5b:0c:d2 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
     vf 3 link/ether ee:6c:e2:f5:2c:70 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
     vf 4 link/ether 0a:d6:b7:66:5e:e8 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
     vf 5 link/ether da:d5:e7:14:4f:aa brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
     vf 6 link/ether d6:8e:85:75:12:5c brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
     vf 7 link/ether d6:eb:ce:9c:ea:78 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
     vf 8 link/ether 5e:c5:cc:05:93:3c brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust on
     vf 9 link/ether a6:5a:7c:1c:2a:16 brd ff:ff:ff:ff:ff:ff, spoof checking on, link-state auto, trust off
     ```

     The `vlan protocol 802.1ad` ID in the output indicates that the interface supports VLAN tagging with protocol 802.1ad (QinQ). The VLAN ID is 171.

## [Chapter 9. Using high performance multicast](#using-sriov-multicast) Copy linkLink copied to clipboard!

You can use multicast on your Single Root I/O Virtualization (SR-IOV) hardware network.

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

### [9.1. High performance multicast](#nw-high-performance-multicast_using-sriov-multicast) Copy linkLink copied to clipboard!

The OVN-Kubernetes network plugin supports multicast between pods on the default network. This is best used for low-bandwidth coordination or service discovery, and not high-bandwidth applications. For applications such as streaming media, such as Internet Protocol television (IPTV) and multipoint videoconferencing, you can use Single Root I/O Virtualization (SR-IOV) hardware to provide near-native performance.

When using additional SR-IOV interfaces for multicast:

* Multicast packages must be sent or received by a pod through the additional SR-IOV interface.
* The physical network which connects the SR-IOV interfaces decides the multicast routing and topology, which is not controlled by OpenShift Container Platform.

### [9.2. Configuring an SR-IOV interface for multicast](#nw-using-an-sriov-interface-for-multicast_using-sriov-multicast) Copy linkLink copied to clipboard!

The following procedure creates an example SR-IOV interface for multicast.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* You must log in to the cluster with a user that has the `cluster-admin` role.

**Procedure**

1. Create a `SriovNetworkNodePolicy` object:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: policy-example
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: example
     nodeSelector:
       feature.node.kubernetes.io/network-sriov.capable: "true"
     numVfs: 4
     nicSelector:
       vendor: "8086"
       pfNames: ['ens803f0']
       rootDevices: ['0000:86:00.0']
   ```
2. Create a `SriovNetwork` object:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: net-example
     namespace: openshift-sriov-network-operator
   spec:
     networkNamespace: default
     ipam: |
       {
         "type": "host-local",
         "subnet": "10.56.217.0/24",
         "rangeStart": "10.56.217.171",
         "rangeEnd": "10.56.217.181",
         "routes": [
           {"dst": "224.0.0.0/5"},
           {"dst": "232.0.0.0/5"}
         ],
         "gateway": "10.56.217.1"
       }
     resourceName: example
   ```

   * If you choose to configure DHCP as IPAM, ensure that you provision the following default routes through your DHCP server: `224.0.0.0/5` and `232.0.0.0/5`. This is to override the static multicast route set by the default network provider.
3. Create a pod with multicast application:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: testpmd
     namespace: default
     annotations:
       k8s.v1.cni.cncf.io/networks: nic1
   spec:
     containers:
     - name: example
       image: rhel7:latest
       securityContext:
         capabilities:
           add: ["NET_ADMIN"]
       command: [ "sleep", "infinity"]
   ```

   * The `NET_ADMIN` capability is required only if your application needs to assign the multicast IP address to the SR-IOV interface. Otherwise, you can omit it.

## [Chapter 10. Using DPDK and RDMA](#using-dpdk-and-rdma) Copy linkLink copied to clipboard!

The containerized Data Plane Development Kit (DPDK) application is supported on OpenShift Container Platform. You can use Single Root I/O Virtualization (SR-IOV) network hardware with the Data Plane Development Kit (DPDK) and with remote direct memory access (RDMA).

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

### [10.1. Example use of a virtual function in a pod](#example-vf-use-in-pod_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

You can run a remote direct memory access (RDMA) or a Data Plane Development Kit (DPDK) application in a pod with SR-IOV VF attached.

This example shows a pod using a virtual function (VF) in RDMA mode:

**`Pod` spec that uses RDMA mode**

```
apiVersion: v1
kind: Pod
metadata:
  name: rdma-app
  annotations:
    k8s.v1.cni.cncf.io/networks: sriov-rdma-mlnx
spec:
  containers:
  - name: testpmd
    image: <RDMA_image>
    imagePullPolicy: IfNotPresent
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
    command: ["sleep", "infinity"]
```

The following example shows a pod with a VF in DPDK mode:

**`Pod` spec that uses DPDK mode**

```
apiVersion: v1
kind: Pod
metadata:
  name: dpdk-app
  annotations:
    k8s.v1.cni.cncf.io/networks: sriov-dpdk-net
spec:
  containers:
  - name: testpmd
    image: <DPDK_image>
    securityContext:
      runAsUser: 0
      capabilities:
        add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
    volumeMounts:
    - mountPath: /dev/hugepages
      name: hugepage
    resources:
      limits:
        memory: "1Gi"
        cpu: "2"
        hugepages-1Gi: "4Gi"
      requests:
        memory: "1Gi"
        cpu: "2"
        hugepages-1Gi: "4Gi"
    command: ["sleep", "infinity"]
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
```

### [10.2. Using a virtual function in DPDK mode with an Intel NIC](#example-vf-use-in-dpdk-mode-intel_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

You can use a virtual function (VF) in Data Plane Development Kit (DPDK) mode with an Intel NIC by creating a `SriovNetworkNodePolicy` object and then deploying a pod.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Install the SR-IOV Network Operator.
* Log in as a user with `cluster-admin` privileges.

**Procedure**

1. Create the following `SriovNetworkNodePolicy` object, and then save the YAML in the `intel-dpdk-node-policy.yaml` file.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: intel-dpdk-node-policy
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: intelnics
     nodeSelector:
       feature.node.kubernetes.io/network-sriov.capable: "true"
     priority: <priority>
     numVfs: <num>
     nicSelector:
       vendor: "8086"
       deviceID: "158b"
       pfNames: ["<pf_name>", ...]
       rootDevices: ["<pci_bus_id>", "..."]
     deviceType: vfio-pci
   ```

   where:

   `spec.deviceType`
   :   Specifies the driver type for the virtual functions. Set to `vfio-pci`.

       Note

       See the `Configuring SR-IOV network devices` section for a detailed explanation on each option in `SriovNetworkNodePolicy`.

       When applying the configuration specified in a `SriovNetworkNodePolicy` object, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes. It might take several minutes for a configuration change to apply. Ensure that there are enough available nodes in your cluster to handle the evicted workload beforehand.

       After the configuration update is applied, all the pods in `openshift-sriov-network-operator` namespace will change to a `Running` status.
2. Create the `SriovNetworkNodePolicy` object by running the following command:

   ```
   $ oc create -f intel-dpdk-node-policy.yaml
   ```
3. Create the following `SriovNetwork` object, and then save the YAML in the `intel-dpdk-network.yaml` file.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: intel-dpdk-network
     namespace: openshift-sriov-network-operator
   spec:
     networkNamespace: <target_namespace>
     ipam: |-
   # ...
     vlan: <vlan>
     resourceName: intelnics
   ```

   where:

   `spec.ipam`
   :   Specifies a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.

       Note

       See the "Configuring SR-IOV additional network" section for a detailed explanation on each option in `SriovNetwork`.

       An optional library, app-netutil, provides several API methods for gathering network information about a container’s parent pod.
4. Create the `SriovNetwork` object by running the following command:

   ```
   $ oc create -f intel-dpdk-network.yaml
   ```
5. Create the following `Pod` spec, and then save the YAML in the `intel-dpdk-pod.yaml` file.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: dpdk-app
     namespace: <target_namespace>
     annotations:
       k8s.v1.cni.cncf.io/networks: intel-dpdk-network
   spec:
     containers:
     - name: testpmd
       image: <DPDK_image>
       securityContext:
         runAsUser: 0
         capabilities:
           add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
       volumeMounts:
       - mountPath: /mnt/huge
         name: hugepage
       resources:
         limits:
           openshift.io/intelnics: "1"
           memory: "1Gi"
           cpu: "4"
           hugepages-1Gi: "4Gi"
         requests:
           openshift.io/intelnics: "1"
           memory: "1Gi"
           cpu: "4"
           hugepages-1Gi: "4Gi"
       command: ["sleep", "infinity"]
     volumes:
     - name: hugepage
       emptyDir:
         medium: HugePages
   ```

   where:

   `metadata.namespace`
   :   Specifies the same namespace where the `SriovNetwork` object `intel-dpdk-network` is created. If you want to create the pod in a different namespace, change `target_namespace` in both the `Pod` spec and the `SriovNetwork` object.

   `spec.containers.image`
   :   Specifies the DPDK image which includes your application and the DPDK library used by application.

   `spec.containers.securityContext.capabilities.add`
   :   Specifies additional capabilities required by the application inside the container for hugepage allocation, system resource allocation, and network interface access.

   `spec.containers.volumeMounts.mountPath`
   :   Specifies the path where a hugepage volume is mounted in the DPDK pod. The hugepage volume is backed by the `emptyDir` volume type with the medium being `Hugepages`.

   `spec.containers.resources.limits.openshift.io/intelnics`
   :   Optional: Specifies the number of DPDK devices allocated to DPDK pod. If not explicitly specified, this resource request and limit is automatically added by the SR-IOV network resource injector. The SR-IOV network resource injector is an admission controller component managed by the SR-IOV Operator. It is enabled by default and can be disabled by setting `enableInjector` option to `false` in the default `SriovOperatorConfig` CR.

   `spec.containers.resources.limits.cpu`
   :   Specifies the number of CPUs. The DPDK pod usually requires exclusive CPUs to be allocated from the kubelet. This is achieved by setting CPU Manager policy to `static` and creating a pod with `Guaranteed` QoS.

   `spec.containers.resources.limits.hugepages-1Gi`
   :   Specifies the hugepage size `hugepages-1Gi` or `hugepages-2Mi` and the quantity of hugepages that will be allocated to the DPDK pod. Configure `2Mi` and `1Gi` hugepages separately. Configuring `1Gi` hugepage requires adding kernel arguments to Nodes. For example, adding kernel arguments `default_hugepagesz=1GB`, `hugepagesz=1G` and `hugepages=16` will result in `16*1Gi` hugepages be allocated during system boot.
6. Create the DPDK pod by running the following command:

   ```
   $ oc create -f intel-dpdk-pod.yaml
   ```

### [10.3. Using a virtual function in DPDK mode with a Mellanox NIC](#example-vf-use-in-dpdk-mode-mellanox_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

You can create a network node policy and create a Data Plane Development Kit (DPDK) pod by using a virtual function in DPDK mode with a Mellanox NIC.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have installed the Single Root I/O Virtualization (SR-IOV) Network Operator.
* You have logged in as a user with `cluster-admin` privileges.

**Procedure**

1. Save the following `SriovNetworkNodePolicy` YAML configuration to an `mlx-dpdk-node-policy.yaml` file:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: mlx-dpdk-node-policy
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: mlxnics
     nodeSelector:
       feature.node.kubernetes.io/network-sriov.capable: "true"
     priority: <priority>
     numVfs: <num>
     nicSelector:
       vendor: "15b3"
       deviceID: "1015"
       pfNames: ["<pf_name>", ...]
       rootDevices: ["<pci_bus_id>", "..."]
     deviceType: netdevice
     isRdma: true
   ```

   where:

   `spec.nicSelector.deviceID`
   :   Specifies the device hex code of the SR-IOV network device. The value `"1015"` is associated with a Mellanox NIC.

   `spec.deviceType`
   :   Specifies the driver type for the virtual functions. A Mellanox SR-IOV Virtual Function (VF) can work in DPDK mode without using the `vfio-pci` device type. Set to `netdevice`. The VF device is displayed as a kernel network interface inside a container.

   `spec.isRdma`
   :   Setting to `true` enables Remote Direct Memory Access (RDMA) mode. This is required for Mellanox cards to work in DPDK mode.

       Note

       See *Configuring an SR-IOV network device* for a detailed explanation of each option in the `SriovNetworkNodePolicy` object.

       When applying the configuration specified in an `SriovNetworkNodePolicy` object, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes. It might take several minutes for a configuration change to apply. Ensure that there are enough available nodes in your cluster to handle the evicted workload beforehand.

       After the configuration update is applied, all the pods in the `openshift-sriov-network-operator` namespace will change to a `Running` status.
2. Create the `SriovNetworkNodePolicy` object by running the following command:

   ```
   $ oc create -f mlx-dpdk-node-policy.yaml
   ```
3. Save the following `SriovNetwork` YAML configuration to an `mlx-dpdk-network.yaml` file:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: mlx-dpdk-network
     namespace: openshift-sriov-network-operator
   spec:
     networkNamespace: <target_namespace>
     ipam: |-
   ...
     vlan: <vlan>
     resourceName: mlxnics
   ```

   where:

   `spec.ipam`
   :   Specifies a configuration object for the IP Address Management (IPAM) Container Network Interface (CNI) plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.

       Note

       See *Configuring an SR-IOV network device* for a detailed explanation on each option in the `SriovNetwork` object.

       The `app-netutil` option library provides several API methods for gathering network information about the parent pod of a container.
4. Create the `SriovNetwork` object by running the following command:

   ```
   $ oc create -f mlx-dpdk-network.yaml
   ```
5. Save the following `Pod` YAML configuration to an `mlx-dpdk-pod.yaml` file:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: dpdk-app
     namespace: <target_namespace>
     annotations:
       k8s.v1.cni.cncf.io/networks: mlx-dpdk-network
   spec:
     containers:
     - name: testpmd
       image: <DPDK_image>
       securityContext:
         runAsUser: 0
         capabilities:
           add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
       volumeMounts:
       - mountPath: /mnt/huge
         name: hugepage
       resources:
         limits:
           openshift.io/mlxnics: "1"
           memory: "1Gi"
           cpu: "4"
           hugepages-1Gi: "4Gi"
         requests:
           openshift.io/mlxnics: "1"
           memory: "1Gi"
           cpu: "4"
           hugepages-1Gi: "4Gi"
       command: ["sleep", "infinity"]
     volumes:
     - name: hugepage
       emptyDir:
         medium: HugePages
   ```

   where:

   `metadata.namespace`
   :   Specifies the same namespace where `SriovNetwork` object `mlx-dpdk-network` is created. To create the pod in a different namespace, change `target_namespace` in both the `Pod` spec and `SriovNetwork` object.

   `spec.containers.image`
   :   Specifies the DPDK image which includes your application and the DPDK library used by the application.

   `spec.containers.securityContext.capabilities.add`
   :   Specifies additional capabilities required by the application inside the container for hugepage allocation, system resource allocation, and network interface access.

   `spec.containers.volumeMounts.mountPath`
   :   Specifies the path where the hugepage volume is mounted in the DPDK pod. The hugepage volume is backed by the `emptyDir` volume type with the medium being `Hugepages`.

   `spec.containers.resources.limits.openshift.io/mlxnics`
   :   Optional: Specifies the number of DPDK devices allocated for the DPDK pod. If not explicitly specified, this resource request and limit is automatically added by the SR-IOV network resource injector. The SR-IOV network resource injector is an admission controller component managed by SR-IOV Operator. It is enabled by default and can be disabled by setting the `enableInjector` option to `false` in the default `SriovOperatorConfig` CR.

   `spec.containers.resources.limits.cpu`
   :   Specifies the number of CPUs. The DPDK pod usually requires that exclusive CPUs be allocated from the kubelet. To do this, set the CPU Manager policy to `static` and create a pod with `Guaranteed` Quality of Service (QoS).

   `spec.containers.resources.limits.hugepages-1Gi`
   :   Specifies the hugepage size `hugepages-1Gi` or `hugepages-2Mi` and the quantity of hugepages that will be allocated to the DPDK pod. Configure `2Mi` and `1Gi` hugepages separately. Configuring `1Gi` hugepages requires adding kernel arguments to Nodes.
6. Create the DPDK pod by running the following command:

   ```
   $ oc create -f mlx-dpdk-pod.yaml
   ```

### [10.4. Using the TAP CNI to run a rootless DPDK workload with kernel access](#nw-running-dpdk-rootless-tap_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

DPDK applications can use `virtio-user` as an exception path to inject certain types of packets, such as log messages, into the kernel for processing. For more information about this feature, see [Virtio\_user as Exception Path](https://doc.dpdk.org/guides/howto/virtio_user_as_exception_path.html).

In OpenShift Container Platform version 4.14 and later, you can use non-privileged pods to run DPDK applications alongside the tap CNI plugin. To enable this functionality, you need to mount the `vhost-net` device by setting the `needVhostNet` parameter to `true` within the `SriovNetworkNodePolicy` object.

**Figure 10.1. DPDK and TAP example configuration**

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have installed the SR-IOV Network Operator.
* You are logged in as a user with `cluster-admin` privileges.
* Ensure that `setsebools container_use_devices=on` is set as root on all nodes.

  Note

  Use the Machine Config Operator to set this SELinux boolean.

**Procedure**

1. Create a file, such as `test-namespace.yaml`, with content such as the following example:

   ```
   apiVersion: v1
   kind: Namespace
   metadata:
     name: test-namespace
     labels:
       pod-security.kubernetes.io/enforce: privileged
       pod-security.kubernetes.io/audit: privileged
       pod-security.kubernetes.io/warn: privileged
       security.openshift.io/scc.podSecurityLabelSync: "false"
   ```
2. Create the new `Namespace` object by running the following command:

   ```
   $ oc apply -f test-namespace.yaml
   ```
3. Create a file, such as `sriov-node-network-policy.yaml`, with content such as the following example:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
    name: sriovnic
    namespace: openshift-sriov-network-operator
   spec:
    deviceType: netdevice
    isRdma: true
    needVhostNet: true
    nicSelector:
      vendor: "15b3"
      deviceID: "101b"
      rootDevices: ["00:05.0"]
    numVfs: 10
    priority: 99
    resourceName: sriovnic
    nodeSelector:
       feature.node.kubernetes.io/network-sriov.capable: "true"
   ```

   where:

   `spec.deviceType`
   :   Specifies that the profile is tailored specifically for Mellanox Network Interface Controllers (NICs). Set to `netdevice`.

   `spec.isRdma`
   :   Setting to `true` is only required for a Mellanox NIC.

   `spec.needVhostNet`
   :   Setting to `true` mounts the `/dev/net/tun` and `/dev/vhost-net` devices into the container so the application can create a tap device and connect the tap device to the DPDK workload.

   `spec.nicSelector.vendor`
   :   Specifies the vendor hexadecimal code of the SR-IOV network device. The value `"15b3"` is associated with a Mellanox NIC.

   `spec.nicSelector.deviceID`
   :   Specifies the device hexadecimal code of the SR-IOV network device.
4. Create the `SriovNetworkNodePolicy` object by running the following command:

   ```
   $ oc create -f sriov-node-network-policy.yaml
   ```
5. Create the following `SriovNetwork` object, and then save the YAML in the `sriov-network-attachment.yaml` file:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
    name: sriov-network
    namespace: openshift-sriov-network-operator
   spec:
    networkNamespace: test-namespace
    resourceName: sriovnic
    spoofChk: "off"
    trust: "on"
   ```

   Note

   See the "Configuring SR-IOV additional network" section for a detailed explanation on each option in `SriovNetwork`.

   An optional library, `app-netutil`, provides several API methods for gathering network information about a container’s parent pod.
6. Create the `SriovNetwork` object by running the following command:

   ```
   $ oc create -f sriov-network-attachment.yaml
   ```
7. Create a file, such as `tap-example.yaml`, that defines a network attachment definition, with content such as the following example:

   ```
   apiVersion: "k8s.cni.cncf.io/v1"
   kind: NetworkAttachmentDefinition
   metadata:
    name: tap-one
    namespace: test-namespace
   spec:
    config: '{
      "cniVersion": "0.4.0",
      "name": "tap",
      "plugins": [
        {
           "type": "tap",
           "multiQueue": true,
           "selinuxcontext": "system_u:system_r:container_t:s0"
        },
        {
          "type":"tuning",
          "capabilities":{
            "mac":true
          }
        }
      ]
    }'
   ```

   where:

   `metadata.namespace`
   :   Specifies the same `target_namespace` where the `SriovNetwork` object is created.
8. Create the `NetworkAttachmentDefinition` object by running the following command:

   ```
   $ oc apply -f tap-example.yaml
   ```
9. Create a file, such as `dpdk-pod-rootless.yaml`, with content such as the following example:

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: dpdk-app
     namespace: test-namespace
     annotations:
       k8s.v1.cni.cncf.io/networks: '[
         {"name": "sriov-network", "namespace": "test-namespace"},
         {"name": "tap-one", "interface": "ext0", "namespace": "test-namespace"}]'
   spec:
     nodeSelector:
       kubernetes.io/hostname: "worker-0"
     securityContext:
         fsGroup: 1001
         runAsGroup: 1001
         seccompProfile:
           type: RuntimeDefault
     containers:
     - name: testpmd
       image: <DPDK_image>
       securityContext:
         capabilities:
           drop: ["ALL"]
           add:
             - IPC_LOCK
             - NET_RAW #for mlx only
         runAsUser: 1001
         privileged: false
         allowPrivilegeEscalation: true
         runAsNonRoot: true
       volumeMounts:
       - mountPath: /mnt/huge
         name: hugepages
       resources:
         limits:
           openshift.io/sriovnic: "1"
           memory: "1Gi"
           cpu: "4"
           hugepages-1Gi: "4Gi"
         requests:
           openshift.io/sriovnic: "1"
           memory: "1Gi"
           cpu: "4"
           hugepages-1Gi: "4Gi"
       command: ["sleep", "infinity"]
     runtimeClassName: performance-cnf-performanceprofile
     volumes:
     - name: hugepages
       emptyDir:
         medium: HugePages
   ```

   where:

   `metadata.namespace`
   :   Specifies the same `target_namespace` in which the `SriovNetwork` object is created. If you want to create the pod in a different namespace, change `target_namespace` in both the `Pod` spec and the `SriovNetwork` object.

   `spec.securityContext.fsGroup`
   :   Sets the group ownership of volume-mounted directories and files created in those volumes.

   `spec.securityContext.runAsGroup`
   :   Specifies the primary group ID used for running the container.

   `spec.containers.image`
   :   Specifies the DPDK image that contains your application and the DPDK library used by application.

   `spec.containers.securityContext.capabilities.drop`
   :   Removing all capabilities (`ALL`) from the container’s `securityContext` means that the container has no special privileges beyond what is necessary for normal operation.

   `spec.containers.securityContext.capabilities.add`
   :   Specifies additional capabilities required by the application inside the container for hugepage allocation, system resource allocation, and network interface access. These capabilities must also be set in the binary file by using the `setcap` command. Mellanox network interface controller (NIC) requires the `NET_RAW` capability.

   `spec.containers.securityContext.runAsUser`
   :   Specifies the user ID used for running the container.

   `spec.containers.securityContext.privileged`
   :   Setting to `false` indicates that the container or containers within the pod should not be granted privileged access to the host system.

   `spec.containers.securityContext.allowPrivilegeEscalation`
   :   Setting to `true` allows a container to escalate its privileges beyond the initial non-root privileges it might have been assigned.

   `spec.containers.securityContext.runAsNonRoot`
   :   Setting to `true` ensures that the container runs with a non-root user. This helps enforce the principle of least privilege, limiting the potential impact of compromising the container and reducing the attack surface.

   `spec.containers.volumeMounts.mountPath`
   :   Specifies the path where a hugepage volume is mounted in the DPDK pod. The hugepage volume is backed by the `emptyDir` volume type with the medium being `Hugepages`.

   `spec.containers.resources.limits.openshift.io/sriovnic`
   :   Optional: Specifies the number of DPDK devices allocated for the DPDK pod. If not explicitly specified, this resource request and limit is automatically added by the SR-IOV network resource injector. The SR-IOV network resource injector is an admission controller component managed by SR-IOV Operator. It is enabled by default and can be disabled by setting the `enableInjector` option to `false` in the default `SriovOperatorConfig` CR.

   `spec.containers.resources.limits.cpu`
   :   Specifies the number of CPUs. The DPDK pod usually requires exclusive CPUs to be allocated from the kubelet. This is achieved by setting CPU Manager policy to `static` and creating a pod with `Guaranteed` QoS.

   `spec.containers.resources.limits.hugepages-1Gi`
   :   Specifies the hugepage size `hugepages-1Gi` or `hugepages-2Mi` and the quantity of hugepages that will be allocated to the DPDK pod. Configure `2Mi` and `1Gi` hugepages separately. Configuring `1Gi` hugepage requires adding kernel arguments to Nodes. For example, adding kernel arguments `default_hugepagesz=1GB`, `hugepagesz=1G` and `hugepages=16` will result in `16*1Gi` hugepages be allocated during system boot.

   `spec.runtimeClassName`
   :   Specifies the performance profile runtime class. If your performance profile is not named `cnf-performance profile`, replace that string with the correct performance profile name.
10. Create the DPDK pod by running the following command:

    ```
    $ oc create -f dpdk-pod-rootless.yaml
    ```

### [10.5. Overview of achieving a specific DPDK line rate](#nw-sriov-example-dpdk-line-rate_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

To achieve a specific Data Plane Development Kit (DPDK) line rate, deploy a Node Tuning Operator and configure Single Root I/O Virtualization (SR-IOV). You must also tune the DPDK settings for the following resources:

* Isolated CPUs
* Hugepages
* The topology scheduler

Note

In previous versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift Container Platform applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator.

The following diagram shows the components of a DPDK test environment:

* **Traffic generator**: An application that can generate high-volume packet traffic.
* **SR-IOV-supporting NIC**: A network interface controller (NIC) compatible with SR-IOV. The card runs several virtual functions on a physical interface.
* **Physical Function (PF)**: A PCI Express (PCIe) function of a network adapter that supports the SR-IOV interface.
* **Virtual Function (VF)**: A lightweight PCIe function on a network adapter that supports SR-IOV. The VF is associated with the PCIe PF on the network adapter. The VF represents a virtualized instance of the network adapter.
* **Switch**: A network switch. Nodes can also be connected back-to-back.
* **`testpmd`**: An example application included with DPDK. The `testpmd` application can be used to test the DPDK in a packet-forwarding mode. The `testpmd` application is also an example of how to build a fully-fledged application using the DPDK Software Development Kit (SDK).
* **worker 0** and **worker 1**: OpenShift Container Platform nodes.

### [10.6. Using SR-IOV and the Node Tuning Operator to achieve a DPDK line rate](#nw-example-dpdk-line-rate_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

You can use the Node Tuning Operator to configure isolated CPUs, hugepages, and a topology scheduler. You can then use the Node Tuning Operator with Single Root I/O Virtualization (SR-IOV) to achieve a specific Data Plane Development Kit (DPDK) line rate.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You have installed the SR-IOV Network Operator.
* You have logged in as a user with `cluster-admin` privileges.
* You have deployed a standalone Node Tuning Operator.

  Note

  In previous versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator.

**Procedure**

1. Create a `PerformanceProfile` object based on the following example:

   ```
   apiVersion: performance.openshift.io/v2
   kind: PerformanceProfile
   metadata:
     name: performance
   spec:
     globallyDisableIrqLoadBalancing: true
     cpu:
       isolated: 21-51,73-103
       reserved: 0-20,52-72
     hugepages:
       defaultHugepagesSize: 1G
       pages:
         - count: 32
           size: 1G
     net:
       userLevelNetworking: true
     numa:
       topologyPolicy: "single-numa-node"
     nodeSelector:
       node-role.kubernetes.io/worker-cnf: ""
   ```

   where:

   `metadata.name`
   :   Specifies the name of the performance profile.

   `spec.cpu.isolated`
   :   Specifies the CPUs that are isolated for the application workloads. If Hyper-Threading is enabled on the system, allocate the relevant symbolic links to the `isolated` and `reserved` CPU groups. If the system has multiple non-uniform memory access (NUMA) nodes, allocate CPUs from both NUMAs to both groups. You can also use the Performance Profile Creator for this task. For more information, see *Creating a performance profile*.

   `spec.cpu.reserved`
   :   Specifies the CPUs that are reserved for the operating system and Kubernetes system daemons. You can also specify a list of devices that will have their queues set to the reserved CPU count. For more information, see *Reducing NIC queues using the Node Tuning Operator*.

   `spec.hugepages.defaultHugepagesSize`
   :   Specifies the default size of hugepages.

   `spec.hugepages.pages`
   :   Specifies the number and size of hugepages to allocate. You can specify the NUMA configuration for the hugepages. By default, the system allocates an even number to every NUMA node on the system.

   `spec.net.userLevelNetworking`
   :   Specifies whether to enable user-level networking. Set to `true` for DPDK workloads.

   `spec.numa.topologyPolicy`
   :   Specifies the NUMA topology policy. Set to `single-numa-node` to ensure that all resources are allocated from the same NUMA node.

   `spec.nodeSelector`
   :   Specifies the node selector label for nodes that this performance profile applies to.
2. Save the `yaml` file as `mlx-dpdk-perfprofile-policy.yaml`.
3. Apply the performance profile using the following command:

   ```
   $ oc create -f mlx-dpdk-perfprofile-policy.yaml
   ```

#### [10.6.1. DPDK library for use with container applications](#nw-sriov-app-netutil_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

An [optional library](https://github.com/openshift/app-netutil), `app-netutil`, provides several API methods for gathering network information about a pod from within a container running within that pod.

This library can assist with integrating SR-IOV virtual functions (VFs) in Data Plane Development Kit (DPDK) mode into the container. The library provides both a Golang API and a C API.

Currently there are three API methods implemented:

`GetCPUInfo()`
:   This function determines which CPUs are available to the container and returns the list.

`GetHugepages()`
:   This function determines the amount of huge page memory requested in the `Pod` spec for each container and returns the values.

`GetInterfaces()`
:   This function determines the set of interfaces in the container and returns the list. The return value includes the interface type and type-specific data for each interface.

The repository for the library includes a sample Dockerfile to build a container image, `dpdk-app-centos`. The container image can run one of the following DPDK sample applications, depending on an environment variable in the pod specification: `l2fwd`, `l3wd` or `testpmd`. The container image provides an example of integrating the `app-netutil` library into the container image itself. The library can also integrate into an init container. The init container can collect the required data and pass the data to an existing DPDK workload.

#### [10.6.2. Example SR-IOV Network Operator for virtual functions](#nw-sriov-network-operator_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

You can use the Single Root I/O Virtualization (SR-IOV) Network Operator to allocate and configure Virtual Functions (VFs) from SR-IOV-supporting Physical Function NICs on the nodes.

For more information on deploying the Operator, see *Installing the SR-IOV Network Operator*. For more information on configuring an SR-IOV network device, see *Configuring an SR-IOV network device*.

There are some differences between running Data Plane Development Kit (DPDK) workloads on Intel VFs and Mellanox VFs. This section provides object configuration examples for both VF types. The following is an example of an `sriovNetworkNodePolicy` object used to run DPDK applications on Intel NICs:

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-1
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  needVhostNet: true
  nicSelector:
    pfNames: ["ens3f0"]
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numVfs: 10
  priority: 99
  resourceName: dpdk_nic_1
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-1
  namespace: openshift-sriov-network-operator
spec:
  deviceType: vfio-pci
  needVhostNet: true
  nicSelector:
    pfNames: ["ens3f1"]
  nodeSelector:
  node-role.kubernetes.io/worker-cnf: ""
  numVfs: 10
  priority: 99
  resourceName: dpdk_nic_2
```

where:

`spec.deviceType`
:   For Intel NICs, `deviceType` must be `vfio-pci`.

`spec.needVhostNet`
:   If kernel communication with DPDK workloads is required, set to `true`. This mounts the `/dev/net/tun` and `/dev/vhost-net` devices into the container so the application can create a tap device and connect the tap device to the DPDK workload.

The following is an example of an `sriovNetworkNodePolicy` object for Mellanox NICs:

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-1
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: true
  nicSelector:
    rootDevices:
      - "0000:5e:00.1"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numVfs: 5
  priority: 99
  resourceName: dpdk_nic_1
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: dpdk-nic-2
  namespace: openshift-sriov-network-operator
spec:
  deviceType: netdevice
  isRdma: true
  nicSelector:
    rootDevices:
      - "0000:5e:00.0"
  nodeSelector:
    node-role.kubernetes.io/worker-cnf: ""
  numVfs: 5
  priority: 99
  resourceName: dpdk_nic_2
```

where:

`spec.deviceType`
:   For Mellanox devices the `deviceType` must be `netdevice`.

`spec.isRdma`
:   For Mellanox devices `isRdma` must be `true`. Mellanox cards are connected to DPDK applications using Flow Bifurcation. This mechanism splits traffic between Linux user space and kernel space, and can enhance line rate processing capability.

#### [10.6.3. Example SR-IOV network operator](#nw-sriov-create-object_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

The following is an example definition of an `sriovNetwork` object. In this case, Intel and Mellanox configurations are identical:

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: dpdk-network-1
  namespace: openshift-sriov-network-operator
spec:
  ipam: '{"type": "host-local","ranges": [[{"subnet": "10.0.1.0/24"}]],"dataDir":
   "/run/my-orchestrator/container-ipam-state-1"}'
  networkNamespace: dpdk-test
  spoofChk: "off"
  trust: "on"
  resourceName: dpdk_nic_1
---
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetwork
metadata:
  name: dpdk-network-2
  namespace: openshift-sriov-network-operator
spec:
  ipam: '{"type": "host-local","ranges": [[{"subnet": "10.0.2.0/24"}]],"dataDir":
   "/run/my-orchestrator/container-ipam-state-1"}'
  networkNamespace: dpdk-test
  spoofChk: "off"
  trust: "on"
  resourceName: dpdk_nic_2
```

* You can use a different IP Address Management (IPAM) implementation, such as Whereabouts. For more information, see *Dynamic IP address assignment configuration with Whereabouts*.
* You must request the `networkNamespace` where the network attachment definition will be created. You must create the `sriovNetwork` CR under the `openshift-sriov-network-operator` namespace.
* The `resourceName` value must match that of the `resourceName` created under the `sriovNetworkNodePolicy`.

#### [10.6.4. Example DPDK base workload](#nw-sriov-dpdk-base-workload_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

The following is an example of a Data Plane Development Kit (DPDK) container:

```
apiVersion: v1
kind: Namespace
metadata:
  name: dpdk-test
---
apiVersion: v1
kind: Pod
metadata:
  annotations:
    k8s.v1.cni.cncf.io/networks: '[
     {
      "name": "dpdk-network-1",
      "namespace": "dpdk-test"
     },
     {
      "name": "dpdk-network-2",
      "namespace": "dpdk-test"
     }
   ]'
    irq-load-balancing.crio.io: "disable"
    cpu-load-balancing.crio.io: "disable"
    cpu-quota.crio.io: "disable"
  labels:
    app: dpdk
  name: testpmd
  namespace: dpdk-test
spec:
  runtimeClassName: performance-performance
  containers:
    - command:
        - /bin/bash
        - -c
        - sleep INF
      image: registry.redhat.io/openshift4/dpdk-base-rhel8
      imagePullPolicy: Always
      name: dpdk
      resources:
        limits:
          cpu: "16"
          hugepages-1Gi: 8Gi
          memory: 2Gi
        requests:
          cpu: "16"
          hugepages-1Gi: 8Gi
          memory: 2Gi
      securityContext:
        capabilities:
          add:
            - IPC_LOCK
            - SYS_RESOURCE
            - NET_RAW
            - NET_ADMIN
        runAsUser: 0
      volumeMounts:
        - mountPath: /mnt/huge
          name: hugepages
  terminationGracePeriodSeconds: 5
  volumes:
    - emptyDir:
        medium: HugePages
      name: hugepages
```

* Request the SR-IOV networks you need. Resources for the devices are injected automatically.
* Disable the CPU and IRQ load balancing base. See *Disabling interrupt processing for individual pods* for more information.
* Set the `runtimeClass` to `performance-performance`. Do not set the `runtimeClass` to `HostNetwork` or `privileged`.
* Request an equal number of resources for requests and limits to start the pod with `Guaranteed` Quality of Service (QoS).

Note

Do not start the pod with `SLEEP` and then exec into the pod to start the testpmd or the DPDK workload. This can add additional interrupts as the `exec` process is not pinned to any CPU.

#### [10.6.5. Example testpmd script](#nw-sriov-dpdk-running-testpmd_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

The following is an example script for running `testpmd`:

```
#!/bin/bash
set -ex
export CPU=$(cat /sys/fs/cgroup/cpuset/cpuset.cpus)
echo ${CPU}

dpdk-testpmd -l ${CPU} -a ${PCIDEVICE_OPENSHIFT_IO_DPDK_NIC_1} -a ${PCIDEVICE_OPENSHIFT_IO_DPDK_NIC_2} -n 4 -- -i --nb-cores=15 --rxd=4096 --txd=4096 --rxq=7 --txq=7 --forward-mode=mac --eth-peer=0,50:00:00:00:00:01 --eth-peer=1,50:00:00:00:00:02
```

This example uses two different `sriovNetwork` CRs. The environment variable contains the Virtual Function (VF) PCI address that was allocated for the pod. If you use the same network in the pod definition, you must split the `pciAddress`. It is important to configure the correct MAC addresses of the traffic generator. This example uses custom MAC addresses.

### [10.7. Using a virtual function in RDMA mode with a Mellanox NIC](#example-vf-use-in-rdma-mode-mellanox_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

Important

RDMA over Converged Ethernet (RoCE) is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

RDMA over Converged Ethernet (RoCE) is the only supported mode when using RDMA on OpenShift Container Platform.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Install the SR-IOV Network Operator.
* Log in as a user with `cluster-admin` privileges.

**Procedure**

1. Create the following `SriovNetworkNodePolicy` object, and then save the YAML in the `mlx-rdma-node-policy.yaml` file.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: mlx-rdma-node-policy
     namespace: openshift-sriov-network-operator
   spec:
     resourceName: mlxnics
     nodeSelector:
       feature.node.kubernetes.io/network-sriov.capable: "true"
     priority: <priority>
     numVfs: <num>
     nicSelector:
       vendor: "15b3"
       deviceID: "1015"
       pfNames: ["<pf_name>", ...]
       rootDevices: ["<pci_bus_id>", "..."]
     deviceType: netdevice
     isRdma: true
   ```

   where:

   `spec.nicSelector.deviceID`
   :   Specifies the device hex code of the SR-IOV network device.

   `spec.deviceType`
   :   Specifies the driver type for the virtual functions. Set to `netdevice` for Mellanox NICs.

   `spec.isRdma`
   :   Set to `true` to enable RDMA mode.

       Note

       See the `Configuring SR-IOV network devices` section for a detailed explanation on each option in `SriovNetworkNodePolicy`.

       When applying the configuration specified in a `SriovNetworkNodePolicy` object, the SR-IOV Operator might drain the nodes, and in some cases, reboot nodes. It might take several minutes for a configuration change to apply. Ensure that there are enough available nodes in your cluster to handle the evicted workload beforehand.

       After the configuration update is applied, all the pods in the `openshift-sriov-network-operator` namespace will change to a `Running` status.
2. Create the `SriovNetworkNodePolicy` object by running the following command:

   ```
   $ oc create -f mlx-rdma-node-policy.yaml
   ```
3. Create the following `SriovNetwork` object, and then save the YAML in the `mlx-rdma-network.yaml` file.

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetwork
   metadata:
     name: mlx-rdma-network
     namespace: openshift-sriov-network-operator
   spec:
     networkNamespace: <target_namespace>
     ipam: |-
   # ...
     vlan: <vlan>
     resourceName: mlxnics
   ```

   where:

   `spec.ipam`
   :   Specifies a configuration object for the IPAM CNI plugin as a YAML block scalar. The plugin manages IP address assignment for the attachment definition.

       Note

       See the "Configuring SR-IOV additional network" section for a detailed explanation on each option in `SriovNetwork`.

       An optional library, app-netutil, provides several API methods for gathering network information about a container’s parent pod.
4. Create the `SriovNetworkNodePolicy` object by running the following command:

   ```
   $ oc create -f mlx-rdma-network.yaml
   ```
5. Create the following `Pod` spec, and then save the YAML in the `mlx-rdma-pod.yaml` file.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: rdma-app
     namespace: <target_namespace>
     annotations:
       k8s.v1.cni.cncf.io/networks: mlx-rdma-network
   spec:
     containers:
     - name: testpmd
       image: <RDMA_image>
       securityContext:
         runAsUser: 0
         capabilities:
           add: ["IPC_LOCK","SYS_RESOURCE","NET_RAW"]
       volumeMounts:
       - mountPath: /mnt/huge
         name: hugepage
       resources:
         limits:
           memory: "1Gi"
           cpu: "4"
           hugepages-1Gi: "4Gi"
         requests:
           memory: "1Gi"
           cpu: "4"
           hugepages-1Gi: "4Gi"
       command: ["sleep", "infinity"]
     volumes:
     - name: hugepage
       emptyDir:
         medium: HugePages
   ```

   where:

   `metadata.namespace`
   :   Specifies the same namespace where `SriovNetwork` object `mlx-rdma-network` is created. If you want to create the pod in a different namespace, change `target_namespace` in both the `Pod` spec and the `SriovNetwork` object.

   `spec.containers.image`
   :   Specifies the RDMA image which includes your application and the RDMA library used by the application.

   `spec.containers.securityContext.capabilities.add`
   :   Specifies additional capabilities required by the application inside the container for hugepage allocation, system resource allocation, and network interface access.

   `spec.containers.volumeMounts.mountPath`
   :   Specifies the path where the hugepage volume is mounted in the RDMA pod. The hugepage volume is backed by the `emptyDir` volume type with the medium being `HugePages`.

   `spec.containers.resources.limits.cpu`
   :   Specifies the number of CPUs. The RDMA pod usually requires exclusive CPUs be allocated from the kubelet. This is achieved by setting CPU Manager policy to `static` and creating a pod with `Guaranteed` QoS.

   `spec.containers.resources.limits.hugepages-1Gi`
   :   Specifies the hugepage size (`hugepages-1Gi` or `hugepages-2Mi`) and the quantity of hugepages that will be allocated to the RDMA pod. Configure `2Mi` and `1Gi` hugepages separately. Configuring `1Gi` hugepage requires adding kernel arguments to Nodes.
6. Create the RDMA pod by running the following command:

   ```
   $ oc create -f mlx-rdma-pod.yaml
   ```

### [10.8. A test pod template for clusters that use OVS-DPDK on OpenStack](#nw-openstack-ovs-dpdk-testpmd-pod_using-dpdk-and-rdma) Copy linkLink copied to clipboard!

The following `testpmd` pod demonstrates container creation with huge pages, reserved CPUs, and the SR-IOV port.

**An example `testpmd` pod**

```
apiVersion: v1
kind: Pod
metadata:
  name: testpmd-dpdk
  namespace: mynamespace
  annotations:
    cpu-load-balancing.crio.io: "disable"
    cpu-quota.crio.io: "disable"
# ...
spec:
  containers:
  - name: testpmd
    command: ["sleep", "99999"]
    image: registry.redhat.io/openshift4/dpdk-base-rhel8:v4.9
    securityContext:
      capabilities:
        add: ["IPC_LOCK","SYS_ADMIN"]
      privileged: true
      runAsUser: 0
    resources:
      requests:
        memory: 1000Mi
        hugepages-1Gi: 1Gi
        cpu: '2'
        openshift.io/dpdk1: 1
      limits:
        hugepages-1Gi: 1Gi
        cpu: '2'
        memory: 1000Mi
        openshift.io/dpdk1: 1
    volumeMounts:
      - mountPath: /mnt/huge
        name: hugepage
        readOnly: False
  runtimeClassName: performance-cnf-performanceprofile
  volumes:
  - name: hugepage
    emptyDir:
      medium: HugePages
```

* The name `dpdk1` in this example is a user-created `SriovNetworkNodePolicy` resource. You can substitute this name for that of a resource that you create.
* If your performance profile is not named `cnf-performance profile`, replace that string with the correct performance profile name.

## [Chapter 11. High availability for pod-level bonds on SR-IOV networks](#sriov-lacp-sriov) Copy linkLink copied to clipboard!

For workloads by using pod-level bonding with SR-IOV virtual functions (VFs), despite an upstream switch failure, an underlying physical function (PF) might still report an `up` state. This creates a silent failure, as attached VFs remain up and pods continue to send traffic to a dead endpoint, causing packet loss.

The PF Status Relay Operator solves this issue by using Link Aggregation Control Protocol (LACP) as an active health check. In this configuration, each physical function (PF) is in its own single-member LACP bond with the upstream switch. When the Operator detects an LACP failure on a PF bond, it changes the link state of the attached VFs from `auto` to `disabled`. This action triggers the pod’s `active-backup` bond to fail over to its backup network path, maintaining high availability.

Important

Configuring LACP state monitoring for SR-IOV networks is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

### [11.1. Installing the PF Status Relay Operator using the CLI](#installing-pfsr-cli_sriov-lacp-sriov) Copy linkLink copied to clipboard!

Install the PF Status Relay Operator to enable OpenShift Container Platform to use Link Aggregation Control Protocol (LACP) as an active health check on physical functions.

**Prerequisites**

* You configured LACP on your upstream switch.
* You configured pod-level bonding for your SR-IOV networks.
* You installed the OpenShift CLI (`oc`).
* You have cluster-admin privileges.

**Procedure**

1. Create the `openshift-pf-status-relay-operator` namespace by entering the following command:

   ```
   $ cat << EOF| oc create -f -
   apiVersion: v1
   kind: Namespace
   metadata:
     name: openshift-pf-status-relay-operator
     annotations:
       workload.openshift.io/allowed: management
   EOF
   ```
2. Create an `OperatorGroup` custom resource (CR) by entering the following command:

   ```
   $ cat << EOF| oc create -f -
   apiVersion: operators.coreos.com/v1
   kind: OperatorGroup
   metadata:
     name: pf-status-relay-operators
     namespace: openshift-pf-status-relay-operator
   spec:
     targetNamespaces:
     - openshift-pf-status-relay-operator
   EOF
   ```
3. Create a `Subscription` CR for the PF Status Relay Operator by entering the following command:

   ```
   $ cat << EOF| oc create -f -
   apiVersion: operators.coreos.com/v1alpha1
   kind: Subscription
   metadata:
     name: pf-status-relay-operator-subscription
     namespace: openshift-pf-status-relay-operator
   spec:
     channel: stable
     name: pf-status-relay-operator
     source: redhat-operators
     sourceNamespace: openshift-marketplace
   EOF
   ```

**Verification**

* To verify that the Operator is installed, enter the following command and then check that output shows `Succeeded` for the Operator:

  ```
  $ oc get csv -n openshift-pf-status-relay-operator -o custom-columns=Name:.metadata.name,Phase:.status.phase
  ```

### [11.2. Installing the PF Status Relay Operator using the web console](#installing-pfsr-console_sriov-lacp-sriov) Copy linkLink copied to clipboard!

Install the PF Status Relay Operator to enable OpenShift Container Platform to use Link Aggregation Control Protocol (LACP) as an active health check on physical functions.

**Prerequisites**

* You configured LACP on your upstream switch.
* You configured pod-level bonding for your SR-IOV networks.
* You have cluster-admin privileges.

**Procedure**

1. Install the PF Status Relay Operator:

   1. In the OpenShift Container Platform web console, click **Ecosystem** → **Software Catalog**.
   2. Select **PF Status Relay Operator** from the list of available Operators, and then click **Install**.
   3. On the **Install Operator** page, under **Installed Namespace**, select **Operator recommended Namespace**.
   4. Click **Install**.

**Verification**

* Verify that the PF Status Relay Operator shows the **Status** as **Succeeded** on the Installed Operators dashboard.

### [11.3. Configuring the PF Status Relay Operator for LACP state monitoring on SR-IOV networks](#configuring-lacp-sriov_sriov-lacp-sriov) Copy linkLink copied to clipboard!

Use the PF Status Relay Operator to enable Link Aggregation Control Protocol (LACP) state monitoring for workloads by using pod-level bonding with SR-IOV networks. The Operator monitors the LACP state on physical functions (PF) and changes the link state for attached virtual functions (VF) when it detects an upstream failure. With this approach, you can detect failures on VFs attached to a PF to ensure a timely failover to a backup network path, ensuring high availability for your workloads.

The following scenario demonstrates how to configure and verify LACP state monitoring for SR-IOV networks:

* Create host-level NIC bonds on worker nodes and configure LACP.
* Define SR-IOV network policies to create virtual functions (VFs) on the bonded interfaces.
* Deploy the PF Status Relay Operator to monitor physical functions and the LACP state.
* Verify that pods using these VFs automatically fail over to a backup network path in case of upstream switch failure.

The following scenario demonstrates how to configure and verify LACP state monitoring for SR-IOV networks. This scenario uses SR-IOV network cards with two ports on each node, `worker-0` and `worker-1`, with both ports connected to a shared switch to support LACP bonding.

**Prerequisites**

* Nodes must have a NIC that supports SR-IOV.
* The SR-IOV Network Operator is installed.
* The PF Status Relay Operator is installed.
* The physical switch ports connected to the worker nodes are configured for LACP with a fast polling rate.
* The `linkState` is set to `auto` or `disable` for the SR-IOV VFs that you want to monitor. The Operator ignores VFs with the `linkState` set to `enable`. The default value for SR-IOV VFs is `linkState: auto`.

**Procedure**

1. Create the project namespace by creating a `namespace.yaml` file such as the following example:

   **Example `namespace.yaml` file**

   ```
   apiVersion: v1
   kind: Namespace
   metadata:
     labels:
       kubernetes.io/metadata.name: sriov-operator-tests
       pod-security.kubernetes.io/audit: privileged
       pod-security.kubernetes.io/enforce: privileged
       pod-security.kubernetes.io/warn: privileged
       security.openshift.io/scc.podSecurityLabelSync: "false"
     name: <namespace>
   ```

   * `<namespace>` specifies the namespace where you deploy the high-availability pod.
2. Apply the namespace by running the following command:

   ```
   $ oc apply -f namespace.yaml
   ```
3. Configure host-level LACP bonds:

   1. Create a YAML file that defines the `NodeNetworkConfigurationPolicy` resource for the `ens5f0` interface on the `worker-0` node:

      **Example `nncpBondF0Worker0.yaml` file**

      ```
      apiVersion: nmstate.io/v1
      kind: NodeNetworkConfigurationPolicy
      metadata:
        name: example-bond-f0
      spec:
        nodeSelector:
          kubernetes.io/hostname: <node_name>
        desiredState:
          interfaces:
            - name: example-bond-f0
              description: example-bond-f0
              type: bond
              state: up
              mtu: 9216
              link-aggregation:
                mode: 802.3ad
                options:
                  miimon: '100'
                  lacp_rate: 'fast'
                  min_links: '1'
                port:
                  - <pf_name>
            - name: ens5f0
              type: ethernet
              state: up
              mtu: 9216
      ```

      * `<node_name>` specifies the node where the bonded interface is created.
      * `mode: 802.3ad` sets the LACP mode to enable LACP on the bond.
      * `lacp_rate: 'fast'` sets the LACP rate on the interface. You must also set the rate to `fast` on the switch. The `fast` rate sends LACP packets every second.
      * `<pf_name>` specifies the PF that you want to include in the bond.
   2. Create a YAML file that defines the `NodeNetworkConfigurationPolicy` resource for the `ens5f1` interface on the `worker-0` node:

      **Example `nncpBondF1Worker0.yaml` file**

      ```
      apiVersion: nmstate.io/v1
      kind: NodeNetworkConfigurationPolicy
      metadata:
        name: example-bond-f1
      spec:
        nodeSelector:
          kubernetes.io/hostname: <node_name>
        desiredState:
          interfaces:
            - name: example-bond-f1
              description: example-bond-f1
              type: bond
              state: up
              mtu: 9216
              link-aggregation:
                mode: 802.3ad
                options:
                  miimon: '100'
                  lacp_rate: 'fast'
                  min_links: '1'
                port:
                  - <pf_name>
            - name: ens5f1
              type: ethernet
              state: up
              mtu: 9216
      ```

      * `<node_name>` specifies the node where the bonded interface is created.
      * `mode: 802.3ad` sets the LACP mode to enable LACP on the bond.
      * `lacp_rate: 'fast'` sets the LACP rate on the interface. You must also set the rate to `fast` on the switch. The `fast` rate sends LACP packets every second.
      * `<pf_name>` specifies the PF that you want to include in the bond.
   3. Apply the resources by running the following commands:

      ```
      $ oc apply -f nncpBondF0Worker0.yaml
      $ oc apply -f nncpBondF1Worker0.yaml
      ```
4. Create SR-IOV network VFs for the bonded interfaces:

   1. Create a YAML file that defines the `SriovNetworkNodePolicy` resource for the `ens5f0` interface on the `worker-0` node:

      **Example `sriovnetworkpolicy-port1.yaml` file**

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetworkNodePolicy
      metadata:
        name: sriovnetpolicy-port-0
        namespace: openshift-sriov-network-operator
      spec:
        deviceType: netdevice
        nicSelector:
          pfNames:
            - <pf_name>
        nodeSelector:
          kubernetes.io/hostname: <node_name>
        numVfs: <num_vfs>
        priority: 99
        resourceName: <resource_name>
      ```

      * `<pf_name>` specifies the PF to create the VFs from.
      * `<node_name>` specifies the node where the VFs are created.
      * `<num_vfs>` specifies the number of VFs to create on the PF.
      * `<resource_name>` specifies the resource name used by pods to request these VFs.
   2. Create a YAML file that defines the `SriovNetworkNodePolicy` resource for the `ens5f1` interface on the `worker-0` node:

      **Example `sriovnetworkpolicy-port2.yaml` file**

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetworkNodePolicy
      metadata:
        name: sriovnetpolicy-port-1
        namespace: openshift-sriov-network-operator
      spec:
        deviceType: netdevice
        nicSelector:
          pfNames:
            - <pf_name>
        nodeSelector:
          kubernetes.io/hostname: <node_name>
        numVfs: <num_vfs>
        priority: 99
        resourceName: <resource_name>
      ```

      * `<pf_name>` specifies the PF to create the VFs from.
      * `<node_name>` specifies the node where the VFs are created.
      * `<num_vfs>` specifies the number of VFs to create on the PF.
      * `<resource_name>` specifies the resource name used by pods to request these VFs.
   3. Apply the resources by running the following commands:

      ```
      $ oc apply -f sriovnetworkpolicy-port1.yaml
      $ oc apply -f sriovnetworkpolicy-port2.yaml
      ```
5. Configure the PF Status Relay Operator:

   1. Create a YAML file that defines the `PFLACPMonitor` resource. This example file configures the Operator to monitor the LACP status of `ens5f0` and `ens5f1` bonded interfaces on the `worker-0` node:

      **Example `pflacpmonitor.yaml` file**

      ```
      apiVersion: pfstatusrelay.openshift.io/v1alpha1
      kind: PFLACPMonitor
      metadata:
        namespace: openshift-pf-status-relay-operator
        labels:
          app.kubernetes.io/name: pf-status-relay-operator
        name: pflacpmonitor-worker-0
      spec:
        interfaces:
          - <pf_name>
          - <pf_name>
        pollingInterval: <polling_interval>
        nodeSelector:
          kubernetes.io/hostname: <node_name>
      ```

      * `<pf_name>` specifies the physical functions to monitor.
      * `<polling_interval>` specifies the polling interval in milliseconds to check the LACP status on the monitored interfaces. The minimum value is `1000`.
      * `<node_name>` specifies the node for the target interfaces.

      Important

      Use only one `PFLACPMonitor` custom resource to monitor each network interface on a node. If you create multiple resources that target the same interface, the PF Status Relay Operator will not process the conflicting configurations.
   2. Apply the `PFLACPMonitor` resource by running the following command:

      ```
      $ oc apply -f pflacpmonitor.yaml
      ```

**Verification**

1. Check the logs of the PF Status Relay Operator to verify that it is monitoring the LACP state:

   ```
   $ oc logs -n openshift-pf-status-relay-operator <pf_status_relay_operator_pod_name>
   ```

   **Example output**

   ```
   {"time":"2025-07-24T13:35:54.653201692Z","level":"INFO","msg":"lacp is up","interface":"ens5f0"}
   {"time":"2025-07-24T13:35:54.65347273Z","level":"INFO","msg":"vf link state was set","id":0,"state":"auto","interface":"ens5f0"}
   ...
   ```
2. Apply the `SriovNetwork` resources to make the VFs available for use within the `sriov-operator-tests` namespace:

   1. Create a YAML file that defines the `SriovNetwork` resource for the VFs created on `ens5f0`:

      **Example `sriovnetwork-port1.yaml` file**

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetwork
      metadata:
        name: sriovnetwork-port0
        namespace: openshift-sriov-network-operator
      spec:
        capabilities: '{ "mac": true }'
        networkNamespace: sriov-operator-tests
        resourceName: resourceport0
      ```
   2. Create a YAML file that defines the `SriovNetwork` resource for the VFs created on `ens5f1`:

      **Example `sriovnetwork-port2.yaml` file**

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetwork
      metadata:
        name: sriovnetwork-port1
        namespace: openshift-sriov-network-operator
      spec:
        capabilities: '{ "mac": true }'
        networkNamespace: sriov-operator-tests
        resourceName: resourceport1
      ```
   3. Apply the resources by running the following commands:

      ```
      $ oc apply -f sriovnetwork-port1.yaml
      $ oc apply -f sriovnetwork-port2.yaml
      ```
3. Define a high-availability pod that uses the SR-IOV VFs:

   1. Apply the `NetworkAttachmentDefinition` resource to create an `active-backup` bond using the two SR-IOV networks:

      **Example `nad-bond.yaml` file**

      ```
      apiVersion: k8s.cni.cncf.io/v1
      kind: NetworkAttachmentDefinition
      metadata:
        name: nad-bond-1
        namespace: sriov-operator-tests
      spec:
        config: |-
          {"type": "bond", "cniVersion": "0.3.1", "name": "bond-net1",
          "mode": "active-backup", "failOverMac": 1, "linksInContainer": true, "miimon": "100", "mtu": 1450,
          "links": [{"name": "net1"},{"name": "net2"}], "capabilities": {"ips": true}, "ipam": {"type": "static"}}
      ```

      * `linksInContainer: true` creates the bond inside the pod’s network namespace.
      * `mode: active-backup` configures the bond to use active-backup mode.
      * `links` specifies the pod-level interfaces to include in the bond.

        Important

        The PF Status Relay Operator provides LACP state monitoring for pod-level bonding with the `mode: active-backup` configuration only.
   2. Apply the `NetworkAttachmentDefinition` resource by running the following command:

      ```
      $ oc apply -f nad-bond.yaml
      ```
   3. Create a YAML file that defines the `Pod` resource that uses the VFs from the bonded interfaces in active-backup mode:

      **Example `client-bond.yaml` file**

      ```
      apiVersion: v1
      kind: Pod
      metadata:
        name: client-bond
        namespace: sriov-operator-tests
        annotations:
          k8s.v1.cni.cncf.io/networks: |-
            [{
                "name": "sriovnetwork-port0",
                "interface": "net1",
                "mac": "<mac_address>"
              },{
                "name": "sriovnetwork-port1",
                "interface": "net2",
                "mac": "<mac_address>"
              },{
                "name": "nad-bond-1",
                "interface": "bond0",
                "ips": ["192.168.10.254/24","2001:100::254/64"],
                "mac": "<mac_address>"
            }]
      spec:
        nodeName: worker-0
        containers:
          - name: client-bond
            image: quay.io/nginx/nginx-unprivileged
            imagePullPolicy: IfNotPresent
            command: ["/bin/sh", "-c", "sleep 3650d"]
            securityContext:
              privileged: true
            command: ["/bin/sleep", "3650d"]
      ```

      * The `k8s.v1.cni.cncf.io/networks` annotation requests three networks: two SR-IOV VFs, `net1` and `net2`, and one bond, `bond0`, which uses them.
   4. Apply the `Pod` resource by running the following command:

      ```
      $ oc apply -f client-bond.yaml
      ```
4. Check that the failover mechanism:

   1. Log in to the `client-bond` pod by running the following command:

      ```
      $ oc rsh -n sriov-operator-tests client-bond
      ```
   2. Check the initial status of the pod-level bond by running the following command:

      ```
      sh-4.4# cat /proc/net/bonding/bond0
      ```

      **Example output**

      ```
      [root@client-bond-tlb /]# cat /proc/net/bonding/bond0
      ...

      Bonding Mode: transmit load balancing
      Transmit Hash Policy: layer2 (0)
      Primary Slave: None
      Currently Active Slave: net1
      MII Status: up
      MII Polling Interval (ms): 100
      Up Delay (ms): 0
      Down Delay (ms): 0
      Peer Notification Delay (ms): 0

      Slave Interface: net1
      MII Status: up
      Speed: 25000 Mbps
      Duplex: full
      Link Failure Count: 0
      Permanent HW addr: AA:BB:CC:DD:EE:FF
      Slave queue ID: 0

      Slave Interface: net2
      MII Status: up
      Speed: 25000 Mbps
      Duplex: full
      Link Failure Count: 0
      Permanent HW addr: BB:CC:DD:EE:FF:GG
      ```

      * Both `net1` and `net2` interfaces are up.
   3. Exit the pod shell.
   4. Simulate an LACP failure on your upstream physical switch. To simulate this scenario, you can filter LACP traffic on the switch port that you want to test the failure on. This ensures that the physical link remains up while the LACP polling fails. The command to do this is vendor-dependent.
   5. Verify the failover inside the pod by logging back into the `client-bond` pod and checking the bond status again:

      ```
      sh-4.4# cat /proc/net/bonding/bond0
      ```

      **Example output**

      ```
      ...

      Bonding Mode: transmit load balancing
      Transmit Hash Policy: layer2 (0)
      Primary Slave: None
      Currently Active Slave: net2
      MII Status: up
      MII Polling Interval (ms): 100
      Up Delay (ms): 0
      Down Delay (ms): 0
      Peer Notification Delay (ms): 0

      Slave Interface: net1
      MII Status: down
      Speed: Unknown
      Duplex: Unknown
      Link Failure Count: 1
      Permanent HW addr: AA:BB:CC:DD:EE:FF
      Slave queue ID: 0

      Slave Interface: net2
      MII Status: up
      Speed: 25000 Mbps
      Duplex: full
      Link Failure Count: 0
      Permanent HW addr: BB:CC:DD:EE:FF:GG
      Slave queue ID: 0
      ```

      * The `net1` interface is down, and the `net2` interface is now the active interface.

        The client-bond pod detects the link state change and switches to the backup network path.

## [Chapter 12. Using pod-level bonding](#using-pod-level-bonding) Copy linkLink copied to clipboard!

Bonding at the pod level is vital to enable workloads inside pods that require high availability and more throughput. With pod-level bonding, you can create a bond interface from multiple single root I/O virtualization (SR-IOV) virtual function interfaces in a kernel mode interface. The SR-IOV virtual functions are passed into the pod and attached to a kernel driver.

One scenario where pod level bonding is required is creating a bond interface from multiple SR-IOV virtual functions on different physical functions. Creating a bond interface from two different physical functions on the host can be used to achieve high availability and throughput at pod level.

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

For guidance on tasks such as creating a SR-IOV network, network policies, network attachment definitions and pods, see [Configuring an SR-IOV network device](#configuring-sriov-device "Chapter 2. Configuring an SR-IOV network device").

### [12.1. Configuring a bond interface from two SR-IOV interfaces](#nw-sriov-cfg-bond-interface-with-virtual-functions_using-pod-level-bonding) Copy linkLink copied to clipboard!

Bonding enables multiple network interfaces to be aggregated into a single logical "bonded" interface. Bond Container Network Interface (Bond-CNI) brings bond capability into containers.

Bond-CNI can be created by using Single Root I/O Virtualization (SR-IOV) virtual functions and placing them in the container network namespace.

OpenShift Container Platform only supports Bond-CNI by using SR-IOV virtual functions. The SR-IOV Network Operator provides the SR-IOV CNI plugin needed to manage the virtual functions. Other CNI plugins or types of interfaces are not supported.

### [12.2. Creating a bond network attachment definition](#nw-sriov-creating-bond-network-attachment-definition_using-pod-level-bonding) Copy linkLink copied to clipboard!

After the SR-IOV virtual functions are available, you can create a bond network attachment definition.

The following YAML example shows a bond network attachment definition:

```
apiVersion: "k8s.cni.cncf.io/v1"
    kind: NetworkAttachmentDefinition
    metadata:
      name: bond-net1
      namespace: demo
    spec:
      config: '{
      "type": "bond",
      "cniVersion": "0.3.1",
      "name": "bond-net1",
      "mode": "active-backup",
      "failOverMac": 1,
      "linksInContainer": true,
      "miimon": "100",
      "mtu": 1500,
      "links": [
            {"name": "net1"},
            {"name": "net2"}
        ],
      "ipam": {
            "type": "host-local",
            "subnet": "10.56.217.0/24",
            "routes": [{
            "dst": "0.0.0.0/0"
            }],
            "gateway": "10.56.217.1"
        }
      }'
```

* The `type` field is always set to `bond`.
* The `mode` field specifies the bonding mode.

  Note

  The supported bonding modes are:

  + `balance-rr` - 0
  + `active-backup` - 1
  + `balance-xor` - 2

  For `balance-rr` or `balance-xor` modes, you must set the `trust` mode to `on` for the SR-IOV virtual function.
* The `failOverMac` field is mandatory for active-backup mode and must be set to `1`.
* The `linksInContainer` field must be set to `true` to inform the Bond CNI that the required interfaces are inside the container. By default, Bond CNI looks for these interfaces on the host, which does not work for integration with SR-IOV and Multus.
* The `links` field defines which interfaces to use for the bond. By default, Multus names the attached interfaces as "net" plus a consecutive number, starting with one.

### [12.3. Creating a pod using a bond interface](#nw-sriov-creating-pod-using-bond-interface_using-pod-level-bonding) Copy linkLink copied to clipboard!

You can create a pod that uses a bond interface by applying a YAML configuration that references SR-IOV and bond network attachments.

**Prerequisites**

* The SR-IOV Network Operator must be installed and configured to obtain virtual functions in a container.
* To configure SR-IOV interfaces, an SR-IOV network and policy must be created for each interface.
* The SR-IOV Network Operator creates a network attachment definition for each SR-IOV interface, based on the SR-IOV network and policy defined.
* The `linkState` is set to the default value `auto` for the SR-IOV virtual function.

**Procedure**

1. Create a pod with a YAML file named for example `podbonding.yaml` with content similar to the following:

   ```
   apiVersion: v1
       kind: Pod
       metadata:
         name: bondpod1
         namespace: demo
         annotations:
           k8s.v1.cni.cncf.io/networks: demo/sriovnet1, demo/sriovnet2, demo/bond-net1
       spec:
         containers:
         - name: podexample
           image: quay.io/openshift/origin-network-interface-bond-cni:4.11.0
           command: ["/bin/bash", "-c", "sleep INF"]
   ```

   The network annotation has two SR-IOV network attachments and one bond network attachment. The bond attachment uses the two SR-IOV interfaces as bonded port interfaces.
2. Apply the YAML by running the following command:

   ```
   $ oc apply -f podbonding.yaml
   ```
3. Inspect the pod interfaces with the following command:

   ```
   $ oc rsh -n demo bondpod1
   sh-4.4#
   sh-4.4# ip a
   1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN qlen 1000
   link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
   inet 127.0.0.1/8 scope host lo
   valid_lft forever preferred_lft forever
   3: eth0@if150: <BROADCAST,MULTICAST,UP,LOWER_UP,M-DOWN> mtu 1450 qdisc noqueue state UP
   link/ether 62:b1:b5:c8:fb:7a brd ff:ff:ff:ff:ff:ff
   inet 10.244.1.122/24 brd 10.244.1.255 scope global eth0
   valid_lft forever preferred_lft forever
   4: net3: <BROADCAST,MULTICAST,UP,LOWER_UP400> mtu 1500 qdisc noqueue state UP qlen 1000
   link/ether 9e:23:69:42:fb:8a brd ff:ff:ff:ff:ff:ff
   inet 10.56.217.66/24 scope global bond0
   valid_lft forever preferred_lft forever
   43: net1: <BROADCAST,MULTICAST,UP,LOWER_UP800> mtu 1500 qdisc mq master bond0 state UP qlen 1000
   link/ether 9e:23:69:42:fb:8a brd ff:ff:ff:ff:ff:ff
   44: net2: <BROADCAST,MULTICAST,UP,LOWER_UP800> mtu 1500 qdisc mq master bond0 state UP qlen 1000
   link/ether 9e:23:69:42:fb:8a brd ff:ff:ff:ff:ff:ff
   ```

   * The bond interface is automatically named `net3`. To set a specific interface name, add the `@name` suffix to the pod’s `k8s.v1.cni.cncf.io/networks` annotation.
   * The `net1` interface is based on an SR-IOV virtual function.
   * The `net2` interface is based on an SR-IOV virtual function.

   Note

   If no interface names are configured in the pod annotation, interface names are assigned automatically as `net<n>`, with `<n>` starting at `1`.
4. Optional: If you want to set a specific interface name, for example `bond0`, edit the `k8s.v1.cni.cncf.io/networks` annotation and set `bond0` as the interface name as follows:

   ```
   annotations:
           k8s.v1.cni.cncf.io/networks: demo/sriovnet1, demo/sriovnet2, demo/bond-net1@bond0
   ```

## [Chapter 13. Configuring hardware offloading](#configuring-hardware-offloading) Copy linkLink copied to clipboard!

As a cluster administrator, you can configure hardware offloading on compatible nodes to increase data processing performance and reduce load on host CPUs.

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

### [13.1. About hardware offloading](#about-hardware-offloading_configuring-hardware-offloading) Copy linkLink copied to clipboard!

Open vSwitch hardware offloading is a method of processing network tasks by diverting them away from the CPU and offloading them to a dedicated processor on a network interface controller. As a result, clusters can benefit from faster data transfer speeds, reduced CPU workloads, and lower computing costs.

The key element for this feature is a modern class of network interface controllers known as SmartNICs. A SmartNIC is a network interface controller that is able to handle computationally-heavy network processing tasks. In the same way that a dedicated graphics card can improve graphics performance, a SmartNIC can improve network performance. In each case, a dedicated processor improves performance for a specific type of processing task.

In OpenShift Container Platform, you can configure hardware offloading for bare-metal nodes that have a compatible SmartNIC. Hardware offloading is configured and enabled by the SR-IOV Network Operator.

Hardware offloading is not compatible with all workloads or application types. Only the following two communication types are supported:

* pod-to-pod
* pod-to-service, where the service is a ClusterIP service backed by a regular pod

In all cases, hardware offloading takes place only when those pods and services are assigned to nodes that have a compatible SmartNIC. Suppose, for example, that a pod on a node with hardware offloading tries to communicate with a service on a regular node. On the regular node, all the processing takes place in the kernel, so the overall performance of the pod-to-service communication is limited to the maximum performance of that regular node. Hardware offloading is not compatible with DPDK applications.

Enabling hardware offloading on a node, but not configuring pods to use, it can result in decreased throughput performance for pod traffic. You cannot configure hardware offloading for pods that are managed by OpenShift Container Platform.

### [13.2. Supported devices](#supported_devices_configuring-hardware-offloading) Copy linkLink copied to clipboard!

Hardware offloading is supported on the following network interface controllers:

Expand

Table 13.1. Supported network interface controllers

| Manufacturer | Model | Vendor ID | Device ID |
| --- | --- | --- | --- |
| Mellanox | MT27800 Family [ConnectX‑5] | 15b3 | 1017 |
| Mellanox | MT28880 Family [ConnectX‑5 Ex] | 15b3 | 1019 |
| Mellanox | MT2892 Family [ConnectX‑6 Dx] | 15b3 | 101d |
| Mellanox | MT2894 Family [ConnectX-6 Lx] | 15b3 | 101f |
| Mellanox | MT42822 BlueField-2 in ConnectX-6 NIC mode | 15b3 | a2d6 |

Show more

### [13.3. Prerequisites](#configuring-hardware-offloading-prerequisites_configuring-hardware-offloading) Copy linkLink copied to clipboard!

Before you configure hardware offloading, ensure that the following conditions are met.

* Your cluster has at least one bare-metal machine with a network interface controller that is supported for hardware offloading.
* You installed the SR-IOV Network Operator.
* Your cluster uses the OVN-Kubernetes network plugin.
* In your OVN-Kubernetes network plugin configuration, the `gatewayConfig.routingViaHost` field is set to `false`.

### [13.4. Setting the SR-IOV Network Operator into systemd mode](#nw-sriov-hwol-configuring-systemd-mode_configuring-hardware-offloading) Copy linkLink copied to clipboard!

To support hardware offloading, you must first set the SR-IOV Network Operator into `systemd` mode.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You have access to the cluster as a user that has the `cluster-admin` role.

**Procedure**

1. Create a `SriovOperatorConfig` custom resource (CR) to deploy all the SR-IOV Operator components:

   1. Create a file named `sriovOperatorConfig.yaml` that contains the following YAML:

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovOperatorConfig
      metadata:
        name: default
        namespace: openshift-sriov-network-operator
      spec:
        enableInjector: true
        enableOperatorWebhook: true
        configurationMode: "systemd"
        logLevel: 2
      ```

      * The only valid name for the `SriovOperatorConfig` resource is `default` and it must be in the namespace where the Operator is deployed.
      * Setting the SR-IOV Network Operator into `systemd` mode is only relevant for Open vSwitch hardware offloading.
   2. Create the resource by running the following command:

      ```
      $ oc apply -f sriovOperatorConfig.yaml
      ```

### [13.5. Configuring a machine config pool for hardware offloading](#configuring-machine-config-pool_configuring-hardware-offloading) Copy linkLink copied to clipboard!

To enable hardware offloading, you now create a dedicated machine config pool and configure it to work with the SR-IOV Network Operator.

**Prerequisites**

* SR-IOV Network Operator installed and set into `systemd` mode.

**Procedure**

1. Create a machine config pool for machines you want to use hardware offloading on.

   1. Create a file, such as `mcp-offloading.yaml`, with content such as the following example:

      ```
      apiVersion: machineconfiguration.openshift.io/v1
      kind: MachineConfigPool
      metadata:
        name: <mcp_name>
      spec:
        machineConfigSelector:
          matchExpressions:
            - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,<mcp_name>]}
        nodeSelector:
          matchLabels:
            node-role.kubernetes.io/<mcp_name>: ""
      ```

      * `<mcp_name>` specifies the name of your machine config pool for hardware offloading. This value is used as the machine config pool name, the machine config selector value, and the node role label.
   2. Apply the configuration for the machine config pool:

      ```
      $ oc create -f mcp-offloading.yaml
      ```
2. Add nodes to the machine config pool. Label each node with the node role label of your pool:

   ```
   $ oc label node worker-2 node-role.kubernetes.io/mcp-offloading=""
   ```
3. Optional: To verify that the new pool is created, run the following command:

   ```
   $ oc get nodes
   ```

   The following is example output:

   ```
   NAME       STATUS   ROLES                   AGE   VERSION
   master-0   Ready    master                  2d    v1.35.4
   master-1   Ready    master                  2d    v1.35.4
   worker-0   Ready    worker                  2d    v1.35.4
   worker-1   Ready    worker                  2d    v1.35.4
   worker-2   Ready    mcp-offloading,worker   47h   v1.35.4
   ```
4. Add this machine config pool to the `SriovNetworkPoolConfig` custom resource:

   1. Create a file, such as `sriov-pool-config.yaml`, with content such as the following example:

      ```
      apiVersion: sriovnetwork.openshift.io/v1
      kind: SriovNetworkPoolConfig
      metadata:
        name: sriovnetworkpoolconfig-offload
        namespace: openshift-sriov-network-operator
      spec:
        ovsHardwareOffloadConfig:
          name: <mcp_name>
      ```

      * `<mcp_name>` specifies the name of your machine config pool for hardware offloading.
   2. Apply the configuration:

      ```
      $ oc create -f <SriovNetworkPoolConfig_name>.yaml
      ```

      Note

      When you apply the configuration specified in a `SriovNetworkPoolConfig` object, the SR-IOV Operator drains and restarts the nodes in the machine config pool.

      It might take several minutes for a configuration changes to apply.

### [13.6. Configuring the SR-IOV network node policy](#configure-sriov-node-policy_configuring-hardware-offloading) Copy linkLink copied to clipboard!

You can create an SR-IOV network device configuration for a node by creating an SR-IOV network node policy. To enable hardware offloading, you must define the `.spec.eSwitchMode` field with the value `"switchdev"`.

The following procedure creates an SR-IOV interface for a network interface controller with hardware offloading.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You have access to the cluster as a user with the `cluster-admin` role.

**Procedure**

1. Create a file, such as `sriov-node-policy.yaml`, with content such as the following example:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: <name>
     namespace: openshift-sriov-network-operator
   spec:
     deviceType: netdevice
     eSwitchMode: "switchdev"
     nicSelector:
       deviceID: "1019"
       rootDevices:
       - 0000:d8:00.0
       vendor: "15b3"
       pfNames:
       - ens8f0
     nodeSelector:
       feature.node.kubernetes.io/network-sriov.capable: "true"
     numVfs: 6
     priority: 5
     resourceName: mlxnics
   ```

   * `<name>` specifies the name for the custom resource object.
   * The `deviceType` field must be set to `netdevice`. Hardware offloading is not supported with `vfio-pci`.
   * The `eSwitchMode` field must be set to `"switchdev"`.
2. Apply the configuration for the policy:

   ```
   $ oc create -f sriov-node-policy.yaml
   ```

   Note

   When you apply the configuration specified in a `SriovNetworkPoolConfig` object, the SR-IOV Operator drains and restarts the nodes in the machine config pool.

   It might take several minutes for a configuration change to apply.

#### [13.6.1. An example SR-IOV network node policy for OpenStack](#nw-sriov-hwol-ref-openstack-sriov-policy_configuring-hardware-offloading) Copy linkLink copied to clipboard!

The following example describes an SR-IOV interface for a network interface controller (NIC) with hardware offloading on Red Hat OpenStack Platform (RHOSP).

The following example shows an SR-IOV interface for a NIC with hardware offloading on RHOSP:

```
apiVersion: sriovnetwork.openshift.io/v1
kind: SriovNetworkNodePolicy
metadata:
  name: ${name}
  namespace: openshift-sriov-network-operator
spec:
  deviceType: switchdev
  isRdma: true
  nicSelector:
    netFilter: openstack/NetworkID:${net_id}
  nodeSelector:
    feature.node.kubernetes.io/network-sriov.capable: 'true'
  numVfs: 1
  priority: 99
  resourceName: ${name}
```

### [13.7. Improving network traffic performance using a virtual function](#improving-network-traffic-performance-using-vf_configuring-hardware-offloading) Copy linkLink copied to clipboard!

Follow this procedure to assign a virtual function to the OVN-Kubernetes management port and increase its network traffic performance.

This procedure results in the creation of two pools: the first has a virtual function used by OVN-Kubernetes, and the second comprises the remaining virtual functions.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You have access to the cluster as a user with the `cluster-admin` role.

**Procedure**

1. Add the `network.operator.openshift.io/smart-nic` label to each worker node with a SmartNIC present by running the following command:

   ```
   $ oc label node <node-name> network.operator.openshift.io/smart-nic=
   ```

   Use the `oc get nodes` command to get a list of the available nodes.
2. Create a policy named `sriov-node-mgmt-vf-policy.yaml` for the management port with content such as the following example:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: sriov-node-mgmt-vf-policy
     namespace: openshift-sriov-network-operator
   spec:
     deviceType: netdevice
     eSwitchMode: "switchdev"
     nicSelector:
       deviceID: "1019"
       rootDevices:
       - 0000:d8:00.0
       vendor: "15b3"
       pfNames:
       - <pf_name>#0-0
     nodeSelector:
       network.operator.openshift.io/smart-nic: ""
     numVfs: <num_vfs>
     priority: 5
     resourceName: mgmtvf
   ```

   * `<pf_name>` specifies the network device for your use case. The `#0-0` part of the `pfNames` value reserves a single virtual function used by OVN-Kubernetes.
   * `<num_vfs>` specifies the number of virtual functions. Replace this value with one that meets your requirements. For more information, see *SR-IOV network node configuration object* in the *Additional resources* section.
3. Create a policy named `sriov-node-policy.yaml` with content such as the following example:

   ```
   apiVersion: sriovnetwork.openshift.io/v1
   kind: SriovNetworkNodePolicy
   metadata:
     name: sriov-node-policy
     namespace: openshift-sriov-network-operator
   spec:
     deviceType: netdevice
     eSwitchMode: "switchdev"
     nicSelector:
       deviceID: "1019"
       rootDevices:
       - 0000:d8:00.0
       vendor: "15b3"
       pfNames:
       - <pf_name>#1-5
     nodeSelector:
       network.operator.openshift.io/smart-nic: ""
     numVfs: <num_vfs>
     priority: 5
     resourceName: mlxnics
   ```

   * `<pf_name>` specifies the network device for your use case.
   * `<num_vfs>` specifies the number of virtual functions. Replace this value with the value specified in the `sriov-node-mgmt-vf-policy.yaml` file. For more information, see *SR-IOV network node configuration object* in the *Additional resources* section.

   Note

   The `sriov-node-mgmt-vf-policy.yaml` file has different values for the `pfNames` and `resourceName` keys than the `sriov-node-policy.yaml` file.
4. Apply the configuration for both policies:

   ```
   $ oc create -f sriov-node-policy.yaml
   ```

   ```
   $ oc create -f sriov-node-mgmt-vf-policy.yaml
   ```
5. Create a Cluster Network Operator (CNO) ConfigMap in the cluster for the management configuration:

   1. Create a ConfigMap named `hardware-offload-config.yaml` with the following contents:

      ```
      apiVersion: v1
      kind: ConfigMap
      metadata:
          name: hardware-offload-config
          namespace: openshift-network-operator
      data:
          mgmt-port-resource-name: openshift.io/mgmtvf
      ```
   2. Apply the configuration for the ConfigMap:

      ```
      $ oc create -f hardware-offload-config.yaml
      ```

### [13.8. Creating a network attachment definition](#create-network-attachment-definition_configuring-hardware-offloading) Copy linkLink copied to clipboard!

After you define the machine config pool and the SR-IOV network node policy, you can create a network attachment definition for the network interface controller (NIC) you specified.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You have access to the cluster as a user with the `cluster-admin` role.

**Procedure**

1. Create a file, such as `net-attach-def.yaml`, with content such as the following example:

   ```
   apiVersion: "k8s.cni.cncf.io/v1"
   kind: NetworkAttachmentDefinition
   metadata:
     name: <net_attach_def_name>
     namespace: <net_attach_def_namespace>
     annotations:
       k8s.v1.cni.cncf.io/resourceName: openshift.io/<resource_name>
   spec:
     config: '{"cniVersion":"0.3.1","name":"ovn-kubernetes","type":"ovn-k8s-cni-overlay","ipam":{},"dns":{}}'
   ```

   * `<net_attach_def_name>` specifies the name for your network attachment definition.
   * `<net_attach_def_namespace>` specifies the namespace for your network attachment definition.
   * `<resource_name>` specifies the value of the `spec.resourceName` field from the `SriovNetworkNodePolicy` object.
2. Apply the configuration for the network attachment definition:

   ```
   $ oc create -f net-attach-def.yaml
   ```

**Verification**

* Run the following command to check that the new definition exists:

  ```
  $ oc get net-attach-def -A
  ```

  The output shows the namespace, name, and age of the new definition.

### [13.9. Adding the network attachment definition to your pods](#adding-network-attachment-definition-to-pods_configuring-hardware-offloading) Copy linkLink copied to clipboard!

After you create the machine config pool, the `SriovNetworkPoolConfig` and `SriovNetworkNodePolicy` custom resources, and the network attachment definition, you can apply these configurations to your pods by adding the network attachment definition to your pod specifications.

**Procedure**

* In the pod specification, add the `.metadata.annotations.k8s.v1.cni.cncf.io/networks` field and specify the network attachment definition you created for hardware offloading:

  ```
  ....
  metadata:
    annotations:
      v1.multus-cni.io/default-network: <namespace>/<net_attach_def_name>
  ```

  + `<namespace>/<net_attach_def_name>` specifies the namespace and name of the network attachment definition you created for hardware offloading.

## [Chapter 14. Switching Bluefield-2 from DPU to NIC](#switching-bf2-nic-dpu) Copy linkLink copied to clipboard!

You can switch the Bluefield-2 network device from data processing unit (DPU) mode to network interface controller (NIC) mode.

Before you perform any tasks in the following documentation, ensure that you [installed the SR-IOV Network Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#installing-sriov-operator).

### [14.1. Switching Bluefield-2 from DPU mode to NIC mode](#proc-switching-bf2-nic_switching-bf2-nic-dpu) Copy linkLink copied to clipboard!

Use the following procedure to switch Bluefield-2 from data processing units (DPU) mode to network interface controller (NIC) mode.

Important

Currently, only switching Bluefield-2 from DPU to NIC mode is supported. Switching from NIC mode to DPU mode is unsupported.

**Prerequisites**

* You have installed the SR-IOV Network Operator. For more information, see "Installing SR-IOV Network Operator".
* You have updated Bluefield-2 to the latest firmware. For more information, see [Firmware for NVIDIA BlueField-2](https://network.nvidia.com/support/firmware/bluefield2/).

**Procedure**

1. Add the following label to each of your compute nodes by entering the following command. You must run the command for each compute node.

   ```
   $ oc label node <node_name> node-role.kubernetes.io/sriov=
   ```

   where:

   `node_name`
   :   Refers to the name of a compute node.
2. Create a machine config pool for the SR-IOV Network Operator, for example:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfigPool
   metadata:
     name: sriov
   spec:
     machineConfigSelector:
       matchExpressions:
       - {key: machineconfiguration.openshift.io/role, operator: In, values: [worker,sriov]}
     nodeSelector:
       matchLabels:
         node-role.kubernetes.io/sriov: ""
   ```
3. Apply the following `machineconfig.yaml` file to the compute nodes:

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfig
   metadata:
     labels:
       machineconfiguration.openshift.io/role: sriov
     name: 99-bf2-dpu
   spec:
     config:
       ignition:
         version: 3.2.0
       storage:
         files:
         - contents:
             source: data:text/plain;charset=utf-8;base64,ZmluZF9jb250YWluZXIoKSB7CiAgY3JpY3RsIHBzIC1vIGpzb24gfCBqcSAtciAnLmNvbnRhaW5lcnNbXSB8IHNlbGVjdCgubWV0YWRhdGEubmFtZT09InNyaW92LW5ldHdvcmstY29uZmlnLWRhZW1vbiIpIHwgLmlkJwp9CnVudGlsIG91dHB1dD0kKGZpbmRfY29udGFpbmVyKTsgW1sgLW4gIiRvdXRwdXQiIF1dOyBkbwogIGVjaG8gIndhaXRpbmcgZm9yIGNvbnRhaW5lciB0byBjb21lIHVwIgogIHNsZWVwIDE7CmRvbmUKISBzdWRvIGNyaWN0bCBleGVjICRvdXRwdXQgL2JpbmRhdGEvc2NyaXB0cy9iZjItc3dpdGNoLW1vZGUuc2ggIiRAIgo=
           mode: 0755
           overwrite: true
           path: /etc/default/switch_in_sriov_config_daemon.sh
       systemd:
         units:
         - name: dpu-switch.service
           enabled: true
           contents: |
             [Unit]
             Description=Switch BlueField2 card to NIC/DPU mode
             RequiresMountsFor=%t/containers
             Wants=network.target
             After=network-online.target kubelet.service
             [Service]
             SuccessExitStatus=0 120
             RemainAfterExit=True
             ExecStart=/bin/bash -c '/etc/default/switch_in_sriov_config_daemon.sh nic || shutdown -r now'
             Type=oneshot
             [Install]
             WantedBy=multi-user.target
   ```

   * `ExecStart` specifies the command to switch the Bluefield-2 into NIC mode. Optionally, you can specify the PCI address of a specific card, for example `ExecStart=/bin/bash -c '/etc/default/switch_in_sriov_config_daemon.sh nic 0000:5e:00.0 || echo done'`. By default, the first device is selected. If there is more than one device, you must specify which PCI address to use. The PCI address must be the same on all nodes that are switching Bluefield-2 from DPU mode to NIC mode.
4. Wait for the compute nodes to restart. After restarting, the Bluefield-2 network device on the compute nodes is switched into NIC mode.
5. Optional: You might need to restart the host hardware because most recent Bluefield-2 firmware releases require a hardware restart to switch into NIC mode.

## [Legal Notice](#idm140583325988416) Copy linkLink copied to clipboard!

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
