---
title: "Installing a Two Node OpenShift Cluster"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_a_two_node_openshift_cluster/index
retrieved_at: 2026-09-05T05:41:55.094251+00:00
---

# Installing a Two Node OpenShift Cluster

---

OpenShift Container Platform 4.22

## Installing OpenShift Container Platform on two nodes

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140668985558032)

**Abstract**

This document describes how to install OpenShift Container Platform on two nodes.

---

## [Chapter 1. Two-Node with Arbiter](#about-two-node-arbiter-installation) Copy linkLink copied to clipboard!

An OpenShift Container Platform cluster with two control plane nodes and one local arbiter node is a compact, cost-effective OpenShift Container Platform topology.

The arbiter node stores the full etcd data, maintaining an etcd quorum and preventing split brain. The arbiter node does not run the additional control plane components `kube-apiserver` and `kube-controller-manager`, nor does it run workloads.

To install a cluster with two control plane nodes and one local arbiter node, assign an arbiter role to at least one of the nodes and set the control plane node count for the cluster to 2. Although OpenShift Container Platform does not currently impose a limit on the number of arbiter nodes, the typical deployment includes only one to minimize the use of hardware resources.

After installation, you can add additional worker nodes to a cluster with two control plane nodes and one local arbiter node but it cannot be converted to a standard multi-node cluster.

Note

Do not add more than two worker nodes to the OpenShift Container Platform cluster. For a cluster with an arbiter, the same networking requirements as a regular cluster for connectivity between machines apply.

## [Chapter 2. Two-node with Fencing](#two-node-with-fencing) Copy linkLink copied to clipboard!

### [2.1. Preparing to install a two-node OpenShift cluster with fencing](#installing-two-node-fencing) Copy linkLink copied to clipboard!

A two-node OpenShift Container Platform cluster with fencing provides high availability (HA) with a reduced hardware footprint. This configuration is designed for distributed or edge environments where deploying a full three-node control plane cluster is not practical.

A two-node cluster does not include compute nodes. The two control plane machines run user workloads in addition to managing the cluster.

Fencing is managed by Pacemaker, which can isolate an unresponsive node by using the Baseboard Management Console (BMC) of the node. After the unresponsive node is fenced, the remaining node can safely continue operating the cluster without the risk of resource corruption.

Note

You can deploy a two-node OpenShift Container Platform cluster with fencing by using either the user-provisioned infrastructure method or the installer-provisioned infrastructure method.

The two-node OpenShift cluster with fencing requires the following hosts:

Expand

Table 2.1. Minimum required hosts

| Hosts | Description |
| --- | --- |
| Two control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| One temporary bootstrap machine | You need a bootstrap machine to deploy the OpenShift Container Platform cluster on the control plane machines. You can remove the bootstrap machine after you install the cluster. |

Show more

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. For instructions on installing RHCOS and starting the bootstrap process, see "Installing RHCOS and starting the OpenShift Container Platform bootstrap process".

Note

The requirement to use RHCOS applies only to user-provisioned infrastructure deployments. For installer-provisioned infrastructure deployments, the bootstrap and control plane machines are provisioned automatically by the installation program, and you do not need to manually install RHCOS.

#### [2.1.1. Minimum resource requirements for installing a two-node OpenShift cluster with fencing](#installation-two-node-fencing-minimum-resource-requirements_installing-two-node-fencing) Copy linkLink copied to clipboard!

Each cluster must meet minimum requirements so that the cluster runs as expected.

Each cluster machine must meet the following minimum requirements:

Expand

Table 2.2. Minimum resource requirements

| Machine | Operating System | CPU [1] | RAM | Storage | Input/Output Per Second (IOPS) [1] |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | RHCOS | 4 | 16 GB | 120 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 120 GB | 300 |

Show more

1. One CPU is equivalent to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = CPUs.
2. OpenShift Container Platform and Kubernetes are sensitive to disk performance, and faster storage is recommended, particularly for etcd on the control plane nodes. Note that on many cloud platforms, storage size and IOPS scale together, so you might need to over-allocate storage volume to obtain sufficient performance.

#### [2.1.2. User-provisioned DNS requirements](#installation-dns-user-infra_installing-two-node-fencing) Copy linkLink copied to clipboard!

In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes.

The following is a list of required cluster components:

* The Kubernetes API
* The OpenShift Container Platform application wildcard
* The bootstrap and control plane machines

Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, and the control plane machines.

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate.

Note

It is recommended to use a DHCP server to provide the hostnames to each cluster node. See the *DHCP recommendations for user-provisioned infrastructure* section for more information.

The following DNS records are required for a user-provisioned OpenShift Container Platform cluster and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

Expand

Table 2.3. Required DNS records

| Component | Record | Description |
| --- | --- | --- |
| Kubernetes API | `api.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |
| `api-int.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.  Important  The API server must be able to resolve the worker nodes by the hostnames that are recorded in Kubernetes. If the API server cannot resolve the node names, then proxied API calls can fail, and you cannot retrieve logs from pods. |
| Routes | `*.apps.<cluster_name>.<base_domain>.` | A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. By default, the Ingress Controller pods run on compute nodes. In cluster topologies without dedicated compute nodes, such as two-node or three-node clusters, the control plane nodes also carry the worker label, so the Ingress pods are scheduled on the control plane nodes. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.  For example, `console-openshift-console.apps.<cluster_name>.<base_domain>` is used as a wildcard route to the OpenShift Container Platform console. |
| Bootstrap machine | `bootstrap.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the bootstrap machine. These records must be resolvable by the nodes within the cluster. |
| Control plane machines | `<control_plane><n>.<cluster_name>.<base_domain>.` | DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the control plane nodes. These records must be resolvable by the nodes within the cluster. |

Show more

Note

In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration.

Tip

You can use the `dig` command to verify name and reverse name resolution. See the section on *Validating DNS resolution for user-provisioned infrastructure* for detailed validation steps.

##### [2.1.2.1. Example DNS configuration for user-provisioned clusters](#installation-dns-user-infra-example_installing-two-node-fencing) Copy linkLink copied to clipboard!

Reference the example DNS configurations to understand how A and PTR record configuration samples meet the DNS requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

The DNS configuration examples provided here are for reference only and are not meant to provide advice for choosing one DNS solution over another.

In the examples, the cluster name is `ocp4` and the base domain is `example.com`.

Note

In a two-node cluster with fencing, the control plane machines are also schedulable worker nodes. The DNS configuration must therefore include only the two control plane nodes. If you later add compute machines, provide corresponding A and PTR records for them as in a standard user-provisioned installation.

The following example is a BIND zone file that shows sample DNS A records for name resolution in a user-provisioned cluster.

Note

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

```
$TTL 1W
@	IN	SOA	ns1.example.com.	root (
			2019070700	; serial
			3H		; refresh (3 hours)
			30M		; retry (30 minutes)
			2W		; expiry (2 weeks)
			1W )		; minimum (1 week)
	IN	NS	ns1.example.com.
	IN	MX 10	smtp.example.com.
;
;
ns1.example.com.		IN	A	192.168.1.5
smtp.example.com.		IN	A	192.168.1.5
;
helper.example.com.		IN	A	192.168.1.5
helper.ocp4.example.com.	IN	A	192.168.1.5
;
api.ocp4.example.com.		IN	A	192.168.1.5
api-int.ocp4.example.com.	IN	A	192.168.1.5
;
*.apps.ocp4.example.com.	IN	A	192.168.1.5
;
bootstrap.ocp4.example.com.	IN	A	192.168.1.96
;
control-plane0.ocp4.example.com.	IN	A	192.168.1.97
control-plane1.ocp4.example.com.	IN	A	192.168.1.98
;
;
;EOF
```

where:

`api.ocp4.example.com.`
:   Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer.

`api-int.ocp4.example.com.`
:   Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer and is used for internal cluster communications.

`*.apps.ocp4.example.com.`
:   Provides name resolution for the wildcard routes. The record refers to the IP address of the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods.

`bootstrap.ocp4.example.com`
:   Provides name resolution for the bootstrap machine.

`control-plane0.ocp4.example.com`
:   Provides name resolution for the control plane machines.

The following example BIND zone file shows sample PTR records for reverse name resolution in a user-provisioned cluster:

```
$TTL 1W
@	IN	SOA	ns1.example.com.	root (
			2019070700	; serial
			3H		; refresh (3 hours)
			30M		; retry (30 minutes)
			2W		; expiry (2 weeks)
			1W )		; minimum (1 week)
	IN	NS	ns1.example.com.
