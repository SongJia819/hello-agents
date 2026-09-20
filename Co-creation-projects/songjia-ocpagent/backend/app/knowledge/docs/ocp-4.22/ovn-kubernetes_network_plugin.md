---
title: "OVN-Kubernetes network plugin"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/index
retrieved_at: 2026-09-05T05:42:43.716402+00:00
---

# OVN-Kubernetes network plugin

---

OpenShift Container Platform 4.22

## In-depth configuration and troubleshooting for the OVN-Kubernetes network plugin in OpenShift Container Platform

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140110959607360)

**Abstract**

This document provides information on the architecture, configuration, and troubleshooting of the OVN-Kubernetes network plugin in OpenShift Container Platform.

---

## [Chapter 1. About the OVN-Kubernetes network plugin](#about-ovn-kubernetes) Copy linkLink copied to clipboard!

The OpenShift Container Platform cluster uses a virtualized network for pod and service networks. The OVN-Kubernetes network plugin is the default provider that implements this virtualized overlay network by transforming configurations into OpenFlow rules to enable advanced routing and security features.

Part of Red Hat OpenShift Networking, the OVN-Kubernetes network plugin is the default network provider for OpenShift Container Platform. OVN-Kubernetes is based on Open Virtual Network (OVN) and provides an overlay-based networking implementation. A cluster that uses the OVN-Kubernetes plugin also runs Open vSwitch (OVS) on each node. OVN configures OVS on each node to implement the declared network configuration.

Note

OVN-Kubernetes is the default networking solution for OpenShift Container Platform and single-node OpenShift deployments.

OVN-Kubernetes, which arose from the OVS project, uses many of the same constructs. For example, the plugin applies OpenFlow rules to direct packet routing through the network infrastructure. For more information, see the "Open Virtual Network website".

OVN-Kubernetes is a series of daemons for OVS that transform virtual network configurations into `OpenFlow` rules. `OpenFlow` is a protocol for communicating with network switches and routers, providing a means for remotely controlling the flow of network traffic on a network device. This means that network administrators can configure, manage, and monitor the flow of network traffic.

OVN-Kubernetes provides more of the advanced functionality not available with `OpenFlow`. OVN supports distributed virtual routing, distributed logical switches, access control, Dynamic Host Configuration Protocol (DHCP), and DNS. OVN implements distributed virtual routing within logic flows that equate to open flows. For example, if you have a pod that sends out a DHCP request to the DHCP server on the network, a logic flow rule in the request enables the OVN-Kubernetes plugin to process the packet. This means that the server can respond with gateway, DNS server, IP address, and other information.

OVN-Kubernetes runs a daemon on each node. There are daemon sets for the databases and for the OVN controller that run on every node. The OVN controller programs the Open vSwitch daemon on the nodes to support the following network provider features:

* Egress IPs
* Firewalls
* Hardware offloading
* Hybrid networking
* Internet Protocol Security (IPsec) encryption
* IPv6
* Multicast.
* Network policy and network policy logs
* Routers

### [1.1. OVN-Kubernetes purpose](#nw-ovn-kubernetes-purpose_about-ovn-kubernetes) Copy linkLink copied to clipboard!

The OVN-Kubernetes network plugin is an open-source, fully-featured Kubernetes CNI plugin that uses Open Virtual Network (OVN) to manage network traffic flows. OVN is a community developed, vendor-agnostic network virtualization solution. The OVN-Kubernetes network plugin uses the following technologies:

* OVN to manage network traffic flows.
* Kubernetes network policy support and logs, including ingress and egress rules.
* The Generic Network Virtualization Encapsulation (Geneve) protocol, rather than Virtual Extensible LAN (VXLAN), to create an overlay network between nodes.

The OVN-Kubernetes network plugin supports the following capabilities:

* Hybrid clusters that can run both Linux and Microsoft Windows workloads. This environment is known as *hybrid networking*.
* Offloading of network data processing from the host central processing unit (CPU) to compatible network cards and data processing units (DPUs). This is known as *hardware offloading*.
* IPv4-primary dual-stack networking on bare-metal, VMware vSphere, IBM Power®, IBM Z®, and Red Hat OpenStack Platform (RHOSP) platforms.
* IPv6 single-stack networking on RHOSP and bare metal platforms.
* IPv6-primary dual-stack networking for a cluster running on a bare-metal, a VMware vSphere, or an RHOSP platform.
* Egress firewall devices and egress IP addresses.
* Egress router devices that operate in redirect mode.
* IPsec encryption of intracluster communications.

Red Hat does not support the following postinstallation configurations that use the OVN-Kubernetes network plugin:

* Configuring the primary network interface, including using the NMState Operator to configure bonding for the interface.
* Configuring a sub-interface or additional network interface on a network device that uses the Open vSwitch (OVS) or an OVN-Kubernetes `br-ex` bridge network.
* Creating additional virtual local area networks (VLANs) on the primary network interface.
* Using the primary network interface, such as `eth0` or `bond0`, that you created for a node during cluster installation to create additional secondary networks.

Red Hat does support the following postinstallation configurations that use the OVN-Kubernetes network plugin:

* Creating additional VLANs from the base physical interface, such as `eth0.100`, where you configured the primary network interface as a VLAN for a node during cluster installation. This works because the Open vSwitch (OVS) bridge attaches to the initial VLAN sub-interface, such as `eth0.100`, leaving the base physical interface available for new configurations.
* Creating an additional OVN secondary network with a `localnet` topology network requires that you define the secondary network in a `NodeNetworkConfigurationPolicy` (NNCP) object. After you create the network, pods or virtual machines (VMs) can then attach to the network. These secondary networks give a dedicated connection to the physical network, which might or might not use VLAN tagging. You cannot access these networks from the host network of a node where the host does not have the required setup, such as the required network settings.
* Defining additional VLANs in the `vlanID` parameter of the `NetworkAttachmentDefinition` (NAD) custom resource (CR). By mapping the `br-ex` bridge to a physical interface, the interface acts as a trunk port that can carry multiple VLANs. OVN-Kubernetes can then manage tagging and untagging of network packets, also known as *Ethernet frames*. To ensure strong connectivity, configure the physical switch ports as trunks.

### [1.2. OVN-Kubernetes IPv6 and dual-stack limitations](#nw-ovn-kubernetes-limitations_about-ovn-kubernetes) Copy linkLink copied to clipboard!

The OVN-Kubernetes network plugin has specific IPv6 and dual-stack networking configuration limitations. These limitations affect gateway configuration, routing layouts, and infrastructure environment stability.

* For clusters configured for dual-stack networking, both IPv4 and IPv6 traffic must use the same network interface as the default gateway.

  If this requirement is not met, pods on the host in the `ovnkube-node` daemon set enter the `CrashLoopBackOff` state.

  If you display a pod with a command such as `oc get pod -n openshift-ovn-kubernetes -l app=ovnkube-node -o yaml`, the `status` field has more than one message about the default gateway, as shown in the following output:

  ```
  I1006 16:09:50.985852   60651 helper_linux.go:73] Found default gateway interface br-ex 192.168.127.1
  I1006 16:09:50.985923   60651 helper_linux.go:73] Found default gateway interface ens4 fe80::5054:ff:febe:bcd4
  F1006 16:09:50.985939   60651 ovnkube.go:130] multiple gateway interfaces detected: br-ex ens4
  ```

  The only resolution is to reconfigure the host networking so that both IP families use the same network interface for the default gateway.
* For clusters configured for dual-stack networking, both the IPv4 and IPv6 routing tables must contain the default gateway.

  If this requirement is not met, pods on the host in the `ovnkube-node` daemon set enter the `CrashLoopBackOff` state.

  If you display a pod with a command such as `oc get pod -n openshift-ovn-kubernetes -l app=ovnkube-node -o yaml`, the `status` field has more than one message about the default gateway, as shown in the following output:

  ```
  I0512 19:07:17.589083  108432 helper_linux.go:74] Found default gateway interface br-ex 192.168.123.1
  F0512 19:07:17.589141  108432 ovnkube.go:133] failed to get default gateway interface
  ```

  The only resolution is to reconfigure the host networking so that both IP families contain the default gateway.
* If you set the `ipv6.disable` parameter to `1` in the `kernelArgument` section of the `MachineConfig` custom resource (CR) for your cluster, OVN-Kubernetes pods enter a `CrashLoopBackOff` state. Additionally, updating your cluster to a later version of OpenShift Container Platform fails because the Network Operator remains on a `Degraded` state. Red Hat does not support disabling IPv6 addresses for your cluster so do not set the `ipv6.disable` parameter to `1`.

### [1.3. Session affinity](#nw-ovn-kubernetes-session-affinity_about-ovn-kubernetes) Copy linkLink copied to clipboard!

You can use *session affinity* if you want to ensure that each time you connect to a <service\_VIP>:<Port>, the traffic is always load balanced to the same back end. For more information, including how to set session affinity based on a client’s IP address, see "Session affinity in Kubernetes".

#### [1.3.1. Stickiness timeout for session affinity](#nw-ovn-kubernetes-session-affinity-stickyness-timeout_about-ovn-kubernetes) Copy linkLink copied to clipboard!

The OVN-Kubernetes network plugin for OpenShift Container Platform calculates the stickiness timeout for a session from a client based on the last packet.

For example, if you run a `curl` command 10 times, the sticky session timer starts from the tenth packet not the first.

As a result, if the client is continuously contacting the service, then the session never times out. The timeout starts when the service has not received a packet for the amount of time set by the `timeoutSeconds` parameter. For more information about `timeoutSeconds`, see "Session stickiness timeout in Kubernetes".

## [Chapter 2. OVN-Kubernetes architecture](#ovn-kubernetes-architecture-assembly) Copy linkLink copied to clipboard!

The following sections describe the OVN-Kubernetes architecture, how OVN components map to cluster resources and databases, and how to install and run `network-tools` for debugging.

### [2.1. Introduction to OVN-Kubernetes architecture](#ovn-kubernetes-architecture-con) Copy linkLink copied to clipboard!

The OVN-Kubernetes architecture comprises specialized databases and daemons that process network state requests. Use this mapping to evaluate data paths and troubleshoot multi-node communication routing.

**Figure 2.1. OVN-Kubernetes architecture**

The key components are:

* **Cloud Management System (CMS)** - A platform specific client for OVN that provides a CMS specific plugin for OVN integration. The plugin translates the cloud management system’s concept of the logical network configuration, stored in the CMS configuration database in a CMS-specific format, into an intermediate representation understood by OVN.
* **OVN Northbound database (`nbdb`) container** - Stores the logical network configuration passed by the CMS plugin.
* **OVN Southbound database (`sbdb`) container** - Stores the physical and logical network configuration state for Open vSwitch (OVS) system on each node, including tables that bind them.
* **OVN north daemon (`ovn-northd`)** - This is the intermediary client between `nbdb` container and `sbdb` container. It translates the logical network configuration in terms of conventional network concepts, taken from the `nbdb` container, into logical data path flows in the `sbdb` container. The container name for `ovn-northd` daemon is `northd` and it runs in the `ovnkube-node` pods.
* **ovn-controller** - This is the OVN agent that interacts with OVS and hypervisors, for any information or update that is required for `sbdb` container. The `ovn-controller` reads logical flows from the `sbdb` container, translates them into `OpenFlow` flows and sends them to the node’s OVS daemon. The container name is `ovn-controller` and it runs in the `ovnkube-node` pods.

The OVN northd, northbound database, and southbound database run on each node in the cluster and mostly contain and process information that is local to that node.

The OVN northbound database has the logical network configuration passed down to it by the cloud management system (CMS). The OVN northbound database contains the current intended state of the network, presented as a collection of logical ports, logical switches, logical routers, and more. The `ovn-northd` (`northd` container) connects to the OVN northbound database and the OVN southbound database. It translates the logical network configuration in terms of conventional network concepts, taken from the OVN northbound database, into logical data path flows in the OVN southbound database.

The OVN southbound database has physical and logical representations of the network and binding tables that link them together. It contains the chassis information of the node and other constructs such as remote transit switch ports that are required to connect to the other nodes in the cluster. The OVN southbound database also contains all the logic flows. The logic flows are shared with the `ovn-controller` process that runs on each node and the `ovn-controller` turns those into `OpenFlow` rules to program `Open vSwitch`(OVS).

The Kubernetes control plane nodes contain two `ovnkube-control-plane` pods on separate nodes, which perform the central IP address management (IPAM) allocation for each node in the cluster. At any given time, a single `ovnkube-control-plane` pod is the leader.

### [2.2. Listing all resources in the OVN-Kubernetes project](#nw-ovn-kubernetes-list-resources_ovn-kubernetes-architecture) Copy linkLink copied to clipboard!

List the resources and containers running within the OVN-Kubernetes project to identify network workload states and verify component placement across the infrastructure.

**Procedure**

1. List all pods and endpoints by entering the following command:

   ```
   $ oc get all,ep,cm -n openshift-ovn-kubernetes
   ```

   **Example output**

   ```
   Warning: apps.openshift.io/v1 DeploymentConfig is deprecated in v4.14+, unavailable in v4.10000+
   NAME                                         READY   STATUS    RESTARTS       AGE
   pod/ovnkube-control-plane-65c6f55656-6d55h   2/2     Running   0              114m
   pod/ovnkube-control-plane-65c6f55656-fd7vw   2/2     Running   2 (104m ago)   114m
   pod/ovnkube-node-bcvts                       8/8     Running   0              113m
   pod/ovnkube-node-drgvv                       8/8     Running   0              113m
   pod/ovnkube-node-f2pxt                       8/8     Running   0              113m
   pod/ovnkube-node-frqsb                       8/8     Running   0              105m
   pod/ovnkube-node-lbxkk                       8/8     Running   0              105m
   pod/ovnkube-node-tt7bx                       8/8     Running   1 (102m ago)   105m

   NAME                                   TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)             AGE
   service/ovn-kubernetes-control-plane   ClusterIP   None         <none>        9108/TCP            114m
   service/ovn-kubernetes-node            ClusterIP   None         <none>        9103/TCP,9105/TCP   114m

   NAME                          DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR                 AGE
   daemonset.apps/ovnkube-node   6         6         6       6            6           beta.kubernetes.io/os=linux   114m

   NAME                                    READY   UP-TO-DATE   AVAILABLE   AGE
   deployment.apps/ovnkube-control-plane   3/3     3            3           114m

   NAME                                               DESIRED   CURRENT   READY   AGE
   replicaset.apps/ovnkube-control-plane-65c6f55656   3         3         3       114m

   NAME                                     ENDPOINTS                                               AGE
   endpoints/ovn-kubernetes-control-plane   10.0.0.3:9108,10.0.0.4:9108,10.0.0.5:9108               114m
   endpoints/ovn-kubernetes-node            10.0.0.3:9105,10.0.0.4:9105,10.0.0.5:9105 + 9 more...   114m

   NAME                                 DATA   AGE
   configmap/control-plane-status       1      113m
   configmap/kube-root-ca.crt           1      114m
   configmap/openshift-service-ca.crt   1      114m
   configmap/ovn-ca                     1      114m
   configmap/ovnkube-config             1      114m
   configmap/signer-ca                  1      114m
   ```

   There is one `ovnkube-node` pod for each node in the cluster. The `ovnkube-config` config map has the OpenShift Container Platform OVN-Kubernetes configurations.
2. Display the container layout within the node pod by entering the following command:

   ```
   $ oc get pods ovnkube-node-bcvts -o jsonpath='{.spec.containers[*].name}' -n openshift-ovn-kubernetes
   ```

   **Example output**

   ```
   ovn-controller ovn-acl-logging kube-rbac-proxy-node kube-rbac-proxy-ovn-metrics northd nbdb sbdb ovnkube-controller
   ```

   The `ovnkube-node` pod hosts the following networking containers:

   * The northbound database, `nbdb`.
   * The southbound database, `sbdb`.
   * The north daemon, `northd`.
   * The `ovn-controller`.
   * The `ovnkube-controller`.

     The `ovnkube-controller` container watches for API objects such as pods, egress IPs, namespaces, services, endpoints, egress firewall, and network policies. The controller is also responsible for allocating pod IP addresses from the available subnet pool for that node.
3. List all the containers in the `ovnkube-control-plane` pods by entering the following command:

   ```
   $ oc get pods ovnkube-control-plane-65c6f55656-6d55h -o jsonpath='{.spec.containers[*].name}' -n openshift-ovn-kubernetes
   ```

   **Example output**

   ```
   kube-rbac-proxy ovnkube-cluster-manager
   ```

   The `ovnkube-control-plane` pod has a container that runs on each OpenShift Container Platform node, the `ovnkube-cluster-manager`. The `ovnkube-cluster-manager` container allocates pod subnet, transit-switch subnet IP addresses, and join-switch subnet IP addresses to each node in the cluster. The `kube-rbac-proxy` container monitors metrics for the `ovnkube-cluster-manager` container.

### [2.3. Listing the OVN-Kubernetes northbound database contents](#nw-ovn-kubernetes-list-database-contents_ovn-kubernetes-architecture) Copy linkLink copied to clipboard!

To understand OVN-Kubernetes (OVN-K) logical networking entities, you must examine the northbound database running as a container inside the ovnkube-node pod. Each node is controlled by the ovnkube-controller container running within that local pod structure.

**Prerequisites**

* Access to the cluster as a user with the `cluster-admin` role.
* The OpenShift CLI (`oc`) is installed.

**Procedure**

1. List the pods in the network namespace by entering the following command:

   ```
   $ oc get po -n openshift-ovn-kubernetes
   ```

   **Example output**

   ```
   NAME                                     READY   STATUS    RESTARTS      AGE
   ovnkube-control-plane-8444dff7f9-4lh9k   2/2     Running   0             27m
   ovnkube-control-plane-8444dff7f9-5rjh9   2/2     Running   0             27m
   ovnkube-node-55xs2                       8/8     Running   0             26m
   ovnkube-node-7r84r                       8/8     Running   0             16m
   ovnkube-node-bqq8p                       8/8     Running   0             17m
   ovnkube-node-mkj4f                       8/8     Running   0             26m
   ovnkube-node-mlr8k                       8/8     Running   0             26m
   ovnkube-node-wqn2m                       8/8     Running   0             16m
   ```
2. Optional: To list the pods with node information, enter the following command:

   ```
   $ oc get pods -n openshift-ovn-kubernetes -owide
   ```

   **Example output**

   ```
   NAME                                     READY   STATUS    RESTARTS      AGE   IP           NODE                                       NOMINATED NODE   READINESS GATES
   ovnkube-control-plane-8444dff7f9-4lh9k   2/2     Running   0             27m   10.0.0.3     ci-ln-t487nnb-72292-mdcnq-master-1         <none>           <none>
   ovnkube-control-plane-8444dff7f9-5rjh9   2/2     Running   0             27m   10.0.0.4     ci-ln-t487nnb-72292-mdcnq-master-2         <none>           <none>
   ovnkube-node-55xs2                       8/8     Running   0             26m   10.0.0.4     ci-ln-t487nnb-72292-mdcnq-master-2         <none>           <none>
   ovnkube-node-7r84r                       8/8     Running   0             17m   10.0.128.3   ci-ln-t487nnb-72292-mdcnq-worker-b-wbz7z   <none>           <none>
   ovnkube-node-bqq8p                       8/8     Running   0             17m   10.0.128.2   ci-ln-t487nnb-72292-mdcnq-worker-a-lh7ms   <none>           <none>
   ovnkube-node-mkj4f                       8/8     Running   0             27m   10.0.0.5     ci-ln-t487nnb-72292-mdcnq-master-0         <none>           <none>
   ovnkube-node-mlr8k                       8/8     Running   0             27m   10.0.0.3     ci-ln-t487nnb-72292-mdcnq-master-1         <none>           <none>
   ovnkube-node-wqn2m                       8/8     Running   0             17m   10.0.128.4   ci-ln-t487nnb-72292-mdcnq-worker-c-przlm   <none>           <none>
   ```
