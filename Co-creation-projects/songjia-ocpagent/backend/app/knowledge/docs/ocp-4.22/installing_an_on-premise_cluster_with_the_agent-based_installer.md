---
title: "Installing an on-premise cluster with the Agent-based Installer"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_an_on-premise_cluster_with_the_agent-based_installer/index
retrieved_at: 2026-09-05T05:41:55.598147+00:00
---

# Installing an on-premise cluster with the Agent-based Installer

---

OpenShift Container Platform 4.22

## Installing an on-premise OpenShift Container Platform cluster with the Agent-based Installer

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140203237577328)

**Abstract**

This document describes how to install an on-premise OpenShift Container Platform cluster with the Agent-based Installer.

---

## [Chapter 1. Preparing to install with the Agent-based Installer](#preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

The Agent-based Installer provides the flexibility to boot your on-premise servers in any way that you choose. It combines the ease of use of the Assisted Installation service with the ability to run offline, including in air-gapped environments.

The Agent-based Installer uses a subcommand of the OpenShift Container Platform installation program. It generates a bootable ISO image containing all of the information required to deploy an OpenShift Container Platform cluster, with an available release image.

The configuration is in the same format as for the installer-provisioned infrastructure and user-provisioned infrastructure installation methods. The Agent-based Installer can also optionally generate or accept Zero Touch Provisioning (ZTP) custom resources. ZTP allows you to provision new edge sites with declarative configurations of bare-metal equipment.

Note

To deploy clusters with virtualized control planes running on OpenShift Virtualization VMs, you can use KubeVirt Redfish to expose VMs as Redfish-compatible endpoints. For more information about using virtualized control planes, see "Using virtualized control planes".

Expand

Table 1.1. Agent-based Installer supported architectures

| CPU architecture | Connected installation | Disconnected installation |
| --- | --- | --- |
| `64-bit x86` | ✓ | ✓ |
| `64-bit ARM` | ✓ | ✓ |
| `ppc64le` | ✓ | ✓ |
| `s390x` | ✓ | ✓ |

Show more

### [1.1. Understanding Agent-based Installer](#understanding-agent-install_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

As an OpenShift Container Platform user, you can leverage the advantages of the Assisted Installer hosted service in disconnected environments.

The Agent-based Installer uses a bootable ISO that contains the Assisted discovery agent and the Assisted Service. Both are required to perform the cluster installation, but the Assisted Service runs on only one of the hosts.

Note

Currently, ISO boot support on IBM Z® (`s390x`) is available only for Red Hat Enterprise Linux (RHEL) KVM, which provides the flexibility to choose either PXE or ISO-based installation. For installations with z/VM and Logical Partition (LPAR), only PXE boot is supported.

The `openshift-install agent create image` subcommand generates an ephemeral ISO based on the inputs that you provide. You can choose to provide inputs through the following manifests:

Preferred manifests:

* `install-config.yaml`
* `agent-config.yaml`

Optional ZTP manifests:

* `cluster-manifests/cluster-deployment.yaml`
* `cluster-manifests/agent-cluster-install.yaml`
* `cluster-manifests/pull-secret.yaml`
* `cluster-manifests/infraenv.yaml`
* `cluster-manifests/cluster-image-set.yaml`
* `cluster-manifests/nmstateconfig.yaml`
* `mirror/registries.conf`
* `mirror/ca-bundle.crt`

#### [1.1.1. Agent-based Installer workflow](#agent-based-installer-workflow_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

One of the control plane hosts runs the Assisted Service at the start of the boot process and eventually becomes the bootstrap host. This node is called the **rendezvous host** (or node 0).

The Assisted Service ensures that all the hosts meet the requirements and triggers an OpenShift Container Platform cluster deployment. All the nodes have the Red Hat Enterprise Linux (RHEL) image written to the disk. The non-bootstrap nodes reboot and initiate a cluster deployment.

Once the nodes are rebooted, the rendezvous host reboots and joins the cluster. The bootstrapping is then complete and the cluster is deployed.

**Figure 1.1. Node installation workflow**

You can install a disconnected OpenShift Container Platform cluster through the `openshift-install agent create image` subcommand for the following topologies:

* **A single-node OpenShift Container Platform cluster**: A node that is both a control plane and compute.
* **A three-node OpenShift Container Platform cluster** : A compact cluster that has three control plane nodes that are also compute nodes.
* **Highly available OpenShift Container Platform cluster (HA)**: Three control plane nodes with any number of compute nodes.
* **Two-node OpenShift Container Platform cluster with Arbiter**: Two control plane nodes with one local arbiter node. For more information, see "About a local arbiter node".

#### [1.1.2. Recommended resources for topologies](#agent-based-installer-recommended-resources_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

The following cluster resources are recommended for each topology:

Expand

Table 1.2. Recommended cluster resources

| Topology | Number of control plane nodes | Number of compute nodes | vCPU | Memory | Storage |
| --- | --- | --- | --- | --- | --- |
| Single-node cluster | 1 | 0 | 8 vCPUs | 16 GB of RAM | 120 GB |
| Two-node OpenShift cluster with Arbiter | 2 (control plane nodes) | 0 | 4 vCPUs | 16 GB of RAM | 120 GB |
| 1 (arbiter node) | 0 | 2 vCPUs | 8 GB of RAM | 50 GB |
| Two-node OpenShift cluster with fencing (TNF) | 2 | 0 | 4 vCPUs | 16 GB of RAM | 120 GB |
| Compact cluster | 3 | 0 or 1 | 8 vCPUs | 16 GB of RAM | 120 GB |
| HA cluster | 3 to 5 | 2 and above | 8 vCPUs | 16 GB of RAM | 120 GB |

Show more

Note

You can use as few as 4 vCPUs for an single-node OpenShift cluster.

However, running single-node OpenShift on 4 vCPUs leaves very little "headroom" for user applications, and creates a high risk of resource contention and performance degradation.

To ensure cluster stability at this threshold, you must take steps to minimize the total resource footprint of the cluster, such as limiting the amount of workloads running on the cluster or limiting cluster capabilities. For more information, see "Cluster capabilities".

Otherwise, it is recommended to provide more compute resources to the cluster.

#### [1.1.3. Supported platforms](#agent-based-installer-supported-platforms_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

In the `install-config.yaml` file, specify the platform on which to perform the installation. The following platforms are supported:

* `baremetal`
* `vsphere`
* `nutanix`
* `external`
* `none`

For a two-node OpenShift Container Platform cluster with fencing (TNF), only the following platforms are supported:

* `baremetal`
* `external`
* `none`

  The `vsphere` and `nutanix` platforms are not supported for two-node clusters with fencing.

Important

For platform `none`:

* The `none` option requires the provision of DNS name resolution and load balancing infrastructure in your cluster. See *Requirements for a cluster using the platform "none" option* in the "Additional resources" section for more information.
* See "Deploying OpenShift 4.x on non-tested platforms using the bare metal install method" before you attempt to install an OpenShift Container Platform cluster in virtualized or cloud environments.

Note

For installations on IBM Z® (`s390x`) architecture, the minimum memory requirement is 24 GB RAM per host instead of 16 GB.

### [1.2. About FIPS compliance](#agent-installer-fips-compliance_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

For many OpenShift Container Platform customers, regulatory readiness, or compliance, on some level is required before any systems can be put into production. That regulatory readiness can be imposed by national standards, industry standards or the organization’s corporate governance framework.

Federal Information Processing Standards (FIPS) compliance is one of the most critical components required in highly secure environments to ensure that only supported cryptographic technologies are allowed on nodes.

Important

To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening).

When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86\_64, ppc64le, and s390x architectures.

### [1.3. Configure FIPS through the Agent-based Installer](#agent-installer-configuring-fips-compliance_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

During a cluster deployment, the Federal Information Processing Standards (FIPS) change is applied when the Red Hat Enterprise Linux CoreOS (RHCOS) machines are deployed in your cluster. For Red Hat Enterprise Linux (RHEL) machines, you must enable FIPS mode when you install the operating system on the machines that you plan to use as worker machines.

Important

OpenShift Container Platform requires the use of a FIPS-capable installation binary to install a cluster in FIPS mode.

You can enable FIPS mode through the preferred method of `install-config.yaml` and `agent-config.yaml` files:

You must set value of the `fips` field to `true` in the `install-config.yaml` file:

**Sample install-config.yaml.file**

```
apiVersion: v1
baseDomain: test.example.com
metadata:
  name: sno-cluster
fips: true
```

Important

To enable FIPS mode on IBM Z® clusters, you must also enable FIPS in either the `.parm` file or using `virt-install` as outlined in the procedures for manually adding IBM Z® agents.

If you are using the optional GitOps ZTP manifests, you must set the value of `fips` as `true` in the `agent-install.openshift.io/install-config-overrides` field in the `agent-cluster-install.yaml` file:

**Sample agent-cluster-install.yaml file**

```
apiVersion: extensions.hive.openshift.io/v1beta1
kind: AgentClusterInstall
metadata:
  annotations:
    agent-install.openshift.io/install-config-overrides: '{"fips":true}'
  name: sno-cluster
  namespace: sno-cluster-test
```

### [1.4. Host configuration](#agent-host-config_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

You can make additional configurations for each host on the cluster in the `agent-config.yaml` file, such as network configurations and root device hints.

Important

For each host you configure, you must specify which host you are configuring by providing the MAC address of an interface on the host.

#### [1.4.1. Host roles](#agent-host-roles_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

Each host in the cluster is assigned a role of either `master` or `worker`. You can define the role for each host in the `agent-config.yaml` file by using the `role` parameter. If you do not assign a role to the hosts, the roles will be assigned at random during installation.

It is recommended to explicitly define roles for your hosts.

The `rendezvousIP` must be assigned to a host with the `master` role. This can be done manually or by allowing the Agent-based Installer to assign the role.

Important

You do not need to explicitly define the `master` role for the rendezvous host, however you cannot create configurations that conflict with this assignment.

For example, if you have 4 hosts with 3 of the hosts explicitly defined to have the `master` role, the last host that is automatically assigned the `worker` role during installation cannot be configured as the rendezvous host.

**Sample agent-config.yaml file**

```
apiVersion: v1beta1
kind: AgentConfig
metadata:
  name: example-cluster
rendezvousIP: 192.168.111.80
hosts:
  - hostname: master-1
    role: master
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a5
  - hostname: master-2
    role: master
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a6
  - hostname: master-3
    role: master
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a7
  - hostname: worker-1
    role: worker
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a8
```

#### [1.4.2. About root device hints](#root-device-hints_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

The `rootDeviceHints` parameter enables the installation program to provision the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device.

The installation program examines the devices in the order it discovers them, and compares the discovered values with the hint values. The installation program uses the first discovered device that matches the hint value. The configuration can combine multiple hints, but a device must match all hints for the installation program to select it.

Expand

Table 1.3. Subfields

| Subfield | Description |
| --- | --- |
| `deviceName` | A string containing a Linux device name such as `/dev/vda` or `/dev/disk/by-path/`.  Note  It is recommended to use the `/dev/disk/by-path/<device_path>` link to the storage location.  The hint must match the actual value exactly. |
| `hctl` | A string containing a SCSI bus address like `0:0:0:0`. The hint must match the actual value exactly. |
| `model` | A string containing a vendor-specific device identifier. The hint can be a substring of the actual value. |
| `vendor` | A string containing the name of the vendor or manufacturer of the device. The hint can be a sub-string of the actual value. |
| `serialNumber` | A string containing the device serial number. The hint must match the actual value exactly. |
| `minSizeGigabytes` | An integer representing the minimum size of the device in gigabytes. |
| `wwn` | A string containing the unique storage identifier. The hint must match the actual value exactly. If you use the `udevadm` command to retrieve the `wwn` value, and the command outputs a value for `ID_WWN_WITH_EXTENSION`, then you must use this value to specify the `wwn` subfield. |
| `rotational` | A boolean indicating whether the device should be a rotating disk (true) or not (false). |

Show more

**Example usage**

```
     - name: master-0
       role: master
       rootDeviceHints:
         deviceName: "/dev/sda"
```

### [1.5. About networking](#agent-install-networking_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

The **rendezvous IP** must be known at the time of generating the agent ISO, so that during the initial boot all the hosts can check in to the assisted service.

If the IP addresses are assigned using a Dynamic Host Configuration Protocol (DHCP) server, then the `rendezvousIP` field must be set to an IP address of one of the hosts that will become part of the deployed control plane. In an environment without a DHCP server, you can define IP addresses statically.

In addition to static IP addresses, you can apply any network configuration that is in NMState format. This includes VLANs and NIC bonds.

Note

By default, Podman uses a subnet of `10.88.0.0/16` as a bridge network. Do not set the `network.machineNetwork.cidr` parameter to include this address range, otherwise a conflict causes the cluster installation to fail.

#### [1.5.1. Port requirements for the rendezvous host](#agent-install-networking-ports_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

During the discovery and bootstrap phases of an installation, all the hosts connect to the Assisted Service that runs on the rendezvous host. Configure your firewall to allow the following traffic from each host to the rendezvous host:

Expand

Table 1.4. Ports required to reach the Assisted Service on the rendezvous host

| Port | Protocol | Description |
| --- | --- | --- |
| `8090` | TCP | Assisted Service API. Hosts use this port to register with the Assisted Service, report hardware information, and retrieve installation instructions. |

Show more

Note

Port `8090` is required only during installation. After installation completes, the Assisted Service is no longer exposed on the rendezvous host.

This specific port requirement is in addition to the standard OpenShift Container Platform networking requirements for installation.

#### [1.5.2. DHCP](#agent-install-networking-DHCP_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

When using Dynamic Host Configuration Protocol (DHCP), you must specify the value for the `rendezvousIP` field in the `agent-config.yaml` file, and the `networkConfig` fields can be left blank:

**Sample agent-config.yaml.file**

```
apiVersion: v1alpha1
kind: AgentConfig
metadata:
  name: sno-cluster
rendezvousIP: 192.168.111.80
```

where:

`rendezvousIP`
:   Specifies the IP address for the rendezvous host.

#### [1.5.3. Static networking](#agent-install-networking-static_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

When using static networking with the preferred `install-config.yaml` and `agent-config.yaml` files, you can specify the value for the `rendezvousIP` field in the `agent-config.yaml` file or allow the installation program to choose a static IP address from the `networkConfig` fields.

**Sample agent-config.yaml.file**

```
cat > agent-config.yaml << EOF
apiVersion: v1alpha1
kind: AgentConfig
metadata:
  name: sno-cluster
rendezvousIP: 192.168.111.80
hosts:
  - hostname: master-0
    interfaces:
      - name: eno1
        macAddress: 00:ef:44:21:e6:a5
    networkConfig:
      interfaces:
        - name: eno1
          type: ethernet
          state: up
          mac-address: 00:ef:44:21:e6:a5
          ipv4:
            enabled: true
            address:
              - ip: 192.168.111.80
                prefix-length: 23
            dhcp: false
      dns-resolver:
        config:
          server:
            - 192.168.111.1
      routes:
        config:
          - destination: 0.0.0.0/0
            next-hop-address: 192.168.111.1
            next-hop-interface: eno1
            table-id: 254
EOF
```

where:

`rendezvousIP`
:   Specifies the IP address for the rendezvous host. If a value is not specified for the `rendezvousIP` field, one address will be chosen from the static IP addresses specified in the `networkConfig` fields.

`hosts.interfaces.macAddress`
:   Specifies the MAC address of an interface on the host, used to determine which host to apply the configuration to.

`ipv4.address.ip`
:   Specifies the static IP address of the target bare-metal host.

`ipv4.address.prefix-length`
:   Specifies the static IP address’s subnet prefix for the target bare-metal host.

`dns-resolver.config.server`
:   Specifies the DNS server for the target bare-metal host.

`routes.config.next-hop-address`
:   Specifies the next-hop address for the node traffic. This must be in the same subnet as the IP address set for the specified interface.

When using static networking with the optional method of GitOps ZTP custom resources, which comprises 6 custom resources, you can configure static IPs in the `nmstateconfig.yaml` file. The rendezvous IP is chosen from the static IP addresses specified in the `config` fields.

**Sample nmstateconfig.yaml file**

```
apiVersion: agent-install.openshift.io/v1beta1
kind: NMStateConfig
metadata:
  name: master-0
  namespace: openshift-machine-api
  labels:
    cluster0-nmstate-label-name: cluster0-nmstate-label-value
spec:
  config:
    interfaces:
      - name: eth0
        type: ethernet
        state: up
        mac-address: 52:54:01:aa:aa:a1
        ipv4:
          enabled: true
          address:
            - ip: 192.168.122.2
              prefix-length: 23
          dhcp: false
    dns-resolver:
      config:
        server:
          - 192.168.122.1
    routes:
      config:
        - destination: 0.0.0.0/0
          next-hop-address: 192.168.122.1
          next-hop-interface: eth0
          table-id: 254
  interfaces:
    - name: eth0
      macAddress: 52:54:01:aa:aa:a1
```

where:

`ipv4.address.ip`
:   Specifies the static IP address of the target bare-metal host.

`ipv4.address.prefix-length`
:   Specifies the static IP address’s subnet prefix for the target bare-metal host.

`dns-resolver.config.server`
:   Specifies the DNS server for the target bare-metal host.

`routes.config.next-hop-address`
:   Specifies the next-hop address for the node traffic. This must be in the same subnet as the IP address set for the specified interface.

`spec.interfaces.macAddress`
:   Specifies the MAC address of an interface on the host, used to determine which host to apply the configuration to.

### [1.6. Requirements for a cluster using the platform "none" option](#installation-requirements-platform-none_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

There are additional requirements when installing a cluster using the platform "none" option with the Agent-based Installer.

Important

See "Deploying OpenShift 4.x on non-tested platforms using the bare metal install method" before you attempt to install an OpenShift Container Platform cluster in virtualized or cloud environments.

#### [1.6.1. Platform "none" DNS requirements](#agent-install-dns-none_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

In OpenShift Container Platform deployments, DNS name resolution is required for several components.

The following components need DNS name resolution:

* The Kubernetes API
* The OpenShift Container Platform application wildcard
* The control plane and compute machines

Reverse DNS resolution is also required for the Kubernetes API, the control plane machines, and the compute machines.

DNS A/AAAA or CNAME records are used for name resolution and PTR records are used for reverse name resolution. The reverse records are important because Red Hat Enterprise Linux CoreOS (RHCOS) uses the reverse records to set the hostnames for all the nodes, unless the hostnames are provided by DHCP. Additionally, the reverse records are used to generate the certificate signing requests (CSR) that OpenShift Container Platform needs to operate.

Note

It is recommended to use a DHCP server to provide the hostnames to each cluster node.

The following DNS records are required for an OpenShift Container Platform cluster using the platform `none` option and they must be in place before installation. In each record, `<cluster_name>` is the cluster name and `<base_domain>` is the base domain that you specify in the `install-config.yaml` file. A complete DNS record takes the form: `<component>.<cluster_name>.<base_domain>.`.

Expand

Table 1.5. Required DNS records

| Component | Record | Description |
| --- | --- | --- |
| Kubernetes API | `api.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to identify the API load balancer. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster. |
| `api-int.<cluster_name>.<base_domain>.` | A DNS A/AAAA or CNAME record, and a DNS PTR record, to internally identify the API load balancer. These records must be resolvable from all the nodes within the cluster.  Important  The API server must be able to resolve the worker nodes by the hostnames that are recorded in Kubernetes. If the API server cannot resolve the node names, then proxied API calls can fail, and you cannot retrieve logs from pods. |
| Routes | `*.apps.<cluster_name>.<base_domain>.` | A wildcard DNS A/AAAA or CNAME record that refers to the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default. These records must be resolvable by both clients external to the cluster and from all the nodes within the cluster.  For example, `console-openshift-console.apps.<cluster_name>.<base_domain>` is used as a wildcard route to the OpenShift Container Platform console. |
| Control plane machines | `<master><n>.<cluster_name>.<base_domain>.` | DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the control plane nodes. These records must be resolvable by the nodes within the cluster. |
| Compute machines | `<worker><n>.<cluster_name>.<base_domain>.` | DNS A/AAAA or CNAME records and DNS PTR records to identify each machine for the worker nodes. These records must be resolvable by the nodes within the cluster. |

Show more

Note

In OpenShift Container Platform 4.4 and later, you do not need to specify etcd host and SRV records in your DNS configuration.

Tip

You can use the `dig` command to verify name and reverse name resolution.

##### [1.6.1.1. Example DNS configuration for platform "none" clusters](#agent-install-dns-none-example_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

This section provides A and PTR record configuration samples that meet the DNS requirements for deploying OpenShift Container Platform using the platform `none` option. The samples are not meant to provide advice for choosing one DNS solution over another.

In the examples, the cluster name is `ocp4` and the base domain is `example.com`.

Example DNS A record configuration for a platform "none" cluster
:   The following example is a BIND zone file that shows sample A records for name resolution in a cluster using the platform `none` option.

**Sample DNS zone database**

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
master0.ocp4.example.com.	IN	A	192.168.1.97
master1.ocp4.example.com.	IN	A	192.168.1.98
master2.ocp4.example.com.	IN	A	192.168.1.99
;
worker0.ocp4.example.com.	IN	A	192.168.1.11
worker1.ocp4.example.com.	IN	A	192.168.1.7
;
;EOF
```

where:

`api.ocp4.example.com.`
:   Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer.

`api-int.ocp4.example.com.`
:   Provides name resolution for the Kubernetes API. The record refers to the IP address of the API load balancer and is used for internal cluster communications.

`*.apps.ocp4.example.com.`
:   Provides name resolution for the wildcard routes. The record refers to the IP address of the application ingress load balancer. The application ingress load balancer targets the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.

    Note

    In the example, the same load balancer is used for the Kubernetes API and application ingress traffic. In production scenarios, you can deploy the API and application ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

`master0.ocp4.example.com.`-`master2.ocp4.example.com.`
:   Provides name resolution for the control plane machines.

`worker0.ocp4.example.com.`-`worker1.ocp4.example.com.`
:   Provides name resolution for the compute machines.

Example DNS PTR record configuration for a platform "none" cluster
:   The following example BIND zone file shows sample PTR records for reverse name resolution in a cluster using the platform `none` option.

