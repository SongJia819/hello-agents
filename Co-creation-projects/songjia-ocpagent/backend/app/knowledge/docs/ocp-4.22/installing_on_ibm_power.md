---
title: "Installing on IBM Power"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_ibm_power/index
retrieved_at: 2026-09-05T05:42:05.821220+00:00
---

# Installing on IBM Power

---

OpenShift Container Platform 4.22

## Installing OpenShift Container Platform on IBM Power

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140143185828416)

**Abstract**

This document describes how to install OpenShift Container Platform on IBM Power.

---

## [Chapter 1. Installation methods](#preparing-to-install-on-ibm-power) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform on IBM Power®, review the available installation methods to select the approach that fits your environment.

### [1.1. Installing a cluster on user-provisioned infrastructure](#installation-methods-ibm-power_preparing-to-install-on-ibm-power) Copy linkLink copied to clipboard!

Choose an installation method for IBM Power® based on your network connectivity requirements.

* **Installing a cluster on IBM Power®**: You can install OpenShift Container Platform on IBM Power® infrastructure that you provision.
* **Installing a cluster on IBM Power® in a restricted network**: You can install OpenShift Container Platform on IBM Power® infrastructure that you provision in a restricted or disconnected network by using an internal mirror of the installation release content. You can use this method to install a cluster that does not have an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

## [Chapter 2. Installing a cluster on IBM Power](#installing-ibm-power) Copy linkLink copied to clipboard!

To install a cluster on IBM Power® infrastructure that you provision, review the prerequisites and complete the installation steps.

Important

Additional considerations exist for non-bare metal platforms. Review the guidelines for deploying OpenShift Container Platform on non-tested platforms before you install an OpenShift Container Platform cluster.

### [2.1. Prerequisites for installing a cluster on IBM Power](#prereqs-ibm-power-upi_installing-ibm-power) Copy linkLink copied to clipboard!

Before you install a OpenShift Container Platform cluster on IBM Power®, complete the prerequisite tasks to review installation details, provision storage, and configure your firewall.

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* Before you begin the installation process, you must clean the installation directory. This ensures that the installation program creates and updates the required installation files.
* You provisioned persistent storage using OpenShift Data Foundation or other supported storage providers for your cluster. To deploy a private image registry, you must set up persistent storage with `ReadWriteMany` access.
* If you use a firewall, you configured it to allow the sites that your cluster requires access to.

  Note

  Be sure to also review this site list if you are configuring a proxy.

### [2.2. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-ibm-power) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [2.3. Requirements for a cluster with user-provisioned infrastructure](#ibm-power-upi-requirements-intro_installing-ibm-power) Copy linkLink copied to clipboard!

For a OpenShift Container Platform cluster with user-provisioned infrastructure on IBM Power®, you must deploy all required machines meeting the hardware, network, DNS, and load balancing requirements.

#### [2.3.1. Required machines for cluster installation](#installation-machine-requirements_installing-ibm-power) Copy linkLink copied to clipboard!

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

Important

For a cluster that has user-provisioned infrastructure, you must deploy all of the required machines.

Expand

Table 2.1. Minimum required hosts

| Hosts | Description |
| --- | --- |
| One temporary bootstrap machine | The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster. |
| Three control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| At least two compute machines, which are also known as worker machines. | The workloads requested by OpenShift Container Platform users run on the compute machines. |

Show more

Important

To keep high availability of your cluster, use separate physical hosts for these cluster machines.

The bootstrap, control plane, and compute machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system.

RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.8 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits).

#### [2.3.2. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-ibm-power) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 2.2. Minimum resource requirements

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | RHCOS | 2 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 2 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Show more

* One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
* OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance.

Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* ppc64le architecture requires IBM® Power9 ISA
* s390x architecture requires IBM® z14 ISA

For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

#### [2.3.3. Minimum IBM Power requirements](#minimum-ibm-power-system-requirements_installing-ibm-power) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform on IBM Power®, verify that your hardware meets the minimum system requirements for processor, disk storage, network, and memory.

* IBM Power®9, IBM Power®10 or IBM Power®11 processor-based systems

##### [2.3.3.1. Hardware requirements](#hardware-requirements) Copy linkLink copied to clipboard!

* Six logical partitions (LPARs) across multiple PowerVM servers

##### [2.3.3.2. Operating system requirements](#operating-system-requirements) Copy linkLink copied to clipboard!

* One instance of an IBM Power®9, Power10 or Power11 processor-based system

On your IBM Power® instance, set up:

* Three LPARs for OpenShift Container Platform control plane machines
* Two LPARs for OpenShift Container Platform compute machines
* One LPAR for the temporary OpenShift Container Platform bootstrap machine

##### [2.3.3.3. Disk storage for the IBM Power guest virtual machines](#disk-storage-for-the-ibm-power-guest-virtual-machines) Copy linkLink copied to clipboard!

* Local storage, or storage provisioned by the Virtual I/O Server using vSCSI, NPIV (N-Port ID Virtualization), Fibre Channel, multipath, or SSP (shared storage pools)

##### [2.3.3.4. Network for the PowerVM guest virtual machines](#network-for-the-powervm-guest-virtual-machines) Copy linkLink copied to clipboard!

* Dedicated physical adapter, or SR-IOV virtual function
* Available by the Virtual I/O Server using Shared Ethernet Adapter
* Virtualized by the Virtual I/O Server using IBM® virtual NIC (vNIC)

##### [2.3.3.5. Storage / main memory](#storage-main-memory) Copy linkLink copied to clipboard!

* 500 GB / 16 GB for OpenShift Container Platform control plane machines
* 500 GB / 8 GB for OpenShift Container Platform compute machines
* 500 GB / 16 GB for the temporary OpenShift Container Platform bootstrap machine

#### [2.3.4. Recommended IBM Power system requirements](#recommended-ibm-power-system-requirements_installing-ibm-power) Copy linkLink copied to clipboard!

OpenShift Container Platform on IBM Power® requires a minimum of six LPARs across multiple PowerVM servers, with specific hardware, storage, and network configuration for each node type.

##### [2.3.4.1. Hardware requirements](#hardware-requirements-2) Copy linkLink copied to clipboard!

* Six LPARs across multiple PowerVM servers

##### [2.3.4.2. Operating system requirements](#operating-system-requirements-2) Copy linkLink copied to clipboard!

* One instance of an IBM Power®9, IBM Power®10 or IBM Power®11 processor-based system

On your IBM Power® instance, set up:

* Three LPARs for OpenShift Container Platform control plane machines
* Two LPARs for OpenShift Container Platform compute machines
* One LPAR for the temporary OpenShift Container Platform bootstrap machine

##### [2.3.4.3. Disk storage for the IBM Power guest virtual machines](#disk-storage-for-the-ibm-power-guest-virtual-machines-2) Copy linkLink copied to clipboard!

* Local storage, or storage provisioned by the Virtual I/O Server using vSCSI, NPIV (N-Port ID Virtualization) or SSP (shared storage pools)

##### [2.3.4.4. Network for the PowerVM guest virtual machines](#network-for-the-powervm-guest-virtual-machines-2) Copy linkLink copied to clipboard!

* Dedicated physical adapter, or SR-IOV virtual function
* Virtualized by the Virtual I/O Server using Shared Ethernet Adapter
* Virtualized by the Virtual I/O Server using IBM® virtual NIC (vNIC)

##### [2.3.4.5. Storage / main memory](#storage-main-memory-2) Copy linkLink copied to clipboard!

* 120 GB / 32 GB for OpenShift Container Platform control plane machines
* 120 GB / 32 GB for OpenShift Container Platform compute machines
* 120 GB / 16 GB for the temporary OpenShift Container Platform bootstrap machine

#### [2.3.5. Certificate signing requests management](#csr-management_installing-ibm-power) Copy linkLink copied to clipboard!

On user-provisioned infrastructure, you must implement a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that kubelet credentials request because it cannot confirm that the correct machine issued the request. You must find and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

#### [2.3.6. Networking requirements for user-provisioned infrastructure](#installation-network-user-infra_installing-ibm-power) Copy linkLink copied to clipboard!

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files.

During the initial boot, the machines require an IP address configuration that is set either through a DHCP server or statically by providing the required boot options. After a network connection is established, the machines download their Ignition config files from an HTTP or HTTPS server. The Ignition config files are then used to set the exact state of each machine. The Machine Config Operator completes more changes to the machines, such as the application of new certificates or keys, after installation.

Note

* Consider using a DHCP server for long-term management of the cluster machines. Ensure that the DHCP server is configured to provide persistent IP addresses, DNS server information, and hostnames to the cluster machines.
* If a DHCP service is not available for your user-provisioned infrastructure, you can instead provide the IP networking configuration and the address of the DNS server to the nodes at RHCOS install time. These can be passed as boot arguments if you are installing from an ISO image. See the *Installing RHCOS and starting the OpenShift Container Platform bootstrap process* section for more information about static IP provisioning and advanced networking options.

The Kubernetes API server must be able to resolve the node names of the cluster machines. If the API servers and worker nodes are in different zones, you can configure a default DNS search zone to allow the API server to resolve the node names. Another supported approach is to always refer to hosts by their fully-qualified domain names in both the node objects and all DNS requests.

##### [2.3.6.1. Setting the cluster node hostnames through DHCP](#installation-host-names-dhcp-user-infra_installing-ibm-power) Copy linkLink copied to clipboard!

On Red Hat Enterprise Linux CoreOS (RHCOS) machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start prior to this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node.

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation.

##### [2.3.6.2. Network connectivity requirements](#installation-network-connectivity-user-infra_installing-ibm-power) Copy linkLink copied to clipboard!

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster.

This section provides details about the ports that are required.

Important

In connected OpenShift Container Platform environments, all nodes are required to have internet access to pull images for platform containers and provide telemetry data to Red Hat.

Expand

Table 2.3. Ports used for all-machine to all-machine communications

| Protocol | Port | Description |
| --- | --- | --- |
| ICMP | N/A | Network reachability tests |
| TCP | `1936` | Metrics |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101` and the Cluster Version Operator on port `9099`. |
| `10250`-`10259` | The default ports that Kubernetes reserves |
| `22623` | The port handles traffic from the Machine Config Server and directs the traffic to the control plane machines. |
| UDP | `6081` | Geneve |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101`. |
| `500` | IPsec IKE packets |
| `4500` | IPsec NAT-T packets |
| `123` | Network Time Protocol (NTP) on UDP port `123`. If an external NTP time server is configured, you must open UDP port `123`. |
| TCP/UDP | `30000`-`32767` |
| Kubernetes node port | ESP | N/A |

Show more

Expand

Table 2.4. Ports used for all-machine to control plane communications

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | `6443` | Kubernetes API |

Show more

Expand

Table 2.5. Ports used for control plane machine to control plane machine communications

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | `2379`-`2380` | etcd server and peer ports |

Show more

##### [2.3.6.3. NTP configuration for user-provisioned infrastructure](#ntp-configuration-for-user-provisioned-infrastructure) Copy linkLink copied to clipboard!

OpenShift Container Platform clusters are configured to use a public Network Time Protocol (NTP) server by default. If you want to use a local enterprise NTP server, or if your cluster is being deployed in a disconnected network, you can configure the cluster to use a specific time server. For more information, see the documentation for *Configuring chrony time service*.

If a DHCP server provides NTP server information, the chrony time service on the Red Hat Enterprise Linux CoreOS (RHCOS) machines read the information and can sync the clock with the NTP servers.

#### [2.3.7. User-provisioned DNS requirements](#installation-dns-user-infra_installing-ibm-power) Copy linkLink copied to clipboard!

In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes.

The following is a list of required cluster components:

* The Kubernetes API
* The OpenShift Container Platform application wildcard
* The bootstrap and control plane machines
* The compute machines

Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate.

Note

It is recommended to use a DHCP server to provide the hostnames to each cluster node. See the *DHCP recommendations for user-provisioned infrastructure* section for more information.

The following DNS records are required for a user-provisioned OpenShift Container Platform cluster and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

Expand

Table 2.6. Required DNS records

| Component | Record | Description |
| --- | --- | --- |
| Kubernetes API | `api.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |
| `api-int.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.  Important  The API server must be able to resolve the worker nodes by the hostnames that are recorded in Kubernetes. If the API server cannot resolve the node names, then proxied API calls can fail, and you cannot retrieve logs from pods. |
| Routes | `*.apps.<cluster_name>.<base_domain>.` | A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.  For example, `console-openshift-console.apps.<cluster_name>.<base_domain>` is used as a wildcard route to the OpenShift Container Platform console. |
| Bootstrap machine | `bootstrap.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the bootstrap machine. These records must be resolvable by the nodes within the cluster. |
| Control plane machines | `<control_plane><n>.<cluster_name>.<base_domain>.` | DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the control plane nodes. These records must be resolvable by the nodes within the cluster. |
| Compute machines | `<compute><n>.<cluster_name>.<base_domain>.` | DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the worker nodes. These records must be resolvable by the nodes within the cluster. |

Show more

Note

In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration.

Tip

You can use the `dig` command to verify name and reverse name resolution. See the section on *Validating DNS resolution for user-provisioned infrastructure* for detailed validation steps.

##### [2.3.7.1. Example DNS configuration for user-provisioned clusters](#installation-dns-user-infra-example_installing-ibm-power) Copy linkLink copied to clipboard!

Reference the example DNS configurations to understand how A and PTR record configuration samples meet the DNS requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

The DNS configuration examples provided here are for reference only and are not meant to provide advice for choosing one DNS solution over another.

In the examples, the cluster name is `ocp4` and the base domain is `example.com`.

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
control-plane2.ocp4.example.com.	IN	A	192.168.1.99
;
compute0.ocp4.example.com.	IN	A	192.168.1.11
compute1.ocp4.example.com.	IN	A	192.168.1.7
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

`compute0.ocp4.example.com.`
:   Provides name resolution for the compute machines.

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
99.1.168.192.in-addr.arpa.	IN	PTR	control-plane2.ocp4.example.com.
;
11.1.168.192.in-addr.arpa.	IN	PTR	compute0.ocp4.example.com.
7.1.168.192.in-addr.arpa.	IN	PTR	compute1.ocp4.example.com.
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

`compute0.ocp4.example.com.`
:   Provides reverse DNS resolution for the compute machines.

Note

A PTR record is not required for the OpenShift Container Platform application wildcard.

#### [2.3.8. Load balancing requirements for user-provisioned infrastructure](#installation-load-balancing-user-infra_installing-ibm-power) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform, you must provision the API and application Ingress load balancing infrastructure. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

Note

If you want to deploy the API and application Ingress load balancers with a Red Hat Enterprise Linux (RHEL) instance, you must purchase the RHEL subscription separately.

The load balancing infrastructure must meet the following requirements:

* API load balancer: Provides a common endpoint for users, both human and machine, to interact with and configure the platform. Configure the following conditions:

  + Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode.
  + A stateless load balancing algorithm. The options vary based on the load balancer implementation.

Important

Do not configure session persistence for an API load balancer. Configuring session persistence for a Kubernetes API server might cause performance issues from excess application traffic for your OpenShift Container Platform cluster and the Kubernetes API that runs inside the cluster.

Configure the following ports on both the front and back of the API load balancers:

Expand

| Port | Back-end machines (pool members) | Internal | External | Description |
| --- | --- | --- | --- | --- |
| `6443` | Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane. You must configure the `/readyz` endpoint for the API server health check probe. | X | X | Kubernetes API server |
| `22623` | Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane. | X |  | Machine config server |

Show more

Note

The load balancer must be configured to take a maximum of 30 seconds from the time the API server turns off the `/readyz` endpoint to the removal of the API server instance from the pool. Within the time frame after `/readyz` returns an error or becomes healthy, the endpoint must have been removed or added. Probing every 5 or 10 seconds, with two successful requests to become healthy and three to become unhealthy, are well-tested values.

* Application Ingress load balancer: Provides an ingress point for application traffic flowing in from outside the cluster. A working configuration for the Ingress router is required for an OpenShift Container Platform cluster. Configure the following conditions:

  + Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode.
  + A connection-based or session-based persistence is recommended, based on the options available and types of applications that will be hosted on the platform.

Tip

If the true IP address of the client can be seen by the application Ingress load balancer, enabling source IP-based session persistence can improve performance for applications that use end-to-end TLS encryption.

Configure the following ports on both the front and back of the load balancers:

Expand

Table 2.7. Application Ingress load balancer

| Port | Back-end machines (pool members) | Internal | External | Description |
| --- | --- | --- | --- | --- |
| `443` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTPS traffic |
| `80` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTP traffic |

Show more

Note

If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.

##### [2.3.8.1. Example load balancer configuration for user-provisioned clusters](#installation-load-balancing-user-infra-example_installing-ibm-power) Copy linkLink copied to clipboard!

Reference the example API and application Ingress load balancer configuration so that you can understand how to meet the load balancing requirements for user-provisioned clusters.

The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another.

Tip

If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node.

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

Note

If you are using HAProxy as a load balancer and SELinux is set to `enforcing`, you must ensure that the HAProxy service can bind to the configured TCP port by running `setsebool -P haproxy_connect_any=1`.

**Sample API and application Ingress load balancer configuration**

```
global
  log         127.0.0.1 local2
  pidfile     /var/run/haproxy.pid
  maxconn     4000
  daemon
defaults
  mode                    http
  log                     global
  option                  dontlognull
  option http-server-close
  option                  redispatch
  retries                 3
  timeout http-request    10s
  timeout queue           1m
  timeout connect         10s
  timeout client          1m
  timeout server          1m
  timeout http-keep-alive 10s
  timeout check           10s
  maxconn                 3000
listen api-server-6443
  bind *:6443
  mode tcp
  option  httpchk GET /readyz HTTP/1.0
  option  log-health-checks
  balance roundrobin
  server bootstrap bootstrap.ocp4.example.com:6443 verify none check check-ssl inter 10s fall 2 rise 3 backup
  server master0 master0.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master1 master1.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master2 master2.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
listen machine-config-server-22623
  bind *:22623
  mode tcp
  server bootstrap bootstrap.ocp4.example.com:22623 check inter 1s backup
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443
  bind *:443
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:443 check inter 1s
  server compute1 compute1.ocp4.example.com:443 check inter 1s
listen ingress-router-80
  bind *:80
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:80 check inter 1s
  server compute1 compute1.ocp4.example.com:80 check inter 1s