3. Open a remote shell into the `nbdb` or `sbdb` containers on the relevant node.
4. Show all the objects in the northbound database by entering the following command:

   ```
   $ ovn-nbctl show
   ```

   The output is too long to list here. The list includes the NAT rules, logical switches, load balancers and so on.

   You can narrow down and focus on specific components by using some of the following optional commands:

   1. View the list of active logical routers by entering the following command:

      ```
      $ oc exec -n openshift-ovn-kubernetes -it ovnkube-node-55xs2 \
      -c northd -- ovn-nbctl lr-list
      ```

      **Example output**

      ```
      45339f4f-7d0b-41d0-b5f9-9fca9ce40ce6 (GR_ci-ln-t487nnb-72292-mdcnq-master-2)
      96a0a0f0-e7ed-4fec-8393-3195563de1b8 (ovn_cluster_router)
      ```

      Note

      From this output you can see there is router on each node plus an `ovn_cluster_router`.
   2. View the list of logical switches by entering the following command:

      ```
      $ oc exec -n openshift-ovn-kubernetes -it ovnkube-node-55xs2 \
      -c nbdb -- ovn-nbctl ls-list
      ```

      **Example output**

      ```
      bdd7dc3d-d848-4a74-b293-cc15128ea614 (ci-ln-t487nnb-72292-mdcnq-master-2)
      b349292d-ee03-4914-935f-1940b6cb91e5 (ext_ci-ln-t487nnb-72292-mdcnq-master-2)
      0aac0754-ea32-4e33-b086-35eeabf0a140 (join)
      992509d7-2c3f-4432-88db-c179e43592e5 (transit_switch)
      ```

      Note

      From this output you can see there is an ext switch for each node plus switches with the node name itself and a join switch.
   3. View the list of load balancers by entering the following command:

      ```
      $ oc exec -n openshift-ovn-kubernetes -it ovnkube-node-55xs2 \
      -c nbdb -- ovn-nbctl lb-list
      ```

      **Example output**

      ```
      UUID                                    LB                  PROTO      VIP                     IPs
      7c84c673-ed2a-4436-9a1f-9bc5dd181eea    Service_default/    tcp        172.30.0.1:443          10.0.0.3:6443,169.254.169.2:6443,10.0.0.5:6443
      4d663fd9-ddc8-4271-b333-4c0e279e20bb    Service_default/    tcp        172.30.0.1:443          10.0.0.3:6443,10.0.0.4:6443,10.0.0.5:6443
      292eb07f-b82f-4962-868a-4f541d250bca    Service_openshif    tcp        172.30.105.247:443      10.129.0.12:8443
      034b5a7f-bb6a-45e9-8e6d-573a82dc5ee3    Service_openshif    tcp        172.30.192.38:443       10.0.0.3:10259,10.0.0.4:10259,10.0.0.5:10259
      a68bb53e-be84-48df-bd38-bdd82fcd4026    Service_openshif    tcp        172.30.161.125:8443     10.129.0.32:8443
      6cc21b3d-2c54-4c94-8ff5-d8e017269c2e    Service_openshif    tcp        172.30.3.144:443        10.129.0.22:8443
      37996ffd-7268-4862-a27f-61cd62e09c32    Service_openshif    tcp        172.30.181.107:443      10.129.0.18:8443
      81d4da3c-f811-411f-ae0c-bc6713d0861d    Service_openshif    tcp        172.30.228.23:443       10.129.0.29:8443
      ac5a4f3b-b6ba-4ceb-82d0-d84f2c41306e    Service_openshif    tcp        172.30.14.240:9443      10.129.0.36:9443
      c88979fb-1ef5-414b-90ac-43b579351ac9    Service_openshif    tcp        172.30.231.192:9001     10.128.0.5:9001,10.128.2.5:9001,10.129.0.5:9001,10.129.2.4:9001,10.130.0.3:9001,10.131.0.3:9001
      fcb0a3fb-4a77-4230-a84a-be45dce757e8    Service_openshif    tcp        172.30.189.92:443       10.130.0.17:8440
      67ef3e7b-ceb9-4bf0-8d96-b43bde4c9151    Service_openshif    tcp        172.30.67.218:443       10.129.0.9:8443
      d0032fba-7d5e-424a-af25-4ab9b5d46e81    Service_openshif    tcp        172.30.102.137:2379     10.0.0.3:2379,10.0.0.4:2379,10.0.0.5:2379
                                                                  tcp        172.30.102.137:9979     10.0.0.3:9979,10.0.0.4:9979,10.0.0.5:9979
      7361c537-3eec-4e6c-bc0c-0522d182abd4    Service_openshif    tcp        172.30.198.215:9001     10.0.0.3:9001,10.0.0.4:9001,10.0.0.5:9001,10.0.128.2:9001,10.0.128.3:9001,10.0.128.4:9001
      0296c437-1259-410b-a6fd-81c310ad0af5    Service_openshif    tcp        172.30.198.215:9001     10.0.0.3:9001,169.254.169.2:9001,10.0.0.5:9001,10.0.128.2:9001,10.0.128.3:9001,10.0.128.4:9001
      5d5679f5-45b8-479d-9f7c-08b123c688b8    Service_openshif    tcp        172.30.38.253:17698     10.128.0.52:17698,10.129.0.84:17698,10.130.0.60:17698
      2adcbab4-d1c9-447d-9573-b5dc9f2efbfa    Service_openshif    tcp        172.30.148.52:443       10.0.0.4:9202,10.0.0.5:9202
                                                                  tcp        172.30.148.52:444       10.0.0.4:9203,10.0.0.5:9203
                                                                  tcp        172.30.148.52:445       10.0.0.4:9204,10.0.0.5:9204
                                                                  tcp        172.30.148.52:446       10.0.0.4:9205,10.0.0.5:9205
      2a33a6d7-af1b-4892-87cc-326a380b809b    Service_openshif    tcp        172.30.67.219:9091      10.129.2.16:9091,10.131.0.16:9091
                                                                  tcp        172.30.67.219:9092      10.129.2.16:9092,10.131.0.16:9092
                                                                  tcp        172.30.67.219:9093      10.129.2.16:9093,10.131.0.16:9093
                                                                  tcp        172.30.67.219:9094      10.129.2.16:9094,10.131.0.16:9094
      f56f59d7-231a-4974-99b3-792e2741ec8d    Service_openshif    tcp        172.30.89.212:443       10.128.0.41:8443,10.129.0.68:8443,10.130.0.44:8443
      08c2c6d7-d217-4b96-b5d8-c80c4e258116    Service_openshif    tcp        172.30.102.137:2379     10.0.0.3:2379,169.254.169.2:2379,10.0.0.5:2379
                                                                  tcp        172.30.102.137:9979     10.0.0.3:9979,169.254.169.2:9979,10.0.0.5:9979
      60a69c56-fc6a-4de6-bd88-3f2af5ba5665    Service_openshif    tcp        172.30.10.193:443       10.129.0.25:8443
      ab1ef694-0826-4671-a22c-565fc2d282ec    Service_openshif    tcp        172.30.196.123:443      10.128.0.33:8443,10.129.0.64:8443,10.130.0.37:8443
      b1fb34d3-0944-4770-9ee3-2683e7a630e2    Service_openshif    tcp        172.30.158.93:8443      10.129.0.13:8443
      95811c11-56e2-4877-be1e-c78ccb3a82a9    Service_openshif    tcp        172.30.46.85:9001       10.130.0.16:9001
      4baba1d1-b873-4535-884c-3f6fc07a50fd    Service_openshif    tcp        172.30.28.87:443        10.129.0.26:8443
      6c2e1c90-f0ca-484e-8a8e-40e71442110a    Service_openshif    udp        172.30.0.10:53          10.128.0.13:5353,10.128.2.6:5353,10.129.0.39:5353,10.129.2.6:5353,10.130.0.11:5353,10.131.0.9:5353
      ```

      Note

      From this truncated output you can see there are many OVN-Kubernetes load balancers. Load balancers in OVN-Kubernetes are representations of services.
5. Display the options available with the `ovn-nbctl` command by entering the following command:

   ```
   $ oc exec -n openshift-ovn-kubernetes -it ovnkube-node-55xs2 \
   -c nbdb ovn-nbctl --help
   ```

### [2.4. Command-line arguments for ovn-nbctl to examine northbound database contents](#nw-ovn-kubernetes-examine-nb-database-contents-ref_ovn-kubernetes-architecture) Copy linkLink copied to clipboard!

The following table describes the command-line arguments that can be used with `ovn-nbctl` to examine the contents of the northbound database.

Note

Open a remote shell in the pod you want to view the contents of and then run the `ovn-nbctl` commands.

Expand

Table 2.1. Command-line arguments to examine northbound database contents

| Argument | Description |
| --- | --- |
| `ovn-nbctl show` | An overview of the northbound database contents as seen from a specific node. |
| `ovn-nbctl show <switch_or_router>` | Show the details associated with the specified switch or router. |
| `ovn-nbctl lr-list` | Show the logical routers. |
| `ovn-nbctl lrp-list <router>` | Using the router information from `ovn-nbctl lr-list` to show the router ports. |
| `ovn-nbctl lr-nat-list <router>` | Show network address translation details for the specified router. |
| `ovn-nbctl ls-list` | Show the logical switches |
| `ovn-nbctl lsp-list <switch>` | Using the switch information from `ovn-nbctl ls-list` to show the switch port. |
| `ovn-nbctl lsp-get-type <port>` | Get the type for the logical port. |
| `ovn-nbctl lb-list` | Show the load balancers. |

Show more

### [2.5. Listing the OVN-Kubernetes southbound database contents](#nw-ovn-kubernetes-list-southbound-database-contents_ovn-kubernetes-architecture) Copy linkLink copied to clipboard!

To understand OVN-Kubernetes (OVN-K) logical networking entities, examine the southbound database running as a container inside the `ovnkube-node` pod. Each node is controlled by the `ovnkube-controller` container running in that pod on the node.

**Prerequisites**

* Access to the cluster as a user with the `cluster-admin` role.
* The OpenShift CLI (`oc`) is installed.

**Procedure**

1. List the pods in the network namespace by entering the following command:

   ```
   $ oc get po -n openshift-ovn-kubernetes
   ```

   **Example output**

   ```
   NAME                                     READY   STATUS    RESTARTS      AGE
   ovnkube-control-plane-8444dff7f9-4lh9k   2/2     Running   0             27m
   ovnkube-control-plane-8444dff7f9-5rjh9   2/2     Running   0             27m
   ovnkube-node-55xs2                       8/8     Running   0             26m
   ovnkube-node-7r84r                       8/8     Running   0             16m
   ovnkube-node-bqq8p                       8/8     Running   0             17m
   ovnkube-node-mkj4f                       8/8     Running   0             26m
   ovnkube-node-mlr8k                       8/8     Running   0             26m
   ovnkube-node-wqn2m                       8/8     Running   0             16m
   ```
2. Optional: To list the pods with node information, enter the following command:

   ```
   $ oc get pods -n openshift-ovn-kubernetes -owide
   ```

   **Example output**

   ```
   NAME                                     READY   STATUS    RESTARTS      AGE   IP           NODE                                       NOMINATED NODE   READINESS GATES
   ovnkube-control-plane-8444dff7f9-4lh9k   2/2     Running   0             27m   10.0.0.3     ci-ln-t487nnb-72292-mdcnq-master-1         <none>           <none>
   ovnkube-control-plane-8444dff7f9-5rjh9   2/2     Running   0             27m   10.0.0.4     ci-ln-t487nnb-72292-mdcnq-master-2         <none>           <none>
   ovnkube-node-55xs2                       8/8     Running   0             26m   10.0.0.4     ci-ln-t487nnb-72292-mdcnq-master-2         <none>           <none>
   ovnkube-node-7r84r                       8/8     Running   0             17m   10.0.128.3   ci-ln-t487nnb-72292-mdcnq-worker-b-wbz7z   <none>           <none>
   ovnkube-node-bqq8p                       8/8     Running   0             17m   10.0.128.2   ci-ln-t487nnb-72292-mdcnq-worker-a-lh7ms   <none>           <none>
   ovnkube-node-mkj4f                       8/8     Running   0             27m   10.0.0.5     ci-ln-t487nnb-72292-mdcnq-master-0         <none>           <none>
   ovnkube-node-mlr8k                       8/8     Running   0             27m   10.0.0.3     ci-ln-t487nnb-72292-mdcnq-master-1         <none>           <none>
   ovnkube-node-wqn2m                       8/8     Running   0             17m   10.0.128.4   ci-ln-t487nnb-72292-mdcnq-worker-c-przlm   <none>           <none>
   ```
3. Open a remote shell into the `nbdb` or `sbdb` containers on the relevant node to examine the southbound database.
4. Show all the objects in the southbound database by entering the following command:

   ```
   $ ovn-sbctl show
   ```

   **Example output**

   ```
   Chassis "5db31703-35e9-413b-8cdf-69e7eecb41f7"
       hostname: ci-ln-9gp362t-72292-v2p94-worker-a-8bmwz
       Encap geneve
           ip: "10.0.128.4"
           options: {csum="true"}
       Port_Binding tstor-ci-ln-9gp362t-72292-v2p94-worker-a-8bmwz
   Chassis "070debed-99b7-4bce-b17d-17e720b7f8bc"
       hostname: ci-ln-9gp362t-72292-v2p94-worker-b-svmp6
       Encap geneve
           ip: "10.0.128.2"
           options: {csum="true"}
       Port_Binding k8s-ci-ln-9gp362t-72292-v2p94-worker-b-svmp6
       Port_Binding rtoe-GR_ci-ln-9gp362t-72292-v2p94-worker-b-svmp6
       Port_Binding openshift-monitoring_alertmanager-main-1
       Port_Binding rtoj-GR_ci-ln-9gp362t-72292-v2p94-worker-b-svmp6
       Port_Binding etor-GR_ci-ln-9gp362t-72292-v2p94-worker-b-svmp6
       Port_Binding cr-rtos-ci-ln-9gp362t-72292-v2p94-worker-b-svmp6
       Port_Binding openshift-e2e-loki_loki-promtail-qcrcz
       Port_Binding jtor-GR_ci-ln-9gp362t-72292-v2p94-worker-b-svmp6
       Port_Binding openshift-multus_network-metrics-daemon-mkd4t
       Port_Binding openshift-ingress-canary_ingress-canary-xtvj4
       Port_Binding openshift-ingress_router-default-6c76cbc498-pvlqk
       Port_Binding openshift-dns_dns-default-zz582
       Port_Binding openshift-monitoring_thanos-querier-57585899f5-lbf4f
       Port_Binding openshift-network-diagnostics_network-check-target-tn228
       Port_Binding openshift-monitoring_prometheus-k8s-0
       Port_Binding openshift-image-registry_image-registry-68899bd877-xqxjj
   Chassis "179ba069-0af1-401c-b044-e5ba90f60fea"
       hostname: ci-ln-9gp362t-72292-v2p94-master-0
       Encap geneve
           ip: "10.0.0.5"
           options: {csum="true"}
       Port_Binding tstor-ci-ln-9gp362t-72292-v2p94-master-0
   Chassis "68c954f2-5a76-47be-9e84-1cb13bd9dab9"
       hostname: ci-ln-9gp362t-72292-v2p94-worker-c-mjf9w
       Encap geneve
           ip: "10.0.128.3"
           options: {csum="true"}
       Port_Binding tstor-ci-ln-9gp362t-72292-v2p94-worker-c-mjf9w
   Chassis "2de65d9e-9abf-4b6e-a51d-a1e038b4d8af"
       hostname: ci-ln-9gp362t-72292-v2p94-master-2
       Encap geneve
           ip: "10.0.0.4"
           options: {csum="true"}
       Port_Binding tstor-ci-ln-9gp362t-72292-v2p94-master-2
   Chassis "1d371cb8-5e21-44fd-9025-c4b162cc4247"
       hostname: ci-ln-9gp362t-72292-v2p94-master-1
       Encap geneve
           ip: "10.0.0.3"
           options: {csum="true"}
       Port_Binding tstor-ci-ln-9gp362t-72292-v2p94-master-1
   ```

   * This detailed output shows the chassis and the ports that are attached to the chassis which in this case are all of the router ports and anything that uses host networking.
   * Any pods communicate out to the wider network by using source network address translation (SNAT). Their IP address is translated into the IP address of the node that the pod is running on and then sent out into the network.
   * In addition to the chassis information the southbound database has all the logic flows and those logic flows are then sent to the `ovn-controller` running on each of the nodes. The `ovn-controller` translates the logic flows into open flow rules and ultimately programs `OpenvSwitch` so that your pods can then follow open flow rules and make it out of the network.
5. Display the options available with the `ovn-sbctl` command by entering the following command:

   ```
   $ oc exec -n openshift-ovn-kubernetes -it ovnkube-node-55xs2 \
   -c sbdb ovn-sbctl --help
   ```

### [2.6. Command-line arguments for ovn-sbctl to examine southbound database contents](#nw-ovn-kubernetes-examine-sb-database-contents-ref_ovn-kubernetes-architecture) Copy linkLink copied to clipboard!

The following table describes the command-line arguments that can be used with `ovn-sbctl` to examine the contents of the southbound database.

Note

Open a remote shell in the pod you wish to view the contents of and then run the `ovn-sbctl` commands.

Expand

Table 2.2. Command-line arguments to examine southbound database contents

| Argument | Description |
| --- | --- |
| `ovn-sbctl show` | An overview of the southbound database contents as seen from a specific node. |
| `ovn-sbctl list Port_Binding <port>` | List the contents of southbound database for a the specified port . |
| `ovn-sbctl dump-flows` | List the logical flows. |

Show more

### [2.7. OVN-Kubernetes logical architecture](#ovn-kubernetes-logical-architecture-con_ovn-kubernetes-architecture) Copy linkLink copied to clipboard!

OVN-Kubernetes is a network virtualization solution that creates logical switches and routers across cluster nodes. These virtual infrastructure components interconnect to construct distinct network topologies.

**Figure 2.2. OVN-Kubernetes router and switch components**

The key components involved in packet processing are:

Gateway routers
:   Gateway routers sometimes called L3 gateway routers, are typically used between the distributed routers and the physical network. Gateway routers including their logical patch ports are bound to a physical location (not distributed), or chassis. The patch ports on this router are known as l3gateway ports in the ovn-southbound database (`ovn-sbdb`).

Distributed logical routers
:   Distributed logical routers and the logical switches behind them, to which virtual machines and containers attach, effectively reside on each hypervisor.

Join local switch
:   Join local switches are used to connect the distributed router and gateway routers. It reduces the number of IP addresses needed on the distributed router.

Logical switches with patch ports
:   Logical switches with patch ports virtualize the network stack. These components connect remote logical ports through network encapsulation tunnels.

Logical switches with localnet ports
:   Logical switches with localnet ports connect the OVN layout to the physical network. These elements connect remote logical ports by bridging packets to directly attached physical Layer 2 segments.

Patch ports
:   Patch ports provide connectivity between logical switches and logical routers, or between peer logical routers. A single connection uses a pair of patch ports at each connectivity intersection, one on each side.

`l3gateway` ports
:   Port binding entries in the `ovn-sbdb` for logical patch ports used in gateway routers. They are called `l3gateway` ports rather than patch ports because these ports are bound to a chassis similar to the gateway router itself.

localnet ports
:   localnet ports are present on the bridged logical switches that allows a connection to a locally accessible network from each `ovn-controller` instance. This helps model the direct connectivity to the physical network from the logical switches. A logical switch can only have a single localnet port attached to it.

Note

Executing `ovnkube-trace` with the log level configuration set to `2` or `5` exposes these internal OVN-Kubernetes logical routing components for analysis.

#### [2.7.1. Installing network-tools on local host](#nw-ovn-kubernetes-installing-network-tools_ovn-kubernetes-architecture) Copy linkLink copied to clipboard!

Install `network-tools` on your local host for debugging OpenShift Container Platform cluster network issues.

**Procedure**

1. Clone the `network-tools` repository onto your workstation with the following command:

   ```
   $ git clone git@github.com:openshift/network-tools.git
   ```
2. Change into the directory for the repository you just cloned:

   ```
   $ cd network-tools
   ```
3. Optional: List all available commands:

   ```
   $ ./debug-scripts/network-tools -h
   ```

#### [2.7.2. Running network-tools](#nw-ovn-kubernetes-running-network-tools_ovn-kubernetes-architecture) Copy linkLink copied to clipboard!

Run `network-tools` to retrieve configuration status from logical switches and routers when diagnosing internal routing loops and cluster network issues.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster as a user with `cluster-admin` privileges.
* You have installed `network-tools` on local host.

**Procedure**

1. Display the logical router map by entering the following command:

   ```
   $ ./debug-scripts/network-tools ovn-db-run-command ovn-nbctl lr-list
   ```

   **Example output**

   ```
   944a7b53-7948-4ad2-a494-82b55eeccf87 (GR_ci-ln-54932yb-72292-kd676-worker-c-rzj99)
   84bd4a4c-4b0b-4a47-b0cf-a2c32709fc53 (ovn_cluster_router)
   ```
2. Locate active port bindings with local network attributes by entering the following command:

   ```
   $ ./debug-scripts/network-tools ovn-db-run-command "ovn-sbctl find Port_Binding type=localnet"
   ```

   **Example output**

   ```
   _uuid               : d05298f5-805b-4838-9224-1211afc2f199
   additional_chassis  : []
   additional_encap    : []
   chassis             : []
   datapath            : f3c2c959-743b-4037-854d-26627902597c
   encap               : []
   external_ids        : {}
   gateway_chassis     : []
   ha_chassis_group    : []
   logical_port        : br-ex_ci-ln-54932yb-72292-kd676-worker-c-rzj99
   mac                 : [unknown]
   mirror_rules        : []
   nat_addresses       : []
   options             : {network_name=physnet}
   parent_port         : []
   port_security       : []
   requested_additional_chassis: []
   requested_chassis   : []
   tag                 : []
   tunnel_key          : 2
   type                : localnet
   up                  : false
   virtual_parent      : []

   [...]
   ```
