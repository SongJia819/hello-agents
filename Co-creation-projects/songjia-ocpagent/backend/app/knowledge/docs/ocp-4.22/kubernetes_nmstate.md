---
title: "Kubernetes NMState"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/kubernetes_nmstate/index
retrieved_at: 2026-09-05T05:42:10.716905+00:00
---

# Kubernetes NMState

---

OpenShift Container Platform 4.22

## Observing and updating node network state and configuration using Kubernetes NMState in OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140026251887840)

**Abstract**

This document covers using Kubernetes NMState to observe, update, and troubleshoot node network configurations in OpenShift Container Platform.

---

## [Chapter 1. Observing and updating the node network state and configuration](#k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

To observe and update the node network state and configuration in your cluster, you can use the Kubernetes NMState Operator. You can view network states, create and manage network configuration policies, and configure interfaces on cluster nodes.

For more information about how to install the NMState Operator, see [Kubernetes NMState Operator](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#k8s-nmstate-about-the-k8s-nmstate-operator).

Important

You cannot modify an existing `br-ex` bridge, an OVN-Kubernetes-managed Open vSwitch bridge, or any interfaces, bonds, VLANs, and so on that associate with the `br-ex` bridge. However, you can configure a customized br-ex bridge.

For more information, see "Creating a manifest object that includes a customized br-ex bridge" in the *Deploying installer-provisioned clusters on bare metal* document or the *Installing a user-provisioned cluster on bare metal* document.

### [1.1. Viewing the network state of a node by using the CLI](#virt-viewing-network-state-of-node_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

Node network state is the network configuration for all nodes in the cluster. A `NodeNetworkState` object exists on every node in the cluster. This object is periodically updated and captures the state of the network for that node.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. List all the `NodeNetworkState` objects in the cluster:

   ```
   $ oc get nns
   ```
2. Inspect a `NodeNetworkState` object to view the network on that node. The output in this example has been redacted for clarity:

   ```
   $ oc get nns node01 -o yaml
   ```

   Example output:

   ```
   apiVersion: nmstate.io/v1
   kind: NodeNetworkState
   metadata:
     name: node01
   status:
     currentState:
       dns-resolver:
   # ...
       interfaces:
   # ...
       route-rules:
   # ...
       routes:
   # ...
     lastSuccessfulUpdateTime: "2020-01-31T12:14:00Z"
   ```

   `metadata.name`
   :   The name of the `NodeNetworkState` object is taken from the node.

   `status.currentState`
   :   The `currentState` contains the complete network configuration for the node, including DNS, interfaces, and routes.

   `status.lastSuccessfulUpdateTime`
   :   Timestamp of the last successful update. This is updated periodically if the node is reachable and can be used to evaluate the freshness of the report.

### [1.2. Viewing a graphical representation of the network state of a node (NNS) topology from the web console](#virt-viewing-graphical-representation-of-network-state-of-node-console_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

To make the configuration of the node network in the cluster easier to understand, you can view it in the form of a diagram.

The NNS topology diagram displays all node components (network interface controllers, bridges, bonds, and VLANs), their properties and configurations, and connections between the nodes.

**Procedure**

* In the **Administrator** view of the OpenShift Container Platform web console, navigate to **Networking** → **Node Network Configuration**.

  The NNS topology diagram opens. Each group of components represents a single node.

  + To display the configuration and properties of a node, click inside the border of the node.
  + To display the features or the YAML file of a specific component (for example, an interface or a bridge), click the icon of the component.
  + The icons of active components have green borders; the icons of disconnected components have red borders.

### [1.3. Viewing the list of NodeNetworkState resources](#virt-viewing-list-of-nodenetworkstate-resources-console_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

As an administrator, you can use the OpenShift Container Platform web console to view the list of `NodeNetworkState` resources and network interfaces, and access network details.

**Procedure**

1. Navigate to **Networking** → **Node Network Configuration**.
2. Click the **List** icon.

   You can now view the list of `NodeNetworkState` resources and the corresponding interfaces that are created on the nodes.

   * You can use **Filter** based on **Interface state**, **Interface type**, and **IP**, or the search bar based on criteria **Name** or **Label**, to narrow down the displayed `NodeNetworkState` resources.
   * To access the detailed information about a `NodeNetworkState` resource, click the `NodeNetworkState` resource name listed in the **Name** column .
   * To expand and view the **Network Details** section for the `NodeNetworkState` resource, click the greater than (**>**) symbol . Alternatively, you can click on each interface type under the **Network interface** column to view the network details.

### [1.4. About the NodeNetworkConfigurationPolicy manifest file](#node-network-configuration-policy-file_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

A `NodeNetworkConfigurationPolicy` manifest file defines policies that the Kubernetes NMState Operator uses to configure networking for nodes in your OpenShift Container Platform cluster. You can create, edit, and delete these policies to manage node network configurations.

Important

If you want to apply multiple NNCP CRs to a node, you must create the NNCPs in a logical order that is based on the alphanumeric sorting of the policy names. The Kubernetes NMState Operator continuously checks for a newly created NNCP CR so that the Operator can instantly apply the CR to node. Consider the following logical order issue example:

1. You create NNCP 1 for defining the bridge interface that listens on a VLAN port, such as `eth1.1000`.
2. You create NNCP 2 for defining the VLAN interface and specify the port for this interface, such as `eth1.1000`.
3. You apply NNCP 1 before you apply NNCP 2 to the node.

The node experiences a node connectivity issue because port `eth1.1000` does not exist. As a result, the cluster fails.

After you apply a node network policy to a node, the Kubernetes NMState Operator configures the networking configuration for nodes according to the node network policy details.

Warning

The following list of interface names are reserved and you cannot use the names with NMstate configurations:

* `br-ext`
* `br-int`
* `br-local`
* `br-nexthop`
* `br0`
* `ext-vxlan`
* `ext`
* `genev_sys_*`
* `int`
* `k8s-*`
* `ovn-k8s-*`
* `patch-br-*`
* `tun0`
* `vxlan_sys_*`

You can create an NNCP by using either the OpenShift CLI (`oc`) or the OpenShift Container Platform web console. As a postinstallation task you can create an NNCP or edit an existing NNCP.

Note

Before you create an NNCP, ensure that you read the "Example policy configurations for different interfaces" document.

If you want to delete an NNCP, you can use the `oc delete nncp` command to complete this action. However, this command does not delete any objects, such as a bridge interface.

Deleting the node network policy that added an interface to a node does not change the configuration of the policy on the node. Similarly, removing an interface does not delete the policy, because the Kubernetes NMState Operator re-adds the removed interface whenever a pod or a node is restarted.

To effectively delete the NNCP, the node network policy, and any interfaces would typically require the following actions:

1. Edit the NNCP and remove interface details from the file. Ensure that you do not remove `name`, `state`, and `type` parameters from the file.
2. Add `state: absent` under the `interfaces.state` section of the NNCP.
3. Run `oc apply -f <nncp_file_name>`. After the Kubernetes NMState Operator applies the node network policy to each node in your cluster, any interface that exists on each node is now marked as *absent*.
4. Run `oc delete nncp` to delete the NNCP.

**Additional resources**

* [Example policy configurations for different interfaces](#virt-nmstate-example-policy-configurations_k8s-nmstate-updating-node-network-config "1.9. Example policy configurations for different interfaces")
* [Removing an interface from nodes](#virt-removing-interface-from-nodes_k8s-nmstate-updating-node-network-config "1.7.3. Removing an interface from nodes")

### [1.5. Managing policy from the web console](#virt-node-network-config-console_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can update the node network configuration, such as adding or removing interfaces from nodes, by applying `NodeNetworkConfigurationPolicy` manifests to the cluster.

Manage the policy from the web console by accessing the list of created policies in the **NodeNetworkConfigurationPolicy** page under the **Networking** menu. This page enables you to create, update, monitor, and delete the policies.

#### [1.5.1. Monitoring the policy status](#virt-monitor-node-network-config-console_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can monitor the policy status from the **NodeNetworkConfigurationPolicy** page. This page displays all the policies created in the cluster in a tabular format, with the following columns:

Name
:   The name of the policy created.

Matched nodes
:   The count of nodes where the policies are applied. This could be either a subset of nodes based on the node selector or all the nodes on the cluster.

Node network state
:   The enactment state of the matched nodes. You can click on the enactment state and view detailed information on the status.

To find the desired policy, you can filter the list either based on enactment state by using the **Filter** option, or by using the search option.

#### [1.5.2. Creating a policy](#virt-create-node-network-config-console_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can create a policy by using either a form or YAML in the web console. When creating a policy using a form, you can see how the new policy changes the topology of the nodes in your cluster in real time.

**Procedure**

1. Navigate to **Networking** → **Node Network Configuration**.
2. On the **Node Network Configuration** page, click **Create** and select the **From Form** option.

   Note

   To create a policy using YAML, click **Create** → **With YAML** option. However, the following steps apply only to the form method.
3. Optional: Check the **Apply this NodeNetworkConfigurationPolicy only to specific subsets of nodes using the node selector** checkbox to specify the nodes where the policy must be applied.
4. Enter the policy name in the **Policy name** field.
5. Optional: Enter the description of the policy in the **Description** field.
6. Click **Next** to move to the **Policy Interfaces** section.
7. In the **Bridging** part of the **Policy Interfaces** section, a bridge interface named `br0` is added by default with preset values in editable fields. If required, edit the values by performing the following steps:

   1. Enter the name of the interface in **Interface name** field.
   2. Select the required network state. The default selected state is **Up**.
   3. Select the type of interface. The available types are **Bridge**, **Bonding**, and **Ethernet**. The default selected value is **Bridge**.

      Note

      Addition of a VLAN interface by using the form is not supported. To add a VLAN interface, you must use YAML to create the policy. Once added, you cannot edit the policy by using form.
   4. Optional: In the IP configuration section, check **IPv4** checkbox to assign an IPv4 address to the interface, and configure the IP address assignment details:

      1. Click **IP address** to configure the interface with a static IP address, or **DHCP** to auto-assign an IP address.
      2. If you have selected **IP address** option, enter the IPv4 address in **IPV4 address** field, and enter the prefix length in **Prefix length** field.

         If you have selected **DHCP** option, uncheck the options that you want to disable. The available options are **Auto-DNS**, **Auto-routes**, and **Auto-gateway**. All the options are selected by default.
   5. Optional: Enter the port number in **Port** field.
   6. Optional: Check the checkbox **Enable STP** to enable STP.
   7. Optional: To add an interface to the policy, click **Add another interface to the policy**.
   8. Optional: To remove an interface from the policy, click
      icon next to the interface.

   Note

   Alternatively, you can click **Edit YAML** on the top of the page to continue editing the form using YAML.
8. Click **Next** to go to the **Review** section of the form.
9. Verify the settings and click **Create** to create the policy.

### [1.6. Updating the NodeNetworkConfigurationPolicy manifest file](#virt-updating-policy-k8s-nmstate_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

To modify the network configuration for nodes in your OpenShift Container Platform cluster, you can update the `NodeNetworkConfigurationPolicy` manifest file.

#### [1.6.1. Updating the policy by using form](#virt-update-node-network-config-form_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can update a `NodeNetworkConfigurationPolicy` object by using the form view in the web console.

Note

Addition of a VLAN interface using the form is not supported. To add a VLAN interface, you must use YAML to create the policy. Once added, you cannot edit the policy using form.

**Procedure**

1. Navigate to **Networking** → **NodeNetworkConfigurationPolicy**.
2. In the **NodeNetworkConfigurationPolicy** page, click the
   icon placed next to the policy you want to edit, and click **Edit**.
3. Edit the fields that you want to update.
4. Click **Save**.

#### [1.6.2. Updating the policy by using YAML](#virt-update-node-network-config-yaml_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can update a `NodeNetworkConfigurationPolicy` object by editing the YAML in the web console.

**Procedure**

1. Navigate to **Networking** → **NodeNetworkConfigurationPolicy**.
2. In the **NodeNetworkConfigurationPolicy** page, click the policy name under the **Name** column for the policy you want to edit.
3. Click the **YAML** tab, and edit the YAML.
4. Click **Save**.

#### [1.6.3. Deleting the policy](#virt-delete-node-network-config_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can delete a `NodeNetworkConfigurationPolicy` object when it is no longer needed.

**Procedure**

1. Navigate to **Networking** → **NodeNetworkConfigurationPolicy**.
2. In the **NodeNetworkConfigurationPolicy** page, click the
   icon placed next to the policy you want to delete, and click **Delete**.
3. In the pop-up window, enter the policy name to confirm deletion, and click **Delete**.

### [1.7. Managing the NodeNetworkConfigurationPolicy manifest file](#virt-manage-nncp-cli_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

To configure network interfaces on nodes in your OpenShift Container Platform cluster, you can manage the `NodeNetworkConfigurationPolicy` manifest file by using the CLI.

#### [1.7.1. Creating an interface on nodes](#virt-creating-interface-on-nodes_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can create an interface on nodes in the cluster by applying a `NodeNetworkConfigurationPolicy` (NNCP) manifest to the cluster. The manifest details the requested configuration for the interface.

By default, the manifest applies to all nodes in the cluster. To add the interface to specific nodes, add the `spec: nodeSelector` parameter and the appropriate `<key>:<value>` for your node selector.

You can configure multiple nmstate-enabled nodes concurrently. The configuration applies to 50% of the nodes in parallel. This strategy prevents the entire cluster from being unavailable if the network connection fails. To apply the policy configuration in parallel to a specific portion of the cluster, use the `maxUnavailable` parameter in the `NodeNetworkConfigurationPolicy` manifest configuration file.

Note

If you have two nodes and you apply an NNCP manifest with the `maxUnavailable` parameter set to `50%` to these nodes, one node at a time receives the NNCP configuration. If you then introduce an additional NNCP manifest file with the `maxUnavailable` parameter set to `50%`, this NCCP is independent of the initial NNCP; this means that if both NNCP manifests apply a bad configuration to nodes, you can no longer guarantee that half of your cluster is functional.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Create the `NodeNetworkConfigurationPolicy` manifest. The following example configures a Linux bridge on all worker nodes and configures the DNS resolver:

   ```
   apiVersion: nmstate.io/v1
   kind: NodeNetworkConfigurationPolicy
   metadata:
     name: br1-eth1-policy
   spec:
     nodeSelector:
       node-role.kubernetes.io/worker: ""
     maxUnavailable: 3
     desiredState:
       interfaces:
         - name: br1
           description: Linux bridge with eth1 as a port
           type: linux-bridge
           state: up
           ipv4:
             dhcp: true
             enabled: true
             auto-dns: false
           bridge:
             options:
               stp:
                 enabled: false
             port:
               - name: eth1
       dns-resolver:
         config:
           search:
           - example.com
           - example.org
           server:
           - 8.8.8.8
   ```

   * `metadata.name` defines the name of the policy.
   * `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes.
   * `spec.nodeSelector.node-role.kubernetes.io/worker` uses the `node-role.kubernetes.io/worker: ""` node selector to select all worker nodes in the cluster.
   * `spec.maxUnavailable` is optional and defines the maximum number of nmstate-enabled nodes that the policy configuration can be applied to concurrently. This parameter can be set to either a percentage value (string), for example, `"10%"`, or an absolute value (number), such as `3`.
   * `spec.desiredState.interfaces.description` is optional and defines a human-readable description for the interface.
   * `spec.desiredState.dns-resolver` is optional and defines the search and server settings for the DNS server.
2. Create the node network policy:

   ```
   $ oc apply -f br1-eth1-policy.yaml
   ```

   where:

   `br1-eth1-policy.yaml`
   :   Specifies the file name of the node network configuration policy manifest.

**Additional resources**

* [Example for creating multiple interfaces in the same policy](#virt-example-nmstate-multiple-interfaces_k8s-nmstate-updating-node-network-config "1.9.5. Example: Multiple interfaces in the same node network configuration policy")
* [Examples of different IP management methods in policies](#virt-example-nmstate-IP-management_k8s-nmstate-updating-node-network-config "1.12. Examples: IP management")

#### [1.7.2. Confirming node network policy updates on nodes](#virt-confirming-policy-updates-on-nodes_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

When you apply a node network policy, a `NodeNetworkConfigurationEnactment` object is created for every node in the cluster. The node network configuration enactment is a read-only object that represents the status of execution of the policy on that node.

If the policy fails to be applied on the node, the enactment for that node includes a traceback for troubleshooting.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. To confirm that a policy has been applied to the cluster, list the policies and their status:

   ```
   $ oc get nncp
   ```
2. Optional: If a policy is taking longer than expected to successfully configure, you can inspect the requested state and status conditions of a particular policy:

   ```
   $ oc get nncp <policy> -o yaml
   ```
3. Optional: If a policy is taking longer than expected to successfully configure on all nodes, you can list the status of the enactments on the cluster:

   ```
   $ oc get nnce
   ```
4. Optional: To view the configuration of a particular enactment, including any error reporting for a failed configuration:

   ```
   $ oc get nnce <node>.<policy> -o yaml
   ```

#### [1.7.3. Removing an interface from nodes](#virt-removing-interface-from-nodes_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can remove an interface from one or more nodes in the cluster by editing the `NodeNetworkConfigurationPolicy` object and setting the `state` of the interface to `absent`.

Removing an interface from a node does not automatically restore the node network configuration to a previous state. If you want to restore the previous state, you will need to define that node network configuration in the policy.

If you remove a bridge or bonding interface, any node NICs in the cluster that were previously attached or subordinate to that bridge or bonding interface are placed in a `down` state and become unreachable. To avoid losing connectivity, configure the node NIC in the same policy so that it has a status of `up` and either DHCP or a static IP address.

Note

Deleting the node network policy that added an interface does not change the configuration of the policy on the node. Although a `NodeNetworkConfigurationPolicy` is an object in the cluster, the object only represents the requested configuration. Similarly, removing an interface does not delete the policy.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Update the `NodeNetworkConfigurationPolicy` manifest used to create the interface. The following example removes a Linux bridge and configures the `eth1` NIC with DHCP to avoid losing connectivity:

   ```
   apiVersion: nmstate.io/v1
   kind: NodeNetworkConfigurationPolicy
   metadata:
     name: <br1-eth1-policy>
   spec:
     nodeSelector:
       node-role.kubernetes.io/worker: ""
     desiredState:
       interfaces:
       - name: br1
         type: linux-bridge
         state: absent
       - name: eth1
         type: ethernet
         state: up
         ipv4:
           dhcp: true
           enabled: true
   ```

   * `metadata.name` defines the name of the policy.
   * `spec.nodeSelector` defines the `nodeSelector` parameter. This parameter is optional. If you do not include the `nodeSelector` parameter, the policy applies to all nodes in the cluster. This example uses the `node-role.kubernetes.io/worker: ""` node selector to select all worker nodes in the cluster.
   * `spec.desiredState.interfaces` defines the name, type, and desired state of an interface. This example creates both Linux bridge and Ethernet networking interfaces. Setting `state: absent` removes the interface.
   * `spec.desiredState.interfaces.ipv4` defines `ipv4` settings for the interface. These settings are optional. If you do not use `dhcp`, you can either set a static IP or leave the interface without an IP address. Setting `enabled: true` enables `ipv4` in this example.
2. Update the policy on the node and remove the interface:

   ```
   $ oc apply -f <filename.yaml>
   ```

   Where `<filename.yaml>` is the filename of the policy manifest.

### [1.8. Configure alternative network interface names](#k8s-nmstate-alternative-interface-names_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can assign alternative names to network interfaces to create consistent, descriptive labels across cluster nodes. Alternative names help you overcome the 15-character kernel interface name limitation and simplify automation in environments where interface naming varies across hardware.

Alternative interface names provide the following benefits:

* **Consistent naming**: Apply standardized names regardless of underlying hardware naming schemes, which is useful in heterogeneous clusters.
* **Descriptive labels**: Use descriptive names up to 127 characters, such as `production-external-interface`, in addition to kernel-assigned names like `ens3f0`.
* **Simplified automation**: Reference interfaces by names that remain constant across different node types, reducing configuration errors.

You can use alternative names anywhere that accepts a standard interface name, including bond ports, VLAN base interfaces, bridge ports, and route next-hop interfaces.

#### [1.8.1. Create alternative interface names by interface name](#k8s-nmstate-creating-alternative-interface-names-by-name_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can create alternative names for network interfaces to enable consistent, descriptive interface references across cluster nodes. Alternative names persist across reboots and can be used anywhere standard interface names are accepted.

Important

You cannot configure alternative names on the `br-ex` bridge or any OVN-Kubernetes-managed Open vSwitch bridge. You also cannot configure alternative names on interfaces, bonds, VLANs, or other devices associated with the `br-ex` bridge.

**Prerequisites**

* You installed the Kubernetes NMState Operator.
* You have access to the cluster as a user with the `cluster-admin` role.
* You installed the OpenShift CLI (`oc`).
* You identified the target interface by interface name.
* The target interface is not the `br-ex` bridge, an OVN-Kubernetes-managed bridge, or associated with these bridges.

**Procedure**

1. Create a `NodeNetworkConfigurationPolicy` custom resource (CR) to define alternative names for a target interface.

   Note

   Alternative names are appended to any existing alternative names. If you apply a policy multiple times with the same alternative names, the configuration remains unchanged.

   The following example creates a file named `ethernet-alt-names.yaml`:

   ```
   apiVersion: nmstate.io/v1
   kind: NodeNetworkConfigurationPolicy
   metadata:
     name: ethernet-alt-names-policy
   spec:
     nodeSelector:
       kubernetes.io/hostname: <node_name>
     desiredState:
       interfaces:
         - name: <interface_name>
           type: ethernet
           state: up
           alt-names:
             - name: <alternative_name_1>
             - name: <alternative_name_2>
   ```

   where:

   * `<node_name>` is the target node name. To target multiple nodes, use a different label selector such as `node-role.kubernetes.io/worker: ""`.
   * `<interface_name>` is the target interface name.
   * `<alternative_name_1>` and `<alternative_name_2>` are the alternative names you want to assign.
2. Apply the policy to the cluster by running the following command:

   ```
   $ oc apply -f ethernet-alt-names.yaml
   ```

   **Example output**

   ```
   nodenetworkconfigurationpolicy.nmstate.io/ethernet-alt-names-policy created
   ```

**Verification**

1. Verify that the policy was applied successfully by running the following command:

   ```
   $ oc get nncp ethernet-alt-names-policy -o yaml
   ```

   Check the `status` section to confirm the policy state is `Available`:

   ```
   status:
     conditions:
     - lastTransitionTime: "2026-03-31T12:00:00Z"
       message: 2/2 nodes successfully configured
       reason: SuccessfullyConfigured
       status: "True"
       type: Available
   ```
2. Create a debug pod on the target node and open a shell to the node filesystem by running the following command:

   ```
   $ oc debug node/<node_name>
   ```
3. Verify that the alternative names are configured on the interface by running the following command:

   ```
   sh-4.4# ip link show <interface_name>
   ```

   **Example output**

   ```
   2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
       link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
       altname production-network
       altname external-interface
   ```

   The `altname` entries show the configured alternative names.

#### [1.8.2. Create alternative interface names by MAC address or PCI address](#k8s-nmstate-creating-alternative-interface-names-by-identifier_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can match network interfaces by MAC address or peripheral component interconnect (PCI) address to create configurations that target interfaces based on hardware identifiers rather than interface name.

MAC address matching is useful when you want to target a specific network interface controller. PCI address matching is useful when interface names vary across nodes but hardware slot locations remain consistent.

**Prerequisites**

* You installed the Kubernetes NMState Operator.
* You have access to the cluster as a user with the `cluster-admin` role.
* You installed the OpenShift CLI (`oc`).
* You identified the target interface by MAC address or PCI address.

**Procedure**

1. Create a `NodeNetworkConfigurationPolicy` custom resource (CR) to define alternative names for a target interface by using one of the following methods:

   1. To target an interface by MAC address, create a file named `identifier-alt-names.yaml` with content similar to the following example:

      ```
      apiVersion: nmstate.io/v1
      kind: NodeNetworkConfigurationPolicy
      metadata:
        name: mac-alt-names-policy
      spec:
        nodeSelector:
          kubernetes.io/hostname: <node_name>
        desiredState:
          interfaces:
            - name: <interface_name>
              type: ethernet
              identifier: mac-address
              mac-address: <mac_address>
              state: up
              alt-names:
                - name: <alternative_name_1>
                - name: <alternative_name_2>
      ```

      where:

      * `<node_name>` is the target node name.
      * `<interface_name>` is any identifier because the interface is matched by MAC address.
      * `<mac_address>` is the MAC address of the target interface.
      * `<alternative_name_1>` and `<alternative_name_2>` are the alternative names you want to assign.
   2. To target an interface by PCI address, create a file named `identifier-alt-names.yaml` with content similar to the following example:

      ```
      apiVersion: nmstate.io/v1
      kind: NodeNetworkConfigurationPolicy
      metadata:
        name: pci-alt-names-policy
      spec:
        nodeSelector:
          node-role.kubernetes.io/worker: ""
        desiredState:
          interfaces:
            - name: <interface_name>
              type: ethernet
              state: up
              identifier: pci-address
              pci-address: <pci_address>
              alt-names:
                - name: <alternative_name_1>
                - name: <alternative_name_2>
      ```

      where:

      * `<interface_name>` is any identifier because the interface is matched by PCI address.
      * `<pci_address>` is the PCI address of the target interface in the format `domain:bus:device.function`, for example, `0000:01:00.0`.
      * `<alternative_name_1>` and `<alternative_name_2>` are the alternative names you want to assign.

        Note

        This example uses `node-role.kubernetes.io/worker: ""` to target all worker nodes. Use this only when all workers have the same PCI slot configuration. For heterogeneous clusters, use `kubernetes.io/hostname: <node_name>` or hardware-specific labels.
2. Apply the policy to the cluster by running the following command:

   ```
   $ oc apply -f identifier-alt-names.yaml
   ```

**Verification**

1. Verify that the policy was applied successfully by running the following command:

   ```
   $ oc get nncp <policy_name> -o yaml
   ```

   Check the `status` section to confirm the policy state is `Available`:

   ```
   status:
     conditions:
     - lastTransitionTime: "2026-03-31T12:00:00Z"
       message: 3/3 nodes successfully configured
       reason: SuccessfullyConfigured
       status: "True"
       type: Available
   ```
2. Create a debug pod on the target node and open a shell to the node filesystem by running the following command:

   ```
   $ oc debug node/<node_name>
   ```
3. Verify that the alternative names are configured on the interface by running the following command:

   ```
   sh-4.4# ip link show <interface_name>
   ```

   **Example output**

   ```
   2: ens1f0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc mq state UP mode DEFAULT group default qlen 1000
       link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
       altname production-uplink
       altname external-interface
   ```

   The `altname` entries show the configured alternative names.

#### [1.8.3. Delete alternative interface names](#k8s-nmstate-deleting-alternative-interface-names_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can remove alternative names from network interfaces when they are no longer needed. Removing alternative names requires explicitly marking them for deletion in a `NodeNetworkConfigurationPolicy` resource.

Warning

Alternative names used as bond ports (`link-aggregation.port.name`), VLAN base interfaces (`vlan.base-iface`), bridge ports (`linux-bridge.port.name`), or route next-hop interfaces might cause those configurations to fail if the name is removed.

**Prerequisites**

* The Kubernetes NMState Operator is installed.
* You have access to the cluster as a user with the `cluster-admin` role.
* You installed the OpenShift CLI (`oc`).
* You configured alternative names on the target interface.

**Procedure**

1. Create or update a `NodeNetworkConfigurationPolicy` custom resource (CR) to remove specific alternative names by using one of the following methods:

   1. To target an interface by interface name, create a file named `remove-alt-names.yaml` with content similar to the following example:

      ```
      apiVersion: nmstate.io/v1
      kind: NodeNetworkConfigurationPolicy
      metadata:
        name: remove-alt-names-policy
      spec:
        nodeSelector:
          kubernetes.io/hostname: <node_name>
        desiredState:
          interfaces:
            - name: <interface_name>
              type: ethernet
              state: up
              alt-names:
                - name: <alternative_name_to_remove>
                  state: absent
                - name: <another_alternative_name_to_remove>
                  state: absent
      ```

      where:

      * `<node_name>` is the target node name. To target multiple nodes, use a different label selector such as `node-role.kubernetes.io/worker: ""`.
      * `<interface_name>` is the target interface name.
      * `<alternative_name_to_remove>` is the alternative name you want to delete.
   2. To target an interface by MAC address, create a file named `remove-alt-names.yaml` with content similar to the following example:

      ```
      apiVersion: nmstate.io/v1
      kind: NodeNetworkConfigurationPolicy
      metadata:
        name: remove-alt-names-policy
      spec:
        nodeSelector:
          kubernetes.io/hostname: <node_name>
        desiredState:
          interfaces:
            - name: <interface_name>
              type: ethernet
              identifier: mac-address
              mac-address: <mac_address>
              state: up
              alt-names:
                - name: <alternative_name_to_remove>
                  state: absent
                - name: <another_alternative_name_to_remove>
                  state: absent
      ```

      where:

      * `<node_name>` is the target node name.
      * `<interface_name>` is any identifier because the interface is matched by MAC address.
      * `<mac_address>` is the MAC address of the target interface.
      * `<alternative_name_to_remove>` is the alternative name you want to delete.
   3. To target an interface by PCI address, create a file named `remove-alt-names.yaml` with content similar to the following example:

      ```
      apiVersion: nmstate.io/v1
      kind: NodeNetworkConfigurationPolicy
      metadata:
        name: remove-alt-names-policy
      spec:
        nodeSelector:
          kubernetes.io/hostname: <node_name>
        desiredState:
          interfaces:
            - name: <interface_name>
              type: ethernet
              identifier: pci-address
              pci-address: <pci_address>
              state: up
              alt-names:
                - name: <alternative_name_to_remove>
                  state: absent
                - name: <another_alternative_name_to_remove>
                  state: absent
      ```

      where:

      * `<node_name>` is the target node name.
      * `<interface_name>` is any identifier because the interface is matched by PCI address.
      * `<pci_address>` is the PCI address of the target interface in the format `domain:bus:device.function` (for example, `0000:01:00.0`).
      * `<alternative_name_to_remove>` is the alternative name you want to delete.
2. Apply the policy to remove the alternative names by running the following command:

   ```
   $ oc apply -f remove-alt-names.yaml
   ```

**Verification**

1. Verify that the policy was applied successfully:

   ```
   $ oc get nncp remove-alt-names-policy -o yaml
   ```

   Check the `status` section to confirm the policy state is `Available`:

   ```
   status:
     conditions:
     - lastTransitionTime: "2026-03-31T12:00:00Z"
       message: 1/1 nodes successfully configured
       reason: SuccessfullyConfigured
       status: "True"
       type: Available
   ```
2. Access the target node:

   ```
   $ oc debug node/<node_name>
   ```
3. Verify that the alternative name was removed:

   ```
   sh-4.4# ip link show <interface_name>
   ```

   **Example output**

   ```
   2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP mode DEFAULT group default qlen 1000
       link/ether 00:11:22:33:44:55 brd ff:ff:ff:ff:ff:ff
       altname production-network
       altname external-interface
   ```

   The removed alternative name (for example, `deprecated-name`) should no longer appear in the `altname` entries.

   Note

   * If you remove an alternative name from the policy YAML without setting `state: absent`, the NMState Operator does not delete it from the interface. Alternative names use an incremental change model where applying a policy appends new names. You must explicitly mark names for deletion with `state: absent`.
   * If you delete the entire interface configuration, all associated alternative names are also deleted.

### [1.9. Example policy configurations for different interfaces](#virt-nmstate-example-policy-configurations_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

Before you read the different example `NodeNetworkConfigurationPolicy` (NNCP) manifest configurations, consider the following factors when you apply a policy to nodes so that your cluster runs under its best performance conditions.

* If you want to apply multiple NNCP CRs to a node, you must create the NNCPs in a logical order that is based on the alphanumeric sorting of the policy names. The Kubernetes NMState Operator continuously checks for a newly created NNCP CR so that the Operator can instantly apply the CR to node.
* When you need to apply a policy to many nodes but you only want to create a single NNCP for all the nodes, the Kubernetes NMState Operator applies the policy to each node in sequence. You can set the speed and coverage of policy application for target nodes with the `maxUnavailable` parameter in the cluster’s configuration file. By setting a lower percentage value for the parameter, you can reduce the risk of a cluster-wide outage if the outage impacts the small percentage of nodes that are receiving the policy application.
* If you set the `maxUnavailable` parameter to `50%` in two NNCP manifests, the policy configuration coverage applies to 100% of the nodes in your cluster.
* When a node restarts, the Kubernetes NMState Operator cannot control the order to which it applies policies to nodes. The Kubernetes NMState Operator might apply interdependent policies in a sequence that results in a degraded network object.
* Consider specifying all related network configurations in a single policy.

#### [1.9.1. Example: Ethernet interface node network configuration policy](#virt-example-ethernet-nncp_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can configure an Ethernet interface on nodes in the cluster by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster.

The following YAML file is an example of a manifest for an Ethernet interface. It includes sample values that you must replace with your own information.

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: eth1-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node01>
  desiredState:
    interfaces:
    - name: eth1
      description: Configuring eth1 on node01
      type: ethernet
      state: up
      ipv4:
        dhcp: true
        enabled: true
```

* `metadata.name` defines the name of the policy.
* `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes.
* `spec.nodeSelector.kubernetes.io/hostname` uses a hostname node selector.
* `spec.desiredState.interfaces.name` defines the name of the interface.
* `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface.
* `spec.desiredState.interfaces.type` defines the type of interface. This example creates an Ethernet networking interface.
* `spec.desiredState.interfaces.state` defines the requested state for the interface after creation.
* `spec.desiredState.interfaces.ipv4.dhcp` is optional. If you do not use `dhcp`, you can either set a static IP or leave the interface without an IP address.
* `spec.desiredState.interfaces.ipv4.enabled` defines that `ipv4` is enabled in this example.

#### [1.9.2. Example: Linux bridge interface node network configuration policy](#virt-example-bridge-nncp_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can create a Linux bridge interface on nodes in the cluster by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster.

The following YAML file is an example of a manifest for a Linux bridge interface. It includes samples values that you must replace with your own information.

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: br1-eth1-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node01>
  desiredState:
    interfaces:
      - name: br1
        description: Linux bridge with eth1 as a port
        type: linux-bridge
        state: up
        ipv4:
          dhcp: true
          enabled: true
        bridge:
          options:
            stp:
              enabled: false
          port:
            - name: eth1
```

* `metadata.name` defines the name of the policy.
* `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes.
* `spec.nodeSelector.kubernetes.io/hostname` uses a hostname node selector.
* `spec.desiredState.interfaces.name` defines the name of the interface.
* `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface.
* `spec.desiredState.interfaces.type` defines the type of interface. This example creates a bridge.
* `spec.desiredState.interfaces.state` defines the requested state for the interface after creation.
* `spec.desiredState.interfaces.ipv4.dhcp` is optional. If you do not use `dhcp`, you can either set a static IP or leave the interface without an IP address.
* `spec.desiredState.interfaces.ipv4.enabled` defines that `ipv4` is enabled in this example.
* `spec.desiredState.interfaces.bridge.options.stp.enabled` defines that `stp` is disabled in this example.
* `spec.desiredState.interfaces.bridge.port.name` defines the node NIC to which the bridge attaches.

#### [1.9.3. Example: VLAN interface node network configuration policy](#virt-example-vlan-nncp_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can create a VLAN interface on nodes in the cluster by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster.

Note

Define all related configurations for the VLAN interface of a node in a single `NodeNetworkConfigurationPolicy` manifest. For example, define the VLAN interface for a node and the related routes for the VLAN interface in the same `NodeNetworkConfigurationPolicy` manifest.

When a node restarts, the Kubernetes NMState Operator cannot control the order in which policies are applied. Therefore, if you use separate policies for related network configurations, the Kubernetes NMState Operator might apply these policies in a sequence that results in a degraded network object.

The following YAML file is an example of a manifest for a VLAN interface. It includes samples values that you must replace with your own information.

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: vlan-eth1-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node01>
  desiredState:
    interfaces:
    - name: eth1.102
      description: VLAN using eth1
      type: vlan
      state: up
      vlan:
        base-iface: eth1
        id: 102
```

* `metadata.name` defines the name of the policy.
* `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes.
* `spec.nodeSelector.kubernetes.io/hostname` uses a hostname node selector.
* `spec.desiredState.interfaces.name` defines the name of the interface. When deploying on bare metal, only the `<interface_name>.<vlan_number>` VLAN format is supported.
* `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface.
* `spec.desiredState.interfaces.type` defines the type of interface. This example creates a VLAN.
* `spec.desiredState.interfaces.state` defines the requested state for the interface after creation.
* `spec.desiredState.interfaces.vlan.base-iface` defines the node NIC to which the VLAN is attached.
* `spec.desiredState.interfaces.vlan.id` defines the VLAN tag.

**Additional resources**

* [Configuring an SR-IOV network device](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/#configuring-sriov-device)
* [Configuring hardware offloading](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/hardware_networks/#configuring-hardware-offloading)

#### [1.9.4. Example: Bond interface node network configuration policy](#virt-example-bond-nncp_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can create a bond interface on nodes in the cluster by applying a `NodeNetworkConfigurationPolicy` manifest to the cluster.

Note

OpenShift Container Platform only supports the following bond modes:

* `active-backup`
* `balance-xor`
* `802.3ad`

Other bond modes are not supported.

The `balance-xor` and `802.3ad` bond modes require switch configuration to establish an "EtherChannel" or similar port grouping. Those two modes also require additional load-balancing configuration, depending on the source and destination of traffic being passed through the interface. The `active-backup` bond mode does not require any switch configuration. Other bond modes are not supported.

The following YAML file is an example of a manifest for a bond interface. It includes samples values that you must replace with your own information.

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: bond0-eth1-eth2-policy
spec:
  nodeSelector:
    kubernetes.io/hostname: <node01>
  desiredState:
    interfaces:
    - name: bond0
      description: Bond with ports eth1 and eth2
      type: bond
      state: up
      ipv4:
        dhcp: true
        enabled: true
      link-aggregation:
        mode: active-backup
        options:
          miimon: '140'
        port:
        - eth1
        - eth2
      mtu: 1450
```

* `metadata.name` defines the name of the policy.
* `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes.
* `spec.nodeSelector.kubernetes.io/hostname` uses a hostname node selector.
* `spec.desiredState.interfaces.name` defines the name of the interface.
* `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface.
* `spec.desiredState.interfaces.type` defines the type of interface. This example creates a bond.
* `spec.desiredState.interfaces.state` defines the requested state for the interface after creation.
* `spec.desiredState.interfaces.ipv4.dhcp` is optional. If you do not use `dhcp`, you can either set a static IP or leave the interface without an IP address.
* `spec.desiredState.interfaces.ipv4.enabled` defines that `ipv4` is enabled in this example.
* `spec.desiredState.interfaces.link-aggregation.mode` defines the driver mode for the bond. This example uses `active backup`.
* `spec.desiredState.interfaces.link-aggregation.options.miimon` is optional and defines that miimon is used to inspect the bond link every 140ms.
* `spec.desiredState.interfaces.link-aggregation.port` defines the subordinate node NICs in the bond.
* `spec.desiredState.interfaces.mtu` is optional and defines the maximum transmission unit (MTU) for the bond. If not specified, this value is set to `1500` by default.

#### [1.9.5. Example: Multiple interfaces in the same node network configuration policy](#virt-example-nmstate-multiple-interfaces_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can create multiple interfaces in the same node network configuration policy. These interfaces can reference each other, allowing you to build and deploy a network configuration by using a single policy manifest.

Important

If multiple interfaces use the same default configuration, a single Network Manager connection profile activates on multiple interfaces simultaneously and this causes connections to have the same universally unique identifier (UUID). To avoid this issue, ensure that each interface has a specific configuration that is different from the default configuration.

The following example YAML file creates a bond that is named `bond10` across two NICs and VLAN that is named `bond10.103` that connects to the bond.

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: bond-vlan
spec:
  nodeSelector:
    kubernetes.io/hostname: <node01>
  desiredState:
    interfaces:
    - name: bond10
      description: Bonding eth2 and eth3
      type: bond
      state: up
      link-aggregation:
        mode: balance-xor
        options:
          miimon: '140'
        port:
        - eth2
        - eth3
    - name: bond10.103
      description: vlan using bond10
      type: vlan
      state: up
      vlan:
         base-iface: bond10
         id: 103
      ipv4:
        dhcp: true
        enabled: true
```

* `metadata.name` defines the name of the policy.
* `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes.
* `spec.nodeSelector.kubernetes.io/hostname` uses a hostname node selector.
* `spec.desiredState.interfaces.name` defines the name of the interface.
* `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface.
* `spec.desiredState.interfaces.type` defines the type of interface.
* `spec.desiredState.interfaces.state` defines the requested state for the interface after creation.
* `spec.desiredState.interfaces.link-aggregation.mode` defines the driver mode for the bond.
* `spec.desiredState.interfaces.link-aggregation.options.miimon` is optional and defines that miimon is used to inspect the bond link every 140ms.
* `spec.desiredState.interfaces.link-aggregation.port` defines the subordinate node NICs in the bond.
* `spec.desiredState.interfaces.vlan.base-iface` defines the node NIC to which the VLAN is attached.
* `spec.desiredState.interfaces.vlan.id` defines the VLAN tag.
* `spec.desiredState.interfaces.ipv4.dhcp` is optional. If you do not use dhcp, you can either set a static IP or leave the interface without an IP address.
* `spec.desiredState.interfaces.ipv4.enabled` defines that ipv4 is enabled in this example.

#### [1.9.6. Example: Node network configuration policy for virtual functions](#virt-example-vf-host-services_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can update host network settings for Single Root I/O Virtualization (SR-IOV) network virtual functions (VF) in an existing cluster by applying a `NodeNetworkConfigurationPolicy` manifest.

You can apply a `NodeNetworkConfigurationPolicy` manifest to an existing cluster to complete the following tasks:

* Configure QoS host network settings for VFs to optimize performance.
* Add, remove, or update VFs for a network interface.
* Manage VF bonding configurations.

Note

To update host network settings for SR-IOV VFs by using NMState on physical functions that are also managed through the SR-IOV Network Operator, you must set the `externallyManaged` parameter in the relevant `SriovNetworkNodePolicy` resource to `true`. For more information, see the *Additional resources* section.

The following YAML file is an example of a manifest that defines QoS policies for a VF. This YAML includes samples values that you must replace with your own information.

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: qos
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  desiredState:
    interfaces:
      - name: ens1f0
        description: Change QOS on VF0
        type: ethernet
        state: up
        ethernet:
         sr-iov:
           total-vfs: 3
           vfs:
           - id: 0
             max-tx-rate: 200
```

* `metadata.name` defines the name of the policy.
* `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes.
* `spec.nodeSelector.node-role.kubernetes.io/worker` defines that this example applies to all nodes with the `worker` role.
* `spec.desiredState.interfaces.name` defines the name of the physical function (PF) network interface.
* `spec.desiredState.interfaces.description` is optional and defines a human-readable description of the interface.
* `spec.desiredState.interfaces.type` defines the type of interface.
* `spec.desiredState.interfaces.state` defines the requested state for the interface after configuration.
* `spec.desiredState.interfaces.ethernet.sr-iov.total-vfs` defines the total number of VFs.
* `spec.desiredState.interfaces.ethernet.sr-iov.vfs.id` defines the VF ID. In this example, the VF has an ID of `0`.
* `spec.desiredState.interfaces.ethernet.sr-iov.vfs.max-tx-rate` defines a maximum transmission rate, in Mbps, for the VF. This sample value sets a rate of 200 Mbps.

The following YAML file is an example of a manifest that adds a VF for a network interface.

In this sample configuration, the `ens1f1v0` VF is created on the `ens1f1` physical interface, and this VF is added to a bonded network interface `bond0`. The bond uses `active-backup` mode for redundancy. In this example, the VF is configured to use hardware offloading to manage the VLAN directly on the physical interface.

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: addvf
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  maxUnavailable: 3
  desiredState:
    interfaces:
      - name: ens1f1
        type: ethernet
        state: up
        ethernet:
            sr-iov:
              total-vfs: 1
              vfs:
                - id: 0
                  trust: true
                  vlan-id: 477
      - name: bond0
        description: Attach VFs to bond
        type: bond
        state: up
        link-aggregation:
          mode: active-backup
          options:
            primary: ens1f0v0
          port:
            - ens1f0v0
            - ens1f1v0
```

* `metadata.name` defines the name of the policy.
* `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes.
* `spec.nodeSelector.node-role.kubernetes.io/worker` defines that the example applies to all nodes with the `worker` role.
* `spec.desiredState.interfaces[0].name` defines the name of the VF network interface.
* `spec.desiredState.interfaces[0].ethernet.sr-iov.total-vfs` defines the number of VFs to create.
* `spec.desiredState.interfaces[0].ethernet.sr-iov.vfs.trust` defines a setting to allow failover bonding between the active and backup VFs.
* `spec.desiredState.interfaces[0].ethernet.sr-iov.vfs.vlan-id` defines the ID of the VLAN. The example uses hardware offloading to define a VLAN directly on the VF.
* `spec.desiredState.interfaces[1].name` defines the name of the bonding network interface.
* `spec.desiredState.interfaces[1].description` is optional and defines a human-readable description of the interface.
* `spec.desiredState.interfaces[1].type` defines the type of interface.
* `spec.desiredState.interfaces[1].state` defines the requested state for the interface after configuration.
* `spec.desiredState.interfaces[1].link-aggregation.mode` defines the bonding policy for the bond.
* `spec.desiredState.interfaces[1].link-aggregation.options.primary` defines the primary attached bonding port.
* `spec.desiredState.interfaces[1].link-aggregation.port` defines the ports for the bonded network interface. In this example, `ens1f1v0` is the VLAN network interface added as an additional interface to the bonded network interface.

#### [1.9.7. Example: Network interface with a VRF instance node network configuration policy](#virt-example-host-vrf_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can associate a Virtual Routing and Forwarding (VRF) instance with a network interface by applying a `NodeNetworkConfigurationPolicy` custom resource (CR).

By associating a VRF instance with a network interface, you can support traffic isolation, independent routing decisions, and the logical separation of network resources.

Warning

When configuring Virtual Route Forwarding (VRF), you must change the VRF value to a table ID lower than `1000` because a value higher than `1000` is reserved for OpenShift Container Platform.

In a bare-metal environment, you can announce load balancer services through interfaces belonging to a VRF instance by using MetalLB. For more information, see the *Additional resources* section.

The following YAML file is an example of associating a VRF instance to a network interface. It includes samples values that you must replace with your own information.

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: vrfpolicy
spec:
  nodeSelector:
    vrf: "true"
  maxUnavailable: 3
  desiredState:
    interfaces:
      - name: ens4vrf
        type: vrf
        state: up
        vrf:
          port:
            - ens4
          route-table-id: 2
```

* `metadata.name` defines the name of the policy.
* `spec.nodeSelector.vrf` defines a node selector. This example applies the policy to all nodes with the label `vrf:true`.
* `spec.desiredState.interfaces.name` defines the name of the interface.
* `spec.desiredState.interfaces.type` defines the type of interface. This example creates a VRF instance.
* `spec.desiredState.interfaces.vrf.port` defines the node interface to which the VRF attaches.
* `spec.desiredState.interfaces.vrf.route-table-id` defines the route table ID for the VRF.

#### [1.9.8. Example: Network interface with a predictable route table ID](#virt-example-predictable-route-table-id_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

To simplify network administration and reduce configuration errors in OpenShift Container Platform, configure routes by using names instead of Virtual Routing and Forwarding (VRF) routing table ID numbers.

Using human-readable names ensures that network routes are easier to identify and maintain without tracking abstract numerical identifiers.

The following `NodeNetworkConfigurationPolicy` (NNCP) YAML file shows an example of creating a VRF instance and applying a route to the VRF instance. The VRF instance uses the stable method of referencing the VRF by name rather than a potentially shifting ID.

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: vrf-predictable-policy
spec:
  nodeSelector:
    vrf: "true"
  maxUnavailable: 3
  desiredState:
    interfaces:
      - name: vrf0
        type: vrf
        state: up
        vrf:
          route-table-id: 100
          port:
            - eth1
            - eth2
    routes:
      config:
        - destination: 198.51.200.0/24
          route-type: blackhole
          vrf-name: vrf0
# ...
```

where:

`spec.nodeSelector.vrf`
:   Specifies the application of the policy only to nodes that have the `vrf: true` label. This configuration prevents accidental network changes on nodes that do not require VRF support.

`spec.desiredState.interfaces.type`
:   Specifies the creation of a VRF-type interface.

`spec.desiredState.interfaces.vrf.route-table-id`
:   Specifies the `route-table-id` that the `vrf` name maps to in the routing table.

`spec.desiredState.routes.config.route-type`
:   Specifies the route type. NetworkManager supports the `unicast`, `local`, `blackhole`, `unreachable`, `prohibit`, and `throw` route types. The default is unicast. The example sets a `blackhole` route that drops any packets within the IP address range of this route. The range for the `blackhole` route is the destination CIDR, such as `198.51.200.0/24`.

`spec.desiredState.routes.config.vrf-name`
:   Specifies a stable link in that if a policy changes the `route-table-id` parameter to a different value, the route automatically follows the `vrf0` name to the new ID. You do not need to manually update the route configuration.

### [1.10. Creating an IP over InfiniBand interface on nodes](#virt-creating-infiniband-interface-on-nodes_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

On the OpenShift Container Platform web console, you can install a Red Hat certified third-party Operator, such as the NVIDIA Network Operator, that supports IP over InfiniBand (IPoIB) mode. Typically, you would use the third-party Operator with other vendor infrastructure to manage resources in an OpenShift Container Platform cluster.

To create an IPoIB interface on nodes in your cluster, you must define an InfiniBand (IPoIB) interface in a `NodeNetworkConfigurationPolicy` (NNCP) manifest file.

If you need to attach IPoIB to a bond interface, only the `active-backup` mode supports this configuration.

Important

The OpenShift Container Platform documentation describes defining only the IPoIB interface configuration in a `NodeNetworkConfigurationPolicy` (NNCP) manifest file. You must refer to the NVIDIA and other third-party vendor documentation for the majority of the configuring steps. Red Hat support does not extend to anything external to the NNCP configuration.

For more information about the NVIDIA Operator, see [Getting Started with Red Hat OpenShift](https://docs.nvidia.com/networking/display/kubernetes2410/getting+started+with+red+hat+openshift) (NVIDIA Docs Hub).

**Prerequisites**

* You installed a Red Hat certified third-party Operator that supports an IPoIB interface.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Create or edit a `NodeNetworkConfigurationPolicy` (NNCP) manifest file, and then specify an IPoIB interface in the file.

   ```
   apiVersion: nmstate.io/v1
   kind: NodeNetworkConfigurationPolicy
   metadata:
     name: worker-0-ipoib
   spec:
   # ...
       interfaces:
       - description: ""
         infiniband:
           mode: datagram
           pkey: "0xffff"
         ipv4:
           address:
           - ip: 100.125.3.4
             prefix-length: 16
           dhcp: false
           enabled: true
         ipv6:
           enabled: false
         name: ibp27s0
         state: up
         identifier: mac-address
         mac-address: 20:00:55:04:01:FE:80:00:00:00:00:00:00:00:02:C9:02:00:23:13:92
         type: infiniband
   # ...
   ```

   where:

   `<mode>`
   :   `datagram` is the default mode for an IPoIB interface. This mode provides improved CPU performance and low-latency capabilitities for pod-to-pod communication. `connected` mode is a supported mode but consider only using this mode when you need to adjust the maximum transmission unit (MTU) value to improve node connectivity with surrounding network devices.

   `<pkey>`
   :   Supports a string or an integer value. The parameter defines the protection key, or *P-key*, for the interface for the purposes of authentication and encrypted communications with a third-party vendor, such as NVIDIA. Values `None` and `0xffff` indicate the protection key for the base interface in an InfiniBand system.

   `<identifier>`
   :   Supported values include `name`, the default value, and `mac-address`. The `name` value applies a configuration to an interface that holds a specified interface name.

   `<mac-address>`
   :   Holds the MAC address of an interface. For an IP-over-InfiniBand (IPoIB) interface, the address is a 20-byte string.

   `<type>`
   :   Sets the type of interface to `infiniband`.
2. Apply the NNCP configuration to each node in your cluster by running the following command. The Kubernetes NMState Operator can then create an IPoIB interface on each node.

   ```
   $ oc apply -f <nncp_file_name>
   ```

   where:

   `<nncp_file_name>`
   :   Replace `<nncp_file_name>` with the name of your NNCP file.

### [1.11. Example policy configurations that use dynamic matching and templating](#virt-example-dynamic-matching-templating_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

The following example configuration snippets show node network policies that use dynamic matching and templating.

Important

Applying node network configuration policies that use dynamic matching and templating is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

#### [1.11.1. Example: Linux bridge interface node network configuration policy to inherit static IP address from the NIC attached to the bridge](#virt-example-inherit-static-ip-from-nic_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

Create a Linux bridge interface on nodes in the cluster and transfer the static IP configuration of the NIC to the bridge by applying a single `NodeNetworkConfigurationPolicy` manifest to the cluster.

The following YAML file is an example of a manifest for a Linux bridge interface. It includes sample values that you must replace with your own information.

```
apiVersion: nmstate.io/v1
kind: NodeNetworkConfigurationPolicy
metadata:
  name: br1-eth1-copy-ipv4-policy
spec:
  nodeSelector:
    node-role.kubernetes.io/worker: ""
  capture:
    eth1-nic: interfaces.name=="eth1"
    eth1-routes: routes.running.next-hop-interface=="eth1"
    br1-routes: capture.eth1-routes | routes.running.next-hop-interface := "br1"
  desiredState:
    interfaces:
      - name: br1
        description: Linux bridge with eth1 as a port
        type: linux-bridge
        state: up
        ipv4: "{{ capture.eth1-nic.interfaces.0.ipv4 }}"
        bridge:
          options:
            stp:
              enabled: false
          port:
            - name: eth1
     routes:
        config: "{{ capture.br1-routes.routes.running }}"
```

* `metadata.name` defines the name of the policy.
* `spec.nodeSelector` defines the nodes in the cluster the networking policy is applied to. If not defined, the default is all nodes. This example uses the `node-role.kubernetes.io/worker: ""` node selector to select all worker nodes in the cluster.
* `spec.capture.eth1-nic` defines the reference to the node NIC to which the bridge attaches.
* `spec.desiredState.interfaces.type` defines the type of interface. This example creates a bridge.
* `spec.desiredState.interfaces.ipv4` defines the IP address of the bridge interface. This value matches the IP address of the NIC which is referenced by the `spec.capture.eth1-nic` entry.
* `spec.desiredState.interfaces.bridge.port.name` defines the node NIC to which the bridge attaches.

**Additional resources**

* [The NMPolicy project - Policy syntax](https://nmstate.io/nmpolicy/user-guide/102-policy-syntax.html)

### [1.12. Examples: IP management](#virt-example-nmstate-IP-management_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

The following example configuration snippets show different methods of IP management.

These examples use the `ethernet` interface type to simplify the example while showing the related context in the policy configuration. These IP management examples can be used with the other interface types.

#### [1.12.1. Static](#virt-example-nmstate-IP-management-static_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

The following snippet statically configures an IP address on the Ethernet interface:

```
# ...
    interfaces:
    - name: eth1
      description: static IP on eth1
      type: ethernet
      state: up
      ipv4:
        dhcp: false
        address:
        - ip: 192.168.122.250
          prefix-length: 24
        enabled: true
# ...
```

where:

`192.168.122.250`
:   Specifies the static IP address for the interface.

#### [1.12.2. No IP address](#virt-example-nmstate-IP-management-no-ip_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

The following snippet ensures that the interface has no IP address:

```
# ...
    interfaces:
    - name: eth1
      description: No IP on eth1
      type: ethernet
      state: up
      ipv4:
        enabled: false
# ...
```

Important

Always set the `state` parameter to `up` when you set both the `ipv4.enabled` and the `ipv6.enabled` parameter to `false` to disable an interface. If you set `state: down` with this configuration, the interface receives a DHCP IP address because of automatic DHCP assignment.

#### [1.12.3. Dynamic host configuration](#virt-example-nmstate-IP-management-dhcp_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

The following snippet configures an Ethernet interface that uses a dynamic IP address, gateway address, and DNS:

```
# ...
    interfaces:
    - name: eth1
      description: DHCP on eth1
      type: ethernet
      state: up
      ipv4:
        dhcp: true
        enabled: true
# ...
```

The following snippet configures an Ethernet interface that uses a dynamic IP address but does not use a dynamic gateway address or DNS:

```
# ...
    interfaces:
    - name: eth1
      description: DHCP without gateway or DNS on eth1
      type: ethernet
      state: up
      ipv4:
        dhcp: true
        auto-gateway: false
        auto-dns: false
        enabled: true
# ...
```

#### [1.12.4. Media Access Control (MAC) address](#virt-example-nmstate-IP-management-mac_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can use a MAC address to identify a network interface instead of using the name of the network interface. A network interface name can change for various reasons, such as an operating system configuration change. However, every network interface has a unique MAC address that does not change. This means that using a MAC address is a more permanent way to identify a specific network interface.

Supported values for the `identifier` parameter include the default `name` value and the value `mac-address`. The `name` value applies a configuration to an interface that holds a specified interface name.

Using a `mac-address` value for the `identifier` parameter indicates that a MAC address is the identifier for the network interface. If you set the `identifier` value to `mac-address`, you must enter a specific MAC address in the following `mac-address` parameter field.

Note

You can still specify a value for the `name` parameter, but setting the `identifier: mac-address` value means that a MAC address is used as the primary identifier for a network interface. If you specify an incorrect MAC address, `nmstate` reports an invalid argument error.

The following snippet specifies a MAC address as the primary identifier for an Ethernet device, named `eth1`, with a MAC address of `8A:8C:92:1A:F6:98`:

```
# ...
interfaces:
- name: eth1
  profile-name: wan0
  type: ethernet
  state: up
  identifier: mac-address
  mac-address: 8A:8C:92:1A:F6:98
# ...
```

#### [1.12.5. PCI address](#virt-example-nmstate-IP-management-pci_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can use a peripheral component interconnect (PCI) address to identify a network interface based on hardware slot location rather than using the interface name or MAC address. PCI address matching is useful when interface names vary across nodes but hardware slot locations remain consistent.

Set the `identifier` value to `pci-address` to identify a network interface by its PCI address. You must enter a specific PCI address in the `pci-address` parameter field. The PCI address must use the format `domain:bus:device.function`, for example, `0000:01:00.0`.

Note

You can still specify a value for the `name` parameter, but setting the `identifier: pci-address` value means that a PCI address is used as the primary identifier for a network interface.

The following snippet specifies a PCI address as the primary identifier for an Ethernet device:

```
# ...
interfaces:
- name: sriov-nic
  type: ethernet
  state: up
  identifier: pci-address
  pci-address: "0000:86:00.0"
  ipv4:
    enabled: false
# ...
```

#### [1.12.6. DNS](#virt-example-nmstate-IP-management-dns_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

By default, the `nmstate` API stores DNS values globally as against storing them in a network interface. For certain situations, you must configure a network interface to store DNS values.

Tip

Setting a DNS configuration is comparable to modifying the `/etc/resolv.conf` file.

To define a DNS configuration for a network interface, you must initially specify the `dns-resolver` section in the network interface’s YAML configuration file. To apply an NNCP configuration to your network interface, you need to run the `oc apply -f <nncp_file_name>` command.

The following example shows a default situation that stores DNS values globally:

* Configure a static DNS without a network interface. Note that when updating the `/etc/resolv.conf` file on a host node, you do not need to specify an interface, IPv4 or IPv6, in the `NodeNetworkConfigurationPolicy` (NNCP) manifest.

  Important

  During pod creation, Kubernetes uses the `/etc/resolv.conf` file that exists on a node. If you modify the `/etc/resolv.conf` file on a host node, the changes do not propagate to the `/etc/resolv.conf` file that exists in a container. You must re-create the container for changes to take effect.

  Example of a DNS configuration for a network interface that globally stores DNS values:

  ```
  apiVersion: nmstate.io/v1
  kind: NodeNetworkConfigurationPolicy
  metadata:
   name: worker-0-dns-testing
  spec:
    nodeSelector:
      kubernetes.io/hostname: <target_node>
    desiredState:
      dns-resolver:
        config:
          server:
          - 2001:db8:f::1
          - 192.0.2.251
          search:
          - example.com
          - example.org
  # ...
  ```

  Important

  You can specify DNS options under the `dns-resolver.config` section of your NNCP file as demonstrated in the following example:

  ```
  # ...
  desiredState:
      dns-resolver:
        config:
          options:
           - timeout:2
           - attempts:3
  # ...
  ```

  If you want to remove the DNS options from your network interface, apply the following configuration to your NNCP and then run the `oc apply -f <nncp_file_name>` command:

  ```
  # ...
      dns-resolver:
        config: {}
      interfaces: []
  # ...
  ```

The following examples show situations that require configuring a network interface to store DNS values:

* If you want to rank a static DNS name server over a dynamic DNS name server, define the interface that runs either the Dynamic Host Configuration Protocol (DHCP) or the IPv6 Autoconfiguration (`autoconf`) mechanism in the network interface YAML configuration file.

  Example configuration that adds `192.0.2.1` to DNS name servers retrieved from the DHCPv4 network protocol:

  ```
  # ...
  dns-resolver:
    config:
      server:
      - 192.0.2.1
  interfaces:
    - name: eth1
      type: ethernet
      state: up
      ipv4:
        enabled: true
        dhcp: true
        auto-dns: true
  # ...
  ```
* If you need to configure a network interface to store DNS values instead of adopting the default method, which uses the `nmstate` API to store DNS values globally, you can set static DNS values and static IP addresses in the network interface YAML file.

  Important

  Storing DNS values at the network interface level might cause name resolution issues after you attach the interface to network components, such as an Open vSwitch (OVS) bridge, a Linux bridge, or a bond.

  Example configuration that stores DNS values at the interface level:

  ```
  # ...
  dns-resolver:
    config:
      server:
      - 2001:db8:1::d1
      - 2001:db8:1::d2
      - 192.0.2.1
      search:
      - example.com
      - example.org
  interfaces:
    - name: eth1
      type: ethernet
      state: up
      ipv4:
        address:
        - ip: 192.0.2.251
          prefix-length: 24
        dhcp: false
        enabled: true
      ipv6:
        address:
        - ip: 2001:db8:1::1
          prefix-length: 64
        dhcp: false
        enabled: true
        autoconf: false
  # ...
  ```
* If you want to set static DNS search domains and static DNS name servers for your network interface, define the static interface that runs either the Dynamic Host Configuration Protocol (DHCP) or the IPv6 Autoconfiguration (`autoconf`) mechanism in the network interface YAML configuration file.

  Important

  Specifying the following `dns-resolver` configurations in the network interface YAML file might cause a race condition at reboot that prevents the `NodeNetworkConfigurationPolicy` (NNCP) from applying to pods that run in your cluster:

  + Setting static DNS search domains and dynamic DNS name servers for your network interface.
  + Specifying domain suffixes for the `search` parameter and not setting IP addresses for the `server` parameter.

  Example configuration that sets `example.com` and `example.org` static DNS search domains along with static DNS name server settings:

  ```
  # ...
  dns-resolver:
    config:
      server:
      - 2001:db8:f::1
      - 192.0.2.251
      search:
      - example.com
      - example.org
  interfaces:
    - name: eth1
      type: ethernet
      state: up
      ipv4:
        enabled: true
        dhcp: true
        auto-dns: true
      ipv6:
        enabled: true
        dhcp: true
        autoconf: true
        auto-dns: true
  # ...
  ```

### [1.13. Enable IP forwarding on specific interfaces](#nw-nmstate-enable-per-interface-ip-forwarding_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

You can enable IPv4 forwarding on specific network interfaces by configuring the `forwarding` field in a `NodeNetworkConfigurationPolicy` custom resource (CR).

Enabling IP forwarding is useful when you need specific secondary network interfaces to forward IP packets. For example, MetalLB load balancers on secondary network interfaces require IP forwarding to function. IP forwarding at the interface level enables this functionality, while retaining global forwarding rules that still disable IP forwarding at the node or cluster level.

Important

The Kubernetes NMState Operator configures forwarding on secondary network interfaces for IPv4 packets only.

**Prerequisites**

* You installed Kubernetes NMState Operator.
* You have access to the cluster as a user with the `cluster-admin` role.
* You have identified the network interfaces that require IPv4 forwarding.
* You have installed the OpenShift CLI (`oc`).

**Procedure**

1. Create a `NodeNetworkConfigurationPolicy` manifest file to enable IP forwarding on the target interface:

   ```
   apiVersion: nmstate.io/v1
   kind: NodeNetworkConfigurationPolicy
   metadata:
     name: enable-forwarding-eth1
   spec:
     nodeSelector:
       node-role.kubernetes.io/worker: ""
     desiredState:
       interfaces:
       - name: eth1
         type: ethernet
         state: up
         ipv4:
           enabled: true
           forwarding: true
   ```

   where:

   * `metadata.name` defines the name of the policy.
   * `spec.nodeSelector` specifies which nodes to apply the policy to based on node labels or roles.
   * `interfaces.name` defines the name of the interface on which to enable IP forwarding. This can be a physical, bond, or VLAN interface.
   * `interfaces.ipv4.enabled` defines whether the IPv4 protocol is active.
   * `interfaces.ipv4.forwarding` specifies whether IPv4 forwarding is enabled on the interface. Setting this to `true` enables IPv4 forwarding on the interface.
2. Apply the policy by running the following command:

   ```
   $ oc apply -f enable-forwarding-eth1.yaml
   ```

**Verification**

1. Verify that the policy was applied successfully by running the following command:

   ```
   $ oc get nncp
   ```

   **Example output**

   ```
   NAME                      STATUS      REASON
   enable-forwarding-eth1    Available   SuccessfullyConfigured
   ```

   The `SuccessfullyConfigured` status indicates that the policy was successfully applied.
2. Start a debug session on a target node and access the root file system:

   ```
   $ oc debug node/<node_name>
   # chroot /host
   ```

   * Replace `<node_name>` with the name of the node.
3. Verify that IP forwarding is enabled on the interface:

   ```
   # sysctl net.ipv4.conf.eth1.forwarding
   ```

   **Example output**

   ```
   net.ipv4.conf.eth1.forwarding = 1
   ```

   A value of `1` indicates that IPv4 forwarding is enabled on the interface.

### [1.14. Routes and route rules](#virt-routes-route-rules_k8s-nmstate-updating-node-network-config) Copy linkLink copied to clipboard!

After you configure an IP address for a network interface, you can configure routes and route rules in the NMState configuration for cluster nodes.

Important

You cannot use the OVN-Kubernetes `br-ex` bridge as the next hop interface when configuring a static route unless you manually configured a customized `br-ex` bridge.

For more information, see "Creating a manifest object that includes a customized br-ex bridge" in the *Deploying installer-provisioned clusters on bare metal* document or the *Installing a user-provisioned cluster on bare metal* document.

The `routes` parameter defines static routes and these routes determine the traffic that leaves the network interfaces and the destination network for the traffic. Supported values include `running` and `config`.

Note

After you apply an NMState configuration to cluster nodes and you want to change existing routes, you must specify the old route with the `state: absent` parameter and the new route with the `state: present` parameter. The NMState Operator can then delete the old route and apply the new route to cluster nodes.

Setting the `state` parameter to `ignore` means that the Operator ignores certain routes.

The `route-rules` parameter implements a policy-based routing capability for cluster nodes. This capability allows traffic that originates from a different source IP address to be segregated and routed through different gateways and network paths.

The following YAML configuration shows a static route and a static IP confiuration on interface `eth1`:

```
dns-resolver:
  config:
# ...
interfaces:
  - name: eth1
    description: Static routing on eth1
    type: ethernet
    state: up
    ipv4:
      dhcp: false
      enabled: true
      address:
        - ip: 192.0.2.251
          prefix-length: 24
route-rules:
  config:
  - ip-from: 198.51.100.0/24
    priority: 1000
    route-table: 200
routes:
  config:
  - destination: 198.51.100.0/24
    next-hop-interface: eth1
    next-hop-address: 192.0.2.1
    metric: 150
    table-id: 200
# ...
```

* `config.ip-from`: Applies a rule to any network packet that originates from the specified IP address.
* `config.priority`: Sets the priority order for the rule.
* `config.route-table`: Specifies the routing table that the Operator uses to check that network traffic matches the `ip-from` condition.
* `address.ip`: The static IP address for the Ethernet interface.
* `config.next-hop-address`: The next hop address for the node traffic. This must be in the same subnet as the IP address set for the Ethernet interface.

**Additional resources**

* [Creating a manifest object that includes a customized br-ex bridge (Installer-provisioned infrastructure)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#creating-manifest-file-customized-br-ex-bridge_ipi-install-installation-workflow)
* [Creating a manifest object that includes a customized br-ex bridge (User-provisioned infrastructure)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_bare_metal/#creating-manifest-file-customized-br-ex-bridge_installing-bare-metal)
* [Routes (nmstate documentation)](https://nmstate.io/devel/yaml_api.html#routes)
* [Route Rules (nmstate documentation)](https://nmstate.io/devel/yaml_api.html#route-rules)

## [Chapter 2. Troubleshooting node network configuration](#k8s-nmstate-troubleshooting-node-network) Copy linkLink copied to clipboard!

If the node network configuration encounters an issue, the policy is automatically rolled back and the enactments report failure. This includes issues such as:

* The configuration fails to be applied on the host.
* The host loses connection to the default gateway.
* The host loses connection to the API server.

### [2.1. Troubleshooting an incorrect node network configuration policy configuration](#virt-troubleshooting-incorrect-policy-config_k8s-nmstate-troubleshooting-node-network) Copy linkLink copied to clipboard!

You can apply changes to the node network configuration across your entire cluster by applying a node network configuration policy. If you applied an incorrect configuration, you can use the following example to troubleshoot and correct the failed node network policy.

The example attempts to apply a Linux bridge policy to a cluster that has three control plane nodes and three compute nodes. The policy is not applied because the policy references the wrong interface.

To find an error, you need to investigate the available NMState resources. You can then update the policy with the correct configuration.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You ensured that an `ens01` interface does not exist on your Linux system.

**Procedure**

1. Create a policy on your cluster. The following example creates a simple bridge, `br1` that has `ens01` as its member:

   ```
   apiVersion: nmstate.io/v1
   kind: NodeNetworkConfigurationPolicy
   metadata:
     name: ens01-bridge-testfail
   spec:
     desiredState:
       interfaces:
         - name: br1
           description: Linux bridge with the wrong port
           type: linux-bridge
           state: up
           ipv4:
             dhcp: true
             enabled: true
           bridge:
             options:
               stp:
                 enabled: false
             port:
               - name: ens01
   # ...
   ```
2. Apply the policy to your network interface:

   ```
   $ oc apply -f ens01-bridge-testfail.yaml
   ```

   Example output:

   ```
   nodenetworkconfigurationpolicy.nmstate.io/ens01-bridge-testfail created
   ```
3. Verify the status of the policy by running the following command:

   ```
   $ oc get nncp
   ```

   The output shows that the policy failed:

   ```
   NAME                    STATUS
   ens01-bridge-testfail   FailedToConfigure
   ```

   The policy status alone does not indicate if it failed on all nodes or a subset of nodes.
4. List the node network configuration enactments to see if the policy was successful on any of the nodes. If the policy failed for only a subset of nodes, the output suggests that the problem is with a specific node configuration. If the policy failed on all nodes, the output suggests that the problem is with the policy.

   ```
   $ oc get nnce
   ```

   The output shows that the policy failed on all nodes:

   ```
   NAME                                         STATUS
   control-plane-1.ens01-bridge-testfail        FailedToConfigure
   control-plane-2.ens01-bridge-testfail        FailedToConfigure
   control-plane-3.ens01-bridge-testfail        FailedToConfigure
   compute-1.ens01-bridge-testfail              FailedToConfigure
   compute-2.ens01-bridge-testfail              FailedToConfigure
   compute-3.ens01-bridge-testfail              FailedToConfigure
   ```
5. View one of the failed enactments. The following command uses the output tool `jsonpath` to filter the output:

   ```
   $ oc get nnce compute-1.ens01-bridge-testfail -o jsonpath='{.status.conditions[?(@.type=="Failing")].message}'
   ```

   Example output:

   ```
   [2024-10-10T08:40:46Z INFO  nmstatectl] Nmstate version: 2.2.37
   NmstateError: InvalidArgument: Controller interface br1 is holding unknown port ens01
   ```

   The previous example shows the output from an `InvalidArgument` error that indicates that the `ens01` is an unknown port. For this example, you might need to change the port configuration in the policy configuration file.
6. To ensure that the policy is configured properly, view the network configuration for one or all of the nodes by requesting the `NodeNetworkState` object. The following command returns the network configuration for the `control-plane-1` node:

   ```
   $ oc get nns control-plane-1 -o yaml
   ```

   The output shows that the interface name on the nodes is `ens1` but the failed policy incorrectly uses `ens01`:

   ```
      - ipv4:
   # ...
         name: ens1
         state: up
         type: ethernet
   ```
7. Correct the error by editing the existing policy:

   ```
   $ oc edit nncp ens01-bridge-testfail
   ```

   ```
   # ...
             port:
               - name: ens1
   ```

   Save the policy to apply the correction.
8. Check the status of the policy to ensure it updated successfully:

   ```
   $ oc get nncp
   ```

   Example output:

   ```
   NAME                    STATUS
   ens01-bridge-testfail   SuccessfullyConfigured
   ```

   The updated policy is successfully configured on all nodes in the cluster.

### [2.2. Troubleshooting DNS connectivity issues in a disconnected environment](#troubleshooting-dns-disconnected-env_k8s-nmstate-troubleshooting-node-network) Copy linkLink copied to clipboard!

If you experience health check probe issues when configuring `nmstate` in a disconnected environment, you can configure the DNS server to resolve the custom domain name instead of the default `root-servers.net` domain.

Important

Ensure that the DNS server includes a name server (NS) entry for the `root-servers.net` zone. The DNS server does not need to forward a query to an upstream resolver, but the server must return a correct answer for the NS query.

#### [2.2.1. Configuring the bind9 DNS named server](#k8s-nmstate-troubleshooting-dns-disconnected-bind9-dns_k8s-nmstate-troubleshooting-node-network) Copy linkLink copied to clipboard!

For a cluster configured to query a `bind9` DNS server, you can add the `root-servers.net` zone to a configuration file that contains at least one DNS record. For example you can use the `/var/named/named.localhost` as a zone file that already matches this criteria.

**Procedure**

1. Add the `root-servers.net` zone at the end of the `/etc/named.conf` configuration file by running the following command:

   ```
   $ cat >> /etc/named.conf <<EOF
   zone "root-servers.net" IN {
       	type master;
       	file "named.localhost";
   };
   EOF
   ```
2. Restart the `named` service by running the following command:

   ```
   $ systemctl restart named
   ```
3. Confirm that the `root-servers.net` zone is present by running the following command:

   ```
   $ journalctl -u named|grep root-servers.net
   ```

   **Example output**

   ```
   Jul 03 15:16:26 rhel-8-10 bash[xxxx]: zone root-servers.net/IN: loaded serial 0
   Jul 03 15:16:26 rhel-8-10 named[xxxx]: zone root-servers.net/IN: loaded serial 0
   ```
4. Verify that the DNS server can resolve the NS record for the `root-servers.net` domain by running the following command:

   ```
   $ host -t NS root-servers.net. 127.0.0.1
   ```

   **Example output**

   ```
   Using domain server:
   Name: 127.0.0.1
   Address: 127.0.0.53
   Aliases:
   root-servers.net name server root-servers.net.
   ```

#### [2.2.2. Configuring the dnsmasq DNS server](#troubleshooting-dns-disconnected-env-dnsmasq_k8s-nmstate-troubleshooting-node-network) Copy linkLink copied to clipboard!

If you are using `dnsmasq` as the DNS server, you can delegate resolution of the `root-servers.net` domain to another DNS server, for example, by creating a new configuration file that resolves `root-servers.net` using a DNS server that you specify.

**Procedure**

1. Create a configuration file that delegates the domain `root-servers.net` to another DNS server by running the following command:

   ```
   $ echo 'server=/root-servers.net/<DNS_server_IP>'> /etc/dnsmasq.d/delegate-root-servers.net.conf
   ```
2. Restart the `dnsmasq` service by running the following command:

   ```
   $ systemctl restart dnsmasq
   ```
3. Confirm that the `root-servers.net` domain is delegated to another DNS server by running the following command:

   ```
   $ journalctl -u dnsmasq|grep root-servers.net
   ```

   **Example output**

   ```
   Jul 03 15:31:25 rhel-8-10 dnsmasq[1342]: using nameserver 192.168.1.1#53 for domain root-servers.net
   ```
4. Verify that the DNS server can resolve the NS record for the `root-servers.net` domain by running the following command:

   ```
   $ host -t NS root-servers.net. 127.0.0.1
   ```

   **Example output**

   ```
   Using domain server:
   Name: 127.0.0.1
   Address: 127.0.0.1#53
   Aliases:
   root-servers.net name server root-servers.net.
   ```

#### [2.2.3. Creating a custom DNS host name to resolve DNS connectivity issues](#k8s-nmstate-troubleshooting-dns-disconnected-env-resolv_k8s-nmstate-troubleshooting-node-network) Copy linkLink copied to clipboard!

In a disconnected environment where the external DNS server cannot be reached, you can resolve Kubernetes NMState Operator health probe issues by specifying a custom DNS host name in the `NMState` custom resource definition (CRD).

**Procedure**

1. Add the DNS host name configuration to the `NMState` CRD of your cluster:

   ```
   apiVersion: nmstate.io/v1
   kind: NMState
   metadata:
     name: nmstate
   spec:
     probeConfiguration:
       dns:
         host: redhat.com
   # ...
   ```
2. Apply the DNS host name configuration to your cluster network by running the following command. Ensure that you replace `<filename>` with the name of your CRD file.

   ```
   $ oc apply -f <filename>.yaml
   ```

## [Legal Notice](#idm140026251887840) Copy linkLink copied to clipboard!

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