```

where:

`listen api-server-6443`
:   Port `6443` handles the Kubernetes API traffic and points to the control plane machines. You must configure health checks on this port to ensure that the API server is available before routing traffic.

`server bootstrap bootstrap.ocp4.example.com`
:   The bootstrap entries must be in place before the OpenShift Container Platform cluster installation and they must be removed after the bootstrap process is complete.

`listen machine-config-server`
:   Port `22623` handles the machine config server traffic and points to the control plane machines.

`listen ingress-router-443`
:   Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.

`listen ingress-router-80`
:   Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.

    Note

    If you are deploying a compact three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.

### [2.4. Preparing the user-provisioned infrastructure](#installation-infrastructure-user-infra_installing-ibm-power) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform on user-provisioned infrastructure, you must prepare the underlying infrastructure.

This section provides details about the high-level steps required to set up your cluster infrastructure in preparation for an OpenShift Container Platform installation. This includes configuring IP networking and network connectivity for your cluster nodes, enabling the required ports through your firewall, and setting up the required DNS and load balancing infrastructure.

After preparation, your cluster infrastructure must meet the requirements outlined in the *Requirements for a cluster with user-provisioned infrastructure* section.

**Prerequisites**

* You have reviewed the [OpenShift Container Platform 4.x Tested Integrations](https://access.redhat.com/articles/4128421) page.
* You have reviewed the infrastructure requirements detailed in the *Requirements for a cluster with user-provisioned infrastructure* section.

**Procedure**

1. If you are using DHCP to provide the IP networking configuration to your cluster nodes, configure your DHCP service.

   1. Add persistent IP addresses for the nodes to your DHCP server configuration. In your configuration, match the MAC address of the relevant network interface to the intended IP address for each node.
   2. When you use DHCP to configure IP addressing for the cluster machines, the machines also obtain the DNS server information through DHCP. Define the persistent DNS server address that is used by the cluster nodes through your DHCP server configuration.

      Note

      If you are not using a DHCP service, you must provide the IP networking configuration and the address of the DNS server to the nodes at RHCOS install time. These can be passed as boot arguments if you are installing from an ISO image. See the *Installing RHCOS and starting the OpenShift Container Platform bootstrap process* section for more information about static IP provisioning and advanced networking options.
   3. Define the hostnames of your cluster nodes in your DHCP server configuration. See the *Setting the cluster node hostnames through DHCP* section for details about hostname considerations.

      Note

      If you are not using a DHCP service, the cluster nodes obtain their hostname through a reverse DNS lookup.
2. Ensure that your network infrastructure provides the required network connectivity between the cluster components. See the *Networking requirements for user-provisioned infrastructure* section for details about the requirements.
3. Configure your firewall to enable the ports required for the OpenShift Container Platform cluster components to communicate. See *Networking requirements for user-provisioned infrastructure* section for details about the ports that are required.

   Important

   By default, port `1936` is accessible for an OpenShift Container Platform cluster, because each control plane node needs access to this port.

   For ingress health check probes, the `/healthz/ready` endpoint is available on this port.

   Avoid using the Ingress load balancer to expose this port, because doing so might result in the exposure of sensitive information, such as statistics and metrics, related to Ingress Controllers.
4. Setup the required DNS infrastructure for your cluster.

   1. Configure DNS name resolution for the Kubernetes API, the application wildcard, the bootstrap machine, the control plane machines, and the compute machines.
   2. Configure reverse DNS resolution for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.

      See the *User-provisioned DNS requirements* section for more information about the OpenShift Container Platform DNS requirements.
5. Validate your DNS configuration.

   1. From your installation node, run DNS lookups against the record names of the Kubernetes API, the wildcard routes, and the cluster nodes. Validate that the IP addresses in the responses correspond to the correct components.
   2. From your installation node, run reverse DNS lookups against the IP addresses of the load balancer and the cluster nodes. Validate that the record names in the responses correspond to the correct components.

      See the *Validating DNS resolution for user-provisioned infrastructure* section for detailed DNS validation steps.
6. Provision the required API and application ingress load balancing infrastructure. See the *Load balancing requirements for user-provisioned infrastructure* section for more information about the requirements.

   Note

   Some load balancing solutions require the DNS name resolution for the cluster nodes to be in place before the load balancing is initialized.

### [2.5. Validating DNS resolution for user-provisioned infrastructure](#installation-user-provisioned-validating-dns_installing-ibm-power) Copy linkLink copied to clipboard!

To prevent network-related installation failures and ensure node connectivity in OpenShift Container Platform, validate your DNS configuration before deploying on user-provisioned infrastructure.

Important

The validation steps detailed in this section must succeed before you install your cluster.

**Prerequisites**

* You have configured the required DNS records for your user-provisioned infrastructure.

**Procedure**

1. From your installation node, run DNS lookups against the record names of the Kubernetes API, the wildcard routes, and the cluster nodes. Validate that the IP addresses contained in the responses correspond to the correct components.

   1. Perform a lookup against the Kubernetes API record name. Check that the result points to the IP address of the API load balancer:

      ```
      $ dig +noall +answer @<nameserver_ip> api.<cluster_name>.<base_domain>
      ```

      Replace `<nameserver_ip>` with the IP address of the name server, `<cluster_name>` with your cluster name, and `<base_domain>` with your base domain name.

      **Example output**

      ```
      api.ocp4.example.com.		604800	IN	A	192.168.1.5
      ```
   2. Perform a lookup against the Kubernetes internal API record name. Check that the result points to the IP address of the API load balancer:

      ```
      $ dig +noall +answer @<nameserver_ip> api-int.<cluster_name>.<base_domain>
      ```

      **Example output**

      ```
      api-int.ocp4.example.com.		604800	IN	A	192.168.1.5
      ```
   3. Test an example `*.apps.<cluster_name>.<base_domain>` DNS wildcard lookup. All of the application wildcard lookups must resolve to the IP address of the application ingress load balancer:

      ```
      $ dig +noall +answer @<nameserver_ip> random.apps.<cluster_name>.<base_domain>
      ```

      **Example output**

      ```
      random.apps.ocp4.example.com.		604800	IN	A	192.168.1.5
      ```

      Note

      In the example outputs, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

      You can replace `random` with another wildcard value. For example, you can query the route to the OpenShift Container Platform console:

      ```
      $ dig +noall +answer @<nameserver_ip> console-openshift-console.apps.<cluster_name>.<base_domain>
      ```

      **Example output**

      ```
      console-openshift-console.apps.ocp4.example.com. 604800 IN	A 192.168.1.5
      ```
   4. Run a lookup against the bootstrap DNS record name. Check that the result points to the IP address of the bootstrap node:

      ```
      $ dig +noall +answer @<nameserver_ip> bootstrap.<cluster_name>.<base_domain>
      ```

      **Example output**

      ```
      bootstrap.ocp4.example.com.		604800	IN	A	192.168.1.96
      ```
   5. Use this method to perform lookups against the DNS record names for the control plane and compute nodes. Check that the results correspond to the IP addresses of each node.
2. From your installation node, run reverse DNS lookups against the IP addresses of the load balancer and the cluster nodes. Validate that the record names contained in the responses correspond to the correct components.

   1. Perform a reverse lookup against the IP address of the API load balancer. Check that the response includes the record names for the Kubernetes API and the Kubernetes internal API:

      ```
      $ dig +noall +answer @<nameserver_ip> -x 192.168.1.5
      ```

      **Example output**

      ```
      5.1.168.192.in-addr.arpa. 604800	IN	PTR	api-int.ocp4.example.com.
      5.1.168.192.in-addr.arpa. 604800	IN	PTR	api.ocp4.example.com.
      ```

      where:

      `api-int.ocp4.example.com`
      :   Specifies the record name for the Kubernetes internal API.

      `api.ocp4.example.com`
      :   Specifies the record name for the Kubernetes API.

          Note

          A PTR record is not required for the OpenShift Container Platform application wildcard. No validation step is needed for reverse DNS resolution against the IP address of the application ingress load balancer.
   2. Perform a reverse lookup against the IP address of the bootstrap node. Check that the result points to the DNS record name of the bootstrap node:

      ```
      $ dig +noall +answer @<nameserver_ip> -x 192.168.1.96
      ```

      **Example output**

      ```
      96.1.168.192.in-addr.arpa. 604800	IN	PTR	bootstrap.ocp4.example.com.
      ```
   3. Use this method to perform reverse lookups against the IP addresses for the control plane and compute nodes. Check that the results correspond to the DNS record names of each node.

### [2.6. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-ibm-power) Copy linkLink copied to clipboard!

During an OpenShift Container Platform installation, you can provide an SSH public key to the installation program. The key is passed to the Red Hat Enterprise Linux CoreOS (RHCOS) nodes through their Ignition config files and is used to authenticate SSH access to the nodes. The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication.

The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication. After the key is passed to the nodes, you can use the key pair to SSH in to the RHCOS nodes as the user `core`. To access the nodes through SSH, the private key identity must be managed by SSH for your local user.

If you want to SSH in to your cluster nodes to perform installation debugging or disaster recovery, you must provide the SSH public key during the installation process. The `./openshift-install gather` command also requires the SSH public key to be in place on the cluster nodes.

Important

Do not skip this procedure in production environments, where disaster recovery and debugging is required.

Note

You must use a local key, not one that you configured with platform-specific approaches.

**Procedure**

1. If you do not have an existing SSH key pair on your local machine to use for authentication onto your cluster nodes, create one. For example, on a computer that uses a Linux operating system, run the following command:

   ```
   $ ssh-keygen -t ed25519 -N '' -f <path>/<file_name>
   ```

   Specifies the path and file name, such as `~/.ssh/id_ed25519`, of the new SSH key. If you have an existing key pair, ensure your public key is in the your `~/.ssh` directory.

   Note

   If you plan to install an OpenShift Container Platform cluster that uses the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the `x86_64`, `ppc64le`, and `s390x` architectures, do not create a key that uses the `ed25519` algorithm. Instead, create a key that uses the `rsa` or `ecdsa` algorithm.
2. View the public SSH key:

   ```
   $ cat <path>/<file_name>.pub
   ```

   For example, run the following to view the `~/.ssh/id_ed25519.pub` public key:

   ```
   $ cat ~/.ssh/id_ed25519.pub
   ```
3. Add the SSH private key identity to the SSH agent for your local user, if it has not already been added. SSH agent management of the key is required for password-less SSH authentication onto your cluster nodes, or if you want to use the `./openshift-install gather` command.

   Note

   On some distributions, default SSH private key identities such as `~/.ssh/id_rsa` and `~/.ssh/id_dsa` are managed automatically.

   1. If the `ssh-agent` process is not already running for your local user, start it as a background task:

      ```
      $ eval "$(ssh-agent -s)"
      ```

      **Example output**

      ```
      Agent pid 31874
      ```

      Note

      If your cluster is in FIPS mode, only use FIPS-compliant algorithms to generate the SSH key. The key must be either RSA or ECDSA.
4. Add your SSH private key to the `ssh-agent`:

   ```
   $ ssh-add <path>/<file_name>
   ```

   Specifies the path and file name for your SSH private key, such as `~/.ssh/id_ed25519`

   **Example output**

   ```
   Identity added: /home/<you>/<path>/<file_name> (<computer_name>)
   ```

**Next steps**

* When you install OpenShift Container Platform, provide the SSH public key to the installation program.

### [2.7. Obtaining the installation program](#installation-obtaining-installer_installing-ibm-power) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform, download the installation file on the host you are using for installation.

**Prerequisites**

* You have a computer that runs Linux or macOS, with 500 MB of local disk space.

**Procedure**

1. Go to the [Cluster Type](https://console.redhat.com/openshift/install) page on the Red Hat Hybrid Cloud Console. If you have a Red Hat account, log in with your credentials. If you do not, create an account.

   Tip

   You can also [download the binaries for a specific OpenShift Container Platform release](https://mirror.openshift.com/pub/openshift-v4/clients/ocp/).
2. Select your infrastructure provider from the **Run it yourself** section of the page.
3. Select your host operating system and architecture from the dropdown menus under **OpenShift Installer** and click **Download Installer**.
4. Place the downloaded file in the directory where you want to store the installation configuration files.

   Important

   * The installation program creates several files on the computer that you use to install your cluster. You must keep the installation program and the files that the installation program creates after you finish installing the cluster. Both of the files are required to delete the cluster.
   * Deleting the files created by the installation program does not remove your cluster, even if the cluster failed during installation. To remove your cluster, complete the OpenShift Container Platform uninstallation procedures for your specific cloud provider.
5. Extract the installation program. For example, on a computer that uses a Linux operating system, run the following command:

   ```
   $ tar -xvf openshift-install-linux.tar.gz
   ```
6. Download your installation [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.

   Tip

   Alternatively, you can retrieve the installation program from the [Red Hat Customer Portal](https://access.redhat.com/downloads/content/290/), where you can specify a version of the installation program to download. However, you must have an active subscription to access this page.

### [2.8. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-ibm-power) Copy linkLink copied to clipboard!

To manage your cluster and deploy applications from the command line on Linux, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

Important

If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.

**Procedure**

1. Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.
2. Select the architecture from the **Product Variant** list.
3. Select the appropriate version from the **Version** list.
4. Click **Download Now** next to the **OpenShift v4.22 Linux Clients** entry and save the file.
5. Unpack the archive:

   ```
   $ tar xvf <file>
   ```
6. Place the `oc` binary in a directory that is on your `PATH`.

   To check your `PATH`, execute the following command:

   ```
   $ echo $PATH
   ```

**Verification**

* After you install the OpenShift CLI, it is available using the `oc` command:

  ```
  $ oc <command>
  ```

### [2.9. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-ibm-power) Copy linkLink copied to clipboard!

To manage your cluster and deploy applications from the command line on Windows, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

Important

If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.

**Procedure**

1. Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.
2. Select the appropriate version from the **Version** list.
3. Click **Download Now** next to the **OpenShift v4.22 Windows Client** entry and save the file.
4. Extract the archive with a ZIP program.
5. Move the `oc` binary to a directory that is on your `PATH` variable.

   To check your `PATH` variable, open the command prompt and execute the following command:

   ```
   C:\> path
   ```

**Verification**

* After you install the OpenShift CLI, it is available using the `oc` command:

  ```
  C:\> oc <command>
  ```

### [2.10. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-ibm-power) Copy linkLink copied to clipboard!

To manage your cluster and deploy applications from the command line on macOS, install the OpenShift CLI (`oc`) binary. You can download the OpenShift CLI (`oc`) from the Red  Customer Portal.

Important

If you installed an earlier version of `oc`, you cannot use it to complete all of the commands in OpenShift Container Platform.

Download and install the new version of `oc`.

**Procedure**

1. Navigate to the [Download OpenShift Container Platform](https://access.redhat.com/downloads/content/290) page on the Red Hat Customer Portal.
2. Select the architecture from the **Product Variant** list.
3. Select the appropriate version from the **Version** list.
4. Click **Download Now** next to the **OpenShift v4.22 macOS Clients** entry and save the file.

   Note

   For macOS arm64, choose the **OpenShift v4.22 macOS arm64 Client** entry.
5. Unpack and unzip the archive.
6. Move the `oc` binary to a directory on your `PATH` variable.

   To check your `PATH` variable, open a terminal and execute the following command:

   ```
   $ echo $PATH
   ```

**Verification**

* Verify your installation by using an `oc` command:

  ```
  $ oc <command>
  ```

### [2.11. Manually creating the installation configuration file](#installation-initializing-manual_installing-ibm-power) Copy linkLink copied to clipboard!

Installing the cluster requires that you manually create the installation configuration file.

**Prerequisites**

* You have an SSH public key on your local machine for use with the installation program. You can use the key for SSH authentication onto your cluster nodes for debugging and disaster recovery.
* You have obtained the OpenShift Container Platform installation program and the pull secret for your cluster.

**Procedure**

1. Create an installation directory to store your required installation assets in:

   ```
   $ mkdir <installation_directory>
   ```

   Important

   You must create a directory. Some installation assets, such as bootstrap X.509 certificates have short expiration intervals, so you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
2. Customize the provided sample `install-config.yaml` file template and save the file in the `<installation_directory>`.

   Note

   You must name this configuration file `install-config.yaml`.
3. Back up the `install-config.yaml` file so that you can use it to install many clusters.

   Important

   Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.

#### [2.11.1. Sample install-config.yaml file for IBM Power](#installation-bare-metal-config-yaml_installing-ibm-power) Copy linkLink copied to clipboard!

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster platform or modify the values of the required parameters.

```
apiVersion: v1
baseDomain: example.com
compute:
- hyperthreading: Enabled
  name: worker
  replicas: 0
  architecture: ppc64le
controlPlane:
  hyperthreading: Enabled
  name: master
  replicas: 3
  architecture: ppc64le
metadata:
  name: test
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  networkType: OVNKubernetes
  machineNetwork:
  - cidr: 192.168.0.0/16
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
fips: false
pullSecret: '{"auths": ...}'
sshKey: 'ssh-ed25519 AAAA...'
```

where:

`baseDomain`
:   Specifies the base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name.

`compute`
:   Specifies the `compute` node configurations, which is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`.

`controlPlane`
:   Specifies the `controlPlane` node configurations, which is a single mapping. To meet the requirements of the different data structures, the first line of the `controlPlane` section must not. Only one control plane pool is used.

`hyperthreading`
:   Specifies simultaneous multithreading (SMT), which you configure as a post-installation task.

`compute.replicas`
:   Specifies the number of compute machines that the cluster creates and manages for you on installer-provisioned installations. You must set this value to `0` when you install OpenShift Container Platform on user-provisioned infrastructure. Additionally for user-provisioned installations, you must manually deploy the compute machines before you finish installing the cluster.

Note

If you are installing a three-node cluster, do not deploy any compute machines when you install the Red Hat Enterprise Linux CoreOS (RHCOS) machines.

`controlPlane.replicas`
:   Specifies the number of control plane machines that you add to the cluster. Because the cluster uses these values as the number of etcd endpoints in the cluster, the value must match the number of control plane machines that you deploy.

`metadata.name`
:   Specifies the cluster name that you specified in your DNS records.

`networking.clusterNetwork.cidr`
:   Specifies a block of IP addresses from which pod IP addresses are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the pod network. If you need to access the pods from an external network, you must configure load balancers and routers to manage the traffic.

Note

Class E CIDR range is reserved for a future use. To use the Class E CIDR range, you must ensure your networking environment accepts the IP addresses within the Class E CIDR range.

`networking.cidr.hostPrefix`
:   Specifies the subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23`, then each node is assigned a `/23` subnet out of the given `cidr`, which allows for 510 (2^(32 - 23) - 2) pod IP addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.

`networking.networkType`
:   Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

`networking.serviceNetwork`
:   Specifies the IP address pool to use for service IP addresses. You can enter only one IP address pool. This block must not overlap with existing physical networks. If you need to access the services from an external network, configure load balancers and routers to manage the traffic.

`platform`
:   Specifies the platform. You must set the platform to `none`. You cannot provide additional platform configuration variables for IBM Power® infrastructure.

Important

Clusters that are installed with the platform type `none` are unable to use some features, such as managing compute machines with the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that would normally support the feature. This parameter cannot be changed after installation.

`fips`
:   Specifies either enabling or disabling FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead.

Important

To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening).

When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86\_64, ppc64le, and s390x architectures.

`pullSecret`
:   Specifies the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret). This pull secret allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.

`sshKey`
:   Specifies the SSH public key for the `core` user in Red Hat Enterprise Linux CoreOS (RHCOS).

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

#### [2.11.2. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-ibm-power) Copy linkLink copied to clipboard!

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

**Prerequisites**

* You have an existing `install-config.yaml` file.
* You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, the proxy handles all cluster egress traffic, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object’s `spec.noProxy` field to bypass the proxy if necessary.

  Note

  The `Proxy` object `status.noProxy` field includes the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration.

  For installations on Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Red Hat OpenStack Platform (RHOSP), the `Proxy` object `status.noProxy` field also includes the instance metadata endpoint (`169.254.169.254`).

**Procedure**

1. Edit your `install-config.yaml` file and add the proxy settings. For example:

   ```
   apiVersion: v1
   baseDomain: my.domain.com
   proxy:
     httpProxy: http://<username>:<pswd>@<ip>:<port>
     httpsProxy: https://<username>:<pswd>@<ip>:<port>
     noProxy: example.com
   additionalTrustBundle: |
       -----BEGIN CERTIFICATE-----
       <MY_TRUSTED_CA_CERT>
       -----END CERTIFICATE-----
   additionalTrustBundlePolicy: <policy_to_add_additionalTrustBundle>
   # ...
   ```

   where:

   `proxy.httpProxy`
   :   Specifies a proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`.

   `proxy.httpsProxy`
   :   Specifies a proxy URL to use for creating HTTPS connections outside the cluster.

   `proxy.noProxy`
   :   Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations.

   `additionalTrustBundle`
   :   If you specify this value, the installation program generates a config map named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you specify `additionalTrustBundle` and at least one proxy setting, the `Proxy` object references the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the RHCOS trust bundle. You must set the `additionalTrustBundle` field unless an authority from the RHCOS trust bundle signs the proxy’s identity certificate.

   `additionalTrustBundlePolicy`
   :   Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when you configure an `http/https` proxy. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter.

       Note

       The installation program does not support the proxy `readinessEndpoints` field.

       Note

       If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:

       ```
       $ ./openshift-install wait-for install-complete --log-level debug
       ```
2. Save the file and reference it when installing OpenShift Container Platform.

   The installation program creates a cluster-wide proxy named `cluster` that uses the proxy settings in the `install-config.yaml` file. If you do not give proxy settings, the installation program still creates a `cluster` `Proxy` object, but it has a nil `spec`.

   Note

   Only the `Proxy` object named `cluster` is supported, and you cannot create additional proxies.

#### [2.11.3. Configuring a three-node cluster](#installation-three-node-cluster_installing-ibm-power) Copy linkLink copied to clipboard!

To create smaller, resource-efficient clusters for testing and production, deploy a bare-metal cluster with zero compute machines. This optional configuration uses only three control plane machines, optimizing infrastructure resources for administrators and developers.

In three-node OpenShift Container Platform environments, the three control plane machines are schedulable, which means that your application workloads run on them.

**Prerequisites**

* You have an existing `install-config.yaml` file.

**Procedure**

* Ensure that the number of compute replicas is set to `0` in your `install-config.yaml` file, as shown in the following `compute` stanza:

  ```
  compute:
  - name: worker
    platform: {}
    replicas: 0
  # ...
  ```

  Note

  You must set the value of the `replicas` parameter for the compute machines to `0` when you install OpenShift Container Platform on user-provisioned infrastructure, regardless of the number of compute machines you deploy. In installer-provisioned installations, the parameter controls the number of compute machines that the cluster creates and manages for you. This does not apply to user-provisioned installations, where you deploy the compute machines manually.

For three-node cluster installations, follow these next steps:

* If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. See the *Load balancing requirements for user-provisioned infrastructure* section for more information.
* When you create the Kubernetes manifest files in the following procedure, ensure that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file is set to `true`. This enables your application workloads to run on the control plane nodes.
* Do not deploy any compute nodes when you create the Red Hat Enterprise Linux CoreOS (RHCOS) machines.

### [2.12. Cluster Network Operator configuration](#nw-operator-cr_installing-ibm-power) Copy linkLink copied to clipboard!

To manage cluster networking, configure the Cluster Network Operator (CNO) `Network` custom resource (CR) named `cluster` so the cluster uses the correct IP ranges and network plugin settings for reliable pod and service connectivity. Some settings and fields are inherited at the time of install or by the `default.Network.type` plugin, OVN-Kubernetes.

The CNO configuration inherits the following fields during cluster installation from the `Network` API in the `Network.config.openshift.io` API group:

`clusterNetwork`
:   IP address pools from which pod IP addresses are allocated.

`serviceNetwork`
:   IP address pool for services.

`defaultNetwork.type`
:   Cluster network plugin. `OVNKubernetes` is the only supported plugin during installation.

You can specify the cluster network plugin configuration for your cluster by setting the fields for the `defaultNetwork` object in the CNO object named `cluster`.

#### [2.12.1. Cluster Network Operator configuration object](#nw-operator-cr-cno-object_installing-ibm-power) Copy linkLink copied to clipboard!

The fields for the Cluster Network Operator (CNO) are described in the following table:

Expand

Table 2.8. Cluster Network Operator configuration object

| Field | Type | Description |
| --- | --- | --- |
| `metadata.name` | `string` | The name of the CNO object. This name is always `cluster`. |
| `spec.clusterNetwork` | `array` | A list specifying the blocks of IP addresses from which pod IP addresses are allocated and the subnet prefix length assigned to each individual node in the cluster. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:  ``` spec:   clusterNetwork:   - cidr: 10.128.0.0/19     hostPrefix: 23   - cidr: fd01::/48     hostPrefix: 64 ```  If you install a cluster on AWS with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first. |
| `spec.serviceNetwork` | `array` | A block of IP addresses for services. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:  ``` spec:   serviceNetwork:   - 172.30.0.0/14   - fd02::/112 ```  If you install a cluster on AWS with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first.  You can customize this field only in the `install-config.yaml` file before you create the manifests. The value is read-only in the manifest file. |
| `spec.defaultNetwork` | `object` | Configures the network plugin for the cluster network. |
| `spec.additionalRoutingCapabilities.providers` | `array` | This setting enables a dynamic routing provider. The FRR routing capability provider is required for the route advertisement feature. The only supported value is `FRR`.  * `FRR`: The FRR routing provider  ``` spec:   additionalRoutingCapabilities:     providers:     - FRR ``` |

Show more

Important

For a cluster that needs to deploy objects across multiple networks, ensure that you specify the same value for the `clusterNetwork.hostPrefix` parameter for each network type that is defined in the `install-config.yaml` file. Setting a different value for each `clusterNetwork.hostPrefix` parameter can impact the OVN-Kubernetes network plugin, where the plugin cannot effectively route object traffic among different nodes.

#### [2.12.2. defaultNetwork object configuration](#nw-operator-cr-defaultnetwork_installing-ibm-power) Copy linkLink copied to clipboard!

The values for the `defaultNetwork` object are defined in the following table:

Expand

Table 2.9. defaultNetwork object

| Field | Type | Description |
| --- | --- | --- |
| `type` | `string` | `OVNKubernetes`. The Red Hat OpenShift Networking network plugin is selected during installation. This value cannot be changed after cluster installation.  Note  OpenShift Container Platform uses the OVN-Kubernetes network plugin by default. |
| `ovnKubernetesConfig` | `object` | This object is only valid for the OVN-Kubernetes network plugin. |

Show more

#### [2.12.3. Configuration for the OVN-Kubernetes network plugin](#nw-operator-configuration-parameters-for-ovn-sdn_installing-ibm-power) Copy linkLink copied to clipboard!

The following table describes the configuration fields for the OVN-Kubernetes network plugin:

Expand

Table 2.10. ovnKubernetesConfig object

| Field | Type | Description |
| --- | --- | --- |
| `mtu` | `integer` | The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This is detected automatically based on the MTU of the primary network interface. You do not normally need to override the detected MTU.  If the auto-detected value is not what you expect it to be, confirm that the MTU on the primary network interface on your nodes is correct. You cannot use this option to change the MTU value of the primary network interface on the nodes.  If your cluster requires different MTU values for different nodes, you must set this value to `100` less than the lowest MTU value in your cluster. For example, if some nodes in your cluster have an MTU of `9001`, and some have an MTU of `1500`, you must set this value to `1400`. |
| `genevePort` | `integer` | The port to use for all Geneve packets. The default value is `6081`. This value cannot be changed after cluster installation. |
| `ipsecConfig` | `object` | Specify a configuration object for customizing the IPsec configuration. |
| `ipv4` | `object` | Specifies a configuration object for IPv4 settings. |
| `ipv6` | `object` | Specifies a configuration object for IPv6 settings. |
| `policyAuditConfig` | `object` | Specify a configuration object for customizing network policy audit logging. If unset, the defaults audit log settings are used. |
| `routeAdvertisements` | `string` | Specifies whether to advertise cluster network routes. The default value is `Disabled`.  * `Enabled`: Import routes to the cluster network and advertise cluster network routes as configured in `RouteAdvertisements` objects. * `Disabled`: Do not import routes to the cluster network or advertise cluster network routes. |
| `gatewayConfig` | `object` | Optional: Specify a configuration object for customizing how egress traffic is sent to the node gateway. Valid values are `Shared` and `Local`. The default value is `Shared`. In the default setting, the Open vSwitch (OVS) outputs traffic directly to the node IP interface. If you are using hardware offloading, Red Hat recommends to use the default `Shared` gateway mode to bypass the host routing plane. In the `Local` setting, it traverses the host network; consequently, it gets applied to the routing table of the host.  Note  While migrating egress traffic, you can expect some disruption to workloads and service traffic until the Cluster Network Operator (CNO) successfully rolls out the changes. |

Show more

Expand

Table 2.11. ovnKubernetesConfig.ipv4 object

| Field | Type | Description |
| --- | --- | --- |
| `internalTransitSwitchSubnet` | string | If your existing network infrastructure overlaps with the `100.88.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.  The default value is `100.88.0.0/16`. |
| `internalJoinSubnet` | string | If your existing network infrastructure overlaps with the `100.64.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster. For example, if the `clusterNetwork.cidr` value is `10.128.0.0/14` and the `clusterNetwork.hostPrefix` value is `/23`, then the maximum number of nodes is `2^(23-14)=512`.  The default value is `100.64.0.0/16`. |