3. List the `l3gateway` ports by entering the following command:

   ```
   $ ./debug-scripts/network-tools ovn-db-run-command "ovn-sbctl find Port_Binding type=l3gateway"
   ```

   **Example output**

   ```
   _uuid               : 5207a1f3-1cf3-42f1-83e9-387bbb06b03c
   additional_chassis  : []
   additional_encap    : []
   chassis             : ca6eb600-3a10-4372-a83e-e0d957c4cd92
   datapath            : f3c2c959-743b-4037-854d-26627902597c
   encap               : []
   external_ids        : {}
   gateway_chassis     : []
   ha_chassis_group    : []
   logical_port        : etor-GR_ci-ln-54932yb-72292-kd676-worker-c-rzj99
   mac                 : ["42:01:0a:00:80:04"]
   mirror_rules        : []
   nat_addresses       : ["42:01:0a:00:80:04 10.0.128.4"]
   options             : {l3gateway-chassis="84737c36-b383-4c83-92c5-2bd5b3c7e772", peer=rtoe-GR_ci-ln-54932yb-72292-kd676-worker-c-rzj99}
   parent_port         : []
   port_security       : []
   requested_additional_chassis: []
   requested_chassis   : []
   tag                 : []
   tunnel_key          : 1
   type                : l3gateway
   up                  : true
   virtual_parent      : []

   _uuid               : 6088d647-84f2-43f2-b53f-c9d379042679
   additional_chassis  : []
   additional_encap    : []
   chassis             : ca6eb600-3a10-4372-a83e-e0d957c4cd92
   datapath            : dc9cea00-d94a-41b8-bdb0-89d42d13aa2e
   encap               : []
   external_ids        : {}
   gateway_chassis     : []
   ha_chassis_group    : []
   logical_port        : jtor-GR_ci-ln-54932yb-72292-kd676-worker-c-rzj99
   mac                 : [router]
   mirror_rules        : []
   nat_addresses       : []
   options             : {l3gateway-chassis="84737c36-b383-4c83-92c5-2bd5b3c7e772", peer=rtoj-GR_ci-ln-54932yb-72292-kd676-worker-c-rzj99}
   parent_port         : []
   port_security       : []
   requested_additional_chassis: []
   requested_chassis   : []
   tag                 : []
   tunnel_key          : 2
   type                : l3gateway
   up                  : true
   virtual_parent      : []

   [...]
   ```
4. List the patch ports by entering the following command:

   ```
   $ ./debug-scripts/network-tools ovn-db-run-command "ovn-sbctl find Port_Binding type=patch"
   ```

   **Example output**

   ```
   _uuid               : 785fb8b6-ee5a-4792-a415-5b1cb855dac2
   additional_chassis  : []
   additional_encap    : []
   chassis             : []
   datapath            : f1ddd1cc-dc0d-43b4-90ca-12651305acec
   encap               : []
   external_ids        : {}
   gateway_chassis     : []
   ha_chassis_group    : []
   logical_port        : stor-ci-ln-54932yb-72292-kd676-worker-c-rzj99
   mac                 : [router]
   mirror_rules        : []
   nat_addresses       : ["0a:58:0a:80:02:01 10.128.2.1 is_chassis_resident(\"cr-rtos-ci-ln-54932yb-72292-kd676-worker-c-rzj99\")"]
   options             : {peer=rtos-ci-ln-54932yb-72292-kd676-worker-c-rzj99}
   parent_port         : []
   port_security       : []
   requested_additional_chassis: []
   requested_chassis   : []
   tag                 : []
   tunnel_key          : 1
   type                : patch
   up                  : false
   virtual_parent      : []

   _uuid               : c01ff587-21a5-40b4-8244-4cd0425e5d9a
   additional_chassis  : []
   additional_encap    : []
   chassis             : []
   datapath            : f6795586-bf92-4f84-9222-efe4ac6a7734
   encap               : []
   external_ids        : {}
   gateway_chassis     : []
   ha_chassis_group    : []
   logical_port        : rtoj-ovn_cluster_router
   mac                 : ["0a:58:64:40:00:01 100.64.0.1/16"]
   mirror_rules        : []
   nat_addresses       : []
   options             : {peer=jtor-ovn_cluster_router}
   parent_port         : []
   port_security       : []
   requested_additional_chassis: []
   requested_chassis   : []
   tag                 : []
   tunnel_key          : 1
   type                : patch
   up                  : false
   virtual_parent      : []
   [...]
   ```

## [Chapter 3. Troubleshooting OVN-Kubernetes](#ovn-kubernetes-troubleshooting-sources) Copy linkLink copied to clipboard!

To troubleshoot OVN-Kubernetes in OpenShift Container Platform, you can use built-in health checks, alerting, logs, and connectivity checks. Follow these sections to examine your cluster before opening a support case.

OVN-Kubernetes has many sources of built-in health checks and logs. Follow the instructions in these sections to examine your cluster. If a support case is necessary, collect additional information through a `must-gather` as described in "Gathering data about your cluster for Red Hat Support". Only use the `-- gather_network_logs` option when instructed by support.

### [3.1. Monitoring OVN-Kubernetes health by using readiness probes](#nw-ovn-kubernetes-readiness-probes_ovn-kubernetes-sources-of-troubleshooting-information) Copy linkLink copied to clipboard!

To monitor OVN-Kubernetes component health in OpenShift Container Platform, you can review readiness probe configuration and status for `ovnkube-control-plane` and `ovnkube-node` pods.

**Prerequisites**

* Access to the OpenShift CLI (`oc`).
* You have access to the cluster with `cluster-admin` privileges.
* You have installed `jq`.

**Procedure**

1. Review the details of the `ovnkube-node` readiness probe by running the following command:

   ```
   $ oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-node \
   -o json | jq '.items[0].spec.containers[] | .name,.readinessProbe'
   ```

   The readiness probe for the northbound and southbound database containers in the `ovnkube-node` pod checks for the health of the databases and the `ovnkube-controller` container.

   The `ovnkube-controller` container in the `ovnkube-node` pod has a readiness probe to verify the presence of the OVN-Kubernetes CNI configuration file, the absence of which would indicate that the pod is not running or is not ready to accept requests to configure pods.
2. Show all events including the probe failures, for the namespace by using the following command:

   ```
   $ oc get events -n openshift-ovn-kubernetes
   ```
3. Show the events for just a specific pod:

   ```
   $ oc describe pod ovnkube-node-9lqfk -n openshift-ovn-kubernetes
   ```
4. Show the messages and statuses from the cluster network operator:

   ```
   $ oc get co/network -o json | jq '.status.conditions[]'
   ```
5. Show the `ready` status of each container in `ovnkube-node` pods by running the following script:

   ```
   $ for p in $(oc get pods --selector app=ovnkube-node -n openshift-ovn-kubernetes \
   -o jsonpath='{range.items[*]}{" "}{.metadata.name}'); do echo === $p ===;  \
   oc get pods -n openshift-ovn-kubernetes $p -o json | jq '.status.containerStatuses[] | .name, .ready'; \
   done
   ```

   Note

   The expectation is all container statuses are reporting as `true`. Failure of a readiness probe sets the status to `false`.

### [3.2. Viewing OVN-Kubernetes alerts in the console](#nw-ovn-kubernetes-alerts-console_ovn-kubernetes-sources-of-troubleshooting-information) Copy linkLink copied to clipboard!

To view OVN-Kubernetes alerts in the OpenShift Container Platform web console, you can open **Observe** → **Alerting** to inspect rules, alerts, and silences.

The Alerting UI provides detailed information about alerts and their governing alerting rules and silences.

**Prerequisites**

* You have access to the cluster as a developer or as a user with view permissions for the project that you are viewing metrics for.

**Procedure**

1. In the **Administrator** perspective, select **Observe** → **Alerting**. The three main pages in the Alerting UI in this perspective are the **Alerts**, **Silences**, and **Alerting Rules** pages.
2. View the rules for OVN-Kubernetes alerts by selecting **Observe** → **Alerting** → **Alerting Rules**.

### [3.3. Viewing OVN-Kubernetes alerts in the CLI](#nw-ovn-kubernetes-alerts-cli_ovn-kubernetes-sources-of-troubleshooting-information) Copy linkLink copied to clipboard!

To view OVN-Kubernetes alerts from the command line in OpenShift Container Platform, you can query the `Alertmanager` API for active alerts and related rules.

**Prerequisites**

* Access to the cluster as a user with the `cluster-admin` role.
* The OpenShift CLI (`oc`) installed.
* You have installed `jq`.

**Procedure**

1. View active or firing alerts by running the following commands.

   1. Set the alert manager route environment variable by running the following command:

      ```
      $ ALERT_MANAGER=$(oc get route alertmanager-main -n openshift-monitoring \
      -o jsonpath='{@.spec.host}')
      ```
   2. Issue a `curl` request to the alert manager route API by running the following command, replacing `$ALERT_MANAGER` with the URL of your `Alertmanager` instance:

      ```
      $ curl -s -k -H "Authorization: Bearer $(oc create token prometheus-k8s -n openshift-monitoring)" https://$ALERT_MANAGER/api/v1/alerts | jq '.data[] | "\(.labels.severity) \(.labels.alertname) \(.labels.pod) \(.labels.container) \(.labels.endpoint) \(.labels.instance)"'
      ```
2. View alerting rules by running the following command:

   ```
   $ oc -n openshift-monitoring exec -c prometheus prometheus-k8s-0 -- curl -s 'http://localhost:9090/api/v1/rules' | jq '.data.groups[].rules[] | select(((.name|contains("ovn")) or (.name|contains("OVN")) or (.name|contains("Ovn")) or (.name|contains("North")) or (.name|contains("South"))) and .type=="alerting")'
   ```

### [3.4. Viewing the OVN-Kubernetes logs using the CLI](#nw-ovn-kubernetes-logs-cli_ovn-kubernetes-sources-of-troubleshooting-information) Copy linkLink copied to clipboard!

To view OVN-Kubernetes pod logs in OpenShift Container Platform, you can use the OpenShift CLI (`oc`) to examine logs from containers in the `openshift-ovn-kubernetes` namespace.

**Prerequisites**

* Access to the cluster as a user with the `cluster-admin` role.
* Access to the OpenShift CLI (`oc`).
* You have installed `jq`.

**Procedure**

1. View the log for a specific pod:

   ```
   $ oc logs -f <pod_name> -c <container_name> -n <namespace>
   ```

   where:

   `-f`
   :   Optional: Specifies that the output follows what is being written into the logs.

   `<pod_name>`
   :   Specifies the name of the pod.

   `<container_name>`
   :   Optional: Specifies the name of a container. When a pod has more than one container, you must specify the container name.

   `<namespace>`
   :   Specify the namespace the pod is running in.

   For example:

   ```
   $ oc logs ovnkube-node-5dx44 -n openshift-ovn-kubernetes
   ```

   ```
   $ oc logs -f ovnkube-node-5dx44 -c ovnkube-controller -n openshift-ovn-kubernetes
   ```

   The contents of log files are printed out.
2. Examine the most recent entries in all the containers in the `ovnkube-node` pods:

   ```
   $ for p in $(oc get pods --selector app=ovnkube-node -n openshift-ovn-kubernetes \
   -o jsonpath='{range.items[*]}{" "}{.metadata.name}'); \
   do echo === $p ===; for container in $(oc get pods -n openshift-ovn-kubernetes $p \
   -o json | jq -r '.status.containerStatuses[] | .name');do echo ---$container---; \
   oc logs -c $container $p -n openshift-ovn-kubernetes --tail=5; done; done
   ```
3. View the last 5 lines of every log in every container in an `ovnkube-node` pod using the following command:

   ```
   $ oc logs -l app=ovnkube-node -n openshift-ovn-kubernetes --all-containers --tail 5
   ```

### [3.5. Viewing the OVN-Kubernetes logs using the web console](#nw-ovn-kubernetes-logs-console_ovn-kubernetes-sources-of-troubleshooting-information) Copy linkLink copied to clipboard!

To view OVN-Kubernetes pod logs in the OpenShift Container Platform web console, you can open pod logs for each container in the `openshift-ovn-kubernetes` project.

**Prerequisites**

* Access to the OpenShift CLI (`oc`).

**Procedure**

1. In the OpenShift Container Platform console, navigate to **Workloads** → **Pods** or navigate to the pod through the resource you want to investigate.
2. Select the `openshift-ovn-kubernetes` project from the drop-down menu.
3. Click the name of the pod you want to investigate.
4. Click **Logs**. By default for the `ovnkube-master` the logs associated with the `northd` container are displayed.
5. Use the down-down menu to select logs for each container in turn.

#### [3.5.1. Changing the OVN-Kubernetes log levels](#nw-ovn-kubernetes-change-log-levels_ovn-kubernetes-sources-of-troubleshooting-information) Copy linkLink copied to clipboard!

To debug OVN-Kubernetes in OpenShift Container Platform, you can raise log levels by applying an `env-overrides` `ConfigMap` and restarting affected pods.

The default log level for OVN-Kubernetes is 4. To debug OVN-Kubernetes, set the log level to 5. Follow this procedure to increase the log level of the OVN-Kubernetes to help you debug an issue.

**Prerequisites**

* You have access to the cluster with `cluster-admin` privileges.
* You have access to the OpenShift Container Platform web console.

**Procedure**

1. Run the following command to get detailed information for all pods in the OVN-Kubernetes project:

   ```
   $ oc get po -o wide -n openshift-ovn-kubernetes
   ```

   **Example output**

   ```
   NAME                                     READY   STATUS    RESTARTS       AGE    IP           NODE                                       NOMINATED NODE   READINESS GATES
   ovnkube-control-plane-65497d4548-9ptdr   2/2     Running   2 (128m ago)   147m   10.0.0.3     ci-ln-3njdr9b-72292-5nwkp-master-0         <none>           <none>
   ovnkube-control-plane-65497d4548-j6zfk   2/2     Running   0              147m   10.0.0.5     ci-ln-3njdr9b-72292-5nwkp-master-2         <none>           <none>
   ovnkube-node-5dx44                       8/8     Running   0              146m   10.0.0.3     ci-ln-3njdr9b-72292-5nwkp-master-0         <none>           <none>
   ovnkube-node-dpfn4                       8/8     Running   0              146m   10.0.0.4     ci-ln-3njdr9b-72292-5nwkp-master-1         <none>           <none>
   ovnkube-node-kwc9l                       8/8     Running   0              134m   10.0.128.2   ci-ln-3njdr9b-72292-5nwkp-worker-a-2fjcj   <none>           <none>
   ovnkube-node-mcrhl                       8/8     Running   0              134m   10.0.128.4   ci-ln-3njdr9b-72292-5nwkp-worker-c-v9x5v   <none>           <none>
   ovnkube-node-nsct4                       8/8     Running   0              146m   10.0.0.5     ci-ln-3njdr9b-72292-5nwkp-master-2         <none>           <none>
   ovnkube-node-zrj9f                       8/8     Running   0              134m   10.0.128.3   ci-ln-3njdr9b-72292-5nwkp-worker-b-v78h7   <none>           <none>
   ```
2. Create a `ConfigMap` file similar to the following example and use a filename such as `env-overrides.yaml`:

   **Example `ConfigMap` file**

   ```
   kind: ConfigMap
   apiVersion: v1
   metadata:
     name: env-overrides
     namespace: openshift-ovn-kubernetes
   data:
     ci-ln-3njdr9b-72292-5nwkp-master-0: |
       # This sets the log level for the ovn-kubernetes node process:
       OVN_KUBE_LOG_LEVEL=5
       # You might also/instead want to enable debug logging for ovn-controller:
       OVN_LOG_LEVEL=dbg
     ci-ln-3njdr9b-72292-5nwkp-master-2: |
       # This sets the log level for the ovn-kubernetes node process:
       OVN_KUBE_LOG_LEVEL=5
       # You might also/instead want to enable debug logging for ovn-controller:
       OVN_LOG_LEVEL=dbg
     _master: |
       # This sets the log level for the ovn-kubernetes master process as well as the ovn-dbchecker:
       OVN_KUBE_LOG_LEVEL=5
       # You might also/instead want to enable debug logging for northd, nbdb and sbdb on all masters:
       OVN_LOG_LEVEL=dbg
   ```

   where, `ci-ln-3njdr9b-72292-5nwkp-master-0:`
   :   Specifies the name of the node you want to set the debug log level on.

   `_master:`
   :   Specifies `_master` to set the log levels of `ovnkube-master` components.
3. Apply the `ConfigMap` file by using the following command:

   ```
   $ oc apply -n openshift-ovn-kubernetes -f env-overrides.yaml
   ```

   **Example output**

   ```
   configmap/env-overrides.yaml created
   ```
4. Restart the `ovnkube` pods to apply the new log level by using the following commands:

   ```
   $ oc delete pod -n openshift-ovn-kubernetes \
   --field-selector spec.nodeName=ci-ln-3njdr9b-72292-5nwkp-master-0 -l app=ovnkube-node
   ```

   ```
   $ oc delete pod -n openshift-ovn-kubernetes \
   --field-selector spec.nodeName=ci-ln-3njdr9b-72292-5nwkp-master-2 -l app=ovnkube-node
   ```

   ```
   $ oc delete pod -n openshift-ovn-kubernetes -l app=ovnkube-node
   ```
5. To verify that the `ConfigMap`file has been applied to all nodes for a specific pod, run the following command:

   ```
   $ oc logs -n openshift-ovn-kubernetes --all-containers --prefix ovnkube-node-<xxxx> | grep -E -m 10 '(Logging config:|vconsole|DBG)'
   ```

   where: `<XXXX>`:: Specifies the random sequence of letters for a pod from the previous step.

   + .Example output

   ```
   [pod/ovnkube-node-2cpjc/sbdb] + exec /usr/share/ovn/scripts/ovn-ctl --no-monitor '--ovn-sb-log=-vconsole:info -vfile:off -vPATTERN:console:%D{%Y-%m-%dT%H:%M:%S.###Z}|%05N|%c%T|%p|%m' run_sb_ovsdb
   [pod/ovnkube-node-2cpjc/ovnkube-controller] I1012 14:39:59.984506   35767 config.go:2247] Logging config: {File: CNIFile:/var/log/ovn-kubernetes/ovn-k8s-cni-overlay.log LibovsdbFile:/var/log/ovnkube/libovsdb.log Level:5 LogFileMaxSize:100 LogFileMaxBackups:5 LogFileMaxAge:0 ACLLoggingRateLimit:20}
   [pod/ovnkube-node-2cpjc/northd] + exec ovn-northd --no-chdir -vconsole:info -vfile:off '-vPATTERN:console:%D{%Y-%m-%dT%H:%M:%S.###Z}|%05N|%c%T|%p|%m' --pidfile /var/run/ovn/ovn-northd.pid --n-threads=1
   [pod/ovnkube-node-2cpjc/nbdb] + exec /usr/share/ovn/scripts/ovn-ctl --no-monitor '--ovn-nb-log=-vconsole:info -vfile:off -vPATTERN:console:%D{%Y-%m-%dT%H:%M:%S.###Z}|%05N|%c%T|%p|%m' run_nb_ovsdb
   [pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.552Z|00002|hmap|DBG|lib/shash.c:114: 1 bucket with 6+ nodes, including 1 bucket with 6 nodes (32 nodes total across 32 buckets)
   [pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.553Z|00003|hmap|DBG|lib/shash.c:114: 1 bucket with 6+ nodes, including 1 bucket with 6 nodes (64 nodes total across 64 buckets)
   [pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.553Z|00004|hmap|DBG|lib/shash.c:114: 1 bucket with 6+ nodes, including 1 bucket with 7 nodes (32 nodes total across 32 buckets)
   [pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.553Z|00005|reconnect|DBG|unix:/var/run/openvswitch/db.sock: entering BACKOFF
   [pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.553Z|00007|reconnect|DBG|unix:/var/run/openvswitch/db.sock: entering CONNECTING
   [pod/ovnkube-node-2cpjc/ovn-controller] 2023-10-12T14:39:54.553Z|00008|ovsdb_cs|DBG|unix:/var/run/openvswitch/db.sock: SERVER_SCHEMA_REQUESTED -> SERVER_SCHEMA_REQUESTED at lib/ovsdb-cs.c:423
   ```
6. Optional: Check the `ConfigMap` file has been applied by running the following command:

   ```
   for f in $(oc -n openshift-ovn-kubernetes get po -l 'app=ovnkube-node' --no-headers -o custom-columns=N:.metadata.name) ; do echo "---- $f ----" ; oc -n openshift-ovn-kubernetes exec -c ovnkube-controller $f --  pgrep -a -f  init-ovnkube-controller | grep -P -o '^.*loglevel\s+\d' ; done
   ```

   **Example output**

   ```
   ---- ovnkube-node-2dt57 ----
   60981 /usr/bin/ovnkube --init-ovnkube-controller xpst8-worker-c-vmh5n.c.openshift-qe.internal --init-node xpst8-worker-c-vmh5n.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 4
   ---- ovnkube-node-4zznh ----
   178034 /usr/bin/ovnkube --init-ovnkube-controller xpst8-master-2.c.openshift-qe.internal --init-node xpst8-master-2.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 4
   ---- ovnkube-node-548sx ----
   77499 /usr/bin/ovnkube --init-ovnkube-controller xpst8-worker-a-fjtnb.c.openshift-qe.internal --init-node xpst8-worker-a-fjtnb.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 4
   ---- ovnkube-node-6btrf ----
   73781 /usr/bin/ovnkube --init-ovnkube-controller xpst8-worker-b-p8rww.c.openshift-qe.internal --init-node xpst8-worker-b-p8rww.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 4
   ---- ovnkube-node-fkc9r ----
   130707 /usr/bin/ovnkube --init-ovnkube-controller xpst8-master-0.c.openshift-qe.internal --init-node xpst8-master-0.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 5
   ---- ovnkube-node-tk9l4 ----
   181328 /usr/bin/ovnkube --init-ovnkube-controller xpst8-master-1.c.openshift-qe.internal --init-node xpst8-master-1.c.openshift-qe.internal --config-file=/run/ovnkube-config/ovnkube.conf --ovn-empty-lb-events --loglevel 4
   ```

### [3.6. Checking the OVN-Kubernetes pod network connectivity](#nw-ovn-kubernetes-pod-connectivity-checks_ovn-kubernetes-sources-of-troubleshooting-information) Copy linkLink copied to clipboard!

To verify pod network connectivity in OpenShift Container Platform, you can inspect `PodNetworkConnectivityCheck` resources in the `openshift-network-diagnostics` namespace.