;
5.1.168.192.in-addr.arpa.	IN	PTR	api.ocp4.example.com.
5.1.168.192.in-addr.arpa.	IN	PTR	api-int.ocp4.example.com.
;
96.1.168.192.in-addr.arpa.	IN	PTR	bootstrap.ocp4.example.com.
;
97.1.168.192.in-addr.arpa.	IN	PTR	control-plane0.ocp4.example.com.
98.1.168.192.in-addr.arpa.	IN	PTR	control-plane1.ocp4.example.com.
;
;
;EOF
```

where:

`api.ocp4.example.com.`
:   Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer.

`api-int.ocp4.example.com.`
:   Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer and is used for internal cluster communications.

`bootstrap.ocp4.example.com.`
:   Provides reverse DNS resolution for the bootstrap machine.

`control-plane0.ocp4.example.com.`
:   Provides rebootstrap.ocp4.example.com.verse DNS resolution for the control plane machines.

Note

A PTR record is not required for the OpenShift Container Platform application wildcard.

#### [2.1.3. Installer-provisioned DNS requirements](#installation-installer-user-infra_installing-two-node-fencing) Copy linkLink copied to clipboard!

In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes.

Clients access the OpenShift Container Platform cluster nodes over the `baremetal` network. A network administrator must configure a subdomain or subzone where the canonical name extension is the cluster name.

```
<cluster_name>.<base_domain>
```

For example:

```
test-cluster.example.com
```

OpenShift Container Platform includes functionality that uses cluster membership information to generate A/AAAA records. This resolves the node names to their IP addresses. After the nodes are registered with the API, the cluster can disperse node information without using CoreDNS-mDNS. This eliminates the network traffic associated with multicast DNS.

CoreDNS requires both TCP and UDP connections to the upstream DNS server to function correctly. Ensure the upstream DNS server can receive both TCP and UDP connections from OpenShift Container Platform cluster nodes.

In OpenShift Container Platform deployments, DNS name resolution is required for the following components:

* The Kubernetes API
* The OpenShift Container Platform application wildcard ingress API

A/AAAA records are used for name resolution and PTR records are used for reverse name resolution. Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records or DHCP to set the hostnames for all the nodes.

Installer-provisioned installation includes functionality that uses cluster membership information to generate A/AAAA records. This resolves the node names to their IP addresses. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

Expand

Table 2.4. Required DNS records

| Component | Record | Description |
| --- | --- | --- |
| Kubernetes API | `api.<cluster_name>.<base_domain>.` | An A/AAAA record and a PTR record identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |
| Routes | `*.apps.<cluster_name>.<base_domain>.` | The wildcard A/AAAA record refers to the application ingress load balancer. The application ingress load balancer targets the nodes that run the Ingress Controller pods. The Ingress Controller pods run on the worker nodes by default. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.  For example, `console-openshift-console.apps.<cluster_name>.<base_domain>` is used as a wildcard route to the OpenShift Container Platform console. |

Show more

Tip

You can use the `dig` command to verify DNS resolution.

#### [2.1.4. Creating a manifest object for a customized br-ex bridge](#creating-manifest-custom-br-ex_installing-two-node-fencing) Copy linkLink copied to clipboard!

You must create a manifest object to modify the cluster’s network configuration after installation. The manifest configures the br-ex bridge, which manages external network connectivity for the cluster.

For instructions on creating this manifest, see "Creating a manifest file for a customized br-ex bridge".

### [2.2. Installing a two-node OpenShift cluster with fencing](#installing-tnf) Copy linkLink copied to clipboard!

For a highly available, small-footprint container platform at your edge sites or resource-constrained environments, you can deploy a two-node OpenShift cluster with fencing (TNF). This fencing mechanism protects your applications and data from `split-brain` scenarios by safely isolating a node if communication fails. To match your existing environment, you can deploy this cluster using automated, manual, or agent-based infrastructure methods.

Automated Infrastructure (installer-provisioned)
:   The cluster installation program controls all aspects of the deployment, including provisioning the underlying cloud or virtualization platforms, configuring network resources, and spinning up the nodes.

Manual Infrastructure (user-provisioned)
:   You provision and manage your own operating system images, networking, storage, and load balancers before starting the OpenShift deployment. This method offers maximum control over custom enterprise environments.

Agent-Based Infrastructure
:   You use a bootable ISO image containing an agent that automates the deployment on bare metal or pre-provisioned infrastructure. This combines the flexibility of manual setups with the ease of an automated workflow, making it ideal for disconnected environments.

Important

Configure node access during installation, for example, by including SSH keys in the `install-config.yaml` file. TNF clusters might require manual intervention in specific error scenarios that can only be resolved through direct node access.

#### [2.2.1. Sample install-config.yaml file for a two-node installer-provisioned infrastructure cluster with fencing](#sample-install-config-two-node-fencing-ipi_install-tnf) Copy linkLink copied to clipboard!

You can use the following `install-config.yaml` configuration file as a template for deploying a two-node OpenShift cluster with fencing (TNF) by using the installer-provisioned infrastructure method:

Note

Back up etcd before proceeding to ensure that you can restore the cluster if an issue occurs.

**Sample `install-config.yaml` configuration**

```
apiVersion: v1
baseDomain: example.com
compute:
- name: worker
  replicas: 0
controlPlane:
  name: master
  replicas: 2
  fencing:
    credentials:
      - hostname: <control_0_hostname>
        address: https://<redfish-api-url>
        username: <username>
        password: <password>
        certificateVerification: Disabled
      - hostname: <control_1_hostname>
        address: https://<redfish-api-url>
        username: <username>
        password: <password>
        certificateVerification: Enabled
metadata:
  name: <cluster_name>
platform:
  baremetal:
    apiVIPs:
      - <api_ip>
    ingressVIPs:
      - <wildcard_ip>
    hosts:
      - name: <control_0_hostname>
        role: master
        bmc:
          address: <bmc_address>
          username: <bmc_username>
          password: <bmc_password>
        bootMACAddress: <boot_mac>
      - name: <control_1_hostname>
        role: master
        bmc:
          address: <bmc_address>
          username: <bmc_username>
          password: <bmc_password>
        bootMACAddress: <boot_mac>
pullSecret: '<pull_secret>'
sshKey: '<ssh_public_key>'
```

* `compute.replicas`: Set this field to `0` because a two-node OpenShift Container Platform cluster with fencing does not include worker nodes.
* `controlPlane.replicas`: Set this field to `2` for a two-node OpenShift Container Platform cluster with fencing deployment.
* `fencing.credentials.hostname`: Provide the Baseboard Management Console (BMC) credentials for each control plane node. These credentials are required for node fencing and prevent split-brain scenarios.
* `fencing.credentials.certificateVerification`: Set this field to `Disabled` if your Redfish URL uses self-signed certificates, which is common for internally-hosted endpoints. Set this field to `Enabled` for URLs with valid CA-signed certificates.
* `metadata.name`: The cluster name is used as a prefix for hostnames and DNS records.
* `platform.baremetal.apiVIPs` and `platform.baremetal.ingressVIPs` : Virtual IPs for the API and Ingress endpoints. Ensure they are reachable by all nodes and external clients.
* `pullSecret`: Contains credentials required to pull container images for the cluster components.
* `sshKey`: The SSH public key for accessing cluster nodes after installation.

#### [2.2.2. Sample install-config.yaml file for a two-node user-provisioned infrastructure cluster with fencing](#sample-install-config-two-node-fencing-upi_install-tnf) Copy linkLink copied to clipboard!

You can use the following `install-config.yaml` configuration file as a template for deploying a two-node OpenShift Container Platform cluster with fencing by using the user-provisioned infrastructure method:

Note

Back up etcd before proceeding to ensure that you can restore the cluster if an issue occurs.

**Sample `install-config.yaml` configuration**

```
apiVersion: v1
baseDomain: example.com
compute:
- name: worker
  replicas: 0
controlPlane:
  name: master
  replicas: 2
  fencing:
    credentials:
      - hostname: <control_0_hostname>
        address: https://<redfish-api-url>
        username: <username>
        password: <password>
      - hostname: <control_1_hostname>
        address: https://<redfish-api-url>
        username: <username>
        password: <password>
metadata:
  name: <cluster_name>
platform:
  none: {}
pullSecret: '<pull_secret>'
sshKey: '<ssh_public_key>'
```

* `compute.replicas`: Set this field to `0` because a two-node OpenShift Container Platform cluster with fencing does not include worker nodes.
* `controlPlane.replicas`: Set this field to `2` for a two-node fencing deployment.
* `fencing.credentials.hostname`: Provide BMC credentials for each control plane node.
* `metadata.name`: Cluster name is used as a prefix for hostnames and DNS records.
* `platform.none` Set the platform to `none` for user-provisioned infrastructure deployments. Bare-metal hosts are pre-provisioned outside of the installation program.
* `pullSecret`: Contains credentials required to pull container images for the cluster components.
* `sshKey`: The SSH public key for accessing cluster nodes after installation.

#### [2.2.3. Sample install-config.yaml file for a two-node cluster with fencing for Agent-based Installer](#sample-install-config-two-node-fencing-abi_install-tnf) Copy linkLink copied to clipboard!

You can use the following `install-config.yaml` configuration file as a template for deploying a two-node OpenShift Container Platform cluster with fencing (TNF) by using the Agent-based Installer method.

See the following sample `install-config.yaml` configuration file for bare-metal:

```
apiVersion: v1
baseDomain: example.com
controlPlane:
  name: master
  replicas: 2
  fencing:
    credentials:
    - hostname: master-0
      address: redfish+https://<bmc_ip_0>:<bmc_port>/redfish/v1/Systems/<system_id_0>
      username: <bmc_username>
      password: <bmc_password>
      certificateVerification: Disabled
    - hostname: master-1
      address: redfish+https://<bmc_ip_1>:<bmc_port>/redfish/v1/Systems/<system_id_1>
      username: <bmc_username>
      password: <bmc_password>
      certificateVerification: Disabled
compute:
- name: worker
  replicas: 0
metadata:
  name: <cluster_name>
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  networkType: OVNKubernetes
  machineNetwork:
  - cidr: <machine_network_cidr>
  serviceNetwork:
  - 172.30.0.0/16
platform:
  baremetal:
    apiVIPs:
    - <api_vip>
    ingressVIPs:
    - <ingress_vip>
pullSecret: '<pull_secret>'
sshKey: '<ssh_public_key>'
```

* `platform.baremetal.apiVIPs` and `ingressVIPs`: Specifies virtual IPs for the API and Ingress endpoints. Required for bare-metal platform; not applicable for `none`.

For other bare metal specific fields, see "Installation configuration parameters for the Agent-based Installer".

The following sample `install-config.yaml` configuration file is for the attribute platform with value `none`.

You must provide DNS name resolution and load balancing infrastructure.

```
apiVersion: v1
baseDomain: example.com
controlPlane:
  name: master
  replicas: 2
  fencing:
    credentials:
    - hostname: master-0
      address: redfish+https://<bmc_ip_0>:<bmc_port>/redfish/v1/Systems/<system_id_0>
      username: <bmc_username>
      password: <bmc_password>
      certificateVerification: Disabled
    - hostname: master-1
      address: redfish+https://<bmc_ip_1>:<bmc_port>/redfish/v1/Systems/<system_id_1>
      username: <bmc_username>
      password: <bmc_password>
      certificateVerification: Disabled