Show more

Expand

Table 2.12. ovnKubernetesConfig.ipv6 object

| Field | Type | Description |
| --- | --- | --- |
| `internalTransitSwitchSubnet` | string | If your existing network infrastructure overlaps with the `fd97::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.  The default value is `fd97::/64`. |
| `internalJoinSubnet` | string | If your existing network infrastructure overlaps with the `fd98::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster.  The default value is `fd98::/64`. |

Show more

Expand

Table 2.13. policyAuditConfig object

| Field | Type | Description |
| --- | --- | --- |
| `rateLimit` | integer | The maximum number of messages to generate every second per node. The default value is `20` messages per second. |
| `maxFileSize` | integer | The maximum size for the audit log in bytes. The default value is `50000000` or 50 MB. |
| `maxLogFiles` | integer | The maximum number of log files that are retained. |
| `destination` | string | One of the following additional audit log targets:  `libc`  The libc `syslog()` function of the journald process on the host.  `udp:<host>:<port>`  A syslog server. Replace `<host>:<port>` with the host and port of the syslog server.  `unix:<file>`  A Unix Domain Socket file specified by `<file>`.  `null`  Do not send the audit logs to any additional target. |
| `syslogFacility` | string | The syslog facility, such as `kern`, as defined by RFC5424. The default value is `local0`. |

Show more

Expand

Table 2.14. gatewayConfig object

| Field | Type | Description |
| --- | --- | --- |
| `routingViaHost` | `boolean` | Set this field to `true` to send egress traffic from pods to the host networking stack. For highly-specialized installations and applications that rely on manually configured routes in the kernel routing table, you might want to route egress traffic to the host networking stack. By default, egress traffic is processed in OVN to exit the cluster and is not affected by specialized routes in the kernel routing table. The default value is `false`.  This field has an interaction with the Open vSwitch hardware offloading feature. If you set this field to `true`, you do not receive the performance benefits of the offloading because egress traffic is processed by the host networking stack. |
| `ipForwarding` | `object` | You can control IP forwarding for all traffic on OVN-Kubernetes managed interfaces by using the `ipForwarding` specification in the `Network` resource. Specify `Restricted` to only allow IP forwarding for Kubernetes related traffic. Specify `Global` to allow forwarding of all IP traffic. For new installations, the default is `Restricted`. For updates to OpenShift Container Platform 4.14 or later, the default is `Global`.  Note  The default value of `Restricted` sets the IP forwarding to drop. |
| `ipv4` | `object` | Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv4 addresses. |
| `ipv6` | `object` | Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv6 addresses. |

Show more

Expand

Table 2.15. gatewayConfig.ipv4 object

| Field | Type | Description |
| --- | --- | --- |
| `internalMasqueradeSubnet` | `string` | The masquerade IPv4 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `169.254.169.0/29`.  Important  For OpenShift Container Platform 4.17 and later versions, clusters use `169.254.0.0/17` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet. |

Show more

Expand

Table 2.16. gatewayConfig.ipv6 object

| Field | Type | Description |
| --- | --- | --- |
| `internalMasqueradeSubnet` | `string` | The masquerade IPv6 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `fd69::/125`.  Important  For OpenShift Container Platform 4.17 and later versions, clusters use `fd69::/112` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet. |

Show more

Expand

Table 2.17. ipsecConfig object

| Field | Type | Description |
| --- | --- | --- |
| `mode` | `string` | Specifies the behavior of the IPsec implementation. Must be one of the following values:  * `Disabled`: IPsec is not enabled on cluster nodes. * `External`: IPsec is enabled for network traffic with external hosts. * `Full`: IPsec is enabled for pod traffic and network traffic with external hosts. |

Show more

**Example OVN-Kubernetes configuration with IPSec enabled**

```
defaultNetwork:
  type: OVNKubernetes
  ovnKubernetesConfig:
    mtu: 1400
    genevePort: 6081
    ipsecConfig:
      mode: Full
```

### [2.13. Creating the Kubernetes manifest and Ignition config files](#installation-user-infra-generate-k8s-manifest-ignition_installing-ibm-power) Copy linkLink copied to clipboard!

Because you manually provision infrastructure, you must generate the Kubernetes manifest and Ignition config files that the cluster requires.

The installation program converts the installation configuration into Kubernetes manifests and then wraps them into Ignition configuration files. You use these Ignition files to configure the cluster machines.

Important

* The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which the system then renews. If you shut down the cluster before the system renews the certificates and you later restart the cluster after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
* Use Ignition config files within 12 hours after you generate them, because the 24-hour certificate rotates from 16 to 22 hours after you install the cluster. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

Note