The connectivity check controller, in OpenShift Container Platform 4.10 and later, orchestrates connection verification checks in your cluster. These include Kubernetes API, OpenShift API and individual nodes. The results for the connection tests are stored in `PodNetworkConnectivity` objects in the `openshift-network-diagnostics` namespace. Connection tests are performed every minute in parallel.

**Prerequisites**

* You have access to the OpenShift CLI (`oc`).
* You are logged in to the cluster with the `cluster-admin` role.
* You have installed `jq`.

**Procedure**

1. To list the current `PodNetworkConnectivityCheck` objects, enter the following command:

   ```
   $ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics
   ```
2. View the most recent success for each connection object by using the following command:

   ```
   $ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics \
   -o json | jq '.items[]| .spec.targetEndpoint,.status.successes[0]'
   ```
3. View the most recent failures for each connection object by using the following command:

   ```
   $ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics \
   -o json | jq '.items[]| .spec.targetEndpoint,.status.failures[0]'
   ```
4. View the most recent outages for each connection object by using the following command:

   ```
   $ oc get podnetworkconnectivitychecks -n openshift-network-diagnostics \
   -o json | jq '.items[]| .spec.targetEndpoint,.status.outages[0]'
   ```

   The connectivity check controller also logs metrics from these checks into Prometheus.
5. View all the metrics by running the following command:

   ```
   $ oc exec prometheus-k8s-0 -n openshift-monitoring -- \
   promtool query instant  http://localhost:9090 \
   '{component="openshift-network-diagnostics"}'
   ```
6. View the latency between the source pod and the openshift api service for the last 5 minutes:

   ```
   $ oc exec prometheus-k8s-0 -n openshift-monitoring -- \
   promtool query instant  http://localhost:9090 \
   '{component="openshift-network-diagnostics"}'
   ```

### [3.7. Checking OVN-Kubernetes network traffic with OVS sampling using the CLI](#nw-ovn-kubernetes-observability_ovn-kubernetes-sources-of-troubleshooting-information) Copy linkLink copied to clipboard!

To trace OVN-Kubernetes network traffic with OVS sampling in OpenShift Container Platform, you can enable the `OVNObservability` feature gate and run `ovnkube-observ` from an `ovnkube-node` pod.

Important

Checking OVN-Kubernetes network traffic with OVS sampling is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

OVN-Kubernetes network traffic can be viewed with OVS sampling via the CLI for the following network APIs:

* `NetworkPolicy`
* `AdminNetworkPolicy`
* `BaselineNetworkPolicy`
* `UserDefinedNetwork` isolation
* `EgressFirewall`
* Multicast ACLs.

Scripts for these networking events are found in the `/usr/bin/ovnkube-observ` path of each OVN-Kubernetes node.

Although both the Network Observability Operator and checking OVN-Kubernetes network traffic with OVS sampling are good for debuggability, the Network Observability Operator is intended for observing network events. Alternatively, checking OVN-Kubernetes network traffic with OVS sampling using the CLI is intended to help with packet tracing; it can also be used while the Network Observability Operator is installed, however that is not a requirement.

Administrators can add the `--add-ovs-collect` option to view network traffic across the node, or pass in additional flags to filter result for specific pods. Additional flags can be found in the "OVN-Kubernetes network traffic with OVS sampling flags" section.

Use the following procedure to view OVN-Kubernetes network traffic using the CLI.

**Prerequisites**

* You are logged in to the cluster as a user with `cluster-admin` privileges.
* You have created a source pod and a destination pod and ran traffic between them.
* You have created at least one of the following network APIs: `NetworkPolicy`, `AdminNetworkPolicy`, `BaselineNetworkPolicy`, `UserDefinedNetwork` isolation, multicast, or egress firewalls.

**Procedure**

1. To enable the `OVNObservability` with OVS sampling feature, enable `TechPreviewNoUpgrade` feature set in the `FeatureGate` CR named `cluster` by entering the following command:

   ```
   $ oc patch --type=merge --patch '{"spec": {"featureSet": "TechPreviewNoUpgrade"}}' featuregate/cluster
   ```

   **Example output**

   ```
   featuregate.config.openshift.io/cluster patched
   ```
2. Confirm that the `OVNObservability` feature is enabled by entering the following command:

   ```
   $ oc get featuregate cluster -o yaml
   ```

   **Example output**

   ```
     featureGates:
   # ...
       enabled:
       - name: OVNObservability
   ```
3. Obtain a list of the pods inside of the namespace in which you have created one of the relevant network APIs by entering the following command. Note the `NODE` name of the pods, as they are used in the following step.

   ```
   $ oc get pods -n <namespace> -o wide
   ```

   **Example output**

   ```
   NAME              READY   STATUS    RESTARTS   AGE     IP            NODE                                       NOMINATED NODE   READINESS GATES
   destination-pod   1/1     Running   0          53s     10.131.0.23   ci-ln-1gqp7b2-72292-bb9dv-worker-a-gtmpc   <none>           <none>
   source-pod        1/1     Running   0          56s     10.131.0.22   ci-ln-1gqp7b2-72292-bb9dv-worker-a-gtmpc   <none>           <none>
   ```
4. Obtain a list of OVN-Kubernetes pods and locate the pod that shares the same `NODE` as the pods from the previous step by entering the following command:

   ```
   $ oc get pods -n openshift-ovn-kubernetes -o wide
   ```

   **Example output**

   ```
   NAME
   ...                             READY   STATUS    RESTARTS      AGE   IP           NODE                                       NOMINATED NODE
   ovnkube-node-jzn5b              8/8     Running   1 (34m ago)   37m   10.0.128.2   ci-ln-1gqp7b2-72292-bb9dv-worker-a-gtmpc   <none>
   ...
   ```
5. Open a bash shell inside of the `ovnkube-node` pod by entering the following command:

   ```
   $ oc exec -it <pod_name> -n openshift-ovn-kubernetes -- bash
   ```
6. While inside of the `ovnkube-node` pod, you can run the `ovnkube-observ -add-ovs-collector` script to show network events using the OVS collector. For example:

   ```
   # /usr/bin/ovnkube-observ -add-ovs-collector
   ```

   **Example output**

   ```
   ...
   2024/12/02 19:41:41.327584 OVN-K message: Allowed by default allow from local node policy, direction ingress
   2024/12/02 19:41:41.327593 src=10.131.0.2, dst=10.131.0.6

   2024/12/02 19:41:41.327692 OVN-K message: Allowed by default allow from local node policy, direction ingress
   2024/12/02 19:41:41.327715 src=10.131.0.6, dst=10.131.0.2
   ...
   ```
7. You can filter the content by type, such as source pods, by entering the following command with the `-filter-src-ip` flag and your pod’s IP address. For example:

   ```
   # /usr/bin/ovnkube-observ -add-ovs-collector -filter-src-ip <pod_ip_address>
   ```

   **Example output**

   ```
   ...
   Found group packets, id 14
   2024/12/10 16:27:12.456473 OVN-K message: Allowed by admin network policy allow-egress-group1, direction Egress
   2024/12/10 16:27:12.456570 src=10.131.0.22, dst=10.131.0.23

   2024/12/10 16:27:14.484421 OVN-K message: Allowed by admin network policy allow-egress-group1, direction Egress
   2024/12/10 16:27:14.484428 src=10.131.0.22, dst=10.131.0.23

   2024/12/10 16:27:12.457222 OVN-K message: Allowed by network policy test:allow-ingress-from-specific-pod, direction Ingress
   2024/12/10 16:27:12.457228 src=10.131.0.22, dst=10.131.0.23

   2024/12/10 16:27:12.457288 OVN-K message: Allowed by network policy test:allow-ingress-from-specific-pod, direction Ingress
   2024/12/10 16:27:12.457299 src=10.131.0.22, dst=10.131.0.23
   ...
   ```

   For a full list of flags that can be passed in with `/usr/bin/ovnkube-observ`, see "OVN-Kubernetes network traffic with OVS sampling flags".

#### [3.7.1. OVN-Kubernetes network traffic with OVS sampling flags](#observability-ovs-sampling-flags_ovn-kubernetes-sources-of-troubleshooting-information) Copy linkLink copied to clipboard!

To filter OVN-Kubernetes traffic samples from `ovnkube-observ`, you can pass command line flags that limit output and collector options.

After you have opened a bash shell inside of the `ovnkube-node` pod, the following flags are available and can be appended using the following syntax:

**Command syntax**

```
# /usr/bin/ovnkube-observ <flag>
```

Expand

| Flag | Description |
| --- | --- |
| `-h` | Returns a complete list flags that can be used with the `usr/bin/ovnkube-observ` command. ` |
| `-add-ovs-collector` | Add OVS collector to enable sampling. Use with caution. Make sure no one else is using observability. |
| `-enable-enrichment` | Enrich samples with NBDB data. Defaults to `true`. |
| `-filter-dst-ip` | Filter only packets to a given destination IP. |
| `-filter-src-ip` | Filters only packets from a given source IP. |
| `-log-cookie` | Print raw sample cookie with psample group\_id. |
| `-output-file` | Output file to write the samples to. |
| `-print-full-packet` | Print full received packet. When false, only source and destination IPs are printed with every sample. |

Show more

## [Chapter 4. Tracing Openflow with ovnkube-trace](#ovn-kubernetes-tracing-using-ovntrace) Copy linkLink copied to clipboard!

To trace Open vSwitch and OVN traffic flows in OpenShift Container Platform, you can use the `ovnkube-trace` utility, which runs `ovn-trace`, `ovs-appctl ofproto/trace`, and `ovn-detrace` in a single correlated output.

You can execute the `ovnkube-trace` binary from a dedicated container. For releases after OpenShift Container Platform 4.7, you can also copy the binary to a local host and execute it from that host.

### [4.1. Installing the ovnkube-trace on local host](#nw-ovn-kubernetes-install-ovnkube-trace-local_ovn-kubernetes-tracing-with-ovnkube) Copy linkLink copied to clipboard!

To run `ovnkube-trace` from your local host against a cluster, you can copy the binary from an `ovnkube-control-plane` pod and use familiar Kubernetes namespace and pod arguments.

The `ovnkube-trace` tool traces packet simulations for arbitrary UDP or TCP traffic between points in an OVN-Kubernetes driven OpenShift Container Platform cluster.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with `cluster-admin` privileges.

**Procedure**

1. Create a pod variable by using the following command:

   ```
   $  POD=$(oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-control-plane -o name | head -1 | awk -F '/' '{print $NF}')
   ```
2. Run the following command on your local host to copy the binary from the `ovnkube-control-plane` pods:

   ```
   $  oc cp -n openshift-ovn-kubernetes $POD:/usr/bin/ovnkube-trace -c ovnkube-cluster-manager ovnkube-trace
   ```

   Note

   If you are using Red Hat Enterprise Linux (RHEL) 8 to run the `ovnkube-trace` tool, you must copy the file `/usr/lib/rhel8/ovnkube-trace` to your local host.
3. Make `ovnkube-trace` executable by running the following command:

   ```
   $  chmod +x ovnkube-trace
   ```
4. Display the options available with `ovnkube-trace` by running the following command:

   ```
   $  ./ovnkube-trace -help
   ```

   **Example output**

   ```
   Usage of ./ovnkube-trace:
     -addr-family string
       	Address family (ip4 or ip6) to be used for tracing (default "ip4")
     -dst string
       	dest: destination pod name
     -dst-ip string
       	destination IP address (meant for tests to external targets)
     -dst-namespace string
       	k8s namespace of dest pod (default "default")
     -dst-port string
       	dst-port: destination port (default "80")
     -kubeconfig string
       	absolute path to the kubeconfig file
     -loglevel string
       	loglevel: klog level (default "0")
     -ovn-config-namespace string
       	namespace used by ovn-config itself
     -service string
       	service: destination service name
     -skip-detrace
       	skip ovn-detrace command
     -src string
       	src: source pod name
     -src-namespace string
       	k8s namespace of source pod (default "default")
     -tcp
       	use tcp transport protocol
     -udp
       	use udp transport protocol
   ```

   The command-line arguments supported are familiar Kubernetes constructs, such as namespaces, pods, services so you do not need to find the MAC address, the IP address of the destination nodes, or the ICMP type.

   The log levels are:

   * 0 (minimal output)
   * 2 (more verbose output showing results of trace commands)
   * 5 (debug output)

### [4.2. Running ovnkube-trace](#nw-ovn-kubernetes-running-ovnkube-trace_ovn-kubernetes-tracing-with-ovnkube) Copy linkLink copied to clipboard!

To simulate packet forwarding in an OVN logical network, you can run `ovnkube-trace` with source and destination pods, ports, and log levels.

The examples in the following procedure show DNS resolution and default-deny network policy troubleshooting.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.
* You have installed the `ovnkube-trace` binary on your local host.

**Procedure**

1. Start a web service in the default namespace by entering the following command:

   ```
   $ oc run web --namespace=default --image=quay.io/openshifttest/nginx --labels="app=web" --expose --port=80
   ```
2. List the pods running in the `openshift-dns` namespace:

   ```
   $ oc get pods -n openshift-dns
   ```

   The output is similar to the following:

   ```
   NAME                  READY   STATUS    RESTARTS   AGE
   dns-default-8s42x     2/2     Running   0          5h8m
   dns-default-mdw6r     2/2     Running   0          4h58m
   dns-default-p8t5h     2/2     Running   0          4h58m
   dns-default-rl6nk     2/2     Running   0          5h8m
   dns-default-xbgqx     2/2     Running   0          5h8m
   dns-default-zv8f6     2/2     Running   0          4h58m
   node-resolver-62jjb   1/1     Running   0          5h8m
   node-resolver-8z4cj   1/1     Running   0          4h59m
   node-resolver-bq244   1/1     Running   0          5h8m
   node-resolver-hc58n   1/1     Running   0          4h59m
   node-resolver-lm6z4   1/1     Running   0          5h8m
   node-resolver-zfx5k   1/1     Running   0          5h
   ```
3. Run the following `ovnkube-trace` command to verify DNS resolution is working:

   ```
   $ ./ovnkube-trace \
     -src-namespace default \
     -src web \
     -dst-namespace openshift-dns \
     -dst dns-default-p8t5h \
     -udp -dst-port 53 \
     -loglevel 0
   ```

   where:

   `-src-namespace`
   :   Specifies namespace of the source pod.

   `-src`
   :   Specifies source pod name.

   `-dst-namespace`
   :   Specifies namespace of destination pod.

   `-dst`
   :   Specifies destination pod name.

   `-udp`
   :   Specifies use of the `udp` transport protocol. Port 53 is the port the DNS service uses.

   `-loglevel`
   :   Specifies the log level to 0 (0 is minimal and 5 is debug).

       If the `src&dst` pod lands on the same node, the output is similar to the following:

       ```
       ovn-trace source pod to destination pod indicates success from web to dns-default-p8t5h
       ovn-trace destination pod to source pod indicates success from dns-default-p8t5h to web
       ovs-appctl ofproto/trace source pod to destination pod indicates success from web to dns-default-p8t5h
       ovs-appctl ofproto/trace destination pod to source pod indicates success from dns-default-p8t5h to web
       ovn-detrace source pod to destination pod indicates success from web to dns-default-p8t5h
       ovn-detrace destination pod to source pod indicates success from dns-default-p8t5h to web
       ```

       If the `src&dst` pod lands on a different node, the output is similar to the following:

       ```
       ovn-trace source pod to destination pod indicates success from web to dns-default-8s42x
       ovn-trace (remote) source pod to destination pod indicates success from web to dns-default-8s42x
       ovn-trace destination pod to source pod indicates success from dns-default-8s42x to web
       ovn-trace (remote) destination pod to source pod indicates success from dns-default-8s42x to web
       ovs-appctl ofproto/trace source pod to destination pod indicates success from web to dns-default-8s42x
       ovs-appctl ofproto/trace destination pod to source pod indicates success from dns-default-8s42x to web
       ovn-detrace source pod to destination pod indicates success from web to dns-default-8s42x
       ovn-detrace destination pod to source pod indicates success from dns-default-8s42x to web
       ```

       The output indicates success from the deployed pod to the DNS port and also indicates that it is successful going back in the other direction. So you know bi-directional traffic is supported on UDP port 53 if my web pod wants to do dns resolution from core DNS.

       If for example that did not work and you wanted to get the `ovn-trace`, the `ovs-appctl` of `proto/trace` and `ovn-detrace`, and more debug type information increase the log level to 2 and run the command again as follows:

       ```
       $ ./ovnkube-trace \
         -src-namespace default \
         -src web \
         -dst-namespace openshift-dns \
         -dst dns-default-467qw \
         -udp -dst-port 53 \
         -loglevel 2
       ```

       The output from this increased log level is too much to list here. In a failure situation the output of this command shows which flow is dropping that traffic. For example an egress or ingress network policy may be configured on the cluster that does not allow that traffic.

### [4.3. Testing a default deny policy with ovnkube-trace](#nw-ovn-kubernetes-ovnkube-trace-default-deny_ovn-kubernetes-tracing-with-ovnkube) Copy linkLink copied to clipboard!

To verify that an ingress default deny network policy blocks traffic in OpenShift Container Platform, you can run `ovnkube-trace` with a higher log level and read the ACL debug output. You can add an allow policy for labeled namespaces and confirm that traffic succeeds.

**Prerequisites**

* You have installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.
* You have installed the `ovnkube-trace` binary on your local host.

**Procedure**

1. Create the following YAML that defines a `deny-by-default` policy to deny ingress from all pods in all namespaces. Save the YAML in the `deny-by-default.yaml` file:

   ```
   kind: NetworkPolicy
   apiVersion: networking.k8s.io/v1
   metadata:
     name: deny-by-default
     namespace: default
   spec:
     podSelector: {}
     ingress: []
   ```
2. Apply the policy by entering the following command:

   ```
   $ oc apply -f deny-by-default.yaml
   ```

   **Example output**

   ```
   networkpolicy.networking.k8s.io/deny-by-default created
   ```
3. Start a web service in the `default` namespace by entering the following command:

   ```
   $ oc run web --namespace=default --image=quay.io/openshifttest/nginx --labels="app=web" --expose --port=80
   ```
4. Run the following command to create the `prod` namespace:

   ```
   $ oc create namespace prod
   ```
5. Run the following command to label the `prod` namespace:

   ```
   $ oc label namespace/prod purpose=production
   ```
6. To deploy an `alpine` image in the `prod` namespace and start a shell, run the following command:

   ```
   $ oc run test-6459 --namespace=prod --rm -i -t --image=alpine -- sh
   ```
7. Open another terminal session.
8. In this new terminal session run `ovn-trace` to verify the failure in communication between the source pod `test-6459` running in namespace `prod` and destination pod running in the `default` namespace:

   ```
   $ ./ovnkube-trace \
    -src-namespace prod \
    -src test-6459 \
    -dst-namespace default \
    -dst web \
    -tcp -dst-port 80 \
    -loglevel 0
   ```

   **Example output**

   ```
   ovn-trace source pod to destination pod indicates failure from test-6459 to web
   ```
9. Increase the log level to 2 to expose the reason for the failure by running the following command:

   ```
   $ ./ovnkube-trace \
    -src-namespace prod \
    -src test-6459 \
    -dst-namespace default \
    -dst web \
    -tcp -dst-port 80 \
    -loglevel 2
   ```

   **Example output**

   ```
   ...
   ------------------------------------------------
    3. ls_out_acl_hint (northd.c:7454): !ct.new && ct.est && !ct.rpl && ct_mark.blocked == 0, priority 4, uuid 12efc456
       reg0[8] = 1;
       reg0[10] = 1;
       next;
    5. ls_out_acl_action (northd.c:7835): reg8[30..31] == 0, priority 500, uuid 69372c5d
       reg8[30..31] = 1;
       next(4);
    5. ls_out_acl_action (northd.c:7835): reg8[30..31] == 1, priority 500, uuid 2fa0af89
       reg8[30..31] = 2;
       next(4);
    4. ls_out_acl_eval (northd.c:7691): reg8[30..31] == 2 && reg0[10] == 1 && (outport == @a16982411286042166782_ingressDefaultDeny), priority 2000, uuid 447d0dab
       reg8[17] = 1;
       ct_commit { ct_mark.blocked = 1; };
       next;
   ...
   ```

   where: `ct_commit { ct_mark.blocked = 1; };`:: Specifies that ingress traffic is blocked due to the default deny policy being in place.
10. Create a policy that allows traffic from all pods in a particular namespaces with a label `purpose=production`. Save the YAML in the `web-allow-prod.yaml` file:

    ```
    kind: NetworkPolicy
    apiVersion: networking.k8s.io/v1
    metadata:
      name: web-allow-prod
      namespace: default
    spec:
      podSelector:
        matchLabels:
          app: web
      policyTypes:
      - Ingress
      ingress:
      - from:
        - namespaceSelector:
            matchLabels:
              purpose: production
    ```
11. Apply the policy by entering the following command:

    ```
    $ oc apply -f web-allow-prod.yaml
    ```
12. Run `ovnkube-trace` to verify that traffic is now allowed by entering the following command:

    ```
    $ ./ovnkube-trace \
     -src-namespace prod \
     -src test-6459 \
     -dst-namespace default \
     -dst web \
     -tcp -dst-port 80 \
     -loglevel 0
    ```

    **Example output**

    ```
    ovn-trace source pod to destination pod indicates success from test-6459 to web
    ovn-trace destination pod to source pod indicates success from web to test-6459
    ovs-appctl ofproto/trace source pod to destination pod indicates success from test-6459 to web
    ovs-appctl ofproto/trace destination pod to source pod indicates success from web to test-6459
    ovn-detrace source pod to destination pod indicates success from test-6459 to web
    ovn-detrace destination pod to source pod indicates success from web to test-6459
    ```
13. Run the following command in the shell that was opened in step six to connect nginx to the web-server:

    ```
    $ wget -qO- --timeout=2 http://web.default
    ```

    **Example output**

    ```
    <!DOCTYPE html>
    <html>
    <head>
    <title>Welcome to nginx!</title>
    <style>
      body {
        width: 35em;
        margin: 0 auto;
        font-family: Tahoma, Verdana, Arial, sans-serif;
      }
    </style>
    </head>
    <body>
    <h1>Welcome to nginx!</h1>
    <p>If you see this page, the nginx web server is successfully installed and
    working. Further configuration is required.</p>

    <p>For online documentation and support please refer to
    <a href="http://nginx.org/">nginx.org</a>.<br/>
    Commercial support is available at
    <a href="http://nginx.com/">nginx.com</a>.</p>

    <p><em>Thank you for using nginx.</em></p>
    </body>
    </html>
    ```

## [Chapter 5. Converting to IPv4/IPv6 dual-stack networking](#converting-to-dual-stack) Copy linkLink copied to clipboard!

To enable IPv4 and IPv6 on your cluster network in OpenShift Container Platform, you can convert a single-stack cluster to dual-stack networking. After conversion, new and existing pods can use both address families when you re-create workloads as needed.

Important

When using dual-stack networking where IPv6 is required, you cannot use IPv4-mapped IPv6 addresses, such as `::FFFF:198.51.100.1`.

### [5.1. Converting to a dual-stack cluster network](#nw-dual-stack-convert_converting-to-dual-stack) Copy linkLink copied to clipboard!

To convert your cluster network from IPv4 single-stack to dual-stack in OpenShift Container Platform, you can patch the cluster network and, on installer-provisioned infrastructure, the infrastructure custom resources. You must re-create existing pods after conversion to receive IPv6 addresses.

As a cluster administrator, you can convert your single-stack cluster network to a dual-stack cluster network.

Important

After converting your cluster to use dual-stack networking, you must re-create any existing pods for them to receive IPv6 addresses, because only new pods are assigned IPv6 addresses.

Converting a single-stack cluster network to a dual-stack cluster network consists of creating patches and applying them to the network and infrastructure of the cluster. You can convert to a dual-stack cluster network for a cluster that runs on either installer-provisioned infrastructure or user-provisioned infrastructure.

Note

Each patch operation that changes `clusterNetwork`, `serviceNetwork`, `apiServerInternalIPs`, and `ingressIP` objects triggers a restart of the cluster. Changing the `MachineNetworks` object does not cause a reboot of the cluster.

On installer-provisioned infrastructure only, if you need to add IPv6 virtual IPs (VIPs) for API and Ingress services to an existing dual-stack-configured cluster, you need to patch only the infrastructure and not the network for the cluster.

Important

If you already upgraded your cluster to OpenShift Container Platform 4.16 or later and you need to convert the single-stack cluster network to a dual-stack cluster network, you must specify an existing IPv4 `machineNetwork` network configuration from the `install-config.yaml` file for API and Ingress services in the YAML configuration patch file. This configuration ensures that IPv4 traffic exists in the same network interface as the default gateway.

The following example adds an IPv4 address block for the `machineNetwork` network:

```
- op: add
  path: /spec/platformSpec/baremetal/machineNetworks/-
  value: 192.168.1.0/24
  # ...