compute:
- name: worker
  replicas: 0
metadata:
  name: <cluster_name>
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  networkType: OVNKubernetes
  machineNetwork:
  - cidr: <machine_network_cidr>
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
pullSecret: '<pull_secret>'
sshKey: '<ssh_public_key>'
```

* `controlPlane.replicas`: Must be `2` for a two-node OpenShift Container Platform cluster with fencing (TNF).
* `compute[0].replicas`: Must be `0`. A two-node OpenShift Container Platform cluster with fencing does not support compute nodes.
* `controlPlane.fencing.credentials`: Exactly 2 entries required, one per control plane node.
* `fencing.credentials[].hostname`: The hostname of the control plane node. Must be unique across credentials.
* `fencing.credentials[].address`: The Redfish BMC URL. Must use the `redfish+https://` scheme (for example, `redfish+[https://192.168.1.10:443/redfish/v1/Systems/1](https://192.168.1.10:443/redfish/v1/Systems/1))`. IPMI addresses are not supported. Vendor-specific Redfish schemes such as `idrac-redfish+https://` and `ilo5-redfish+https://` are also accepted.
* `fencing.credentials[].username`: BMC username for the node.
* `fencing.credentials[].password`: BMC password for the node.
* `fencing.credentials[].certificateVerification`: Optional. Set to Disabled if your BMC uses self-signed certificates (common for internally-hosted endpoints). Set to Enabled (default) for BMCs with valid CA-signed certificates.

#### [2.2.4. Sample agent-config.yaml file for a two-node cluster with fencing for Agent-based Installer](#sample-agent-config-two-node-fencing-abi_install-tnf) Copy linkLink copied to clipboard!

You can use the following `agent-config.yaml` configuration file as a template for deploying a two-node OpenShift Container Platform cluster with fencing (TNF) by using the Agent-based Installer method:

See the following sample `agent-config.yaml` file with minimal configuration:

```
apiVersion: v1beta1
metadata:
  name: <cluster_name>
rendezvousIP: <rendezvous_ip>
```

* `rendezvousIP`: Specifies the IP address of the node that will act as the rendezvous host during installation. This node runs the Assisted Service and coordinates the installation of both nodes.

See the following sample `agent-config.yaml` file with host configuration and static networking:

Note

The `hostname` values in the `agent-config.yaml` file must match the `hostname` values in the fencing credentials section of the `install-config.yaml`.

```
apiVersion: v1beta1
metadata:
  name: <cluster_name>
rendezvousIP: <rendezvous_ip>
additionalNTPSources:
- 0.rhel.pool.ntp.org
- 1.rhel.pool.ntp.org
hosts:
- hostname: master-0
  role: master
  interfaces:
  - name: <nic_name>
    macAddress: <mac_address_0>
  networkConfig:
    interfaces:
    - name: <nic_name>
      type: ethernet
      state: up
      ipv4:
        enabled: true
        dhcp: false
        address:
        - ip: <master_0_ip>
          prefix-length: <prefix_length>
      ipv6:
        enabled: false
    dns-resolver:
      config:
        server:
        - <dns_server>
    routes:
      config:
      - destination: 0.0.0.0/0
        next-hop-address: <gateway>
        next-hop-interface: <nic_name>
        table-id: 254
- hostname: master-1
  role: master
  interfaces:
  - name: <nic_name>
    macAddress: <mac_address_1>
  networkConfig:
    interfaces:
    - name: <nic_name>
      type: ethernet
      state: up
      ipv4:
        enabled: true
        dhcp: false
        address:
        - ip: <master_1_ip>
          prefix-length: <prefix_length>
      ipv6:
        enabled: false
    dns-resolver:
      config:
        server:
        - <dns_server>
    routes:
      config:
      - destination: 0.0.0.0/0
        next-hop-address: <gateway>
        next-hop-interface: <nic_name>
        table-id: 254
```

### [2.3. Operating a degraded two-node OpenShift cluster with fencing](#operating-a-degraded-tnf) Copy linkLink copied to clipboard!

A two-node OpenShift cluster with fencing (TNF) enters a `degraded` state when one of its two control plane nodes becomes unavailable. The remaining node continues to host the active control plane; however, the cluster loses its high-availability (HA) redundancy until the failed node recovers.

Degraded operation is an intentional design state rather than a system failure. In this state, the cluster remains functional and core services continue to operate. Only specific capabilities that strictly require two-node redundancy are temporarily unavailable.

Important

A degraded cluster has zero fault tolerance. If the surviving node also fails, the cluster fails. Restore the second node as soon as possible. Degraded operation is a temporary recovery window, not a long-term steady state.

#### [2.3.1. TNF cluster degradation causes](#tnf-cluster-degradation-causes_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

A two-node OpenShift cluster with fencing (TNF) becomes degraded when one node fails or loses communication with the cluster. Identifying the specific cause of degradation is essential because it determines whether the cluster can automatically recover or if manual intervention, such as fencing or hardware repair, is required to prevent data corruption and maintain service availability.

Some common causes of cluster degradation include:

Graceful shutdown or power-off
:   A graceful shutdown occurs when an administrator manually initiates a power-off sequence, allowing the operating system to signal processes to stop and unmount file systems correctly. This intentional action ensures that data remains consistent and the node is marked as `Offline` within the cluster before the hardware ceases operation.

Hardware failure or power loss
:   Sudden hardware malfunctions, such as a disk controller failure or an unconditioned power loss, result in an immediate cessation of service without warning. Unlike a graceful shutdown, these events provide the system no opportunity to clean up active processes, which often necessitates a consistency check or automated recovery once power is restored.

Network partition or loss of connectivity
:   A network partition occurs when a failure in the switching fabric or cabling prevents nodes from communicating with each other, even though the individual nodes remain powered on. In a two-node cluster, this split-brain scenario is particularly dangerous because each node might respond as if the other has failed and attempt to take exclusive control of shared resources.

Kernel panic
:   A kernel panic occurs when the core operating system encounters a critical internal error such as a memory corruption or an unrecoverable driver conflict from which it might not safely recover. To protect the integrity of the data, the kernel immediately halts all system execution, effectively freezing the node until a hard reboot is performed.

Node hang
:   A node hang describes a situation where the hardware remains powered on, but the system stops responding to all external requests, including pings and SSH attempts. This state is often the result of deadlocks in the software or an infinite loop in a high-priority process that starves the rest of the system of CPU cycles.

Kubelet failure or resource exhaustion
:   A node becomes unstable if the kubelet crashes or if the node suffers from extreme resource exhaustion, such as running out of RAM (OOM) or disk space. When the kubelet cannot report its heartbeat to the control plane, the cluster eventually marks the node as `NotReady` and attempts to evacuate its workloads.

#### [2.3.2. Node failure sequence in a TNF cluster](#node-failure-sequence-in-a-tnf-cluster_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

A two-node OpenShift cluster with fencing (TNF) enters a `degraded` state when one of its two control plane nodes becomes unavailable. The active control plane remains hosted on the surviving node, allowing the cluster to remain functional within defined constraints.

The automatic failure handling has the following sequence:

* Detection: Corosync detects the failure.

  The cluster framework registers that heartbeat signals from the peer node have ceased.
* Isolation: STONITH fencing execution.

  The surviving node uses the Redfish API to contact the baseboard management controller (BMC) of the failed node. It issues a power-off or reboot command to ensure the failed node is isolated. This prevents a `split-brain` scenario where the isolated node continues running containers locally while OpenShift Container Platform attempts to reschedule those same workloads onto healthy nodes, ensuring that stateful pods, routing services, and storage volumes maintain a single, valid owner.

  If the Shoot The Other Node In The Head (STONITH) fencing operation fails, the surviving node cannot safely assume control of cluster resources. In this case, an administrator must manually power off the failed hardware before the cluster can recover.
* Quorum Adjustment: etcd transits to single-member operation.

  The etcd Operator demotes the etcd member of the failed node to a non-voting learner. The surviving member operates as the sole voter, maintaining quorum. etcd continues to operate with a single voting member, maintaining a valid quorum so that the Kubernetes API remains accessible.
* Scheduling: Node status transitions to `NotReady`.

  When a node fails, Kubernetes updates its status, and affected workloads lose redundancy. On a live cluster, `DaemonSet` pods remain `Running` and `Deployment` pods display a `Terminating` status. However, because the unreachable kubelet cannot process the deletion, these `Deployment` pods technically remain in a Running API phase and are only rescheduled if surviving nodes have available resources and clear anti-affinity rules.

#### [2.3.3. Pacemaker and fencing behavior during degraded operation](#pacemaker-and-fencing-behavior-during-degraded-operation_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

During degraded operation, the Pacemaker cluster manager transitions from a distributed coordination model to a localized enforcement structure on the surviving node.

Degraded cluster operations include the following structural behaviors:

* The surviving node remains `ONLINE` and continues managing etcd, kubelet, and Shoot The Other Node In The Head (STONITH) fence devices.
* The failed node is reported as `OFFLINE` or `UNCLEAN OFFLINE`, depending on whether the shutdown was clean.
* Fencing devices remain enabled. The STONITH device for the failed node is still available on the surviving node. However, the STONITH device for the surviving node cannot be used because the node that would trigger it is offline.
* Pacemaker does not attempt to restart resources on the failed node or migrate resources to it.

Important

Mutual fencing protection is unavailable during degraded operations. Fencing actions cannot execute against the surviving node because the communication and execution paths from the peer node are offline.

