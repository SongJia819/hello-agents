---
title: "Migrating from version 3 to 4"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/migrating_from_version_3_to_4/index
retrieved_at: 2026-09-05T05:42:14.727860+00:00
---

# Migrating from version 3 to 4

---

OpenShift Container Platform 4.22

## Migrating to OpenShift Container Platform 4

Red Hat OpenShift Documentation Team

[Legal Notice](#idm139624436978000)

**Abstract**

This document provides instructions for migrating your OpenShift Container Platform cluster from version 3 to version 4.

---

## [Chapter 1. Migration from OpenShift Container Platform 3 to 4 overview](#migration-from-version-3-to-4-overview) Copy linkLink copied to clipboard!

OpenShift Container Platform 4 clusters are different from OpenShift Container Platform 3 clusters. OpenShift Container Platform 4 clusters contain new technologies and functionality that result in a cluster that is self-managing, flexible, and automated. To learn more about migrating from OpenShift Container Platform 3 to 4 see [About migrating from OpenShift Container Platform 3 to 4](#about-migrating-from-3-to-4 "Chapter 2. About migrating from OpenShift Container Platform 3 to 4").

### [1.1. Differences between OpenShift Container Platform 3 and 4](#mtc-3-to-4-overview-differences-mtc) Copy linkLink copied to clipboard!

Before migrating from OpenShift Container Platform 3 to 4, you can check [differences between OpenShift Container Platform 3 and 4](#planning-migration-3-4 "Chapter 3. Differences between OpenShift Container Platform 3 and 4"). Review the following information:

* [Architecture](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture)
* [Installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation)
* [Storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#index), [network](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_overview/#understanding-networking), [security](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/security_and_compliance/#index), and [monitoring considerations](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/monitoring/#about-ocp-monitoring)

### [1.2. Planning network considerations](#mtc-3-to-4-overview-planning-network-considerations-mtc) Copy linkLink copied to clipboard!

Before migrating from OpenShift Container Platform 3 to 4, review the [differences between OpenShift Container Platform 3 and 4](#planning-migration-3-4 "Chapter 3. Differences between OpenShift Container Platform 3 and 4") for information about the following areas:

* [DNS considerations](#dns-considerations_planning-considerations-3-4 "4.1. DNS considerations")

  + [Isolating the DNS domain of the target cluster from the clients](#migration-isolating-dns-domain-of-target-cluster-from-clients_planning-considerations-3-4 "4.1.1. Isolating the DNS domain of the target cluster from the clients").
  + [Setting up the target cluster to accept the source DNS domain](#migration-setting-up-target-cluster-to-accept-source-dns-domain_planning-considerations-3-4 "4.1.2. Setting up the target cluster to accept the source DNS domain").

## [Chapter 2. About migrating from OpenShift Container Platform 3 to 4](#about-migrating-from-3-to-4) Copy linkLink copied to clipboard!

OpenShift Container Platform 4 contains new technologies and functionality that result in a cluster that is self-managing, flexible, and automated. OpenShift Container Platform 4 clusters are deployed and managed very differently from OpenShift Container Platform 3.

The most effective way to migrate from OpenShift Container Platform 3 to 4 is by using a CI/CD pipeline to automate deployments in an [application lifecycle management](https://www.redhat.com/en/topics/devops/what-is-application-lifecycle-management-alm) framework.

You can use Red Hat Advanced Cluster Management for Kubernetes to help you import and manage your OpenShift Container Platform 3 clusters easily, enforce policies, and redeploy your applications. Take advantage of the [free subscription](https://www.redhat.com/en/engage/free-access-redhat-e-202202170127) to use Red Hat Advanced Cluster Management to simplify your migration process.

To successfully transition to OpenShift Container Platform 4, review the following information:

[Differences between OpenShift Container Platform 3 and 4](#planning-migration-3-4 "Chapter 3. Differences between OpenShift Container Platform 3 and 4")
:   * Architecture
    * Installation and upgrade
    * Storage, network, logging, security, and monitoring considerations

## [Chapter 3. Differences between OpenShift Container Platform 3 and 4](#planning-migration-3-4) Copy linkLink copied to clipboard!

OpenShift Container Platform 4.22 introduces architectural changes and enhancements/ The procedures that you used to manage your OpenShift Container Platform 3 cluster might not apply to OpenShift Container Platform 4.

For information on configuring your OpenShift Container Platform 4 cluster, review the appropriate sections of the OpenShift Container Platform documentation. For information on new features and other notable technical changes, review the [OpenShift Container Platform 4.22 release notes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/release_notes/#ocp-4-21-release-notes).

It is not possible to upgrade your existing OpenShift Container Platform 3 cluster to OpenShift Container Platform 4. You must start with a new OpenShift Container Platform 4 installation. Tools are available to assist in migrating your control plane settings and application workloads.

### [3.1. Architecture](#migration-differences-architecture) Copy linkLink copied to clipboard!

With OpenShift Container Platform 3, administrators individually deployed Red Hat Enterprise Linux (RHEL) hosts, and then installed OpenShift Container Platform on top of these hosts to form a cluster. Administrators were responsible for properly configuring these hosts and performing updates.

OpenShift Container Platform 4 represents a significant change in the way that OpenShift Container Platform clusters are deployed and managed. OpenShift Container Platform 4 includes new technologies and functionality, such as Operators, machine sets, and Red Hat Enterprise Linux CoreOS (RHCOS), which are core to the operation of the cluster. This technology shift enables clusters to self-manage some functions previously performed by administrators. This also ensures platform stability and consistency, and simplifies installation and scaling.

Beginning with OpenShift Container Platform 4.13, RHCOS now uses Red Hat Enterprise Linux (RHEL) 9.2 packages. This enhancement enables the latest fixes and features as well as the latest hardware support and driver updates. For more information about how this upgrade to RHEL 9.2 might affect your options configuration and services as well as driver and container support, see the [RHCOS now uses RHEL 9.2](https://docs.openshift.com/container-platform/4.13/release_notes/ocp-4-13-release-notes.html#ocp-4-13-rhel-9-considerations) in the *OpenShift Container Platform 4.13 release notes*.

For more information, see [OpenShift Container Platform architecture](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture).

#### [3.1.1. Immutable infrastructure](#immutable-infrastructure) Copy linkLink copied to clipboard!

OpenShift Container Platform 4 uses Red Hat Enterprise Linux CoreOS (RHCOS), which is designed to run containerized applications, and provides efficient installation, Operator-based management, and simplified upgrades. RHCOS is an immutable container host, rather than a customizable operating system like RHEL. RHCOS enables OpenShift Container Platform 4 to manage and automate the deployment of the underlying container host. RHCOS is a part of OpenShift Container Platform, which means that everything runs inside a container and is deployed using OpenShift Container Platform.

In OpenShift Container Platform 4, control plane nodes must run RHCOS, ensuring that full-stack automation is maintained for the control plane. This makes rolling out updates and upgrades a much easier process than in OpenShift Container Platform 3.

For more information, see [Red Hat Enterprise Linux CoreOS (RHCOS)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-rhcos).

#### [3.1.2. Operators](#operators) Copy linkLink copied to clipboard!

Operators are a method of packaging, deploying, and managing a Kubernetes application. Operators ease the operational complexity of running another piece of software. They watch over your environment and use the current state to make decisions in real time. Advanced Operators are designed to upgrade and react to failures automatically.

For more information, see [Understanding Operators](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/operators/#olm-what-operators-are).

### [3.2. Installation and upgrade](#migration-differences-install) Copy linkLink copied to clipboard!

#### [3.2.1. Installation process](#installation-process) Copy linkLink copied to clipboard!

To install OpenShift Container Platform 3.11, you prepared your Red Hat Enterprise Linux (RHEL) hosts, set all of the configuration values your cluster needed, and then ran an Ansible playbook to install and set up your cluster.

In OpenShift Container Platform 4.22, you use the OpenShift installation program to create a minimum set of resources required for a cluster. After the cluster is running, you use Operators to further configure your cluster and to install new services. After first boot, Red Hat Enterprise Linux CoreOS (RHCOS) systems are managed by the Machine Config Operator (MCO) that runs in the OpenShift Container Platform cluster.

For more information, see [Installation process](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#installation-process_architecture-installation).

#### [3.2.2. Infrastructure options](#infrastructure-options) Copy linkLink copied to clipboard!

In OpenShift Container Platform 3.11, you installed your cluster on infrastructure that you prepared and maintained. In addition to providing your own infrastructure, OpenShift Container Platform 4 offers an option to deploy a cluster on infrastructure that the OpenShift Container Platform installation program provisions and the cluster maintains.

For more information, see [OpenShift Container Platform installation overview](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#installation-overview_architecture-installation).

#### [3.2.3. Upgrading your cluster](#upgrading-your-cluster) Copy linkLink copied to clipboard!

In OpenShift Container Platform 3.11, you upgraded your cluster by running Ansible playbooks. In OpenShift Container Platform 4.22, the cluster manages its own updates, including updates to Red Hat Enterprise Linux CoreOS (RHCOS) on cluster nodes. You can easily upgrade your cluster by using the web console or by using the `oc adm upgrade` command from the OpenShift CLI and the Operators will automatically upgrade themselves. If your OpenShift Container Platform 4.22 cluster has RHEL worker machines, then you will still need to run an Ansible playbook to upgrade those worker machines.

For more information, see [Updating clusters](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/updating_clusters/#updating-cluster-web-console).

### [3.3. Migration considerations](#migration-considerations) Copy linkLink copied to clipboard!

Review the changes and other considerations that might affect your transition from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.

#### [3.3.1. Storage considerations](#migration-preparing-storage) Copy linkLink copied to clipboard!

Review the following storage changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.22.

##### [3.3.1.1. Local volume persistent storage](#local-volume-persistent-storage) Copy linkLink copied to clipboard!

Local storage is only supported by using the Local Storage Operator in OpenShift Container Platform 4.22. It is not supported to use the local provisioner method from OpenShift Container Platform 3.11.

For more information, see [Persistent storage using local volumes](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-local-volume).

##### [3.3.1.2. FlexVolume persistent storage](#flexvolume-persistent-storage) Copy linkLink copied to clipboard!

The FlexVolume plugin location changed from OpenShift Container Platform 3.11. The new location in OpenShift Container Platform 4.22 is `/etc/kubernetes/kubelet-plugins/volume/exec`. Attachable FlexVolume plugins are no longer supported.

For more information, see [Persistent storage using FlexVolume](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-flexvolume).

##### [3.3.1.3. Container Storage Interface (CSI) persistent storage](#container-storage-interface-csi-persistent-storage) Copy linkLink copied to clipboard!

Persistent storage using the Container Storage Interface (CSI) was [Technology Preview](https://access.redhat.com/support/offerings/techpreview) in OpenShift Container Platform 3.11. OpenShift Container Platform 4.22 includes with [several CSI drivers](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-drivers-supported_persistent-storage-csi). You can also install your own driver.

For more information, see [Persistent storage using the Container Storage Interface (CSI)](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-using-csi).

##### [3.3.1.4. Red Hat OpenShift Data Foundation](#red-hat-openshift-data-foundation) Copy linkLink copied to clipboard!

OpenShift Container Storage 3, which is available for use with OpenShift Container Platform 3.11, uses Red Hat Gluster Storage as the backing storage.

Red Hat OpenShift Data Foundation 4, which is available for use with OpenShift Container Platform 4, uses Red Hat Ceph Storage as the backing storage.

For more information, see [Persistent storage using Red Hat OpenShift Data Foundation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#red-hat-openshift-data-foundation) and the [interoperability matrix](https://access.redhat.com/articles/4731161) article.

##### [3.3.1.5. Unsupported persistent storage options](#unsupported-persistent-storage-options) Copy linkLink copied to clipboard!

Support for the following persistent storage options from OpenShift Container Platform 3.11 has changed in OpenShift Container Platform 4.22:

* GlusterFS is no longer supported.
* CephFS as a standalone product is no longer supported.
* Ceph RBD as a standalone product is no longer supported.

If you used one of these in OpenShift Container Platform 3.11, you must choose a different persistent storage option for full support in OpenShift Container Platform 4.22.

For more information, see [Understanding persistent storage](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#understanding-persistent-storage).

##### [3.3.1.6. Migration of in-tree volumes to CSI drivers](#migration-of-in-tree-volumes-to-csi-drivers) Copy linkLink copied to clipboard!

OpenShift Container Platform 4 is migrating in-tree volume plugins to their Container Storage Interface (CSI) counterparts. In OpenShift Container Platform 4.22, CSI drivers are the new default for the following in-tree volume types:

* Amazon Web Services (AWS) Elastic Block Storage (EBS)
* Azure Disk
* Azure File
* Google Cloud Persistent Disk (GCP PD)
* OpenStack Cinder
* VMware vSphere

  Note

  As of OpenShift Container Platform 4.13, VMware vSphere is not available by default. However, you can opt into VMware vSphere.

All aspects of volume lifecycle, such as creation, deletion, mounting, and unmounting, is handled by the CSI driver.

For more information, see [CSI automatic migration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/storage/#persistent-storage-csi-migration).

#### [3.3.2. Networking considerations](#migration-preparing-networking) Copy linkLink copied to clipboard!

Review the following networking changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.22.

##### [3.3.2.1. Network isolation mode](#network-isolation-mode) Copy linkLink copied to clipboard!

The default network isolation mode for OpenShift Container Platform 3.11 was `ovs-subnet`, though users frequently switched to use `ovn-multitenant`. The default network isolation mode for OpenShift Container Platform 4.22 is controlled by a network policy.

If your OpenShift Container Platform 3.11 cluster used the `ovs-subnet` or `ovs-multitenant` mode, it is recommended to switch to a network policy for your OpenShift Container Platform 4.22 cluster. Network policies are supported upstream, are more flexible, and they provide the functionality that `ovs-multitenant` does. If you want to maintain the `ovs-multitenant` behavior while using a network policy in OpenShift Container Platform 4.22, follow the steps to [configure multitenant isolation using network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#multitenant-network-policy).

For more information, see [About network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#about-network-policy).

##### [3.3.2.2. OVN-Kubernetes as the default networking plugin in Red Hat OpenShift Networking](#ovn-kubernetes-as-the-default-networking-plugin-in-red-hat-openshift-networking) Copy linkLink copied to clipboard!

In OpenShift Container Platform 3.11, OpenShift SDN was the default networking plugin in Red Hat OpenShift Networking. In OpenShift Container Platform 4.22, OVN-Kubernetes is now the default networking plugin.

For more information on the removal of the OpenShift SDN network plugin and why it has been removed see [OpenShiftSDN CNI removal in OCP 4.17](https://access.redhat.com/articles/7065170).

For information on OVN-Kubernetes features that are similar to features in the OpenShift SDN plugin see:

* [Configuring an egress IP address](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#configuring-egress-ips)
* [Configuring an egress firewall for a project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#configuring-egress-firewall-ovn)
* [Enabling multicast for a project](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#enabling-multicast)
* [Deploying an egress router pod in redirect mode](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/ovn-kubernetes_network_plugin/#deploying-egress-router-ovn-redirection)
* [Configuring multitenant isolation with network policy](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/network_security/#multitenant-network-policy)

Warning

You should install OpenShift Container Platform 4 with the OVN-Kubernetes network plugin because it is not possible to upgrade a cluster to OpenShift Container Platform 4.17 or later if it is using the OpenShift SDN network plugin.

#### [3.3.3. Logging considerations](#migration-preparing-logging) Copy linkLink copied to clipboard!

Review the following logging changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.22.

##### [3.3.3.1. Deploying OpenShift Logging](#deploying-openshift-logging) Copy linkLink copied to clipboard!

OpenShift Container Platform 4 provides a simple deployment mechanism for OpenShift Logging, by using a Cluster Logging custom resource.

##### [3.3.3.2. Aggregated logging data](#aggregated-logging-data) Copy linkLink copied to clipboard!

You cannot transition your aggregate logging data from OpenShift Container Platform 3.11 into your new OpenShift Container Platform 4 cluster.

##### [3.3.3.3. Unsupported logging configurations](#unsupported-logging-configurations) Copy linkLink copied to clipboard!

Some logging configurations that were available in OpenShift Container Platform 3.11 are no longer supported in OpenShift Container Platform 4.22.

#### [3.3.4. Security considerations](#migration-preparing-security) Copy linkLink copied to clipboard!

Review the following security changes to consider when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.22.

##### [3.3.4.1. Unauthenticated access to discovery endpoints](#unauthenticated-access-to-discovery-endpoints) Copy linkLink copied to clipboard!

In OpenShift Container Platform 3.11, an unauthenticated user could access the discovery endpoints (for example, `/api/*` and `/apis/*`). For security reasons, unauthenticated access to the discovery endpoints is no longer allowed in OpenShift Container Platform 4.22. If you do need to allow unauthenticated access, you can configure the RBAC settings as necessary; however, be sure to consider the security implications as this can expose internal cluster components to the external network.

##### [3.3.4.2. Identity providers](#identity-providers) Copy linkLink copied to clipboard!

Configuration for identity providers has changed for OpenShift Container Platform 4, including the following notable changes:

* The request header identity provider in OpenShift Container Platform 4.22 requires mutual TLS, where in OpenShift Container Platform 3.11 it did not.
* The configuration of the OpenID Connect identity provider was simplified in OpenShift Container Platform 4.22. It now obtains data, which previously had to specified in OpenShift Container Platform 3.11, from the provider’s `/.well-known/openid-configuration` endpoint.

For more information, see [Understanding identity provider configuration](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#understanding-identity-provider).

##### [3.3.4.3. OAuth token storage format](#oauth-token-storage-format) Copy linkLink copied to clipboard!

Newly created OAuth HTTP bearer tokens no longer match the names of their OAuth access token objects. The object names are now a hash of the bearer token and are no longer sensitive. This reduces the risk of leaking sensitive information.

##### [3.3.4.4. Default security context constraints](#default-security-context-constraints) Copy linkLink copied to clipboard!

The `restricted` security context constraints (SCC) in OpenShift Container Platform 4 can no longer be accessed by any authenticated user as the `restricted` SCC in OpenShift Container Platform 3.11. The broad authenticated access is now granted to the `restricted-v2` SCC, which is more restrictive than the old `restricted` SCC. The `restricted` SCC still exists; users that want to use it must be specifically given permissions to do it.

For more information, see [Managing security context constraints](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/authentication_and_authorization/#managing-pod-security-policies).

#### [3.3.5. Monitoring considerations](#migration-preparing-monitoring) Copy linkLink copied to clipboard!

Review the following monitoring changes when transitioning from OpenShift Container Platform 3.11 to OpenShift Container Platform 4.22. You cannot migrate Hawkular configurations and metrics to Prometheus.

##### [3.3.5.1. Alert for monitoring infrastructure availability](#alert-for-monitoring-infrastructure-availability) Copy linkLink copied to clipboard!

The default alert that triggers to ensure the availability of the monitoring structure was called `DeadMansSwitch` in OpenShift Container Platform 3.11. This was renamed to `Watchdog` in OpenShift Container Platform 4. If you had PagerDuty integration set up with this alert in OpenShift Container Platform 3.11, you must set up the PagerDuty integration for the `Watchdog` alert in OpenShift Container Platform 4.

For more information, see [Configuring alert routing for default platform alerts](https://docs.redhat.com/en/documentation/monitoring_stack_for_red_hat_openshift/latest/html/configuring_core_platform_monitoring/configuring-alerts-and-notifications#configuring-alert-routing-default-platform-alerts_configuring-alerts-and-notifications).

## [Chapter 4. Network considerations](#planning-considerations-3-4) Copy linkLink copied to clipboard!

Review the strategies for redirecting your application network traffic after migration.

### [4.1. DNS considerations](#dns-considerations_planning-considerations-3-4) Copy linkLink copied to clipboard!

The DNS domain of the target cluster is different from the domain of the source cluster. By default, applications get FQDNs of the target cluster after migration.

To preserve the source DNS domain of migrated applications, select one of the two options described below.

#### [4.1.1. Isolating the DNS domain of the target cluster from the clients](#migration-isolating-dns-domain-of-target-cluster-from-clients_planning-considerations-3-4) Copy linkLink copied to clipboard!

You can allow the clients' requests sent to the DNS domain of the source cluster to reach the DNS domain of the target cluster without exposing the target cluster to the clients.

**Procedure**

1. Place an exterior network component, such as an application load balancer or a reverse proxy, between the clients and the target cluster.
2. Update the application FQDN on the source cluster in the DNS server to return the IP address of the exterior network component.
3. Configure the network component to send requests received for the application in the source domain to the load balancer in the target cluster domain.
4. Create a wildcard DNS record for the `*.apps.source.example.com` domain that points to the IP address of the load balancer of the source cluster.
5. Create a DNS record for each application that points to the IP address of the exterior network component in front of the target cluster. A specific DNS record has higher priority than a wildcard record, so no conflict arises when the application FQDN is resolved.

Note

* The exterior network component must terminate all secure TLS connections. If the connections pass through to the target cluster load balancer, the FQDN of the target application is exposed to the client and certificate errors occur.
* The applications must not return links referencing the target cluster domain to the clients. Otherwise, parts of the application might not load or work properly.

#### [4.1.2. Setting up the target cluster to accept the source DNS domain](#migration-setting-up-target-cluster-to-accept-source-dns-domain_planning-considerations-3-4) Copy linkLink copied to clipboard!

You can set up the target cluster to accept requests for a migrated application in the DNS domain of the source cluster.

**Procedure**

For both non-secure HTTP access and secure HTTPS access, perform the following steps:

1. Create a route in the target cluster’s project that is configured to accept requests addressed to the application’s FQDN in the source cluster:

   ```
   $ oc expose svc <app1-svc> --hostname <app1.apps.source.example.com> \
    -n <app1-namespace>
   ```

   With this new route in place, the server accepts any request for that FQDN and sends it to the corresponding application pods. In addition, when you migrate the application, another route is created in the target cluster domain. Requests reach the migrated application using either of these hostnames.
2. Create a DNS record with your DNS provider that points the application’s FQDN in the source cluster to the IP address of the default load balancer of the target cluster. This will redirect traffic away from your source cluster to your target cluster.

   The FQDN of the application resolves to the load balancer of the target cluster. The default Ingress Controller router accept requests for that FQDN because a route for that hostname is exposed.

For secure HTTPS access, perform the following additional step:

1. Replace the x509 certificate of the default Ingress Controller created during the installation process with a custom certificate.
2. Configure this certificate to include the wildcard DNS domains for both the source and target clusters in the `subjectAltName` field.

   The new certificate is valid for securing connections made using either DNS domain.

### [4.2. Network traffic redirection strategies](#migration-network-traffic-redirection-strategies_planning-considerations-3-4) Copy linkLink copied to clipboard!

After a successful migration, you must redirect network traffic of your stateless applications from the source cluster to the target cluster.

The strategies for redirecting network traffic are based on the following assumptions:

* The application pods are running on both the source and target clusters.
* Each application has a route that contains the source cluster hostname.
* The route with the source cluster hostname contains a CA certificate.
* For HTTPS, the target router CA certificate contains a Subject Alternative Name for the wildcard DNS record of the source cluster.

Consider the following strategies and select the one that meets your objectives.

* Redirecting all network traffic for all applications at the same time

  Change the wildcard DNS record of the source cluster to point to the target cluster router’s virtual IP address (VIP).

  This strategy is suitable for simple applications or small migrations.
* Redirecting network traffic for individual applications

  Create a DNS record for each application with the source cluster hostname pointing to the target cluster router’s VIP. This DNS record takes precedence over the source cluster wildcard DNS record.
* Redirecting network traffic gradually for individual applications

  1. Create a proxy that can direct traffic to both the source cluster router’s VIP and the target cluster router’s VIP, for each application.
  2. Create a DNS record for each application with the source cluster hostname pointing to the proxy.
  3. Configure the proxy entry for the application to route a percentage of the traffic to the target cluster router’s VIP and the rest of the traffic to the source cluster router’s VIP.
  4. Gradually increase the percentage of traffic that you route to the target cluster router’s VIP until all the network traffic is redirected.
* User-based redirection of traffic for individual applications

  Using this strategy, you can filter TCP/IP headers of user requests to redirect network traffic for predefined groups of users. This allows you to test the redirection process on specific populations of users before redirecting the entire network traffic.

  1. Create a proxy that can direct traffic to both the source cluster router’s VIP and the target cluster router’s VIP, for each application.
  2. Create a DNS record for each application with the source cluster hostname pointing to the proxy.
  3. Configure the proxy entry for the application to route traffic matching a given header pattern, such as `test customers`, to the target cluster router’s VIP and the rest of the traffic to the source cluster router’s VIP.
  4. Redirect traffic to the target cluster router’s VIP in stages until all the traffic is on the target cluster router’s VIP.

## [Legal Notice](#idm139624436978000) Copy linkLink copied to clipboard!

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