**Sample DNS zone database for reverse records**

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
97.1.168.192.in-addr.arpa.	IN	PTR	master0.ocp4.example.com.
98.1.168.192.in-addr.arpa.	IN	PTR	master1.ocp4.example.com.
99.1.168.192.in-addr.arpa.	IN	PTR	master2.ocp4.example.com.
;
11.1.168.192.in-addr.arpa.	IN	PTR	worker0.ocp4.example.com.
7.1.168.192.in-addr.arpa.	IN	PTR	worker1.ocp4.example.com.
;
;EOF
```

where:

`api.ocp4.example.com.`
:   Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer.

`api-int.ocp4.example.com.`
:   Provides reverse DNS resolution for the Kubernetes API. The PTR record refers to the record name of the API load balancer and is used for internal cluster communications.

`master0.ocp4.example.com.`-`master2.ocp4.example.com.`
:   Provides reverse DNS resolution for the control plane machines.

`worker0.ocp4.example.com.`-`worker1.ocp4.example.com.`
:   Provides reverse DNS resolution for the compute machines.

Note

A PTR record is not required for the OpenShift Container Platform application wildcard.

#### [1.6.2. Platform "none" Load balancing requirements](#agent-install-load-balancing-none_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

Before you install OpenShift Container Platform, you must provision the API and application Ingress load balancing infrastructure. In production scenarios, you can deploy the API and application Ingress load balancers separately so that you can scale the load balancer infrastructure for each in isolation.

Note

* These requirements do not apply to single-node OpenShift clusters using the platform `none` option.
* If you want to deploy the API and application Ingress load balancers with a Red Hat Enterprise Linux (RHEL) instance, you must purchase the RHEL subscription separately.

The load balancing infrastructure must meet the following requirements:

1. **API load balancer**: Provides a common endpoint for users, both human and machine, to interact with and configure the platform. Configure the following conditions:

   * Layer 4 load balancing only. This can be referred to as Raw TCP, SSL Passthrough, or SSL Bridge mode. If you use SSL Bridge mode, you must enable Server Name Indication (SNI) for the API routes.
   * A stateless load balancing algorithm. The options vary based on the load balancer implementation.

   Important

   Do not configure session persistence for an API load balancer.

   Configure the following ports on both the front and back of the load balancers:

   Expand

   Table 1.6. API load balancer

   | Port | Back-end machines (pool members) | Internal | External | Description |
   | --- | --- | --- | --- | --- |
   | `6443` | Control plane. You must configure the `/readyz` endpoint for the API server health check probe. | X | X | Kubernetes API server |
   | `22623` | Control plane. | X |  | Machine config server |

   Show more

   Important

   The Agent-based Installer requires TCP port `8090` to be open between all hosts and the rendezvous host so that the hosts can access the Assisted Service API. Port `8090` is required only during the discovery and bootstrap phases. For more information, see "Port requirements for the rendezvous host".

   Note

   The load balancer must be configured to take a maximum of 30 seconds from the time the API server turns off the `/readyz` endpoint to the removal of the API server instance from the pool. Within the time frame after `/readyz` returns an error or becomes healthy, the endpoint must have been removed or added. Probing every 5 or 10 seconds, with two successful requests to become healthy and three to become unhealthy, are well-tested values.
2. **Application Ingress load balancer**: Provides an ingress point for application traffic flowing in from outside the cluster. A working configuration for the Ingress router is required for an OpenShift Container Platform cluster.

   Configure the following conditions:

   * Layer 4 load balancing only. This can be referred to as Raw TCP, SSL Passthrough, or SSL Bridge mode. If you use SSL Bridge mode, you must enable Server Name Indication (SNI) for the ingress routes.
   * A connection-based or session-based persistence is recommended, based on the options available and types of applications that will be hosted on the platform.

   Tip

   If the true IP address of the client can be seen by the application Ingress load balancer, enabling source IP-based session persistence can improve performance for applications that use end-to-end TLS encryption.

   Configure the following ports on both the front and back of the load balancers:

   Expand

   Table 1.7. Application Ingress load balancer

   | Port | Back-end machines (pool members) | Internal | External | Description |
   | --- | --- | --- | --- | --- |
   | `443` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTPS traffic |
   | `80` | The machines that run the Ingress Controller pods, compute, or worker, by default. | X | X | HTTP traffic |

   Show more

   Note

   If you are deploying a three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.

##### [1.6.2.1. Example load balancer configuration for platform "none" clusters](#agent-install-load-balancing-none-example_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

This section provides an example API and application Ingress load balancer configuration that meets the load balancing requirements for clusters using the platform `none` option. The sample is an `/etc/haproxy/haproxy.cfg` configuration for an HAProxy load balancer. The example is not meant to provide advice for choosing one load balancing solution over another.

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
  server master0 master0.ocp4.example.com:6443 check inter 1s
  server master1 master1.ocp4.example.com:6443 check inter 1s
  server master2 master2.ocp4.example.com:6443 check inter 1s
listen machine-config-server-22623
  bind *:22623
  mode tcp
  server master0 master0.ocp4.example.com:22623 check inter 1s
  server master1 master1.ocp4.example.com:22623 check inter 1s
  server master2 master2.ocp4.example.com:22623 check inter 1s
listen ingress-router-443
  bind *:443
  mode tcp
  balance source
  server worker0 worker0.ocp4.example.com:443 check inter 1s
  server worker1 worker1.ocp4.example.com:443 check inter 1s
listen ingress-router-80
  bind *:80
  mode tcp
  balance source
  server worker0 worker0.ocp4.example.com:80 check inter 1s
  server worker1 worker1.ocp4.example.com:80 check inter 1s
```

* Port `6443` handles the Kubernetes API traffic and points to the control plane machines. You must configure health checks on this port to ensure that the API server is available before routing traffic.
* Port `22623` handles the machine config server traffic and points to the control plane machines.
* Port `443` handles the HTTPS traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.
* Port `80` handles the HTTP traffic and points to the machines that run the Ingress Controller pods. The Ingress Controller pods run on the compute machines by default.

  Note

  If you are deploying a compact three-node cluster with zero compute nodes, the Ingress Controller pods run on the control plane nodes. In three-node cluster deployments, you must configure your application Ingress load balancer to route HTTP and HTTPS traffic to the control plane nodes.

Tip

If you are using HAProxy as a load balancer, you can check that the `haproxy` process is listening on ports `6443`, `22623`, `443`, and `80` by running `netstat -nltupe` on the HAProxy node.

### [1.7. About an arbiter node](#installing-ocp-agent-local-arbiter-node_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

You can configure an OpenShift Container Platform cluster with two control plane nodes and one arbiter node so as to retain high availability (HA) while reducing infrastructure costs for your cluster.

An arbiter node is a lower-cost, co-located machine that participates in control plane quorum decisions. Unlike a standard control plane node, the arbiter node does not run the full set of control plane services. You can use this configuration to maintain HA in your cluster with only two fully provisioned control plane nodes instead of three.

To deploy a cluster with two control plane nodes and one arbiter node, you must define the following nodes in the `install-config.yaml` file:

* 2 control plane nodes
* 1 arbiter node

The arbiter node must meet the following minimum system requirements:

* 2 vCPUs
* 8 GB of RAM
* 50 GB of SSD or equivalent storage
* The arbiter node must be located in a network environment with an end-to-end latency of less than 100 milliseconds, including disk I/O. In high-latency environments, you might need to apply the `etcd` slow profile.

The control plane nodes must meet the following minimum system requirements:

* 4 vCPUs
* 16 GB of RAM
* 120 GB of SSD or equivalent storage

Additionally, the control plane nodes must also have enough storage for the workload.

**Example `install-config.yaml` configuration for deploying an arbiter node**

```
apiVersion: v1
baseDomain: devcluster.openshift.com
compute:
  - architecture: amd64
    hyperthreading: Enabled
    name: worker
    platform: {}
    replicas: 0
arbiter:
  architecture: amd64
  hyperthreading: Enabled
  replicas: 1
  name: arbiter
  platform:
    baremetal: {}
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    baremetal: {}
  replicas: 2
platform:
  baremetal:
    hosts:
      - name: cluster-master-0
        role: master
# ...
      - name: cluster-master-1
        role: master
        ...
      - name: cluster-arbiter-0
        role: arbiter
# ...
```

where:

`arbiter`
:   Specifies the arbiter machine pool. You configure this field to deploy a cluster with an arbiter node.

`arbiter.replicas`
:   Specifies the `arbiter.replicas` parameter as `1` for the arbiter pool. You cannot set this field to a value that is greater than 1.

`arbiter.name`
:   Specifies a name for the arbiter machine pool.

`controlPlane`
:   Specifies the control plane machine pool.

`controlPlane.replicas`
:   Specifies the `controlPlane.replicas` parameter. When an arbiter pool is defined, two control plane replicas are valid.

### [1.8. Example: Bonds and VLAN interface node network configuration](#agent-install-sample-config-bonds-vlans_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

See example manifest files to better understand configuration options for deploying your cluster.

The following `agent-config.yaml` file is an example of a manifest for bond and VLAN interfaces:

```
  apiVersion: v1alpha1
  kind: AgentConfig
  rendezvousIP: 10.10.10.14
  hosts:
    - hostname: master0
      role: master
      interfaces:
       - name: enp0s4
         macAddress: 00:21:50:90:c0:10
       - name: enp0s5
         macAddress: 00:21:50:90:c0:20
      networkConfig:
        interfaces:
          - name: bond0.300
            type: vlan
            state: up
            vlan:
              base-iface: bond0
              id: 300
            ipv4:
              enabled: true
              address:
                - ip: 10.10.10.14
                  prefix-length: 24
              dhcp: false
          - name: bond0
            type: bond
            state: up
            mac-address: 00:21:50:90:c0:10
            ipv4:
              enabled: false
            ipv6:
              enabled: false
            link-aggregation:
              mode: active-backup
              options:
                miimon: "150"
              port:
               - enp0s4
               - enp0s5
        dns-resolver:
          config:
            server:
              - 10.10.10.11
              - 10.10.10.12
        routes:
          config:
            - destination: 0.0.0.0/0
              next-hop-address: 10.10.10.10
              next-hop-interface: bond0.300
              table-id: 254
```

where:

`networkConfig.interfaces.name`
:   Specifies the name of the interface.

    Note

    This value does not need to match the device name.

`networkConfig.interfaces.type`
:   Specifies the type of interface. Specifying `vlan` creates a VLAN and specifying `bond` creates a bond.

`link-aggregation.mode`
:   Specifies the bonding mode.

`link-aggregation.options.mode`
:   Specifies the MII link monitoring frequency in milliseconds. This example inspects the bond link every 150 milliseconds.

`dns-resolver`
:   Specifies the search and server settings for the DNS server. This configuration is optional.

`routes.config.next-hop-address`
:   Specifies the next hop address for the node traffic. This must be in the same subnet as the IP address set for the specified interface.

`routes.config.next-hop-interface`
:   Specifies the next hop interface for the node traffic.

### [1.9. Example: Bonds and SR-IOV dual-NIC node network configuration](#agent-install-sample-config-bond-sriov_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

See example manifest files to better understand configuration options for deploying your cluster.

The following `agent-config.yaml` file is an example of a manifest for dual port network interface controller (NIC) with a bond and SR-IOV interfaces:

```
apiVersion: v1alpha1
kind: AgentConfig
rendezvousIP: 10.10.10.14
hosts:
  - hostname: worker-1
    interfaces:
      - name: eno1
        macAddress: 0c:42:a1:55:f3:06
      - name: eno2
        macAddress: 0c:42:a1:55:f3:07
    networkConfig:
      interfaces:
        - name: eno1
          type: ethernet
          state: up
          mac-address: 0c:42:a1:55:f3:06
          ipv4:
            enabled: true
            dhcp: false
          ethernet:
            sr-iov:
              total-vfs: 2
          ipv6:
            enabled: false
        - name: sriov:eno1:0
          type: ethernet
          state: up
          ipv4:
            enabled: false
          ipv6:
            enabled: false
            dhcp: false
        - name: sriov:eno1:1
          type: ethernet
          state: down
        - name: eno2
          type: ethernet
          state: up
          mac-address: 0c:42:a1:55:f3:07
          ipv4:
            enabled: true
          ethernet:
            sr-iov:
              total-vfs: 2
          ipv6:
            enabled: false
        - name: sriov:eno2:0
          type: ethernet
          state: up
          ipv4:
            enabled: false
          ipv6:
            enabled: false
        - name: sriov:eno2:1
          type: ethernet
          state: down
        - name: bond0
          type: bond
          state: up
          min-tx-rate: 100
          max-tx-rate: 200
          link-aggregation:
            mode: active-backup
            options:
              primary: sriov:eno1:0
            port:
              - sriov:eno1:0
              - sriov:eno2:0
          ipv4:
            address:
              - ip: 10.19.16.57
                prefix-length: 23
            dhcp: false
            enabled: true
          ipv6:
            enabled: false
          dns-resolver:
            config:
              server:
              - 10.11.5.160
              - 10.2.70.215
          routes:
            config:
            - destination: 0.0.0.0/0
              next-hop-address: 10.19.17.254
              next-hop-interface: bond0
              table-id: 254
```

where:

`networkConfig`
:   Specifies information about the network configuration of the host, with subfields including `interfaces`,`dns-resolver`, and `routes`.

`networkConfig.interfaces`
:   Specifies an array of network interfaces defined for the host.

`networkConfig.interfaces.name`
:   Specifies the name of the interface.

    Note

    This value does not need to match the device name.

`networkConfig.interfaces.type`
:   Specifies the type of interface. This example creates an ethernet interface.

`networkConfig.interfaces.ipv4.dhcp`
:   Specifies DHCP enablement. Set this to `false` to disable DHCP for the physical function (PF) if it is not strictly required.

`ethernet.sr-iov.total-vfs`
:   Specifies the number of SR-IOV virtual functions (VFs) to instantiate.

`networkConfig.interfaces.state`
:   Specifies the value of `networkConfig.interfaces.state`. Set this parameter to `up`.

`networkConfig.interfaces.ipv4.enabled`
:   Specifies the enablement of IPv4 addressing for the VF attached to the bond. Set this to `false` to disable.