#### [2.3.4. Cluster operator stability during degraded operation](#cluster-operator-stability-during-degraded-operation_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

OpenShift Container Platform cluster Operators maintain control plane stability and API availability when a two-node OpenShift cluster with fencing (TNF) enters a degraded state.

During degraded operations, cluster Operator conditions exhibit the following behaviors:

* Most Operators maintain an `Available=True` condition, ensuring that core API functionality remains accessible.
* The following Operators transition to a `Degraded=True` condition because only one of the two expected control plane instances is operational:

  + `etcd`
  + `kube-apiserver`
  + `kube-controller-manager`
  + `kube-scheduler`
  + `machine-config`
* Specific Operators might exhibit a `Progressing=True` condition during reconciliation routines that require data from both infrastructure nodes. This condition resolves when the second node returns to an online state.

Note

Unexpected or cascading Operator failures must not occur during degraded operation. If they do, investigate the issue as a potential bug.

#### [2.3.5. Capabilities during degraded TNF operation](#capabilities-during-degraded-tnf-operation_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

When a two-node OpenShift cluster with fencing (TNF) cluster is operating in a degraded state, some of the cluster capabilities are still available.

Expand

Table 2.5. Cluster capabilities during degraded operation

| Capability | Available |
| --- | --- |
| Kubernetes API server (read and write) | Yes |
| Workloads on the surviving node | Yes |
| Scheduling new workloads to the surviving node | Yes |
| etcd (single-member quorum) | Yes |
| Cluster monitoring and alerting | Yes |
| Ingress (single endpoint) | Yes |
| Existing certificates | Yes |
| Static pod restarts using existing configuration | Yes |
| etcd redundancy | No |
| Fencing of the surviving node | No |
| Cluster upgrades | No |
| etcd CA rotation | No |
| `MachineConfig` object changes that require a node reboot | No |
| Workloads or storage tied exclusively to the failed node | No |

Show more

#### [2.3.6. Prohibited operations during degraded TNF operation](#prohibited-operations-during-degraded-tnf-operation_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

You must not perform certain administrative operations while a two-node OpenShift cluster with fencing (TNF) is in a degraded state. Attempting these operations can leave the cluster in a state that is more difficult to recover from than the original degraded state.

Do not perform the following operations while the cluster is degraded:

Cluster upgrades
:   Do not initiate a cluster upgrade while the cluster is degraded. The upgrade process requires rolling out new configurations to both control plane nodes. With one node unavailable, configuration rollouts cannot complete. The cluster stalls in a partially upgraded state, which is more difficult to recover from than the original degraded state.

    Do not initiate any upgrade before restoring the second node. If you cannot restore the second node, replace it.

etcd certificate authority (CA) rotation
:   Do not initiate etcd CA rotation while the cluster is degraded. The etcd CA rotation requires distributing new trust bundles to both control plane nodes and converging a new static pod revision on each. With one node down, bundle distribution cannot complete and the revision cannot advance.

    As a result, a new signer CA may be created, but downstream certificates such as peer, serving, and client certificates are not regenerated by using the new CA. The cluster appears to have partially rotated, but the rotation is incomplete.

Warning

Do not delete the etcd signer secret while the cluster is degraded. Doing so triggers a new CA creation, but the downstream certificates cannot be regenerated. The `kube-apiserver` eventually loses trust in etcd, resulting in permanent control plane failure that cannot be recovered.

Certificate validity operations
:   Individual leaf certificate regeneration, for example an etcd serving certificate for the surviving node, does work during degraded operation because it uses the existing signer rather than a new one.

    Existing etcd certificates remain valid during degraded operation. Certificate validity periods are approximately five years for peer, serving certificates, and signer CA.

`MachineConfig` object updates
:   `MachineConfig` object changes that require a node reboot are not applied during degraded operation. The primary `MachineConfigPool` resource has a `maxUnavailable` setting, which defaults to `1`. The unavailable node already counts against this budget. Because the budget is fully consumed, the Machine Config Operator does not proceed with updates that might require draining and rebooting the surviving node. New `MachineConfig` resources are accepted, but the `MachineConfigPool` resource update does not progress.

    Queued `MachineConfig` object changes are applied after the second node is restored and the cluster exits degraded mode.

Pod disruption budget (PDB) enforcement
:   `PodDisruptionBudget` (PDB) enforcement continues during degraded operation. Eviction requests that might violate `minAvailable` or `maxUnavailable` policies are rejected. Administrative operations involving pod eviction, such as node drains, might be blocked.

    Do not bypass PDBs during degraded operation. Forcing evictions might remove the last running instance of critical services.

#### [2.3.7. Recovering a failed TNF node](#recovering-a-failed-tnf-node_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

Recovery is automatic when the failed node is powered on and rejoins the network. Degraded operation is a temporary state. Restore the failed node as soon as possible to regain fault tolerance, fencing protection, and the ability to perform upgrades and maintenance. If the original node cannot be recovered, replace it.

Important

A two-node OpenShift cluster with fencing (TNF) running on a single node indefinitely is at risk of experiencing the following issues:

* Complete cluster loss if the surviving node fails
* Inability to apply security updates or upgrades
* Certificate expiration if the cluster remains degraded beyond certificate validity periods

**Procedure**

1. Power on the failed node and verify network connectivity on all three network planes before the node can fully rejoin the cluster.

   * BMC or management network: Ensure that the peer node must reach the BMC address of the failed node. Without BMC connectivity, fencing cannot protect the cluster if a subsequent failure occurs.
   * Cluster network: Ensure that there is bilateral connectivity between nodes for Corosync membership (ports 5405 to 5407), Pacemaker management (port 2224), and etcd replication (ports 2379, 2380).
   * Kubernetes API: Ensure that the recovering node can reach the API server (port 6443).
2. Wait for Pacemaker to re-establish communication. Corosync detects the returning node and Pacemaker marks it as `ONLINE`. Pacemaker then starts managed resources, including kubelet and etcd, on the returning node.
3. Wait for etcd to re-join the cluster. The returning member first rejoins as a learner (non-voting), receives a data snapshot, and replicates the log from the surviving member. After it has caught up, it is promoted to a voting member, and the cluster returns to two-member quorum.

   Note

   This process typically takes about 15 to 25 minutes.
4. Verify that the node transitions to `Ready` status by running the following command:

   ```
   $ oc get nodes
   ```

**Verification**

1. Verify that cluster Operators have cleared their degraded conditions by running the following command:

   ```
   $ oc get co
   ```
2. After recovery, confirm the following conditions:

   * Both nodes show `Ready` status by running the following command:

     ```
     $ oc get nodes
     ```

     The output is similar to the following example:

     ```
     oc get nodes
     NAME                                                   STATUS   ROLES                         AGE    VERSION
     e920t-01.cluster1.metal-platform.eng.rdu2.redhat.com   Ready    control-plane,master,worker   5d1h   v1.35.4
     e920t-02.cluster1.metal-platform.eng.rdu2.redhat.com   Ready    control-plane,master,worker   5d1h   v1.35.4
     ```
   * Verify that the etcd Operator no longer reports `Degraded=True` by running the following command:

     ```
     $ oc get co etcd
     ```

     The output is similar to the following example:

     ```
     NAME   VERSION       AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
     etcd   4.22.0-rc.3   True        False         False      5d1h
     ```
   * Verify that both fencing devices are operational.
   * Queued MachineConfig changes, upgrades, and certificate rotations can proceed.

#### [2.3.8. Verifying TNF cluster state](#verifying-tnf-cluster-state_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

You can diagnose and resolve common issues during degraded operation of a Two-Node with Fencing (TNF) cluster by assessing the health of Pacemaker, etcd, and node status.

**Procedure**

1. Check Pacemaker status from the surviving node by running the following command:

   ```
   $ oc debug node/<surviving-node> -- chroot /host pcs status
   ```
2. Check etcd membership by running the following command:

   ```
   $ oc debug node/<surviving-node> -- chroot /host podman exec etcd etcdctl member list -w table
   ```
3. Check node status by running the following command:

   ```
   $ oc get nodes
   ```
4. Check cluster Operators by running the following command:

   ```
   $ oc get co
   ```

#### [2.3.9. Resolving a fencing failure in TNF](#resolving-a-fencing-failure-in-tnf_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

You must manually intervene when a cluster cannot automatically fence a failed node. Use the following procedure to safely power off the unresponsive hardware and clear the `UNCLEAN (offline)` state to allow the surviving node to resume cluster operations.

If the `pcs status` command shows the failed node as `UNCLEAN (offline)`, the automated fencing sequence did not succeed, and manual recovery is required.

**Procedure**

1. Verify that the failed node is powered off using the BMC console or physical inspection.
2. Confirm the fencing manually by running the following command:

   ```
   $ oc debug node/<surviving-node> -- chroot /host pcs stonith confirm <failed_node_name> --force
   ```

#### [2.3.10. Resolving etcd not recovering on the surviving node](#resolving-etcd-not-recovering-on-the-surviving-node_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

If the surviving node does not automatically restart etcd after a successful fencing operation, reset the resource state to restore service. .Prerequisites

* Ensure that you run the following `oc debug` commands in the two-node OpenShift cluster with fencing (TNF).

**Procedure**

1. Clean up the etcd resource by running the following command:

   ```
   $ oc debug node/<surviving_node> -- chroot /host bash -c '
     pcs resource cleanup etcd
   '
   ```

   The output is similar to the following example:

   **Example**

   ```
   sudo  pcs resource cleanup etcd
   +
   Cleaned up etcd:0 on e920t-02.cluster1.metal-platform.eng.rdu2.redhat.com
   +
   Cleaned up etcd:1 on e920t-01.cluster1.metal-platform.eng.rdu2.redhat.com
   +
   Waiting for 1 reply from the controller
   +
   ... got reply (done)
   ```