```

where:

`/spec/platformSpec/baremetal/machineNetworks/-`
:   Specifies an address block for the `machineNetwork` network where your machines operate. You must select both API and Ingress IP addresses for the machine network.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.
* Your cluster uses the OVN-Kubernetes network plugin.
* The cluster nodes have IPv6 addresses.
* You have configured an IPv6-enabled router based on your infrastructure.

**Procedure**

1. To specify IPv6 address blocks for cluster and service networks, create a YAML configuration patch file that has a similar configuration to the following example:

   ```
   - op: add
     path: /spec/clusterNetwork/-
     value:
       cidr: fd01::/48
       hostPrefix: 64
   - op: add
     path: /spec/serviceNetwork/-
     value: fd02::/112
   ```

   where:

   `/spec/clusterNetwork/-`
   :   Specifies an object with the `cidr` and `hostPrefix` parameters. The host prefix must be `64` or greater. The IPv6 Classless Inter-Domain Routing (CIDR) prefix must be large enough to accommodate the specified host prefix.

   `/spec/serviceNetwork/-`
   :   Specifies an IPv6 CIDR with a prefix of `112`. Kubernetes uses only the lowest 16 bits. For a prefix of `112`, IP addresses are assigned from `112` to `128` bits.
2. Patch the cluster network configuration by entering the following command in your CLI:

   ```
   $ oc patch network.config.openshift.io cluster \
     --type='json' --patch-file <file>.yaml
   ```

   For `<file>`, specify the name of the YAML file you created.

   **Example output**

   ```
   network.config.openshift.io/cluster patched
   ```
3. On installer-provisioned infrastructure where you added IPv6 VIPs for API and Ingress services, complete the following steps:

   1. Specify IPv6 VIPs for API and Ingress services for your cluster. Create a YAML configuration patch file that has a similar configuration to the following example:

      ```
      - op: add
        path: /spec/platformSpec/baremetal/machineNetworks/-
        value: fd2e:6f44:5dd8::/64
      - op: add
        path: /spec/platformSpec/baremetal/apiServerInternalIPs/-
        value: fd2e:6f44:5dd8::4
      - op: add
        path: /spec/platformSpec/baremetal/ingressIPs/-
        value: fd2e:6f44:5dd8::5
      ```

      where:

      `/spec/platformSpec/baremetal/machineNetworks/-`
      :   Specifies an address block for the `machineNetwork` network where your machines operate. You must select both API and Ingress IP addresses for the machine network.

      `/spec/platformSpec/baremetal/apiServerInternalIPs/-`
      :   Specifies each file path according to your platform. The example demonstrates a file path on a bare metal platform.
   2. Patch the infrastructure by entering the following command in your CLI:

      ```
      $ oc patch infrastructure cluster \
        --type='json' --patch-file <file>.yaml
      ```

      For `<file>`, specify the name of the YAML file you created.

      **Example output**

      ```
      infrastructure/cluster patched
      ```

**Verification**

1. Show the cluster network configuration by entering the following command in your CLI:

   ```
   $ oc describe network
   ```
2. Verify the successful installation of the patch on the network configuration by checking that the cluster network configuration recognizes the IPv6 address blocks that you specified in the YAML file.

   **Example output**

   ```
   # ...
   Status:
     Cluster Network:
       Cidr:               10.128.0.0/14
       Host Prefix:        23
       Cidr:               fd01::/48
       Host Prefix:        64
     Cluster Network MTU:  1400
     Network Type:         OVNKubernetes
     Service Network:
       172.30.0.0/16
       fd02::/112
   # ...
   ```
3. Complete the following additional tasks for a cluster that runs on installer-provisioned infrastructure:

   1. Show the cluster infrastructure configuration by entering the following command in your CLI:

      ```
      $ oc describe infrastructure
      ```
   2. Verify the successful installation of the patch on the cluster infrastructure by checking that the infrastructure recognizes the IPv6 address blocks that you specified in the YAML file.

      **Example output**

      ```
      # ...
      spec:
      # ...
        platformSpec:
          baremetal:
            apiServerInternalIPs:
            - 192.168.123.5
            - fd2e:6f44:5dd8::4
            ingressIPs:
            - 192.168.123.10
            - fd2e:6f44:5dd8::5
      status:
      # ...
        platformStatus:
          baremetal:
            apiServerInternalIP: 192.168.123.5
            apiServerInternalIPs:
            - 192.168.123.5
            - fd2e:6f44:5dd8::4
            ingressIP: 192.168.123.10
            ingressIPs:
            - 192.168.123.10
            - fd2e:6f44:5dd8::5
      # ...
      ```

### [5.2. Converting to a single-stack cluster network](#nw-dual-stack-convert-back-single-stack_converting-to-dual-stack) Copy linkLink copied to clipboard!

To revert dual-stack networking in OpenShift Container Platform, you can edit the cluster network configuration and remove the IPv4 or IPv6 blocks you added during dual-stack conversion. You can convert back only to the same single-stack family you had before dual-stack (IPv4 or IPv6).

Important

If you originally converted your IPv4 single-stack cluster network to a dual-stack cluster, you can convert only back to the IPv4 single-stack cluster and not an IPv6 single-stack cluster network. The same restriction applies for converting back to an IPv6 single-stack cluster network.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.
* Your cluster uses the OVN-Kubernetes network plugin.
* The cluster nodes have IPv6 addresses.
* You have enabled dual-stack networking.

**Procedure**

1. Edit the `networks.config.openshift.io` custom resource (CR) by running the following command:

   ```
   $ oc edit networks.config.openshift.io
   ```
2. Remove the IPv4 or IPv6 configuration that you added to the `cidr` and the `hostPrefix` parameters from completing the "Converting to a dual-stack cluster network " procedure steps.

## [Chapter 6. Configuring OVN-Kubernetes internal IP address subnets](#configure-ovn-kubernetes-subnets) Copy linkLink copied to clipboard!

As a cluster administrator, you can change the IP address ranges that the OVN-Kubernetes network plugin uses for the join and transit subnets.

### [6.1. Configuring the OVN-Kubernetes join subnet](#nw-ovn-kubernetes-change-join-subnet_configure-ovn-kubernetes-subnets) Copy linkLink copied to clipboard!

You can change the join subnet used by OVN-Kubernetes to avoid conflicting with any existing subnets already in use in your environment.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in to the cluster with a user with `cluster-admin` privileges.
* Ensure that the cluster uses the OVN-Kubernetes network plugin.

**Procedure**

* To change the OVN-Kubernetes join subnet, enter the following command:

  ```
  $ oc patch network.operator.openshift.io cluster --type='merge' \
    -p='{"spec":{"defaultNetwork":{"ovnKubernetesConfig":
      {"ipv4":{"internalJoinSubnet": "<join_subnet>"},
      "ipv6":{"internalJoinSubnet": "<join_subnet>"}}}}}'
  ```

  where:

  `<join_subnet>`
  :   Specifies an IP address subnet for internal use by OVN-Kubernetes. The subnet must be larger than the number of nodes in the cluster and it must be large enough to accommodate one IP address per node in the cluster. This subnet cannot overlap with any other subnets used by OpenShift Container Platform or on the host itself. The default value for IPv4 is `100.64.0.0/16` and the default value for IPv6 is `fd98::/64`.

  **Example output**

  ```
  network.operator.openshift.io/cluster patched
  ```

**Verification**

* To confirm that the configuration is active, enter the following command:

  ```
  $ oc get network.operator.openshift.io \
    -o jsonpath="{.items[0].spec.defaultNetwork}"
  ```

  The command operation can take up to 30 minutes for this change to take effect.

  **Example output**

  ```
  {
    "ovnKubernetesConfig": {
      "ipv4": {
        "internalJoinSubnet": "100.64.1.0/16"
      },
    },
    "type": "OVNKubernetes"
  }
  ```

### [6.2. Configuring the OVN-Kubernetes masquerade subnet as a post-installation operation](#nw-ovn-k-day-2-masq-subnet_configure-ovn-kubernetes-subnets) Copy linkLink copied to clipboard!

You can change the masquerade subnet used by OVN-Kubernetes as a post-installation operation to avoid conflicts with any existing subnets that are already in use in your environment.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in to the cluster as a user with `cluster-admin` privileges.

**Procedure**

* Change your cluster’s masquerade subnet:

  + For dualstack clusters using IPv6, run the following command:

    ```
    $ oc patch networks.operator.openshift.io cluster --type=merge -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig":{"ipv4":{"internalMasqueradeSubnet": "<ipv4_masquerade_subnet>"},"ipv6":{"internalMasqueradeSubnet": "<ipv6_masquerade_subnet>"}}}}}}'
    ```

    where:

    `ipv4_masquerade_subnet`
    :   Specifies an IP address to be used as the IPv4 masquerade subnet. This range cannot overlap with any other subnets used by OpenShift Container Platform or on the host itself. In versions of OpenShift Container Platform earlier than 4.17, the default value for IPv4 was `169.254.169.0/29`, and clusters that were upgraded to version 4.17 maintain this value. For new clusters starting from version 4.17, the default value is `169.254.0.0/17`.

    `ipv6_masquerade_subnet`
    :   Specifies an IP address to be used as the IPv6 masquerade subnet. This range cannot overlap with any other subnets used by OpenShift Container Platform or on the host itself. The default value for IPv6 is `fd69::/125`.
  + For clusters using IPv4, run the following command:

    ```
    $ oc patch networks.operator.openshift.io cluster --type=merge -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig":{"ipv4":{"internalMasqueradeSubnet": "<ipv4_masquerade_subnet>"}}}}}}'
    ```

    where:

    `ipv4_masquerade_subnet`::Specifies an IP address to be used as the IPv4 masquerade subnet. This range cannot overlap with any other subnets used by OpenShift Container Platform or on the host itself. In versions of OpenShift Container Platform earlier than 4.17, the default value for IPv4 was `169.254.169.0/29`, and clusters that were upgraded to version 4.17 maintain this value. For new clusters starting from version 4.17, the default value is `169.254.0.0/17`.

### [6.3. Configuring the OVN-Kubernetes transit subnet](#nw-ovn-kubernetes-change-transit-subnet_configure-ovn-kubernetes-subnets) Copy linkLink copied to clipboard!

You can change the transit subnet used by OVN-Kubernetes to avoid conflicting with any existing subnets already in use in your environment.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in to the cluster with a user with `cluster-admin` privileges.
* Ensure that the cluster uses the OVN-Kubernetes network plugin.

**Procedure**

* To change the OVN-Kubernetes transit subnet, enter the following command:

  ```
  $ oc patch network.operator.openshift.io cluster --type='merge' \
    -p='{"spec":{"defaultNetwork":{"ovnKubernetesConfig":
      {"ipv4":{"internalTransitSwitchSubnet": "<transit_subnet>"},
      "ipv6":{"internalTransitSwitchSubnet": "<transit_subnet>"}}}}}'
  ```

  where:

  `<transit_subnet>`
  :   Specifies an IP address subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. The default value for IPv4 is `100.88.0.0/16` and the default value for IPv6 is `fd97::/64`.

  **Example output**

  ```
  network.operator.openshift.io/cluster patched
  ```

**Verification**

* To confirm that the configuration is active, enter the following command:

  ```
  $ oc get network.operator.openshift.io \
    -o jsonpath="{.items[0].spec.defaultNetwork}"
  ```

  It can take up to 30 minutes for this change to take effect.

  **Example output**

  ```
  {
    "ovnKubernetesConfig": {
      "ipv4": {
        "internalTransitSwitchSubnet": "100.88.1.0/16"
      },
    },
    "type": "OVNKubernetes"
  }
  ```

## [Chapter 7. Configuring a gateway](#configuring-gateway) Copy linkLink copied to clipboard!

As a cluster administrator you can configure the `gatewayConfig` object to manage how external traffic leaves the cluster. You do so by setting the `routingViaHost` parameter to one of the following values:

* `true` means that egress traffic routes through a specific local gateway on the node that hosts the pod. Egress traffic routes through the host and this traffic applies to the routing table of the host.
* `false` means that egress traffic routes through a dedicated node but a group of nodes share the same gateway. Egress traffic does not route through the host. The Open vSwitch (OVS) outputs traffic directly to the node IP interface.

### [7.1. Configuring egress routing policies](#nwt-configure-egress-routing-policies_configuring-gateway-mode) Copy linkLink copied to clipboard!

As a cluster administrator you can configure egress routing policies by using the `gatewayConfig` specification in the Cluster Network Operator (CNO). You can use the following procedure to set the `routingViaHost` field to `true` or `false`.

You can follow the optional step in the procedure to enable IP forwarding alongside the `routingViaHost=true` configuration if you need the host network of the node to act as a router for traffic not related to OVN-Kubernetes. For example, possible use cases for combining local gateway with IP forwarding include:

* Configuring all pod egress traffic to be forwarded via the node’s IP
* Integrating OVN-Kubernetes CNI with external network address translation (NAT) devices
* Configuring OVN-Kubernetes CNI to use a kernel routing table

**Prerequisites**

* You are logged in as a user with administrator privileges.

**Procedure**

1. Back up the existing network configuration by running the following command:

   ```
   $ oc get network.operator cluster -o yaml > network-config-backup.yaml
   ```
2. Set the `routingViaHost` parameter to `true` by entering the following command. Egress traffic then gets routed through a specific gateway according to the routes that you configured on the node.

   ```
   $ oc patch networks.operator.openshift.io cluster --type=merge -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig":{"routingViaHost": true}}}}}'
   ```
3. Verify the correct application of the `routingViaHost=true` configuration by running the following command:

   ```
   $ oc get networks.operator.openshift.io cluster -o yaml | grep -A 5 "gatewayConfig"
   ```

   **Example output**

   ```
   apiVersion: operator.openshift.io/v1
   kind: Network
   metadata:
     name: cluster
   # ...
   gatewayConfig:
           ipv4: {}
           ipv6: {}
           routingViaHost: true
         genevePort: 6081
         ipsecConfig:
   # ...
   ```

   * `routingViaHost`:: Specifies a value of `true` means that egress traffic gets routed through a specific local gateway on the node that hosts the pod. A value of `false` for the parameter means that a group of nodes share a single gateway so traffic does not get routed through a single host.
4. Optional: Enable IP forwarding globally by running the following command:

   ```
   $ oc patch network.operator cluster --type=merge -p '{"spec":{"defaultNetwork":{"ovnKubernetesConfig":{"gatewayConfig":{"ipForwarding": "Global"}}}}}'
   ```

   1. Verify that the `ipForwarding` spec has been set to `Global` by running the following command:

      ```
      $ oc get networks.operator.openshift.io cluster -o yaml | grep -A 5 "gatewayConfig"
      ```

      **Example output**

      ```
      apiVersion: operator.openshift.io/v1
      kind: Network
      metadata:
        name: cluster
      # ...
      gatewayConfig:
              ipForwarding: Global
              ipv4: {}
              ipv6: {}
              routingViaHost: true
            genevePort: 6081
      # ...
      ```

## [Chapter 8. Configure an external gateway on the default network](#configuring-secondary-external-gateway) Copy linkLink copied to clipboard!

As a cluster administrator, you can configure an external gateway on the default network.

This feature offers the following benefits:

* Granular control over egress traffic on a per-namespace basis
* Flexible configuration of static and dynamic external gateway IP addresses
* Support for both IPv4 and IPv6 address families

### [8.1. Prerequisites](#configuring-secondary-external-gateway_prerequisites) Copy linkLink copied to clipboard!

* Your cluster uses the OVN-Kubernetes network plugin.
* Your infrastructure is configured to route traffic from the secondary external gateway.

### [8.2. How OpenShift Container Platform determines the external gateway IP address](#nw-secondary-ext-gw-about_configuring-secondary-external-gateway) Copy linkLink copied to clipboard!

You configure a secondary external gateway with the `AdminPolicyBasedExternalRoute` custom resource (CR) from the `k8s.ovn.org` API group. The CR supports static and dynamic approaches for specifying an IP address for an external gateway.

Each namespace that an `AdminPolicyBasedExternalRoute` CR targets cannot be selected by any other `AdminPolicyBasedExternalRoute` CR. A namespace cannot have concurrent secondary external gateways.

Changes to policies are isolated in the controller. If a policy fails to apply, changes to other policies do not trigger a retry of other policies. Policies are re-evaluated when updates occur to the policy or to related objects such as target namespaces, pod gateways, or the namespaces that host them from dynamic hops. When re-evaluated, the policy applies any differences from the changes.

Static assignment
:   You specify an IP address directly.

Dynamic assignment
:   You specify an IP address indirectly, with namespace and pod selectors, and an optional network attachment definition.

Important

If the name of a network attachment definition is provided, the external gateway IP address of the network attachment is used.

If the name of a network attachment definition is not provided, the external gateway IP address for the pod itself is used. However, this approach works only if the pod is configured with `hostNetwork` set to `true`.

### [8.3. AdminPolicyBasedExternalRoute object configuration](#nw-secondary-ext-gw-object_configuring-secondary-external-gateway) Copy linkLink copied to clipboard!

You can define an `AdminPolicyBasedExternalRoute` object, which is cluster scoped, with specific properties.

A namespace can be selected by only one `AdminPolicyBasedExternalRoute` CR at a time.

The following tables detail supported fields for objects.

Expand

Table 8.1. AdminPolicyBasedExternalRoute object

| Field | Type | Description |
| --- | --- | --- |
| `metadata.name` | `string` | Specifies the name of the `AdminPolicyBasedExternalRoute` object. |
| `spec.from` | `string` | Specifies a namespace selector that the routing policies apply to. Only `namespaceSelector` is supported for external traffic. For example:  ``` from:   namespaceSelector:     matchLabels:       kubernetes.io/metadata.name: novxlan-externalgw-ecmp-4059 ```  A namespace can only be targeted by one `AdminPolicyBasedExternalRoute` CR. If a namespace is selected by more than one `AdminPolicyBasedExternalRoute` CR, a `failed` error status occurs on the second and subsequent CRs that target the same namespace. To apply updates, you must change the policy itself or related objects such as target namespaces, pod gateways, or namespaces hosting them from dynamic hops. The policy is then re-evaluated and your changes are applied. |
| `spec.nextHops` | `object` | Specifies the destinations where the packets are forwarded to. Must be either or both of `static` and `dynamic`. You must have at least one next hop defined. |

Show more

Expand

Table 8.2. nextHops object

| Field | Type | Description |
| --- | --- | --- |
| `static` | `array` | Specifies an array of static IP addresses. |
| `dynamic` | `array` | Specifies an array of pod selectors corresponding to pods configured with a network attachment definition to use as the external gateway target. |

Show more

Expand

Table 8.3. nextHops.static object

| Field | Type | Description |
| --- | --- | --- |
| `ip` | `string` | Specifies either an IPv4 or IPv6 address of the next destination hop. |
| `bfdEnabled` | `boolean` | Optional field. Specifies whether Bi-Directional Forwarding Detection (BFD) is supported by the network. The default value is `false`. |

Show more

Expand

Table 8.4. nextHops.dynamic object

| Field | Type | Description |
| --- | --- | --- |
| `podSelector` | `string` | Specifies a set-based label selector to filter the pods in the namespace that match this network configuration. For more information, see "Set-based requirement" in the *Additional resources* section. |
| `namespaceSelector` | `string` | Specifies a `set-based` selector to filter the namespaces that the `podSelector` applies to. You must specify a value for this field. |
| `bfdEnabled` | `boolean` | Optional field. Specifies whether Bi-Directional Forwarding Detection (BFD) is supported by the network. The default value is `false`. |
| `networkAttachmentName` | `string` | Optional field. Specifies the name of a network attachment definition. The name must match the list of logical networks associated with the pod. If this field is not specified, the host network of the pod is used. However, the pod must be configured as a host network pod to use the host network. |

Show more

### [8.5. Example secondary external gateway configurations](#example-secondary-external-gateway-configurations_configuring-secondary-external-gateway) Copy linkLink copied to clipboard!

Reference the `AdminPolicyBasedExternalRoute` objects to better understand secondary external gateway configurations.

In the following example, the `AdminPolicyBasedExternalRoute` object configures two static IP addresses as external gateways for pods in namespaces with the `kubernetes.io/metadata.name: novxlan-externalgw-ecmp-4059` label:

```
apiVersion: k8s.ovn.org/v1
kind: AdminPolicyBasedExternalRoute
metadata:
  name: default-route-policy