The installation program that generates the manifest and Ignition files is architecture specific. You can obtain it from the [client image mirror](https://mirror.openshift.com/pub/openshift-v4/ppc64le/clients/ocp/latest/). The Linux version of the installation program (without an architecture postfix) runs on ppc64le only. This installation program is also available as a macOS version.

**Prerequisites**

* You obtained the OpenShift Container Platform installation program.
* You created the `install-config.yaml` installation configuration file.

**Procedure**

1. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```

   where:

   `<installation_directory>`
   :   Specifies the installation directory that contains the `install-config.yaml` file you created.

   Warning

   If you are installing a three-node cluster, skip the following step to allow the control plane nodes to be schedulable.

   +

   Important

   When you configure control plane nodes from the default unschedulable to schedulable, you require additional subscriptions because control plane nodes then become compute nodes.
2. Verify that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:

   1. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.
   2. Locate the `mastersSchedulable` parameter and verify that it is set to `false`.
   3. Save and exit the file.
3. To create the Ignition configuration files, run the following command from the directory that contains the installation program:

   ```
   $ ./openshift-install create ignition-configs --dir <installation_directory>
   ```

   where:

   `<installation_directory>`
   :   Specifies the same installation directory.

       The installation program creates Ignition config files for the bootstrap, control plane, and compute nodes in the installation directory. The program also creates the `kubeadmin-password` and `kubeconfig` files in the `./<installation_directory>/auth` directory:

       ```
       .
       ├── auth
       │   ├── kubeadmin-password
       │   └── kubeconfig
       ├── bootstrap.ign
       ├── master.ign
       ├── metadata.json
       └── worker.ign
       ```

### [2.14. Installing RHCOS and starting the OpenShift Container Platform bootstrap process](#ibm-power-upi-installing-rhcos-intro_installing-ibm-power) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on IBM Power® infrastructure that you provision, you must install Red Hat Enterprise Linux CoreOS (RHCOS) on the machines by using an ISO image or network PXE booting.

To install RHCOS, you must give the Ignition config file generated by the OpenShift Container Platform installation program for the type of machine you are installing. If you have configured suitable networking, DNS, and load balancing infrastructure, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS machines have rebooted.

Follow either the steps to use an ISO image or network PXE booting to install RHCOS on the machines.

#### [2.14.1. Installing RHCOS by using an ISO image](#installation-user-infra-machines-iso_installing-ibm-power) Copy linkLink copied to clipboard!

To provision physical or virtual machines, install RHCOS by using a bootable ISO image.

**Prerequisites**

* You have created the Ignition config files for your cluster.
* You have configured a suitable network, DNS, and load balancing infrastructure.
* You have an HTTP server that can be accessed from your computer, and from the machines that you create.
* You have reviewed the *Advanced RHCOS installation configuration* section for different ways to configure features, such as networking and disk partitioning.

**Procedure**

1. Obtain the SHA512 digest for each of your Ignition config files. For example, you can use the following on a system running Linux to get the SHA512 digest for your `bootstrap.ign` Ignition config file:

   ```
   $ sha512sum <installation_directory>/bootstrap.ign
   ```

   The digests are provided to the `coreos-installer` in a later step to validate the authenticity of the Ignition config files on the cluster nodes.
2. Upload the bootstrap, control plane, and compute node Ignition config files that the installation program created to your HTTP server. Note the URLs of these files.

   Important

   You can add or change configuration settings in your Ignition configs before saving them to your HTTP server. If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.
3. From the installation host, validate that the Ignition config files are available on the URLs. The following example gets the Ignition config file for the bootstrap node:

   ```
   $ curl -k http://<HTTP_server>/bootstrap.ign
   ```

   * <HTTP\_server>: Replace `bootstrap.ign` with `master.ign` or `worker.ign` in the command to validate that the Ignition config files for the control plane and compute nodes are also available.

     **Example output**

     ```
       % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                      Dload  Upload   Total   Spent    Left  Speed
       0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{"ignition":{"version":"3.2.0"},"passwd":{"users":[{"name":"core","sshAuthorizedKeys":["ssh-rsa...
     ```
4. Although it is possible to obtain the RHCOS images that are required for your preferred method of installing operating system instances from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/ppc64le/dependencies/rhcos/) page, the recommended way to obtain the correct version of your RHCOS images are from the output of `openshift-install` command:

   ```
   $ openshift-install coreos print-stream-json | grep '\.iso[^.]'
   ```

   **Example output**

   ```
   "location": "<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live.aarch64.iso",
   "location": "<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live.ppc64le.iso",
   "location": "<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live.s390x.iso",
   "location": "<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live.x86_64.iso",
   ```

   Important

   The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. Use only ISO images for this procedure. RHCOS qcow2 images are not supported for this installation type.

   ISO file names resemble the following example:

   `rhcos-<version>-live.<architecture>.iso`
5. Use the ISO to start the RHCOS installation. Use one of the following installation options:

   * Burn the ISO image to a disk and boot it directly.
   * Use ISO redirection by using a lights-out management (LOM) interface.
6. Boot the RHCOS ISO image without specifying any options or interrupting the live boot sequence. Wait for the installer to boot into a shell prompt in the RHCOS live environment.

   Note

   It is possible to interrupt the RHCOS installation boot process to add kernel arguments. However, for this ISO procedure you should use the `coreos-installer` command as outlined in the following steps, instead of adding kernel arguments.
7. Run the `coreos-installer` command and specify the options that meet your installation requirements. At a minimum, you must specify the URL that points to the Ignition config file for the node type, and the device that you are installing to:

   ```
   $ sudo coreos-installer install --ignition-url=http://<HTTP_server>/<node_type>.ign <device> \
   --ignition-hash=sha512-<digest>
   ```

   * `<device>`: You must run the `coreos-installer` command by using `sudo`, because the `core` user does not have the required root privileges to perform the installation.
   * `<digest>`: The `--ignition-hash` option is required when the Ignition config file is obtained through an HTTP URL to validate the authenticity of the Ignition config file on the cluster node. `<digest>` is the Ignition config file SHA512 digest obtained in a preceding step.

     Note

     If you want to provide your Ignition config files through an HTTPS server that uses TLS, you can add the internal certificate authority (CA) to the system trust store before running `coreos-installer`.

     The following example initializes a bootstrap node installation to the `/dev/sda` device. The Ignition config file for the bootstrap node is obtained from an HTTP web server with the IP address 192.168.1.2:

     ```
     $ sudo coreos-installer install --ignition-url=http://192.168.1.2:80/installation_directory/bootstrap.ign /dev/sda \
     --ignition-hash=sha512-a5a2d43879223273c9b60af66b44202a1d1248fc01cf156c46d4a79f552b6bad47bc8cc78ddf0116e80c59d2ea9e32ba53bc807afbca581aa059311def2c3e3b
     ```
8. Monitor the progress of the RHCOS installation on the console of the machine.

   Important

   Be sure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of RHCOS installation issues that might arise.
9. After RHCOS installs, you must reboot the system. During the system reboot, it applies the Ignition config file that you specified.
10. Check the console output to verify that Ignition ran.

    **Example command**

    ```
    Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
    Ignition: user-provided config was applied
    ```
11. Continue to create the other machines for your cluster.

    Important

    You must create the bootstrap and control plane machines at this time. If the control plane machines are not made schedulable, also create at least two compute machines before you install OpenShift Container Platform.

    If the required network, DNS, and load balancer infrastructure are in place, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS nodes have rebooted.

    Note

    RHCOS nodes do not include a default password for the `core` user. You can access the nodes by running `ssh core@<node>.<cluster_name>.<base_domain>` as a user with access to the SSH private key that is paired to the public key that you specified in your `install_config.yaml` file. OpenShift Container Platform 4 cluster nodes running RHCOS are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, when investigating installation issues, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on a target node, SSH access might be required for debugging or disaster recovery.

#### [2.14.2. Networking and bonding options for ISO installations](#installation-user-infra-machines-routing-bonding_installing-ibm-power) Copy linkLink copied to clipboard!

You can configure advanced options so that you can modify the Red Hat Enterprise Linux CoreOS (RHCOS) manual installation process. The subsequent sections show examples of networking options for an ISO installation.

If you install RHCOS from an ISO image, you can add kernel arguments manually when you boot the image to configure networking for a node. If no networking arguments are specified, DHCP is activated in the initramfs when RHCOS detects that networking is required to fetch the Ignition config file.

Important

When adding networking arguments manually, you must also add the `rd.neednet=1` kernel argument to bring the network up in the initramfs.

The following information provides examples for configuring networking and bonding on your RHCOS nodes for ISO installations. The examples describe how to use the `ip=`, `nameserver=`, and `bond=` kernel arguments.

Note

Ordering is important when adding the kernel arguments: `ip=`, `nameserver=`, and then `bond=`.

The networking options are passed to the `dracut` tool during system boot. For more information about the networking options supported by `dracut`, see `dracut.cmdline` manual page.

##### [2.14.2.1. Configuring DHCP or static IP addresses](#configuring-dhcp-or-static-ip-addresses_installing-ibm-power) Copy linkLink copied to clipboard!

You can configure an IP address by using either DHCP or an individual static IP address. If you set a static IP, you must then identify the DNS server IP address on each node.

The configuration examples in the procedure, update the IP addresses for the following components:

* The node’s IP address to `10.10.10.2`
* The gateway address to `10.10.10.254`
* The netmask to `255.255.255.0`
* The hostname to `core0.example.com`
* The DNS server address to `4.4.4.41`
* The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically.

**Procedure**

1. Enter a command like the following command to configure a static IP address:

   ```
   ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
   nameserver=4.4.4.41
   ```
2. Enter a command like the following command to configure a DHCP IP address:

   ```
   ip=enp1s0:dhcp
   ```

   Note

   When you use DHCP to configure IP addressing for the RHCOS machines, the machines also obtain the DNS server information through DHCP. For DHCP-based deployments, you can define the DNS server address that is used by the RHCOS nodes through your DHCP server configuration.
3. If two or more network interfaces and only one interface exists, disable DHCP on a single interface. In the example, the `enp1s0` interface has a static networking configuration and DHCP is disabled for `enp2s0`, which is not used:

   ```
   ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
   ip=::::core0.example.com:enp2s0:none
   ```
4. If you need to combine DHCP and static IP configurations on systems with multiple network interfaces, run the following example command:

   ```
   ip=enp1s0:dhcp
   ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
   ```

##### [2.14.2.2. Configuring an IP address without a static hostname](#configuring-ip-address-without-static-hostname_installing-ibm-power) Copy linkLink copied to clipboard!

You can configure an IP address without assigning a static hostname. If a static hostname is not set by the user, the static hostname gets picked up and automatically set by a reverse DNS lookup.

The configuration examples in the procedure, update the IP addresses for the following components:

* The node’s IP address to `10.10.10.2`
* The gateway address to `10.10.10.254`
* The netmask to `255.255.255.0`
* The DNS server address to `4.4.4.41`
* The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically.

**Procedure**

* To configure an IP address without a static hostname, enter a command like the following command:

  ```
  ip=10.10.10.2::10.10.10.254:255.255.255.0::enp1s0:none
  nameserver=4.4.4.41
  ```

##### [2.14.2.3. Specifying multiple network interfaces and DNS servers](#specifying-multiple-network-interfaces_installing-ibm-power) Copy linkLink copied to clipboard!

You can specify multiple network interfaces by setting multiple `ip=` entries. You can provide multiple DNS servers by adding a `nameserver=` entry for each server,

**Procedure**

* To specify multiple network interfaces for your interfaces, you can enter a command like the following command:

  ```
  ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
  ip=10.10.10.3::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
  ```
* To provide multiple DNS servers by adding a `nameserver=` entry for each server, enter a command like the following command:

  ```
  nameserver=1.1.1.1
  nameserver=8.8.8.8
  ```

##### [2.14.2.4. Configuring default gateway and route](#configuring-default-gateway-route_installing-ibm-power) Copy linkLink copied to clipboard!

As an optional task, you can configure routes to additional networks by setting an `rd.route=` value.

Note

When you configure one or multiple networks, one default gateway is required. If the additional network gateway is different from the primary network gateway, the default gateway must be the primary network gateway.

**Procedure**

* To configure the default gateway, enter the following command:

  ```
  ip=::10.10.10.254::::
  ```
* To configure the route for an additional network, enter the following command:

  ```
  rd.route=20.20.20.0/24:20.20.20.254:enp2s0
  ```

##### [2.14.2.5. Configuring VLANs on individual interfaces](#configuring-vlans-individual-interfaces_installing-ibm-power) Copy linkLink copied to clipboard!

As an optional task, you can configure VLANs on individual interfaces by using the `vlan=` parameter.

**Procedure**

* To configure a VLAN on a network interface and use a static IP address, run the following command:

  ```
  ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0.100:none
  vlan=enp2s0.100:enp2s0
  ```
* To configure a VLAN on a network interface and to use DHCP, run the following command:

  ```
  ip=enp2s0.100:dhcp
  vlan=enp2s0.100:enp2s0
  ```

##### [2.14.2.6. Bonding multiple network interfaces to a single interface](#bonding-multiple-network-interfaces-to-single-interface_installing-ibm-power) Copy linkLink copied to clipboard!

As an optional task, you can bond multiple network interfaces to a single interface by using the `bond=` option.

The following example demonstrates editing the `/etc/config/network` file and specifying the following syntax for bonding multiple network interfaces to a single interface:

```
bond=<name>[:<network_interfaces>][:<options>]
```

* `<name>`: Specifies the bonding device name, for example `bond0`.
* `<network_interfaces>`: Specifies a comma-separated list of physical (ethernet) interfaces, such as `em1,em2`.
* `` <options>: Specifies a comma-separated list of bonding options. Enter the `modinfo bonding `` command to see available options.

When you create a bonded interface using the `bond=` command, you must specify how the IP address is assigned and other information for the bonded interface.

**Procedure**

* To configure the bonded interface to use DHCP, edit the `/etc/config/network` file by setting the IP address for the bond to `dhcp`. For example:

  ```
  ip=bond0:dhcp
  ```
* To configure the bonded interface to use a static IP address, edit the `/etc/config/network` file entering the specific IP address you want and related information. For example:

  ```
  ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
  ```

##### [2.14.2.7. Bonding multiple SR-IOV network interfaces to a dual port NIC interface](#bonding-multiple-sriov-network-interfaces-to-dual-port_installing-ibm-power) Copy linkLink copied to clipboard!

You can bond multiple SR-IOV network interfaces to a dual port NIC interface by using the `bond=` option. Ensure you apply the procedure tasks to each node.

**Procedure**

1. Create the SR-IOV virtual functions (VFs) following the guidance in [Managing SR-IOV devices](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/managing-virtual-devices_configuring-and-managing-virtualization#managing-sr-iov-devices_managing-virtual-devices). Follow the procedure in the "Attaching SR-IOV networking devices to virtual machines" section.
2. Create the bond, attach the desired VFs to the bond and set the bond link state up following the guidance in [Configuring network bonding](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/configuring-network-bonding_configuring-and-managing-networking). Follow any of the described procedures to create the bond.

   The following examples illustrate the syntax you must use:

   * The syntax for configuring a bonded interface is `bond=<name>[:<network_interfaces>][:options]`.

     `<name>` is the bonding device name (`bond0`), `<network_interfaces>` represents the virtual functions (VFs) by their known name in the kernel and shown in the output of the `ip link` command(`eno1f0`, `eno2f0`), and *options* is a comma-separated list of bonding options. Enter `modinfo bonding` to see available options.
   * When you create a bonded interface using `bond=`, you must specify how the IP address is assigned and other information for the bonded interface.

     + To configure the bonded interface to use DHCP, set the bond’s IP address to `dhcp`. For example:

       ```
       bond=bond0:eno1f0,eno2f0:mode=active-backup
       ip=bond0:dhcp::AA:BB:CC:DD:EE:FF
       ip=eno1f0:none::AA:BB:CC:DD:EE:FF
       ip=eno2f0:none::AA:BB:CC:DD:EE:FF
       ```
     + To configure the bonded interface to use a static IP address, enter the specific IP address you want and related information. For example:

       ```
       bond=bond0:eno1f0,eno2f0:mode=active-backup
       ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
       ```

#### [2.14.3. Installing RHCOS by using PXE booting](#installation-user-infra-machines-pxe_installing-ibm-power) Copy linkLink copied to clipboard!

You can use PXE booting to install RHCOS on the machines.

**Prerequisites**

* You have created the Ignition config files for your cluster.
* You have configured a suitable network, DNS and load balancing infrastructure.
* You have configured suitable PXE infrastructure.
* You have an HTTP server that can be accessed from your computer, and from the machines that you create.
* You have reviewed the *Advanced RHCOS installation configuration* section for different ways to configure features, such as networking and disk partitioning.

**Procedure**

1. Upload the bootstrap, control plane, and compute node Ignition config files that the installation program created to your HTTP server. Note the URLs of these files.

   Important

   You can add or change configuration settings in your Ignition configs before saving them to your HTTP server. If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.
2. From the installation host, validate that the Ignition config files are available on the URLs. The following example gets the Ignition config file for the bootstrap node:

   ```
   $ curl -k http://<HTTP_server>/bootstrap.ign
   ```

   * `<HTTP_server>`: Replace `bootstrap.ign` with `master.ign` or `worker.ign` in the command to validate that the Ignition config files for the control plane and compute nodes are also available.

     **Example output**

     ```
       % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                      Dload  Upload   Total   Spent    Left  Speed
       0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{"ignition":{"version":"3.2.0"},"passwd":{"users":[{"name":"core","sshAuthorizedKeys":["ssh-rsa...
     ```
3. Although it is possible to obtain the RHCOS `kernel`, `initramfs` and `rootfs` files that are required for your preferred method of installing operating system instances from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/ppc64le/dependencies/rhcos/) page, the recommended way to obtain the correct version of your RHCOS files are from the output of `openshift-install` command:

   ```
   $ openshift-install coreos print-stream-json | grep -Eo '"https.*(kernel-|initramfs.|rootfs.)\w+(\.img)?"'
   ```

   **Example output**

   ```
   "<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-kernel-aarch64"
   "<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-initramfs.aarch64.img"
   "<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-rootfs.aarch64.img"
   "<url>/art/storage/releases/rhcos-4.22-ppc64le/49.84.202110081256-0/ppc64le/rhcos-<release>-live-kernel-ppc64le"
   "<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live-initramfs.ppc64le.img"
   "<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live-rootfs.ppc64le.img"
   "<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-kernel-s390x"
   "<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-initramfs.s390x.img"
   "<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-rootfs.s390x.img"
   "<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-kernel-x86_64"
   "<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-initramfs.x86_64.img"
   "<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-rootfs.x86_64.img"
   ```

   Important

   The RHCOS artifacts might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described below for this procedure. RHCOS QCOW2 images are not supported for this installation type.

   The file names contain the OpenShift Container Platform version number. They resemble the following examples:

   * `kernel`: `rhcos-<version>-live-kernel-<architecture>`
   * `initramfs`: `rhcos-<version>-live-initramfs.<architecture>.img`
   * `rootfs`: `rhcos-<version>-live-rootfs.<architecture>.img`
4. Upload the `rootfs`, `kernel`, and `initramfs` files to your HTTP server.

   Important

   If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.
5. Configure the network boot infrastructure so that the machines boot from their local disks after RHCOS is installed on them.
6. Configure PXE installation for the RHCOS images and begin the installation.
7. Modify the following example menu entry for your environment and verify that the image and Ignition files are properly accessible:

   ```
   DEFAULT pxeboot
   TIMEOUT 20
   PROMPT 0
   LABEL pxeboot
       KERNEL http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture>
       APPEND initrd=http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign
   ```

   where:

   `kernel`
   :   Specify the location of the live `kernel` file that you uploaded to your HTTP server. The URL must be HTTP, TFTP, or FTP; HTTPS and NFS are not supported.

   `initrd=main`
   :   If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`. Specify the locations of the RHCOS files that you uploaded to your HTTP server. The `initrd` parameter value is the location of the `initramfs` file, the `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file. You can also add more kernel arguments to the `APPEND` line to configure networking or other boot options.

       Note

       This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `APPEND` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information, see [How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?](https://access.redhat.com/articles/7212) and "Enabling the serial console for PXE and ISO installation" in the "Advanced RHCOS installation configuration" section.
8. Monitor the progress of the RHCOS installation on the console of the machine.

   Important

   Be sure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of RHCOS installation issues that might arise.
9. After RHCOS installs, the system reboots. During reboot, the system applies the Ignition config file that you specified.
10. Check the console output to verify that Ignition ran.

    **Example command**

    ```
    Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
    Ignition: user-provided config was applied
    ```
11. Continue to create the machines for your cluster.

    Important

    You must create the bootstrap and control plane machines at this time. If the control plane machines are not made schedulable, also create at least two compute machines before you install the cluster.

    If the required network, DNS, and load balancer infrastructure are in place, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS nodes have rebooted.

    Note

    RHCOS nodes do not include a default password for the `core` user. You can access the nodes by running `ssh core@<node>.<cluster_name>.<base_domain>` as a user with access to the SSH private key that is paired to the public key that you specified in your `install_config.yaml` file. OpenShift Container Platform 4 cluster nodes running RHCOS are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, when investigating installation issues, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on a target node, SSH access might be required for debugging or disaster recovery.

#### [2.14.4. Enabling multipathing with kernel arguments on RHCOS](#rhcos-enabling-multipathday-1-power_installing-ibm-power) Copy linkLink copied to clipboard!

During installation, you can enable multipathing for provisioned nodes on IBM Power®. RHCOS supports multipathing on the primary disk, providing stronger resilience to hardware failure.

During the initial cluster creation, you might want to add kernel arguments to all control plane or worker nodes. To add kernel arguments to control plane or worker nodes, you can create a `MachineConfig` object and inject that object into the set of manifest files used by Ignition during cluster setup.

**Procedure**

1. Change to the directory that contains the installation program and generate the Kubernetes manifests for the cluster:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```
2. Decide if you want to add kernel arguments to worker or control plane nodes.

   * Create a machine config file. For example, create a `99-master-kargs-mpath.yaml` that instructs the cluster to add the control plane label and identify the multipath kernel argument:

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
3. To enable multipathing on worker nodes:

   * Create a machine config file. For example, create a `99-worker-kargs-mpath.yaml` that instructs the cluster to add the compute label and identify the multipath kernel argument:

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

     You can now continue on to create the cluster.

Important

Additional postinstallation steps are required to fully enable multipathing. For more information, see "Enabling multipathing with kernel arguments on RHCOS" in *Postinstallation machine configuration tasks*.

In case of MPIO failure, use the `bootlist` command to update the boot device list with alternate logical device names. The command displays a boot list and designates the possible boot devices for when the system is booted in normal mode.

1. To display a boot list and specify the possible boot devices if the system is booted in normal mode, enter the following command:

   ```
   $ bootlist -m normal -o
   sda
   ```
2. To update the boot list for normal mode and add alternate device names, enter the following command:

   ```
   $ bootlist -m normal -o /dev/sdc /dev/sdd /dev/sde
   sdc
   sdd
   sde
   ```

   If the original boot disk path is down, the node reboots from the alternate device registered in the normal boot device list.

### [2.15. Waiting for the bootstrap process to complete](#installation-installing-bare-metal_installing-ibm-power) Copy linkLink copied to clipboard!

The OpenShift Container Platform bootstrap process begins after the cluster nodes first boot into the persistent RHCOS environment that has been installed to disk. The configuration information provided through the Ignition config files is used to initialize the bootstrap process and install OpenShift Container Platform on the machines. You must wait for the bootstrap process to complete.

**Prerequisites**

* You have created the Ignition config files for your cluster.
* You have configured suitable network, DNS, and load balancing infrastructure.
* You have obtained the installation program and generated the Ignition config files for your cluster.
* You installed RHCOS on your cluster machines and provided the Ignition config files that the OpenShift Container Platform installation program generated.
* Your machines have direct internet access or have an HTTP or HTTPS proxy available.

**Procedure**

1. Monitor the bootstrap process:

   ```
   $ ./openshift-install --dir <installation_directory> wait-for bootstrap-complete \
       --log-level=info
   ```

   where:

   `<installation_directory>`
   :   Specifies the path to the directory that stores the installation files.

   `--log-level=info`
   :   Specifies `warn`, `debug`, or `error` instead of `info` to view different installation details.

       **Example output**

       ```
       INFO Waiting up to 20m0s for the Kubernetes API at https://api.test.example.com:6443...
       INFO API v1.35.4 up
       INFO Waiting up to 1h0m0s for bootstrapping to complete...
       INFO It is now safe to remove the bootstrap resources
       ```

       The bootstrapping completion wait time varies per platform.

       The command succeeds when the Kubernetes API server signals that it has been bootstrapped on the control plane machines.
2. After the bootstrap process is complete, remove the bootstrap machine from the load balancer.

   Important

   You must remove the bootstrap machine from the load balancer at this point. You can also remove or reformat the bootstrap machine itself.

### [2.16. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-ibm-power) Copy linkLink copied to clipboard!

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and OpenShift Container Platform generates it during installation.

**Prerequisites**

* You deployed an OpenShift Container Platform cluster.
* You installed the OpenShift CLI (`oc`).

**Procedure**

1. Export the `kubeadmin` credentials by running the following command:

   ```
   $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
   ```

   where:

   `<installation_directory>`
   :   Specifies the path to the directory that stores the installation files.
2. Verify you can run `oc` commands successfully using the exported configuration by running the following command:

   ```
   $ oc whoami
   ```

   **Example output**

   ```
   system:admin
   ```

**Next steps**

* "Customize your cluster"
* "Remote health reporting"

### [2.17. Approving the certificate signing requests for your machines](#installation-approve-csrs_installing-ibm-power) Copy linkLink copied to clipboard!

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

### [2.18. Initial Operator configuration](#installation-operators-config_installing-ibm-power) Copy linkLink copied to clipboard!

After the control plane initializes, you must immediately configure some Operators so that they all become available.

**Prerequisites**

* Your control plane has initialized.

**Procedure**

1. Watch the cluster components come online:

   ```
   $ watch -n5 oc get clusteroperators
   ```

   **Example output**

   ```
   NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
   authentication                             4.22.0    True        False         False      19m
   baremetal                                  4.22.0    True        False         False      37m
   cloud-credential                           4.22.0    True        False         False      40m
   cluster-autoscaler                         4.22.0    True        False         False      37m
   config-operator                            4.22.0    True        False         False      38m
   console                                    4.22.0    True        False         False      26m
   csi-snapshot-controller                    4.22.0    True        False         False      37m
   dns                                        4.22.0    True        False         False      37m
   etcd                                       4.22.0    True        False         False      36m
   image-registry                             4.22.0    True        False         False      31m
   ingress                                    4.22.0    True        False         False      30m
   insights                                   4.22.0    True        False         False      31m
   kube-apiserver                             4.22.0    True        False         False      26m
   kube-controller-manager                    4.22.0    True        False         False      36m
   kube-scheduler                             4.22.0    True        False         False      36m
   kube-storage-version-migrator              4.22.0    True        False         False      37m
   machine-api                                4.22.0    True        False         False      29m
   machine-approver                           4.22.0    True        False         False      37m
   machine-config                             4.22.0    True        False         False      36m
   marketplace                                4.22.0    True        False         False      37m
   monitoring                                 4.22.0    True        False         False      29m
   network                                    4.22.0    True        False         False      38m
   node-tuning                                4.22.0    True        False         False      37m
   openshift-apiserver                        4.22.0    True        False         False      32m
   openshift-controller-manager               4.22.0    True        False         False      30m
   openshift-samples                          4.22.0    True        False         False      32m
   operator-lifecycle-manager                 4.22.0    True        False         False      37m
   operator-lifecycle-manager-catalog         4.22.0    True        False         False      37m
   operator-lifecycle-manager-packageserver   4.22.0    True        False         False      32m
   service-ca                                 4.22.0    True        False         False      38m
   storage                                    4.22.0    True        False         False      37m
   ```
2. Configure the Operators that are not available.

#### [2.18.1. Image registry storage configuration](#installation-registry-storage-config_installing-ibm-power) Copy linkLink copied to clipboard!

The Image Registry Operator is not initially available for platforms that do not provide default storage. After installation, you must configure your registry to use storage so that the Registry Operator is made available.

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters.

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades.

##### [2.18.1.1. Configuring registry storage for IBM Power](#registry-configuring-storage-baremetal_installing-ibm-power) Copy linkLink copied to clipboard!

As a cluster administrator, following installation you must configure your registry to use storage.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have a cluster on IBM Power®.
* You have provisioned persistent storage for your cluster, such as Red Hat OpenShift Data Foundation.

  Important

  OpenShift Container Platform supports `ReadWriteOnce` access for image registry storage when you have only one replica. `ReadWriteOnce` access also requires that the registry uses the `Recreate` rollout strategy. To deploy an image registry that supports high availability with two or more replicas, `ReadWriteMany` access is required.
* You must have a system with at least 100Gi capacity.

**Procedure**

1. To configure your registry to use storage, change the `spec.storage.pvc` in the `configs.imageregistry/cluster` resource.

   Note

   When you use shared storage, review your security settings to prevent outside access.
2. Verify that you do not have a registry pod:

   ```
   $ oc get pod -n openshift-image-registry -l docker-registry=default
   ```

   **Example output**

   ```
   No resources found in openshift-image-registry namespace
   ```

   Note

   If you do have a registry pod in your output, you do not need to continue with this procedure.
3. Check the registry configuration:

   ```
   $ oc edit configs.imageregistry.operator.openshift.io
   ```

   **Example output**

   ```
   storage:
     pvc:
       claim:
   ```

   Leave the `claim` field blank to allow the automatic creation of an `image-registry-storage` PVC.
4. Check the `clusteroperator` status:

   ```
   $ oc get clusteroperator image-registry
   ```

   **Example output**

   ```
   NAME             VERSION              AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
   image-registry   4.22                 True        False         False      6h50m
   ```
5. Ensure that your registry is set to managed to enable building and pushing of images.

   * Run:

     ```
     $ oc edit configs.imageregistry/cluster
     ```

     Then, change the line

     ```
     managementState: Removed
     ```

     to

     ```
     managementState: Managed
     ```

##### [2.18.1.2. Configuring storage for the image registry in non-production clusters](#installation-registry-storage-non-production_installing-ibm-power) Copy linkLink copied to clipboard!

You must configure storage for the Image Registry Operator. For non-production clusters, you can set the image registry to an empty directory, but you lose all images if you restart the registry.

**Procedure**

* To set the image registry storage to an empty directory:

  ```
  $ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"storage":{"emptyDir":{}}}}'
  ```

  Warning

  Configure this option only for non-production clusters.

  If you run this command before the Image Registry Operator initializes its components, the `oc patch` command fails with the following error:

  **Example output**

  ```
  Error from server (NotFound): configs.imageregistry.operator.openshift.io "cluster" not found
  ```

  Wait a few minutes and run the command again.

### [2.19. Completing installation on user-provisioned infrastructure](#installation-complete-user-infra_installing-ibm-power) Copy linkLink copied to clipboard!

To finalize the installation on user-provisioned infrastructure, complete the cluster deployment after configuring the Operators. This ensures the cluster is fully operational on the infrastructure that you provide.

**Prerequisites**

* Your control plane has initialized.
* You have completed the initial Operator configuration.

**Procedure**

1. Confirm that all the cluster components are online with the following command:

   ```
   $ watch -n5 oc get clusteroperators
   ```

   **Example output**

   ```
   NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
   authentication                             4.22.0    True        False         False      19m
   baremetal                                  4.22.0    True        False         False      37m
   cloud-credential                           4.22.0    True        False         False      40m
   cluster-autoscaler                         4.22.0    True        False         False      37m
   config-operator                            4.22.0    True        False         False      38m
   console                                    4.22.0    True        False         False      26m
   csi-snapshot-controller                    4.22.0    True        False         False      37m
   dns                                        4.22.0    True        False         False      37m
   etcd                                       4.22.0    True        False         False      36m
   image-registry                             4.22.0    True        False         False      31m
   ingress                                    4.22.0    True        False         False      30m
   insights                                   4.22.0    True        False         False      31m
   kube-apiserver                             4.22.0    True        False         False      26m
   kube-controller-manager                    4.22.0    True        False         False      36m
   kube-scheduler                             4.22.0    True        False         False      36m
   kube-storage-version-migrator              4.22.0    True        False         False      37m
   machine-api                                4.22.0    True        False         False      29m
   machine-approver                           4.22.0    True        False         False      37m
   machine-config                             4.22.0    True        False         False      36m
   marketplace                                4.22.0    True        False         False      37muser
   monitoring                                 4.22.0    True        False         False      29m
   network                                    4.22.0    True        False         False      38m
   node-tuning                                4.22.0    True        False         False      37m
   openshift-apiserver                        4.22.0    True        False         False      32muser
   openshift-controller-manager               4.22.0    True        False         False      30m
   openshift-samples                          4.22.0    True        False         False      32m
   operator-lifecycle-manager                 4.22.0    True        False         False      37m
   operator-lifecycle-manager-catalog         4.22.0    True        False         False      37m
   operator-lifecycle-manager-packageserver   4.22.0    True        False         False      32m
   service-ca                                 4.22.0    True        False         False      38m
   storage                                    4.22.0    True        False         False      37m
   ```

   Alternatively, the following command notifies you when all of the clusters are available. The command also retrieves and displays credentials:

   ```
   $ ./openshift-install --dir <installation_directory> wait-for install-complete
   ```

   where:

   `<installation_directory>`
   :   Specifies the path to the directory that you stored the installation files in.

       **Example output**

       ```
       INFO Waiting up to 30m0s for the cluster to initialize...
       ```

       The command succeeds when the Cluster Version Operator finishes deploying the OpenShift Container Platform cluster from Kubernetes API server.

       Important

       * The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
       * It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
2. Confirm that the Kubernetes API server is communicating with the pods.

   1. To view a list of all pods, use the following command:

      ```
      $ oc get pods --all-namespaces
      ```

      **Example output**

      ```
      NAMESPACE                         NAME                                            READY   STATUS      RESTARTS   AGE
      openshift-apiserver-operator      openshift-apiserver-operator-85cb746d55-zqhs8   1/1     Running     1          9m
      openshift-apiserver               apiserver-67b9g                                 1/1     Running     0          3m
      openshift-apiserver               apiserver-ljcmx                                 1/1     Running     0          1m
      openshift-apiserver               apiserver-z25h4                                 1/1     Running     0          2m
      openshift-authentication-operator authentication-operator-69d5d8bf84-vh2n8        1/1     Running     0          5m
      ```
   2. View the logs for a pod that is listed in the output of the previous command by using the following command:

      ```
      $ oc logs <pod_name> -n <namespace>
      ```

      where:

      `<namespace>`
      :   Specifies the pod name and namespace, as shown in the output of an earlier command.

          If the pod logs display, the Kubernetes API server can communicate with the cluster machines.
3. Additional steps are required to enable multipathing. Do not enable multipathing during installation.

   See "Enabling multipathing with kernel arguments on RHCOS" in the *Postinstallation machine configuration tasks* documentation for more information.

### [2.20. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-ibm-power) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

## [Chapter 3. Installing a cluster on IBM Power in a disconnected environment](#installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You can install OpenShift Container Platform on IBM Power® infrastructure that you provision in a disconnected environment by mirroring the required release images to an internal registry and then running the installation program.

Important

Additional considerations exist for non-bare metal platforms. Review the guidelines for deploying OpenShift Container Platform on non-tested platforms before you install an OpenShift Container Platform cluster.

### [3.1. Prerequisites for installing a cluster on IBM Power in a disconnected environment](#prereqs-ibm-power-upi-disconnected_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

Before you install a OpenShift Container Platform cluster on IBM Power® in a restricted network, complete the prerequisite tasks to mirror images and prepare your environment.

* You reviewed details about the OpenShift Container Platform installation and update processes.
* You read the documentation on selecting a cluster installation method and preparing it for users.
* You created a mirror registry for installation in a restricted network and obtained the `imageContentSources` data for your version of OpenShift Container Platform.
* Before you begin the installation process, you must move or remove any existing installation files. This ensures that the installation program creates and updates the required installation files.

  Important

  Perform installation steps on a machine with access to the installation media.
* You provisioned persistent storage using OpenShift Data Foundation or other supported storage protocols for your cluster. To deploy a private image registry, you must set up persistent storage with `ReadWriteMany` access.
* If you use a firewall and plan to use the Telemetry service, you configured the firewall to allow the sites that your cluster requires access to.

  Note

  Be sure to also review this site list if you are configuring a proxy.

### [3.2. About installations in restricted networks](#installation-about-restricted-networks_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You can install OpenShift Container Platform 4.22 in a restricted network without an active internet connection to obtain software components. Restricted network installations can use installer-provisioned or user-provisioned infrastructure, depending on the cloud platform to which you are installing the cluster.

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and has the installation media. You can create this registry on a mirror host, which can access both the internet and your closed network, or by using other methods that meet your restrictions.

Important

Because of the complexity of the configuration for user-provisioned installations, consider completing a standard user-provisioned infrastructure installation before you try a restricted network installation using user-provisioned infrastructure. Completing this test installation might make it easier to isolate and troubleshoot any issues that might arise during your installation in a restricted network.

#### [3.2.1. Additional limits](#installation-restricted-network-limits_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

Clusters in restricted networks have the following additional limitations and restrictions:

* The `ClusterVersion` status includes an `Unable to retrieve available updates` error.
* By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags.

### [3.3. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to obtain the images that are necessary to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

### [3.4. Requirements for a cluster with user-provisioned infrastructure](#ibm-power-upi-requirements-intro_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

For a OpenShift Container Platform cluster with user-provisioned infrastructure on IBM Power®, you must deploy all required machines meeting the hardware, network, DNS, and load balancing requirements.

#### [3.4.1. Required machines for cluster installation](#installation-machine-requirements_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

Important

For a cluster that has user-provisioned infrastructure, you must deploy all of the required machines.

Expand

Table 3.1. Minimum required hosts

| Hosts | Description |
| --- | --- |
| One temporary bootstrap machine | The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster. |
| Three control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| At least two compute machines, which are also known as worker machines. | The workloads requested by OpenShift Container Platform users run on the compute machines. |

Show more

Important

To keep high availability of your cluster, use separate physical hosts for these cluster machines.

The bootstrap, control plane, and compute machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system.

RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.8 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits).

#### [3.4.2. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 3.2. Minimum resource requirements

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | RHCOS | 2 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 2 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Show more

* One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
* OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance.

Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* ppc64le architecture requires IBM® Power9 ISA
* s390x architecture requires IBM® z14 ISA

For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

#### [3.4.3. Minimum IBM Power requirements](#minimum-ibm-power-system-requirements_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform on IBM Power®, verify that your hardware meets the minimum system requirements for processor, disk storage, network, and memory.

* IBM Power®9, IBM Power®10 or IBM Power®11 processor-based systems

##### [3.4.3.1. Hardware requirements](#hardware-requirements-3) Copy linkLink copied to clipboard!

* Six logical partitions (LPARs) across multiple PowerVM servers

##### [3.4.3.2. Operating system requirements](#operating-system-requirements-3) Copy linkLink copied to clipboard!

* One instance of an IBM Power®9, Power10 or Power11 processor-based system

On your IBM Power® instance, set up:

* Three LPARs for OpenShift Container Platform control plane machines
* Two LPARs for OpenShift Container Platform compute machines
* One LPAR for the temporary OpenShift Container Platform bootstrap machine

##### [3.4.3.3. Disk storage for the IBM Power guest virtual machines](#disk-storage-for-the-ibm-power-guest-virtual-machines-3) Copy linkLink copied to clipboard!

* Local storage, or storage provisioned by the Virtual I/O Server using vSCSI, NPIV (N-Port ID Virtualization), Fibre Channel, multipath, or SSP (shared storage pools)

##### [3.4.3.4. Network for the PowerVM guest virtual machines](#network-for-the-powervm-guest-virtual-machines-3) Copy linkLink copied to clipboard!

* Dedicated physical adapter, or SR-IOV virtual function
* Available by the Virtual I/O Server using Shared Ethernet Adapter
* Virtualized by the Virtual I/O Server using IBM® virtual NIC (vNIC)

##### [3.4.3.5. Storage / main memory](#storage-main-memory-3) Copy linkLink copied to clipboard!

* 500 GB / 16 GB for OpenShift Container Platform control plane machines
* 500 GB / 8 GB for OpenShift Container Platform compute machines
* 500 GB / 16 GB for the temporary OpenShift Container Platform bootstrap machine

#### [3.4.4. Recommended IBM Power system requirements](#recommended-ibm-power-system-requirements_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

OpenShift Container Platform on IBM Power® requires a minimum of six LPARs across multiple PowerVM servers, with specific hardware, storage, and network configuration for each node type.

##### [3.4.4.1. Hardware requirements](#hardware-requirements-4) Copy linkLink copied to clipboard!

* Six LPARs across multiple PowerVM servers

##### [3.4.4.2. Operating system requirements](#operating-system-requirements-4) Copy linkLink copied to clipboard!

* One instance of an IBM Power®9, IBM Power®10 or IBM Power®11 processor-based system

On your IBM Power® instance, set up:

* Three LPARs for OpenShift Container Platform control plane machines
* Two LPARs for OpenShift Container Platform compute machines
* One LPAR for the temporary OpenShift Container Platform bootstrap machine

##### [3.4.4.3. Disk storage for the IBM Power guest virtual machines](#disk-storage-for-the-ibm-power-guest-virtual-machines-4) Copy linkLink copied to clipboard!

* Local storage, or storage provisioned by the Virtual I/O Server using vSCSI, NPIV (N-Port ID Virtualization) or SSP (shared storage pools)

##### [3.4.4.4. Network for the PowerVM guest virtual machines](#network-for-the-powervm-guest-virtual-machines-4) Copy linkLink copied to clipboard!

* Dedicated physical adapter, or SR-IOV virtual function
* Virtualized by the Virtual I/O Server using Shared Ethernet Adapter
* Virtualized by the Virtual I/O Server using IBM® virtual NIC (vNIC)

##### [3.4.4.5. Storage / main memory](#storage-main-memory-4) Copy linkLink copied to clipboard!

* 120 GB / 32 GB for OpenShift Container Platform control plane machines
* 120 GB / 32 GB for OpenShift Container Platform compute machines
* 120 GB / 16 GB for the temporary OpenShift Container Platform bootstrap machine

#### [3.4.5. Certificate signing requests management](#csr-management_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

On user-provisioned infrastructure, you must implement a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that kubelet credentials request because it cannot confirm that the correct machine issued the request. You must find and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

#### [3.4.6. Networking requirements for user-provisioned infrastructure](#installation-network-user-infra_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files.

During the initial boot, the machines require an IP address configuration that is set either through a DHCP server or statically by providing the required boot options. After a network connection is established, the machines download their Ignition config files from an HTTP or HTTPS server. The Ignition config files are then used to set the exact state of each machine. The Machine Config Operator completes more changes to the machines, such as the application of new certificates or keys, after installation.

Note

* Consider using a DHCP server for long-term management of the cluster machines. Ensure that the DHCP server is configured to provide persistent IP addresses, DNS server information, and hostnames to the cluster machines.
* If a DHCP service is not available for your user-provisioned infrastructure, you can instead provide the IP networking configuration and the address of the DNS server to the nodes at RHCOS install time. These can be passed as boot arguments if you are installing from an ISO image. See the *Installing RHCOS and starting the OpenShift Container Platform bootstrap process* section for more information about static IP provisioning and advanced networking options.

The Kubernetes API server must be able to resolve the node names of the cluster machines. If the API servers and worker nodes are in different zones, you can configure a default DNS search zone to allow the API server to resolve the node names. Another supported approach is to always refer to hosts by their fully-qualified domain names in both the node objects and all DNS requests.

##### [3.4.6.1. Setting the cluster node hostnames through DHCP](#installation-host-names-dhcp-user-infra_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

On Red Hat Enterprise Linux CoreOS (RHCOS) machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start prior to this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node.

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation.

##### [3.4.6.2. Network connectivity requirements](#installation-network-connectivity-user-infra_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster.

This section provides details about the ports that are required.

Expand

Table 3.3. Ports used for all-machine to all-machine communications

| Protocol | Port | Description |
| --- | --- | --- |
| ICMP | N/A | Network reachability tests |
| TCP | `1936` | Metrics |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101` and the Cluster Version Operator on port `9099`. |
| `10250`-`10259` | The default ports that Kubernetes reserves |
| `22623` | The port handles traffic from the Machine Config Server and directs the traffic to the control plane machines. |
| UDP | `6081` | Geneve |
| `9000`-`9999` | Host level services, including the node exporter on ports `9100`-`9101`. |
| `500` | IPsec IKE packets |
| `4500` | IPsec NAT-T packets |
| `123` | Network Time Protocol (NTP) on UDP port `123`. If an external NTP time server is configured, you must open UDP port `123`. |
| TCP/UDP | `30000`-`32767` |
| Kubernetes node port | ESP | N/A |

Show more

Expand

Table 3.4. Ports used for all-machine to control plane communications

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | `6443` | Kubernetes API |

Show more

Expand

Table 3.5. Ports used for control plane machine to control plane machine communications

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | `2379`-`2380` | etcd server and peer ports |

Show more

##### [3.4.6.3. NTP configuration for user-provisioned infrastructure](#ntp-configuration-for-user-provisioned-infrastructure-2) Copy linkLink copied to clipboard!

OpenShift Container Platform clusters are configured to use a public Network Time Protocol (NTP) server by default. If you want to use a local enterprise NTP server, or if your cluster is being deployed in a disconnected network, you can configure the cluster to use a specific time server. For more information, see the documentation for *Configuring chrony time service*.

If a DHCP server provides NTP server information, the chrony time service on the Red Hat Enterprise Linux CoreOS (RHCOS) machines read the information and can sync the clock with the NTP servers.

#### [3.4.7. User-provisioned DNS requirements](#installation-dns-user-infra_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

In OpenShift Container Platform deployments, you must ensure that cluster components meet certain DNS name resolution criteria for internal communication, certificate validation, and automated node discovery purposes.

The following is a list of required cluster components:

* The Kubernetes API
* The OpenShift Container Platform application wildcard
* The bootstrap and control plane machines
* The compute machines

Reverse DNS resolution is also required for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate.

Note

It is recommended to use a DHCP server to provide the hostnames to each cluster node. See the *DHCP recommendations for user-provisioned infrastructure* section for more information.

The following DNS records are required for a user-provisioned OpenShift Container Platform cluster and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

Expand

Table 3.6. Required DNS records

| Component | Record | Description |
| --- | --- | --- |
| Kubernetes API | `api.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |
| `api-int.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.  Important  The API server must be able to resolve the worker nodes by the hostnames that are recorded in Kubernetes. If the API server cannot resolve the node names, then proxied API calls can fail, and you cannot retrieve logs from pods. |
| Routes | `*.apps.<cluster_name>.<base_domain>.` | A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.  For example, `console-openshift-console.apps.<cluster_name>.<base_domain>` is used as a wildcard route to the OpenShift Container Platform console. |
| Bootstrap machine | `bootstrap.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the bootstrap machine. These records must be resolvable by the nodes within the cluster. |
| Control plane machines | `<control_plane><n>.<cluster_name>.<base_domain>.` | DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the control plane nodes. These records must be resolvable by the nodes within the cluster. |
| Compute machines | `<compute><n>.<cluster_name>.<base_domain>.` | DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the worker nodes. These records must be resolvable by the nodes within the cluster. |

Show more

Note

In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration.

Tip

You can use the `dig` command to verify name and reverse name resolution. See the section on *Validating DNS resolution for user-provisioned infrastructure* for detailed validation steps.

##### [3.4.7.1. Example DNS configuration for user-provisioned clusters](#installation-dns-user-infra-example_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

Reference the example DNS configurations to understand how A and PTR record configuration samples meet the DNS requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

The DNS configuration examples provided here are for reference only and are not meant to provide advice for choosing one DNS solution over another.

In the examples, the cluster name is `ocp4` and the base domain is `example.com`.

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
control-plane2.ocp4.example.com.	IN	A	192.168.1.99
;
compute0.ocp4.example.com.	IN	A	192.168.1.11
compute1.ocp4.example.com.	IN	A	192.168.1.7
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

`compute0.ocp4.example.com.`
:   Provides name resolution for the compute machines.

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
99.1.168.192.in-addr.arpa.	IN	PTR	control-plane2.ocp4.example.com.
;
11.1.168.192.in-addr.arpa.	IN	PTR	compute0.ocp4.example.com.
7.1.168.192.in-addr.arpa.	IN	PTR	compute1.ocp4.example.com.
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

`compute0.ocp4.example.com.`
:   Provides reverse DNS resolution for the compute machines.

Note

A PTR record is not required for the OpenShift Container Platform application wildcard.

#### [3.4.8. Load balancing requirements for user-provisioned infrastructure](#installation-load-balancing-user-infra_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform, you must provision the API and application Ingress load balancing infrastructure. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

Note

If you want to deploy the API and application Ingress load balancers with a Red Hat Enterprise Linux (RHEL) instance, you must purchase the RHEL subscription separately.

The load balancing infrastructure must meet the following requirements:

* API load balancer: Provides a common endpoint for users, both human and machine, to interact with and configure the platform. Configure the following conditions:

  + Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode.
  + A stateless load balancing algorithm. The options vary based on the load balancer implementation.

Important

Do not configure session persistence for an API load balancer. Configuring session persistence for a Kubernetes API server might cause performance issues from excess application traffic for your OpenShift Container Platform cluster and the Kubernetes API that runs inside the cluster.

Configure the following ports on both the front and back of the API load balancers:

Expand

| Port | Back-end machines (pool members) | Internal | External | Description |
| --- | --- | --- | --- | --- |
| `6443` | Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane. You must configure the `/readyz` endpoint for the API server health check probe. | X | X | Kubernetes API server |
| `22623` | Bootstrap and control plane. You remove the bootstrap machine from the load balancer after the bootstrap machine initializes the cluster control plane. | X |  | Machine config server |

Show more

Note

The load balancer must be configured to take a maximum of 30 seconds from the time the API server turns off the `/readyz` endpoint to the removal of the API server instance from the pool. Within the time frame after `/readyz` returns an error or becomes healthy, the endpoint must have been removed or added. Probing every 5 or 10 seconds, with two successful requests to become healthy and three to become unhealthy, are well-tested values.

* Application Ingress load balancer: Provides an ingress point for application traffic flowing in from outside the cluster. A working configuration for the Ingress router is required for an OpenShift Container Platform cluster. Configure the following conditions:

  + Layer 4 load balancing only. This can be referred to as Raw TCP or SSL Passthrough mode.
  + A connection-based or session-based persistence is recommended, based on the options available and types of applications that will be hosted on the platform.

Tip

If the true IP address of the client can be seen by the application Ingress load balancer, enabling source IP-based session persistence can improve performance for applications that use end-to-end TLS encryption.

Configure the following ports on both the front and back of the load balancers:

Expand

Table 3.7. Application Ingress load balancer

| Port | Back-end machines (pool members) | Internal | External | Description |
| --- | --- | --- | --- | --- |
| `443` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTPS traffic |
| `80` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTP traffic |

Show more

Note

If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.

##### [3.4.8.1. Example load balancer configuration for user-provisioned clusters](#installation-load-balancing-user-infra-example_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

Reference the example API and application Ingress load balancer configuration so that you can understand how to meet the load balancing requirements for user-provisioned clusters.

The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another.

Tip

If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node.

In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

Note

If you are using HAProxy as a load balancer and SELinux is set to `enforcing`, you must ensure that the HAProxy service can bind to the configured TCP port by running `setsebool -P haproxy_connect_any=1`.

**Sample API and application Ingress load balancer configuration**

```
global
  log         127.0.0.1 local2
  pidfile     /var/run/haproxy.pid
  maxconn     4000
  daemon
defaults
  mode                    http
  log                     global
  option                  dontlognull
  option http-server-close
  option                  redispatch
  retries                 3
  timeout http-request    10s
  timeout queue           1m
  timeout connect         10s
  timeout client          1m
  timeout server          1m
  timeout http-keep-alive 10s
  timeout check           10s
  maxconn                 3000
listen api-server-6443
  bind *:6443
  mode tcp
  option  httpchk GET /readyz HTTP/1.0
  option  log-health-checks
  balance roundrobin
  server bootstrap bootstrap.ocp4.example.com:6443 verify none check check-ssl inter 10s fall 2 rise 3 backup
  server master0 master0.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master1 master1.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
  server master2 master2.ocp4.example.com:6443 weight 1 verify none check check-ssl inter 10s fall 2 rise 3
listen machine-config-server-22623
  bind *:22623
  mode tcp
  server bootstrap bootstrap.ocp4.example.com:22623 check inter 1s backup
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443
  bind *:443
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:443 check inter 1s
  server compute1 compute1.ocp4.example.com:443 check inter 1s
listen ingress-router-80
  bind *:80
  mode tcp
  balance source
  server compute0 compute0.ocp4.example.com:80 check inter 1s
  server compute1 compute1.ocp4.example.com:80 check inter 1s
```

where:

`listen api-server-6443`
:   Port `6443` handles the Kubernetes API traffic and points to the control plane machines. You must configure health checks on this port to ensure that the API server is available before routing traffic.

`server bootstrap bootstrap.ocp4.example.com`
:   The bootstrap entries must be in place before the OpenShift Container Platform cluster installation and they must be removed after the bootstrap process is complete.

`listen machine-config-server`
:   Port `22623` handles the machine config server traffic and points to the control plane machines.

`listen ingress-router-443`
:   Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.

`listen ingress-router-80`
:   Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.

    Note

    If you are deploying a compact three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.

### [3.5. Preparing the user-provisioned infrastructure](#installation-infrastructure-user-infra_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform on user-provisioned infrastructure, you must prepare the underlying infrastructure.

This section provides details about the high-level steps required to set up your cluster infrastructure in preparation for an OpenShift Container Platform installation. This includes configuring IP networking and network connectivity for your cluster nodes, enabling the required ports through your firewall, and setting up the required DNS and load balancing infrastructure.

After preparation, your cluster infrastructure must meet the requirements outlined in the *Requirements for a cluster with user-provisioned infrastructure* section.

**Prerequisites**

* You have reviewed the [OpenShift Container Platform 4.x Tested Integrations](https://access.redhat.com/articles/4128421) page.
* You have reviewed the infrastructure requirements detailed in the *Requirements for a cluster with user-provisioned infrastructure* section.

**Procedure**

1. If you are using DHCP to provide the IP networking configuration to your cluster nodes, configure your DHCP service.

   1. Add persistent IP addresses for the nodes to your DHCP server configuration. In your configuration, match the MAC address of the relevant network interface to the intended IP address for each node.
   2. When you use DHCP to configure IP addressing for the cluster machines, the machines also obtain the DNS server information through DHCP. Define the persistent DNS server address that is used by the cluster nodes through your DHCP server configuration.

      Note

      If you are not using a DHCP service, you must provide the IP networking configuration and the address of the DNS server to the nodes at RHCOS install time. These can be passed as boot arguments if you are installing from an ISO image. See the *Installing RHCOS and starting the OpenShift Container Platform bootstrap process* section for more information about static IP provisioning and advanced networking options.
   3. Define the hostnames of your cluster nodes in your DHCP server configuration. See the *Setting the cluster node hostnames through DHCP* section for details about hostname considerations.

      Note

      If you are not using a DHCP service, the cluster nodes obtain their hostname through a reverse DNS lookup.
2. Ensure that your network infrastructure provides the required network connectivity between the cluster components. See the *Networking requirements for user-provisioned infrastructure* section for details about the requirements.
3. Configure your firewall to enable the ports required for the OpenShift Container Platform cluster components to communicate. See *Networking requirements for user-provisioned infrastructure* section for details about the ports that are required.

   Important

   By default, port `1936` is accessible for an OpenShift Container Platform cluster, because each control plane node needs access to this port.

   For ingress health check probes, the `/healthz/ready` endpoint is available on this port.

   Avoid using the Ingress load balancer to expose this port, because doing so might result in the exposure of sensitive information, such as statistics and metrics, related to Ingress Controllers.
4. Setup the required DNS infrastructure for your cluster.

   1. Configure DNS name resolution for the Kubernetes API, the application wildcard, the bootstrap machine, the control plane machines, and the compute machines.
   2. Configure reverse DNS resolution for the Kubernetes API, the bootstrap machine, the control plane machines, and the compute machines.

      See the *User-provisioned DNS requirements* section for more information about the OpenShift Container Platform DNS requirements.
5. Validate your DNS configuration.

   1. From your installation node, run DNS lookups against the record names of the Kubernetes API, the wildcard routes, and the cluster nodes. Validate that the IP addresses in the responses correspond to the correct components.
   2. From your installation node, run reverse DNS lookups against the IP addresses of the load balancer and the cluster nodes. Validate that the record names in the responses correspond to the correct components.

      See the *Validating DNS resolution for user-provisioned infrastructure* section for detailed DNS validation steps.
6. Provision the required API and application ingress load balancing infrastructure. See the *Load balancing requirements for user-provisioned infrastructure* section for more information about the requirements.

   Note

   Some load balancing solutions require the DNS name resolution for the cluster nodes to be in place before the load balancing is initialized.

### [3.6. Validating DNS resolution for user-provisioned infrastructure](#installation-user-provisioned-validating-dns_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

To prevent network-related installation failures and ensure node connectivity in OpenShift Container Platform, validate your DNS configuration before deploying on user-provisioned infrastructure.

Important

The validation steps detailed in this section must succeed before you install your cluster.

**Prerequisites**

* You have configured the required DNS records for your user-provisioned infrastructure.

**Procedure**

1. From your installation node, run DNS lookups against the record names of the Kubernetes API, the wildcard routes, and the cluster nodes. Validate that the IP addresses contained in the responses correspond to the correct components.

   1. Perform a lookup against the Kubernetes API record name. Check that the result points to the IP address of the API load balancer:

      ```
      $ dig +noall +answer @<nameserver_ip> api.<cluster_name>.<base_domain>
      ```

      Replace `<nameserver_ip>` with the IP address of the name server, `<cluster_name>` with your cluster name, and `<base_domain>` with your base domain name.

      **Example output**

      ```
      api.ocp4.example.com.		604800	IN	A	192.168.1.5
      ```
   2. Perform a lookup against the Kubernetes internal API record name. Check that the result points to the IP address of the API load balancer:

      ```
      $ dig +noall +answer @<nameserver_ip> api-int.<cluster_name>.<base_domain>
      ```

      **Example output**

      ```
      api-int.ocp4.example.com.		604800	IN	A	192.168.1.5
      ```
   3. Test an example `*.apps.<cluster_name>.<base_domain>` DNS wildcard lookup. All of the application wildcard lookups must resolve to the IP address of the application ingress load balancer:

      ```
      $ dig +noall +answer @<nameserver_ip> random.apps.<cluster_name>.<base_domain>
      ```

      **Example output**

      ```
      random.apps.ocp4.example.com.		604800	IN	A	192.168.1.5
      ```

      Note

      In the example outputs, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

      You can replace `random` with another wildcard value. For example, you can query the route to the OpenShift Container Platform console:

      ```
      $ dig +noall +answer @<nameserver_ip> console-openshift-console.apps.<cluster_name>.<base_domain>
      ```

      **Example output**

      ```
      console-openshift-console.apps.ocp4.example.com. 604800 IN	A 192.168.1.5
      ```
   4. Run a lookup against the bootstrap DNS record name. Check that the result points to the IP address of the bootstrap node:

      ```
      $ dig +noall +answer @<nameserver_ip> bootstrap.<cluster_name>.<base_domain>
      ```

      **Example output**

      ```
      bootstrap.ocp4.example.com.		604800	IN	A	192.168.1.96
      ```
   5. Use this method to perform lookups against the DNS record names for the control plane and compute nodes. Check that the results correspond to the IP addresses of each node.
2. From your installation node, run reverse DNS lookups against the IP addresses of the load balancer and the cluster nodes. Validate that the record names contained in the responses correspond to the correct components.

   1. Perform a reverse lookup against the IP address of the API load balancer. Check that the response includes the record names for the Kubernetes API and the Kubernetes internal API:

      ```
      $ dig +noall +answer @<nameserver_ip> -x 192.168.1.5
      ```

      **Example output**

      ```
      5.1.168.192.in-addr.arpa. 604800	IN	PTR	api-int.ocp4.example.com.
      5.1.168.192.in-addr.arpa. 604800	IN	PTR	api.ocp4.example.com.
      ```

      where:

      `api-int.ocp4.example.com`
      :   Specifies the record name for the Kubernetes internal API.

      `api.ocp4.example.com`
      :   Specifies the record name for the Kubernetes API.

          Note

          A PTR record is not required for the OpenShift Container Platform application wildcard. No validation step is needed for reverse DNS resolution against the IP address of the application ingress load balancer.
   2. Perform a reverse lookup against the IP address of the bootstrap node. Check that the result points to the DNS record name of the bootstrap node:

      ```
      $ dig +noall +answer @<nameserver_ip> -x 192.168.1.96
      ```

      **Example output**

      ```
      96.1.168.192.in-addr.arpa. 604800	IN	PTR	bootstrap.ocp4.example.com.
      ```
   3. Use this method to perform reverse lookups against the IP addresses for the control plane and compute nodes. Check that the results correspond to the DNS record names of each node.

### [3.7. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

During an OpenShift Container Platform installation, you can provide an SSH public key to the installation program. The key is passed to the Red Hat Enterprise Linux CoreOS (RHCOS) nodes through their Ignition config files and is used to authenticate SSH access to the nodes. The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication.

The key is added to the `~/.ssh/authorized_keys` list for the `core` user on each node, which enables password-less authentication. After the key is passed to the nodes, you can use the key pair to SSH in to the RHCOS nodes as the user `core`. To access the nodes through SSH, the private key identity must be managed by SSH for your local user.

If you want to SSH in to your cluster nodes to perform installation debugging or disaster recovery, you must provide the SSH public key during the installation process. The `./openshift-install gather` command also requires the SSH public key to be in place on the cluster nodes.

Important

Do not skip this procedure in production environments, where disaster recovery and debugging is required.

Note

You must use a local key, not one that you configured with platform-specific approaches.

**Procedure**

1. If you do not have an existing SSH key pair on your local machine to use for authentication onto your cluster nodes, create one. For example, on a computer that uses a Linux operating system, run the following command:

   ```
   $ ssh-keygen -t ed25519 -N '' -f <path>/<file_name>
   ```

   Specifies the path and file name, such as `~/.ssh/id_ed25519`, of the new SSH key. If you have an existing key pair, ensure your public key is in the your `~/.ssh` directory.

   Note

   If you plan to install an OpenShift Container Platform cluster that uses the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the `x86_64`, `ppc64le`, and `s390x` architectures, do not create a key that uses the `ed25519` algorithm. Instead, create a key that uses the `rsa` or `ecdsa` algorithm.
2. View the public SSH key:

   ```
   $ cat <path>/<file_name>.pub
   ```

   For example, run the following to view the `~/.ssh/id_ed25519.pub` public key:

   ```
   $ cat ~/.ssh/id_ed25519.pub
   ```
3. Add the SSH private key identity to the SSH agent for your local user, if it has not already been added. SSH agent management of the key is required for password-less SSH authentication onto your cluster nodes, or if you want to use the `./openshift-install gather` command.

   Note

   On some distributions, default SSH private key identities such as `~/.ssh/id_rsa` and `~/.ssh/id_dsa` are managed automatically.

   1. If the `ssh-agent` process is not already running for your local user, start it as a background task:

      ```
      $ eval "$(ssh-agent -s)"
      ```

      **Example output**

      ```
      Agent pid 31874
      ```

      Note

      If your cluster is in FIPS mode, only use FIPS-compliant algorithms to generate the SSH key. The key must be either RSA or ECDSA.
4. Add your SSH private key to the `ssh-agent`:

   ```
   $ ssh-add <path>/<file_name>
   ```

   Specifies the path and file name for your SSH private key, such as `~/.ssh/id_ed25519`

   **Example output**

   ```
   Identity added: /home/<you>/<path>/<file_name> (<computer_name>)
   ```

**Next steps**

* When you install OpenShift Container Platform, provide the SSH public key to the installation program.

### [3.8. Manually creating the installation configuration file](#installation-initializing-manual_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

Installing the cluster requires that you manually create the installation configuration file.

**Prerequisites**

* You have an SSH public key on your local machine for use with the installation program. You can use the key for SSH authentication onto your cluster nodes for debugging and disaster recovery.
* You have obtained the OpenShift Container Platform installation program and the pull secret for your cluster.

**Procedure**

1. Create an installation directory to store your required installation assets in:

   ```
   $ mkdir <installation_directory>
   ```

   Important

   You must create a directory. Some installation assets, such as bootstrap X.509 certificates have short expiration intervals, so you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
2. Customize the provided sample `install-config.yaml` file template and save the file in the `<installation_directory>`.

   Note

   You must name this configuration file `install-config.yaml`.
3. Back up the `install-config.yaml` file so that you can use it to install many clusters.

   Important

   Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.

#### [3.8.1. Sample install-config.yaml file for IBM Power](#installation-bare-metal-config-yaml_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster platform or modify the values of the required parameters.

```
apiVersion: v1
baseDomain: example.com
compute:
- hyperthreading: Enabled
  name: worker
  replicas: 0
  architecture: ppc64le
controlPlane:
  hyperthreading: Enabled
  name: master
  replicas: 3
  architecture: ppc64le
metadata:
  name: test
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  networkType: OVNKubernetes
  machineNetwork:
  - cidr: 192.168.0.0/16
  serviceNetwork:
  - 172.30.0.0/16
platform:
  none: {}
fips: false
pullSecret: '{"auths":{"<local_registry>": {"auth": "<credentials>","email": "you@example.com"}}}'
sshKey: 'ssh-ed25519 AAAA...'
additionalTrustBundle: |
  -----BEGIN CERTIFICATE-----
  ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
  -----END CERTIFICATE-----
imageContentSources:
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-release
- mirrors:
  - <local_registry>/<local_repository_name>/release
  source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
```

where:

`baseDomain`
:   Specifies the base domain of the cluster. All DNS records must be sub-domains of this base and include the cluster name.

`compute`
:   Specifies the `compute` node configurations, which is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`.

`controlPlane`
:   Specifies the `controlPlane` node configurations, which is a single mapping. To meet the requirements of the different data structures, the first line of the `controlPlane` section must not. Only one control plane pool is used.

`hyperthreading`
:   Specifies simultaneous multithreading (SMT), which you configure as a post-installation task.

`compute.replicas`
:   Specifies the number of compute machines that the cluster creates and manages for you on installer-provisioned installations. You must set this value to `0` when you install OpenShift Container Platform on user-provisioned infrastructure. Additionally for user-provisioned installations, you must manually deploy the compute machines before you finish installing the cluster.

Note

If you are installing a three-node cluster, do not deploy any compute machines when you install the Red Hat Enterprise Linux CoreOS (RHCOS) machines.

`controlPlane.replicas`
:   Specifies the number of control plane machines that you add to the cluster. Because the cluster uses these values as the number of etcd endpoints in the cluster, the value must match the number of control plane machines that you deploy.

`metadata.name`
:   Specifies the cluster name that you specified in your DNS records.

`networking.clusterNetwork.cidr`
:   Specifies a block of IP addresses from which pod IP addresses are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the pod network. If you need to access the pods from an external network, you must configure load balancers and routers to manage the traffic.

Note

Class E CIDR range is reserved for a future use. To use the Class E CIDR range, you must ensure your networking environment accepts the IP addresses within the Class E CIDR range.

`networking.cidr.hostPrefix`
:   Specifies the subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23`, then each node is assigned a `/23` subnet out of the given `cidr`, which allows for 510 (2^(32 - 23) - 2) pod IP addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.

`networking.networkType`
:   Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

`networking.serviceNetwork`
:   Specifies the IP address pool to use for service IP addresses. You can enter only one IP address pool. This block must not overlap with existing physical networks. If you need to access the services from an external network, configure load balancers and routers to manage the traffic.

`platform`
:   Specifies the platform. You must set the platform to `none`. You cannot provide additional platform configuration variables for IBM Power® infrastructure.

Important

Clusters that are installed with the platform type `none` are unable to use some features, such as managing compute machines with the Machine API. This limitation applies even if the compute machines that are attached to the cluster are installed on a platform that would normally support the feature. This parameter cannot be changed after installation.

`fips`
:   Specifies either enabling or disabling FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead.

Important

To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening).

When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86\_64, ppc64le, and s390x architectures.

`pullSecret`
:   Specifies the registry domain name for `<local_registry>`, and optionally the port, that your mirror registry uses to serve content. For example, `registry.example.com` or `registry.example.com:5000`. For `<credentials>`, specify the base64-encoded user name and password for your mirror registry.

`sshKey`
:   Specifies the SSH public key for the `core` user in Red Hat Enterprise Linux CoreOS (RHCOS).

Note

For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

`additionalTrustBundle`
:   Specifies the contents of the certificate file that you used for your mirror registry.

`imageContentSources`
:   Specifies the `imageContentSources` section according to the output of the command that you used to mirror the repository.

Important

* When using the `oc adm release mirror` command, use the output from the `imageContentSources` section.
* When using `oc mirror` command, use the `repositoryDigestMirrors` section of the `ImageContentSourcePolicy` file that results from running the command.
* `ImageContentSourcePolicy` is deprecated. For more information see *Configuring image registry repository mirroring*.

#### [3.8.2. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

**Prerequisites**

* You have an existing `install-config.yaml` file.
* You have reviewed the sites that your cluster requires access to and determined whether any of them need to bypass the proxy. By default, the proxy handles all cluster egress traffic, including calls to hosting cloud provider APIs. You added sites to the `Proxy` object’s `spec.noProxy` field to bypass the proxy if necessary.

  Note

  The `Proxy` object `status.noProxy` field includes the values of the `networking.machineNetwork[].cidr`, `networking.clusterNetwork[].cidr`, and `networking.serviceNetwork[]` fields from your installation configuration.

  For installations on Amazon Web Services (AWS), Google Cloud, Microsoft Azure, and Red Hat OpenStack Platform (RHOSP), the `Proxy` object `status.noProxy` field also includes the instance metadata endpoint (`169.254.169.254`).

**Procedure**

1. Edit your `install-config.yaml` file and add the proxy settings. For example:

   ```
   apiVersion: v1
   baseDomain: my.domain.com
   proxy:
     httpProxy: http://<username>:<pswd>@<ip>:<port>
     httpsProxy: https://<username>:<pswd>@<ip>:<port>
     noProxy: example.com
   additionalTrustBundle: |
       -----BEGIN CERTIFICATE-----
       <MY_TRUSTED_CA_CERT>
       -----END CERTIFICATE-----
   additionalTrustBundlePolicy: <policy_to_add_additionalTrustBundle>
   # ...
   ```

   where:

   `proxy.httpProxy`
   :   Specifies a proxy URL to use for creating HTTP connections outside the cluster. The URL scheme must be `http`.

   `proxy.httpsProxy`
   :   Specifies a proxy URL to use for creating HTTPS connections outside the cluster.

   `proxy.noProxy`
   :   Specifies a comma-separated list of destination domain names, IP addresses, or other network CIDRs to exclude from proxying. Preface a domain with `.` to match subdomains only. For example, `.y.com` matches `x.y.com`, but not `y.com`. Use `*` to bypass the proxy for all destinations.

   `additionalTrustBundle`
   :   If you specify this value, the installation program generates a config map named `user-ca-bundle` in the `openshift-config` namespace to hold the additional CA certificates. If you specify `additionalTrustBundle` and at least one proxy setting, the `Proxy` object references the `user-ca-bundle` config map in the `trustedCA` field. The Cluster Network Operator then creates a `trusted-ca-bundle` config map that merges the contents specified for the `trustedCA` parameter with the RHCOS trust bundle. You must set the `additionalTrustBundle` field unless an authority from the RHCOS trust bundle signs the proxy’s identity certificate.

   `additionalTrustBundlePolicy`
   :   Specifies the policy that determines the configuration of the `Proxy` object to reference the `user-ca-bundle` config map in the `trustedCA` field. The allowed values are `Proxyonly` and `Always`. Use `Proxyonly` to reference the `user-ca-bundle` config map only when you configure an `http/https` proxy. Use `Always` to always reference the `user-ca-bundle` config map. The default value is `Proxyonly`. Optional parameter.

       Note

       The installation program does not support the proxy `readinessEndpoints` field.

       Note

       If the installation program times out, restart and then complete the deployment by using the `wait-for` command of the installation program. For example:

       ```
       $ ./openshift-install wait-for install-complete --log-level debug
       ```
2. Save the file and reference it when installing OpenShift Container Platform.

   The installation program creates a cluster-wide proxy named `cluster` that uses the proxy settings in the `install-config.yaml` file. If you do not give proxy settings, the installation program still creates a `cluster` `Proxy` object, but it has a nil `spec`.

   Note

   Only the `Proxy` object named `cluster` is supported, and you cannot create additional proxies.

#### [3.8.3. Configuring a three-node cluster](#installation-three-node-cluster_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

To create smaller, resource-efficient clusters for testing and production, deploy a bare-metal cluster with zero compute machines. This optional configuration uses only three control plane machines, optimizing infrastructure resources for administrators and developers.

In three-node OpenShift Container Platform environments, the three control plane machines are schedulable, which means that your application workloads run on them.

**Prerequisites**

* You have an existing `install-config.yaml` file.

**Procedure**

* Ensure that the number of compute replicas is set to `0` in your `install-config.yaml` file, as shown in the following `compute` stanza:

  ```
  compute:
  - name: worker
    platform: {}
    replicas: 0
  # ...
  ```

  Note

  You must set the value of the `replicas` parameter for the compute machines to `0` when you install OpenShift Container Platform on user-provisioned infrastructure, regardless of the number of compute machines you deploy. In installer-provisioned installations, the parameter controls the number of compute machines that the cluster creates and manages for you. This does not apply to user-provisioned installations, where you deploy the compute machines manually.

For three-node cluster installations, follow these next steps:

* If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes. See the *Load balancing requirements for user-provisioned infrastructure* section for more information.
* When you create the Kubernetes manifest files in the following procedure, ensure that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file is set to `true`. This enables your application workloads to run on the control plane nodes.
* Do not deploy any compute nodes when you create the Red Hat Enterprise Linux CoreOS (RHCOS) machines.

### [3.9. Cluster Network Operator configuration](#nw-operator-cr_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

To manage cluster networking, configure the Cluster Network Operator (CNO) `Network` custom resource (CR) named `cluster` so the cluster uses the correct IP ranges and network plugin settings for reliable pod and service connectivity. Some settings and fields are inherited at the time of install or by the `default.Network.type` plugin, OVN-Kubernetes.

The CNO configuration inherits the following fields during cluster installation from the `Network` API in the `Network.config.openshift.io` API group:

`clusterNetwork`
:   IP address pools from which pod IP addresses are allocated.

`serviceNetwork`
:   IP address pool for services.

`defaultNetwork.type`
:   Cluster network plugin. `OVNKubernetes` is the only supported plugin during installation.

You can specify the cluster network plugin configuration for your cluster by setting the fields for the `defaultNetwork` object in the CNO object named `cluster`.

#### [3.9.1. Cluster Network Operator configuration object](#nw-operator-cr-cno-object_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

The fields for the Cluster Network Operator (CNO) are described in the following table:

Expand

Table 3.8. Cluster Network Operator configuration object

| Field | Type | Description |
| --- | --- | --- |
| `metadata.name` | `string` | The name of the CNO object. This name is always `cluster`. |
| `spec.clusterNetwork` | `array` | A list specifying the blocks of IP addresses from which pod IP addresses are allocated and the subnet prefix length assigned to each individual node in the cluster. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:  ``` spec:   clusterNetwork:   - cidr: 10.128.0.0/19     hostPrefix: 23   - cidr: fd01::/48     hostPrefix: 64 ```  If you install a cluster on AWS with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first. |
| `spec.serviceNetwork` | `array` | A block of IP addresses for services. If you use dual-stack networking, specify IPv4 and IPv6 address families. For example:  ``` spec:   serviceNetwork:   - 172.30.0.0/14   - fd02::/112 ```  If you install a cluster on AWS with dual-stack networking, the order of addresses must match the dual-stack configuration you selected. For example, if you specified the `DualStackIPv4Primary`, list the IPv4 address first.  You can customize this field only in the `install-config.yaml` file before you create the manifests. The value is read-only in the manifest file. |
| `spec.defaultNetwork` | `object` | Configures the network plugin for the cluster network. |
| `spec.additionalRoutingCapabilities.providers` | `array` | This setting enables a dynamic routing provider. The FRR routing capability provider is required for the route advertisement feature. The only supported value is `FRR`.  * `FRR`: The FRR routing provider  ``` spec:   additionalRoutingCapabilities:     providers:     - FRR ``` |

Show more

Important

For a cluster that needs to deploy objects across multiple networks, ensure that you specify the same value for the `clusterNetwork.hostPrefix` parameter for each network type that is defined in the `install-config.yaml` file. Setting a different value for each `clusterNetwork.hostPrefix` parameter can impact the OVN-Kubernetes network plugin, where the plugin cannot effectively route object traffic among different nodes.

#### [3.9.2. defaultNetwork object configuration](#nw-operator-cr-defaultnetwork_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

The values for the `defaultNetwork` object are defined in the following table:

Expand

Table 3.9. defaultNetwork object

| Field | Type | Description |
| --- | --- | --- |
| `type` | `string` | `OVNKubernetes`. The Red Hat OpenShift Networking network plugin is selected during installation. This value cannot be changed after cluster installation.  Note  OpenShift Container Platform uses the OVN-Kubernetes network plugin by default. |
| `ovnKubernetesConfig` | `object` | This object is only valid for the OVN-Kubernetes network plugin. |

Show more

#### [3.9.3. Configuration for the OVN-Kubernetes network plugin](#nw-operator-configuration-parameters-for-ovn-sdn_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

The following table describes the configuration fields for the OVN-Kubernetes network plugin:

Expand

Table 3.10. ovnKubernetesConfig object

| Field | Type | Description |
| --- | --- | --- |
| `mtu` | `integer` | The maximum transmission unit (MTU) for the Geneve (Generic Network Virtualization Encapsulation) overlay network. This is detected automatically based on the MTU of the primary network interface. You do not normally need to override the detected MTU.  If the auto-detected value is not what you expect it to be, confirm that the MTU on the primary network interface on your nodes is correct. You cannot use this option to change the MTU value of the primary network interface on the nodes.  If your cluster requires different MTU values for different nodes, you must set this value to `100` less than the lowest MTU value in your cluster. For example, if some nodes in your cluster have an MTU of `9001`, and some have an MTU of `1500`, you must set this value to `1400`. |
| `genevePort` | `integer` | The port to use for all Geneve packets. The default value is `6081`. This value cannot be changed after cluster installation. |
| `ipsecConfig` | `object` | Specify a configuration object for customizing the IPsec configuration. |
| `ipv4` | `object` | Specifies a configuration object for IPv4 settings. |
| `ipv6` | `object` | Specifies a configuration object for IPv6 settings. |
| `policyAuditConfig` | `object` | Specify a configuration object for customizing network policy audit logging. If unset, the defaults audit log settings are used. |
| `routeAdvertisements` | `string` | Specifies whether to advertise cluster network routes. The default value is `Disabled`.  * `Enabled`: Import routes to the cluster network and advertise cluster network routes as configured in `RouteAdvertisements` objects. * `Disabled`: Do not import routes to the cluster network or advertise cluster network routes. |
| `gatewayConfig` | `object` | Optional: Specify a configuration object for customizing how egress traffic is sent to the node gateway. Valid values are `Shared` and `Local`. The default value is `Shared`. In the default setting, the Open vSwitch (OVS) outputs traffic directly to the node IP interface. If you are using hardware offloading, Red Hat recommends to use the default `Shared` gateway mode to bypass the host routing plane. In the `Local` setting, it traverses the host network; consequently, it gets applied to the routing table of the host.  Note  While migrating egress traffic, you can expect some disruption to workloads and service traffic until the Cluster Network Operator (CNO) successfully rolls out the changes. |

Show more

Expand

Table 3.11. ovnKubernetesConfig.ipv4 object

| Field | Type | Description |
| --- | --- | --- |
| `internalTransitSwitchSubnet` | string | If your existing network infrastructure overlaps with the `100.88.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.  The default value is `100.88.0.0/16`. |
| `internalJoinSubnet` | string | If your existing network infrastructure overlaps with the `100.64.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster. For example, if the `clusterNetwork.cidr` value is `10.128.0.0/14` and the `clusterNetwork.hostPrefix` value is `/23`, then the maximum number of nodes is `2^(23-14)=512`.  The default value is `100.64.0.0/16`. |

Show more

Expand

Table 3.12. ovnKubernetesConfig.ipv6 object

| Field | Type | Description |
| --- | --- | --- |
| `internalTransitSwitchSubnet` | string | If your existing network infrastructure overlaps with the `fd97::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.  The default value is `fd97::/64`. |
| `internalJoinSubnet` | string | If your existing network infrastructure overlaps with the `fd98::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster.  The default value is `fd98::/64`. |

Show more

Expand

Table 3.13. policyAuditConfig object

| Field | Type | Description |
| --- | --- | --- |
| `rateLimit` | integer | The maximum number of messages to generate every second per node. The default value is `20` messages per second. |
| `maxFileSize` | integer | The maximum size for the audit log in bytes. The default value is `50000000` or 50 MB. |
| `maxLogFiles` | integer | The maximum number of log files that are retained. |
| `destination` | string | One of the following additional audit log targets:  `libc`  The libc `syslog()` function of the journald process on the host.  `udp:<host>:<port>`  A syslog server. Replace `<host>:<port>` with the host and port of the syslog server.  `unix:<file>`  A Unix Domain Socket file specified by `<file>`.  `null`  Do not send the audit logs to any additional target. |
| `syslogFacility` | string | The syslog facility, such as `kern`, as defined by RFC5424. The default value is `local0`. |

Show more

Expand

Table 3.14. gatewayConfig object

| Field | Type | Description |
| --- | --- | --- |
| `routingViaHost` | `boolean` | Set this field to `true` to send egress traffic from pods to the host networking stack. For highly-specialized installations and applications that rely on manually configured routes in the kernel routing table, you might want to route egress traffic to the host networking stack. By default, egress traffic is processed in OVN to exit the cluster and is not affected by specialized routes in the kernel routing table. The default value is `false`.  This field has an interaction with the Open vSwitch hardware offloading feature. If you set this field to `true`, you do not receive the performance benefits of the offloading because egress traffic is processed by the host networking stack. |
| `ipForwarding` | `object` | You can control IP forwarding for all traffic on OVN-Kubernetes managed interfaces by using the `ipForwarding` specification in the `Network` resource. Specify `Restricted` to only allow IP forwarding for Kubernetes related traffic. Specify `Global` to allow forwarding of all IP traffic. For new installations, the default is `Restricted`. For updates to OpenShift Container Platform 4.14 or later, the default is `Global`.  Note  The default value of `Restricted` sets the IP forwarding to drop. |
| `ipv4` | `object` | Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv4 addresses. |
| `ipv6` | `object` | Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv6 addresses. |

Show more

Expand

Table 3.15. gatewayConfig.ipv4 object

| Field | Type | Description |
| --- | --- | --- |
| `internalMasqueradeSubnet` | `string` | The masquerade IPv4 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `169.254.169.0/29`.  Important  For OpenShift Container Platform 4.17 and later versions, clusters use `169.254.0.0/17` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet. |

Show more

Expand

Table 3.16. gatewayConfig.ipv6 object

| Field | Type | Description |
| --- | --- | --- |
| `internalMasqueradeSubnet` | `string` | The masquerade IPv6 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `fd69::/125`.  Important  For OpenShift Container Platform 4.17 and later versions, clusters use `fd69::/112` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet. |

Show more

Expand

Table 3.17. ipsecConfig object

| Field | Type | Description |
| --- | --- | --- |
| `mode` | `string` | Specifies the behavior of the IPsec implementation. Must be one of the following values:  * `Disabled`: IPsec is not enabled on cluster nodes. * `External`: IPsec is enabled for network traffic with external hosts. * `Full`: IPsec is enabled for pod traffic and network traffic with external hosts. |

Show more

**Example OVN-Kubernetes configuration with IPSec enabled**

```
defaultNetwork:
  type: OVNKubernetes
  ovnKubernetesConfig:
    mtu: 1400
    genevePort: 6081
    ipsecConfig:
      mode: Full
```

### [3.10. Creating the Kubernetes manifest and Ignition config files](#installation-user-infra-generate-k8s-manifest-ignition_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

Because you manually provision infrastructure, you must generate the Kubernetes manifest and Ignition config files that the cluster requires.

The installation program converts the installation configuration into Kubernetes manifests and then wraps them into Ignition configuration files. You use these Ignition files to configure the cluster machines.

Important

* The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which the system then renews. If you shut down the cluster before the system renews the certificates and you later restart the cluster after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
* Use Ignition config files within 12 hours after you generate them, because the 24-hour certificate rotates from 16 to 22 hours after you install the cluster. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

Note

The installation program that generates the manifest and Ignition files is architecture specific. You can obtain it from the [client image mirror](https://mirror.openshift.com/pub/openshift-v4/ppc64le/clients/ocp/latest/). The Linux version of the installation program (without an architecture postfix) runs on ppc64le only. This installation program is also available as a macOS version.

**Prerequisites**

* You obtained the OpenShift Container Platform installation program. For a restricted network installation, these files are on your mirror host.
* You created the `install-config.yaml` installation configuration file.

**Procedure**

1. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```

   where:

   `<installation_directory>`
   :   Specifies the installation directory that contains the `install-config.yaml` file you created.

   Warning

   If you are installing a three-node cluster, skip the following step to allow the control plane nodes to be schedulable.

   +

   Important

   When you configure control plane nodes from the default unschedulable to schedulable, you require additional subscriptions because control plane nodes then become compute nodes.
2. Verify that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:

   1. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.
   2. Locate the `mastersSchedulable` parameter and verify that it is set to `false`.
   3. Save and exit the file.
3. To create the Ignition configuration files, run the following command from the directory that contains the installation program:

   ```
   $ ./openshift-install create ignition-configs --dir <installation_directory>
   ```

   where:

   `<installation_directory>`
   :   Specifies the same installation directory.

       The installation program creates Ignition config files for the bootstrap, control plane, and compute nodes in the installation directory. The program also creates the `kubeadmin-password` and `kubeconfig` files in the `./<installation_directory>/auth` directory:

       ```
       .
       ├── auth
       │   ├── kubeadmin-password
       │   └── kubeconfig
       ├── bootstrap.ign
       ├── master.ign
       ├── metadata.json
       └── worker.ign
       ```

### [3.11. Installing RHCOS and starting the OpenShift Container Platform bootstrap process](#ibm-power-upi-installing-rhcos-intro_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on IBM Power® infrastructure that you provision, you must install Red Hat Enterprise Linux CoreOS (RHCOS) on the machines by using an ISO image or network PXE booting.

To install RHCOS, you must give the Ignition config file generated by the OpenShift Container Platform installation program for the type of machine you are installing. If you have configured suitable networking, DNS, and load balancing infrastructure, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS machines have rebooted.

Follow either the steps to use an ISO image or network PXE booting to install RHCOS on the machines.

#### [3.11.1. Installing RHCOS by using an ISO image](#installation-user-infra-machines-iso_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

To provision physical or virtual machines, install RHCOS by using a bootable ISO image.

**Prerequisites**

* You have created the Ignition config files for your cluster.
* You have configured a suitable network, DNS, and load balancing infrastructure.
* You have an HTTP server that can be accessed from your computer, and from the machines that you create.
* You have reviewed the *Advanced RHCOS installation configuration* section for different ways to configure features, such as networking and disk partitioning.

**Procedure**

1. Obtain the SHA512 digest for each of your Ignition config files. For example, you can use the following on a system running Linux to get the SHA512 digest for your `bootstrap.ign` Ignition config file:

   ```
   $ sha512sum <installation_directory>/bootstrap.ign
   ```

   The digests are provided to the `coreos-installer` in a later step to validate the authenticity of the Ignition config files on the cluster nodes.
2. Upload the bootstrap, control plane, and compute node Ignition config files that the installation program created to your HTTP server. Note the URLs of these files.

   Important

   You can add or change configuration settings in your Ignition configs before saving them to your HTTP server. If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.
3. From the installation host, validate that the Ignition config files are available on the URLs. The following example gets the Ignition config file for the bootstrap node:

   ```
   $ curl -k http://<HTTP_server>/bootstrap.ign
   ```

   * <HTTP\_server>: Replace `bootstrap.ign` with `master.ign` or `worker.ign` in the command to validate that the Ignition config files for the control plane and compute nodes are also available.

     **Example output**

     ```
       % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                      Dload  Upload   Total   Spent    Left  Speed
       0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{"ignition":{"version":"3.2.0"},"passwd":{"users":[{"name":"core","sshAuthorizedKeys":["ssh-rsa...
     ```
4. Although it is possible to obtain the RHCOS images that are required for your preferred method of installing operating system instances from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/ppc64le/dependencies/rhcos/) page, the recommended way to obtain the correct version of your RHCOS images are from the output of `openshift-install` command:

   ```
   $ openshift-install coreos print-stream-json | grep '\.iso[^.]'
   ```

   **Example output**

   ```
   "location": "<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live.aarch64.iso",
   "location": "<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live.ppc64le.iso",
   "location": "<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live.s390x.iso",
   "location": "<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live.x86_64.iso",
   ```

   Important

   The RHCOS images might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Use the image versions that match your OpenShift Container Platform version if they are available. Use only ISO images for this procedure. RHCOS qcow2 images are not supported for this installation type.

   ISO file names resemble the following example:

   `rhcos-<version>-live.<architecture>.iso`
5. Use the ISO to start the RHCOS installation. Use one of the following installation options:

   * Burn the ISO image to a disk and boot it directly.
   * Use ISO redirection by using a lights-out management (LOM) interface.
6. Boot the RHCOS ISO image without specifying any options or interrupting the live boot sequence. Wait for the installer to boot into a shell prompt in the RHCOS live environment.

   Note

   It is possible to interrupt the RHCOS installation boot process to add kernel arguments. However, for this ISO procedure you should use the `coreos-installer` command as outlined in the following steps, instead of adding kernel arguments.
7. Run the `coreos-installer` command and specify the options that meet your installation requirements. At a minimum, you must specify the URL that points to the Ignition config file for the node type, and the device that you are installing to:

   ```
   $ sudo coreos-installer install --ignition-url=http://<HTTP_server>/<node_type>.ign <device> \
   --ignition-hash=sha512-<digest>
   ```

   * `<device>`: You must run the `coreos-installer` command by using `sudo`, because the `core` user does not have the required root privileges to perform the installation.
   * `<digest>`: The `--ignition-hash` option is required when the Ignition config file is obtained through an HTTP URL to validate the authenticity of the Ignition config file on the cluster node. `<digest>` is the Ignition config file SHA512 digest obtained in a preceding step.

     Note

     If you want to provide your Ignition config files through an HTTPS server that uses TLS, you can add the internal certificate authority (CA) to the system trust store before running `coreos-installer`.

     The following example initializes a bootstrap node installation to the `/dev/sda` device. The Ignition config file for the bootstrap node is obtained from an HTTP web server with the IP address 192.168.1.2:

     ```
     $ sudo coreos-installer install --ignition-url=http://192.168.1.2:80/installation_directory/bootstrap.ign /dev/sda \
     --ignition-hash=sha512-a5a2d43879223273c9b60af66b44202a1d1248fc01cf156c46d4a79f552b6bad47bc8cc78ddf0116e80c59d2ea9e32ba53bc807afbca581aa059311def2c3e3b
     ```
8. Monitor the progress of the RHCOS installation on the console of the machine.

   Important

   Be sure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of RHCOS installation issues that might arise.
9. After RHCOS installs, you must reboot the system. During the system reboot, it applies the Ignition config file that you specified.
10. Check the console output to verify that Ignition ran.

    **Example command**

    ```
    Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
    Ignition: user-provided config was applied
    ```
11. Continue to create the other machines for your cluster.

    Important

    You must create the bootstrap and control plane machines at this time. If the control plane machines are not made schedulable, also create at least two compute machines before you install OpenShift Container Platform.

    If the required network, DNS, and load balancer infrastructure are in place, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS nodes have rebooted.

    Note

    RHCOS nodes do not include a default password for the `core` user. You can access the nodes by running `ssh core@<node>.<cluster_name>.<base_domain>` as a user with access to the SSH private key that is paired to the public key that you specified in your `install_config.yaml` file. OpenShift Container Platform 4 cluster nodes running RHCOS are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, when investigating installation issues, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on a target node, SSH access might be required for debugging or disaster recovery.

#### [3.11.2. Networking and bonding options for ISO installations](#installation-user-infra-machines-routing-bonding_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You can configure advanced options so that you can modify the Red Hat Enterprise Linux CoreOS (RHCOS) manual installation process. The subsequent sections show examples of networking options for an ISO installation.

If you install RHCOS from an ISO image, you can add kernel arguments manually when you boot the image to configure networking for a node. If no networking arguments are specified, DHCP is activated in the initramfs when RHCOS detects that networking is required to fetch the Ignition config file.

Important

When adding networking arguments manually, you must also add the `rd.neednet=1` kernel argument to bring the network up in the initramfs.

The following information provides examples for configuring networking and bonding on your RHCOS nodes for ISO installations. The examples describe how to use the `ip=`, `nameserver=`, and `bond=` kernel arguments.

Note

Ordering is important when adding the kernel arguments: `ip=`, `nameserver=`, and then `bond=`.

The networking options are passed to the `dracut` tool during system boot. For more information about the networking options supported by `dracut`, see `dracut.cmdline` manual page.

##### [3.11.2.1. Configuring DHCP or static IP addresses](#configuring-dhcp-or-static-ip-addresses_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You can configure an IP address by using either DHCP or an individual static IP address. If you set a static IP, you must then identify the DNS server IP address on each node.

The configuration examples in the procedure, update the IP addresses for the following components:

* The node’s IP address to `10.10.10.2`
* The gateway address to `10.10.10.254`
* The netmask to `255.255.255.0`
* The hostname to `core0.example.com`
* The DNS server address to `4.4.4.41`
* The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically.

**Procedure**

1. Enter a command like the following command to configure a static IP address:

   ```
   ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
   nameserver=4.4.4.41
   ```
2. Enter a command like the following command to configure a DHCP IP address:

   ```
   ip=enp1s0:dhcp
   ```

   Note

   When you use DHCP to configure IP addressing for the RHCOS machines, the machines also obtain the DNS server information through DHCP. For DHCP-based deployments, you can define the DNS server address that is used by the RHCOS nodes through your DHCP server configuration.
3. If two or more network interfaces and only one interface exists, disable DHCP on a single interface. In the example, the `enp1s0` interface has a static networking configuration and DHCP is disabled for `enp2s0`, which is not used:

   ```
   ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
   ip=::::core0.example.com:enp2s0:none
   ```
4. If you need to combine DHCP and static IP configurations on systems with multiple network interfaces, run the following example command:

   ```
   ip=enp1s0:dhcp
   ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
   ```

##### [3.11.2.2. Configuring an IP address without a static hostname](#configuring-ip-address-without-static-hostname_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You can configure an IP address without assigning a static hostname. If a static hostname is not set by the user, the static hostname gets picked up and automatically set by a reverse DNS lookup.

The configuration examples in the procedure, update the IP addresses for the following components:

* The node’s IP address to `10.10.10.2`
* The gateway address to `10.10.10.254`
* The netmask to `255.255.255.0`
* The DNS server address to `4.4.4.41`
* The auto-configuration value to `none`. No auto-configuration is required when IP networking is configured statically.

**Procedure**

* To configure an IP address without a static hostname, enter a command like the following command:

  ```
  ip=10.10.10.2::10.10.10.254:255.255.255.0::enp1s0:none
  nameserver=4.4.4.41
  ```

##### [3.11.2.3. Specifying multiple network interfaces and DNS servers](#specifying-multiple-network-interfaces_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You can specify multiple network interfaces by setting multiple `ip=` entries. You can provide multiple DNS servers by adding a `nameserver=` entry for each server,

**Procedure**

* To specify multiple network interfaces for your interfaces, you can enter a command like the following command:

  ```
  ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp1s0:none
  ip=10.10.10.3::10.10.10.254:255.255.255.0:core0.example.com:enp2s0:none
  ```
* To provide multiple DNS servers by adding a `nameserver=` entry for each server, enter a command like the following command:

  ```
  nameserver=1.1.1.1
  nameserver=8.8.8.8
  ```

##### [3.11.2.4. Configuring default gateway and route](#configuring-default-gateway-route_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

As an optional task, you can configure routes to additional networks by setting an `rd.route=` value.

Note

When you configure one or multiple networks, one default gateway is required. If the additional network gateway is different from the primary network gateway, the default gateway must be the primary network gateway.

**Procedure**

* To configure the default gateway, enter the following command:

  ```
  ip=::10.10.10.254::::
  ```
* To configure the route for an additional network, enter the following command:

  ```
  rd.route=20.20.20.0/24:20.20.20.254:enp2s0
  ```

##### [3.11.2.5. Configuring VLANs on individual interfaces](#configuring-vlans-individual-interfaces_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

As an optional task, you can configure VLANs on individual interfaces by using the `vlan=` parameter.

**Procedure**

* To configure a VLAN on a network interface and use a static IP address, run the following command:

  ```
  ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:enp2s0.100:none
  vlan=enp2s0.100:enp2s0
  ```
* To configure a VLAN on a network interface and to use DHCP, run the following command:

  ```
  ip=enp2s0.100:dhcp
  vlan=enp2s0.100:enp2s0
  ```

##### [3.11.2.6. Bonding multiple network interfaces to a single interface](#bonding-multiple-network-interfaces-to-single-interface_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

As an optional task, you can bond multiple network interfaces to a single interface by using the `bond=` option.

The following example demonstrates editing the `/etc/config/network` file and specifying the following syntax for bonding multiple network interfaces to a single interface:

```
bond=<name>[:<network_interfaces>][:<options>]
```

* `<name>`: Specifies the bonding device name, for example `bond0`.
* `<network_interfaces>`: Specifies a comma-separated list of physical (ethernet) interfaces, such as `em1,em2`.
* `` <options>: Specifies a comma-separated list of bonding options. Enter the `modinfo bonding `` command to see available options.

When you create a bonded interface using the `bond=` command, you must specify how the IP address is assigned and other information for the bonded interface.

**Procedure**

* To configure the bonded interface to use DHCP, edit the `/etc/config/network` file by setting the IP address for the bond to `dhcp`. For example:

  ```
  ip=bond0:dhcp
  ```
* To configure the bonded interface to use a static IP address, edit the `/etc/config/network` file entering the specific IP address you want and related information. For example:

  ```
  ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
  ```

##### [3.11.2.7. Bonding multiple SR-IOV network interfaces to a dual port NIC interface](#bonding-multiple-sriov-network-interfaces-to-dual-port_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You can bond multiple SR-IOV network interfaces to a dual port NIC interface by using the `bond=` option. Ensure you apply the procedure tasks to each node.

**Procedure**

1. Create the SR-IOV virtual functions (VFs) following the guidance in [Managing SR-IOV devices](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_virtualization/managing-virtual-devices_configuring-and-managing-virtualization#managing-sr-iov-devices_managing-virtual-devices). Follow the procedure in the "Attaching SR-IOV networking devices to virtual machines" section.
2. Create the bond, attach the desired VFs to the bond and set the bond link state up following the guidance in [Configuring network bonding](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html/configuring_and_managing_networking/configuring-network-bonding_configuring-and-managing-networking). Follow any of the described procedures to create the bond.

   The following examples illustrate the syntax you must use:

   * The syntax for configuring a bonded interface is `bond=<name>[:<network_interfaces>][:options]`.

     `<name>` is the bonding device name (`bond0`), `<network_interfaces>` represents the virtual functions (VFs) by their known name in the kernel and shown in the output of the `ip link` command(`eno1f0`, `eno2f0`), and *options* is a comma-separated list of bonding options. Enter `modinfo bonding` to see available options.
   * When you create a bonded interface using `bond=`, you must specify how the IP address is assigned and other information for the bonded interface.

     + To configure the bonded interface to use DHCP, set the bond’s IP address to `dhcp`. For example:

       ```
       bond=bond0:eno1f0,eno2f0:mode=active-backup
       ip=bond0:dhcp::AA:BB:CC:DD:EE:FF
       ip=eno1f0:none::AA:BB:CC:DD:EE:FF
       ip=eno2f0:none::AA:BB:CC:DD:EE:FF
       ```
     + To configure the bonded interface to use a static IP address, enter the specific IP address you want and related information. For example:

       ```
       bond=bond0:eno1f0,eno2f0:mode=active-backup
       ip=10.10.10.2::10.10.10.254:255.255.255.0:core0.example.com:bond0:none
       ```

#### [3.11.3. Installing RHCOS by using PXE booting](#installation-user-infra-machines-pxe_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You can use PXE booting to install RHCOS on the machines.

**Prerequisites**

* You have created the Ignition config files for your cluster.
* You have configured a suitable network, DNS and load balancing infrastructure.
* You have configured suitable PXE infrastructure.
* You have an HTTP server that can be accessed from your computer, and from the machines that you create.
* You have reviewed the *Advanced RHCOS installation configuration* section for different ways to configure features, such as networking and disk partitioning.

**Procedure**

1. Upload the bootstrap, control plane, and compute node Ignition config files that the installation program created to your HTTP server. Note the URLs of these files.

   Important

   You can add or change configuration settings in your Ignition configs before saving them to your HTTP server. If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.
2. From the installation host, validate that the Ignition config files are available on the URLs. The following example gets the Ignition config file for the bootstrap node:

   ```
   $ curl -k http://<HTTP_server>/bootstrap.ign
   ```

   * `<HTTP_server>`: Replace `bootstrap.ign` with `master.ign` or `worker.ign` in the command to validate that the Ignition config files for the control plane and compute nodes are also available.

     **Example output**

     ```
       % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                      Dload  Upload   Total   Spent    Left  Speed
       0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0{"ignition":{"version":"3.2.0"},"passwd":{"users":[{"name":"core","sshAuthorizedKeys":["ssh-rsa...
     ```
3. Although it is possible to obtain the RHCOS `kernel`, `initramfs` and `rootfs` files that are required for your preferred method of installing operating system instances from the [RHCOS image mirror](https://mirror.openshift.com/pub/openshift-v4/ppc64le/dependencies/rhcos/) page, the recommended way to obtain the correct version of your RHCOS files are from the output of `openshift-install` command:

   ```
   $ openshift-install coreos print-stream-json | grep -Eo '"https.*(kernel-|initramfs.|rootfs.)\w+(\.img)?"'
   ```

   **Example output**

   ```
   "<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-kernel-aarch64"
   "<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-initramfs.aarch64.img"
   "<url>/art/storage/releases/rhcos-4.22-aarch64/<release>/aarch64/rhcos-<release>-live-rootfs.aarch64.img"
   "<url>/art/storage/releases/rhcos-4.22-ppc64le/49.84.202110081256-0/ppc64le/rhcos-<release>-live-kernel-ppc64le"
   "<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live-initramfs.ppc64le.img"
   "<url>/art/storage/releases/rhcos-4.22-ppc64le/<release>/ppc64le/rhcos-<release>-live-rootfs.ppc64le.img"
   "<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-kernel-s390x"
   "<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-initramfs.s390x.img"
   "<url>/art/storage/releases/rhcos-4.22-s390x/<release>/s390x/rhcos-<release>-live-rootfs.s390x.img"
   "<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-kernel-x86_64"
   "<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-initramfs.x86_64.img"
   "<url>/art/storage/releases/rhcos-4.22/<release>/x86_64/rhcos-<release>-live-rootfs.x86_64.img"
   ```

   Important

   The RHCOS artifacts might not change with every release of OpenShift Container Platform. You must download images with the highest version that is less than or equal to the OpenShift Container Platform version that you install. Only use the appropriate `kernel`, `initramfs`, and `rootfs` artifacts described below for this procedure. RHCOS QCOW2 images are not supported for this installation type.

   The file names contain the OpenShift Container Platform version number. They resemble the following examples:

   * `kernel`: `rhcos-<version>-live-kernel-<architecture>`
   * `initramfs`: `rhcos-<version>-live-initramfs.<architecture>.img`
   * `rootfs`: `rhcos-<version>-live-rootfs.<architecture>.img`
4. Upload the `rootfs`, `kernel`, and `initramfs` files to your HTTP server.

   Important

   If you plan to add more compute machines to your cluster after you finish installation, do not delete these files.
5. Configure the network boot infrastructure so that the machines boot from their local disks after RHCOS is installed on them.
6. Configure PXE installation for the RHCOS images and begin the installation.
7. Modify the following example menu entry for your environment and verify that the image and Ignition files are properly accessible:

   ```
   DEFAULT pxeboot
   TIMEOUT 20
   PROMPT 0
   LABEL pxeboot
       KERNEL http://<HTTP_server>/rhcos-<version>-live-kernel-<architecture>
       APPEND initrd=http://<HTTP_server>/rhcos-<version>-live-initramfs.<architecture>.img coreos.live.rootfs_url=http://<HTTP_server>/rhcos-<version>-live-rootfs.<architecture>.img coreos.inst.install_dev=/dev/sda coreos.inst.ignition_url=http://<HTTP_server>/bootstrap.ign
   ```

   where:

   `kernel`
   :   Specify the location of the live `kernel` file that you uploaded to your HTTP server. The URL must be HTTP, TFTP, or FTP; HTTPS and NFS are not supported.

   `initrd=main`
   :   If you use multiple NICs, specify a single interface in the `ip` option. For example, to use DHCP on a NIC that is named `eno1`, set `ip=eno1:dhcp`. Specify the locations of the RHCOS files that you uploaded to your HTTP server. The `initrd` parameter value is the location of the `initramfs` file, the `coreos.live.rootfs_url` parameter value is the location of the `rootfs` file, and the `coreos.inst.ignition_url` parameter value is the location of the bootstrap Ignition config file. You can also add more kernel arguments to the `APPEND` line to configure networking or other boot options.

       Note

       This configuration does not enable serial console access on machines with a graphical console. To configure a different console, add one or more `console=` arguments to the `APPEND` line. For example, add `console=tty0 console=ttyS0` to set the first PC serial port as the primary console and the graphical console as a secondary console. For more information, see [How does one set up a serial terminal and/or console in Red Hat Enterprise Linux?](https://access.redhat.com/articles/7212) and "Enabling the serial console for PXE and ISO installation" in the "Advanced RHCOS installation configuration" section.
8. Monitor the progress of the RHCOS installation on the console of the machine.

   Important

   Be sure that the installation is successful on each node before commencing with the OpenShift Container Platform installation. Observing the installation process can also help to determine the cause of RHCOS installation issues that might arise.
9. After RHCOS installs, the system reboots. During reboot, the system applies the Ignition config file that you specified.
10. Check the console output to verify that Ignition ran.

    **Example command**

    ```
    Ignition: ran on 2022/03/14 14:48:33 UTC (this boot)
    Ignition: user-provided config was applied
    ```
11. Continue to create the machines for your cluster.

    Important

    You must create the bootstrap and control plane machines at this time. If the control plane machines are not made schedulable, also create at least two compute machines before you install the cluster.

    If the required network, DNS, and load balancer infrastructure are in place, the OpenShift Container Platform bootstrap process begins automatically after the RHCOS nodes have rebooted.

    Note

    RHCOS nodes do not include a default password for the `core` user. You can access the nodes by running `ssh core@<node>.<cluster_name>.<base_domain>` as a user with access to the SSH private key that is paired to the public key that you specified in your `install_config.yaml` file. OpenShift Container Platform 4 cluster nodes running RHCOS are immutable and rely on Operators to apply cluster changes. Accessing cluster nodes by using SSH is not recommended. However, when investigating installation issues, if the OpenShift Container Platform API is not available, or the kubelet is not properly functioning on a target node, SSH access might be required for debugging or disaster recovery.

#### [3.11.4. Enabling multipathing with kernel arguments on RHCOS](#rhcos-enabling-multipathday-1-power_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

During installation, you can enable multipathing for provisioned nodes on IBM Power®. RHCOS supports multipathing on the primary disk, providing stronger resilience to hardware failure.

During the initial cluster creation, you might want to add kernel arguments to all control plane or worker nodes. To add kernel arguments to control plane or worker nodes, you can create a `MachineConfig` object and inject that object into the set of manifest files used by Ignition during cluster setup.

**Procedure**

1. Change to the directory that contains the installation program and generate the Kubernetes manifests for the cluster:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```
2. Decide if you want to add kernel arguments to worker or control plane nodes.

   * Create a machine config file. For example, create a `99-master-kargs-mpath.yaml` that instructs the cluster to add the control plane label and identify the multipath kernel argument:

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
3. To enable multipathing on worker nodes:

   * Create a machine config file. For example, create a `99-worker-kargs-mpath.yaml` that instructs the cluster to add the compute label and identify the multipath kernel argument:

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

     You can now continue on to create the cluster.

Important

Additional postinstallation steps are required to fully enable multipathing. For more information, see "Enabling multipathing with kernel arguments on RHCOS" in *Postinstallation machine configuration tasks*.

In case of MPIO failure, use the `bootlist` command to update the boot device list with alternate logical device names. The command displays a boot list and designates the possible boot devices for when the system is booted in normal mode.

1. To display a boot list and specify the possible boot devices if the system is booted in normal mode, enter the following command:

   ```
   $ bootlist -m normal -o
   sda
   ```
2. To update the boot list for normal mode and add alternate device names, enter the following command:

   ```
   $ bootlist -m normal -o /dev/sdc /dev/sdd /dev/sde
   sdc
   sdd
   sde
   ```

   If the original boot disk path is down, the node reboots from the alternate device registered in the normal boot device list.

### [3.12. Waiting for the bootstrap process to complete](#installation-installing-bare-metal_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

The OpenShift Container Platform bootstrap process begins after the cluster nodes first boot into the persistent RHCOS environment that has been installed to disk. The configuration information provided through the Ignition config files is used to initialize the bootstrap process and install OpenShift Container Platform on the machines. You must wait for the bootstrap process to complete.

**Prerequisites**

* You have created the Ignition config files for your cluster.
* You have configured suitable network, DNS, and load balancing infrastructure.
* You have obtained the installation program and generated the Ignition config files for your cluster.
* You installed RHCOS on your cluster machines and provided the Ignition config files that the OpenShift Container Platform installation program generated.

**Procedure**

1. Monitor the bootstrap process:

   ```
   $ ./openshift-install --dir <installation_directory> wait-for bootstrap-complete \
       --log-level=info
   ```

   where:

   `<installation_directory>`
   :   Specifies the path to the directory that stores the installation files.

   `--log-level=info`
   :   Specifies `warn`, `debug`, or `error` instead of `info` to view different installation details.

       **Example output**

       ```
       INFO Waiting up to 20m0s for the Kubernetes API at https://api.test.example.com:6443...
       INFO API v1.35.4 up
       INFO Waiting up to 1h0m0s for bootstrapping to complete...
       INFO It is now safe to remove the bootstrap resources
       ```

       The bootstrapping completion wait time varies per platform.

       The command succeeds when the Kubernetes API server signals that it has been bootstrapped on the control plane machines.
2. After the bootstrap process is complete, remove the bootstrap machine from the load balancer.

   Important

   You must remove the bootstrap machine from the load balancer at this point. You can also remove or reformat the bootstrap machine itself.

### [3.13. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and OpenShift Container Platform generates it during installation.

**Prerequisites**

* You deployed an OpenShift Container Platform cluster.
* You installed the OpenShift CLI (`oc`).

**Procedure**

1. Export the `kubeadmin` credentials by running the following command:

   ```
   $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
   ```

   where:

   `<installation_directory>`
   :   Specifies the path to the directory that stores the installation files.
2. Verify you can run `oc` commands successfully using the exported configuration by running the following command:

   ```
   $ oc whoami
   ```

   **Example output**

   ```
   system:admin
   ```

**Next steps**

* "Customize your cluster"
* "Remote health reporting"

### [3.14. Approving the certificate signing requests for your machines](#installation-approve-csrs_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

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

### [3.15. Initial Operator configuration](#installation-operators-config_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

After the control plane initializes, you must immediately configure some Operators so that they all become available.

**Prerequisites**

* Your control plane has initialized.

**Procedure**

1. Watch the cluster components come online:

   ```
   $ watch -n5 oc get clusteroperators
   ```

   **Example output**

   ```
   NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
   authentication                             4.22.0    True        False         False      19m
   baremetal                                  4.22.0    True        False         False      37m
   cloud-credential                           4.22.0    True        False         False      40m
   cluster-autoscaler                         4.22.0    True        False         False      37m
   config-operator                            4.22.0    True        False         False      38m
   console                                    4.22.0    True        False         False      26m
   csi-snapshot-controller                    4.22.0    True        False         False      37m
   dns                                        4.22.0    True        False         False      37m
   etcd                                       4.22.0    True        False         False      36m
   image-registry                             4.22.0    True        False         False      31m
   ingress                                    4.22.0    True        False         False      30m
   insights                                   4.22.0    True        False         False      31m
   kube-apiserver                             4.22.0    True        False         False      26m
   kube-controller-manager                    4.22.0    True        False         False      36m
   kube-scheduler                             4.22.0    True        False         False      36m
   kube-storage-version-migrator              4.22.0    True        False         False      37m
   machine-api                                4.22.0    True        False         False      29m
   machine-approver                           4.22.0    True        False         False      37m
   machine-config                             4.22.0    True        False         False      36m
   marketplace                                4.22.0    True        False         False      37m
   monitoring                                 4.22.0    True        False         False      29m
   network                                    4.22.0    True        False         False      38m
   node-tuning                                4.22.0    True        False         False      37m
   openshift-apiserver                        4.22.0    True        False         False      32m
   openshift-controller-manager               4.22.0    True        False         False      30m
   openshift-samples                          4.22.0    True        False         False      32m
   operator-lifecycle-manager                 4.22.0    True        False         False      37m
   operator-lifecycle-manager-catalog         4.22.0    True        False         False      37m
   operator-lifecycle-manager-packageserver   4.22.0    True        False         False      32m
   service-ca                                 4.22.0    True        False         False      38m
   storage                                    4.22.0    True        False         False      37m
   ```
2. Configure the Operators that are not available.

#### [3.15.1. Disabling the default software catalog sources](#olm-restricted-networks-operatorhub_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

To use only trusted or locally available Operator catalogs, disable the default software catalog sources that OpenShift Container Platform configures during installation. In a restricted network environment, you must disable the default catalogs as a cluster administrator.

**Procedure**

* Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object:

  ```
  $ oc patch OperatorHub cluster --type json \
      -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
  ```

  Tip

  Or, you can use the web console to manage catalog sources. From the **Administration** → **Cluster Settings** → **Configuration** → **OperatorHub** page, click the **Sources** tab, where you can create, update, delete, disable, and enable individual sources.

#### [3.15.2. Image registry storage configuration](#installation-registry-storage-config_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

The Image Registry Operator is not initially available for platforms that do not provide default storage. After installation, you must configure your registry to use storage so that the Registry Operator is made available.

Configure a persistent volume, which is required for production clusters. Where applicable, you can configure an empty directory as the storage location for non-production clusters.

You can also allow the image registry to use block storage types by using the `Recreate` rollout strategy during upgrades.

##### [3.15.2.1. Changing the image registry’s management state](#registry-change-management-state_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

To start the image registry, you must change the Image Registry Operator configuration’s `managementState` from `Removed` to `Managed`.

**Procedure**

* Change `managementState` Image Registry Operator configuration from `Removed` to `Managed`. For example:

  ```
  $ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"managementState":"Managed"}}'
  ```

##### [3.15.2.2. Configuring registry storage for IBM Power](#registry-configuring-storage-baremetal_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

As a cluster administrator, following installation you must configure your registry to use storage.

**Prerequisites**

* You have access to the cluster as a user with the `cluster-admin` role.
* You have a cluster on IBM Power®.
* You have provisioned persistent storage for your cluster, such as Red Hat OpenShift Data Foundation.

  Important

  OpenShift Container Platform supports `ReadWriteOnce` access for image registry storage when you have only one replica. `ReadWriteOnce` access also requires that the registry uses the `Recreate` rollout strategy. To deploy an image registry that supports high availability with two or more replicas, `ReadWriteMany` access is required.
* You must have a system with at least 100Gi capacity.

**Procedure**

1. To configure your registry to use storage, change the `spec.storage.pvc` in the `configs.imageregistry/cluster` resource.

   Note

   When you use shared storage, review your security settings to prevent outside access.
2. Verify that you do not have a registry pod:

   ```
   $ oc get pod -n openshift-image-registry -l docker-registry=default
   ```

   **Example output**

   ```
   No resources found in openshift-image-registry namespace
   ```

   Note

   If you do have a registry pod in your output, you do not need to continue with this procedure.
3. Check the registry configuration:

   ```
   $ oc edit configs.imageregistry.operator.openshift.io
   ```

   **Example output**

   ```
   storage:
     pvc:
       claim:
   ```

   Leave the `claim` field blank to allow the automatic creation of an `image-registry-storage` PVC.
4. Check the `clusteroperator` status:

   ```
   $ oc get clusteroperator image-registry
   ```

   **Example output**

   ```
   NAME             VERSION              AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
   image-registry   4.22                 True        False         False      6h50m
   ```
5. Ensure that your registry is set to managed to enable building and pushing of images.

   * Run:

     ```
     $ oc edit configs.imageregistry/cluster
     ```

     Then, change the line

     ```
     managementState: Removed
     ```

     to

     ```
     managementState: Managed
     ```

##### [3.15.2.3. Configuring storage for the image registry in non-production clusters](#installation-registry-storage-non-production_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

You must configure storage for the Image Registry Operator. For non-production clusters, you can set the image registry to an empty directory, but you lose all images if you restart the registry.

**Procedure**

* To set the image registry storage to an empty directory:

  ```
  $ oc patch configs.imageregistry.operator.openshift.io cluster --type merge --patch '{"spec":{"storage":{"emptyDir":{}}}}'
  ```

  Warning

  Configure this option only for non-production clusters.

  If you run this command before the Image Registry Operator initializes its components, the `oc patch` command fails with the following error:

  **Example output**

  ```
  Error from server (NotFound): configs.imageregistry.operator.openshift.io "cluster" not found
  ```

  Wait a few minutes and run the command again.

### [3.16. Completing installation on user-provisioned infrastructure](#installation-complete-user-infra_installing-restricted-networks-ibm-power) Copy linkLink copied to clipboard!

To finalize the installation on user-provisioned infrastructure, complete the cluster deployment after configuring the Operators. This ensures the cluster is fully operational on the infrastructure that you provide.

**Prerequisites**

* Your control plane has initialized.
* You have completed the initial Operator configuration.

**Procedure**

1. Confirm that all the cluster components are online with the following command:

   ```
   $ watch -n5 oc get clusteroperators
   ```

   **Example output**

   ```
   NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
   authentication                             4.22.0    True        False         False      19m
   baremetal                                  4.22.0    True        False         False      37m
   cloud-credential                           4.22.0    True        False         False      40m
   cluster-autoscaler                         4.22.0    True        False         False      37m
   config-operator                            4.22.0    True        False         False      38m
   console                                    4.22.0    True        False         False      26m
   csi-snapshot-controller                    4.22.0    True        False         False      37m
   dns                                        4.22.0    True        False         False      37m
   etcd                                       4.22.0    True        False         False      36m
   image-registry                             4.22.0    True        False         False      31m
   ingress                                    4.22.0    True        False         False      30m
   insights                                   4.22.0    True        False         False      31m
   kube-apiserver                             4.22.0    True        False         False      26m
   kube-controller-manager                    4.22.0    True        False         False      36m
   kube-scheduler                             4.22.0    True        False         False      36m
   kube-storage-version-migrator              4.22.0    True        False         False      37m
   machine-api                                4.22.0    True        False         False      29m
   machine-approver                           4.22.0    True        False         False      37m
   machine-config                             4.22.0    True        False         False      36m
   marketplace                                4.22.0    True        False         False      37muser
   monitoring                                 4.22.0    True        False         False      29m
   network                                    4.22.0    True        False         False      38m
   node-tuning                                4.22.0    True        False         False      37m
   openshift-apiserver                        4.22.0    True        False         False      32muser
   openshift-controller-manager               4.22.0    True        False         False      30m
   openshift-samples                          4.22.0    True        False         False      32m
   operator-lifecycle-manager                 4.22.0    True        False         False      37m
   operator-lifecycle-manager-catalog         4.22.0    True        False         False      37m
   operator-lifecycle-manager-packageserver   4.22.0    True        False         False      32m
   service-ca                                 4.22.0    True        False         False      38m
   storage                                    4.22.0    True        False         False      37m
   ```

   Alternatively, the following command notifies you when all of the clusters are available. The command also retrieves and displays credentials:

   ```
   $ ./openshift-install --dir <installation_directory> wait-for install-complete
   ```

   where:

   `<installation_directory>`
   :   Specifies the path to the directory that you stored the installation files in.

       **Example output**

       ```
       INFO Waiting up to 30m0s for the cluster to initialize...
       ```

       The command succeeds when the Cluster Version Operator finishes deploying the OpenShift Container Platform cluster from Kubernetes API server.

       Important

       * The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
       * It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
2. Confirm that the Kubernetes API server is communicating with the pods.

   1. To view a list of all pods, use the following command:

      ```
      $ oc get pods --all-namespaces
      ```

      **Example output**

      ```
      NAMESPACE                         NAME                                            READY   STATUS      RESTARTS   AGE
      openshift-apiserver-operator      openshift-apiserver-operator-85cb746d55-zqhs8   1/1     Running     1          9m
      openshift-apiserver               apiserver-67b9g                                 1/1     Running     0          3m
      openshift-apiserver               apiserver-ljcmx                                 1/1     Running     0          1m
      openshift-apiserver               apiserver-z25h4                                 1/1     Running     0          2m
      openshift-authentication-operator authentication-operator-69d5d8bf84-vh2n8        1/1     Running     0          5m
      ```
   2. View the logs for a pod that is listed in the output of the previous command by using the following command:

      ```
      $ oc logs <pod_name> -n <namespace>
      ```

      where:

      `<namespace>`
      :   Specifies the pod name and namespace, as shown in the output of an earlier command.

          If the pod logs display, the Kubernetes API server can communicate with the cluster machines.
3. Additional steps are required to enable multipathing. Do not enable multipathing during installation.

   See "Enabling multipathing with kernel arguments on RHCOS" in the *Postinstallation machine configuration tasks* documentation for more information.
4. Register your cluster on the [Cluster registration](https://console.redhat.com/openshift/register) page.

## [Chapter 4. Installation configuration parameters for IBM Power](#installation-config-parameters-ibm-power) Copy linkLink copied to clipboard!

Before you deploy an OpenShift Container Platform cluster, you create a customized `install-config.yaml` installation configuration file that describes the details for your environment.

### [4.1. Available installation configuration parameters for IBM Power](#installation-configuration-parameters_installation-config-parameters-ibm-power) Copy linkLink copied to clipboard!

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file.

The following tables specify the required, optional, and IBM Power-specific installation configuration parameters that you can set as part of the installation process.

Important

After installation, you cannot change these parameters in the `install-config.yaml` file.

#### [4.1.1. Required configuration parameters](#installation-configuration-parameters-required_installation-config-parameters-ibm-power) Copy linkLink copied to clipboard!

Required installation configuration parameters are described in the following table:

Expand

Table 4.1. Required parameters

| Parameter | Description |
| --- | --- |
| ``` apiVersion: ``` | The API version for the `install-config.yaml` content. The current version is `v1`. The installation program might also support older API versions.  **Value:** String |
| ``` baseDomain: ``` | The base domain of your cloud provider. The base domain is used to create routes to your OpenShift Container Platform cluster components. The full DNS name for your cluster is a combination of the `baseDomain` and `metadata.name` parameter values that uses the `<metadata.name>.<baseDomain>` format.  **Value:** A fully-qualified domain or subdomain name, such as `example.com`. |
| ``` metadata: ``` | Kubernetes resource `ObjectMeta`, from which only the `name` parameter is consumed.  **Value:** Object |
| ``` metadata:   name: ``` | The name of the cluster. DNS records for the cluster are all subdomains of `{{.metadata.name}}.{{.baseDomain}}`.  **Value:** String of lowercase letters, hyphens (`-`), and periods (`.`), such as `dev`. |
| ``` platform: ``` | The configuration for the specific platform upon which to perform the installation: `aws`, `baremetal`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`. For additional information about `platform.<platform>` parameters, consult the table for your specific platform that follows.  **Value:** Object |
| ``` pullSecret: ``` | Get a [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) to authenticate downloading container images for OpenShift Container Platform components from services such as Quay.io.  **Value:**  ``` {    "auths":{       "cloud.openshift.com":{          "auth":"b3Blb=",          "email":"you@example.com"       },       "quay.io":{          "auth":"b3Blb=",          "email":"you@example.com"       }    } } ``` |

Show more

#### [4.1.2. Network configuration parameters](#installation-configuration-parameters-network_installation-config-parameters-ibm-power) Copy linkLink copied to clipboard!

You can customize your installation configuration based on the requirements of your existing network infrastructure. For example, you can expand the IP address block for the cluster network or configure different IP address blocks than the defaults.

Consider the following information before you configure network parameters for your cluster:

* If you use the Red Hat OpenShift Networking OVN-Kubernetes network plugin, both IPv4 and IPv6 address families are supported.
* If you deployed nodes in an OpenShift Container Platform cluster with a network that supports both IPv4 and non-link-local IPv6 addresses, configure your cluster to use a dual-stack network.

  + For clusters configured for dual-stack networking, both IPv4 and IPv6 traffic must use the same network interface as the default gateway. This ensures that in a multiple network interface controller (NIC) environment, a cluster can detect what NIC to use based on the available network interface. For more information, see "OVN-Kubernetes IPv6 and dual-stack limitations" in *About the OVN-Kubernetes network plugin*.
  + To prevent network connectivity issues, do not install a single-stack IPv4 cluster on a host that supports dual-stack networking.

If you configure your cluster to use both IP address families, review the following requirements:

* Both IP families must use the same network interface for the default gateway.
* Both IP families must have the default gateway.
* You must specify IPv4 and IPv6 addresses in the same order for all network configuration parameters. For example, in the following configuration, IPv4 addresses are listed before IPv6 addresses:

  ```
  networking:
    clusterNetwork:
    - cidr: 10.128.0.0/14
      hostPrefix: 23
    - cidr: fd00:10:128::/56
      hostPrefix: 64
    serviceNetwork:
    - 172.30.0.0/16
    - fd00:172:16::/112
  ```

  If you are installing your cluster on AWS, the order of address families must match the `platform.aws.ipFamily` parameter. For example, if you specified the `DualStackIPv6Primary` parameter, you must list the IPv6 address first.

Expand

Table 4.2. Network parameters

| Parameter | Description |
| --- | --- |
| ``` networking: ``` | The configuration for the cluster network.  **Value:** Object  Note  You cannot change parameters specified by the `networking` object after installation. |
| ``` networking:   networkType: ``` | The Red Hat OpenShift Networking network plugin to install.  **Value:**`OVNKubernetes`. `OVNKubernetes` is a Container Network Interface (CNI) plugin for Linux networks and hybrid networks that contain both Linux and Windows servers. The default value is `OVNKubernetes`. |
| ``` networking:   clusterNetwork: ``` | The IP address blocks for pods.  The default value is `10.128.0.0/14` with a host prefix of `/23`.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  ``` networking:   clusterNetwork:   - cidr: 10.128.0.0/14     hostPrefix: 23 ``` |
| ``` networking:   clusterNetwork:     cidr: ``` | Required if you use `networking.clusterNetwork`. An IP address block.  An IPv4 network. |
| ``` networking:   clusterNetwork:     hostPrefix: ``` | The subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23` then each node is assigned a `/23` subnet out of the given `cidr`. A `hostPrefix` value of `23` provides 510 (2^(32 - 23) - 2) pod IP addresses.  **Value:** A subnet prefix.  The default value is `23`. |
| ``` networking:   serviceNetwork: ``` | The IP address block for services. The default value is `172.30.0.0/16`.  **Value:** An array with an IP address block in CIDR format. For example:  ``` networking:   serviceNetwork:    - 172.30.0.0/16 ``` |
| ``` networking:   machineNetwork: ``` | The IP address blocks for machines.  If you specify multiple IP address blocks, the blocks must not overlap.  If you specify multiple IP kernel arguments, the `machineNetwork.cidr` value must be the CIDR of the primary network.  **Value:** An array of objects. For example:  ``` networking:   machineNetwork:   - cidr: 10.0.0.0/16 ``` |
| ``` networking:   machineNetwork:     cidr: ``` | Required if you use `networking.machineNetwork`. An IP address block. The default value is `10.0.0.0/16` for all platforms other than libvirt and IBM Power® Virtual Server. For libvirt, the default value is `192.168.126.0/24`. For IBM Power® Virtual Server, the default value is `192.168.0.0/24`.  **Value:** An IP network block in CIDR notation.  For example, `10.0.0.0/16`.  Note  Set the `networking.machineNetwork` to match the CIDR of the preferred NIC.  If you are installing a cluster on AWS with dual-stack networking, consider the following distinction:  * If the installation program creates the VPC, do not specify an IPv6 entry in `networking.machineNetwork`. The installation program will assign an IPv6 address to the VPC. * If you provide existing dual-stack subnets using the `platform.aws.vpc.subnets` parameter, you must specify IPv6 entries corresponding to either the VPC CIDR or the CIDR of the subnets. * In both cases, you must provide an IPv4 CIDR entry. |
| ``` networking:   ovnKubernetesConfig:     ipv4:       internalJoinSubnet: ``` | Configures the IPv4 join subnet that is used internally by `ovn-kubernetes`. This subnet must not overlap with any other subnet that OpenShift Container Platform is using, including the node network. The size of the subnet must be larger than the number of nodes. You cannot change the value after installation.  **Value:** An IP network block in CIDR notation. The default value is `100.64.0.0/16`. |

Show more

#### [4.1.3. Optional configuration parameters](#installation-configuration-parameters-optional_installation-config-parameters-ibm-power) Copy linkLink copied to clipboard!

Optional installation configuration parameters are described in the following table:

Expand

Table 4.3. Optional parameters

| Parameter | Description |
| --- | --- |
| ``` additionalTrustBundle: ``` | A PEM-encoded X.509 certificate bundle that is added to the nodes' trusted certificate store. This trust bundle might also be used when a proxy has been configured.  **Value:** String |
| ``` capabilities: ``` | Controls the installation of optional core cluster components. You can reduce the footprint of your OpenShift Container Platform cluster by disabling optional components. For more information, see the "Cluster capabilities" page in *Installing*.  **Value:** String array |
| ``` capabilities:   baselineCapabilitySet: ``` | Selects an initial set of optional capabilities to enable. Valid values are `None`, `v4.11`, `v4.12` and `vCurrent`. The default value is `vCurrent`.  **Value:** String |
| ``` capabilities:   additionalEnabledCapabilities: ``` | Extends the set of optional capabilities beyond what you specify in `baselineCapabilitySet`. You can specify multiple capabilities in this parameter.  **Value:** String array |
| ``` cpuPartitioningMode: ``` | Enables workload partitioning, which isolates OpenShift Container Platform services, cluster management workloads, and infrastructure pods to run on a reserved set of CPUs. You can only enable workload partitioning during installation. You cannot disable it after installation. While this field enables workload partitioning, it does not configure workloads to use specific CPUs. For more information, see the *Workload partitioning* page in the *Scalability and Performance* section.  **Value:** `None` or `AllNodes`. `None` is the default value. |
| ``` compute: ``` | The configuration for the machines that comprise the compute nodes.  **Value:** Array of `MachinePool` objects. |
| ``` compute:   architecture: ``` | Determines the instruction set architecture of the machines in the pool. Currently, heterogeneous clusters are not supported, so all pools must specify the same architecture. The valid value is the default: `ppc64le`.  **Value:** String |
| ``` compute:   hyperthreading: ``` | Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on compute machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important  If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled` |
| ``` compute:   name: ``` | Required if you use `compute`. The name of the machine pool.  **Value:** `worker` |
| ``` compute:   platform: ``` | Required if you use `compute`. Use this parameter to specify the cloud provider to host the worker machines. This parameter value must match the `controlPlane.platform` parameter value.  **Value:**`aws`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}` |
| ``` compute:   replicas: ``` | The number of compute machines, which are also known as worker machines, to provision.  **Value:** A positive integer greater than or equal to `2`. The default value is `3`. |
| ``` featureSet: ``` | Enables the cluster for a feature set. A feature set is a collection of OpenShift Container Platform features that are not enabled by default. For more information about enabling a feature set during installation, see "Enabling features using feature gates".  **Value:** String. The name of the feature set to enable, such as `TechPreviewNoUpgrade`. |
| ``` controlPlane: ``` | The configuration for the machines that form the control plane.  **Value:** Array of `MachinePool` objects. |
| ``` controlPlane:   architecture: ``` | Determines the instruction set architecture of the machines in the pool. Currently, heterogeneous clusters are not supported, so all pools must specify the same architecture. The valid value is the default: `ppc64le`.  **Value:** String |
| ``` controlPlane:   hyperthreading: ``` | Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on control plane machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important  If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled` |
| ``` controlPlane:   name: ``` | Required if you use `controlPlane`. The name of the machine pool.  **Value:** `master` |
| ``` controlPlane:   platform: ``` | Required if you use `controlPlane`. Use this parameter to specify the cloud provider that hosts the control plane machines. This parameter value must match the `compute.platform` parameter value.  **Value:**`aws`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}` |
| ``` controlPlane:   replicas: ``` | The number of control plane machines to provision.  **Value:** Supported values are `3`, or `1` when deploying single-node OpenShift. |
| ``` arbiter:     name: ``` | The OpenShift Container Platform cluster requires a name for arbiter nodes. For example, `arbiter`. |
| ``` arbiter:     replicas: ``` | The `replicas` parameter sets the number of arbiter nodes for the OpenShift Container Platform cluster. You cannot set this field to a value that is greater than 1. |
| ``` credentialsMode: ``` | The Cloud Credential Operator (CCO) mode. If no mode is specified, the CCO dynamically tries to determine the capabilities of the provided credentials, with a preference for mint mode on the platforms where multiple modes are supported.  Note  Not all CCO modes are supported for all cloud providers. For more information about CCO modes, see the "Managing cloud provider credentials" entry in the *Authentication and authorization* content.  **Value:** `Mint`, `Passthrough`, `Manual` or an empty string (`""`). |
| ``` fips: ``` | Enable or disable FIPS mode. The default is `false` (disabled). If you enable FIPS mode, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that RHCOS provides instead.  Important  To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening).  When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86\_64, ppc64le, and s390x architectures.   Important  If you are using Azure File storage, you cannot enable FIPS mode.  **Value:** `false` or `true` |
| ``` endpoint:   name: <endpoint_name>   clusterUseOnly: `true` or `false` ``` | The `name` parameter contains the name of the Private Service Connect (PSC) endpoints.  Important  When `clusterUseOnly` is `false`, its default setting, you must run the installation program from a bastion host that is within the same VPC where you want to deploy the cluster.  When you want the installation program to use the public API endpoints and cluster Operators to use the API endpoint overrides, set `clusterUseOnly` to `true`. When you want both the installation program and the cluster Operators to use the API endpoint overrides, for example if you are running the installation program from a bastion host that is within the same VPC where you want to deploy the cluster, set `clusterUseOnly` to `false` . The parameter is optional and defaults to `false`.  **Value:** String or boolean |
| ``` imageContentSources: ``` | Sources and repositories for the release-image content.  **Value:** Array of objects. Includes a `source` and, optionally, `mirrors`, as described in the following rows of this table. |
| ``` imageContentSources:   source: ``` | Required if you use `imageContentSources`. Specify the repository that users refer to, for example, in image pull specifications.  **Value:** String |
| ``` imageContentSources:   mirrors: ``` | Specify one or more repositories that might also contain the same images.  **Value:** Array of strings |
| ``` osImageStream: ``` | Specifies the image stream that will be used for all machines in the cluster. `osImageStream` is a Technology Preview feature. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.  **Value:** String. Valid values are `rhel-9` or `rhel-10`. |
| ``` publish: ``` | How to publish or expose the user-facing endpoints of your cluster, such as the Kubernetes API, OpenShift routes.  **Value:**`Internal` or `External`. The default value is `External`.  Setting this field to `Internal` is not supported on non-cloud platforms. |
| ``` sshKey: ``` | The SSH key to authenticate access to your cluster machines.  Note  For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.  **Value:** For example, `sshKey: ssh-ed25519 AAAA..`. |

Show more

## [Legal Notice](#idm140143185828416) Copy linkLink copied to clipboard!

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