2. Verify Pacemaker status by running the following command:

   ```
   $ oc debug node/<surviving_node> -- chroot /host bash -c ' \
     pcs status
   '
   ```

   The output is similar to the following example:

   ```
   Cluster name: TNF
   +
   Cluster Summary:
   +
   Stack: corosync (Pacemaker is running)
   +
   Current DC: e920t-02.cluster1.metal-platform.eng.rdu2.redhat.com (version 2.1.10-2.el9-5693eaeee) - partition with quorum
   +
   Last updated: Wed May 20 17:36:23 2026 on e920t-01.cluster1.metal-platform.eng.rdu2.redhat.com
   +
   Last change:  Wed May 20 17:36:22 2026 by root via root on e920t-01.cluster1.metal-platform.eng.rdu2.redhat.com
   +
   2 nodes configured
   +
   6 resource instances configured
   +
   Node List:
   +
   Online: [ e920t-01.cluster1.metal-platform.eng.rdu2.redhat.com e920t-02.cluster1.metal-platform.eng.rdu2.redhat.com ]
   +
   Full List of Resources:
   +
   Clone Set: kubelet-clone [kubelet]:
   +
   Started: [ e920t-01.cluster1.metal-platform.eng.rdu2.redhat.com e920t-02.cluster1.metal-platform.eng.rdu2.redhat.com ]
   +
   e920t-01.cluster1.metal-platform.eng.rdu2.redhat.com_redfish	(stonith:fence_redfish):	 Started e920t-02.cluster1.metal-platform.eng.rdu2.redhat.com
   +
   e920t-02.cluster1.metal-platform.eng.rdu2.redhat.com_redfish	(stonith:fence_redfish):	 Started e920t-02.cluster1.metal-platform.eng.rdu2.redhat.com
   +
   Clone Set: etcd-clone [etcd]:
   +
   Started: [ e920t-01.cluster1.metal-platform.eng.rdu2.redhat.com e920t-02.cluster1.metal-platform.eng.rdu2.redhat.com ]
   +
   Failed Resource Actions:
   +
   e920t-01.cluster1.metal-platform.eng.rdu2.redhat.com_redfish 1m-interval monitor on e920t-02.cluster1.metal-platform.eng.rdu2.redhat.com could not be executed (Timed Out: Fence agent did not complete within 20s) at Sun May 17 12:50:32 2026 after 20.003s
   +
   Daemon Status:
   +
   corosync: active/enabled
   +
   pacemaker: active/enabled
   +
   pcsd: active/enabled
   ```

#### [2.3.11. Resolving a failed node not rejoining after power-on](#resolving-a-failed-node-not-rejoining-after-power-on_operating-a-degraded-tnf) Copy linkLink copied to clipboard!

If the failed node does not rejoin the cluster after being powered on, verify Corosync connectivity and service health.

**Procedure**

1. Verify Corosync and cluster service status on the returning node by running the following command:

   ```
   $ oc debug node/<returning-node> -- chroot /host bash -c '\
     corosync-cfgtool -s\
     systemctl status corosync pacemaker pcsd
   '
   ```
2. Verify network connectivity between both nodes.

   * For a Cluster Network (Corosync), ping an adjacent node to check the peer node on the cluster network by running the following command:

     ```
     $ ping -c 3 <peer_node_ip>
     ```
   * For a Management or BMC Network (Fencing Path), run the following command:

     ```
     $ ping -c 3
     ```

     The output is similar to the following example:

     ```
     HTTP_CODE: 401
     TIME_TOTAL: 0.224628s
     TIME_CONNECT: 0.000322s
     ```

     Note

     The `HTTP 401` code is expected because the curl command does not pass credentials (no --user Administrator:password). It confirms the Redfish API is listening and rejecting unauthenticated requests.

     TIME\_CONNECT value is approximately 0.322ms which shows the fast connectivity.
   * For an Application Network (OpenShift/etcd), perform the following tasks:

     + Check API server health on the local node by running the following command:

       ```
       $ curl -sk https://localhost:6443/healthz
       ```
     + Check API server health on the peer node by running the following command:

       ```
       $ curl -sk https://<peer-node-ip>:6443/healthz
       ```
     + List etcd cluster members by running the following command:

       ```
       $ podman exec etcd etcdctl member list --write-out=table
       ```
     + Check etcd endpoint health across the cluster by running the following command:

       ```
       $ podman exec etcd etcdctl endpoint health --cluster
       ```

### [2.4. Post-installation troubleshooting and recovery](#installing-post-tnf) Copy linkLink copied to clipboard!

You can troubleshoot and restore a two-node OpenShift Container Platform cluster with fencing (TNF) after a disruption event. Manually recover services when automated recovery is unavailable, replace degraded control plane nodes, and use the `fencing_validator` script to verify cluster health.

#### [2.4.1. Manually recovering from a disruption event when automated recovery is unavailable](#installation-manual-recovering-when-auto-recovery-is-unavail_install-post-tnf) Copy linkLink copied to clipboard!

You might need to perform manual recovery steps if a disruption event prevents fencing from functioning correctly. In this case, you can run commands directly on the control plane nodes to recover the cluster. There are five main recovery scenarios, which should be attempted in the following order:

1. Update fencing secrets: Refresh the Baseboard Management Console (BMC) credentials if they are incorrect or outdated.
2. Recover from a single-node failure: Restore functionality when only one control plane node is down.
3. Recover from dual node power loss: Restore functionality when both control plane nodes are down and can be restarted.
4. Restore corosync quorum after dual node power loss: Restore corosync quorum when both control plane nodes lost power but only one node can be restarted.
5. Replace a control plane node that cannot be recovered: Replace the node to restore cluster functionality.

**Prerequisites**

* You have administrative access to the control plane nodes.
* You can connect to the nodes by using SSH.

**Procedure**

1. Update the fencing secrets:

   1. If the Cluster API is unavailable, update the fencing secret by running the following command on one of the cluster nodes:

      ```
      $ sudo pcs stonith update <node_name>_redfish username=<user_name> password=<password>
      ```

      After the Cluster API recovers, or if the Cluster API is already available, update the fencing secret in the cluster to ensure it stays in sync, as described in the following step.
   2. Edit the username and password for the existing fencing secret for the control plane node by running the following commands:

      ```
      $ oc project openshift-etcd
      ```

      ```
      $ oc edit secret <node_name>-fencing
      $ oc edit secret fencing-credentials-<node_name>
      ```

      The secret contains the following data keys:

      Expand

      Table 2.6. Data keys

      | Key | Description | Changes during credential rotation? |
      | --- | --- | --- |
      | `username` | BMC username | Yes |
      | `password` | BMC password | Yes |
      | `address` | Full Redfish URL (for example, `redfish+https://192.168.1.10:443/redfish/v1/Systems/1`) | Only if BMC address changed |
      | `certificateVerification` | `Disabled` or `Enabled` | Only if TLS settings changed |

      Show more

      Note

      The `oc edit secret` command displays base64-encoded values. If you modify any of the values, the new values must also be base64-encoded.

      Alternatively, you can use the following command to create or update the secret with literal strings:

      ```
      $ oc create secret generic fencing-credentials-<node_name> \
        --from-literal=address='<redfish_address>' \
        --from-literal=username='<new_username>' \
        --from-literal=password='<new_password>' \
        --from-literal=certificateVerification='<Disabled_or_Enabled>' \
        --dry-run=client -o yaml | oc apply -f -
      ```

      All four keys must be present. The cluster etcd Operator rejects secrets with missing keys.
   3. Verify that the new credentials can reach the BMC by running the following command:

      ```
      $ sudo pcs stonith config <node_name>_redfish
      ```
   4. Verify that no STONITH resources are blocked by running the following command:

      ```
      $ sudo pcs status --full
      ```

      The cluster etcd Operator performs this validation automatically when it applies credentials from the secret by using the following command:

      ```
      $ fence_redfish --action status
      ```

      If the cluster recovers after updating the fencing secrets, no further action is required. If the issue persists, proceed to the next step.
2. Recover from a single-node failure:

   1. Gather initial diagnostics by running the following command:

      ```
      $ sudo pcs status --full
      ```

      This command provides a detailed view of the current cluster and resource states. You can use the output to identify issues with fencing or etcd startup.
   2. Run the following additional diagnostic commands, if necessary:

      Reset the resources on your cluster by running the following command:

      ```
      $ sudo pcs resource cleanup
      ```
   3. Review all Pacemaker activity on the node by running the following command:

      ```
      $ sudo journalctl -u pacemaker
      ```
   4. Diagnose etcd resource startup issues by running the following command:

      ```
      $ sudo journalctl -u pacemaker | grep podman-etcd
      ```
   5. View the fencing configuration for the node by running the following command:

      ```
      $ sudo pcs stonith config <node_name>_redfish
      ```

      If fencing is required but is not functioning, ensure that the Redfish fencing endpoint is accessible and verify that the credentials are correct.

      If you have verified the failed node is permanently inaccessible but automated fencing cannot function, verify the failed node meets ALL of the following conditions:

      * The node is powered off and cannot be restarted.
      * The node cannot access any shared storage or cluster resources.
      * The node is completely isolated from the cluster network.
   6. Confirm the node is fenced by running the following command:

      ```
      $ sudo pcs stonith confirm <failed_node_name>
      ```

      Warning

      If the failed node is accessible or can access shared resources, confirming fencing can cause data corruption and cluster failure.
   7. If etcd is not starting despite fencing being operational, restore etcd from a backup by running the following commands:

      ```
      $ sudo cp -r /var/lib/etcd-backup/* /var/lib/etcd/
      ```

      ```
      $ sudo chown -R etcd:etcd /var/lib/etcd
      ```

      If the recovery is successful, no further action is required. If the issue persists, proceed to the next step.