spec:
  from:
    namespaceSelector:
      matchLabels:
        kubernetes.io/metadata.name: novxlan-externalgw-ecmp-4059
  nextHops:
    static:
    - ip: "172.18.0.8"
    - ip: "172.18.0.9"
# ...
```

In the following example, the `AdminPolicyBasedExternalRoute` object configures a dynamic external gateway. The IP addresses used for the external gateway are derived from the additional network attachments associated with each of the selected pods.

```
apiVersion: k8s.ovn.org/v1
kind: AdminPolicyBasedExternalRoute
metadata:
  name: shadow-traffic-policy
spec:
  from:
    namespaceSelector:
      matchLabels:
        externalTraffic: ""
  nextHops:
    dynamic:
    - podSelector:
        matchLabels:
          gatewayPod: ""
      namespaceSelector:
        matchLabels:
          shadowTraffic: ""
      networkAttachmentName: shadow-gateway
    - podSelector:
        matchLabels:
          gigabyteGW: ""
      namespaceSelector:
        matchLabels:
          gatewayNamespace: ""
      networkAttachmentName: gateway
# ...
```

In the following example, the `AdminPolicyBasedExternalRoute` object configures both static and dynamic external gateways:

```
apiVersion: k8s.ovn.org/v1
kind: AdminPolicyBasedExternalRoute
metadata:
  name: multi-hop-policy
spec:
  from:
    namespaceSelector:
      matchLabels:
        trafficType: "egress"
  nextHops:
    static:
    - ip: "172.18.0.8"
    - ip: "172.18.0.9"
    dynamic:
    - podSelector:
        matchLabels:
          gatewayPod: ""
      namespaceSelector:
        matchLabels:
          egressTraffic: ""
      networkAttachmentName: gigabyte
# ...
```

### [8.6. Configure a secondary external gateway](#nw-secondary-ext-gw-configure_configuring-secondary-external-gateway) Copy linkLink copied to clipboard!

You can configure an external gateway on the default network for a namespace in your cluster.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.

**Procedure**

1. Create a YAML file that contains an `AdminPolicyBasedExternalRoute` object. For more information, see "AdminPolicyBasedExternalRoute object configuration".
2. To create an admin policy based external route, enter the following command:

   ```
   $ oc create -f <file>.yaml
   ```

   * `<file>`: Specifies the name of the YAML file that you created in a previous step.

     **Example output**

     ```
     adminpolicybasedexternalroute.k8s.ovn.org/default-route-policy created
     ```
3. To confirm that the admin policy based external route was created, enter the following command:

   ```
   $ oc describe apbexternalroute <name> | tail -n 6
   ```

   * `<name>`: Specifies the name of the `AdminPolicyBasedExternalRoute` object.

     **Example output**

     ```
     Status:
       Last Transition Time:  2023-04-24T15:09:01Z
       Messages:
       Configured external gateway IPs: 172.18.0.8
       Status:  Success
     Events:  <none>
     ```

## [Chapter 9. Configuring an egress IP address](#configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

As a cluster administrator, you can configure the OVN-Kubernetes Container Network Interface (CNI) network plugin to assign one or more egress IP addresses to a namespace, or to specific pods in a namespace.

### [9.1. Egress IP address architectural design and implementation](#nw-egress-ips-about_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

By using the OpenShift Container Platform egress IP address functionality, you can ensure that the traffic from one or more pods in one or more namespaces has a consistent source IP address for services outside the cluster network.

For example, you might have a pod that periodically queries a database that is hosted on a server outside of your cluster. To enforce access requirements for the server, a packet filtering device is configured to allow traffic only from specific IP addresses.

To ensure that you can reliably allow access to the server from only that specific pod, you can configure a specific egress IP address for the pod that makes the requests to the server.

An egress IP address assigned to a namespace is different from an egress router, which is used to send traffic to specific destinations.

In some cluster configurations, application pods and ingress router pods run on the same node. If you configure an egress IP address for an application project in this scenario, the IP address is not used when you send a request to a route from the application project.

Important

Egress IP addresses must not be configured in any Linux network configuration files, such as `ifcfg-eth0`.

Important

The assignment of egress IP addresses to control plane nodes with the EgressIP feature is not supported on a cluster provisioned on Amazon Web Services (AWS). For more information, see "BZ#2039656".

The following examples illustrate the annotation from nodes on several public cloud providers. The annotations are indented for readability.

**Example `cloud.network.openshift.io/egress-ipconfig` annotation on AWS**

```
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"eni-078d267045138e436",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ipv4":14,"ipv6":15}
  }
]
```

The following sections describe the IP address capacity for supported public cloud environments for use in your capacity calculation.

Amazon Web Services (AWS) IP address capacity limits
:   On AWS, constraints on IP address assignments depend on the instance type configured. For more information, see "IP addresses per network interface per instance type".

Google Cloud IP address capacity limits
:   On Google Cloud, the networking model implements additional node IP addresses through IP address aliasing, rather than IP address assignments. However, IP address capacity maps directly to IP aliasing capacity.

The following capacity limits exist for IP aliasing assignment:

* Per node, the maximum number of IP aliases, both IPv4 and IPv6, is 100.
* Per VPC, the maximum number of IP aliases is unspecified, but OpenShift Container Platform scalability testing reveals the maximum to be approximately 15,000.

For more information, see "Per instance" quotas and "Alias IP ranges overview".

Microsoft Azure IP address capacity limits
:   On Azure, the following capacity limits exist for IP address assignment:

    * Per NIC, the maximum number of assignable IP addresses, for both IPv4 and IPv6, is 256.
    * Per virtual network, the maximum number of assigned IP addresses cannot exceed 65,536.

For more information, see "Networking limits".

#### [9.1.1. Platform support](#nw-egress-ips-platform-support_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

The Egress IP address feature that runs on a primary host network is supported on specific platforms.

The following table shows supported platforms for egress IP on primary host networks:

Expand

| Platform | Supported |
| --- | --- |
| Bare metal | Yes |
| VMware vSphere | Yes |
| Red Hat OpenStack Platform (RHOSP) | Yes |
| Amazon Web Services (AWS) | Yes |
| Google Cloud | Yes |
| Microsoft Azure | Yes |
| IBM Z® and IBM® LinuxONE | Yes |
| IBM Z® and IBM® LinuxONE for Red Hat Enterprise Linux (RHEL) KVM | Yes |
| IBM Power® | Yes |
| Nutanix | Yes |

Show more

Important

Support for egress IP addresses in Microsoft Azure is restricted to the infra subnet. As a workaround for this limitation, you can use a Network Address Translation (NAT) gateway instead of a general purpose public load balancer.

The Egress IP address feature that runs on secondary host networks is supported on the following platform:

Expand

| Platform | Supported |
| --- | --- |
| Bare metal | Yes |

Show more

#### [9.1.2. Public cloud platform considerations](#nw-egress-ips-public-cloud-platform-considerations_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

Typically, public cloud providers place a limit on egress IP addresses. You must understand the existence of a constraint on the absolute number of assignable IP addresses per node for clusters provisioned on public cloud infrastructure.

The maximum number of assignable IP addresses per node, or the *IP capacity*, can be described in the following formula:

```
IP capacity = public cloud default capacity - sum(current IP assignments)
```

While the Egress IP addresses capability manages the IP address capacity per node, ensure you plan for this constraint in your deployments. For example, if a public cloud provider limits IP address capacity to 10 IP addresses per node, and you have 8 nodes, the total number of assignable IP addresses is only 80. To achieve a higher IP address capacity, you would need to allocate additional nodes. For example, if you needed 150 assignable IP addresses, you would need to allocate 7 additional nodes.

To confirm the IP capacity and subnets for any node in your public cloud environment, you can enter the `oc get node <node_name> -o yaml` command. The `cloud.network.openshift.io/egress-ipconfig` annotation includes capacity and subnet information for the node.

The annotation value is an array with a single object with fields that provide the following information for the primary network interface:

* `interface`: Specifies the interface ID on AWS and Azure and the interface name on Google Cloud.
* `ifaddr`: Specifies the subnet mask for one or both IP address families.
* `capacity`: Specifies the IP address capacity for the node. On AWS, the IP address capacity is provided per IP address family. On Azure and Google Cloud, the IP address capacity includes both IPv4 and IPv6 addresses.

Automatic attachment and detachment of egress IP addresses for traffic between nodes are available. Traffic from many pods in namespaces can have a consistent source IP address to locations outside of the cluster.

Note

When an RHOSP cluster administrator assigns a floating IP to the reservation port, OpenShift Container Platform cannot delete the reservation port. The `CloudPrivateIPConfig` object cannot perform delete and move operations until an RHOSP cluster administrator unassigns the floating IP from the reservation port.

The following examples illustrate the annotation from nodes on several public cloud providers. The annotations are indented for readability.

**Example `cloud.network.openshift.io/egress-ipconfig` annotation on AWS**

```
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"eni-078d267045138e436",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ipv4":14,"ipv6":15}
  }
]
```

**Example `cloud.network.openshift.io/egress-ipconfig` annotation on Google Cloud**

```
cloud.network.openshift.io/egress-ipconfig: [
  {
    "interface":"nic0",
    "ifaddr":{"ipv4":"10.0.128.0/18"},
    "capacity":{"ip":14}
  }
]
```

#### [9.1.3. Considerations for using an egress IP address on additional network interfaces](#nw-egress-ips-multi-nic-considerations_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

In OpenShift Container Platform, egress IP addresses provide administrators a way to control network traffic. You can use egress IP addresses with a `br-ex` Open vSwitch (OVS) bridge interface. You can also use any physical interface that has IP connectivity enabled.

You can inspect your network interface type by running the following command:

```
$ ip -details link show
```

The primary network interface is assigned a node IP address which also contains a subnet mask. You can retrieve this node IP address information from the Kubnernetes node object. Inspect the `k8s.ovn.org/node-primary-ifaddr` annotation for each node in your cluster. In an IPv4 cluster, this annotation is similar to the following example: `"k8s.ovn.org/node-primary-ifaddr: {"ipv4":"192.168.111.23/24"}"`.

If the egress IP address is not within the subnet of the primary network interface subnet, use another Linux network interface. This interface must not be of the primary network interface type. With this approach, an administrator can provide a greater level of control over networking aspects such as routing, addressing, segmentation, and security policies. With this feature, you can route workload traffic over specific network interfaces for purposes such as traffic segmentation or meeting specialized requirements.

If the egress IP address is not within the subnet of the primary network interface, then the selection of another network interface for egress traffic might occur if they are present on a node.

You can determine which other network interfaces might support egress IP address addresses by inspecting the `k8s.ovn.org/host-cidrs` Kubernetes node annotation. This annotation contains the addresses and subnet mask found for the primary network interface. The annotation also contains additional network interface addresses and subnet mask information. These addresses and subnet masks are assigned to network interfaces that use the longest prefix match routing mechanism to determine which network interface supports the egress IP address. For more information, see "Longest prefix match routing" in the *Additional resources* section.

Note

By using OVN-Kubernetes, you can control how outbound traffic leaves the cluster. You can configure traffic from specific namespaces or pods to exit through a chosen network interface and use a designated egress IP address. This configuration routes application traffic over specific network paths, providing better network isolation and traffic management.

As an administrator who wants an egress IP address and traffic to route over a particular interface that is not the primary network interface, you must meet the following conditions:

* OpenShift Container Platform is installed on a bare-metal cluster. This feature is disabled within a cloud or a hypervisor environment.
* Your OpenShift Container Platform pods are not configured as *host-networked*.
* You understand that if a network interface is removed or if the IP address and subnet mask which allows the egress IP address to be hosted on the interface is removed, reconfiguration of the egress IP address occurs. Consequently, the egress IP address might get assigned to another node and interface.
* You configured a NIC with routes by ensuring a gateway exists in the main routing table. As a postinstallation task, Red Hat does not support configuring a NIC on a cluster that uses OVN-Kubernetes.
* Routes associated with an egress interface get copied from the main routing table to the routing table that was created to support the Egress IP object.
* You can use an Egress IP address on a secondary network interface card (NIC). However, you must use the Node Tuning Operator to enable IP forwarding on the secondary NIC.

  Important

  Red Hat does not support EgressIP multi-NIC configurations when the target network interface is bound to a VRF instance.

#### [9.1.4. Architectural diagram of an egress IP address configuration](#nw-egress-ips-node-architecture_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

To better understand egress IP address configuration, reference the architectural diagram.

The following diagram shows an egress IP address configuration. The diagram describes four pods in two different namespaces running on three nodes in a cluster. The nodes are assigned IP addresses from the `192.168.126.0/18` CIDR block on the host network.

Both Node 1 and Node 3 are labeled with `k8s.ovn.org/egress-assignable: ""` and thus available for the assignment of egress IP addresses.

The dashed lines in the diagram depict the traffic flow from pod1, pod2, and pod3 traveling through the pod network to egress the cluster from Node 1 and Node 3. When an external service receives traffic from any of the pods selected by the example `EgressIP` object, the source IP address is either `192.168.126.10` or `192.168.126.102`. The traffic is balanced roughly equally between these two nodes.

Based on the diagram, the following manifest file defines namespaces:

**Namespace objects**

```
apiVersion: v1
kind: Namespace
metadata:
  name: namespace1
  labels:
    env: prod
---
apiVersion: v1
kind: Namespace
metadata:
  name: namespace2
  labels:
    env: prod
```

Based on the diagram, the following `EgressIP` object describes a configuration that selects all pods in any namespace with the `env` label set to `prod`. The egress IP addresses for the selected pods are `192.168.126.10` and `192.168.126.102`.

**`EgressIP` object**

```
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egressips-prod
spec:
  egressIPs:
  - 192.168.126.10
  - 192.168.126.102
  namespaceSelector:
    matchLabels:
      env: prod
status:
  items:
  - node: node1
    egressIP: 192.168.126.10
  - node: node3
    egressIP: 192.168.126.102
```

For the configuration in the previous example, OpenShift Container Platform assigns both egress IP addresses to the available nodes. The `status` field reflects whether and where the egress IP addresses are assigned.

### [9.2. EgressIP object](#nw-egress-ips-object_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

You can view YAML files to better understand how you can effectively configure an `EgressIP` object to better meet your needs.

When the `EgressIP` namespace selector matches the label on multiple namespaces, consider the following behaviors:

* All traffic for selected pods must pass through a single node. During times of high traffic, the network interface of the node might experience performance issues.
* An error in a label selector might change the outbound IP address for many cluster namespaces.
* Only a cluster administrator can create or change cluster-scoped objects.
* Packets must move from a pod that exists in a node to the named host node that is referenced in the `EgressIP` object. This approach adds a network hop.

Important

Do not create egress rules, such as a single label selector, that forces all namespaces that exist in a cluster to use the same outbound IP address. This configuration can cause the node that hosts the IP address to crash during times of high network traffic.

The following YAML describes the API for the `EgressIP` object. The scope of the object is cluster-wide and is not created in a namespace.

```
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: <name>
spec:
  egressIPs:
  - <ip_address>
  namespaceSelector:
    ...
  podSelector:
    ...
```

where:

`<name>`
:   Specifies the name for the `EgressIPs` object.

`<egressIPs>`
:   Specifies an array of one or more IP addresses.

`<namespaceSelector>`
:   Specifies one or more selectors for the namespaces to associate the egress IP addresses with.

`<podSelector>`
:   Optional parameter. Specifies one or more selectors for pods in the specified namespaces to associate egress IP addresses with. Applying these selectors allows for the selection of a subset of pods within a namespace.

The following YAML describes the stanza for the namespace selector:

**Namespace selector stanza**

```
namespaceSelector:
  matchLabels:
    <label_name>: <label_value>
```

where:

`<namespaceSelector>`
:   Specifies one or more matching rules for namespaces. If more than one match rule is provided, all matching namespaces are selected.

The following YAML describes the optional stanza for the pod selector:

**Pod selector stanza**

```
podSelector:
  matchLabels:
    <label_name>: <label_value>
```

where:

`<podSelector>`
:   Optional parameter. Specifies one or more matching rules for pods in the namespaces that match the specified `namespaceSelector` rules. If specified, only pods that match are selected. Others pods in the namespace are not selected.

In the following example, the `EgressIP` object associates the `192.168.126.11` and `192.168.126.102` egress IP addresses with pods that have the `app` label set to `web` and are in the namespaces that have the `env` label set to `prod`:

**Example `EgressIP` object**

```
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egress-group1
spec:
  egressIPs:
  - 192.168.126.11
  - 192.168.126.102
  podSelector:
    matchLabels:
      app: web
  namespaceSelector:
    matchLabels:
      env: prod
```

In the following example, the `EgressIP` object associates the `192.168.127.30` and `192.168.127.40` egress IP addresses with any pods that do not have the `environment` label set to `development`:

**Example `EgressIP` object**

```
apiVersion: k8s.ovn.org/v1
kind: EgressIP
metadata:
  name: egress-group2
spec:
  egressIPs:
  - 192.168.127.30
  - 192.168.127.40
  namespaceSelector:
    matchExpressions:
    - key: environment
      operator: NotIn
      values:
      - development