`networkConfig.interfaces.min-tx-rate`
:   Specifies a minimum transmission rate, in Mbps, for the VF. This sample value sets a rate of 100 Mbps. This value must be less than or equal to the maximum transmission rate.

    Note

    Intel NICs do not support the `min-tx-rate` parameter. For more information, see [**BZ#1772847**](https://bugzilla.redhat.com/show_bug.cgi?id=1772847).

`networkConfig.interfaces.max-tx-rate`
:   Specifies a maximum transmission rate, in Mbps, for the VF. This sample value sets a rate of 200 Mbps.

`link-aggregation.mode`
:   Specifies the needed bond mode.

`link-aggregation.options.primary`
:   Specifies the preferred port of the bonding interface. The primary device is the first of the bonding interfaces to be used and is not abandoned unless it fails. This setting is particularly useful when one NIC in the bonding interface is faster and, therefore, able to handle a bigger load. This setting is only valid when the bonding interface is in `active-backup` mode (mode 1).

`ipv4.address.ip`
:   Specifies a static IP address for the bond interface. This is the node IP address.

`routes.config.next-hop-interface`
:   Specifies `bond0` as the gateway for the default route.

### [1.10. Sample install-config.yaml file for bare metal](#installation-bare-metal-agent-installer-config-yaml_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters.

**Sample install-config.yaml file for bare metal**

```
apiVersion: v1
baseDomain: example.com
compute:
- name: worker
  replicas: 0
  architecture: amd64
controlPlane:
  name: master
  replicas: 1
  architecture: amd64
metadata:
  name: sno-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 192.168.0.0/16
  networkType: OVNKubernetes
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
:   Specifies a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, -.

`compute.replicas`
:   Specifies the number of compute machines that the Agent-based Installer waits to discover before triggering the installation process. It is the number of compute machines that must be booted with the generated ISO.

    Note

    If you are installing a three-node cluster, do not deploy any compute machines when you install the Red Hat Enterprise Linux CoreOS (RHCOS) machines.

`controlPlane`
:   Specifies a single mapping. To meet the requirements of the different data structures, the first line of the `controlPlane` section must not begin with a hyphen, -. Only one control plane pool is used.

`controlPlane.replicas`
:   Specifies the number of control plane machines that you add to the cluster. Because the cluster uses these values as the number of etcd endpoints in the cluster, the value must match the number of control plane machines that you deploy.

`metadata.name`
:   Specifies the cluster name that you specified in your DNS records.

`networking.clusterNetwork.cidr`
:   Specifies a block of IP addresses from which pod IP addresses are allocated. This block must not overlap with existing physical networks. These IP addresses are used for the pod network. If you need to access the pods from an external network, you must configure load balancers and routers to manage the traffic.

    Note

    Class E CIDR range is reserved for a future use. To use the Class E CIDR range, you must ensure your networking environment accepts the IP addresses within the Class E CIDR range.

`networking.clusterNetwork.hostPrefix`
:   Specifies the subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23`, then each node is assigned a `/23` subnet out of the given `cidr`, which allows for 510 (2^(32 - 23) - 2) pod IP addresses. If you are required to provide access to nodes from an external network, configure load balancers and routers to manage the traffic.

`networking.networkType`
:   Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

`networking.serviceNetwork`
:   Specifies the IP address pool to use for service IP addresses. You can enter only one IP address pool. This block must not overlap with existing physical networks. If you need to access the services from an external network, configure load balancers and routers to manage the traffic.

`platform.none`
:   Specifies platform `none`. You must set the platform to `none` for a single-node cluster. You can set the platform to `vsphere`, `baremetal`, or `none` for multi-node clusters.

    Note

    If you set the platform to `vsphere` or `baremetal`, you can configure IP address endpoints for cluster nodes in three ways:

    * IPv4
    * IPv6
    * IPv4 and IPv6 in parallel (dual-stack)

    **Example of dual-stack networking**

    ```
    networking:
      clusterNetwork:
        - cidr: 172.21.0.0/16
          hostPrefix: 23
        - cidr: fd02::/48
          hostPrefix: 64
      machineNetwork:
        - cidr: 192.168.11.0/16
        - cidr: 2001:DB8::/32
      serviceNetwork:
        - 172.22.0.0/16
        - fd03::/112
      networkType: OVNKubernetes
    platform:
      baremetal:
        apiVIPs:
        - 192.168.11.3
        - 2001:DB8::4
        ingressVIPs:
        - 192.168.11.4
        - 2001:DB8::5
    ```

`fips`
:   Specifies whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead.

    Important

    When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86\_64, ppc64le, and s390x architectures.

`pullSecret`
:   Specifies a pull secret that allows you to authenticate with the services that are provided by the included authorities, including Quay.io, which serves the container images for OpenShift Container Platform components.

`sshKey`
:   Specifies the SSH public key for the `core` user in Red Hat Enterprise Linux CoreOS (RHCOS).

    Note

    For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

### [1.11. Validation checks before agent ISO creation](#validations-before-agent-iso-creation_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

The Agent-based Installer performs validation checks on user defined YAML files before the ISO is created. Once the validations are successful, the agent ISO is created.

`install-config.yaml`
:   * `baremetal`, `vsphere` and `none` platforms are supported.
    * The `networkType` parameter must be `OVNKubernetes` in the case of `none` platform.
    * `apiVIPs` and `ingressVIPs` parameters must be set for bare metal and vSphere platforms.
    * Some host-specific fields in the bare metal platform configuration that have equivalents in `agent-config.yaml` file are ignored. A warning message is logged if these fields are set.

`agent-config.yaml`
:   * Each interface must have a defined MAC address. Additionally, all interfaces must have a different MAC address.
    * At least one interface must be defined for each host.
    * World Wide Name (WWN) vendor extensions are not supported in root device hints.
    * The `role` parameter in the `host` object must have a value of either `master` or `worker`.

Additional validation checks for Two-Node with Fencing (TNF)
:   * When the `controlPlane.replicas` parameter is set to `2`, you must provide exactly 2 fencing credentials.
    * Each fencing credential must include `hostName`, `address`, `username`, and `password`.
    * The `address` field must contain a Redfish URL, that is, the string must contain "redfish". IPMI addresses are explicitly rejected.
    * All `hostName` values must be unique.
    * If you specify `certificateVerification`, the value must be either `Enabled` or `Disabled`.
    * Fencing credentials are valid only with `baremetal`, `external`, or `none` platforms. Other platforms result in a validation error.

#### [1.11.1. Validation checks for ZTP manifests](#agent-validations-ztp_preparing-to-install-with-agent-based-installer) Copy linkLink copied to clipboard!

The following validation checks are performed when using ZTP manifests:

`agent-cluster-install.yaml`
:   * For IPv6, the only supported value for the `networkType` parameter is `OVNKubernetes`. The `OpenshiftSDN` value can be used only for IPv4.

`cluster-image-set.yaml`
:   * The `ReleaseImage` parameter must match the release defined in the installer.

Important

Zero Touch Provisioning (ZTP) is not supported for two-node clusters with fencing (TNF). Although you can use Red Hat Advanced Cluster Management (RHACM) for installations, the additional infrastructure components required for ZTP are not validated for this topology.

## [Chapter 2. Understanding disconnected installation mirroring](#understanding-disconnected-installation-mirroring) Copy linkLink copied to clipboard!

You can use a mirror registry for disconnected installations and to ensure that your clusters only use container images that satisfy your organization’s controls on external content.

Before you install a cluster on infrastructure that you provision in a disconnected environment, you must mirror the required container images into that environment. To mirror container images, you must have a registry for mirroring.

You can use one of the following procedures to mirror your OpenShift Container Platform image repository to your mirror registry:

* "Mirroring images for a disconnected installation by using the oc-mirror plugin v2"
* "Mirroring images for a disconnected installation"

### [2.1. About mirroring the OpenShift Container Platform image repository for a disconnected registry](#agent-install-about-mirroring-for-disconnected-registry_understanding-disconnected-installation-mirroring) Copy linkLink copied to clipboard!

To use mirror images for a disconnected installation with the Agent-based Installer, you must modify the `install-config.yaml` file.

You can mirror the release image by using the output of the `oc mirror` command.

Important

The `oc adm release mirror` command is deprecated as of OpenShift Container Platform 4.22 and will be removed in a future release.

As an alternative, use the oc-mirror plugin v2.

The following example shows the output of the `oc adm release mirror` command.

```
$ oc adm release mirror
```

**Example output**

```
To use the new mirrored repository to install, add the following
section to the install-config.yaml:

imageContentSources:

mirrors:
virthost.ostest.test.metalkube.org:5000/localimages/local-release-image
source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
mirrors:
virthost.ostest.test.metalkube.org:5000/localimages/local-release-image
source: registry.ci.openshift.org/ocp/release
```

The following example shows part of the `imageContentSourcePolicy.yaml` file generated by the oc-mirror plugin. The file can be found in the results directory, for example `oc-mirror-workspace/results-1682697932/`.

**Example `imageContentSourcePolicy.yaml` file**

```
spec:
  repositoryDigestMirrors:
  - mirrors:
    - virthost.ostest.test.metalkube.org:5000/openshift/release
    source: quay.io/openshift-release-dev/ocp-v4.0-art-dev
  - mirrors:
    - virthost.ostest.test.metalkube.org:5000/openshift/release-images
    source: quay.io/openshift-release-dev/ocp-release
```

#### [2.1.1. Configuring the Agent-based Installer to use mirrored images](#agent-install-configuring-for-disconnected-registry_understanding-disconnected-installation-mirroring) Copy linkLink copied to clipboard!

You must use the output of either the `oc adm release mirror` command or the oc-mirror plugin to configure the Agent-based Installer to use mirrored images.

**Procedure**

1. If you used the oc-mirror plugin to mirror your release images:

   1. Open the `imageContentSourcePolicy.yaml` located in the results directory, for example `oc-mirror-workspace/results-1682697932/`.
   2. Copy the text in the `repositoryDigestMirrors` section of the yaml file.
2. If you used the `oc adm release mirror` command to mirror your release images:

   * Copy the text in the `imageContentSources` section of the command output.
3. Paste the copied text into the `imageContentSources` field of the `install-config.yaml` file.
4. Add the certificate file used for the mirror registry to the `additionalTrustBundle` field of the yaml file.

   Important

   The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority, or the self-signed certificate that you generated for the mirror registry.

   **Example `install-config.yaml` file**

   ```
     additionalTrustBundle: |
       -----BEGIN CERTIFICATE-----
       ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
       -----END CERTIFICATE-----
   ```
5. If you are using GitOps ZTP manifests: add the `registries.conf` and `ca-bundle.crt` files to the `mirror` path to add the mirror configuration in the agent ISO image.

   Note

   You can create the `registries.conf` file from the output of either the `oc adm release mirror` command or the `oc mirror` plugin. The format of the `/etc/containers/registries.conf` file has changed. It is now version 2 and in TOML format.

   **Example `registries.conf` file**

   ```
   [[registry]]
   location = "registry.ci.openshift.org/ocp/release" mirror-by-digest-only = true

   [[registry.mirror]] location = "virthost.ostest.test.metalkube.org:5000/localimages/local-release-image"

   [[registry]]
   location = "quay.io/openshift-release-dev/ocp-v4.0-art-dev" mirror-by-digest-only = true

   [[registry.mirror]] location = "virthost.ostest.test.metalkube.org:5000/localimages/local-release-image"
   ```

## [Chapter 3. Installing a cluster](#installing-with-agent-basic) Copy linkLink copied to clipboard!

You can install a basic OpenShift Container Platform cluster using the Agent-based Installer.

The following procedures deploy a single-node OpenShift Container Platform in a disconnected environment. You can use these procedures as a basis and modify according to your requirements.

For procedures that include optional customizations you can make while using the Agent-based Installer, see "Installing a cluster with customizations".

### [3.1. Prerequisites for installing a cluster with the Agent-based Installer](#prerequisites_installing-with-agent-basic) Copy linkLink copied to clipboard!

Before beginning your cluster installation, you must complete prerequisite tasks that prepare your environment.

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update".
* You read "Selecting a cluster installation method and preparing it for users".
* If you use a firewall or proxy, you configured it to allow the sites that your cluster requires access to. For more information, see "Configuring your firewall".
* You configured your firewall to allow TCP traffic on port `8090` from all hosts to the rendezvous host so that hosts can reach the Assisted Service API during discovery and bootstrap. For more information, see "Port requirements for the rendezvous host".

### [3.2. Downloading the Agent-based Installer](#installing-ocp-agent-retrieve_installing-with-agent-basic) Copy linkLink copied to clipboard!

Begin the installation process by downloading the Agent-based Installer and the CLI needed for your installation.

**Procedure**

1. Log in to the Red Hat Hybrid Cloud Console using your login credentials.
2. Navigate to [Datacenter](https://console.redhat.com/openshift/create/datacenter).
3. Click **Run Agent-based Installer locally**.
4. Select the operating system and architecture for the **OpenShift Installer** and **Command line interface**.
5. Click **Download Installer** to download and extract the install program.
6. Download or copy the pull secret by clicking on **Download pull secret** or **Copy pull secret**.
7. Click **Download command-line tools** and place the `openshift-install` binary in a directory that is on your `PATH`.

### [3.3. Creating the configuration inputs](#installing-ocp-agent-basic-inputs_installing-with-agent-basic) Copy linkLink copied to clipboard!

Create the configuration files that are used by the installation program to generate the agent image.

**Procedure**

1. Place the `openshift-install` binary in a directory that is on your PATH.
2. Create a directory to store the install configuration by running the following command:

   ```
   $ mkdir ~/<directory_name>
   ```
3. Create the `install-config.yaml` file by running the following command:

   ```
   $ cat << EOF > ./my-cluster/install-config.yaml
   apiVersion: v1
   baseDomain: test.example.com
   compute:
   - architecture: amd64
     hyperthreading: Enabled
     name: worker
     replicas: 0
   controlPlane:
     architecture: amd64
     hyperthreading: Enabled
     name: master
     replicas: 1
   metadata:
     name: sno-cluster
   networking:
     clusterNetwork:
     - cidr: fd01::/48
       hostPrefix: 64
     machineNetwork:
     - cidr: fd2e:6f44:5dd8:c956::/120
     networkType: OVNKubernetes
     serviceNetwork:
     - fd02::/112
   platform:
     none: {}
   pullSecret: '<pull_secret>'
   sshKey: '<ssh_pub_key>'
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
   EOF
   ```

   where:

   `compute.architecture`
   :   Specifies the system architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`.

       If you are using the release image with the `multi` payload, you can install the cluster on different architectures such as `arm64`, `amd64`, `s390x`, and `ppc64le`. Otherwise, you can install the cluster only on the `release architecture` displayed in the output of the `openshift-install version` command. For more information, see "Verifying the supported architecture for installing an Agent-based Installer cluster".

   `metadata.name`
   :   Specifies your cluster name. This value is required.

   `networking.networkingType`
   :   Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

   `platform`
   :   Specifies your platform.

       Note

       For bare metal platforms, host settings made in the platform section of the `install-config.yaml` file are used by default, unless they are overridden by configurations made in the `agent-config.yaml` file.

   `pullSecret`
   :   Specifies your pull secret.

   `sshKey`
   :   Specifies your SSH public key.

   `additionalTrustBundle`
   :   Specifies the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry. You must specify this parameter if you are using a disconnected mirror registry.

   `imageContentSources`
   :   Specifies the `imageContentSources` section according to the output of the command that you used to mirror the repository. You must specify this parameter if you are using a disconnected mirror registry.

       Important

       * When using the `oc adm release mirror` command, use the output from the `imageContentSources` section.
       * When using the `oc mirror` command, use the `repositoryDigestMirrors` section of the `ImageContentSourcePolicy` file that results from running the command.
       * The `ImageContentSourcePolicy` resource is deprecated.
4. Create the `agent-config.yaml` file by running the following command:

   ```
   $ cat > agent-config.yaml << EOF
   apiVersion: v1beta1
   kind: AgentConfig
   metadata:
     name: sno-cluster
   rendezvousIP: fd2e:6f44:5dd8:c956::50
   EOF
   ```

   where:

   `rendezvousIP`
   :   Specifies the IP address used to determine which node performs the bootstrapping process as well as running the `assisted-service` component. You must provide the rendezvous IP address when you do not specify at least one host IP address in the `networkConfig` parameter. If this address is not provided, one IP address is selected from the provided host `networkConfig` parameter.

### [3.4. Creating and booting the agent image](#installing-ocp-agent-boot_installing-with-agent-basic) Copy linkLink copied to clipboard!

After you have prepared the configuration inputs for your installation, create the ISO image and boot it on your machines.

**Prerequisites**

* If you plan to boot the agent image from a USB drive, you have installed the `syslinux` package.

**Procedure**

1. Create the agent image by running the following command:

   ```
   $ openshift-install --dir <install_directory> agent create image
   ```

   Note

   Red Hat Enterprise Linux CoreOS (RHCOS) supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability. Multipathing is enabled by default in the agent ISO image, with a default `/etc/multipath.conf` configuration.
2. If you plan to boot the ISO image from a USB drive, add a master boot record to the image by running the following command:

   ```
   $ isohybrid --uefi <agent_iso_image>
   ```

   **Example command**

   ```
   $ isohybrid --uefi agent.x86_64.iso
   ```
3. Boot the `agent.x86_64.iso`, `agent.aarch64.iso`, or `agent.s390x.iso` image on the bare-metal machines.

### [3.5. Verifying that the current installation host can pull release images](#installing-ocp-agent-tui_installing-with-agent-basic) Copy linkLink copied to clipboard!

After you boot the agent image and network services are made available to the host, the agent console application performs a pull check to verify that the current host can retrieve release images.

If the primary pull check passes, you can quit the application to continue with the installation. If the pull check fails, the application performs additional checks, as seen in the `Additional checks` section of the TUI, to help you troubleshoot the problem. A failure for any of the additional checks is not necessarily critical as long as the primary pull check succeeds.

If there are host network configuration issues that might cause an installation to fail, you can use the console application to make adjustments to your network configurations.

Important

If the agent console application detects host network configuration issues, the installation workflow will be halted until the user manually stops the console application and signals the intention to proceed.

**Procedure**

1. Wait for the agent console application to check whether or not the configured release image can be pulled from a registry.
2. If the agent console application states that the installer connectivity checks have passed, wait for the prompt to time out to continue with the installation.

   Note

   You can still choose to view or change network configuration settings even if the connectivity checks have passed.

   However, if you choose to interact with the agent console application rather than letting it time out, you must manually quit the TUI to proceed with the installation.
3. If the agent console application checks have failed, which is indicated by a red icon beside the `Release image URL` pull check, use the following steps to reconfigure the host’s network settings:

   1. Read the `Check Errors` section of the TUI. This section displays error messages specific to the failed checks.
   2. Select **Configure network** to launch the NetworkManager TUI.
   3. Select **Edit a connection** and select the connection you want to reconfigure.
   4. Edit the configuration and select **OK** to save your changes.
   5. Select **Back** to return to the main screen of the NetworkManager TUI.
   6. Select **Activate a Connection**.
   7. Select the reconfigured network to deactivate it.
   8. Select the reconfigured network again to reactivate it.
   9. Select **Back** and then select **Quit** to return to the agent console application.
   10. Wait at least five seconds for the continuous network checks to restart using the new network configuration.
   11. If the `Release image URL` pull check succeeds and displays a green icon beside the URL, select **Quit** to exit the agent console application and continue with the installation.

### [3.6. Tracking and verifying installation progress](#installing-ocp-agent-verify_installing-with-agent-basic) Copy linkLink copied to clipboard!

After the installation has started, you can track installation progress and verify a successful installation.

**Prerequisites**

* You have configured a DNS record for the Kubernetes API server.

**Procedure**

1. Optional: To know when the bootstrap host (rendezvous host) reboots, run the following command:

   ```
   $ ./openshift-install --dir <install_directory> agent wait-for bootstrap-complete \
       --log-level=info
   ```

   where:

   `--dir`
   :   specifies the path to the directory where the agent ISO was generated.

   `--log-level`
   :   Specifies the level of installation details. Valid values are `info`, `warn`, `debug`, and `error`.

   **Example output**

   ```
   ...................................................................
   ...................................................................
   INFO Bootstrap configMap status is complete
   INFO cluster bootstrap is complete
   ```

   The command succeeds when the Kubernetes API server signals that it has been bootstrapped on the control plane machines.
2. Track the progress and verify successful installation by running the following command:

   ```
   $ openshift-install --dir <install_directory> agent wait-for install-complete
   ```

   1

   Replace `<install_directory>` with the path to the directory where the agent ISO was generated.

   **Example output**

   ```
   ...................................................................
   ...................................................................
   INFO Cluster is installed
   INFO Install complete!
   INFO To access the cluster as the system:admin user when using 'oc', run
   INFO     export KUBECONFIG=/home/core/installer/auth/kubeconfig
   INFO Access the OpenShift web-console here: https://console-openshift-console.apps.sno-cluster.test.example.com
   ```

### [3.7. Gathering log data from a failed Agent-based installation](#installing-ocp-agent-gather-log_installing-with-agent-basic) Copy linkLink copied to clipboard!

If you encounter a failed Agent-based installation, you can gather log data to provide for a support case.

**Prerequisites**

* You have configured a DNS record for the Kubernetes API server.

**Procedure**

1. Run the following command and collect the output:

   ```
   $ ./openshift-install --dir <installation_directory> agent wait-for bootstrap-complete --log-level=debug
   ```

   **Example error message**

   ```
   ...
   ERROR Bootstrap failed to complete: : bootstrap process timed out: context deadline exceeded
   ```
2. If the output from the previous command indicates a failure, or if the bootstrap is not progressing, run the following command to connect to the rendezvous host and collect the output:

   ```
   $ ssh core@<node-ip> agent-gather -O >agent-gather.tar.xz
   ```

   Note

   Red Hat Support can diagnose most issues using the data gathered from the rendezvous host, but if some hosts are not able to register, gathering this data from every host might be helpful.
3. If the bootstrap completes and the cluster nodes reboot, run the following command and collect the output:

   ```
   $ ./openshift-install --dir <install_directory> agent wait-for install-complete --log-level=debug
   ```
4. If the output from the previous command indicates a failure, perform the following steps:

   1. Export the `kubeconfig` file to your environment by running the following command:

      ```
      $ export KUBECONFIG=<install_directory>/auth/kubeconfig
      ```
   2. Gather information for debugging by running the following command:

      ```
      $ oc adm must-gather
      ```
   3. Create a compressed file from the `must-gather` directory that was just created in your working directory by running the following command:

      ```
      $ tar cvaf must-gather.tar.gz <must_gather_directory>
      ```
5. Excluding the `/auth` subdirectory, attach the installation directory used during the deployment to your support case on the [Red Hat Customer Portal](https://access.redhat.com).
6. Attach all other data gathered from this procedure to your support case.

## [Chapter 4. Installing a cluster with customizations](#installing-with-agent-based-installer) Copy linkLink copied to clipboard!

You can install an OpenShift Container Platform cluster using the Agent-based Installer, with customizations to meet your deployment needs.

The following procedures deploy a single-node OpenShift Container Platform cluster in a disconnected environment. You can use these procedures as a basis and modify according to your requirements.

### [4.1. Prerequisites for installing a cluster with the Agent-based Installer](#prerequisites_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

Before beginning your cluster installation, you must complete prerequisite tasks that prepare your environment.

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update".
* You read "Selecting a cluster installation method and preparing it for users".
* If you use a firewall or proxy, you configured it to allow the sites that your cluster requires access to. For more information, see "Configuring your firewall".
* You configured your firewall to allow TCP traffic on port `8090` from all hosts to the rendezvous host so that hosts can reach the Assisted Service API during discovery and bootstrap. For more information, see "Port requirements for the rendezvous host".

### [4.2. Downloading the Agent-based Installer](#installing-ocp-agent-retrieve_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

Begin the installation process by downloading the Agent-based Installer and the CLI needed for your installation.

**Procedure**

1. Log in to the Red Hat Hybrid Cloud Console using your login credentials.
2. Navigate to [Datacenter](https://console.redhat.com/openshift/create/datacenter).
3. Click **Run Agent-based Installer locally**.
4. Select the operating system and architecture for the **OpenShift Installer** and **Command line interface**.
5. Click **Download Installer** to download and extract the install program.
6. Download or copy the pull secret by clicking on **Download pull secret** or **Copy pull secret**.
7. Click **Download command-line tools** and place the `openshift-install` binary in a directory that is on your `PATH`.

### [4.3. Verifying the supported architecture for an Agent-based installation](#agent-install-verifying-architectures_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

Before installing an OpenShift Container Platform cluster using the Agent-based Installer, you can optionally verify the supported architecture on which you can install the cluster.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You have downloaded the installation program.

**Procedure**

1. Log in to the OpenShift CLI (`oc`).
2. Check your release payload by running the following command:

   ```
   $ ./openshift-install version
   ```

   **Example output**

   ```
   ./openshift-install 4.22.0
   built from commit abc123def456
   release image quay.io/openshift-release-dev/ocp-release@sha256:123abc456def789ghi012jkl345mno678pqr901stu234vwx567yz0
   release architecture amd64
   ```

   If you are using the release image with the `multi` payload, the `release architecture` displayed in the output of this command is the default architecture.
3. To check the architecture of the payload, run the following command:

   ```
   $ oc adm release info <release_image> -o jsonpath="{ .metadata.metadata}"
   ```

   Replace `<release_image>` with the release image. For example: `quay.io/openshift-release-dev/ocp-release@sha256:123abc456def789ghi012jkl345mno678pqr901stu234vwx567yz0`.

   **Example output when the release image uses the `multi` payload**

   ```
   {"release.openshift.io architecture":"multi"}
   ```

   If you are using the release image with the `multi` payload, you can install the cluster on different architectures such as `arm64`, `amd64`, `s390x`, and `ppc64le`. Otherwise, you can install the cluster only on the `release architecture` displayed in the output of the `openshift-install version` command.

### [4.4. Creating the preferred configuration inputs](#installing-ocp-agent-inputs_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

Create the preferred configuration inputs used to create the agent image.

Note

Configuring the `install-config.yaml` and `agent-config.yaml` files is the preferred method for using the Agent-based Installer. Using GitOps ZTP manifests is optional.

**Procedure**

1. Install the `nmstate` dependency by running the following command:

   ```
   $ sudo dnf install /usr/bin/nmstatectl -y
   ```
2. Place the `openshift-install` binary in a directory that is on your PATH.
3. Create a directory to store the install configuration by running the following command:

   ```
   $ mkdir ~/<directory_name>
   ```
4. Create the `install-config.yaml` file by running the following command:

   ```
   $ cat << EOF > ./<directory_name>/install-config.yaml
   apiVersion: v1
   baseDomain: test.example.com
   compute:
   - architecture: amd64
     hyperthreading: Enabled
     name: worker
     replicas: 0
   controlPlane:
     architecture: amd64
     hyperthreading: Enabled
     name: master
     replicas: 1
   metadata:
     name: sno-cluster
   networking:
     clusterNetwork:
     - cidr: 10.128.0.0/14
       hostPrefix: 23
     machineNetwork:
     - cidr: 192.168.0.0/16
     networkType: OVNKubernetes
     serviceNetwork:
     - 172.30.0.0/16
   platform:
     none: {}
   pullSecret: '<pull_secret>'
   sshKey: '<ssh_pub_key>'
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
   EOF
   ```

   where:

   `compute.architecture`
   :   Specifies the system architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`.

       If you are using the release image with the `multi` payload, you can install the cluster on different architectures such as `arm64`, `amd64`, `s390x`, and `ppc64le`. Otherwise, you can install the cluster only on the `release architecture` displayed in the output of the `openshift-install version` command. For more information, see "Verifying the supported architecture for installing an Agent-based Installer cluster".

   `metadata.name`
   :   Specifies your cluster name. This value is required.

   `networking.networkingType`
   :   Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

   `platform`
   :   Specifies your platform. If you set the platform to `vSphere`, `baremetal`, or `none`, you can configure IP address endpoints for cluster nodes in three ways: IPv4, IPv6, or IPv4 and IPv6 in parallel (dual-stack).

       **Example of dual-stack networking**

       ```
       networking:
         clusterNetwork:
           - cidr: 172.21.0.0/16
             hostPrefix: 23
           - cidr: fd02::/48
             hostPrefix: 64
         machineNetwork:
           - cidr: 192.168.11.0/16
           - cidr: 2001:DB8::/32
         serviceNetwork:
           - 172.22.0.0/16
           - fd03::/112
         networkType: OVNKubernetes
       platform:
         baremetal:
           apiVIPs:
           - 192.168.11.3
           - 2001:DB8::4
           ingressVIPs:
           - 192.168.11.4
           - 2001:DB8::5
       ```

       Note

       For bare-metal platforms, host settings made in the platform section of the `install-config.yaml` file are used by default, unless they are overridden by configurations made in the `agent-config.yaml` file.

   `pullSecret`
   :   Specifies your pull secret.

   `sshKey`
   :   Specifies your SSH public key.

   `additionalTrustBundle`
   :   Specifies the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry. You must specify this parameter if you are using a disconnected mirror registry.

   `imageContentSources`
   :   Specifies the `imageContentSources` section according to the output of the command that you used to mirror the repository. You must specify this parameter if you are using a disconnected mirror registry.

       Important

       * When using the `oc adm release mirror` command, use the output from the `imageContentSources` section.
       * When using the `oc mirror` command, use the `repositoryDigestMirrors` section of the `ImageContentSourcePolicy` file that results from running the command.
       * The `ImageContentSourcePolicy` resource is deprecated.
5. Create the `agent-config.yaml` file by running the following command:

   ```
   $ cat > agent-config.yaml << EOF
   apiVersion: v1beta1
   kind: AgentConfig
   metadata:
     name: sno-cluster
   rendezvousIP: 192.168.111.80
   hosts:
     - hostname: master-0
       interfaces:
         - name: eno1
           macAddress: 00:ef:44:21:e6:a5
       rootDeviceHints:
         deviceName: /dev/sdb
       networkConfig:
         interfaces:
           - name: eno1
             type: ethernet
             state: up
             mac-address: 00:ef:44:21:e6:a5
             ipv4:
               enabled: true
               address:
                 - ip: 192.168.111.80
                   prefix-length: 23
               dhcp: false
         dns-resolver:
           config:
             server:
               - 192.168.111.1
         routes:
           config:
             - destination: 0.0.0.0/0
               next-hop-address: 192.168.111.2
               next-hop-interface: eno1
               table-id: 254
   EOF
   ```

   where:

   `rendezvousIP`
   :   Specifies the IP address used to determine which node performs the bootstrapping process as well as running the `assisted-service` component. You must provide the rendezvous IP address when you do not specify at least one host’s IP address in the `networkConfig` parameter. If this address is not provided, one IP address is selected from the provided hosts' `networkConfig`.

   `hosts`
   :   Specifies host configuration. The number of hosts defined must not exceed the total number of hosts defined in the `install-config.yaml` file, which is the sum of the values of the `compute.replicas` and `controlPlane.replicas` parameters. This configuration is optional.

   `hosts.hostname`
   :   Specifies a value that overrides the hostname obtained from either the Dynamic Host Configuration Protocol (DHCP) or a reverse DNS lookup. Each host must have a unique hostname supplied by one of these methods. This configuration is optional.

   `hosts.rootDeviceHints`
   :   Specifies a configuration that enables provisioning of the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device. The installation program examines the devices in the order it discovers them, and compares the discovered values with the hint values. It uses the first discovered device that matches the hint value.

       Note

       This parameter is mandatory for FCP multipath configurations on IBM Z.

   `hosts.networkConfig`
   :   Specifies the network interface configuration of a host in NMState format. This configuration is optional.

### [4.5. Creating additional manifest files](#installing-ocp-agent-opt-manifests_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

As an optional task, you can create additional manifests to further configure your cluster beyond the configurations available in the `install-config.yaml` and `agent-config.yaml` files.

Important

Customizations to the cluster made by additional manifests are not validated, are not guaranteed to work, and might result in a nonfunctional cluster.

#### [4.5.1. Creating a directory to contain additional manifests](#installing-ocp-agent-manifest-folder_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

If you create additional manifests to configure your Agent-based installation beyond the `install-config.yaml` and `agent-config.yaml` files, you must create an `openshift` subdirectory within your installation directory. All of your additional machine configurations must be located within this subdirectory.

Note

The most common type of additional manifest you can add is a `MachineConfig` object. For examples of `MachineConfig` objects you can add during the Agent-based installation, see "Using MachineConfig objects to configure nodes" in the "Additional resources" section.

**Procedure**

* On your installation host, create an `openshift` subdirectory within the installation directory by running the following command:

  ```
  $ mkdir <installation_directory>/openshift
  ```

#### [4.5.2. Creating a manifest object that includes a customized br-ex bridge](#creating-manifest-file-customized-br-ex-bridge_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

By default, OpenShift Container Platform automatically configures the Open vSwitch (OVS) `br-ex` bridge on nodes. For advanced networking requirements, you can override this default behavior on bare-metal platforms. To do this, use the Agent-based Installer to create a `MachineConfig` object that includes an NMState configuration file.

Important

Customizations to the cluster made by additional manifests are not validated and not guaranteed to work. These manifests might result in a nonfunctional cluster.

For more information about an additional manifest file, see "Creating a directory to contain additional manifests".

Consider using the customized `br-ex` bridge configuration for any of the following tasks:

* You need to modify the `br-ex` bridge after you installed the cluster.
* You need to modify the maximum transmission unit (MTU) for your cluster.
* You need to update DNS values.
* You need to modify attributes for a different bond interface. Examples include MIImon (Media Independent Interface Monitor), bonding mode or Quality of Service (QoS).
* You need to enable Link Layer Discovery Protocol (LLDP) to discover and troubleshoot switch connectivity.

Note

Use the default OVS `br-ex` bridge for standard environments.

Use the default OVS `br-ex` bridge mechanism for single network interface controller (NIC) environments with default network settings.

After you install Red Hat Enterprise Linux CoreOS (RHCOS) and the system reboots, the Machine Config Operator injects Ignition configuration files into each node. This operation ensures that each node receives the `br-ex` bridge network configuration. To prevent configuration conflicts, the default OVS `br-ex` bridge mechanism is disabled.

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

**Prerequisites**

* Optional: You have installed the [`nmstatectl`](https://nmstate.io/user/quick_guide.html) CLI tool to validate your NMState configuration.
* You checked that an `openshift` subdirectory exists in your installation directory. If the subdirectory does not exist, create the subdirectory.

**Procedure**

1. Create an NMState configuration file and define a customized `br-ex` bridge network configuration in the file:

   **Example of an NMState configuration for a customized `br-ex` bridge network**

   ```
   interfaces:
   - name: enp2s0
     type: ethernet
     state: up
     mtu: 9000
     ipv4:
       enabled: false
     ipv6:
       enabled: false
   - name: br-ex
     type: ovs-bridge
     state: up
     ipv4:
       enabled: false
       dhcp: false
     ipv6:
       enabled: false
       dhcp: false
     bridge:
       options:
         mcast-snooping-enable: true
       port:
       - name: enp2s0
       - name: br-ex
   - name: br-ex
     type: ovs-interface
     state: up
     copy-mac-from: enp2s0
     mtu: 9000
     ipv4:
       enabled: true
       dhcp: true
       auto-route-metric: 48
     ipv6:
       enabled: true
       dhcp: true
       auto-route-metric: 48
   # ...
   ```

   where:

   `interfaces.name`
   :   Specifies the name of the interface.

   `interfaces.type`
   :   Specifies the type of ethernet.

   `interfaces.state`
   :   Specifies the requested state for the interface after creation.

   `mtu`
   :   To ensure network stability and performance, you must explicitly declare the MTU in the manifest for every interface. Do not rely on automatic MTU configuration. The MTU configured on a bridge port or VLAN-tagged interface must not exceed the maximum frame size supported by the attached physical medium. A mismatch causes packet fragmentation or connectivity loss.

   `ipv4.enabled`
   :   Disables IPv4 and IPv6 in this example.

   `port.name`
   :   Specifies the node NIC to which the bridge attaches.

   `auto-route-metric`
   :   Sets the parameter to `48` to ensure the `br-ex` default route always has the highest precedence (lowest metric). This configuration prevents routing conflicts with any other interfaces that are automatically configured by the `NetworkManager` service.
2. Use the `cat` command to base64-encode the contents of the NMState configuration:

   ```
   $ cat <nmstate_configuration>.yml | base64
   ```

   where:

   `<nmstate_configuration>`
   :   Replace `<nmstate_configuration>` with the name of your NMState resource YAML file.
3. Create a `MachineConfig` file as an additional manifest file. Define a customized `br-ex` bridge network configuration analogous to the following example in the file. The Agent-based Installer automatically applies the updates from the `MachineConfig` object to your cluster.

   ```
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfig
   metadata:
     labels:
       machineconfiguration.openshift.io/role: worker
     name: 10-br-ex-worker
   spec:
     config:
       ignition:
         version: 3.2.0
       storage:
         files:
         - contents:
             source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
           mode: 0644
           overwrite: true
           path: /etc/nmstate/openshift/worker-0.yml
         - contents:
             source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
           mode: 0644
           overwrite: true
           path: /etc/nmstate/openshift/worker-1.yml
   # ...
   ```

   where:

   `metadata.name`
   :   Specifies the name of the policy.

   `contents.source`
   :   Writes the encoded base64 information to the specified path.

   `path`
   :   For each node in your cluster, specify the hostname path to your node and the base-64 encoded Ignition configuration file data for the machine type. The `worker` role is the default role for nodes in your cluster. You must use the `.yml` extension for configuration files. For example, use `$(hostname -s).yml` when specifying the short hostname path for each node or all nodes in the `MachineConfig` manifest file.

       You can apply a single global configuration to all nodes in your cluster by using the `/etc/nmstate/openshift/cluster.yml` configuration file. In this case, you do not need to specify the short hostname path for each node, such as `/etc/nmstate/openshift/<node_hostname>.yml`. For example:

       **Example /etc/nmstate/openshift/cluster.yml configuration file**

       ```
       # ...
             - contents:
                 source: data:text/plain;charset=utf-8;base64,<base64_encoded_nmstate_configuration>
               mode: 0644
               overwrite: true
               path: /etc/nmstate/openshift/cluster.yml
       # ...
       ```
4. Save the additional manifest file in the `openshift` subdirectory of your installation directory.

   On completing other configuration inputs for your installation, such as encrypting the disk, you create the ISO image. After booting this image, the customized `br-ex` bridge configuration applies to each node in your cluster.

#### [4.5.3. Creating disk partitions](#installation-user-infra-machines-advanced-disk_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

In general, you must use the default disk partitioning that is created during the RHCOS installation. However, there are cases where you might want to create a separate partition for a directory that you expect to grow.

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` directory or a subdirectory of `/var`. For example:

* `/var/lib/containers`: Holds container-related content that can grow as more images and containers are added to a system.
* `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage.
* `/var`: Holds data that you might want to keep separate for purposes such as auditing.

  Important

  For disk sizes larger than 100GB, and especially larger than 1TB, create a separate `/var` partition.

Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date to keep that data intact. This method eliminates the need to re-pull containers or copy large log files during system updates.

The use of a separate partition for the `/var` directory or a subdirectory of `/var` also prevents data growth in the partitioned directory from filling up the root file system.

The following procedure sets up a separate `/var` partition by adding a machine config manifest that is wrapped into the Ignition config file for a node type during the preparation phase of an installation.

**Prerequisites**

* You have created an `openshift` subdirectory within your installation directory.

**Procedure**

1. Create a Butane config that configures the additional partition. For example, name the file `$HOME/clusterconfig/98-var-partition.bu`, change the disk device name to the name of the storage device on the `worker` systems, and set the storage size as appropriate. This example places the `/var` directory on a separate partition:

   ```
   variant: openshift
   version: 4.22.0
   metadata:
     labels:
       machineconfiguration.openshift.io/role: worker
     name: 98-var-partition
   storage:
     disks:
     - device: /dev/disk/by-id/<device_name>
       partitions:
       - label: var
         start_mib: <partition_start_offset>
         size_mib: <partition_size>
         number: 5
     filesystems:
       - device: /dev/disk/by-partlabel/var
         path: /var
         format: xfs
         mount_options: [defaults, prjquota]
         with_mount_unit: true
   ```

   where:

   `<device_name>`
   :   Specifies the storage device name of the disk that you want to partition.

   `<partition_start_offset>`
   :   Specifies the minimum offset value for the boot disk. For best performance, specify a minimum offset value of 25000 mebibytes. The root file system is automatically resized to fill all available space up to the specified offset. If no offset value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of RHCOS might overwrite the beginning of the data partition.

   `<partition_size>`
   :   Specifies the size of the data partition in mebibytes.

   `mount_options`
   :   The `prjquota` mount option must be enabled for filesystems used for container storage.

       Note

       When creating a separate `/var` partition, you cannot use different instance types for compute nodes, if the different instance types do not have the same device name.
2. Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command:

   ```
   $ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
   ```

#### [4.5.4. Using ZTP manifests](#installing-ocp-agent-ztp_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

As an optional task, you can use GitOps Zero Touch Provisioning (ZTP) manifests to configure your installation beyond the options available through the `install-config.yaml` and `agent-config.yaml` files.

See "Challenges of the network far edge" to learn more about GitOps Zero Touch Provisioning (ZTP).

Important

Zero Touch Provisioning (ZTP) is not supported for two-node clusters with fencing (TNF). Although you can use Red Hat Advanced Cluster Management (RHACM) for installations, the additional infrastructure components required for ZTP are not validated for this topology.

Note

GitOps ZTP manifests can be generated with or without configuring the `install-config.yaml` and `agent-config.yaml` files beforehand. If you chose to configure the `install-config.yaml` and `agent-config.yaml` files, the configurations will be imported to the ZTP cluster manifests when they are generated.

**Prerequisites**

* You have placed the `openshift-install` binary in a directory that is on your `PATH`.
* Optional: You have created and configured the `install-config.yaml` and `agent-config.yaml` files.

**Procedure**

1. Generate ZTP cluster manifests by running the following command:

   ```
   $ openshift-install agent create cluster-manifests --dir <installation_directory>
   ```

   Important

   If you have created the `install-config.yaml` and `agent-config.yaml` files, those files are deleted and replaced by the cluster manifests generated through this command.

   Any configurations made to the `install-config.yaml` and `agent-config.yaml` files are imported to the ZTP cluster manifests when you run the `openshift-install agent create cluster-manifests` command.
2. Navigate to the `cluster-manifests` directory by running the following command:

   ```
   $ cd <installation_directory>/cluster-manifests
   ```
3. Configure the manifest files in the `cluster-manifests` directory. For sample files, see the "Sample GitOps ZTP custom resources" section.
4. Disconnected clusters: If you did not define mirror configuration in the `install-config.yaml` file before generating the ZTP manifests, perform the following steps:

   1. Navigate to the `mirror` directory by running the following command:

      ```
      $ cd ../mirror
      ```
   2. Configure the manifest files in the `mirror` directory.

#### [4.5.5. Encrypting the disk](#installing-ocp-agent-encrypt_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

As an optional task, you can encrypt your disk or partition while installing OpenShift Container Platform with the Agent-based Installer.

Important

If there are leftover TPM encryption keys from a previous operating system on the bare-metal host, the cluster deployment can get stuck. To avoid this situation, it is highly recommended to reset the TPM chip in the BIOS before booting the ISO.

**Prerequisites**

* You have created and configured the `install-config.yaml` and `agent-config.yaml` files, unless you are using ZTP manifests.
* You have placed the `openshift-install` binary in a directory that is on your `PATH`.

**Procedure**

1. Generate ZTP cluster manifests by running the following command:

   ```
   $ openshift-install agent create cluster-manifests --dir <installation_directory>
   ```

   Important

   If you have created the `install-config.yaml` and `agent-config.yaml` files, those files are deleted and replaced by the cluster manifests generated through this command.

   Any configurations made to the `install-config.yaml` and `agent-config.yaml` files are imported to the ZTP cluster manifests when you run the `openshift-install agent create cluster-manifests` command.

   Note

   If you have already generated ZTP manifests, skip this step.
2. Navigate to the `cluster-manifests` directory by running the following command:

   ```
   $ cd <installation_directory>/cluster-manifests
   ```
3. Add the following section to the `agent-cluster-install.yaml` file:

   ```
   diskEncryption:
       enableOn: all
       mode: tang
       tangServers: "server1": "http://tang-server-1.example.com:7500"
   ```

   where:

   `diskEncryption.enableOn`
   :   Specifies which nodes to enable disk encryption on. Valid values are `none`, `all`, `masters`, and `workers`.

   `diskEncryption.mode`
   :   Specifies which disk encryption mode to use. Valid values are `tpmv2` and `tang`.

   `diskEncryption.tangServers`
   :   Specifies the Tang servers if you are using Tang. This value is optional.

#### [4.5.6. Configuring cluster network MTU at installation time](#installing-ocp-agent-cluster-network-mtu_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

You can explicitly set the cluster network maximum transmission unit (MTU) during installation by placing a `Network` custom resource (CR) as an additional manifest in the `openshift` directory of your Agent-based Installer configuration.

Setting the cluster network MTU with additional headroom during deployment prevents the need for a Day 2 MTU update that requires at least two rolling reboots of all cluster nodes.

During installation, the Cluster Network Operator (CNO) automatically calculates the cluster network MTU based on the primary network interface MTU. When you enable IPsec at installation time, the calculation includes both the OVN-Kubernetes overhead of 100 bytes and the IPsec overhead. If you plan to enable IPsec or another encapsulation technology as a Day 2 operation, the calculated MTU includes only the OVN-Kubernetes overhead and might be insufficient.

By explicitly setting the cluster network MTU at installation time, you can include additional headroom for those future needs and avoid a disruptive MTU migration.

Important

The cluster network MTU value must be lower than the machine network MTU by at least 100 bytes to account for OVN-Kubernetes overlay overhead. If you plan to enable IPsec as a Day 2 operation, allow an additional 46 bytes for IPsec headroom. For example, with a machine network MTU of `9100` bytes, set the cluster network MTU to `8900` bytes, which accounts for the following offset:

* OVN-Kubernetes overhead: 100 bytes
* IPsec headroom: 46 bytes
* Extra headroom: 54 bytes
* Total offset: 200 bytes

To avoid selecting an MTU value that a node cannot support, verify the maximum MTU (`maxmtu`) that the network interface accepts by running the `ip -d link` command.

**Prerequisites**

* You have created the `install-config.yaml` and `agent-config.yaml` files for your installation.
* You have created the `openshift` subdirectory within your installation directory as described in "Creating a directory to contain additional manifests".

**Procedure**

1. In your `agent-config.yaml` file, set the machine network MTU on the network interface for each host by using NMState configuration.

   The following example configures an Ethernet interface with MTU `9100`:

   ```
   apiVersion: v1beta1
   kind: AgentConfig
   metadata:
     name: sno-cluster
   rendezvousIP: 192.168.111.80
   hosts:
     - hostname: master-0
       interfaces:
         - name: eno1
           macAddress: 00:ef:44:21:e6:a5
       networkConfig:
         interfaces:
           - name: eno1
             type: ethernet
             state: up
             mtu: 9100
             ipv4:
               enabled: true
               dhcp: false
               address:
                 - ip: "192.168.111.80"
                   prefix-length: 24
   ```
2. Create a `Network` CR manifest file named `set-cluster-mtu.yaml` that sets the cluster network MTU:

   ```
   apiVersion: operator.openshift.io/v1
   kind: Network
   metadata:
     name: cluster
   spec:
     defaultNetwork:
       ovnKubernetesConfig:
         mtu: 8900
   ```

   where:

   `mtu`
   :   Specifies the cluster network MTU value. This value must be at least 100 bytes less than the machine network MTU. In this example, the value is 200 bytes less than the machine network MTU of 9100 to allow headroom for IPsec and other future requirements.
3. Place the `set-cluster-mtu.yaml` manifest file in the `openshift` subdirectory of your installation directory:

   ```
   <installation_directory>/
   ├── install-config.yaml
   ├── agent-config.yaml
   └── openshift/
       └── set-cluster-mtu.yaml
   ```

   Note

   Manifests in the `openshift` directory cannot override default cluster manifests. This restriction does not affect the `Network` CR for cluster network MTU because MTU configuration is not part of the default manifest set.
4. Create the agent image and boot your servers as described in "Creating and booting the agent image".

   During cluster installation, the installation program applies the `Network` CR as an additional manifest, and the CNO uses the specified MTU value instead of auto-calculating it.

**Verification**

* After the cluster installation is complete, verify the cluster network MTU by running the following command:

  ```
  $ oc get networks.operator.openshift.io cluster -o yaml
  ```

  **Example output**

  ```
  apiVersion: operator.openshift.io/v1
  kind: Network
  metadata:
    name: cluster
  # ...
  spec:
    # ...
    defaultNetwork:
      ovnKubernetesConfig:
        # ...
        mtu: 8900
  ```

### [4.6. Creating and booting the agent image](#installing-ocp-agent-boot_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

After you have prepared the configuration inputs for your installation, create the ISO image and boot it on your machines.

**Prerequisites**

* If you plan to boot the agent image from a USB drive, you have installed the `syslinux` package.

**Procedure**

1. Create the agent image by running the following command:

   ```
   $ openshift-install --dir <install_directory> agent create image
   ```

   Note

   Red Hat Enterprise Linux CoreOS (RHCOS) supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability. Multipathing is enabled by default in the agent ISO image, with a default `/etc/multipath.conf` configuration.
2. If you plan to boot the ISO image from a USB drive, add a master boot record to the image by running the following command:

   ```
   $ isohybrid --uefi <agent_iso_image>
   ```

   **Example command**

   ```
   $ isohybrid --uefi agent.x86_64.iso
   ```
3. Boot the `agent.x86_64.iso`, `agent.aarch64.iso`, or `agent.s390x.iso` image on the bare-metal machines.

### [4.7. Adding IBM Z agents with RHEL KVM](#installing-ocp-agent-ibm-z-kvm_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

You can manually add IBM Z® agents with RHEL KVM.

Only use this procedure for IBM Z® clusters with RHEL KVM.

Note

The `nmstateconfig` parameter must be configured for the KVM boot.

**Procedure**

1. Boot your RHEL KVM machine.
2. To deploy the virtual server, run the `virt-install` command with the following parameters:

   **ISO boot**

   ```
   $ virt-install
       --name <vm_name> \
       --autostart \
       --memory=<memory> \
       --cpu host \
       --vcpus=<vcpus> \
       --cdrom \<path_to_image>/<agent_iso_image> \
       --disk pool=default,size=<disk_pool_size> \
       --network network:default,mac=<mac_address> \
       --graphics none \
       --noautoconsole \
       --os-variant rhel9.0 \
       --wait=-1
   ```

   For the `--cdrom` parameter, specify the location of the ISO image on the local server, for example, `<path_to_image>/home/<image>.iso`.

   Note

   For KVM-based installations using DASD devices on IBM Z, a partition (for example, `/dev/dasdb1`) must be created using the `fdasd` partitioning tool.
3. Optional: Enable FIPS mode.

   To enable FIPS mode on IBM Z® clusters with RHEL KVM you must use PXE boot instead and run the `virt-install` command with the following parameters:

   **PXE boot**

   ```
   $ virt-install \
      --name <vm_name> \
      --autostart \
      --ram=16384 \
      --cpu host \
      --vcpus=8 \
      --location <path_to_kernel_initrd_image>,kernel=kernel.img,initrd=initrd.img \
      --disk <qcow_image_path> \
      --network network:macvtap ,mac=<mac_address> \
      --graphics none \
      --noautoconsole \
      --wait=-1 \
      --extra-args "rd.neednet=1 nameserver=<nameserver>" \
      --extra-args "ip=<IP>::<nameserver>::<hostname>:enc1:none" \
      --extra-args "coreos.live.rootfs_url=http://<http_server>:8080/agent.s390x-rootfs.img" \
      --extra-args "random.trust_cpu=on rd.luks.options=discard" \
      --extra-args "ignition.firstboot ignition.platform.id=metal" \
      --extra-args "console=tty1 console=ttyS1,115200n8" \
      --extra-args "coreos.inst.persistent-kargs=console=tty1 console=ttyS1,115200n8" \
      --extra-args "fips=1" \
      --osinfo detect=on,require=off
   ```

   where:

   `--location`
   :   Specifies the location of the kernel/initrd on the HTTP or HTTPS server.

   `--extra-args "fips=1"`
   :   Specifies the enablement of FIPS mode. This entry is required in addition to setting the `fips` parameter to `true` in the `install-config.yaml` file.

       Note

       * For KVM-based installations using DASD devices on IBM Z, a partition (for example, `/dev/dasdb1`) must be created using the `fdasd` partitioning tool.
       * Currently, only PXE boot is supported to enable FIPS mode on IBM Z®.

### [4.8. Verifying that the current installation host can pull release images](#installing-ocp-agent-tui_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

After you boot the agent image and network services are made available to the host, the agent console application performs a pull check to verify that the current host can retrieve release images.

If the primary pull check passes, you can quit the application to continue with the installation. If the pull check fails, the application performs additional checks, as seen in the `Additional checks` section of the TUI, to help you troubleshoot the problem. A failure for any of the additional checks is not necessarily critical as long as the primary pull check succeeds.

If there are host network configuration issues that might cause an installation to fail, you can use the console application to make adjustments to your network configurations.

Important

If the agent console application detects host network configuration issues, the installation workflow will be halted until the user manually stops the console application and signals the intention to proceed.

**Procedure**

1. Wait for the agent console application to check whether or not the configured release image can be pulled from a registry.
2. If the agent console application states that the installer connectivity checks have passed, wait for the prompt to time out to continue with the installation.

   Note

   You can still choose to view or change network configuration settings even if the connectivity checks have passed.

   However, if you choose to interact with the agent console application rather than letting it time out, you must manually quit the TUI to proceed with the installation.
3. If the agent console application checks have failed, which is indicated by a red icon beside the `Release image URL` pull check, use the following steps to reconfigure the host’s network settings:

   1. Read the `Check Errors` section of the TUI. This section displays error messages specific to the failed checks.
   2. Select **Configure network** to launch the NetworkManager TUI.
   3. Select **Edit a connection** and select the connection you want to reconfigure.
   4. Edit the configuration and select **OK** to save your changes.
   5. Select **Back** to return to the main screen of the NetworkManager TUI.
   6. Select **Activate a Connection**.
   7. Select the reconfigured network to deactivate it.
   8. Select the reconfigured network again to reactivate it.
   9. Select **Back** and then select **Quit** to return to the agent console application.
   10. Wait at least five seconds for the continuous network checks to restart using the new network configuration.
   11. If the `Release image URL` pull check succeeds and displays a green icon beside the URL, select **Quit** to exit the agent console application and continue with the installation.

### [4.9. Tracking and verifying installation progress](#installing-ocp-agent-verify_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

After the installation has started, you can track installation progress and verify a successful installation.

**Prerequisites**

* You have configured a DNS record for the Kubernetes API server.

**Procedure**

1. Optional: To know when the bootstrap host (rendezvous host) reboots, run the following command:

   ```
   $ ./openshift-install --dir <install_directory> agent wait-for bootstrap-complete \
       --log-level=info
   ```

   where:

   `--dir`
   :   specifies the path to the directory where the agent ISO was generated.

   `--log-level`
   :   Specifies the level of installation details. Valid values are `info`, `warn`, `debug`, and `error`.

   **Example output**

   ```
   ...................................................................
   ...................................................................
   INFO Bootstrap configMap status is complete
   INFO cluster bootstrap is complete
   ```

   The command succeeds when the Kubernetes API server signals that it has been bootstrapped on the control plane machines.
2. Track the progress and verify successful installation by running the following command:

   ```
   $ openshift-install --dir <install_directory> agent wait-for install-complete
   ```

   1

   Replace `<install_directory>` with the path to the directory where the agent ISO was generated.

   **Example output**

   ```
   ...................................................................
   ...................................................................
   INFO Cluster is installed
   INFO Install complete!
   INFO To access the cluster as the system:admin user when using 'oc', run
   INFO     export KUBECONFIG=/home/core/installer/auth/kubeconfig
   INFO Access the OpenShift web-console here: https://console-openshift-console.apps.sno-cluster.test.example.com
   ```

   Note

   If you are using the optional method of GitOps ZTP manifests, you can configure IP address endpoints for cluster nodes through the `AgentClusterInstall.yaml` file in three ways:

   * IPv4
   * IPv6
   * IPv4 and IPv6 in parallel (dual-stack)

   IPv6 is supported only on bare metal platforms.

   **Example of dual-stack networking**

   ```
   apiVIP: 192.168.11.3
   ingressVIP: 192.168.11.4
   clusterDeploymentRef:
     name: mycluster
   imageSetRef:
     name: openshift-4.22
   networking:
     clusterNetwork:
     - cidr: 172.21.0.0/16
       hostPrefix: 23
     - cidr: fd02::/48
       hostPrefix: 64
     machineNetwork:
     - cidr: 192.168.11.0/16
     - cidr: 2001:DB8::/32
     serviceNetwork:
     - 172.22.0.0/16
     - fd03::/112
     networkType: OVNKubernetes
   ```

### [4.10. Sample GitOps ZTP custom resources](#sample-ztp-custom-resources_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

You can optionally use GitOps Zero Touch Provisioning (ZTP) custom resource (CR) objects to install an OpenShift Container Platform cluster with the Agent-based Installer.

You can customize the following GitOps ZTP custom resources to specify more details about your OpenShift Container Platform cluster. The following sample GitOps ZTP custom resources are for a single-node cluster.

**Example `agent-cluster-install.yaml` file**

```
  apiVersion: extensions.hive.openshift.io/v1beta1
  kind: AgentClusterInstall
  metadata:
    name: test-agent-cluster-install
    namespace: cluster0
  spec:
    clusterDeploymentRef:
      name: ostest
    imageSetRef:
      name: openshift-4.22
    networking:
      clusterNetwork:
      - cidr: 10.128.0.0/14
        hostPrefix: 23
      serviceNetwork:
      - 172.30.0.0/16
    provisionRequirements:
      controlPlaneAgents: 1
      workerAgents: 0
    sshPublicKey: <ssh_public_key>
```

**Example `cluster-deployment.yaml` file**

```
apiVersion: hive.openshift.io/v1
kind: ClusterDeployment
metadata:
  name: ostest
  namespace: cluster0
spec:
  baseDomain: test.metalkube.org
  clusterInstallRef:
    group: extensions.hive.openshift.io
    kind: AgentClusterInstall
    name: test-agent-cluster-install
    version: v1beta1
  clusterName: ostest
  controlPlaneConfig:
    servingCertificates: {}
  platform:
    agentBareMetal: {}
  pullSecretRef:
    name: pull-secret
```

To declaratively bind specific bare-metal hosts to a cluster, use the `bmac.agent-install.openshift.io/cluster-reference` annotation on `BareMetalHost` resources.

**Example `cluster-image-set.yaml` file**

```
apiVersion: hive.openshift.io/v1
kind: ClusterImageSet
metadata:
  name: openshift-4.22
spec:
  releaseImage: registry.ci.openshift.org/ocp/release:4.22.0-0.nightly-2022-06-06-025509
```

**Example `infra-env.yaml` file**

```
apiVersion: agent-install.openshift.io/v1beta1
kind: InfraEnv
metadata:
  name: myinfraenv
  namespace: cluster0
spec:
  clusterRef:
    name: ostest
    namespace: cluster0
  cpuArchitecture: aarch64
  pullSecretRef:
    name: pull-secret
  sshAuthorizedKey: <ssh_public_key>
  nmStateConfigLabelSelector:
    matchLabels:
      cluster0-nmstate-label-name: cluster0-nmstate-label-value
```

The `clusterRef` field and its child fields (`name` and `namespace`) are optional. To enable the late-binding workflow, remove the `clusterRef` field and its child fields from the `InfraEnv` CR. Hosts are then bound to clusters individually by using the `bmac.agent-install.openshift.io/cluster-reference` annotation on `BareMetalHost` resources.

**Example `nmstateconfig.yaml` file**

```
apiVersion: agent-install.openshift.io/v1beta1
kind: NMStateConfig
metadata:
  name: master-0
  namespace: openshift-machine-api
  labels:
    cluster0-nmstate-label-name: cluster0-nmstate-label-value
spec:
  config:
    interfaces:
      - name: eth0
        type: ethernet
        state: up
        mac-address: 52:54:01:aa:aa:a1
        ipv4:
          enabled: true
          address:
            - ip: 192.168.122.2
              prefix-length: 23
          dhcp: false
    dns-resolver:
      config:
        server:
          - 192.168.122.1
    routes:
      config:
        - destination: 0.0.0.0/0
          next-hop-address: 192.168.122.1
          next-hop-interface: eth0
          table-id: 254
  interfaces:
    - name: "eth0"
      macAddress: 52:54:01:aa:aa:a1
```

**Example `pull-secret.yaml` file**

```
apiVersion: v1
kind: Secret
type: kubernetes.io/dockerconfigjson
metadata:
  name: pull-secret
  namespace: cluster0
stringData:
  .dockerconfigjson: <pull_secret>
```

### [4.11. Gathering log data from a failed Agent-based installation](#installing-ocp-agent-gather-log_installing-with-agent-based-installer) Copy linkLink copied to clipboard!

If you encounter a failed Agent-based installation, you can gather log data to provide for a support case.

**Prerequisites**

* You have configured a DNS record for the Kubernetes API server.

**Procedure**

1. Run the following command and collect the output:

   ```
   $ ./openshift-install --dir <installation_directory> agent wait-for bootstrap-complete --log-level=debug
   ```

   **Example error message**

   ```
   ...
   ERROR Bootstrap failed to complete: : bootstrap process timed out: context deadline exceeded
   ```
2. If the output from the previous command indicates a failure, or if the bootstrap is not progressing, run the following command to connect to the rendezvous host and collect the output:

   ```
   $ ssh core@<node-ip> agent-gather -O >agent-gather.tar.xz
   ```

   Note

   Red Hat Support can diagnose most issues using the data gathered from the rendezvous host, but if some hosts are not able to register, gathering this data from every host might be helpful.
3. If the bootstrap completes and the cluster nodes reboot, run the following command and collect the output:

   ```
   $ ./openshift-install --dir <install_directory> agent wait-for install-complete --log-level=debug
   ```
4. If the output from the previous command indicates a failure, perform the following steps:

   1. Export the `kubeconfig` file to your environment by running the following command:

      ```
      $ export KUBECONFIG=<install_directory>/auth/kubeconfig
      ```
   2. Gather information for debugging by running the following command:

      ```
      $ oc adm must-gather
      ```
   3. Create a compressed file from the `must-gather` directory that was just created in your working directory by running the following command:

      ```
      $ tar cvaf must-gather.tar.gz <must_gather_directory>
      ```
5. Excluding the `/auth` subdirectory, attach the installation directory used during the deployment to your support case on the [Red Hat Customer Portal](https://access.redhat.com).
6. Attach all other data gathered from this procedure to your support case.

## [Chapter 5. Installing a cluster without an external registry](#installing-ove) Copy linkLink copied to clipboard!

You can deploy an OpenShift Container Platform cluster without the need for an external image registry, either in a connected or disconnected environment. This installation method uses a simplified user interface and self-contained media to facilitate the installation.

Although the method supports general clusters, the downloaded media contains an Operator bundle that is curated specifically for Red Hat OpenShift Virtualization Engine, meaning additional Operators must be retrieved separately if required for other use cases.

Important

Installing a cluster without an external registry is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.

For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

### [5.1. Installation method advantages](#virt-installing-ove-advantages_installing-ove) Copy linkLink copied to clipboard!

This method has several advantages for users who want to install a cluster primarily to run virtualized workloads using OpenShift Virtualization.

Simplified web interface
:   The cluster installation is performed through a graphical user interface. In addition to providing reasonable default configurations, this interface guides you through the installation by providing hints and warnings about configuring your cluster, without limiting the configurations that are available at installation time. This reduces the need for in-depth knowledge of OpenShift Container Platform while still allowing for complex configurations to be made.

No external registry needed
:   If you are installing your cluster in a disconnected environment, you do not need to configure an external image registry in your environment when using this method. All other disconnected installation methods require this additional environment setup.

Included Operator bundle
:   You can install the Virtualization bundle, which includes all of the additional Operator Lifecycle Manager (OLM) Operators needed to run virtual machines on your cluster, at the same time as the cluster installation.

Note

This installation method does not come with any storage Operators as part of the Operator bundle. You must configure your own storage solution separately.

### [5.2. Downloading the installation ISO](#virt-installing-ove-iso_installing-ove) Copy linkLink copied to clipboard!

You must first download the ISO image that will be used to run the installation on your bare-metal machines. This image includes all of the necessary OpenShift Container Platform release images, as well as the Operator Lifecycle Manager (OLM) Operators needed to install Virtualization on the cluster.

Note

The size of the ISO image can vary depending on the release you select.

**Procedure**

1. Log in to the [Red Hat Hybrid Cloud Console](https://console.redhat.com).
2. On the **Red Hat OpenShift** tile, click **OpenShift**.
3. On the **Red Hat OpenShift Container Platform** tile, click **Create cluster**.
4. Click the **Datacenter** tab.
5. Under **Assisted Installer**, click **Create cluster**.
6. In the **Cluster details** page, select the toggle for "I’m installing on a disconnected/air-gapped/secured environment".
7. Click **Next**.
8. Click **Download ISO**.

### [5.3. Mounting the ISO and booting the rendezvous node](#virt-installing-ove-booting_installing-ove) Copy linkLink copied to clipboard!

To initiate the cluster installation, attach the downloaded ISO to the machine that will serve as your rendezvous host and boot the machine from the ISO.

The rendezvous node runs as the bootstrap host during the installation, which hosts the configuration web console and runs an Assisted Service that facilitates the cluster deployment.

**Prerequisites**

* You have downloaded the installation ISO.

**Procedure**

1. On the machine that you have designated to be the rendezvous node, attach the ISO image to the machine and boot the machine from this image. You can also boot from a USB drive containing the ISO image.

   Note

   If you mount the ISO via a virtual drive, the cluster installation might take several hours to complete. Mount the ISO with physical media such as a USB drive to reduce the overall installation time.
2. Wait for the machine to boot from the image and display the **Rendezvous node setup** menu.
3. Select **This is the rendezvous node** in the **Rendezvous node setup** menu.

   Important

   You must select only one machine to act as the rendezvous node. Selecting two or more machines as a rendezvous node is not supported.
4. In the **Rendezvous node IP selection** menu, select an IP address from the list to use as the rendezvous node IP address and select **Continue**. Make note of this address for later use.
5. Wait for the rendezvous node to provide a URL for finishing the installation and save the URL for later use, as shown in the following image.

### [5.4. Configuring cluster details and choosing Operators to install](#virt-installing-ove-console-initial_installing-ove) Copy linkLink copied to clipboard!

Once the rendezvous node has been booted from the ISO image, configure details about your cluster and choose Virtualization Operators to install from the web console.

**Prerequisites**

* You have the URL of the installation web console that was provided by the rendezvous node.

**Procedure**

1. In a web browser, go to the URL provided by the rendezvous node.
2. Configure your cluster in the **Cluster details** page:

   1. Enter a name for the cluster in the **Cluster name** field.
   2. Enter a base domain for the cluster in the **Base domain** field. All subdomains for the cluster will use this base domain.

      Note

      The base domain must be a valid DNS name. You must not have a wildcard domain set up for the base domain.
   3. Enter your pull secret in the **Pull secret** field. You can obtain a copy of your pull secret from the [Red Hat Hybrid Cloud Console](https://console.redhat.com/openshift/install/pull-secret).
   4. Optional: In the **Number of control plane nodes** field, select the number of control plane nodes for your installation from the dropdown menu. The default value is `3`.
   5. Optional: Select the **Include custom manifests** checkbox if you want to upload custom manifests to further configure your cluster. This option adds an additional page for custom manifests that you use later in the configuration process.

      Important

      If you have already added custom manifests, clearing the **Include custom manifests** checkbox automatically deletes them all. You must confirm the deletion.
   6. Optional: Under **Encryption of installation disks**, select the toggle switch for each disk you want to encrypt.
   7. If you are encrypting disks, select either **TPM v2** or **Tang** as your encryption method.
   8. If you are encrypting disks using a Tang server, enter the **Server URL** and **Server Thumbprint** in the **Tang servers** section of the page. You can select **Add another Tang server** to configure details for additional Tang server.
   9. Click **Next** to continue. Once you proceed to the next page, you cannot go back to change any of these cluster details.
3. Choose additional Operators to install in the **Operators** page:

   1. If you want to install all of the Operators recommended for running Virtualization on your cluster, select **Virtualization** in the **Bundles** section.
   2. If you want to install only some Operators, select the individual Operators from the Single Operators section.

      Note

      Some of the listed Operators are available only as part of the Virtualization Operator bundle.
   3. Click **Next** to continue.

### [5.5. Booting the remaining cluster hosts](#virt-installing-ove-hosts_installing-ove) Copy linkLink copied to clipboard!

After you have configured initial cluster details in the installation web console and have a defined cluster topology, you must boot the remaining machines that will make up your cluster from the ISO image.

Note

You can boot non-rendezvous node machines earlier in the installation process, even before you designate a machine as the rendezvous node. However, you must know the valid IP address that you will select for the rendezvous node.

When you boot your non-rendezvous node machines, the machines will perform a check to see if an Assisted Service is running at the specified rendezvous IP address. If the service is not yet running, a warning appears to confirm whether you would still like to proceed booting the machine from the ISO image.

**Prerequisites**

* You have downloaded the installation ISO.

**Procedure**

1. Attach the ISO image to a machine and boot the machine from this image. You can also boot from a USB drive containing the ISO image.
2. Wait for a machine to boot from the image and display the **Rendezvous node setup** menu.
3. Enter the rendezvous node IP address in the **Rendezvous node setup** menu and select **Save rendezvous IP**.
4. Select **Save and Continue**.
5. Repeat this process for each remaining machine that will comprise the hosts in your cluster.

### [5.6. Completing cluster configuration and initiating the installation](#virt-installing-ove-console-final_installing-ove) Copy linkLink copied to clipboard!

Before you can finally initiate the cluster installation, you must verify host details, configure cluster networking details, and download the default cluster credentials.

**Prerequisites**

* You have booted all of the hosts that will comprise your cluster and configured them with the correct rendezvous node IP address.

  Important

  You can add as many hosts as you want to your cluster. However, at this stage, you must at least have enough available hosts to match the value you specified in the **Number of control plane nodes** field of the installation console’s **Cluster details** page.

**Procedure**

1. On the installation console hosted by the rendezvous node, configure the hosts in the **Host discovery** page:

   1. Verify that every machine you booted from the ISO image appears in the **Host Inventory** section and has a **Status** value of **Ready**.
   2. For each host, click the expand icon and verify that all of the specification fields are correct.
   3. Optional: For each host except the rendezvous node, configure the role by selecting an option from the dropdown menu of the **Role** column. The default value for every host except the rendezvous node is `Auto-assign`.
   4. Click **Next** to continue.
2. On the **Storage** page, click the expand icon for each host and verify that all of the specification fields are correct.
3. Click **Next** to continue.
4. If you want to manage your own networking, select the **User-Managed Networking** option on the **Networking** page.
5. If you want the cluster to manage networking, select the **Cluster-Managed Networking** option on the **Networking** page and configure cluster networking:

   1. Select a **Networking stack type**.
   2. Optional: Select a machine network from the dropdown menu of the **Machine network** field. Otherwise, a default value is selected.
   3. Enter an IP address in the **API IP** field. An API IP provides an endpoint for all users to interact with and configure the platform.
   4. Enter an IP address in the **Ingress IP** field. An ingress IP provides an endpoint for application traffic flowing from outside the cluster.
6. Optional: Select the **Use advanced networking** checkbox and configure other parameters such as the **Cluster network CIDR**, the **Cluster network host prefix**, or **the Service network CIDR**.

   This option is available for both cluster-managed and user-managed networking.
7. Optional: Enter a key in the **Host SSH Public Key for troubleshooting after installation** field, which you can use to connect to hosts using a public SSH key for troubleshooting after installation.

   This option is available for both cluster-managed and user-managed networking.
8. Click **Next** to continue.
9. On the **Download credentials** page, select the checkbox to acknowledge that you must download credential files prior to cluster installation.
10. Click **Download credentials** and save the cluster credentials file in a secure location.

    Important

    You must download the credentials at this stage. Once you initiate the cluster installation, the rendezvous node reboots and you can no longer retrieve the credentials.
11. On the **Review and create** page, review all of the cluster details and click **Install cluster** to initiate the cluster installation.

    During the installation process, the rendezvous node reboots and the console you used to configure the installation is no longer accessible. At that point, the URL of the deployed cluster’s web console is provided, although this console is not accessible until the cluster installation is completed.

    Once the cluster is installed, you can visit this URL and sign in to the web console with your downloaded credentials.

## [Chapter 6. Preparing PXE assets for OpenShift Container Platform](#prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

You can create the assets needed to PXE boot an OpenShift Container Platform cluster by using the Agent-based Installer.

The assets you create in these procedures will deploy a single-node OpenShift Container Platform installation. You can use these procedures as a basis and modify configurations according to your requirements.

See "Installing an OpenShift Container Platform cluster with the Agent-based Installer" to learn about more configurations available with the Agent-based Installer.

### [6.1. Prerequisites for preparing PXE assets](#prerequisites_prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

Before beginning to prepare PXE assets, you must complete prerequisite tasks.

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update".

### [6.2. Downloading the Agent-based Installer](#installing-ocp-agent-retrieve_prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

Begin the installation process by downloading the Agent-based Installer and the CLI needed for your installation.

**Procedure**

1. Log in to the Red Hat Hybrid Cloud Console using your login credentials.
2. Navigate to [Datacenter](https://console.redhat.com/openshift/create/datacenter).
3. Click **Run Agent-based Installer locally**.
4. Select the operating system and architecture for the **OpenShift Installer** and **Command line interface**.
5. Click **Download Installer** to download and extract the install program.
6. Download or copy the pull secret by clicking on **Download pull secret** or **Copy pull secret**.
7. Click **Download command-line tools** and place the `openshift-install` binary in a directory that is on your `PATH`.

### [6.3. Creating the preferred configuration inputs](#installing-ocp-agent-inputs_prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

Create the preferred configuration inputs used to create the PXE files.

Note

Configuring the `install-config.yaml` and `agent-config.yaml` files is the preferred method for using the Agent-based Installer. Using GitOps ZTP manifests is optional.

**Procedure**

1. Install the `nmstate` dependency by running the following command:

   ```
   $ sudo dnf install /usr/bin/nmstatectl -y
   ```
2. Place the `openshift-install` binary in a directory that is on your PATH.
3. Create a directory to store the install configuration by running the following command:

   ```
   $ mkdir ~/<directory_name>
   ```
4. Create the `install-config.yaml` file by running the following command:

   ```
   $ cat << EOF > ./<directory_name>/install-config.yaml
   apiVersion: v1
   baseDomain: test.example.com
   compute:
   - architecture: amd64
     hyperthreading: Enabled
     name: worker
     replicas: 0
   controlPlane:
     architecture: amd64
     hyperthreading: Enabled
     name: master
     replicas: 1
   metadata:
     name: sno-cluster
   networking:
     clusterNetwork:
     - cidr: 10.128.0.0/14
       hostPrefix: 23
     machineNetwork:
     - cidr: 192.168.0.0/16
     networkType: OVNKubernetes
     serviceNetwork:
     - 172.30.0.0/16
   platform:
     none: {}
   pullSecret: '<pull_secret>'
   sshKey: '<ssh_pub_key>'
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
   EOF
   ```

   where:

   `compute.architecture`
   :   Specifies the system architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`.

       If you are using the release image with the `multi` payload, you can install the cluster on different architectures such as `arm64`, `amd64`, `s390x`, and `ppc64le`. Otherwise, you can install the cluster only on the `release architecture` displayed in the output of the `openshift-install version` command. For more information, see "Verifying the supported architecture for installing an Agent-based Installer cluster".

   `metadata.name`
   :   Specifies your cluster name. This value is required.

   `networking.networkingType`
   :   Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

   `platform`
   :   Specifies your platform. If you set the platform to `vSphere`, `baremetal`, or `none`, you can configure IP address endpoints for cluster nodes in three ways: IPv4, IPv6, or IPv4 and IPv6 in parallel (dual-stack).

       **Example of dual-stack networking**

       ```
       networking:
         clusterNetwork:
           - cidr: 172.21.0.0/16
             hostPrefix: 23
           - cidr: fd02::/48
             hostPrefix: 64
         machineNetwork:
           - cidr: 192.168.11.0/16
           - cidr: 2001:DB8::/32
         serviceNetwork:
           - 172.22.0.0/16
           - fd03::/112
         networkType: OVNKubernetes
       platform:
         baremetal:
           apiVIPs:
           - 192.168.11.3
           - 2001:DB8::4
           ingressVIPs:
           - 192.168.11.4
           - 2001:DB8::5
       ```

       Note

       For bare-metal platforms, host settings made in the platform section of the `install-config.yaml` file are used by default, unless they are overridden by configurations made in the `agent-config.yaml` file.

   `pullSecret`
   :   Specifies your pull secret.

   `sshKey`
   :   Specifies your SSH public key.

   `additionalTrustBundle`
   :   Specifies the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry. You must specify this parameter if you are using a disconnected mirror registry.

   `imageContentSources`
   :   Specifies the `imageContentSources` section according to the output of the command that you used to mirror the repository. You must specify this parameter if you are using a disconnected mirror registry.

       Important

       * When using the `oc adm release mirror` command, use the output from the `imageContentSources` section.
       * When using the `oc mirror` command, use the `repositoryDigestMirrors` section of the `ImageContentSourcePolicy` file that results from running the command.
       * The `ImageContentSourcePolicy` resource is deprecated.
5. Create the `agent-config.yaml` file by running the following command:

   ```
   $ cat > agent-config.yaml << EOF
   apiVersion: v1beta1
   kind: AgentConfig
   metadata:
     name: sno-cluster
   rendezvousIP: 192.168.111.80
   hosts:
     - hostname: master-0
       interfaces:
         - name: eno1
           macAddress: 00:ef:44:21:e6:a5
       rootDeviceHints:
         deviceName: /dev/sdb
       networkConfig:
         interfaces:
           - name: eno1
             type: ethernet
             state: up
             mac-address: 00:ef:44:21:e6:a5
             ipv4:
               enabled: true
               address:
                 - ip: 192.168.111.80
                   prefix-length: 23
               dhcp: false
         dns-resolver:
           config:
             server:
               - 192.168.111.1
         routes:
           config:
             - destination: 0.0.0.0/0
               next-hop-address: 192.168.111.2
               next-hop-interface: eno1
               table-id: 254
   EOF
   ```

   where:

   `rendezvousIP`
   :   Specifies the IP address used to determine which node performs the bootstrapping process as well as running the `assisted-service` component. You must provide the rendezvous IP address when you do not specify at least one host’s IP address in the `networkConfig` parameter. If this address is not provided, one IP address is selected from the provided hosts' `networkConfig`.

   `hosts`
   :   Specifies host configuration. The number of hosts defined must not exceed the total number of hosts defined in the `install-config.yaml` file, which is the sum of the values of the `compute.replicas` and `controlPlane.replicas` parameters. This configuration is optional.

   `hosts.hostname`
   :   Specifies a value that overrides the hostname obtained from either the Dynamic Host Configuration Protocol (DHCP) or a reverse DNS lookup. Each host must have a unique hostname supplied by one of these methods. This configuration is optional.

   `hosts.rootDeviceHints`
   :   Specifies a configuration that enables provisioning of the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device. The installation program examines the devices in the order it discovers them, and compares the discovered values with the hint values. It uses the first discovered device that matches the hint value.

       Note

       This parameter is mandatory for FCP multipath configurations on IBM Z.

   `hosts.networkConfig`
   :   Specifies the network interface configuration of a host in NMState format. This configuration is optional.
6. Optional: To create an iPXE script, add the `bootArtifactsBaseURL` to the `agent-config.yaml` file:

   ```
   apiVersion: v1beta1
   kind: AgentConfig
   metadata:
     name: sno-cluster
   rendezvousIP: 192.168.111.80
   bootArtifactsBaseURL: <asset_server_URL>
   ```

   Where `<asset_server_URL>` is the URL of the server you will upload the PXE assets to.

### [6.4. Creating the PXE assets](#pxe-assets-ocp-agent_prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

Create the assets and optional script to implement in your PXE infrastructure.

**Procedure**

1. Create the PXE assets by running the following command:

   ```
   $ openshift-install agent create pxe-files
   ```

   The generated PXE assets and optional iPXE script can be found in the `boot-artifacts` directory.

   **Example filesystem with PXE assets and optional iPXE script**

   ```
   boot-artifacts
       ├─ agent.x86_64-initrd.img
       ├─ agent.x86_64.ipxe
       ├─ agent.x86_64-rootfs.img
       └─ agent.x86_64-vmlinuz
   ```

   Important

   The contents of the `boot-artifacts` directory vary depending on the specified architecture.

   Note

   Red Hat Enterprise Linux CoreOS (RHCOS) supports multipathing on the primary disk, allowing stronger resilience to hardware failure to achieve higher host availability. Multipathing is enabled by default in the Agent ISO image, with a default `/etc/multipath.conf` configuration.
2. Upload the PXE assets and optional script to your infrastructure where they will be accessible during the boot process.

   Note

   If you generated an iPXE script, the location of the assets must match the `bootArtifactsBaseURL` value you added to the `agent-config.yaml` file.

### [6.5. Manually adding IBM Z agents](#installing-ocp-agent-ibm-z_prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

After creating the PXE assets, you can add IBM Z® agents.

Only use this procedure for IBM Z® clusters.

Depending on your IBM Z® environment, you can choose from the following options:

* Adding IBM Z® agents with z/VM
* Adding IBM Z® agents with RHEL KVM
* Adding IBM Z® agents with Logical Partition (LPAR)

Note

Currently, ISO boot support on IBM Z® (`s390x`) is available only for Red Hat Enterprise Linux (RHEL) KVM, which provides the flexibility to choose either PXE or ISO-based installation. For installations with z/VM and Logical Partition (LPAR), only PXE boot is supported.

#### [6.5.1. Networking requirements for IBM Z](#networking-reqs-ibm-z_prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

In IBM Z environments, advanced networking technologies such as Open Systems Adapter (OSA), HiperSockets, and Remote Direct Memory Access (RDMA) over Converged Ethernet (RoCE) require specific configurations that deviate from the standard network settings and those needs to be persisted for multiple boot scenarios that occur in the Agent-based Installation.

To persist these parameters during boot, the `ai.ip_cfg_override=1` parameter is required in the `.parm` file. This parameter is used with the configured network cards to ensure a successful and efficient deployment on IBM Z.

The following table lists the network devices that are supported on each hypervisor for the network configuration override functionality:

Expand

| Network device | z/VM | KVM | LPAR Classic | LPAR Dynamic Partition Manager (DPM) |
| --- | --- | --- | --- | --- |
| Virtual Switch | Supported [1] | Not applicable [2] | Not applicable | Not applicable |
| Direct attached Open Systems Adapter (OSA) | Supported | Not required [3] | Supported | Not required |
| RDMA over Converged Ethernet (RoCE) | Not required | Not required | Not required | Not required |
| HiperSockets | Supported | Not required | Supported | Not required |

Show more

1. Supported: When the `ai.ip_cfg_override` parameter is required for the installation procedure.
2. Not Applicable: When a network card is not applicable to be used on the hypervisor.
3. Not required: When the `ai.ip_cfg_override` parameter is not required for the installation procedure.

#### [6.5.2. Configuring network overrides in an IBM Z environment](#configuring-network-overrides-ibm_prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

You can specify a static IP address on IBM Z machines that use Logical Partition (LPAR) and z/VM. This is useful when the network devices do not have a static MAC address assigned to them.

Note

If you are using an OSA network device in Processor Resource/Systems Manager (PR/SM) mode, the lack of persistent MAC addresses can lead to a dynamic assignment of roles for nodes. This means that the roles of individual nodes are not fixed and can change, as the system is unable to reliably associate specific MAC addresses with designated node roles. If MAC addresses are not persistent for any of the interfaces, roles for the nodes are assigned randomly during Agent-based installation.

**Procedure**

* If you have an existing `.parm` file, edit it to include the following entry:

  ```
  ai.ip_cfg_override=1
  ```

  This parameter allows the file to add the network settings to the Red Hat Enterprise Linux CoreOS (RHCOS) installer.

  Note

  The `override` parameter overrides the host’s network configuration settings.

  **Example `.parm` file**

  ```
  rd.neednet=1 cio_ignore=all,!condev
  console=ttysclp0
  coreos.live.rootfs_url=<coreos_url>
  ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns>
  rd.znet=qeth,<network_adaptor_range>,layer2=1
  rd.<disk_type>=<adapter>
  rd.zfcp=<adapter>,<wwpn>,<lun> random.trust_cpu=on
  zfcp.allow_lun_scan=0
  ai.ip_cfg_override=1
  ignition.firstboot ignition.platform.id=metal
  random.trust_cpu=on
  ```

  + For the `coreos.live.rootfs_url` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` that you are booting. Only HTTP and HTTPS protocols are supported.
  + For installations on direct access storage devices (DASD) type disks, use `rd.` to specify the DASD where Red Hat Enterprise Linux CoreOS (RHCOS) is to be installed. For installations on Fibre Channel Protocol (FCP) disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where RHCOS is to be installed.
  + Specify values for `<adapter>`, `<wwpn>`, and `<lun>` as in the following example: `rd.zfcp=0.0.8002,0x500507630400d1e3,0x4000404600000000`.

  Important

  The `ip=` kernel parameter uses the following syntax:

  `ip=[IP]:[Gateway]:[Netmask]:[Hostname]:[Interface]:[None]:[DNS]`

  For VLAN configurations:

  + Define both the **base interface** and the **tagged VLAN interface** separately.
  + The `vlan=` parameter links the tagged interface (for example, `encbdf0.300`) to the underlying physical interface (`encbdf0`).

  For bonded interfaces:

  + No changes are required in the default kernel command-line parameters.
  + To install nodes by using bonded interfaces, provide the appropriate bond configuration in the `agent-config` file.

#### [6.5.3. Adding IBM Z agents with z/VM](#installing-ocp-agent-ibm-z-zvm_prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

You can manually add IBM Z® agents with z/VM.

Only use this procedure for IBM Z® clusters with z/VM.

**Prerequisites**

* You have a running file server with access to the guest virtual machines (VMs).

**Procedure**

1. Create a parameter file for the z/VM guest:

   **Example parameter file**

   ```
   rd.neednet=1 \
   console=ttysclp0 \
   coreos.live.rootfs_url=<rootfs_url> \
   ip=172.18.78.2::172.18.78.1:255.255.255.0:::none nameserver=172.18.78.1 \
   zfcp.allow_lun_scan=0 \
   ai.ip_cfg_override=1 \
   rd.znet=qeth,0.0.bdd0,0.0.bdd1,0.0.bdd2,layer2=1 \
   rd.dasd=0.0.4411 \
   rd.zfcp=0.0.8001,0x50050763040051e3,0x4000406300000000 \
   fips=1 \
   random.trust_cpu=on rd.luks.options=discard \
   ignition.firstboot ignition.platform.id=metal \
   console=tty1 console=ttyS1,115200n8 \
   coreos.inst.persistent-kargs="console=tty1 console=ttyS1,115200n8"
   ```

   * For the `coreos.live.rootfs_url` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` that you are booting. Only HTTP and HTTPS protocols are supported.
   * For the `ip` parameter, assign the IP address automatically using DHCP, or manually assign the IP address, as described in "Installing a cluster with z/VM on IBM Z® and IBM® LinuxONE".
   * The default for `zfcp.allow_lun_scan` is `1`. Omit this entry when using an OSA network adapter.
   * For installations on DASD-type disks, use `rd.dasd` to specify the DASD where Red Hat Enterprise Linux CoreOS (RHCOS) is to be installed. Omit this entry for FCP-type disks.
   * For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where RHCOS is to be installed. Omit this entry for DASD-type disks.

     Note

     For FCP multipath configurations, provide available multiple paths to the disk instead of a single path, and add `rd.multipath=default` to enable multipath during installation.

     **Example**

     ```
     rd.zfcp=<adapter1>,<wwpn1>,<lun1> \
     rd.zfcp=<adapter2>,<wwpn2>,<lun2> \
     rd.multipath=default
     ```
   * To enable FIPS mode, specify `fips=1`. This entry is required in addition to setting the `fips` parameter to `true` in the `install-config.yaml` file.

   Leave all other parameters unchanged.
2. Punch the `kernel.img`,`generic.parm`, and `initrd.img` files to the virtual reader of the z/VM guest virtual machine.

   For more information, see [PUNCH](https://www.ibm.com/docs/en/zvm/latest?topic=commands-punch) (IBM Documentation).

   Tip

   You can use the `CP PUNCH` command or, if you use Linux, the `vmur` command, to transfer files between two z/VM guest virtual machines.
3. Log in to the conversational monitor system (CMS) on the bootstrap machine.
4. IPL the bootstrap machine from the reader by running the following command:

   ```
   $ ipl c
   ```

   For more information, see [IPL](https://www.ibm.com/docs/en/zvm/latest?topic=commands-ipl) (IBM Documentation).

#### [6.5.4. Adding IBM Z agents with RHEL KVM](#installing-ocp-agent-ibm-z-kvm_prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

You can manually add IBM Z® agents with RHEL KVM.

Only use this procedure for IBM Z® clusters with RHEL KVM.

Note

The `nmstateconfig` parameter must be configured for the KVM boot.

**Procedure**

1. Boot your RHEL KVM machine.
2. To deploy the virtual server, run the `virt-install` command with the following parameters:

   ```
   $ virt-install \
      --name <vm_name> \
      --autostart \
      --ram=16384 \
      --cpu host \
      --vcpus=8 \
      --location <path_to_kernel_initrd_image>,kernel=kernel.img,initrd=initrd.img \
      --disk <qcow_image_path> \
      --network network:macvtap ,mac=<mac_address> \
      --graphics none \
      --noautoconsole \
      --wait=-1 \
      --extra-args "rd.neednet=1 nameserver=<nameserver>" \
      --extra-args "ip=<IP>::<nameserver>::<hostname>:enc1:none" \
      --extra-args "coreos.live.rootfs_url=http://<http_server>:8080/agent.s390x-rootfs.img" \
      --extra-args "random.trust_cpu=on rd.luks.options=discard" \
      --extra-args "ignition.firstboot ignition.platform.id=metal" \
      --extra-args "console=tty1 console=ttyS1,115200n8" \
      --extra-args "coreos.inst.persistent-kargs=console=tty1 console=ttyS1,115200n8" \
      --osinfo detect=on,require=off
   ```

   For the `--location` parameter, specify the location of the `kernel` and `initrd` files. The location can be a local server path or a URL using HTTP or HTTPS.
3. Optional: Enable FIPS mode.

   To enable FIPS mode on IBM Z® clusters with RHEL KVM you must use PXE boot instead and run the `virt-install` command with the following parameters:

   **PXE boot**

   ```
   $ virt-install \
      --name <vm_name> \
      --autostart \
      --ram=16384 \
      --cpu host \
      --vcpus=8 \
      --location <path_to_kernel_initrd_image>,kernel=kernel.img,initrd=initrd.img \
      --disk <qcow_image_path> \
      --network network:macvtap ,mac=<mac_address> \
      --graphics none \
      --noautoconsole \
      --wait=-1 \
      --extra-args "rd.neednet=1 nameserver=<nameserver>" \
      --extra-args "ip=<IP>::<nameserver>::<hostname>:enc1:none" \
      --extra-args "coreos.live.rootfs_url=http://<http_server>:8080/agent.s390x-rootfs.img" \
      --extra-args "random.trust_cpu=on rd.luks.options=discard" \
      --extra-args "ignition.firstboot ignition.platform.id=metal" \
      --extra-args "console=tty1 console=ttyS1,115200n8" \
      --extra-args "coreos.inst.persistent-kargs=console=tty1 console=ttyS1,115200n8" \
      --extra-args "fips=1" \
      --osinfo detect=on,require=off
   ```

   where:

   `--location`
   :   Specifies the location of the kernel/initrd on the HTTP or HTTPS server.

   `--extra-args "fips=1"`
   :   Specifies the enablement of FIPS mode. This entry is required in addition to setting the `fips` parameter to `true` in the `install-config.yaml` file.

       Note

       * For KVM-based installations using DASD devices on IBM Z, a partition (for example, `/dev/dasdb1`) must be created using the `fdasd` partitioning tool.
       * Currently, only PXE boot is supported to enable FIPS mode on IBM Z®.

#### [6.5.5. Adding IBM Z agents in a Logical Partition (LPAR)](#adding-ibm-z-lpar-agents_prepare-pxe-assets-agent) Copy linkLink copied to clipboard!

You can manually add IBM Z® agents to your cluster that runs in an LPAR environment.

Use this procedure only for IBM Z® clusters running in an LPAR.

**Prerequisites**

* You have Python 3 installed.
* You have a running file server with access to the Logical Partition (LPAR).

**Procedure**

1. Create a boot parameter file for the agents.

   **Example parameter file**

   ```
   rd.neednet=1 cio_ignore=all,!condev \
   console=ttysclp0 \
   ignition.firstboot ignition.platform.id=metal
   coreos.live.rootfs_url=http://<http_server>/rhcos-<version>-live-rootfs.<architecture>.img \
   coreos.inst.persistent-kargs=console=ttysclp0 \
   ip=<ip>::<gateway>:<netmask>:<hostname>::none nameserver=<dns> \
   rd.znet=qeth,<network_adaptor_range>,layer2=1
   rd.<disk_type>=<adapter> \
   fips=1 \
   zfcp.allow_lun_scan=0 \
   ai.ip_cfg_override=1 \
   random.trust_cpu=on rd.luks.options=discard
   ```

   * For the `coreos.live.rootfs_url` artifact, specify the matching `rootfs` artifact for the `kernel` and `initramfs` that you are starting. Only HTTP and HTTPS protocols are supported.
   * For the `ip` parameter, manually assign the IP address, as described in "Installing a cluster with z/VM on IBM Z and IBM LinuxONE".
   * For installations on DASD-type disks, use `rd.dasd` to specify the DASD where Red Hat Enterprise Linux CoreOS (RHCOS) is to be installed. For installations on FCP-type disks, use `rd.zfcp=<adapter>,<wwpn>,<lun>` to specify the FCP disk where RHCOS is to be installed.

     Note

     For FCP multipath configurations, provide available multiple paths to the disk instead of a single path, and add `rd.multipath=default` to enable multipath during installation.

     **Example**

     ```
     rd.zfcp=<adapter1>,<wwpn1>,<lun1> \
     rd.zfcp=<adapter2>,<wwpn2>,<lun2> \
     rd.multipath=default
     ```
   * To enable FIPS mode, specify `fips=1`. This entry is required in addition to setting the `fips` parameter to `true` in the `install-config.yaml` file.

     Note

     The `.ins` and `initrd.img.addrsize` files are automatically generated for `s390x` architecture as part of boot-artifacts from the installation program and are only used when booting in an LPAR environment.

     **Example filesystem with LPAR boot**

     ```
     boot-artifacts
         ├─ agent.s390x-generic.ins
         ├─ agent.s390x-initrd.addrsize
         ├─ agent.s390x-rootfs.img
         └─ agent.s390x-kernel.img
         └─ agent.s390x-rootfs.img
     ```
2. Rename the `boot-artifacts` file present in the `generic.ins` parameter file to match the names of the `boot-artifacts` file generated by the installation program.
3. Transfer the `initrd`, `kernel`, `generic.ins`, and `initrd.img.addrsize` parameter files to the file server. For more information, see [Booting Linux in LPAR mode](https://www.ibm.com/docs/en/linux-on-systems?topic=bl-booting-linux-in-lpar-mode) (IBM documentation).
4. Start the machine.
5. Repeat the procedure for all other machines in the cluster.

## [Chapter 7. Preparing installation assets for iSCSI booting](#installing-using-iscsi) Copy linkLink copied to clipboard!

You can boot an OpenShift Container Platform cluster through Internet Small Computer System Interface (iSCSI) by using an ISO image generated by the Agent-based Installer.

The following procedures describe how to prepare the necessary installation resources to boot from an iSCSI target.

The assets you create in these procedures deploy a single-node OpenShift Container Platform installation. You can use these procedures as a basis and modify configurations according to your requirements.

### [7.1. Requirements for iSCSI booting](#iscsi-boot-requirements_installing-using-iscsi) Copy linkLink copied to clipboard!

Several configurations are necessary to enable iSCSI booting when using the Agent-based Installer.

The following configurations are required:

* Dynamic Host Configuration Protocol (DHCP) must be configured. Static networking is not supported.
* You must create an additional network for iSCSI that is separate from the machine network of the cluster. The machine network is rebooted during cluster installation and cannot be used for the iSCSI session.
* If the host on which you are booting the agent ISO image also has an installed disk, it might be necessary to specify the iSCSI disk name in the `rootDeviceHints` parameter to ensure that it is chosen as the boot disk for the final Red Hat Enterprise Linux CoreOS (RHCOS) image. You can also use a diskless environment for iSCSI booting, in which case you do not need to set the `rootDeviceHints` parameter.

### [7.2. Prerequisites for installing a cluster with the Agent-based Installer](#prerequisites_installing-using-iscsi) Copy linkLink copied to clipboard!

Before beginning your cluster installation, you must complete prerequisite tasks that prepare your environment.

* You reviewed details about the OpenShift Container Platform installation and update processes. For more information, see "Installation and update".
* You read "Selecting a cluster installation method and preparing it for users".
* If you use a firewall or proxy, you configured it to allow the sites that your cluster requires access to. For more information, see "Configuring your firewall".
* You configured your firewall to allow TCP traffic on port `8090` from all hosts to the rendezvous host so that hosts can reach the Assisted Service API during discovery and bootstrap. For more information, see "Port requirements for the rendezvous host".

### [7.3. Downloading the Agent-based Installer](#installing-ocp-agent-retrieve_installing-using-iscsi) Copy linkLink copied to clipboard!

Begin the installation process by downloading the Agent-based Installer and the CLI needed for your installation.

**Procedure**

1. Log in to the Red Hat Hybrid Cloud Console using your login credentials.
2. Navigate to [Datacenter](https://console.redhat.com/openshift/create/datacenter).
3. Click **Run Agent-based Installer locally**.
4. Select the operating system and architecture for the **OpenShift Installer** and **Command line interface**.
5. Click **Download Installer** to download and extract the install program.
6. Download or copy the pull secret by clicking on **Download pull secret** or **Copy pull secret**.
7. Click **Download command-line tools** and place the `openshift-install` binary in a directory that is on your `PATH`.

### [7.4. Creating the preferred configuration inputs](#installing-ocp-agent-inputs_installing-using-iscsi) Copy linkLink copied to clipboard!

Create the preferred configuration inputs used to create the agent image.

Note

Configuring the `install-config.yaml` and `agent-config.yaml` files is the preferred method for using the Agent-based Installer. Using GitOps ZTP manifests is optional.

**Procedure**

1. Install the `nmstate` dependency by running the following command:

   ```
   $ sudo dnf install /usr/bin/nmstatectl -y
   ```
2. Place the `openshift-install` binary in a directory that is on your PATH.
3. Create a directory to store the install configuration by running the following command:

   ```
   $ mkdir ~/<directory_name>
   ```
4. Create the `install-config.yaml` file by running the following command:

   ```
   $ cat << EOF > ./<directory_name>/install-config.yaml
   apiVersion: v1
   baseDomain: test.example.com
   compute:
   - architecture: amd64
     hyperthreading: Enabled
     name: worker
     replicas: 0
   controlPlane:
     architecture: amd64
     hyperthreading: Enabled
     name: master
     replicas: 1
   metadata:
     name: sno-cluster
   networking:
     clusterNetwork:
     - cidr: 10.128.0.0/14
       hostPrefix: 23
     machineNetwork:
     - cidr: 192.168.0.0/16
     networkType: OVNKubernetes
     serviceNetwork:
     - 172.30.0.0/16
   platform:
     none: {}
   pullSecret: '<pull_secret>'
   sshKey: '<ssh_pub_key>'
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
   EOF
   ```

   where:

   `compute.architecture`
   :   Specifies the system architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`.

       If you are using the release image with the `multi` payload, you can install the cluster on different architectures such as `arm64`, `amd64`, `s390x`, and `ppc64le`. Otherwise, you can install the cluster only on the `release architecture` displayed in the output of the `openshift-install version` command. For more information, see "Verifying the supported architecture for installing an Agent-based Installer cluster".

   `metadata.name`
   :   Specifies your cluster name. This value is required.

   `networking.networkingType`
   :   Specifies the cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

   `platform`
   :   Specifies your platform. If you set the platform to `vSphere`, `baremetal`, or `none`, you can configure IP address endpoints for cluster nodes in three ways: IPv4, IPv6, or IPv4 and IPv6 in parallel (dual-stack).

       **Example of dual-stack networking**

       ```
       networking:
         clusterNetwork:
           - cidr: 172.21.0.0/16
             hostPrefix: 23
           - cidr: fd02::/48
             hostPrefix: 64
         machineNetwork:
           - cidr: 192.168.11.0/16
           - cidr: 2001:DB8::/32
         serviceNetwork:
           - 172.22.0.0/16
           - fd03::/112
         networkType: OVNKubernetes
       platform:
         baremetal:
           apiVIPs:
           - 192.168.11.3
           - 2001:DB8::4
           ingressVIPs:
           - 192.168.11.4
           - 2001:DB8::5
       ```

       Note

       For bare-metal platforms, host settings made in the platform section of the `install-config.yaml` file are used by default, unless they are overridden by configurations made in the `agent-config.yaml` file.

   `pullSecret`
   :   Specifies your pull secret.

   `sshKey`
   :   Specifies your SSH public key.

   `additionalTrustBundle`
   :   Specifies the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority or the self-signed certificate that you generated for the mirror registry. You must specify this parameter if you are using a disconnected mirror registry.

   `imageContentSources`
   :   Specifies the `imageContentSources` section according to the output of the command that you used to mirror the repository. You must specify this parameter if you are using a disconnected mirror registry.

       Important

       * When using the `oc adm release mirror` command, use the output from the `imageContentSources` section.
       * When using the `oc mirror` command, use the `repositoryDigestMirrors` section of the `ImageContentSourcePolicy` file that results from running the command.
       * The `ImageContentSourcePolicy` resource is deprecated.
5. Create the `agent-config.yaml` file by running the following command:

   ```
   $ cat > agent-config.yaml << EOF
   apiVersion: v1beta1
   kind: AgentConfig
   metadata:
     name: sno-cluster
   rendezvousIP: 192.168.111.80
   hosts:
     - hostname: master-0
       interfaces:
         - name: eno1
           macAddress: 00:ef:44:21:e6:a5
       rootDeviceHints:
         deviceName: /dev/sdb
       networkConfig:
         interfaces:
           - name: eno1
             type: ethernet
             state: up
             mac-address: 00:ef:44:21:e6:a5
             ipv4:
               enabled: true
               address:
                 - ip: 192.168.111.80
                   prefix-length: 23
               dhcp: false
         dns-resolver:
           config:
             server:
               - 192.168.111.1
         routes:
           config:
             - destination: 0.0.0.0/0
               next-hop-address: 192.168.111.2
               next-hop-interface: eno1
               table-id: 254
   minimalISO: true
   EOF
   ```

   where:

   `rendezvousIP`
   :   Specifies the IP address used to determine which node performs the bootstrapping process as well as running the `assisted-service` component. You must provide the rendezvous IP address when you do not specify at least one host’s IP address in the `networkConfig` parameter. If this address is not provided, one IP address is selected from the provided hosts' `networkConfig`.

   `hosts`
   :   Specifies host configuration. The number of hosts defined must not exceed the total number of hosts defined in the `install-config.yaml` file, which is the sum of the values of the `compute.replicas` and `controlPlane.replicas` parameters. This configuration is optional.

   `hosts.hostname`
   :   Specifies a value that overrides the hostname obtained from either the Dynamic Host Configuration Protocol (DHCP) or a reverse DNS lookup. Each host must have a unique hostname supplied by one of these methods. This configuration is optional.

   `hosts.rootDeviceHints`
   :   Specifies a configuration that enables provisioning of the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device. The installation program examines the devices in the order it discovers them, and compares the discovered values with the hint values. It uses the first discovered device that matches the hint value.

       Note

       This parameter is mandatory for FCP multipath configurations on IBM Z.

   `hosts.networkConfig`
   :   Specifies the network interface configuration of a host in NMState format. This configuration is optional.

   `minimalISO`
   :   Specifies whether to generate an ISO image without the rootfs image file, instead providing details about where to pull the rootfs file from. You must set this parameter to `true` to enable iSCSI booting.

### [7.5. Creating the installation files](#installing-ocp-agent-iscsi-files_installing-using-iscsi) Copy linkLink copied to clipboard!

Generate the ISO image and create an iPXE script to upload to your iSCSI target.

**Procedure**

1. Create the agent image by running the following command:

   ```
   $ openshift-install --dir <install_directory> agent create image
   ```
2. Create an iPXE script by running the following command:

   ```
   $ cat << EOF > agent.ipxe
   !ipxe
   set initiator-iqn <iscsi_initiator_base>:\${hostname}
   sanboot --keep iscsi:<iscsi_network_subnet>.1::::<iscsi_target_base>:\${hostname}
   EOF
   ```

   where:

   `<iscsi_initiator_base>`
   :   Specifies the iSCSI initiator name on the host that is booting the ISO. This name can also be used by the iSCSI target.

   `<iscsi_network_subnet>`
   :   Specifies the IP address of the iSCSI target.

   `<iscsi_target_base>`
   :   Specifies the iSCSI target name. This name can be the same as the initiator name.

   **Example Command**

   ```
   $ cat << EOF > agent.ipxe
   !ipxe
   set initiator-iqn iqn.2023-01.com.example:\${hostname}
   sanboot --keep iscsi:192.168.45.1::::iqn.2023-01.com.example:\${hostname}
   EOF
   ```

## [Chapter 8. Preparing an Agent-based installed cluster for the multicluster engine for Kubernetes Operator](#preparing-an-agent-based-installed-cluster-for-mce) Copy linkLink copied to clipboard!

You can install the multicluster engine Operator and deploy a hub cluster with the Agent-based Installer.

The following procedure is partially automated and requires manual steps after the initial cluster is deployed.

### [8.1. Prerequisites](#prerequisites_preparing-an-agent-based-installed-cluster-for-mce) Copy linkLink copied to clipboard!

Before installing the multicluster engine Operator and deploying a hub cluster with the Agent-based Installer, you must complete several prerequisites.

The following prerequisites must be completed:

* You have read the following documentation:

  + "Cluster lifecycle with multicluster engine operator overview"
  + "Persistent storage using local volumes"
  + "Using GitOps ZTP to provision clusters at the network far edge"
  + "Preparing to install with the Agent-based Installer"
  + "About disconnected installation mirroring"
* You have access to the internet to obtain the necessary container images.
* You have installed the OpenShift CLI (`oc`).
* If you are installing in a disconnected environment, you must have a configured local mirror registry for disconnected installation mirroring.

### [8.2. Preparing an Agent-based cluster deployment for the multicluster engine for Kubernetes Operator while disconnected](#preparing-an-initial-cluster-deployment-for-mce-disconnected_preparing-an-agent-based-installed-cluster-for-mce) Copy linkLink copied to clipboard!

You can mirror the required OpenShift Container Platform container images, the multicluster engine Operator, and the Local Storage Operator (LSO) into your local mirror registry in a disconnected environment. Ensure that you note the local DNS hostname and port of your mirror registry.

Note

To mirror your OpenShift Container Platform image repository to your mirror registry, you can use either the `oc adm release image` or `oc mirror` command. In this procedure, the `oc mirror` command is used as an example.

**Procedure**

1. Create an `<assets_directory>` folder to contain valid `install-config.yaml` and `agent-config.yaml` files. This directory is used to store all the assets.
2. To mirror an OpenShift Container Platform image repository, the multicluster engine, and the LSO, create a `ImageSetConfiguration.yaml` file with the following settings:

   **Example `ImageSetConfiguration.yaml`**

   ```
     kind: ImageSetConfiguration
     apiVersion: mirror.openshift.io/v1alpha2
     archiveSize: 4
     storageConfig:
       imageURL: <your-local-registry-dns-name>:<your-local-registry-port>/mirror/oc-mirror-metadata
       skipTLS: true
     mirror:
       platform:
         architectures:
           - "amd64"
         channels:
           - name: stable-4.22
             type: ocp
       additionalImages:
         - name: registry.redhat.io/ubi9/ubi:latest
       operators:
         - catalog: registry.redhat.io/redhat/redhat-operator-index:v4.22
           packages:
             - name: multicluster-engine
             - name: local-storage-operator
   ```

   where:

   `archiveSize`
   :   Specifies the maximum size, in GiB, of each file within the image set.

   `storageConfig`
   :   Specifies the back-end location to receive the image set metadata. This location can be a registry or local directory. It is required to specify `storageConfig` values.

   `storageConfig.imageURL`
   :   Specifies the registry URL for the storage backend.

   `channels.name`
   :   Specifies the channel that contains the OpenShift Container Platform images for the version you are installing.

   `operators.catalog`
   :   Specifies the Operator catalog that contains the OpenShift Container Platform images that you are installing.

   `packages`
   :   Specifies only certain Operator packages and channels to include in the image set. Remove this field to retrieve all packages in the catalog. In this example, a `package.name` value of `multicluster-engine` includes the multicluster engine packages and channels, and `local-storage-operator` includes the LSO packages and channels.

       Note

       This file is required by the `oc mirror` command when mirroring content.
3. To mirror a specific OpenShift Container Platform image repository, the multicluster engine, and the LSO, run the following command:

   ```
   $ oc mirror --dest-skip-tls --config ocp-mce-imageset.yaml docker://<your-local-registry-dns-name>:<your-local-registry-port>
   ```
4. Update the registry and certificate in the `install-config.yaml` file:

   **Example `imageContentSources.yaml`**

   ```
     imageContentSources:
       - source: "quay.io/openshift-release-dev/ocp-release"
         mirrors:
           - "<your-local-registry-dns-name>:<your-local-registry-port>/openshift/release-images"
       - source: "quay.io/openshift-release-dev/ocp-v4.0-art-dev"
         mirrors:
           - "<your-local-registry-dns-name>:<your-local-registry-port>/openshift/release"
       - source: "registry.redhat.io/ubi9"
         mirrors:
           - "<your-local-registry-dns-name>:<your-local-registry-port>/ubi9"
       - source: "registry.redhat.io/multicluster-engine"
         mirrors:
           - "<your-local-registry-dns-name>:<your-local-registry-port>/multicluster-engine"
       - source: "registry.redhat.io/rhel8"
         mirrors:
           - "<your-local-registry-dns-name>:<your-local-registry-port>/rhel8"
       - source: "registry.redhat.io/redhat"
         mirrors:
           - "<your-local-registry-dns-name>:<your-local-registry-port>/redhat"
   ```

   Additionally, ensure your certificate is present in the `additionalTrustBundle` field of the `install-config.yaml`.

   **Example `install-config.yaml`**

   ```
   additionalTrustBundle: |
     -----BEGIN CERTIFICATE-----
     zzzzzzzzzzz
     -----END CERTIFICATE-------
   ```

   Important

   The `oc mirror` command creates a folder called `oc-mirror-workspace` with several outputs. This includes the `imageContentSourcePolicy.yaml` file that identifies all the mirrors you need for OpenShift Container Platform and your selected Operators.
5. Generate the cluster manifests by running the following command:

   ```
   $ openshift-install agent create cluster-manifests
   ```

   This command updates the cluster manifests folder to include a `mirror` folder that contains your mirror configuration.

### [8.3. Preparing an Agent-based cluster deployment for the multicluster engine for Kubernetes Operator while connected](#preparing-an-initial-cluster-deployment-for-mce-connected_preparing-an-agent-based-installed-cluster-for-mce) Copy linkLink copied to clipboard!

Create the required manifests for the multicluster engine Operator, the Local Storage Operator (LSO), and to deploy an agent-based OpenShift Container Platform cluster as a hub cluster.

**Procedure**

1. Create a sub-folder named `openshift` in the `<assets_directory>` folder. This sub-folder is used to store the extra manifests that will be applied during the installation to further customize the deployed cluster. The `<assets_directory>` folder contains all the assets including the `install-config.yaml` and `agent-config.yaml` files.

   Note

   The installer does not validate extra manifests.
2. For the multicluster engine, create the following manifests and save them in the `<assets_directory>/openshift` folder:

   **Example `mce_namespace.yaml`**

   ```
     apiVersion: v1
     kind: Namespace
     metadata:
       labels:
         openshift.io/cluster-monitoring: "true"
       name: multicluster-engine
   ```

   **Example `mce_operatorgroup.yaml`**

   ```
     apiVersion: operators.coreos.com/v1
     kind: OperatorGroup
     metadata:
       name: multicluster-engine-operatorgroup
       namespace: multicluster-engine
     spec:
       targetNamespaces:
       - multicluster-engine
   ```

   **Example `mce_subscription.yaml`**

   ```
     apiVersion: operators.coreos.com/v1alpha1
     kind: Subscription
     metadata:
       name: multicluster-engine
       namespace: multicluster-engine
     spec:
       channel: "stable-2.3"
       name: multicluster-engine
       source: redhat-operators
       sourceNamespace: openshift-marketplace
   ```

   Note

   You can install a distributed unit (DU) at scale with the Red Hat Advanced Cluster Management (RHACM) using the assisted installer (AI). These distributed units must be enabled in the hub cluster. The AI service requires persistent volumes (PVs), which are manually created.
3. For the AI service, create the following manifests and save them in the `<assets_directory>/openshift` folder:

   **Example `lso_namespace.yaml`**

   ```
     apiVersion: v1
     kind: Namespace
     metadata:
       annotations:
         openshift.io/cluster-monitoring: "true"
       name: openshift-local-storage
   ```

   **Example `lso_operatorgroup.yaml`**

   ```
     apiVersion: operators.coreos.com/v1
     kind: OperatorGroup
     metadata:
       name: local-operator-group
       namespace: openshift-local-storage
     spec:
       targetNamespaces:
         - openshift-local-storage
   ```

   **Example `lso_subscription.yaml`**

   ```
     apiVersion: operators.coreos.com/v1alpha1
     kind: Subscription
     metadata:
       name: local-storage-operator
       namespace: openshift-local-storage
     spec:
       installPlanApproval: Automatic
       name: local-storage-operator
       source: redhat-operators
       sourceNamespace: openshift-marketplace
   ```

   Note

   After creating all the manifests, your filesystem must display as follows:

   **Example Filesystem**

   ```
   <assets_directory>
       ├─ install-config.yaml
       ├─ agent-config.yaml
       └─ /openshift
           ├─ mce_namespace.yaml
           ├─ mce_operatorgroup.yaml
           ├─ mce_subscription.yaml
           ├─ lso_namespace.yaml
           ├─ lso_operatorgroup.yaml
           └─ lso_subscription.yaml
   ```
4. Create the agent ISO image by running the following command:

   ```
   $ openshift-install agent create image --dir <assets_directory>
   ```
5. When the image is ready, boot the target machine and wait for the installation to complete.
6. To monitor the installation, run the following command:

   ```
   $ openshift-install agent wait-for install-complete --dir <assets_directory>
   ```

   Note

   To configure a fully functional hub cluster, you must create the following manifests and manually apply them by running the command `$ oc apply -f <manifest-name>`. The order of the manifest creation is important and where required, the waiting condition is displayed.
7. For the PVs that are required by the AI service, create the following manifests:

   ```
     apiVersion: local.storage.openshift.io/v1
     kind: LocalVolume
     metadata:
      name: assisted-service
      namespace: openshift-local-storage
     spec:
      logLevel: Normal
      managementState: Managed
      storageClassDevices:
        - devicePaths:
            - /dev/vda
            - /dev/vdb
          storageClassName: assisted-service
          volumeMode: Filesystem
   ```
8. Use the following command to wait for the availability of the PVs, before applying the subsequent manifests:

   ```
   $ oc wait localvolume -n openshift-local-storage assisted-service --for condition=Available --timeout 10m
   ```

   Note

   ```
   The `devicePath` is an example and may vary depending on the actual hardware configuration used.
   ```
9. Create a manifest for a multicluster engine instance.

   **Example `MultiClusterEngine.yaml`**

   ```
     apiVersion: multicluster.openshift.io/v1
     kind: MultiClusterEngine
     metadata:
       name: multiclusterengine
     spec: {}
   ```
10. Create a manifest to enable the AI service.

    **Example `agentserviceconfig.yaml`**

    ```
      apiVersion: agent-install.openshift.io/v1beta1
      kind: AgentServiceConfig
      metadata:
        name: agent
        namespace: assisted-installer
      spec:
       databaseStorage:
        storageClassName: assisted-service
        accessModes:
        - ReadWriteOnce
        resources:
         requests:
          storage: 10Gi
       filesystemStorage:
        storageClassName: assisted-service
        accessModes:
        - ReadWriteOnce
        resources:
         requests:
          storage: 10Gi
    ```
11. Create a manifest to deploy subsequently spoke clusters.

    **Example `clusterimageset.yaml`**

    ```
      apiVersion: hive.openshift.io/v1
      kind: ClusterImageSet
      metadata:
        name: "4.22"
      spec:
        releaseImage: quay.io/openshift-release-dev/ocp-release:4.22.0-x86_64
    ```
12. Create a manifest to import the agent installed cluster (that hosts the multicluster engine and the Assisted Service) as the hub cluster.

    **Example `autoimport.yaml`**

    ```
      apiVersion: cluster.open-cluster-management.io/v1
      kind: ManagedCluster
      metadata:
       labels:
         local-cluster: "true"
         cloud: auto-detect
         vendor: auto-detect
       name: local-cluster
      spec:
       hubAcceptsClient: true
    ```
13. Wait for the managed cluster to be created.

    ```
    $ oc wait -n multicluster-engine managedclusters local-cluster --for condition=ManagedClusterJoined=True --timeout 10m
    ```

**Verification**

* To confirm that the managed cluster installation is successful, run the following command:

  ```
  $ oc get managedcluster
  NAME            HUB ACCEPTED   MANAGED CLUSTER URLS             JOINED   AVAILABLE  AGE
  local-cluster   true           https://<your cluster url>:6443   True     True       77m
  ```

## [Chapter 9. Installation configuration parameters for the Agent-based Installer](#installation-config-parameters-agent) Copy linkLink copied to clipboard!

Before you deploy an OpenShift Container Platform cluster using the Agent-based Installer, you provide parameters to customize your cluster and the platform that hosts it.

When you create the `install-config.yaml` and `agent-config.yaml` files, you must provide values for the required parameters, and you can use the optional parameters to customize your cluster further.

### [9.1. Available installation configuration parameters](#installation-configuration-parameters_installation-config-parameters-agent) Copy linkLink copied to clipboard!

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file.

The following tables specify the required and optional installation configuration parameters that you can set as part of the Agent-based installation process.

These values are specified in the `install-config.yaml` file.

Important

These settings are used for installation only, and cannot be changed after installation.

#### [9.1.1. Required configuration parameters](#installation-configuration-parameters-required_installation-config-parameters-agent) Copy linkLink copied to clipboard!

Required installation configuration parameters are described in the following table:

Expand

Table 9.1. Required parameters

| Parameter | Description |
| --- | --- |
| ``` apiVersion: ``` | The API version for the `install-config.yaml` content. The current version is `v1`. The installation program might also support older API versions.  **Value:** String |
| ``` baseDomain: ``` | The base domain of your cloud provider. The base domain is used to create routes to your OpenShift Container Platform cluster components. The full DNS name for your cluster is a combination of the `baseDomain` and `metadata.name` parameter values that uses the `<metadata.name>.<baseDomain>` format.  **Value:** A fully-qualified domain or subdomain name, such as `example.com`. |
| ``` metadata: ``` | Kubernetes resource `ObjectMeta`, from which only the `name` parameter is consumed.  **Value:** Object |
| ``` metadata:   name: ``` | The name of the cluster. DNS records for the cluster are all subdomains of `{{.metadata.name}}.{{.baseDomain}}`. The cluster name is set to `agent-cluster` when you do not provide the `metadata.name` parameter through either the `install-config.yaml` or `agent-config.yaml` files. For example, installations that only use ZTP manifests do not provide the `metadata.name` parameter.  **Value:** String of lowercase letters, hyphens (`-`), and periods (`.`), such as `dev`. |
| ``` platform: ``` | The configuration for the specific platform upon which to perform the installation: `baremetal`, `external`, `none`, `vsphere`, or `nutanix`.  **Value:** Object |
| ``` pullSecret: ``` | Get a [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) to authenticate downloading container images for OpenShift Container Platform components from services such as Quay.io.  **Value:**  ``` {    "auths":{       "cloud.openshift.com":{          "auth":"b3Blb=",          "email":"you@example.com"       },       "quay.io":{          "auth":"b3Blb=",          "email":"you@example.com"       }    } } ``` |

Show more

#### [9.1.2. Network configuration parameters](#installation-configuration-parameters-network_installation-config-parameters-agent) Copy linkLink copied to clipboard!

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

Table 9.2. Network parameters

| Parameter | Description |
| --- | --- |
| ``` networking: ``` | The configuration for the cluster network.  **Value:** Object  Note  You cannot change parameters specified by the `networking` object after installation. |
| ``` networking:   networkType: ``` | The Red Hat OpenShift Networking network plugin to install.  **Value:**`OVNKubernetes`. `OVNKubernetes` is a Container Network Interface (CNI) plugin for Linux networks and hybrid networks that contain both Linux and Windows servers. The default value is `OVNKubernetes`. |
| ``` networking:   clusterNetwork: ``` | The IP address blocks for pods.  The default value is `10.128.0.0/14` with a host prefix of `/23`.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  ``` networking:   clusterNetwork:   - cidr: 10.128.0.0/14     hostPrefix: 23   - cidr: fd01::/48     hostPrefix: 64 ``` |
| ``` networking:   clusterNetwork:     cidr: ``` | Required if you use `networking.clusterNetwork`. An IP address block.  If you use the OVN-Kubernetes network plugin, you can specify IPv4 and IPv6 networks.  **Value:** An IP address block in Classless Inter-Domain Routing (CIDR) notation. The prefix length for an IPv4 block is between `0` and `32`. The prefix length for an IPv6 block is between `0` and `128`. For example, `10.128.0.0/14` or `fd01::/48`. |
| ``` networking:   clusterNetwork:     hostPrefix: ``` | The subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23` then each node is assigned a `/23` subnet out of the given `cidr`. A `hostPrefix` value of `23` provides 510 (2^(32 - 23) - 2) pod IP addresses.  **Value:** A subnet prefix.  For an IPv4 network the default value is `23`. For an IPv6 network `hostPrefix` must be set to `64`, which is the default value. |
| ``` networking:   serviceNetwork: ``` | The IP address block for services. The default value is `172.30.0.0/16`.  If you use the OVN-Kubernetes network plugin, you can specify an IP address block for both of the IPv4 and IPv6 address families.  **Value:** An array with an IP address block in CIDR format. For example:  ``` networking:   serviceNetwork:    - 172.30.0.0/16    - fd02::/112 ``` |
| ``` networking:   machineNetwork: ``` | The IP address blocks for machines.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  ``` networking:   machineNetwork:   - cidr: 10.0.0.0/16 ``` |
| ``` networking:   machineNetwork:     cidr: ``` | Required if you use `networking.machineNetwork`. An IP address block. The default value is `10.0.0.0/16` for all platforms other than libvirt and IBM Power® Virtual Server. For libvirt, the default value is `192.168.126.0/24`. For IBM Power® Virtual Server, the default value is `192.168.0.0/24`.  **Value:** An IP network block in CIDR notation.  For example, `10.0.0.0/16` or `fd00::/48`.  Note  Set the `networking.machineNetwork` to match the CIDR of the preferred NIC.  If you are installing a cluster on AWS with dual-stack networking, consider the following distinction:  * If the installation program creates the VPC, do not specify an IPv6 entry in `networking.machineNetwork`. The installation program will assign an IPv6 address to the VPC. * If you provide existing dual-stack subnets using the `platform.aws.vpc.subnets` parameter, you must specify IPv6 entries corresponding to either the VPC CIDR or the CIDR of the subnets. * In both cases, you must provide an IPv4 CIDR entry. |
| ``` networking:   ovnKubernetesConfig:     ipv4:       internalJoinSubnet: ``` | Configures the IPv4 join subnet that is used internally by `ovn-kubernetes`. This subnet must not overlap with any other subnet that OpenShift Container Platform is using, including the node network. The size of the subnet must be larger than the number of nodes. You cannot change the value after installation.  **Value:** An IP network block in CIDR notation. The default value is `100.64.0.0/16`. |

Show more

#### [9.1.3. Optional configuration parameters](#installation-configuration-parameters-optional_installation-config-parameters-agent) Copy linkLink copied to clipboard!

Optional installation configuration parameters are described in the following table:

Expand

Table 9.3. Optional parameters

| Parameter | Description |
| --- | --- |
| ``` additionalTrustBundle: ``` | A PEM-encoded X.509 certificate bundle that is added to the nodes' trusted certificate store. This trust bundle might also be used when a proxy has been configured.  **Value:** String |
| ``` capabilities: ``` | Controls the installation of optional core cluster components. You can reduce the footprint of your OpenShift Container Platform cluster by disabling optional components. For more information, see the "Cluster capabilities" page in *Installing*.  **Value:** String array |
| ``` capabilities:   baselineCapabilitySet: ``` | Selects an initial set of optional capabilities to enable. Valid values are `None`, `v4.11`, `v4.12` and `vCurrent`. The default value is `vCurrent`.  **Value:** String |
| ``` capabilities:   additionalEnabledCapabilities: ``` | Extends the set of optional capabilities beyond what you specify in `baselineCapabilitySet`. You can specify multiple capabilities in this parameter.  **Value:** String array |
| ``` cpuPartitioningMode: ``` | Enables workload partitioning, which isolates OpenShift Container Platform services, cluster management workloads, and infrastructure pods to run on a reserved set of CPUs. You can only enable workload partitioning during installation. You cannot disable it after installation. While this field enables workload partitioning, it does not configure workloads to use specific CPUs. For more information, see the *Workload partitioning* page in the *Scalability and Performance* section.  **Value:** `None` or `AllNodes`. `None` is the default value. |
| ``` compute: ``` | The configuration for the machines that comprise the compute nodes.  **Value:** Array of `MachinePool` objects. |
| ``` compute:   architecture: ``` | Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`.  **Value:** String |
| ``` compute:   hyperthreading: ``` | Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on compute machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important  If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled` |
| ``` compute:   name: ``` | Required if you use `compute`. The name of the machine pool.  **Value:** `worker` |
| ``` compute:   platform: ``` | Required if you use `compute`. Use this parameter to specify the cloud provider to host the worker machines. This parameter value must match the `controlPlane.platform` parameter value.  **Value:**`baremetal`, `vsphere`, or `{}` |
| ``` compute:   replicas: ``` | The number of compute machines, which are also known as worker machines, to provision.  **Value:** A positive integer greater than or equal to `2`. The default value is `3`. |
| ``` featureSet: ``` | Enables the cluster for a feature set. A feature set is a collection of OpenShift Container Platform features that are not enabled by default. For more information about enabling a feature set during installation, see "Enabling features using feature gates".  **Value:** String. The name of the feature set to enable, such as `TechPreviewNoUpgrade`. |
| ``` controlPlane: ``` | The configuration for the machines that form the control plane.  **Value:** Array of `MachinePool` objects. |
| ``` controlPlane:   architecture: ``` | Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are `amd64`, `arm64`, `ppc64le`, and `s390x`.  **Value:** String |
| ``` controlPlane:   hyperthreading: ``` | Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on control plane machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important  If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled` |
| ``` controlPlane:   name: ``` | Required if you use `controlPlane`. The name of the machine pool.  **Value:** `master` |
| ``` controlPlane:   platform: ``` | Required if you use `controlPlane`. Use this parameter to specify the cloud provider that hosts the control plane machines. This parameter value must match the `compute.platform` parameter value.  **Value:**`baremetal`, `vsphere`, or `{}` |
| ``` controlPlane:   replicas: ``` | The number of control plane machines to provision.  **Value:** Supported values are `3`, `4`, `5`, or `1` when deploying single-node OpenShift. |
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

#### [9.1.4. Additional bare metal configuration parameters for the Agent-based Installer](#installation-configuration-parameters-additional-bare_installation-config-parameters-agent) Copy linkLink copied to clipboard!

Additional bare metal installation configuration parameters for the Agent-based Installer are described in the following table:

Note

These fields are not used during the initial provisioning of the cluster, but they are available to use once the cluster has been installed. Configuring these fields at install time eliminates the need to set them as a Day 2 operation.

Expand

Table 9.4. Additional bare metal parameters

| Parameter | Description |
| --- | --- |
| ``` platform:   baremetal:     clusterProvisioningIP: ``` | The IP address within the cluster where the provisioning services run. Defaults to the third IP address of the provisioning subnet. For example, `172.22.0.3` or `2620:52:0:1307::3`.  **Value:** IPv4 or IPv6 address. |
| ``` platform:   baremetal:     provisioningNetwork: ``` | The `provisioningNetwork` configuration setting determines whether the cluster uses the provisioning network. If it does, the configuration setting also determines if the cluster manages the network.  `Managed`: Default. Set this parameter to `Managed` to fully manage the provisioning network, including DHCP, TFTP, and so on.  `Disabled`: Set this parameter to `Disabled` to disable the requirement for a provisioning network. When set to `Disabled`, you can use only virtual media based provisioning on Day 2. If `Disabled` and using power management, BMCs must be accessible from the bare-metal network. If Disabled, you must provide two IP addresses on the bare-metal network that are used for the provisioning services.  **Value:** `Managed` or `Disabled`. |
| ``` platform:   baremetal:     provisioningMACAddress: ``` | The MAC address within the cluster where provisioning services run.  **Value:** MAC address. |
| ``` platform:   baremetal:     provisioningNetworkCIDR: ``` | The CIDR for the network to use for provisioning. This option is required when not using the default address range on the provisioning network.  **Value:** Valid CIDR, for example `10.0.0.0/16`. |
| ``` platform:   baremetal:     provisioningNetworkInterface: ``` | The name of the network interface on nodes connected to the provisioning network. Use the `bootMACAddress` configuration setting to enable Ironic to identify the IP address of the NIC instead of using the `provisioningNetworkInterface` configuration setting to identify the name of the NIC.  **Value:** String. |
| ``` platform:   baremetal:     provisioningDHCPRange: ``` | Defines the IP range for nodes on the provisioning network, for example `172.22.0.10,172.22.0.254`.  **Value:** IP address range. |
| ``` platform:   baremetal:     hosts: ``` | Configuration for bare metal hosts.  **Value:** Array of host configuration objects. |
| ``` platform:   baremetal:     hosts:       name: ``` | The name of the host.  **Value:** String. |
| ``` platform:   baremetal:     hosts:       bootMACAddress: ``` | The MAC address of the NIC used for provisioning the host.  **Value:** MAC address. |
| ``` platform:   baremetal:     hosts:       bmc: ``` | Configuration for the host to connect to the baseboard management controller (BMC).  **Value:** Dictionary of BMC configuration objects. |
| ``` platform:   baremetal:     hosts:       bmc:         username: ``` | The username for the BMC.  **Value:** String. |
| ``` platform:   baremetal:     hosts:       bmc:         password: ``` | Password for the BMC.  **Value:** String. |
| ``` platform:   baremetal:     hosts:       bmc:         address: ``` | The URL for communicating with the host’s BMC controller. The address configuration setting specifies the protocol. For example, `redfish+http://10.10.10.1:8000/redfish/v1/Systems/1234` enables Redfish. For more information, see "BMC addressing" in the "Deploying installer-provisioned clusters on bare metal" section.  **Value:** URL. |
| ``` platform:   baremetal:     hosts:       bmc:         disableCertificateVerification: ``` | `redfish` and `redfish-virtualmedia` need this parameter to manage BMC addresses. The value should be `True` when using a self-signed certificate for BMC addresses.  **Value:** Boolean. |

Show more

#### [9.1.5. Additional VMware vSphere configuration parameters](#installation-configuration-parameters-additional-vsphere_installation-config-parameters-agent) Copy linkLink copied to clipboard!

Additional VMware vSphere configuration parameters are described in the following table:

Expand

Table 9.5. Additional VMware vSphere cluster parameters

| Parameter | Description |
| --- | --- |
| ``` platform:   vsphere: ``` | Describes your account on the cloud platform that hosts your cluster. You can use the parameter to customize the platform. If you provide additional configuration settings for compute and control plane machines in the machine pool, the parameter is not required.  **Value:** A dictionary of vSphere configuration objects |
| ``` platform:   vsphere:     failureDomains: ``` | Establishes the relationships between a region and zone. You define a failure domain by using vCenter objects, such as a `datastore` object. A failure domain defines the vCenter location for OpenShift Container Platform cluster nodes.  **Value:** An array of failure domain configuration objects. |
| ``` platform:   vsphere:     failureDomains:       name: ``` | The name of the failure domain.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       region: ``` | If you define multiple failure domains for your cluster, you must attach the tag to each vCenter data center. To define a region, use a tag from the `openshift-region` tag category. For a single vSphere data center environment, you do not need to attach a tag, but you must enter an alphanumeric value, such as `datacenter`, for the parameter. If you want to base your failure domains on host groups, attach these tags to your vSphere clusters instead of your data centers.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       regionType: ``` | Specifies the `ComputeCluster` region type to enable host groups.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       server: ``` | Specifies the fully-qualified hostname or IP address of the VMware vCenter server, so that a client can access failure domain resources. You must apply the `server` role to the vSphere vCenter server location.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       zone: ``` | If you define multiple failure domains for your cluster, you must attach a tag to each vCenter cluster. To define a zone, use a tag from the `openshift-zone` tag category. For a single vSphere data center environment, you do not need to attach a tag, but you must enter an alphanumeric value, such as `cluster`, for the parameter. If you want to base your failure domains on host groups, define zones that correspond to your host groups instead of your clusters. Use these tags to associate each ESXi host with its host group.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       zoneType: ``` | Specifies the `HostGroup` zone type to enable host groups.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       topology:         computeCluster: ``` | The path to the vSphere compute cluster.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       topology:         datacenter: ``` | Lists and defines the data centers where OpenShift Container Platform virtual machines (VMs) operate. The list of data centers must match the list of data centers specified in the `vcenters` field.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       topology:         datastore: ``` | The path to the vSphere datastore that holds virtual machine files, templates, and ISO images.  Important  You can specify the path of any datastore that exists in a datastore cluster. By default, Storage vMotion is automatically enabled for a datastore cluster. Red Hat does not support Storage vMotion, so you must disable Storage vMotion to avoid data loss issues for your OpenShift Container Platform cluster.  If you must specify VMs across multiple datastores, use a `datastore` object to specify a failure domain in your cluster’s `install-config.yaml` configuration file. For more information, see "VMware vSphere region and zone enablement".  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       topology:         folder: ``` | Optional: The absolute path of an existing folder where the user creates the virtual machines, for example, `/<data_center_name>/vm/<folder_name>/<subfolder_name>`.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       topology:         hostGroup: ``` | Specifies the vSphere host group to associate with the failure domain.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       topology:         networks: ``` | Lists any network in the vCenter instance that contains the virtual IP addresses and DNS records that you configured.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       topology:         resourcePool: ``` | Optional: The absolute path of an existing resource pool where the installation program creates the virtual machines, for example, `/<data_center_name>/host/<cluster_name>/Resources/<resource_pool_name>/<optional_nested_resource_pool_name>`.  **Value:** String |
| ``` platform:   vsphere:     failureDomains:       topology:         tagIDs: ``` | Optional: Specifies the ID of the tag to be associated by the installation program. Each VM created by OpenShift Container Platform is assigned a unique tag that is specific to the cluster. The assigned tag enables the installation program to identify and remove the associated VMs when a cluster is decommissioned. You can list up to ten additional tag IDs to be attached to the VMs provisioned by the installation program. For more information about determining the tag ID, see the [vSphere Tags and Attributes documentation](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-E8E854DD-AA97-4E0C-8419-CE84F93C4058.html).  **Value:** String, for example `urn:vmomi:InventoryServiceTag:208e713c-cae3-4b7f-918e-4051ca7d1f97:GLOBAL`. |
| ``` platform:   vsphere:     failureDomains:       topology:         template: ``` | Specifies the absolute path to a pre-existing Red Hat Enterprise Linux CoreOS (RHCOS) image template or virtual machine. The installation program can use the image template or virtual machine to quickly install RHCOS on vSphere hosts. Consider using this parameter as an alternative to uploading an RHCOS image on vSphere hosts. This parameter is available for use only on installer-provisioned infrastructure.  **Value:** String |
| ``` platform:   vsphere:     vcenters: ``` | Configures the connection details so that services can communicate with a vCenter server.  **Value:** An array of vCenter configuration objects. |
| ``` platform:   vsphere:     vcenters:       datacenters: ``` | Lists and defines the data centers where OpenShift Container Platform virtual machines (VMs) operate. The list of data centers must match the list of data centers specified in the `failureDomains` field.  **Value:** String |
| ``` platform:   vsphere:     vcenters:       password: ``` | The password associated with the vSphere user.  **Value:** String |
| ``` platform:   vsphere:     vcenters:       port: ``` | The port number used to communicate with the vCenter server.  **Value:** Integer |
| ``` platform:   vsphere:     vcenters:       server: ``` | The fully qualified host name (FQHN) or IP address of the vCenter server.  **Value:** String |
| ``` platform:   vsphere:     vcenters:       user: ``` | The username associated with the vSphere user.  **Value:** String |

Show more

#### [9.1.6. Deprecated VMware vSphere configuration parameters](#deprecated-parameters-vsphere_installation-config-parameters-agent) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.13, the following vSphere configuration parameters are deprecated. You can continue to use these parameters, but the installation program does not automatically specify these parameters in the `install-config.yaml` file.

The following table lists each deprecated vSphere configuration parameter:

Expand

Table 9.6. Deprecated VMware vSphere cluster parameters

| Parameter | Description |
| --- | --- |
| ``` platform:   vsphere:     cluster: ``` | The vCenter cluster to install the OpenShift Container Platform cluster in.  **Value:** String |
| ``` platform:   vsphere:     datacenter: ``` | Defines the data center where OpenShift Container Platform virtual machines (VMs) operate.  **Value:** String |
| ``` platform:   vsphere:     defaultDatastore: ``` | The name of the default datastore to use for provisioning volumes.  **Value:** String |
| ``` platform:   vsphere:     folder: ``` | Optional: The absolute path of an existing folder where the installation program creates the virtual machines. If you do not provide this value, the installation program creates a folder that is named with the infrastructure ID in the data center virtual machine folder.  **Value:** String, for example, `/<data_center_name>/vm/<folder_name>/<subfolder_name>`. |
| ``` platform:   vsphere:     password: ``` | The password for the vCenter user name.  **Value:** String |
| ``` platform:   vsphere:     resourcePool: ``` | Optional: The absolute path of an existing resource pool where the installation program creates the virtual machines. If you do not specify a value, the installation program installs the resources in the root of the cluster under `/<data_center_name>/host/<cluster_name>/Resources`.  **Value:** String, for example, `/<data_center_name>/host/<cluster_name>/Resources/<resource_pool_name>/<optional_nested_resource_pool_name>`. |
| ``` platform:   vsphere:     username: ``` | The user name to use to connect to the vCenter instance with. This user must have at least the roles and privileges that are required for [static or dynamic persistent volume provisioning](https://github.com/vmware-archive/vsphere-storage-for-kubernetes/blob/master/documentation/vcp-roles.md) in vSphere.  **Value:** String |
| ``` platform:   vsphere:     vCenter: ``` | The fully-qualified hostname or IP address of a vCenter server.  **Value:** String |

Show more

### [9.2. Available Agent configuration parameters](#agent-configuration-parameters_installation-config-parameters-agent) Copy linkLink copied to clipboard!

To customize your cluster installation, configuration parameters are available to use in the `agent-config.yaml` file.

The following tables specify the required and optional Agent configuration parameters that you can set as part of the Agent-based installation process.

Note

These settings are used for installation only, and cannot be modified after installation.

#### [9.2.1. Required configuration parameters](#agent-configuration-parameters-required_installation-config-parameters-agent) Copy linkLink copied to clipboard!

Required Agent configuration parameters are described in the following table:

Expand

Table 9.7. Required parameters

| Parameter | Description |
| --- | --- |
| ``` apiVersion: ``` | The API version for the `agent-config.yaml` content. The current version is `v1beta1`. The installation program might also support older API versions.  **Value:** String |
| ``` metadata: ``` | Kubernetes resource `ObjectMeta`, from which only the `name` parameter is consumed.  **Value:** Object |
| ``` metadata:   name: ``` | The name of the cluster. DNS records for the cluster are all subdomains of `{{.metadata.name}}.{{.baseDomain}}`. The value entered in the `agent-config.yaml` file is ignored, and instead the value specified in the `install-config.yaml` file is used. When you do not provide `metadata.name` through either the `install-config.yaml` or `agent-config.yaml` files, for example when you use only ZTP manifests, the cluster name is set to `agent-cluster`.  **Value:** String of lowercase letters and hyphens (`-`), such as `dev`. |

Show more

#### [9.2.2. Optional configuration parameters](#agent-configuration-parameters-optional_installation-config-parameters-agent) Copy linkLink copied to clipboard!

Optional Agent configuration parameters are described in the following table:

Expand

Table 9.8. Optional parameters

| Parameter | Description |
| --- | --- |
| ``` rendezvousIP: ``` | The IP address of the node that performs the bootstrapping process as well as running the `assisted-service` component. You must provide the rendezvous IP address when you do not specify at least one host’s IP address in the `networkConfig` parameter. If this address is not provided, one IP address is selected from the provided hosts' `networkConfig`.  **Value:** IPv4 or IPv6 address. |
| ``` bootArtifactsBaseURL: ``` | When you use the Agent-based Installer to generate a minimal ISO image, this parameter specifies a URL where the rootfs image file can be retrieved from during cluster installation. This parameter is optional for booting minimal ISO images in connected environments.  When you use the Agent-based Installer to generate an iPXE script, this parameter specifies the URL of the server to upload Preboot Execution Environment (PXE) assets to. For more information, see "Preparing PXE assets for OpenShift Container Platform".  **Value:** String. |
| ``` additionalNTPSources: ``` | A list of Network Time Protocol (NTP) sources to be added to all cluster hosts, which are added to any NTP sources that are configured through other means.  **Value:** List of hostnames or IP addresses. |
| ``` hosts: ``` | Host configuration. An optional list of hosts. The number of hosts defined must not exceed the total number of hosts defined in the `install-config.yaml` file, which is the sum of the values of the `compute.replicas` and `controlPlane.replicas` parameters.  **Value:** An array of host configuration objects. |
| ``` hosts:   hostname: ``` | Hostname. Overrides the hostname obtained from either the Dynamic Host Configuration Protocol (DHCP) or a reverse DNS lookup. Each host must have a unique hostname supplied by one of these methods, although configuring a hostname through this parameter is optional.  **Value:** String. |
| ``` hosts:   interfaces: ``` | Provides a table of the name and MAC address mappings for the interfaces on the host. If a `NetworkConfig` section is provided in the `agent-config.yaml` file, this table must be included and the values must match the mappings provided in the `NetworkConfig` section.  **Value:** An array of host configuration objects. |
| ``` hosts:   interfaces:     name: ``` | The name of an interface on the host.  Note  This value does not need to match the device name.  **Value:** String. |
| ``` hosts:   interfaces:     macAddress: ``` | The MAC address of an interface on the host.  **Value:** A MAC address such as the following example: `00-B0-D0-63-C2-26`. |
| ``` hosts:   role: ``` | Defines whether the host is a `master` or `worker` node. If no role is defined in the `agent-config.yaml` file, roles will be assigned at random during cluster installation.  **Value:** `master` or `worker`. |
| ``` hosts:   rootDeviceHints: ``` | Enables provisioning of the Red Hat Enterprise Linux CoreOS (RHCOS) image to a particular device. The installation program examines the devices in the order it discovers them, and compares the discovered values with the hint values. It uses the first discovered device that matches the hint value. This is the device that the operating system is written on during installation.  **Value:** A dictionary of key-value pairs. For more information, see "Root device hints" in the "Setting up the environment for an OpenShift installation" page. |
| ``` hosts:   rootDeviceHints:     deviceName: ``` | The name of the device the RHCOS image is provisioned to.  **Value:** String. |
| ``` hosts:   networkConfig: ``` | The host network definition. The configuration must match the Host Network Management API defined in the "Declarative Network API (nmstate documentation)".  **Value:** A dictionary of host network configuration objects. |
| ``` minimalISO: ``` | Defines whether the Agent-based Installer generates a full ISO or a minimal ISO image. When this parameter is set to `True`, the Agent-based Installer generates an ISO without a rootfs image file, and instead contains details about where to pull the rootfs file from.  When you generate a minimal ISO, if you do not specify a rootfs URL through the `bootArtifactsBaseURL` parameter, the Agent-based Installer embeds a default URL that is accessible in environments with an internet connection.  The default value is `False`.  **Value:** Boolean. |

Show more

## [Chapter 10. Postinstallation tasks](#agent-based-installer-postinstallation) Copy linkLink copied to clipboard!

After using the Agent-based Installer to deploy your cluster, you can perform post-installation procedures such as customizing a `br-ex` bridge for nodes in your cluster. Customizing your cluster can help prepare the cluster for specific workloads and deployment requirements.

### [10.1. Creating a manifest object that includes a customized br-ex bridge](#creating-manifest-file-customized-br-ex-bridge-post_agent-based-installer-postinstallation) Copy linkLink copied to clipboard!

Use the default OVS br-ex bridge configuration for standard environments. This configuration applies when you have a single network interface controller (NIC) and standard OVS settings.

By default, OpenShift Container Platform automatically configures the Open vSwitch (OVS) `br-ex` bridge on bare-metal nodes. For advanced networking requirements, you can override this default behavior on bare-metal platforms. To do this, create an `NodeNetworkConfigurationPolicy` (NNCP) custom resource (CR) that includes an NMState configuration file.

The Kubernetes NMState Operator uses the NMState configuration file to create a customized `br-ex` bridge network configuration. This configuration applies to each node in your cluster.

Important

After creating the `NodeNetworkConfigurationPolicy` CR, copy content from the installation NMState configuration file into the NNCP CR. An incomplete NNCP CR can result in loss of network connectivity, because the NNCP overrides all existing policies.

Consider using the customized `br-ex` bridge configuration for any of the following tasks:

* You need to modify the `br-ex` bridge after you installed the cluster.
* You need to modify the maximum transmission unit (MTU) for your cluster.
* You need to update DNS values.
* You need to modify attributes for a different bond interface, such as MIImon (Media Independent Interface Monitor), bonding mode, or Quality of Service (QoS).
* You need to enable Link Layer Discovery Protocol (LLDP) to discover and troubleshoot switch connectivity.

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

**Prerequisites**

* You have installed the Kubernetes NMState Operator.
* You have identified the specific nodes where you want to apply the policy.

**Procedure**

* Create a `NodeNetworkConfigurationPolicy` (NNCP) CR and define a customized `br-ex` bridge network configuration. The `br-ex` NNCP CR must include the OVN-Kubernetes masquerade IP address and subnet of your network. The example NNCP CR includes default values in the `ipv4.address.ip` and `ipv6.address.ip` parameters. You can set the masquerade IP address in the `ipv4.address.ip`, `ipv6.address.ip`, or both parameters.

  Important

  As a post-installation task, you cannot change the primary IP address of the customized `br-ex` bridge. If you want to convert your single-stack cluster network to a dual-stack cluster network, you can add or change a secondary IPv6 address in the NNCP CR, but the existing primary IP address cannot be changed.

  ```
  apiVersion: nmstate.io/v1
  kind: NodeNetworkConfigurationPolicy
  metadata:
    name: worker-0-br-ex
  spec:
    nodeSelector:
      kubernetes.io/hostname: worker-0
    desiredState:
      interfaces:
      - name: enp2s0
        type: ethernet
        state: up
        mtu: 9000
        ipv4:
          enabled: false
        ipv6:
          enabled: false
      - name: br-ex
        type: ovs-bridge
        state: up
        ipv4:
          enabled: false
          dhcp: false
        ipv6:
          enabled: false
          dhcp: false
        bridge:
          options:
            mcast-snooping-enable: true
          port:
          - name: enp2s0
          - name: br-ex
      - name: br-ex
        type: ovs-interface
        state: up
        copy-mac-from: enp2s0
        mtu: 9000
        ipv4:
          enabled: true
          dhcp: true
          auto-route-metric: 48
          address:
          - ip: "169.254.0.2"
            prefix-length: 17
        ipv6:
          enabled: true
          dhcp: true
          auto-route-metric: 48
          address:
          - ip: "fd69::2"
          prefix-length: 112
  # ...
  ```

  where:

  `metadata.name`
  :   Specifies the name of the policy.

  `interfaces.name`
  :   Specifies the name of the interface.

  `interfaces.type`
  :   Specifies the type of ethernet.

  `interfaces.state`
  :   Specifies the requested state for the interface after creation.

  `mtu`
  :   To ensure network stability and performance, you must explicitly declare the MTU in the manifest for every interface. Do not rely on automatic MTU configuration. The MTU configured on a bridge port or VLAN-tagged interface must not exceed the maximum frame size supported by the attached physical medium. A mismatch causes packet fragmentation or connectivity loss.

  `ipv4.enabled`
  :   Disables IPv4 and IPv6 in this example.

  `port.name`
  :   Specifies the node NIC to which the bridge is attached.

  `address.ip`
  :   Shows the default IPv4 and IPv6 IP addresses. Ensure that you set the masquerade IPv4 and IPv6 IP addresses of your network.

  `auto-route-metric`
  :   Set the parameter to `48` to ensure the `br-ex` default route always has the highest precedence (lowest metric). This configuration prevents routing conflicts with any other interfaces automatically configured by the `NetworkManager` service.

**Next steps**

* Scaling compute nodes to apply the manifest object that includes a customized `br-ex` bridge to each compute node that exists in your cluster. For more information, see "Expanding the cluster" in the *Additional resources* section.

## [Legal Notice](#idm140203237577328) Copy linkLink copied to clipboard!

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