3. Recover from dual node power loss where both nodes are recoverable:

   This procedure applies when both control plane nodes lost power and both nodes can be restarted. If only one node can be restarted, proceed to step 4.

   1. Power on both control plane nodes.

      Pacemaker starts automatically and begins the recovery operation when it detects both nodes are online. If the recovery does not start as expected, use the diagnostic commands described in the previous step to investigate the issue.
   2. Reset the resources on your cluster and instruct Pacemaker to attempt to start them fresh by running the following command:

      ```
      $ sudo pcs resource cleanup
      ```
   3. Check resource start order by running the following command:

      ```
      $ sudo pcs status --full
      ```
   4. Inspect the pacemaker service journal if kubelet fails by running the following commands:

      ```
      $ sudo journalctl -u pacemaker
      ```

      ```
      $ sudo journalctl -u kubelet
      ```
   5. Handle out-of-sync etcd.

      If one node has a more up-to-date etcd, Pacemaker attempts to fence the lagging node and start it as a learner. If this process stalls, verify the Redfish fencing endpoint and credentials by running the following command:

      ```
      $ sudo pcs stonith config
      ```

      If the recovery is successful, no further action is required. If the issue persists, perform manual recovery as described in the next step.
4. Restore corosync quorum after dual node power loss (single node recoverable):

   This procedure applies when both control plane nodes lost power and only one node can be restarted. In this scenario, the cluster has lost corosync quorum because the last known state showed both nodes were online before the power loss.

   Important

   Perform this procedure only when both of the following conditions are met:

   * Both control plane nodes lost power
   * Only one control plane node can be restarted

   This scenario typically occurs when you need to replace a control plane node (one node is not recoverable) and the surviving node lost power before the replacement procedure.

   1. Verify that only one node is online by running the following command on the surviving node:

      ```
      $ sudo pcs status --full
      ```

      The output shows only one node online. The sample output is as follows:

      ```
      Cluster name: TNF
      Cluster Summary:
        * Stack: corosync (Pacemaker is running)
        * Current DC: NONE
        * Last updated: Wed Apr 29 16:21:17 2026 on master-0.ostest.test.metalkube.org
        * Last change:  Wed Apr 29 16:19:25 2026 by root via root on master-1.ostest.test.metalkube.org
        * 2 nodes configured
        * 6 resource instances configured

      Node List:
        * Node master-0.ostest.test.metalkube.org (1): UNCLEAN (offline)
        * Node master-1.ostest.test.metalkube.org (2): UNCLEAN (offline)

      Full List of Resources:
        * Clone Set: kubelet-clone [kubelet]:
          * kubelet	(systemd:kubelet):	 Stopped
          * kubelet	(systemd:kubelet):	 Stopped
        * master-0.ostest.test.metalkube.org_redfish	(stonith:fence_redfish):	 Stopped
        * master-1.ostest.test.metalkube.org_redfish	(stonith:fence_redfish):	 Stopped
        * Clone Set: etcd-clone [etcd]:
          * etcd	(ocf:heartbeat:podman-etcd):	 Stopped
          * etcd	(ocf:heartbeat:podman-etcd):	 Stopped

      Tickets:

      PCSD Status:
        master-0.ostest.test.metalkube.org: Online
        master-1.ostest.test.metalkube.org: Offline

      Daemon Status:
        corosync: active/enabled
        pacemaker: active/enabled
        pcsd: active/enabled
      ```

      The PCSD status shows that the master-0 node is Online, and the other is offline. BOTH nodes in the node list section are offline because neither has quorum.

      ```
      [core@master-0 ~]$   sudo pcs quorum status --debug
      Running: /usr/sbin/corosync-quorumtool -p
      Environment:
        LC_ALL=C

      Finished running: /usr/sbin/corosync-quorumtool -p
      Return value: 2
      --Debug Stdout Start--
      Quorum information
      ------------------
      Date:             Wed Apr 29 16:25:55 2026
      Quorum provider:  corosync_votequorum
      Nodes:            1
      Node ID:          1
      Ring ID:          1.e
      Quorate:          No

      Votequorum information
      ----------------------
      Expected votes:   2
      Highest expected: 2
      Total votes:      1
      Quorum:           1 Activity blocked
      Flags:            2Node WaitForAll

      Membership information
      ----------------------
          Nodeid      Votes    Qdevice Name
               1          1         NR master-0.ostest.test.metalkube.org (local)

      --Debug Stdout End--
      --Debug Stderr Start--

      --Debug Stderr End--

      Error: Unable to get quorum status:
      ```
   2. Verify that the failed node is permanently inaccessible before proceeding.

      Before confirming to Pacemaker that the failed node is fenced, you must ensure that the failed node meets ALL of the following conditions:

      * The node is powered off and cannot be restarted
      * The node cannot access any shared storage or cluster resources
      * The node is completely isolated from the cluster network

        If the failed node is accessible or can access shared resources, DO NOT proceed with this step. Confirming fencing for a node that is still active can cause data corruption and cluster failure.
   3. Confirm to Pacemaker that the failed node is fenced by running the following command:

      ```
      $ sudo pcs quorum unblock
      ```

      The command shows the following sample output:

      ```
      WARNING: If node 'master-1' is not powered off or it does have access to shared resources, data corruption and/or cluster failure may occur
      Type 'yes' or 'y' to proceed, anything else to cancel:
      ```

      Replace <failed\_node\_name> with the name of the failed control plane node (for example, control-plane-1).
   4. Verify that quorum is restored by running the following command:

      ```
      $ sudo pcs quorum status
      ```

      The command shows the following sample output:

      **Example output**

      ```
      Quorum information
      ------------------
      Date:             Fri Oct  3 14:15:31 2025
      Quorum provider:  corosync_votequorum
      Nodes:            1
      Node ID:          1
      Ring ID:          1.16
      Quorate:          Yes

      Votequorum information
      ----------------------
      Expected votes:   2
      Highest expected: 2
      Total votes:      1
      Quorum:           1
      Flags:            2Node Quorate
      ```
   5. Wait 30 seconds for Pacemaker to process the fencing confirmation and begin recovery.
   6. Verify that etcd is running on the surviving node by running the following command:

      ```
      $ sudo pcs resource status etcd
      ```

      If etcd is not running, restart it by running the following command:

      ```
      $ sudo pcs resource cleanup etcd
      ```

      Wait up to 5 minutes for etcd to start. Check the status periodically by running the following command:

      ```
      $ sudo pcs resource status etcd
      ```

      The command shows that the `podman-etcd` resource is started. If the container is started successfully, you can see the logs by running the following command:

      ```
      $ sudo podman logs etcd
      ```

      If the container is not started, you can see the logs by running the following command:

      ```
      $ journalctl -u pacemaker | grep podman-etcd
      ```

      The relevant logs are placed at `/var/log/paceamaker/pacemaker.log`. The output must show that etcd is started on the surviving node.

      After restoring corosync quorum and confirming etcd is running, proceed to step 5 to replace the failed control plane node.
5. If you need to manually recover from an event when one of the nodes is not recoverable, follow the procedure in "Replacing control plane nodes in a two-node OpenShift cluster".

   When a cluster loses a single node, it enters degraded mode. In this state, Pacemaker automatically unblocks quorum and allows the cluster to temporarily operate on the remaining node.

   If both nodes fail and both can be restarted, Pacemaker reestablishes quorum automatically when both nodes are online.

   If only one node can be restarted, proceed to step 4 to restore corosync quorum manually.

   If manual recovery is still required and it fails, collect a must-gather and sosreport, and file a bug.

**Verification**

For information about verifying that both control plane nodes and etcd are operating correctly, see "Verifying etcd health in a two-node OpenShift cluster with fencing".

#### [2.4.2. Replacing control plane nodes in a two-node OpenShift cluster with fencing](#installation-replacing-control-plane-nodes_install-post-tnf) Copy linkLink copied to clipboard!

You can replace a failed control plane node in a two-node OpenShift cluster. The replacement node must use the same host name and IP address as the failed node.

**Prerequisites**

* You have a functioning survivor control plane node.
* You have verified that either the machine is not running or the node is not ready.
* You have access to the cluster as a user with the `cluster-admin` role.
* You know the host name and IP address of the failed node.

Note

Do an etcd backup before proceeding to ensure that you can restore the cluster if any issues occur.

**Procedure**

1. Check the quorum state by running the following command:

   ```
   $ sudo pcs quorum status
   ```

   **Example output**

   ```
   Quorum information
   ------------------
   Date:             Fri Oct  3 14:15:31 2025
   Quorum provider:  corosync_votequorum
   Nodes:            2
   Node ID:          1
   Ring ID:          1.16
   Quorate:          Yes

   Votequorum information
   ----------------------
   Expected votes:   2
   Highest expected: 2
   Total votes:      2
   Quorum:           1
   Flags:            2Node Quorate WaitForAll

   Membership information
   ----------------------
       Nodeid      Votes    Qdevice Name
            1          1         NR master-0 (local)
            2          1         NR master-1
   ```

   1. If quorum is lost and one control plane node is still running, restore quorum manually on the survivor node by running the following command:

      ```
      $ sudo pcs quorum unblock
      ```
   2. If only one node failed, verify that etcd is running on the survivor node by running the following command:

      ```
      $ sudo pcs resource status etcd
      ```
   3. If etcd is not running, restart etcd by running the following command:

      ```
      $ sudo pcs resource cleanup etcd
      ```

      If etcd still does not start, force it manually on the survivor node, skipping fencing:

      Important

      Before running this commands, ensure that the node being replaced is inaccessible. Otherwise, you risk etcd corruption.

      ```
      $ sudo pcs resource debug-stop etcd
      ```

      ```
      $ sudo OCF_RESKEY_CRM_meta_notify_start_resource='etcd' pcs resource debug-start etcd
      ```

      After recovery, etcd must be running successfully on the survivor node.