```

### [9.3. Assignment of egress IPs to a namespace, nodes, and pods](#nw-egress-ips-considerations_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

To assign one or more egress IPs to a namespace or specific pods in a namespace, you must meet specific conditions.

* At least one node in your cluster must have the `k8s.ovn.org/egress-assignable: ""` label.
* An `EgressIP` object exists that defines one or more egress IP addresses to use as the source IP address for traffic leaving the cluster from pods in a namespace.

Important

If you create `EgressIP` objects prior to labeling any nodes in your cluster for egress IP assignment, OpenShift Container Platform might assign every egress IP address to the first node with the `k8s.ovn.org/egress-assignable: ""` label.

To ensure that egress IP addresses are widely distributed across nodes in the cluster, always apply the label to the nodes you intend to host the egress IP addresses before creating any `EgressIP` objects.

When creating an `EgressIP` object, the following conditions apply to nodes that are labeled with the `k8s.ovn.org/egress-assignable: ""` label:

* An egress IP address is never assigned to more than one node at a time.
* An egress IP address is equally balanced between available nodes that can host the egress IP address.
* If the `spec.EgressIPs` array in an `EgressIP` object specifies more than one IP address, the following conditions apply:

  + No node will ever host more than one of the specified IP addresses.
  + Traffic is balanced roughly equally between the specified IP addresses for a given namespace.
* If a node becomes unavailable, any egress IP addresses assigned to it are automatically reassigned, subject to the previously described conditions.

Important

If the number of nodes labeled with `k8s.ovn.org/egress-assignable` is less than the number of egress IP addresses specified in the `EgressIP` object, the additional egress IP addresses remain unassigned. To ensure all specified egress IP addresses are active and traffic is balanced as expected, verify that the number of egress-assignable nodes is equal to or greater than the number of egress IP addresses defined in the `EgressIP` object.

When a pod matches the selector for multiple `EgressIP` objects, there is no guarantee which of the egress IP addresses that are specified in the `EgressIP` objects is assigned as the egress IP address for the pod.

Additionally, if an `EgressIP` object specifies multiple egress IP addresses, there is no guarantee which of the egress IP addresses might be used. For example, if a pod matches a selector for an `EgressIP` object with two egress IP addresses, `10.10.20.1` and `10.10.20.2`, either might be used for each TCP connection or UDP conversation.

### [9.4. Assigning an egress IP address to a namespace](#nw-egress-ips-assign_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

You can assign one or more egress IP addresses to a namespace or to specific pods in a namespace.

**Prerequisites**

* The OpenShift CLI (`oc`) is installed.
* You are logged in to the cluster as a cluster administrator.
* At least one node is configured to host an egress IP address.

**Procedure**

1. Create an `EgressIP` object.

   1. Create a `<egressips_name>.yaml` file where `<egressips_name>` is the name of the object.
   2. In the file that you created, define an `EgressIP` object, as in the following example:

      ```
      apiVersion: k8s.ovn.org/v1
      kind: EgressIP
      metadata:
        name: egress-project1
      spec:
        egressIPs:
        - 192.168.127.10
        - 192.168.127.11
        namespaceSelector:
          matchLabels:
            env: qa
      # ...
      ```
2. To create the object, enter the following command.

   ```
   $ oc apply -f <egressips_name>.yaml
   ```

   where:

   `<egressips_name>`
   :   Replace `<egressips_name>` with the name of the object.

   **Example output**

   ```
   egressips.k8s.ovn.org/<egressips_name> created
   ```
3. Optional: Store the `<egressips_name>.yaml` file so that you can make changes later.
4. Add labels to the namespace that requires egress IP addresses. To add a label to the namespace of an `EgressIP` object defined in a previous step, run the following command:

   ```
   $ oc label ns <namespace> env=qa
   ```

   where:

   `<namespace>`
   :   Replace `<namespace>` with the namespace that requires egress IP addresses.

**Verification**

* To show all egress IP addresses that are in use in your cluster, enter the following command:

  ```
  $ oc get egressip -o yaml
  ```

  Note

  The command `oc get egressip` only returns one egress IP address regardless of how many are configured. This is not a bug and is a limitation of Kubernetes. As a workaround, you can pass in the `-o yaml` or `-o json` flags to return all egress IPs addresses in use.

  **Example output**

  ```
  # ...
  spec:
    egressIPs:
    - 192.168.127.10
    - 192.168.127.11
  # ...
  ```

### [9.5. Understanding EgressIP failover control](#egressip_failover_concept_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

The `reachabilityTotalTimeoutSeconds` parameter controls how quickly the system detects a failing `egressIP` node and initiates a failover. This parameter directly determines the maximum time the platform waits before declaring a node unreachable.

Important

When you configure `egressIP` with multiple egress nodes, the complete failover time from node failure to recovery on a new node is expected to be on the order of seconds or longer. This is because the new IP assignment can only begin after the `reachabilityTotalTimeoutSeconds` period has fully elapsed without a successful check.

To ensure traffic uses the correct external path, `egressIP` traffic on a node will always egress through the network interface on which the `egressIP` address has been assigned.

#### [9.5.1. Configuring the EgressIP failover time limit](#egressip_configure_failover_task_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

You can configure the `reachabilityTotalTimeoutSeconds` parameter to control how quickly the system detects a failing `egressIP` node and initiates a failover.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You logged in to the cluster as a cluster administrator.

**Procedure**

1. Edit the `Network` custom resource by running the following command:

   ```
   $ oc edit network.operator cluster
   ```
2. Navigate to the `egressIPConfig: {}` section under `spec:defaultNetwork:ovnKubernetesConfig:`
3. Modify the block to include the `reachabilityTotalTimeoutSeconds` parameter with your chosen value, 5 seconds for example. Make sure to use the correct indentation:

   ```
     defaultNetwork:
       ovnKubernetesConfig:
         egressIPConfig:
           reachabilityTotalTimeoutSeconds: 5
   ```

   Note

   The value must be an integer between 0 and 60. For details on possible values, see the "EgressIP failover settings" section.
4. Save and exit the editor. The operator automatically applies the changes.

**Verification**

1. Verify that the system correctly accepted the `reachabilityTotalTimeoutSeconds` parameter by running the following command:

   ```
   $ oc get network.operator cluster -o yaml
   ```
2. Inspect the output and confirm that the `reachabilityTotalTimeoutSeconds` parameter is correctly nested under `spec:defaultNetwork:ovnKubernetesConfig:egressIPConfig:` with your intended value:

   ```
    # ...
     spec:
       # ...
       defaultNetwork:
         ovnKubernetesConfig:
           egressIPConfig:
             reachabilityTotalTimeoutSeconds: 5
           gatewayConfig:
     # ...
   ```

#### [9.5.2. EgressIP failover settings](#egressip_failover_reference_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

The `reachabilityTotalTimeoutSeconds` parameter defines the total time limit in seconds for the platform health check process before a node is declared down.

The following table summarizes the acceptable values and their implications:

Expand

| Parameter Value (Seconds) | Effect on reachability check | Failover impact and use case |
| --- | --- | --- |
| `0` | Disables the reachability check. | No automatic failover: Use only if an external system handles node health monitoring and failover. The platform will not automatically react to node failures. |
| `1 - 60` | Sets the total time limit for reachability probing. | Directly controls detection time: This value defines the lower limit for your overall failover time. A smaller value leads to faster failover but might increase network traffic. Default: 1 second. The maximum accepted integer value is 60. |

Show more

### [9.6. Labeling a node to host egress IP addresses](#nw-egress-ips-node_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

You can apply the `k8s.ovn.org/egress-assignable=""` label to a node in your cluster so that OpenShift Container Platform can assign one or more egress IP addresses to the node.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You logged in to the cluster as a cluster administrator.

**Procedure**

* To label a node so that it can host one or more egress IP addresses, enter the following command:

  ```
  $ oc label nodes <node_name> k8s.ovn.org/egress-assignable=""
  ```

  `<node_name>`
  :   Specifies the name of the node to label.

      Tip

      You can alternatively apply the following YAML to add the label to a node:

      ```
      apiVersion: v1
      kind: Node
      metadata:
        labels:
          k8s.ovn.org/egress-assignable: ""
        name: <node_name>
      ```

### [9.7. Configuring dual-stack networking for an EgressIP object](#nw-egress-ips-object-dual-stack_configuring-egress-ips-ovn) Copy linkLink copied to clipboard!

For a cluster configured for dual-stack networking, you can apply dual-stack networking to a single `EgressIP` object. The `EgressIP` object can then extend dual-stack networking capabilities to a pod.

Important

Red Hat does not support creating two `EgressIP` objects to represent dual-stack networking capabilities. For example, specifying IPv4 addresses with one object and using another object to specify IPv6 addresses. This configuration limit impacts address-type assignments to pods.

**Prerequisites**

* You created two egress nodes so that an `EgressIP` object can allocate IPv4 addresses to one node and IPv6 addresses to the other node. For more information, see "Assignment of egress IP addresses to nodes".

**Procedure**

* Create an `EgressIP` object and configure IPv4 and IPv6 addresses for the object. The following example `EgressIP` object uses selectors to identify which pods use the specified egress IP addresses for their outbound traffic:

  ```
  kind: EgressIP
  metadata:
    name: egressip-dual
  spec:
    egressIPs:
      - 192.168.118.30
      - 2600:52:7:94::30
    namespaceSelector:
      matchLabels:
        env: qa
    podSelector:
      matchLabels:
        egressip: ds
  # ...
  ```

**Verification**

1. Create a `Pod` manifest file to test and validate your `EgressIP` object. The pod serves as a client workload that sends outbound traffic to verify that your `EgressIP` policy works as expected.

   ```
   apiVersion: v1
   kind: Pod
   metadata:
     name: ubi-egressip-pod
     namespace: test
     labels:
       egressip: ds
   spec:
     containers:
     - name: fedora-curl
       image: registry.redhat.io/ubi9/ubi
       command: ["/bin/bash", "-c", "sleep infinity"]
   # ...
   ```

   where:

   `<labels>`
   :   Sets custom identifiers so that the `EgressIP` object can use these labels to apply egress IP address to target pods.
2. Run a `curl` request from inside a pod to an external server. This action verifies that outbound traffic correctly uses an address that you specified in the `EgressIP` object.

   ```
   $ curl <ipv_address>
   ```

   where:

   `<ipv_address>`
   :   Depending on the `EgressIP` object, enter an IPv4 or IPv6 address.

## [Chapter 10. Configuring an egress service](#configuring-egress-traffic-loadbalancer-services) Copy linkLink copied to clipboard!

As a cluster administrator, you can configure egress traffic for pods behind a load balancer service by using an egress service.

Important

Egress service is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

You can use the `EgressService` custom resource (CR) to manage egress traffic in the following ways:

* Assign a load balancer service IP address as the source IP address for egress traffic for pods behind the load balancer service.

  Assigning the load balancer IP address as the source IP address in this context is useful to present a single point of egress and ingress. For example, in some scenarios, an external system communicating with an application behind a load balancer service can expect the source and destination IP address for the application to be the same.

  Note

  When you assign the load balancer service IP address to egress traffic for pods behind the service, OVN-Kubernetes restricts the ingress and egress point to a single node. This limits the load balancing of traffic that MetalLB typically provides.
* Assign the egress traffic for pods behind a load balancer to a different network than the default node network.

  This is useful to assign the egress traffic for applications behind a load balancer to a different network than the default network. Typically, the different network is implemented by using a VRF instance associated with a network interface.

### [10.1. Egress service custom resource](#nw-egress-service-ovn-cr_configuring-egress-traffic-loadbalancer-services) Copy linkLink copied to clipboard!

You can define the configuration for an egress service in an `EgressService` custom resource.

The following YAML describes the fields for the configuration of an egress service:

```
apiVersion: k8s.ovn.org/v1
kind: EgressService
metadata:
  name: <egress_service_name>
  namespace: <namespace>
spec:
  sourceIPBy: <egress_traffic_ip>
  nodeSelector:
    matchLabels:
      node-role.kubernetes.io/<role>: ""
  network: <egress_traffic_network>
```

where:

`metadata.name`
:   Specifies the name for the egress service. The name of the `EgressService` resource must match the name of the load-balancer service that you want to modify.

`metadata.namespace`
:   Specifies the namespace for the egress service. The namespace for the `EgressService` must match the namespace of the load-balancer service that you want to modify. The egress service is namespace-scoped.

`spec.sourceIPBy`
:   Specifies the source IP address of egress traffic for pods behind a service. Valid values are `LoadBalancerIP` or `Network`. Use the `LoadBalancerIP` value to assign the `LoadBalancer` service ingress IP address as the source IP address for egress traffic. Specify `Network` to assign the network interface IP address as the source IP address for egress traffic.

`spec.nodeSelector`
:   Optional parameter. If you use the `LoadBalancerIP` value for the `sourceIPBy` specification, a single node handles the `LoadBalancer` service traffic. Use the `nodeSelector` field to limit which node can be assigned this task. When a node is selected to handle the service traffic, OVN-Kubernetes labels the node in the following format: `egress-service.k8s.ovn.org/<svc-namespace>-<svc-name>: ""`. When the `nodeSelector` field is not specified, any node can manage the `LoadBalancer` service traffic.

`spec.network`
:   Optional parameter. Specifies the routing table ID for egress traffic. Ensure that the value matches the `route-table-id` ID defined in the `NodeNetworkConfigurationPolicy` resource. If you do not include the `network` specification, the egress service uses the default host network.

**Example egress service specification**

```
apiVersion: k8s.ovn.org/v1
kind: EgressService
metadata:
  name: test-egress-service
  namespace: test-namespace
spec:
  sourceIPBy: "LoadBalancerIP"
  nodeSelector:
    matchLabels:
      vrf: "true"
  network: "2"
```

### [10.2. Deploying an egress service](#nw-egress-service-ovn_configuring-egress-traffic-loadbalancer-services) Copy linkLink copied to clipboard!

You can deploy an egress service to manage egress traffic for pods behind a `LoadBalancer` service.

The following example configures the egress traffic to have the same source IP address as the ingress IP address of the `LoadBalancer` service.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in as a user with `cluster-admin` privileges.
* You configured MetalLB `BGPPeer` resources.

**Procedure**

1. Create an `IPAddressPool` CR with the desired IP for the service:

   1. Create a file, such as `ip-addr-pool.yaml`, with content like the following example:

      ```
      apiVersion: metallb.io/v1beta1
      kind: IPAddressPool
      metadata:
        name: example-pool
        namespace: metallb-system
      spec:
        addresses:
        - 172.19.0.100/32
      ```
   2. Apply the configuration for the IP address pool by running the following command:

      ```
      $ oc apply -f ip-addr-pool.yaml
      ```
2. Create `Service` and `EgressService` CRs:

   1. Create a file, such as `service-egress-service.yaml`, with content like the following example:

      ```
      apiVersion: v1
      kind: Service
      metadata:
        name: example-service
        namespace: example-namespace
        annotations:
          metallb.io/address-pool: example-pool
      spec:
        selector:
          app: example
        ports:
          - name: http
            protocol: TCP
            port: 8080
            targetPort: 8080
        type: LoadBalancer
      ---
      apiVersion: k8s.ovn.org/v1
      kind: EgressService
      metadata:
        name: example-service
        namespace: example-namespace
      spec:
        sourceIPBy: "LoadBalancerIP"
        nodeSelector:
          matchLabels:
            node-role.kubernetes.io/worker: ""
      ```

      where:

      `metadata.annotations.metallb.io/address-pool`
      :   Specifies the `LoadBalancer` service uses the IP address assigned by MetalLB from the `example-pool` IP address pool.

      `spec.sourceIPBy`
      :   This example uses the `LoadBalancerIP` value to assign the ingress IP address of the `LoadBalancer` service as the source IP address of egress traffic.

      `spec.nodeSelector`
      :   When you specify the `LoadBalancerIP` value, a single node handles the `LoadBalancer` service’s traffic. In this example, only nodes with the `worker` label can be selected to handle the traffic. When a node is selected, OVN-Kubernetes labels the node in the following format `egress-service.k8s.ovn.org/<svc-namespace>-<svc-name>: ""`.

          Note

          If you use the `sourceIPBy: "LoadBalancerIP"` setting, you must specify the load-balancer node in the `BGPAdvertisement` custom resource (CR).
   2. Apply the configuration for the service and egress service by running the following command:

      ```
      $ oc apply -f service-egress-service.yaml
      ```
3. Create a `BGPAdvertisement` CR to advertise the service:

   1. Create a file, such as `service-bgp-advertisement.yaml`, with content like the following example:

      ```
      apiVersion: metallb.io/v1beta1
      kind: BGPAdvertisement
      metadata:
        name: example-bgp-adv
        namespace: metallb-system
      spec:
        ipAddressPools:
        - example-pool
        nodeSelectors:
        - matchLabels:
            egress-service.k8s.ovn.org/example-namespace-example-service: ""
      ```

      where:

      `spec.nodeSelectors.matchLabels`
      :   In the example, the `EgressService` CR configures the source IP address for egress traffic to use the load-balancer service IP address. Therefore, you must specify the load-balancer node for return traffic to use the same return path for the traffic originating from the pod.

**Verification**

1. Verify that you can access the application endpoint of the pods running behind the MetalLB service by running the following command:

   ```
   $ curl <external_ip_address>:<port_number>
   ```

   `<external_ip_address>:<port_number`
   :   Update the external IP address and port number to suit your application endpoint.
2. If you assigned the `LoadBalancer` service’s ingress IP address as the source IP address for egress traffic, verify this configuration by using tools such as `tcpdump` to analyze packets received at the external client.

## [Chapter 11. Considerations for the use of an egress router pod](#using-an-egress-router-ovn) Copy linkLink copied to clipboard!

Before you use the egress router pod, you must understand how the pod works. Doing so can prevent situations such as creating large numbers of egress router pods that exceed the limits of your network hardware.

### [11.1. About an egress router pod](#nw-egress-router-about_using-an-egress-router-ovn) Copy linkLink copied to clipboard!

The OpenShift Container Platform egress router pod redirects traffic to a specified remote server from a private source IP address that is not used for any other purpose. An egress router pod can send network traffic to servers that are set up to allow access only from specific IP addresses.

Note

The egress router pod is not intended for every outgoing connection. Creating large numbers of egress router pods can exceed the limits of your network hardware. For example, creating an egress router pod for every project or application could exceed the number of local MAC addresses that the network interface can handle before reverting to filtering MAC addresses in software.

Important

The egress router image is not compatible with Amazon Web Services (AWS), Microsoft Azure, or any other cloud platform that does not support layer 2 manipulations due to their incompatibility with macvlan traffic.

#### [11.1.1. Egress router modes](#nw-egress-router-about-modes_using-an-egress-router-ovn) Copy linkLink copied to clipboard!

In *redirect mode*, an egress router pod configures `iptables` rules to redirect traffic from its own IP address to one or more destination IP addresses. Client pods that need to use the reserved source IP address must be configured to access the service for the egress router rather than connecting directly to the destination IP. You can access the destination service and port from the application pod by using the `curl` command. For example:

```
$ curl <router_service_IP> <port>
```

Note

The egress router CNI plugin supports redirect mode only. The egress router CNI plugin does not support HTTP proxy mode or DNS proxy mode.

#### [11.1.2. Egress router pod implementation](#nw-egress-router-about-router-pod-implementation_using-an-egress-router-ovn) Copy linkLink copied to clipboard!

The egress router implementation uses the egress router Container Network Interface (CNI) plugin. The plugin adds a secondary network interface to a pod.

An egress router is a pod that has two network interfaces. For example, the pod can have `eth0` and `net1` network interfaces. The `eth0` interface is on the cluster network and the pod continues to use the interface for ordinary cluster-related network traffic. The `net1` interface is on a secondary network and has an IP address and gateway for that network. Other pods in the OpenShift Container Platform cluster can access the egress router service and the service enables the pods to access external services. The egress router acts as a bridge between pods and an external system.

Traffic that leaves the egress router exits through a node, but the packets have the MAC address of the `net1` interface from the egress router pod.

When you add an egress router custom resource, the Cluster Network Operator creates the following objects:

* The network attachment definition for the `net1` secondary network interface of the pod.
* A deployment for the egress router.

If you delete an egress router custom resource, the Operator deletes the two objects in the preceding list that are associated with the egress router.

#### [11.1.3. Deployment considerations](#nw-egress-router-about-deployments_using-an-egress-router-ovn) Copy linkLink copied to clipboard!

An egress router pod adds an additional IP address and MAC address to the primary network interface of the node. As a result, you might need to configure your hypervisor or cloud provider to allow the additional address.

Red Hat OpenStack Platform (RHOSP)
:   If you deploy OpenShift Container Platform on RHOSP, you must allow traffic from the IP and MAC addresses of the egress router pod on your OpenStack environment. If you do not allow the traffic, see "OpenShift on OpenStack: Egress router not working" Knowledgebase article in the *Additional resources* section.

    ```
    $ openstack port set --allowed-address \
      ip_address=<ip_address>,mac_address=<mac_address> <neutron_port_uuid>
    ```

VMware vSphere
:   If you are using VMware vSphere, see the VMware documentation for securing vSphere standard switches. View and change VMware vSphere default settings by selecting the host virtual switch from the vSphere Web Client. Specifically, ensure that you enable the following components:

    * MAC address changes
    * Forged transits
    * Promiscuous Mode Operation

For more information on these components, see the *Additional resources* section.

#### [11.1.4. Failover configuration](#nw-egress-router-about-failover_using-an-egress-router-ovn) Copy linkLink copied to clipboard!

To avoid downtime, the Cluster Network Operator deploys the egress router pod as a deployment resource. The deployment name is `egress-router-cni-deployment`. The pod that corresponds to the deployment has a label of `app=egress-router-cni`.

To create a new service for the deployment, use the `oc expose deployment/egress-router-cni-deployment --port <port_number>` command or create a file like the following example:

```
apiVersion: v1
kind: Service
metadata:
  name: app-egress
spec:
  ports:
  - name: tcp-8080
    protocol: TCP
    port: 8080
  - name: tcp-8443
    protocol: TCP
    port: 8443
  - name: udp-80
    protocol: UDP
    port: 80
  type: ClusterIP
  selector:
    app: egress-router-cni
```

## [Chapter 12. Deploying an egress router pod in redirect mode](#deploying-egress-router-ovn-redirection) Copy linkLink copied to clipboard!

As a cluster administrator, you can deploy an egress router pod to redirect traffic to specified destination IP addresses from a reserved source IP address.

The egress router implementation uses the egress router Container Network Interface (CNI) plugin.

### [12.1. Egress router custom resource](#nw-egress-router-ovn-cr_deploying-egress-router-ovn-redirection) Copy linkLink copied to clipboard!

You can define the configuration for an egress router pod in an egress router custom resource.

The following YAML describes the fields for the configuration of an egress router in redirect mode:

```
apiVersion: network.operator.openshift.io/v1
kind: EgressRouter
metadata:
  name: <egress_router_name>
  namespace: <namespace>
spec:
  addresses: [
    {
      ip: "<egress_router>",
      gateway: "<egress_gateway>"
    }
  ]
  mode: Redirect
  redirect: {
    redirectRules: [
      {
        destinationIP: "<egress_destination>",
        port: <egress_router_port>,
        targetPort: <target_port>,
        protocol: <network_protocol>
      },
      ...
    ],
    fallbackIP: "<egress_destination>"
  }