2. Delete etcd secrets for the failed node by running the following commands:

   ```
   $ oc project openshift-etcd
   ```

   ```
   $ oc delete secret etcd-peer-<node_name>
   ```

   ```
   $ oc delete secret etcd-serving-<node_name>
   ```

   ```
   $ oc delete secret etcd-serving-metrics-<node_name>
   ```

   Note

   To replace the failed node, you must delete its etcd secrets first. When etcd is running, it might take some time for the API server to respond to these commands.
3. Delete resources for the failed node:

   1. If you have the `BareMetalHost` (BMH) objects, list them to identify the host you are replacing by running the following command:

      ```
      $ oc get bmh -n openshift-machine-api
      ```
   2. Delete the BMH object for the failed node by running the following command:

      ```
      $ oc delete bmh/<bmh_name> -n openshift-machine-api
      ```
   3. List the `Machine` objects to identify the object that maps to the node that you are replacing by running the following command:

      ```
      $ oc get machines.machine.openshift.io -n openshift-machine-api
      ```
   4. Get the label with the machine hash value from the `Machine` object by running the following command:

      ```
      $ oc get machines.machine.openshift.io/<machine_name> -n openshift-machine-api \
        -o jsonpath='Machine hash label: {.metadata.labels.machine\.openshift\.io/cluster-api-cluster}{"\n"}'
      ```

      Replace `<machine_name>` with the name of a `Machine` object in your cluster. For example, `ostest-bfs7w-ctrlplane-0`.

      You need this label to provision a new `Machine` object.
   5. Delete the `Machine` object for the failed node by running the following command:

      ```
      $ oc delete machines.machine.openshift.io/<machine_name>-<failed nodename> -n openshift-machine-api
      ```

      Note

      The node object is deleted automatically after deleting the `Machine` object.
4. Recreate the failed host by using the same name and IP address:

   Important

   You must perform this step only if you are using installer-provisioned infrastructure or the Machine API to create the original node. For information about replacing a failed bare-metal control plane node, see "Replacing an unhealthy etcd member on bare metal".

   1. Remove the BMH and `Machine` objects. The machine controller automatically deletes the node object.
   2. Provision a new machine by using the following sample configuration:

      **Example `Machine` object configuration**

      ```
      apiVersion: machine.openshift.io/v1beta1
      kind: Machine
      metadata:
        annotations:
          metal3.io/BareMetalHost: openshift-machine-api/{bmh_name}
        finalizers:
        - machine.machine.openshift.io
        labels:
          machine.openshift.io/cluster-api-cluster: {machine_hash_label}
          machine.openshift.io/cluster-api-machine-role: master
          machine.openshift.io/cluster-api-machine-type: master
        name: {machine_name}
        namespace: openshift-machine-api
      spec:
        authoritativeAPI: MachineAPI
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
      ```

      * `metadata.annotations.metal3.io/BareMetalHost`: Replace `{bmh_name}` with the name of the BMH object that is associated with the host that you are replacing.
      * `labels.machine.openshift.io/cluster-api-cluster`: Replace `{machine_hash_label}` with the label that you fetched from the machine you deleted.
      * `metadata.name`: Replace `{machine_name}` with the name of the machine you deleted.
   3. Create the new BMH object and the secret to store the BMC credentials by running the following command:

      ```
      cat <<EOF | oc apply -f -
      apiVersion: v1
      kind: Secret
      metadata:
        name: <secret_name>
        namespace: openshift-machine-api
      data:
        password: <password>
        username: <username>
      type: Opaque
      ---
      apiVersion: metal3.io/v1alpha1
      kind: BareMetalHost
      metadata:
        name: {bmh_name}
        namespace: openshift-machine-api
      spec:
        automatedCleaningMode: disabled
        bmc:
          address: <redfish_url>/{uuid}
          credentialsName: <name>
          disableCertificateVerification: true
        bootMACAddress: {boot_mac_address}
        bootMode: UEFI
        externallyProvisioned: false
        online: true
        rootDeviceHints:
          deviceName: /dev/disk/by-id/scsi-<serial_number>
        userData:
          name: master-user-data-managed
          namespace: openshift-machine-api
      EOF
      ```

      * `metadata.name`: Specify the name of the secret.
      * `metadata.name`: Replace `{bmh_name}` with the name of the BMH object that you deleted.
      * `bmc.address`: Replace `{uuid}` with the UUID of the node that you created.
      * `bmc.credentialsName`: Replace `name` with the name of the secret that you created.
      * `bootMACAddress`: Specify the MAC address of the provisioning network interface. This is the MAC address the node uses to identify itself when communicating with Ironic during provisioning.
5. Verify that the new node has reached the `Provisioned` state by running the following command:

   ```
   $ oc get bmh -o wide
   ```

   The value of the `STATUS` column in the output of this command must be `Provisioned`.

   Note

   The provisioning process can take 10 to 20 minutes to complete.
6. Verify that both control plane nodes are in the `Ready` state by running the following command:

   ```
   $ oc get nodes
   ```

   The value of the `STATUS` column in the output of this command must be `Ready` for both nodes.
7. Apply the `detached` annotation to the BMH object to prevent the Machine API from managing it by running the following command:

   ```
   $ oc annotate bmh <bmh_name> -n openshift-machine-api baremetalhost.metal3.io/detached='' --overwrite
   ```
8. Rejoin the replacement node to the pacemaker cluster by running the following command:

   Note

   Run the following command on the survivor control plane node, not the node being replaced.

   ```
   $ sudo pcs cluster node remove <node_name>
   ```

   ```
   $ sudo pcs cluster node add <node_name> addr=<node_ip> --start --enable
   ```
9. Delete stale jobs for the failed node by running the following command:

   ```
   $ oc project openshift-etcd
   ```

   ```
   $ oc delete job tnf-auth-job-<node_name>
   ```

   ```
   $ oc delete job tnf-after-setup-job-<node_name>
   ```

**Verification**

For information about verifying that both control plane nodes and etcd are operating correctly, see "Verifying etcd health in a two-node OpenShift cluster with fencing".

#### [2.4.3. Verifying etcd health in a two-node OpenShift cluster with fencing](#installation-verifying-etcd-health_install-post-tnf) Copy linkLink copied to clipboard!

After completing node recovery or maintenance procedures, verify that both control plane nodes and etcd are operating correctly.

**Prerequisites**

* You have access to the cluster as a user with `cluster-admin` privileges.
* You can access at least one control plane node through SSH.

**Procedure**

1. Check the overall node status by running the following command:

   ```
   $ oc get nodes
   ```

   This command verifies that both control plane nodes are in the `Ready` state, indicating that they can receive workloads for scheduling.
2. Verify the status of the `cluster-etcd-operator` by running the following command:

   ```
   $ oc describe co/etcd
   ```

   The `cluster-etcd-operator` manages and reports on the health of your etcd setup. Reviewing its status helps you identify any ongoing issues or degraded conditions.
3. Review the etcd member list by running the following command:

   ```
   $ oc rsh -n openshift-etcd <etcd_pod> etcdctl member list -w table
   ```

   This command shows the current etcd members and their roles. Look for any nodes marked as `learner`, which indicates that they are in the process of becoming voting members.
4. Review the Pacemaker resource status by running the following command on either control plane node:

   ```
   $ sudo pcs status --full
   ```

   This command provides a detailed overview of all resources managed by Pacemaker. You must ensure that the following conditions are met:

   * Both nodes are online.
   * The `kubelet` and `etcd` resources are running.
   * Fencing is correctly configured for both nodes.

#### [2.4.4. Fencing validator script overview](#fencing-validator-script-overview_install-post-tnf) Copy linkLink copied to clipboard!

A two-node OpenShift Container Platform cluster with fencing (TNF) relies on the Shoot The Other Node In The Head (STONITH) mechanism to ensure data integrity during node failures. If the fencing subsystem is misconfigured, the cluster might fail to recover safely, resulting in data corruption or a split-brain scenario.

Before the introduction of this utility, administrators or support engineers had to manually verify several subsystems, including:

* Pacemaker status
* STONITH device configurations
* Daemon health
* etcd quorum
* Fencing secrets

The `fencing_validator` script automates these manual checks into a single command, providing clear pass or fail results and descriptive error messages to reduce troubleshooting time and human error.

The `fencing_validator` is a Bash-based diagnostic utility available on every control-plane node in a TNF OpenShift Container Platform cluster. As a health check tool for the fencing subsystem, it verifies that the STONITH stack is correctly configured and operational.

The script is located at `/usr/local/bin/fencing_validator` on both control-plane nodes. The script is automatically installed by the Machine Config Operator (MCO). There is no manual installation step required.

When you deploy a TNF cluster, the MCO renders a set of `MachineConfig` manifests specific to that topology. One of these manifests is `fencing-validator.yaml`, located in the MCO source at `templates/master/00-master/two-node-with-fencing/files/fencing-validator.yaml`. This `MachineConfig` writes the script to `/usr/local/bin/fencing_validator` with executable mode `0755` on every control-plane node. The script is available as soon as the node has finished applying its `MachineConfig`, that is, after initial deployment or after any MCO-driven reboot.

Important

The script is deployed on TNF clusters only. It does not appear on standard HA clusters, Single-node OpenShift, or Two-Node with Arbiter clusters.

You can use the script for the following:

* Post-deployment validation: Use the utility to verify that the TNF configuration is correct and fully functional after deployment.
* Troubleshooting: Identify the specific underlying issues when a TNF setup fails to operate as expected.
* Pre-upgrade validation: Confirm the health of the fencing stack to ensure the cluster is stable enough to proceed with a version upgrade.
* Support interactions: Execute the script and provide the output to support engineers to facilitate the rapid resolution of technical issues.

##### [2.4.4.1. Fencing validator script prerequisites](#fencing-validator-script-prerequisites_install-post-tnf) Copy linkLink copied to clipboard!

Use the `fencing_validator` script to verify your fencing configuration on a two-node OpenShift Container Platform cluster. This script, deployed automatically by the Machine Config Operator, ensures that power management interfaces are correctly configured to prevent data corruption during a node failure. To run it, ensure the `jq` utility is installed, and you have both Kubernetes API access (`oc`) and SSH access to the control-plane nodes.

You can see what the script would do without actually performing any validation for TNF by running the following command:

```
$ oc debug node/<node_name> --chroot /host /usr/local/bin/fencing_validator --dry-run
```

##### [2.4.4.2. Command-line options for fencing validator script](#command-line-options-for-fencing-validator-script_install-post-tnf) Copy linkLink copied to clipboard!

To quickly verify a high-availability configuration of your two-node OpenShift Container Platform cluster with fencing (TNF), you can review the available command-line options and environment variables for the `fencing_validator` script. This reference helps you customize your connection methods, set execution timeouts, and safely test node reboots to ensure your fencing mechanism is reliable before moving to production.

You can see different command-line options for the `fencing_ validator` script by running the following command:

```
$ oc debug node/<node_name> --chroot /host /usr/local/bin/fencing_validator --help
```

The following table details command-line options for the `oc debug node` command:

Expand

| Flag | Description |
| --- | --- |
| `--user` | SSH username for remote node access. The default value is `core`. Optionally, you can use `SSH_USER` environment variable to set the value. |
| `--ssh-key` | Path to SSH private key. Optionally, you can use the `SSH_KEY` environment variable to set the value. |
| `--kubeconfig` | Path to kubeconfig file. Optionally, you can use the `KUBECONFIG` environment variable to set the value. |
| `--transport` | How the script connects to the other node. The possible values are `auto`, `ssh`, and `ocdebug`. The default value is `auto`. Optionally, you can use the `TRANSPORT` environment variable to set the value. For more information, see "Transport mode for fencing validator script". |
| `--timeout` | Maximum wait time for recovery loops. Optionally, you can use the `TIMEOUT` environment variable to set the value. By default, it is 1200 seconds or 20 minutes. |
| `--hosts` | Comma-separated pair of node hostnames or IP addresses. |
| `--host-a` | Explicitly set the first node. |
| `--host-b` | Explicitly set the second node. |
| `--disruptive` | Enable destructive fencing tests (reboots nodes). Optionally, you can use the `DISRUPTIVE` environment variable to set the value. |
| `--dry-run` | Show what could be the result of the `fencing_validator` script without doing actual validations. Optionally, you can use the `DRY_RUN` environment variable to set the value. |
| `-h`, `--help` | Show usage information. |

Show more

You can set all the flags by using the following environment variables:

* `IP_A / IP_B`: set host addresses directly
* `OC_BIN`: custom `oc` binary path
* `OC_REQ_TIMEOUT`: per-API-call timeout. The default value is 10 seconds.
* `CMD_EXEC_TIMEOUT_SECS`: per-command timeout. The default value is 60 seconds.

##### [2.4.4.3. Fencing validator script for non-disruptive checks](#fencing-validator-script-for-non-disruptive-checks_install-post-tnf) Copy linkLink copied to clipboard!

To ensure your two-node OpenShift Container Platform cluster with fencing (TNF) remains highly available without risking downtime, you can run the `fencing_validator` script in validation mode. This script performs a series of read-only health checks to verify cluster quorum, daemon health, and STONITH device status without disrupting active services.

The simplest way to run the script is from a debug session on either control plane node by running the following command:

```
$ oc debug node/<node_name> --chroot /host /usr/local/bin/fencing_validator
```

This command does not reboot or fence any nodes. These checks are read-only and safe to run at any time. They run the following non-disruptive checks and report the results:

1. **OpenShift version check** - Confirms the cluster is running OpenShift Container Platform 4.20.0 or later.
2. **Node count check** - Confirms exactly 2 control-plane nodes exist.
3. **Transport connectivity** - Establishes a connection to both nodes (via SSH or `oc debug`).
4. **STONITH device check** - Verifies that STONITH devices are present and enabled in Pacemaker.
5. **Pacemaker status** - Confirms both nodes are reporting ONLINE in the Pacemaker cluster.
6. **Daemon health** - Checks that `corosync`, `pacemaker`, and `pcsd` services are active on both nodes.
7. **etcd quorum** - Verifies that etcd has 2 healthy voting members and the cluster has quorum.
8. **Fencing secrets** - Confirms that the fencing credential secrets (used by STONITH to authenticate to the BMC/IPMI) exist and are correctly bound to each node.

   When all non-disruptive checks pass, the output resembles the following:

```
[INFO]
====
OpenShift version: 4.20.0 - OK [INFO]  Detected 2 control-plane nodes [INFO]  Transport: ssh [OK]    STONITH devices found and enabled [OK]    Both nodes ONLINE in Pacemaker [OK]    All daemons healthy on both nodes [OK]    etcd quorum healthy (2/2 voters) [OK]    Fencing secrets correctly bound [INFO]  All non-disruptive checks passed When something fails:
====
```

+ When non-disruptive checks fail, the output resembles the following:

```
[INFO]
====
OpenShift version: 4.20.0 - OK [INFO]  Detected 2 control-plane nodes [INFO]  Transport: ssh [ERROR] No STONITH devices found - fencing is not configured
====
```

##### [2.4.4.4. Fencing validator script for disruptive checks](#fencing-validator-script-for-disruptive-checks_install-post-tnf) Copy linkLink copied to clipboard!

You can validate your cluster’s resilience and perform disruptive checks from a peer node by using the `fencing_validator` script. By executing these simulated failures, you can ensure your high-availability environment correctly isolates and recovers from errors.

You can trigger the Shoot The Other Node In The Head (STONITH) action for the failed node and cut off its access to shared resources and prevent data corruption by running the following command:

```
$ pcs stonith fence <node>
```

You can check whether a two-node OpenShift Container Platform cluster with fencing (TNF) setup actually works by running the following command:

```
$ oc debug node/<node_name> --chroot /host /usr/local/bin/fencing_validator --disruptive
```

Warning

The `--disruptive` flag fences each control plane node one at a time and verifies recovery. The `--disruptive` flag performs the STONITH fence operations such as power cycle or VM reset. It does not perform graceful shutdown, and causes temporary workload disruption.

The fencing validator script with `--disruptive` flag runs the following checks:

1. **Fence Node A** - Triggers STONITH to reboot the first control-plane node.
2. **Verify NotReady** - Waits for Kubernetes to report the node A as `NotReady`, which confirms the reboot happened.
3. **Verify recovery** - Waits for the node A to come back to the `Ready` state, rejoin the Pacemaker cluster as `ONLINE`, and for etcd to regain quorum.
4. **Post-recovery daemon check** - Re-checks all daemons are healthy after recovery.
5. **Fence Node B** - Triggers STONITH to reboot the second node.
6. . **Verify NotReady** - Waits for Kubernetes to report the node B as `NotReady`, which confirms the reboot happened.
7. **Verify recovery** - Waits for the node B to come back to the `Ready` state, rejoin the Pacemaker cluster as `ONLINE`, and for etcd to regain quorum.
8. **Post-recovery daemon check** - Re-checks all daemons are healthy after recovery.

##### [2.4.4.5. Exit codes for fencing-validator script](#exit-codes-for-fencing-validator-script_install-post-tnf) Copy linkLink copied to clipboard!

The `fencing_validator` script uses specific exit codes so automation and support tooling can programmatically determine what went wrong.

The following table lists the specific exit codes that the `fencing_validator` script returns, mapping each numerical value to its corresponding diagnostic state to assist with automated troubleshooting.

Expand

| Exit code | Description |
| --- | --- |
| 0 | All checks passed |
| 1 | Generic or unexpected failure |
| 20 | STONITH devices are missing or not enabled |
| 21 | One or both nodes are not ONLINE in Pacemaker |
| 22 | One or more required daemons (corosync, pacemaker, pcsd) are not running |
| 23 | etcd does not have quorum or not all members are healthy |
| 26 | Fencing secrets are missing or do not match the expected nodes |

Show more

##### [2.4.4.6. Transport mode for fencing validator script](#transport-mode-for-fencing-validator-script_install-post-tnf) Copy linkLink copied to clipboard!

The `fencing_validator` script connects to control-plane nodes to run validation commands. Use the `--transport` flag or the `TRANSPORT` environment variable to define the connection method.

The `--transport` flag supports the following options:

* `auto`: This is the default option. The script first attempts `SSH` to both nodes. If `SSH` succeeds, it uses `SSH` for the session. If `SSH` fails, it falls back to `oc debug`. If neither works on both nodes, the script exits with an error.
* `ssh`: This option uses `SSH` to connect as the user defined by `--user`. The `--user` value defaults to `core`.

  + Permissions: Requires password-less `sudo` access on all nodes.
  + Automation: The script runs in `BatchMode`, disables interactive prompts, and skips host-key checking.
  + Authentication: Use the `--ssh-key` flag to provide a specific SSH key for all connections.
* `oc debug`: Connects by running the following command against each node:

  ```
  $ oc debug node/<node> --chroot /host
  ```

You do not need SSH access. The `fencing_validator` script only requires a valid `KUBECONFIG` with `cluster-admin` privileges.

For non-disruptive checks, both transports behave identically. However, the transport mode is critical when using the `--disruptive` option. During these tests, the script dispatches the `fence` command asynchronously using `systemd-run` or no hup as a fallback. This fire-and-forget method ensures the command completes even if the `oc debug` session terminates when the node fences.

## [Legal Notice](#idm140668985558032) Copy linkLink copied to clipboard!

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