```

where:

`metadata.namespace`
:   Optional parameter. Specifies the `namespace` for creating the egress router. If you do not specify a value in the file or on the command line, the `default` namespace is used.

`spec.addresses`
:   Specifies the IP addresses to configure on the secondary network interface.

`spec.addresses.ip`
:   Specifies the reserve source IP address and netmask from the physical network that the node is on to use with egress router pod. Use CIDR notation to specify the IP address and netmask.

`spec.addresses.gateway`
:   Specifies the IP address of the network gateway.

`spec.redirect.redirectRules`
:   Optional parameter. Specifies the combinination of egress destination IP address, egress router port, and protocol. Incoming connections to the egress router on the specified port and protocol are routed to the destination IP address.

`spec.redirect.redirectRules.targetPort`
:   Optional parameter. Specifies the network port on the destination IP address. If this field is not specified, traffic is routed to the same network port that it arrived on.

`spec.redirect.redirectRules.protocol`
:   Specifies the protocols to support, such as TCP, UDP, or SCTP.

`spec.redirect.fallbackIP`
:   Optional parameter. Specifies a destination IP address. If you do not specify any redirect rules, the egress router sends all traffic to this fallback IP address. If you specify redirect rules, any connections to network ports that are not defined in the rules are sent by the egress router to this fallback IP address. If you do not specify this field, the egress router rejects connections to network ports that are not defined in the rules.

**Example egress router specification**

```
apiVersion: network.operator.openshift.io/v1
kind: EgressRouter
metadata:
  name: egress-router-redirect
spec:
  networkInterface: {
    macvlan: {
      mode: "Bridge"
    }
  }
  addresses: [
    {
      ip: "192.168.12.99/24",
      gateway: "192.168.12.1"
    }
  ]
  mode: Redirect
  redirect: {
    redirectRules: [
      {
        destinationIP: "10.0.0.99",
        port: 80,
        protocol: UDP
      },
      {
        destinationIP: "203.0.113.26",
        port: 8080,
        targetPort: 80,
        protocol: TCP
      },
      {
        destinationIP: "203.0.113.27",
        port: 8443,
        targetPort: 443,
        protocol: TCP
      }
    ]
  }
```

### [12.2. Deploying an egress router in redirect mode](#nw-egress-router-redirect-mode-ovn_deploying-egress-router-ovn-redirection) Copy linkLink copied to clipboard!

You can deploy an egress router to redirect traffic from its own reserved source IP address to one or more destination IP addresses.

After you add an egress router, the client pods that need to use the reserved source IP address must be modified to connect to the egress router rather than connecting directly to the destination IP.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You logged in as a user with `cluster-admin` privileges.

**Procedure**

1. Create an egress router definition.
2. To ensure that other pods can find the IP address of the egress router pod, create a service that uses the egress router, as in the following example:

   ```
   apiVersion: v1
   kind: Service
   metadata:
     name: egress-1
   spec:
     ports:
     - name: web-app
       protocol: TCP
       port: 8080
     type: ClusterIP
     selector:
       app: egress-router-cni
   ```

   `spec.selector`: Specifies the label for the egress router. The value shown is added by the Cluster Network Operator and is not configurable.

   After you create the service, your pods can connect to the service. The egress router pod redirects traffic to the corresponding port on the destination IP address. The connections originate from the reserved source IP address.

**Verification**

1. View the network attachment definition that the Operator created for the egress router:

   ```
   $ oc get network-attachment-definition egress-router-cni-nad
   ```

   The name of the network attachment definition is not configurable.

   **Example output**

   ```
   NAME                    AGE
   egress-router-cni-nad   18m
   ```
2. View the deployment for the egress router pod:

   ```
   $ oc get deployment egress-router-cni-deployment
   ```

   The name of the deployment is not configurable.

   **Example output**

   ```
   NAME                           READY   UP-TO-DATE   AVAILABLE   AGE
   egress-router-cni-deployment   1/1     1            1           18m
   ```
3. View the status of the egress router pod:

   ```
   $ oc get pods -l app=egress-router-cni
   ```

   **Example output**

   ```
   NAME                                            READY   STATUS    RESTARTS   AGE
   egress-router-cni-deployment-575465c75c-qkq6m   1/1     Running   0          18m
   ```
4. View the logs and the routing table for the egress router pod.

   1. Get the node name for the egress router pod:

      ```
      $ POD_NODENAME=$(oc get pod -l app=egress-router-cni -o jsonpath="{.items[0].spec.nodeName}")
      ```
   2. Enter into a debug session on the target node. This step instantiates a debug pod called `<node_name>-debug`:

      ```
      $ oc debug node/$POD_NODENAME
      ```
   3. Set `/host` as the root directory within the debug shell. The debug pod mounts the root file system of the host in `/host` within the pod. By changing the root directory to `/host`, you can run binaries from the executable paths of the host:

      ```
      # chroot /host
      ```
   4. From within the `chroot` environment console, display the egress router logs:

      ```
      # cat /tmp/egress-router-log
      ```

      **Example output**

      ```
      2021-04-26T12:27:20Z [debug] Called CNI ADD
      2021-04-26T12:27:20Z [debug] Gateway: 192.168.12.1
      2021-04-26T12:27:20Z [debug] IP Source Addresses: [192.168.12.99/24]
      2021-04-26T12:27:20Z [debug] IP Destinations: [80 UDP 10.0.0.99/30 8080 TCP 203.0.113.26/30 80 8443 TCP 203.0.113.27/30 443]
      2021-04-26T12:27:20Z [debug] Created macvlan interface
      2021-04-26T12:27:20Z [debug] Renamed macvlan to "net1"
      2021-04-26T12:27:20Z [debug] Adding route to gateway 192.168.12.1 on macvlan interface
      2021-04-26T12:27:20Z [debug] deleted default route {Ifindex: 3 Dst: <nil> Src: <nil> Gw: 10.128.10.1 Flags: [] Table: 254}
      2021-04-26T12:27:20Z [debug] Added new default route with gateway 192.168.12.1
      2021-04-26T12:27:20Z [debug] Added iptables rule: iptables -t nat PREROUTING -i eth0 -p UDP --dport 80 -j DNAT --to-destination 10.0.0.99
      2021-04-26T12:27:20Z [debug] Added iptables rule: iptables -t nat PREROUTING -i eth0 -p TCP --dport 8080 -j DNAT --to-destination 203.0.113.26:80
      2021-04-26T12:27:20Z [debug] Added iptables rule: iptables -t nat PREROUTING -i eth0 -p TCP --dport 8443 -j DNAT --to-destination 203.0.113.27:443
      2021-04-26T12:27:20Z [debug] Added iptables rule: iptables -t nat -o net1 -j SNAT --to-source 192.168.12.99
      ```

      The logging file location and logging level are not configurable when you start the egress router by creating an `EgressRouter` object as described in this procedure.
   5. From within the `chroot` environment console, get the container ID:

      ```
      # crictl ps --name egress-router-cni-pod | awk '{print $1}'
      ```

      **Example output**

      ```
      CONTAINER
      bac9fae69ddb6
      ```
   6. Determine the process ID of the container. In this example, the container ID is `bac9fae69ddb6`:

      ```
      # crictl inspect -o yaml bac9fae69ddb6 | grep 'pid:' | awk '{print $2}'
      ```

      **Example output**

      ```
      68857
      ```
   7. Enter the network namespace of the container:

      ```
      # nsenter -n -t 68857
      ```
   8. Display the routing table:

      ```
      # ip route
      ```

      In the following example output, the `net1` network interface is the default route. Traffic for the cluster network uses the `eth0` network interface. Traffic for the `192.168.12.0/24` network uses the `net1` network interface and originates from the reserved source IP address `192.168.12.99`. The pod routes all other traffic to the gateway at IP address `192.168.12.1`. Routing for the service network is not shown.

      **Example output**

      ```
      default via 192.168.12.1 dev net1
      10.128.10.0/23 dev eth0 proto kernel scope link src 10.128.10.18
      192.168.12.0/24 dev net1 proto kernel scope link src 192.168.12.99
      192.168.12.1 dev net1
      ```

## [Chapter 13. Enabling multicast for a project](#nw-ovn-kubernetes-enabling-multicast) Copy linkLink copied to clipboard!

In OpenShift Container Platform with OVN-Kubernetes, you can enable IP multicast on a per-project basis so pods can send and receive multicast traffic.

### [13.1. About multicast](#nw-about-multicast_ovn-kubernetes-enabling-multicast) Copy linkLink copied to clipboard!

With IP multicast in OpenShift Container Platform, data is broadcast to many IP addresses simultaneously. With OVN-Kubernetes, multicast is off by default and is not affected by network policies when you enable it in a project.

Important

* At this time, multicast is best used for low-bandwidth coordination or service discovery and not a high-bandwidth solution.
* By default, network policies affect all connections in a namespace. However, multicast is unaffected by network policies. If multicast is enabled in the same namespace as your network policies, it is always allowed, even if there is a `deny-all` network policy.
* Cluster administrators must consider the implications of the exemption of multicast from network policies before enabling it.

Multicast traffic between OpenShift Container Platform pods is disabled by default. If you are using the OVN-Kubernetes network plugin, you can enable multicast on a per-project basis.

### [13.2. Enabling multicast between pods](#nw-enabling-multicast_ovn-kubernetes-enabling-multicast) Copy linkLink copied to clipboard!

To enable multicast between pods in a project, you can add the `k8s.ovn.org/multicast-enabled` annotation to the namespace by using the `oc annotate` command or a namespace manifest.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* You must log in to the cluster with a user that has the `cluster-admin` role.

**Procedure**

* Run the following command to enable multicast for a project. Replace `<namespace>` with the namespace for the project you want to enable multicast for.

  ```
  $ oc annotate namespace <namespace> \
      k8s.ovn.org/multicast-enabled=true
  ```

  Tip

  You can alternatively apply the following YAML to add the annotation:

  ```
  apiVersion: v1
  kind: Namespace
  metadata:
    name: <namespace>
    annotations:
      k8s.ovn.org/multicast-enabled: "true"
  ```

**Verification**

To verify that multicast is enabled for a project, complete the following procedure:

1. Change your current project to the project that you enabled multicast for. Replace `<project>` with the project name.

   ```
   $ oc project <project>
   ```
2. Create a pod to act as a multicast receiver:

   ```
   $ cat <<EOF| oc create -f -
   apiVersion: v1
   kind: Pod
   metadata:
     name: mlistener
     labels:
       app: multicast-verify
   spec:
     containers:
       - name: mlistener
         image: registry.access.redhat.com/ubi9
         command: ["/bin/sh", "-c"]
         args:
           ["dnf -y install socat hostname && sleep inf"]
         ports:
           - containerPort: 30102
             name: mlistener
             protocol: UDP
   EOF
   ```
3. Create a pod to act as a multicast sender:

   ```
   $ cat <<EOF| oc create -f -
   apiVersion: v1
   kind: Pod
   metadata:
     name: msender
     labels:
       app: multicast-verify
   spec:
     containers:
       - name: msender
         image: registry.access.redhat.com/ubi9
         command: ["/bin/sh", "-c"]
         args:
           ["dnf -y install socat && sleep inf"]
   EOF
   ```
4. In a new terminal window or tab, start the multicast listener.

   1. Get the IP address for the Pod:

      ```
      $ POD_IP=$(oc get pods mlistener -o jsonpath='{.status.podIP}')
      ```
   2. Start the multicast listener by entering the following command:

      ```
      $ oc exec mlistener -i -t -- \
          socat UDP4-RECVFROM:30102,ip-add-membership=224.1.0.1:$POD_IP,fork EXEC:hostname
      ```
5. Start the multicast transmitter.

   1. Get the pod network IP address range:

      ```
      $ CIDR=$(oc get Network.config.openshift.io cluster \
          -o jsonpath='{.status.clusterNetwork[0].cidr}')
      ```
   2. To send a multicast message, enter the following command:

      ```
      $ oc exec msender -i -t -- \
          /bin/bash -c "echo | socat STDIO UDP4-DATAGRAM:224.1.0.1:30102,range=$CIDR,ip-multicast-ttl=64"
      ```

      If multicast is working, the previous command returns the following output:

      ```
      mlistener
      ```

## [Chapter 14. Disabling multicast for a project](#nw-ovn-kubernetes-disabling-multicast) Copy linkLink copied to clipboard!

In OpenShift Container Platform with OVN-Kubernetes, you can disable IP multicast on a per-project basis so pods no longer receive multicast traffic.

### [14.1. Disabling multicast between pods](#nw-disabling-multicast_ovn-kubernetes-disabling-multicast) Copy linkLink copied to clipboard!

To disable multicast between pods in a project, you can remove the `k8s.ovn.org/multicast-enabled` annotation from the namespace by using the `oc annotate` command or a namespace manifest.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* You must log in to the cluster with a user that has the `cluster-admin` role.

**Procedure**

* Disable multicast by running the following command:

  ```
  $ oc annotate namespace <namespace> \
      k8s.ovn.org/multicast-enabled-
  ```

  For `<namespace>`, specify the namespace for the project you want to disable multicast for.

  Tip

  You can alternatively apply the following YAML to delete the annotation:

  ```
  apiVersion: v1
  kind: Namespace
  metadata:
    name: <namespace>
    annotations:
      k8s.ovn.org/multicast-enabled: null
  ```

## [Chapter 15. Tracking network flows](#tracking-network-flows) Copy linkLink copied to clipboard!

As a cluster administrator, you can collect information about pod network flows from your cluster to assist with the following areas:

* Monitor ingress and egress traffic on the pod network.
* Troubleshoot performance issues.
* Gather data for capacity planning and security audits.

When you enable the collection of the network flows, only the metadata about the traffic is collected. For example, packet data is not collected, but the protocol, source address, destination address, port numbers, number of bytes, and other packet-level information is collected.

The data is collected in one or more of the following record formats:

* NetFlow
* sFlow
* IPFIX

When you configure the Cluster Network Operator (CNO) with one or more collector IP addresses and port numbers, the Operator configures Open vSwitch (OVS) on each node to send the network flows records to each collector.

You can configure the Operator to send records to more than one type of network flow collector. For example, you can send records to NetFlow collectors and also send records to sFlow collectors.

When OVS sends data to the collectors, each type of collector receives identical records. For example, if you configure two NetFlow collectors, OVS on a node sends identical records to the two collectors. If you also configure two sFlow collectors, the two sFlow collectors receive identical records. However, each collector type has a unique record format.

Collecting the network flows data and sending the records to collectors affects performance. Nodes process packets at a slower rate. If the performance impact is too great, you can delete the destinations for collectors to disable collecting network flows data and restore performance.

Note

Enabling network flow collectors might have an impact on the overall performance of the cluster network.

### [15.1. Network object configuration for tracking network flows](#nw-network-flows-object_tracking-network-flows) Copy linkLink copied to clipboard!

The fields for configuring network flows collectors in the Cluster Network Operator (CNO) are shown in the following table:

Expand

Table 15.1. Network flows configuration

| Field | Type | Description |
| --- | --- | --- |
| `metadata.name` | `string` | The name of the CNO object. This name is always `cluster`. |
| `spec.exportNetworkFlows` | `object` | One or more of `netFlow`, `sFlow`, or `ipfix`. |
| `spec.exportNetworkFlows.netFlow.collectors` | `array` | A list of IP address and network port pairs for up to 10 collectors. |
| `spec.exportNetworkFlows.sFlow.collectors` | `array` | A list of IP address and network port pairs for up to 10 collectors. |
| `spec.exportNetworkFlows.ipfix.collectors` | `array` | A list of IP address and network port pairs for up to 10 collectors. |

Show more

After applying the following manifest to the CNO, the Operator configures Open vSwitch (OVS) on each node in the cluster to send network flows records to the NetFlow collector that is listening at `192.168.1.99:2056`.

**Example configuration for tracking network flows**

```
apiVersion: operator.openshift.io/v1
kind: Network
metadata:
  name: cluster
spec:
  exportNetworkFlows:
    netFlow:
      collectors:
        - 192.168.1.99:2056
```

### [15.2. Adding destinations for network flows collectors](#nw-network-flows-create_tracking-network-flows) Copy linkLink copied to clipboard!

As a cluster administrator, you can configure the Cluster Network Operator (CNO) to send network flows metadata about the pod network to a network flows collector.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.
* You have a network flows collector and know the IP address and port that it listens on.

**Procedure**

1. Create a patch file that specifies the network flows collector type and the IP address and port information of the collectors:

   ```
   spec:
     exportNetworkFlows:
       netFlow:
         collectors:
           - 192.168.1.99:2056
   ```
2. Configure the CNO with the network flows collectors:

   ```
   $ oc patch network.operator cluster --type merge -p "$(cat <file_name>.yaml)"
   ```

   **Example output**

   ```
   network.operator.openshift.io/cluster patched
   ```

**Verification**

Verification is not typically necessary. You can run the following command to confirm that Open vSwitch (OVS) on each node is configured to send network flows records to one or more collectors.

1. View the Operator configuration to confirm that the `exportNetworkFlows` field is configured:

   ```
   $ oc get network.operator cluster -o jsonpath="{.spec.exportNetworkFlows}"
   ```

   **Example output**

   ```
   {"netFlow":{"collectors":["192.168.1.99:2056"]}}
   ```
2. View the network flows configuration in OVS from each node:

   ```
   $ for pod in $(oc get pods -n openshift-ovn-kubernetes -l app=ovnkube-node -o jsonpath='{range@.items[*]}{.metadata.name}{"\n"}{end}');
     do ;
       echo;
       echo $pod;
       oc -n openshift-ovn-kubernetes exec -c ovnkube-controller $pod \
         -- bash -c 'for type in ipfix sflow netflow ; do ovs-vsctl find $type ; done';
   done
   ```

   **Example output**

   ```
   ovnkube-node-xrn4p
   _uuid               : a4d2aaca-5023-4f3d-9400-7275f92611f9
   active_timeout      : 60
   add_id_to_interface : false
   engine_id           : []
   engine_type         : []
   external_ids        : {}
   targets             : ["192.168.1.99:2056"]

   ovnkube-node-z4vq9
   _uuid               : 61d02fdb-9228-4993-8ff5-b27f01a29bd6
   active_timeout      : 60
   add_id_to_interface : false
   engine_id           : []
   engine_type         : []
   external_ids        : {}
   targets             : ["192.168.1.99:2056"]-

   ...
   ```

### [15.3. Deleting all destinations for network flows collectors](#nw-network-flows-delete_tracking-network-flows) Copy linkLink copied to clipboard!

As a cluster administrator, you can configure the Cluster Network Operator (CNO) to stop sending network flows metadata to a network flows collector.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You are logged in to the cluster with a user with `cluster-admin` privileges.

**Procedure**

1. Remove all network flows collectors:

   ```
   $ oc patch network.operator cluster --type='json' \
       -p='[{"op":"remove", "path":"/spec/exportNetworkFlows"}]'
   ```

   **Example output**

   ```
   network.operator.openshift.io/cluster patched
   ```

## [Chapter 16. Configuring hybrid networking](#configuring-hybrid-networking) Copy linkLink copied to clipboard!

In OpenShift Container Platform, you can configure OVN-Kubernetes hybrid networking so Linux and Windows nodes run Linux and Windows workloads in the same cluster.

### [16.1. Configuring hybrid networking with OVN-Kubernetes](#configuring-hybrid-ovnkubernetes_configuring-hybrid-networking) Copy linkLink copied to clipboard!

To configure hybrid networking with OVN-Kubernetes, you can set `hybridOverlayConfig` during installation or patch the Cluster Network Operator (CNO) after installation.

Note

This configuration is necessary to run both Linux and Windows nodes in the same cluster.

**Prerequisites**

* Install the OpenShift CLI (`oc`).
* Log in to the cluster as a user with `cluster-admin` privileges.
* Ensure that the cluster uses the OVN-Kubernetes network plugin.

**Procedure**

1. To configure the OVN-Kubernetes hybrid network overlay, enter the following command:

   ```
   $ oc patch networks.operator.openshift.io cluster --type=merge \
     -p '{
       "spec":{
         "defaultNetwork":{
           "ovnKubernetesConfig":{
             "hybridOverlayConfig":{
               "hybridClusterNetwork":[
                 {
                   "cidr": "<cidr>",
                   "hostPrefix": <prefix>
                 }
               ],
               "hybridOverlayVXLANPort": <overlay_port>
             }
           }
         }
       }
     }'
   ```

   where:

   `<cidr>`
   :   Specifies the CIDR configuration used for nodes on the additional overlay network. This CIDR must not overlap with the cluster network CIDR.

   `<prefix>`
   :   Specifies the subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23`, then each node is assigned a `/23` subnet out of the given `cidr`, which allows for 510 (2^(32 - 23) - 2) pod IP addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.

   `<overlay_port>`
   :   Specifies a custom VXLAN port for the additional overlay network. This is required for running Windows nodes in a cluster installed on vSphere, and must not be configured for any other cloud provider. The custom port can be any open port excluding the default `6081` port. For more information on this requirement, see [Pod-to-pod connectivity between hosts is broken](https://docs.microsoft.com/en-us/virtualization/windowscontainers/kubernetes/common-problems#pod-to-pod-connectivity-between-hosts-is-broken-on-my-kubernetes-cluster-running-on-vsphere) in the Microsoft documentation.

       Note

       Windows Server Long-Term Servicing Channel (LTSC): Windows Server 2019 is not supported on clusters with a custom `hybridOverlayVXLANPort` value because this Windows server version does not support selecting a custom VXLAN port.

       **Example output**

       ```
       network.operator.openshift.io/cluster patched
       ```
2. To confirm that the configuration is active, enter the following command. It can take several minutes for the update to apply.

   ```
   $ oc get network.operator.openshift.io -o jsonpath="{.items[0].spec.defaultNetwork.ovnKubernetesConfig}"
   ```

## [Legal Notice](#idm140110959607360) Copy linkLink copied to clipboard!

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
