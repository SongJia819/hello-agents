---
title: "Installing on Google Cloud"
source_url: https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installing_on_google_cloud/index
retrieved_at: 2026-09-05T05:42:04.679025+00:00
---

# Installing on Google Cloud

---

OpenShift Container Platform 4.22

## Installing OpenShift Container Platform on Google Cloud

Red Hat OpenShift Documentation Team

[Legal Notice](#idm140613129376576)

**Abstract**

This document describes how to install OpenShift Container Platform on Google Cloud.

---

## [Chapter 1. Preparing to install on Google Cloud](#preparing-to-install-on-gcp) Copy linkLink copied to clipboard!

### [1.1. Prerequisites](#preparing-to-install-on-gcp-prerequisites) Copy linkLink copied to clipboard!

* You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes.
* You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing).

### [1.2. Requirements for installing OpenShift Container Platform on Google Cloud](#requirements-for-installing-ocp-on-gcp) Copy linkLink copied to clipboard!

Before installing OpenShift Container Platform on Google Cloud, you must create a service account and configure a Google Cloud project. See [Configuring a Google Cloud project](#installing-gcp-account "Chapter 2. Configuring a Google Cloud project") for details about creating a project, enabling API services, configuring DNS, Google Cloud account limits, and supported Google Cloud regions.

If the cloud Identity and Access Management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, see [Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-gcp-customizations "4.10.2. Configuring a Google Cloud cluster to use short-term credentials"), [Manually creating long-term credentials for Google Cloud](#manually-create-iam_installing-gcp-customizations "4.10.1. Manually creating long-term credentials"), or both for other options.

### [1.3. Choosing a method to install OpenShift Container Platform on Google Cloud](#choosing-an-method-to-install-ocp-on-gcp) Copy linkLink copied to clipboard!

You can install OpenShift Container Platform on installer-provisioned or user-provisioned infrastructure. The default installation type uses installer-provisioned infrastructure, where the installation program provisions the underlying infrastructure for the cluster. You can also install OpenShift Container Platform on infrastructure that you provision. If you do not use infrastructure that the installation program provisions, you must manage and maintain the cluster resources yourself.

See [Installation process](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#installation-process_architecture-installation) for more information about installer-provisioned and user-provisioned installation processes.

#### [1.3.1. Installing a cluster on installer-provisioned infrastructure](#choosing-an-method-to-install-ocp-on-gcp-installer-provisioned) Copy linkLink copied to clipboard!

You can install a cluster on Google Cloud infrastructure that is provisioned by the OpenShift Container Platform installation program, by using one of the following methods:

* **[Installing a cluster quickly on Google Cloud](#installing-gcp-default "Chapter 3. Installing a cluster quickly on Google Cloud")**: You can install OpenShift Container Platform on Google Cloud infrastructure that is provisioned by the OpenShift Container Platform installation program. You can install a cluster quickly by using the default configuration options.
* **[Installing a customized cluster on Google Cloud](#installing-gcp-customizations "Chapter 4. Installing a cluster on Google Cloud with customizations")**: You can install a customized cluster on Google Cloud infrastructure that the installation program provisions. You can customize your OpenShift Container Platform network configuration during installation, so that your cluster can coexist with your existing IP address allocations and adhere to your network requirements. The installation program allows for some customization to be applied at the installation stage. Many other customization options are available [post-installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#post-install-cluster-tasks).
* **[Installing a cluster on Google Cloud in a restricted network](#installing-restricted-networks-gcp-installer-provisioned "Chapter 5. Installing a cluster on Google Cloud in a disconnected environment")**: You can install OpenShift Container Platform on Google Cloud on installer-provisioned infrastructure by using an internal mirror of the installation release content. You can use this method to install a cluster that does not require an active internet connection to obtain the software components. While you can install OpenShift Container Platform by using the mirrored content, your cluster still requires internet access to use the Google Cloud APIs.
* **[Installing a cluster into an existing Virtual Private Cloud](#installing-gcp-vpc "Chapter 6. Installing a cluster on Google Cloud into an existing VPC")**: You can install OpenShift Container Platform on an existing Google Cloud Virtual Private Cloud (VPC). You can use this installation method if you have constraints set by the guidelines of your company, such as limits on creating new accounts or infrastructure.
* **[Installing a private cluster on an existing VPC](#installing-gcp-private "Chapter 8. Installing a private cluster on Google Cloud")**: You can install a private cluster on an existing Google Cloud VPC. You can use this method to deploy OpenShift Container Platform on an internal network that is not visible to the internet.

#### [1.3.2. Installing a cluster on user-provisioned infrastructure](#choosing-an-method-to-install-ocp-on-gcp-user-provisioned) Copy linkLink copied to clipboard!

You can install a cluster on Google Cloud infrastructure that you provision, by using one of the following methods:

* **[Installing a cluster on Google Cloud with user-provisioned infrastructure](#installing-gcp-user-infra "Chapter 9. Installing a cluster on user-provisioned infrastructure in Google Cloud by using Infrastructure Manager templates")**: You can install OpenShift Container Platform on Google Cloud infrastructure that you provide. You can use the provided Infrastructure Manager templates to assist with the installation.
* **[Installing a cluster with shared VPC on user-provisioned infrastructure in Google Cloud](#installing-gcp-user-infra-vpc "Chapter 10. Installing a cluster into a shared VPC on Google Cloud using Infrastructure Manager templates")**: You can use the provided Infrastructure Manager templates to create Google Cloud resources in a shared VPC infrastructure.
* **[Installing a cluster on Google Cloud in a restricted network with user-provisioned infrastructure](#installing-restricted-networks-gcp "Chapter 11. Installing a cluster on Google Cloud in a disconnected environment with user-provisioned infrastructure")**: You can install OpenShift Container Platform on Google Cloud in a restricted network with user-provisioned infrastructure. By creating an internal mirror of the installation release content, you can install a cluster that does not require an active internet connection to obtain the software components. You can also use this installation method to ensure that your clusters only use container images that satisfy your organizational controls on external content.

### [1.4. Next steps](#preparing-to-install-on-gcp-next-steps) Copy linkLink copied to clipboard!

* [Configuring a Google Cloud project](#installing-gcp-account "Chapter 2. Configuring a Google Cloud project")

## [Chapter 2. Configuring a Google Cloud project](#installing-gcp-account) Copy linkLink copied to clipboard!

Before you can install OpenShift Container Platform, you must configure a Google Cloud project to host it. You can configure custom roles and permissions, DNS configuration, and manage your own Google Cloud firewall rules.

### [2.1. Creating a Google Cloud project](#installation-gcp-project_installing-gcp-account) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, you must create a project in your Google Cloud account to host the cluster.

**Procedure**

* Create a project to host your OpenShift Container Platform cluster. See [Creating and Managing Projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in the Google Cloud documentation.

  Important

  Your Google Cloud project must use the Premium Network Service Tier if you are using installer-provisioned infrastructure. The Standard Network Service Tier is not supported for clusters installed using the installation program. The installation program configures internal load balancing for the `api-int.<cluster_name>.<base_domain>` URL; the Premium Tier is required for internal load balancing.

### [2.2. Enabling API services in Google Cloud](#installation-gcp-enabling-api-services_installing-gcp-account) Copy linkLink copied to clipboard!

Your Google Cloud project requires access to several API services to complete OpenShift Container Platform installation.

**Prerequisites**

* You created a project to host your cluster.

**Procedure**

* Enable the following required API services in the project that hosts your cluster. You may also enable optional API services which are not required for installation. See [Enabling services](https://cloud.google.com/service-usage/docs/enable-disable#enabling) in the Google Cloud documentation.

  Expand

  Table 2.1. Required API services

  | API service | Console service name |
  | --- | --- |
  | Compute Engine API | `compute.googleapis.com` |
  | Cloud Resource Manager API | `cloudresourcemanager.googleapis.com` |
  | Cloud DNS API | `dns.googleapis.com` |
  | IAM Service Account Credentials API | `iamcredentials.googleapis.com` |
  | Identity and Access Management (IAM) API | `iam.googleapis.com` |
  | Service Usage API | `serviceusage.googleapis.com` |

  Show more

  Expand

  Table 2.2. Optional API services

  | API service | Console service name |
  | --- | --- |
  | Google Cloud APIs | `cloudapis.googleapis.com` |
  | Service Management API | `servicemanagement.googleapis.com` |
  | Google Cloud Storage JSON API | `storage-api.googleapis.com` |
  | Cloud Storage | `storage-component.googleapis.com` |

  Show more

### [2.3. Configuring DNS for Google Cloud](#installation-gcp-dns_installing-gcp-account) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, the Google Cloud account you use must have a dedicated public hosted zone in the same project that you host the OpenShift Container Platform cluster. This zone must be authoritative for the domain. The DNS service provides cluster DNS resolution and name lookup for external connections to the cluster.

**Procedure**

1. Identify your domain, or subdomain, and registrar. You can transfer an existing domain and registrar or obtain a new one through Google Cloud or another source.

   Note

   If you purchase a new domain, it can take time for the relevant DNS changes to propagate. For more information about purchasing domains through Google, see [Google Domains](https://domains.google/).
2. Create a public hosted zone for your domain or subdomain in your Google Cloud project. See [Creating public zones](https://cloud.google.com/dns/zones/#creating_public_zones) in the Google Cloud documentation.

   Use an appropriate root domain, such as `openshiftcorp.com`, or subdomain, such as `clusters.openshiftcorp.com`.
3. Extract the new authoritative name servers from the hosted zone records. See [Look up your Cloud DNS name servers](https://cloud.google.com/dns/docs/update-name-servers#look_up_your_name_servers) in the Google Cloud documentation.

   You typically have four name servers.
4. Update the registrar records for the name servers that your domain uses. For example, if you registered your domain to Google Domains, see the following topic in the Google Domains Help: [How to switch to custom name servers](https://support.google.com/domains/answer/3290309?hl=en).
5. If you migrated your root domain to Google Cloud DNS, migrate your DNS records. See [Migrating to Cloud DNS](https://cloud.google.com/dns/docs/migrating) in the Google Cloud documentation.
6. If you use a subdomain, follow your company’s procedures to add its delegation records to the parent domain. This process might include a request to your company’s IT department or the division that controls the root domain and DNS services for your company.

### [2.4. Google Cloud account limits](#installation-gcp-limits_installing-gcp-account) Copy linkLink copied to clipboard!

The OpenShift Container Platform cluster uses a number of Google Cloud components, but the default [Quotas](https://cloud.google.com/docs/quota) do not affect your ability to install a default OpenShift Container Platform cluster.

A default cluster, which contains three compute and three control plane machines, uses the following resources. Note that some resources are required only during the bootstrap process and are removed after the cluster deploys.

Expand

Table 2.3. Google Cloud resources used in a default cluster

| Service | Component | Location | Total resources required | Resources removed after bootstrap |
| --- | --- | --- | --- | --- |
| Service account | IAM | Global | 6 | 1 |
| Firewall rules | Compute | Global | 11 | 1 |
| Forwarding rules | Compute | Global | 2 | 0 |
| In-use global IP addresses | Compute | Global | 4 | 1 |
| Health checks | Compute | Global | 3 | 0 |
| Images | Compute | Global | 1 | 0 |
| Networks | Compute | Global | 2 | 0 |
| Static IP addresses | Compute | Region | 4 | 1 |
| Routers | Compute | Global | 1 | 0 |
| Routes | Compute | Global | 2 | 0 |
| Subnetworks | Compute | Global | 2 | 0 |
| Target pools | Compute | Global | 3 | 0 |
| CPUs | Compute | Region | 28 | 4 |
| Persistent disk SSD (GB) | Compute | Region | 896 | 128 |

Show more

Note

If any of the quotas are insufficient during installation, the installation program displays an error that states both which quota was exceeded and the region.

Be sure to consider your actual cluster size, planned cluster growth, and any usage from other clusters that are associated with your account. The CPU, static IP addresses, and persistent disk SSD (storage) quotas are the ones that are most likely to be insufficient.

If you plan to deploy your cluster in one of the following regions, you will exceed the maximum storage quota and are likely to exceed the CPU quota limit:

* `asia-east2`
* `asia-northeast2`
* `asia-south1`
* `australia-southeast1`
* `europe-north1`
* `europe-west2`
* `europe-west3`
* `europe-west6`
* `northamerica-northeast1`
* `southamerica-east1`
* `us-west2`

You can increase resource quotas from the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas), but you might need to file a support ticket. Be sure to plan your cluster size early so that you can allow time to resolve the support ticket before you install your OpenShift Container Platform cluster.

### [2.5. Creating a service account in Google Cloud](#installation-gcp-service-account_installing-gcp-account) Copy linkLink copied to clipboard!

OpenShift Container Platform requires a Google Cloud service account that provides authentication and authorization to access data in the Google APIs. If you do not have an existing IAM service account that contains the required roles in your project, you must create one.

Note

To reduce the scope of permissions granted to the main service account in your Google Cloud project while still being able to use the Google Cloud Container Storage Interface (CSI) Driver Operator, you can transfer the control of permissions from the project-wide service account to the control plane and compute node service accounts instead, thus reducing the scope of the permission. For more information, see Section *Reducing permissions while using the Google Cloud CSI Driver Operator*.

**Prerequisites**

* You created a project to host your cluster.

**Procedure**

1. Create a service account in the project that you use to host your OpenShift Container Platform cluster. See [Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account) in the Google Cloud documentation.
2. Grant the service account the appropriate permissions. You can either grant the individual permissions that follow or assign the `Owner` role to it. See [Granting roles to a service account for specific resources](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource).

   Note

   While making the service account an owner of the project is the easiest way to gain the required permissions, it means that service account has complete control over the project. You must determine if the risk that comes from offering that power is acceptable.
3. You can create the service account key in JSON format, or attach the service account to a Google Cloud virtual machine. See [Creating service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and [Creating and enabling service accounts for instances](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances) in the Google Cloud documentation.

   Note

   If you use a virtual machine with an attached service account to create your cluster, you must set `credentialsMode: Manual` in the `install-config.yaml` file before installation.

#### [2.5.1. Required Google Cloud roles](#installation-gcp-permissions_installing-gcp-account) Copy linkLink copied to clipboard!

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform. If your organization’s security policies require a more restrictive set of permissions, you can create a service account with the following permissions. If you deploy your cluster into an existing virtual private cloud (VPC), the service account does not require certain networking permissions, which are noted in the following lists:

**Required roles for the installation program**

* Compute Admin
* Role Administrator
* Security Admin
* Service Account Admin
* Service Account Key Admin
* Service Account User
* Storage Admin

**Required roles for creating network resources during installation**

* DNS Administrator

**Required roles for using the Cloud Credential Operator in passthrough mode**

* Compute Load Balancer Admin
* Tag User

The following roles are applied to the service accounts that the control plane and compute machines use:

Expand

Table 2.4. Google Cloud service account roles

| Account | Roles |
| --- | --- |
| Control Plane | `roles/compute.instanceAdmin` |
| `roles/compute.networkAdmin` |
| `roles/compute.securityAdmin` |
| `roles/storage.admin` |
| `roles/iam.serviceAccountUser` |
| Compute | `roles/compute.viewer` |
| `roles/storage.admin` |
| `roles/artifactregistry.reader` |

Show more

#### [2.5.2. Required Google Cloud permissions for installer-provisioned infrastructure](#minimum-required-permissions-ipi-gcp_installing-gcp-account) Copy linkLink copied to clipboard!

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform. If your organization’s security policies require a more restrictive set of permissions, you can create [custom roles](https://cloud.google.com/iam/docs/creating-custom-roles) with the necessary permissions.

The following permissions are required for the installer-provisioned infrastructure for creating and deleting the OpenShift Container Platform cluster.

**Example 2.1. Required permissions for creating network resources**

* `compute.addresses.create`
* `compute.addresses.createInternal`
* `compute.addresses.delete`
* `compute.addresses.get`
* `compute.addresses.list`
* `compute.addresses.use`
* `compute.addresses.useInternal`
* `compute.firewalls.create`

  + This permission is not required if you install into an existing VPC and manage your own firewall rules. See the *Managing your own firewall rules* section.
* `compute.firewalls.delete`

  + This permission is not required if you install into an existing VPC and manage your own firewall rules. See the *Managing your own firewall rules* section.
* `compute.firewalls.get`
* `compute.firewalls.list`
* `compute.forwardingRules.create`
* `compute.forwardingRules.get`
* `compute.forwardingRules.list`
* `compute.forwardingRules.setLabels`
* `compute.globalAddresses.create`
* `compute.globalAddresses.get`
* `compute.globalAddresses.use`
* `compute.globalForwardingRules.create`
* `compute.globalForwardingRules.get`
* `compute.globalForwardingRules.setLabels`
* `compute.networks.create`
* `compute.networks.get`
* `compute.networks.list`
* `compute.networks.updatePolicy`
* `compute.networks.use`
* `compute.routers.create`
* `compute.routers.get`
* `compute.routers.list`
* `compute.routers.update`
* `compute.routes.list`
* `compute.subnetworks.create`
* `compute.subnetworks.get`
* `compute.subnetworks.list`
* `compute.subnetworks.use`
* `compute.subnetworks.useExternalIp`

**Example 2.2. Required permissions for creating load balancer resources**

* `compute.backendServices.create`
* `compute.backendServices.get`
* `compute.backendServices.list`
* `compute.backendServices.update`
* `compute.backendServices.use`
* `compute.regionBackendServices.create`
* `compute.regionBackendServices.get`
* `compute.regionBackendServices.list`
* `compute.regionBackendServices.update`
* `compute.regionBackendServices.use`
* `compute.targetPools.addInstance`
* `compute.targetPools.create`
* `compute.targetPools.get`
* `compute.targetPools.list`
* `compute.targetPools.removeInstance`
* `compute.targetPools.use`
* `compute.targetTcpProxies.create`
* `compute.targetTcpProxies.get`
* `compute.targetTcpProxies.use`

**Example 2.3. Required permissions for creating DNS resources**

* `dns.changes.create`
* `dns.changes.get`
* `dns.managedZones.create`
* `dns.managedZones.get`
* `dns.managedZones.list`
* `dns.networks.bindPrivateDNSZone`
* `dns.resourceRecordSets.create`
* `dns.resourceRecordSets.list`

**Example 2.4. Required permissions for creating Service Account resources**

* `iam.serviceAccountKeys.create`
* `iam.serviceAccountKeys.delete`
* `iam.serviceAccountKeys.get`
* `iam.serviceAccountKeys.list`
* `iam.serviceAccounts.actAs`

  + This permission can be limited to act as the control plane and compute service accounts. Alternatively, you may grant the service account that the installation program uses the `iam.serviceAccountUser` role on the control plane and compute service accounts.
* `iam.serviceAccounts.create`
* `iam.serviceAccounts.delete`
* `iam.serviceAccounts.get`
* `iam.serviceAccounts.list`
* `resourcemanager.projects.get`
* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`

  + This permission is not required if you use `credentialsMode: Manual` and supply your own service accounts for compute and control plane nodes.

**Example 2.5. Required permissions for creating compute resources**

* `compute.disks.create`
* `compute.disks.get`
* `compute.disks.list`
* `compute.disks.setLabels`
* `compute.instanceGroups.create`
* `compute.instanceGroups.delete`
* `compute.instanceGroups.get`
* `compute.instanceGroups.list`
* `compute.instanceGroups.update`
* `compute.instanceGroups.use`
* `compute.instances.create`
* `compute.instances.delete`
* `compute.instances.get`
* `compute.instances.list`
* `compute.instances.setLabels`
* `compute.instances.setMetadata`
* `compute.instances.setServiceAccount`
* `compute.instances.setTags`
* `compute.instances.use`
* `compute.machineTypes.get`
* `compute.machineTypes.list`

**Example 2.6. Required for creating storage resources**

* `storage.buckets.create`
* `storage.buckets.delete`
* `storage.buckets.get`
* `storage.buckets.list`
* `storage.objects.create`
* `storage.objects.delete`
* `storage.objects.get`
* `storage.objects.list`

**Example 2.7. Required permissions for creating health check resources**

* `compute.healthChecks.create`
* `compute.healthChecks.get`
* `compute.healthChecks.list`
* `compute.healthChecks.useReadOnly`
* `compute.httpHealthChecks.create`
* `compute.httpHealthChecks.get`
* `compute.httpHealthChecks.list`
* `compute.httpHealthChecks.useReadOnly`
* `compute.regionHealthChecks.create`
* `compute.regionHealthChecks.get`
* `compute.regionHealthChecks.useReadOnly`

**Example 2.8. Required permissions to get Google Cloud zone and region related information**

* `compute.globalOperations.get`
* `compute.regionOperations.get`
* `compute.regions.get`
* `compute.regions.list`
* `compute.zoneOperations.get`
* `compute.zones.get`
* `compute.zones.list`

**Example 2.9. Required permissions for checking services and quotas**

* `monitoring.timeSeries.list`
* `serviceusage.quotas.get`
* `serviceusage.services.list`

**Example 2.10. Required IAM permissions for installation**

* `iam.roles.create`
* `iam.roles.get`
* `iam.roles.update`

**Example 2.11. Required permissions when authenticating without a service account key**

* `iam.serviceAccounts.signBlob`

**Example 2.12. Required permissions when providing Key Management Service (KMS) key rings**

* `cloudkms.keyRings.list`

**Example 2.13. Optional Images permissions for installation**

* `compute.images.list`

**Example 2.14. Optional permission for running gather bootstrap**

* `compute.instances.getSerialPortOutput`

**Example 2.15. Required permissions for deleting network resources**

* `compute.addresses.delete`
* `compute.addresses.deleteInternal`
* `compute.addresses.list`
* `compute.addresses.setLabels`
* `compute.firewalls.delete`
* `compute.firewalls.list`
* `compute.forwardingRules.delete`
* `compute.forwardingRules.list`
* `compute.globalAddresses.delete`
* `compute.globalAddresses.list`
* `compute.globalForwardingRules.delete`
* `compute.globalForwardingRules.list`
* `compute.networks.delete`
* `compute.networks.list`
* `compute.networks.updatePolicy`
* `compute.routers.delete`
* `compute.routers.list`
* `compute.routes.list`
* `compute.subnetworks.delete`
* `compute.subnetworks.list`

**Example 2.16. Required permissions for deleting load balancer resources**

* `compute.backendServices.delete`
* `compute.backendServices.list`
* `compute.regionBackendServices.delete`
* `compute.regionBackendServices.list`
* `compute.targetPools.delete`
* `compute.targetPools.list`
* `compute.targetTcpProxies.delete`
* `compute.targetTcpProxies.list`

**Example 2.17. Required permissions for deleting DNS resources**

* `dns.changes.create`
* `dns.managedZones.delete`
* `dns.managedZones.get`
* `dns.managedZones.list`
* `dns.resourceRecordSets.delete`
* `dns.resourceRecordSets.list`

**Example 2.18. Required permissions for deleting Service Account resources**

* `iam.serviceAccounts.delete`
* `iam.serviceAccounts.get`
* `iam.serviceAccounts.list`
* `resourcemanager.projects.getIamPolicy`

**Example 2.19. Required permissions for deleting compute resources**

* `compute.disks.delete`
* `compute.disks.list`
* `compute.instanceGroups.delete`
* `compute.instanceGroups.list`
* `compute.instances.delete`
* `compute.instances.list`
* `compute.instances.stop`
* `compute.machineTypes.list`

**Example 2.20. Required for deleting storage resources**

* `storage.buckets.delete`
* `storage.buckets.getIamPolicy`
* `storage.buckets.list`
* `storage.objects.delete`
* `storage.objects.list`

**Example 2.21. Required permissions for deleting health check resources**

* `compute.healthChecks.delete`
* `compute.healthChecks.list`
* `compute.httpHealthChecks.delete`
* `compute.httpHealthChecks.list`
* `compute.regionHealthChecks.delete`
* `compute.regionHealthChecks.list`

**Example 2.22. Required Images permissions for deletion**

* `compute.images.list`

#### [2.5.3. Required Google Cloud permissions for shared VPC installations](#minimum-required-permissions-ipi-gcp-xpn_installing-gcp-account) Copy linkLink copied to clipboard!

When you are installing a cluster to a [shared VPC](https://cloud.google.com/vpc/docs/shared-vpc), you must configure the service account for both the host project and the service project.

Important

You can use granular permissions for a Cloud Credential Operator (CCO) that operates in either Manual or Mint credentials mode. For more information about the minimum permissions required for a standard installation that is configured with either of these credentials modes, see "Required Google Cloud permissions for installer-provisioned infrastructure".

You cannot use granular permissions in Passthrough credentials mode. For more information about the minimum roles required, see "Required Google Cloud roles".

If you are not installing to a shared Virtual Private Cloud (VPC), you can skip the procedure.

Important

When installing a cluster on a shared VPC by using short-lived credentials, you must grant the `compute.subnetworks.use` permission in the host project to Day 2 Operator service accounts.

After using the `ccoctl` utility to generate the Google Cloud credentials, manually grant this permission to the Cluster CAPI Operator and Machine API Operator service accounts.

Ensure that the host project applies one of the following configurations to the service account, noting that the permissions for creating and deleting firewalls are not required if you manage your own firewall rules:

**Example 2.23. Required permissions for creating firewalls in the host project**

* `projects/<host-project>/roles/dns.networks.bindPrivateDNSZone`
* `roles/compute.networkAdmin`
* `roles/compute.securityAdmin`

**Example 2.24. Required permissions for deleting firewalls in the host project**

* `compute.firewalls.delete`
* `compute.networks.updatePolicy`

**Example 2.25. Required minimal permissions**

* `projects/<host-project>/roles/dns.networks.bindPrivateDNSZone`
* `roles/compute.networkUser`

If you do not supply a service account for control plane nodes in the `install-config.yaml` file, grant the following permissions to the service account in the host project. If you do not supply a service account for compute nodes in the `install-config.yaml` file, grant the following permissions to the service account in the host project for cluster destruction. If you do supply service accounts for control plane and compute nodes, you do not need to grant the following permissions.

* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`

The following permissions are required when you select a separate project for the location of the DNS zone or zones. These permissions are also required when the DNS zone or zones are located in a third project.

**Example 2.26. Required minimal permissions for provisioning DNS resources in a separate project**

* `dns.changes.create`
* `dns.changes.get`
* `dns.managedZones.create`
* `dns.managedZones.delete`
* `dns.managedZones.get`
* `dns.managedZones.list`
* `dns.managedZones.update`
* `dns.resourceRecordSets.create`
* `dns.resourceRecordSets.delete`
* `dns.resourceRecordSets.list`

#### [2.5.4. Required Google Cloud permissions for user-provided service accounts](#minimum-required-permissions-ipi-gcp-provided-sas_installing-gcp-account) Copy linkLink copied to clipboard!

When you are installing a cluster, the compute and control plane nodes require their own service accounts. By default, the installation program creates a service account for the control plane and compute nodes. The service account that the installation program uses requires the roles and permissions that are listed in the *Creating a service account in Google Cloud* section, as well as the `resourcemanager.projects.getIamPolicy` and `resourcemanager.projects.setIamPolicy` permissions. These permissions should be applied to the service account in the host project. If this approach does not meet the security requirements of your organization, you can provide a service account email address for the control plane or compute nodes in the `install-config.yaml` file. For more information, see the *Installation configuration parameters for Google Cloud* page. If you provide a service account for control plane nodes during an installation into a shared VPC, you must grant that service account the `roles/compute.networkUser` role in the host project. If you want the installation program to automatically create firewall rules when you supply the control plane service account, you must grant that service account the `roles/compute.networkAdmin` and `roles/compute.securityAdmin` roles in the host project. If you only supply the `roles/compute.networkUser` role, you must create the firewall rules manually.

Important

The following roles are required for user-provided service accounts for control plane and compute nodes respectively.

**Example 2.27. Required roles for control plane nodes**

* `roles/compute.instanceAdmin`
* `roles/compute.networkAdmin`
* `roles/compute.securityAdmin`
* `roles/storage.admin`

**Example 2.28. Required roles for compute nodes**

* `roles/compute.viewer`
* `roles/storage.admin`
* `roles/artifactregistry.reader`

### [2.6. Managing your own firewall rules](#installation-gcp-user-managed-firewall-rules_installing-gcp-account) Copy linkLink copied to clipboard!

You can manage your own firewall rules when installing a cluster on Google Cloud into an existing VPC by enabling the `firewallRulesManagement` parameter in the `install-config.yaml` file. You can limit the permissions that you grant to the installation program by managing your own firewall rules.

Important

If you manage your own firewall rules, you must continue to manage them through the lifetime of the cluster. If you create a new service, create a new firewall rule that permits traffic on the service port, from the desired source addresses to the compute nodes. An example rule is described in the table below.

If you want to manage your own firewall rules, you must create the following rules before installation:

Expand

| Rule Name | Protocol:Port | Source | Destination |
| --- | --- | --- | --- |
| bootstrap-in-ssh | `tcp:22` | `<allowed_external_cidr>` | `<control_plane_node_tags>` |
| api | `tcp:6443` | `<allowed_external_cidr>` | `<control_plane_node_tags>` |
| health-checks | `tcp:6080,6443,22624` | `35.191.0.0/16`, `130.211.0.0/22`, `209.85.152.0/22`, `209.85.204.0/22` | `<control_plane_node_tags>` |
| etcd | `tcp:2379,2380` | `<control_plane_node_tags>` | `<control_plane_node_tags>` |
| control-plane | `tcp:10257,10259,22623` | `<control_plane_node_tags>`, `<compute_node_tags>` | `<control_plane_node_tags>` |
| internal-network | icmp,`tcp:22` | `<internal_network_cidr>` | `<control_plane_node_tags>`, `<compute_node_tags>` |
| internal-cluster | `udp:500,4500,4789,6081`, `udp:9000-9999,30000-32767`, `esp`, `tcp:9000-9999,10250`, `tcp:30000-32767` | `<control_plane_node_tags>`, `<compute_node_tags>` | `<control_plane_node_tags>`, `<compute_node_tags>` |
| ingress-k8s-fw | `tcp:80,443` | `<allowed_external_cidr>` | `<control_plane_node_tags>`, `<compute_node_tags>` |
| ingress-k8s-http-hc | `tcp:30000-32767` | `35.191.0.0/16`, `130.211.0.0/22`, `209.85.152.0/22`, `209.85.204.0/22` | `<control_plane_node_tags>`, `<compute_node_tags>` |
| `<sample_rule_name>` | `<service_port>` | `<allowed_external_cidr>` | `<compute_node_tags>` |

Show more

where:

`<allowed_external_cidr>`
:   Specifies a network CIDR of the machines that you want to grant access to your cluster. For a public cluster, this would typically be `0.0.0.0/0`. For a private cluster, access might be restricted to the cluster machine network.

`<control_plane_node_tags>`
:   Specifies the network tags that apply to the control plane machines in your cluster. These tags must be specified in the `install-config.yaml` file you use to deploy the cluster.

`<compute_node_tags>`
:   Specifies the network tags that apply to the compute machines in your cluster. These tags must be specified in the `install-config.yaml` file you use to deploy the cluster.

`<internal_network_cidr>`
:   Specifies the network CIDR of the machine network that contains all the machines in your cluster.

`<sample_rule_name>`
:   Specifies the name of a custom rule added after installation, for example if you create a new service in your cluster. You can add multiple custom rules as needed.

`<service_port>`
:   Specifies the port or port range of the service you created, and the network protocol, such as TCP or UDP. If you create a service using `oc expose`, you can find the service port and protocol by running the command `oc get service <service_name> -o jsonpath='{.spec.ports[0].port}'`, where `<service_name>` is the name of the service you created.

After installation, you can reduce the port range of the `ingress-k8s-http-hc` and `internal-cluster` rules from `tcp:30000-32767` to the individual port that the ingress load balancer service uses, which is not known before installation. You can determine the service port by running the following command after installation:

```
$ oc get svc router-default -n openshift-ingress -o jsonpath='{.spec.ports[*].nodePort}'
```

### [2.7. Configuring Google Cloud organization policies and VPC service controls](#installation-gcp-organization-policies_installing-gcp-account) Copy linkLink copied to clipboard!

OpenShift Container Platform requires that you modify or remove some organization policies and VPC service controls when installing a cluster on Google Cloud.

If your organization uses the following policies, they must be modified or removed:

* `compute.trustedImageProjects`
* `iam.allowedPolicyMemberDomains`
* `storage.publicAccessPrevention`
* VPC Service Controls egress rules

**Prerequisites**

* You created a project to host your cluster.

**Procedure**

1. Modify the `constraints/compute.trustedImageProjects` constraint in your Google Cloud project and add `projects/rhcos-cloud` to the `allowedValues` list, as in the following example:

   ```
   constraint: constraints/compute.trustedImageProjects
   listPolicy:
    allowedValues:
       - projects/rhcos-cloud
   ```

   Alternatively, you can delete the `constraints/compute.trustedImageProjects` constraint.
2. Modify the `iam.managed.allowedPolicyMembers` constraint to allow the service account that the installation program uses to authenticate with Google Cloud and create storage as in the following example:

   ```
   name: organizations/<organization_id>/policies/iam.managed.allowedPolicyMembers
   spec:
   rules:
    - enforce: true
      parameters:
        allowedMemberSubjects:
          - <allowed_member>
   ```

   where:

   `<organization_id>`
   :   Specifies the numeric ID of your Google Cloud organization.

   `<allowed_member>`
   :   Specifies the IAM role that you created for the installation program. You can specify a service account in the format of "serviceAccount:example-service-account@example.com" or a user in the format of "user:example-user@example.com".
3. Disable the `storage.publicAccessPrevention` constraint so that the installation program can access the cloud storage for your project.
4. Create an egress rule that allows access to the RHCOS project, as in the following example:

   ```
   - egressFrom:
       identityType: ANY_IDENTITY
       identities:
         - "serviceAccount:<installation_program_sa>@<project_id>.iam.gserviceaccount.com"
         - "user:<admin_email>"
     egressTo:
       resources:
         - <project_id>
       operations:
         - serviceName: "compute.googleapis.com"
           methodSelectors: [{method: "*"}]
         - serviceName: "storage.googleapis.com"
           methodSelectors: [{method: "*"}]
         - serviceName: "dns.googleapis.com"
           methodSelectors: [{method: "*"}]
         - serviceName: "iam.googleapis.com"
           methodSelectors: [{method: "*"}]
         - serviceName: "cloudresourcemanager.googleapis.com"
           methodSelectors: [{method: "*"}]
         - serviceName: "serviceusage.googleapis.com"
           methodSelectors: [{method: "*"}]
         - serviceName: "artifactregistry.googleapis.com"
           methodSelectors: [{method: "*"}]
         - serviceName: "deploymentmanager.googleapis.com"
           methodSelectors: [{method: "*"}]
   ```

   where:

   `<installation_program_sa>`
   :   Specifies the service account that you created for the installation program. This service account will be granted access to the specified resources.

   `<project_id>`
   :   Specifies the project ID of the Google Cloud project where you are installing the cluster.

   `<admin_email>`
   :   Specifies the email address of an administrator account. You do not need to specify both a service account and an administrator email address. This service account will be granted access to the specified resources.

   `<project_id>`
   :   Specifies one or more projects that the specified identities can access. You can specify a wildcard such as `projects/*` to grant access to all projects, or specific project IDs such as `projects/1234567890`.

### [2.8. Supported Google Cloud regions](#installation-gcp-regions_installing-gcp-account) Copy linkLink copied to clipboard!

You can deploy an OpenShift Container Platform cluster to the following Google Cloud regions:

* `africa-south1` (Johannesburg, South Africa)
* `asia-east1` (Changhua County, Taiwan)
* `asia-east2` (Hong Kong)
* `asia-northeast1` (Tokyo, Japan)
* `asia-northeast2` (Osaka, Japan)
* `asia-northeast3` (Seoul, South Korea)
* `asia-south1` (Mumbai, India)
* `asia-south2` (Delhi, India)
* `asia-southeast1` (Jurong West, Singapore)
* `asia-southeast2` (Jakarta, Indonesia)
* `australia-southeast1` (Sydney, Australia)
* `australia-southeast2` (Melbourne, Australia)
* `europe-central2` (Warsaw, Poland)
* `europe-north1` (Hamina, Finland)
* `europe-southwest1` (Madrid, Spain)
* `europe-west1` (St. Ghislain, Belgium)
* `europe-west2` (London, England, UK)
* `europe-west3` (Frankfurt, Germany)
* `europe-west4` (Eemshaven, Netherlands)
* `europe-west6` (Zürich, Switzerland)
* `europe-west8` (Milan, Italy)
* `europe-west9` (Paris, France)
* `europe-west12` (Turin, Italy)
* `me-central1` (Doha, Qatar, Middle East)
* `me-central2` (Dammam, Saudi Arabia, Middle East)
* `me-west1` (Tel Aviv, Israel)
* `northamerica-northeast1` (Montréal, Québec, Canada)
* `northamerica-northeast2` (Toronto, Ontario, Canada)
* `southamerica-east1` (São Paulo, Brazil)
* `southamerica-west1` (Santiago, Chile)
* `us-central1` (Council Bluffs, Iowa, USA)
* `us-east1` (Moncks Corner, South Carolina, USA)
* `us-east4` (Ashburn, Northern Virginia, USA)
* `us-east5` (Columbus, Ohio)
* `us-south1` (Dallas, Texas)
* `us-west1` (The Dalles, Oregon, USA)
* `us-west2` (Los Angeles, California, USA)
* `us-west3` (Salt Lake City, Utah, USA)
* `us-west4` (Las Vegas, Nevada, USA)

Note

To determine which machine type instances are available by region and zone, see the Google [documentation](https://cloud.google.com/compute/docs/regions-zones#available).

### [2.9. Next steps](#next-steps) Copy linkLink copied to clipboard!

* Install an OpenShift Container Platform cluster on Google Cloud. You can [install a customized cluster](#installing-gcp-customizations "Chapter 4. Installing a cluster on Google Cloud with customizations") or [quickly install a cluster](#installing-gcp-default "Chapter 3. Installing a cluster quickly on Google Cloud") with default options.

## [Chapter 3. Installing a cluster quickly on Google Cloud](#installing-gcp-default) Copy linkLink copied to clipboard!

In OpenShift Container Platform version 4.22, you can install a cluster on Google Cloud that uses the default configuration options.

### [3.1. Prerequisites](#prerequisites) Copy linkLink copied to clipboard!

* You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes.
* You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing).
* You [configured a Google Cloud project](#installing-gcp-account "Chapter 2. Configuring a Google Cloud project") to host the cluster.
* If you use a firewall, you [configured it to allow the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires access to.
* If you are installing using a [Private Service Connect (PSC) endpoint](https://cloud.google.com/vpc/docs/private-service-connect), you must configure the endpoint in the same Virtual Private Cloud (VPC) where you install the cluster, specified in the `install-config.yaml` file, as described in [Installing a cluster on Google Cloud into an existing VPC](#installing-gcp-vpc "Chapter 6. Installing a cluster on Google Cloud into an existing VPC").

### [3.2. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-gcp-default) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [3.3. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-gcp-default) Copy linkLink copied to clipboard!

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

### [3.4. Obtaining the installation program](#installation-obtaining-installer_installing-gcp-default) Copy linkLink copied to clipboard!

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

### [3.5. Deploying the cluster](#installation-launching-installer_installing-gcp-default) Copy linkLink copied to clipboard!

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

Important

You can run the `create cluster` command of the installation program only once, during initial installation.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

**Procedure**

1. Remove any existing Google Cloud credentials that do not use the service account key for the Google Cloud account that you configured for your cluster and that are stored in the following locations:

   * The `GOOGLE_CREDENTIALS`, `GOOGLE_CLOUD_KEYFILE_JSON`, or `GCLOUD_KEYFILE_JSON` environment variables
   * The `~/.gcp/osServiceAccount.json` file
   * The `gcloud cli` default credentials
2. In the directory that contains the installation program, initialize the cluster deployment by running the following command:

   ```
   $ ./openshift-install create cluster --dir <installation_directory> \
       --log-level=info
   ```

   * For `<installation_directory>`, specify the directory name to store the files that the installation program creates.
   * To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

   When specifying the directory:

   * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
   * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
3. Provide values at the prompts:

   1. Optional: Select an SSH key to use to access your cluster machines.

      Note

      For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
   2. Select **gcp** as the platform to target.
   3. If you have not configured the service account key for your Google Cloud account on your host, you must obtain it from Google Cloud and paste the contents of the file or enter the absolute path to the file.
   4. Select the project ID to provision the cluster in. The default value is specified by the service account that you configured.
   5. Select the region to deploy the cluster to.
   6. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.
   7. Enter a descriptive name for your cluster. If you provide a name that is longer than 6 characters, only the first 6 characters will be used in the infrastructure ID that is generated from the cluster name.
   8. Paste the [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret).
4. Optional: You can reduce the number of permissions for the service account that you used to install the cluster.

   * If you assigned the `Owner` role to your service account, you can remove that role and replace it with the `Viewer` role.
   * If you included the `Service Account Key Admin` role, you can remove it.

**Verification**

When the cluster deployment completes successfully:

* The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.
* Credential information also outputs to `<installation_directory>/.openshift_install.log`.

  Important

  Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.

  **Example output**

  ```
  ...
  INFO Install complete!
  INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
  INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
  INFO Login to the console with user: "kubeadmin", and password: "password"
  INFO Time elapsed: 36m22s
  ```

  Important

  + The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
  + It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

### [3.6. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-gcp-default) Copy linkLink copied to clipboard!

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

### [3.7. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-gcp-default) Copy linkLink copied to clipboard!

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

### [3.8. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-gcp-default) Copy linkLink copied to clipboard!

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

### [3.9. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-gcp-default) Copy linkLink copied to clipboard!

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

### [3.10. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-gcp-default) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

### [3.11. Next steps](#next-steps-2) Copy linkLink copied to clipboard!

* [Customize your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations).
* If necessary, you can [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting).

## [Chapter 4. Installing a cluster on Google Cloud with customizations](#installing-gcp-customizations) Copy linkLink copied to clipboard!

In OpenShift Container Platform version 4.22, you can install a cluster on Google Cloud by using installer-provisioned infrastructure with customizations, including network configuration options. In each, you modify parameters in the `install-config.yaml` file before you install the cluster.

By customizing your network configuration, your cluster can coexist with existing IP address allocations in your environment and integrate with existing MTU and VXLAN configurations.

You must set most of the network configuration parameters during installation, and you can modify only `kubeProxy` configuration parameters in a running cluster.

### [4.1. Prerequisites](#prerequisites-2) Copy linkLink copied to clipboard!

* You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes.
* You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing).
* You [configured a Google Cloud project](#installing-gcp-account "Chapter 2. Configuring a Google Cloud project") to host the cluster.
* If you use a firewall, you [configured it to allow the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

### [4.2. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-gcp-customizations) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [4.3. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-gcp-customizations) Copy linkLink copied to clipboard!

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

### [4.4. Obtaining the installation program](#installation-obtaining-installer_installing-gcp-customizations) Copy linkLink copied to clipboard!

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

### [4.5. Creating the installation configuration file](#installation-initializing_installing-gcp-customizations) Copy linkLink copied to clipboard!

You can customize the OpenShift Container Platform cluster you install on Google Cloud.

**Prerequisites**

* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* Configure a Google Cloud account.

**Procedure**

1. Create the `install-config.yaml` file.

   1. Change to the directory that contains the installation program and run the following command:

      ```
      $ ./openshift-install create install-config --dir <installation_directory>
      ```

      * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

        When specifying the directory:
      * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
      * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
   2. At the prompts, provide the configuration details for your cloud:

      1. Optional: Select an SSH key to use to access your cluster machines.

         Note

         For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
      2. Select **gcp** as the platform to target.
      3. If you have not configured the service account key for your Google Cloud account on your computer, you must obtain it from Google Cloud and paste the contents of the file or enter the absolute path to the file.
      4. Select the project ID to provision the cluster in. The default value is specified by the service account that you configured.
      5. Select the region to deploy the cluster to.
      6. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.
      7. Enter a descriptive name for your cluster.
2. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.

   Note

   If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that the cluster’s control planes are schedulable. For more information, see "Installing a three-node cluster on Google Cloud".
3. Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

   Important

   The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

#### [4.5.1. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-gcp-customizations) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 4.1. Minimum resource requirements

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Show more

* One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
* OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance.
* As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines.

Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* ppc64le architecture requires IBM® Power9 ISA
* s390x architecture requires IBM® z14 ISA

For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

#### [4.5.2. Tested instance types for Google Cloud](#installation-gcp-tested-machine-types_installing-gcp-customizations) Copy linkLink copied to clipboard!

The following Google Cloud instance types have been tested with OpenShift Container Platform.

Note

Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) (Google documentation).

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see [machine series support for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in *Storage*.

See the following machine series:

* `A2`
* `A3`
* `C2`
* `C2D`
* `C3`
* `C3D`
* `C4`
* `E2`
* `M1`
* `N1`
* `N2`
* `N2D`
* `N4`
* `Tau T2D`

#### [4.5.3. Tested instance types for Google Cloud on 64-bit ARM infrastructures](#installation-gcp-tested-machine-types-arm_installing-gcp-customizations) Copy linkLink copied to clipboard!

The following Google Cloud 64-bit ARM instance types have been tested with OpenShift Container Platform.

See the following machine series for 64-bit ARM machines:

* `C4A`
* `N4A`
* `Tau T2A`

#### [4.5.4. Using custom machine types](#installation-custom-machine-types_installing-gcp-customizations) Copy linkLink copied to clipboard!

Using a custom machine type to install a OpenShift Container Platform cluster is supported.

Consider the following when using a custom machine type:

* Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation".
* The name of the custom machine type must adhere to the following syntax:

  `custom-<number_of_cpus>-<amount_of_memory_in_mb>`

  For example, `custom-6-20480`.

As part of the installation process, you specify the custom machine type in the `install-config.yaml` file.

**Sample `install-config.yaml` file with a custom machine type**

```
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  platform:
    gcp:
      type: custom-6-20480
  replicas: 2
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    gcp:
      type: custom-6-20480
  replicas: 3
```

#### [4.5.5. Enabling Shielded VMs](#installation-gcp-enabling-shielded-vms_installing-gcp-customizations) Copy linkLink copied to clipboard!

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).

Note

Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use shielded VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            secureBoot: Enabled
     ```
  2. To use shielded VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            secureBoot: Enabled
     ```
  3. To use shielded VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            secureBoot: Enabled
     ```

#### [4.5.6. Enabling Confidential VMs](#installation-gcp-enabling-confidential-vms_installing-gcp-customizations) Copy linkLink copied to clipboard!

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google’s documentation on [Confidential Computing](https://cloud.google.com/confidential-computing). You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

Note

Confidential VMs are currently not supported on 64-bit ARM architectures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use confidential VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
     ```

     1

     ```
            type: n2d-standard-8
     ```

     2

     ```
            onHostMaintenance: Terminate
     ```

     3

     [1](#CO1-1)
     :   Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional Google Cloud configuration parameters".

     [2](#CO1-2)
     :   Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see [Supported operating systems and machine types](https://cloud.google.com/compute/confidential-vm/docs/os-and-machine-type#machine-type).

     [3](#CO1-3)
     :   Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.
  2. To use confidential VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```
  3. To use confidential VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```

#### [4.5.7. Enabling a user-managed DNS](#installation-gcp-enabling-user-managed-DNS_installing-gcp-customizations) Copy linkLink copied to clipboard!

You can install a cluster with a domain name server (DNS) solution that you manage instead of the default cluster-provisioned DNS solution. As a result, you can manage the API and Ingress DNS records in your own system rather than adding the records to the DNS of the cloud.

For example, your organization’s security policies might not allow the use of public DNS services such as Google Cloud DNS. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services.

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation.

**Prerequisites**

* You installed the `jq` package.

**Procedure**

* Before you deploy your cluster, use a text editor to open the `install-config.yaml` file and add the following stanza:

  + To enable user-managed DNS:

    ```
    platform:
      gcp:
        userProvisionedDNS: Enabled
    ```

    where:

    `Enabled`
    :   Enables user-provisioned DNS management.

For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records".

#### [4.5.8. Sample customized install-config.yaml file for Google Cloud](#installation-gcp-config-yaml_installing-gcp-customizations) Copy linkLink copied to clipboard!

To specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters, you can customize the `install-config.yaml` file.

Important

This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.

```
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
controlPlane:
  name: master
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
compute:
- name: worker
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  gcp:
    projectID: sample-project
    region: us-east1
```

where:

`controlPlane`
:   Specifies parameters that apply to control plane machines.

`compute`
:   Specifies parameters that apply to compute machines.

`networking`
:   Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.

`platform`
:   Specifies parameters that apply to the infrastructure platform that hosts the cluster.

#### [4.5.9. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-gcp-customizations) Copy linkLink copied to clipboard!

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

### [4.6. Managing user-defined labels and tags for Google Cloud](#installing-gcp-user-defined-labels-and-tags_installing-gcp-customizations) Copy linkLink copied to clipboard!

Google Cloud provides labels and tags that help to identify and organize the resources created for a specific OpenShift Container Platform cluster, making them easier to manage.

You can define labels and tags for each Google Cloud resource only during OpenShift Container Platform cluster installation.

Important

User-defined labels and tags are not supported for OpenShift Container Platform clusters upgraded to OpenShift Container Platform 4.22.

Note

You cannot update the tags that are already added. Also, a new tag-supported resource creation fails if the configured tag keys or tag values are deleted.

**User-defined labels**

User-defined labels and OpenShift Container Platform specific labels are applied only to resources created by OpenShift Container Platform installation program and its core components such as:

* Google Cloud filestore CSI Driver Operator
* Google Cloud PD CSI Driver Operator
* Image Registry Operator
* Machine API provider for Google Cloud

User-defined labels are not attached to the resources created by any other Operators or the Kubernetes in-tree components.

User-defined labels and OpenShift Container Platform labels are available on the following Google Cloud resources:

* Compute disk
* Compute forwarding rule
* Compute image
* Compute instance
* DNS managed zone
* Filestore backup
* Filestore instance
* Storage bucket

**Limitations to user-defined labels**

* Labels for `ComputeAddress` are supported in the Google Cloud beta version. OpenShift Container Platform does not add labels to the resource.

**User-defined tags**

User-defined tags are applied only to resources created by OpenShift Container Platform installation program and its core components, such as the following resources:

* Google Cloud FileStore CSI Driver Operator
* Google Cloud PD CSI Driver Operator
* Image Registry Operator
* Machine API provider for Google Cloud

User-defined tags are not attached to the resources created by any other Operators or the Kubernetes in-tree components.

User-defined tags are available on the following Google Cloud resources:

* Compute disk
* Compute instance
* Filestore backup
* Filestore instance
* Storage bucket

**Limitations to the user-defined tags**

* Tags must not be restricted to particular service accounts, because Operators create and use service accounts with minimal roles.
* OpenShift Container Platform does not create any key and value resources of the tag.
* OpenShift Container Platform specific tags are not added to any resource.

#### [4.6.1. Criteria for user-defined labels and tags](#installing-gcp-cluster-label-tag-reference_installing-gcp-customizations) Copy linkLink copied to clipboard!

Before configuring user-defined labels and tags for Google Cloud, consider the importance of meeting the requirements for these tag and labels to ensure proper resource governance.

The following list details the requirements for user-defined labels:

* A label key and value must have a minimum of 1 character and can have a maximum of 63 characters.
* A label key and value must contain only lowercase letters, numeric characters, an underscore (`_`), and a dash (`-`).
* A label key must start with a lowercase letter.
* You can configure a maximum of 32 labels per resource.

  + Each resource has a maximum of 64 labels, where OpenShift Container Platform reserves 32 labels for internal use.

The following list details the requirements for user-defined tags:

* Tag key and tag value must already exist. OpenShift Container Platform does not create the key and the value.
* A tag `parentID` can be either `OrganizationID` or `ProjectID`:

  + `OrganizationID` must consist of decimal numbers without leading zeros.
  + `ProjectID` must be 6 to 30 characters in length, that includes only lowercase letters, numbers, and hyphens.
  + `ProjectID` must start with a letter, and cannot end with a hyphen.
* A tag key must contain only uppercase and lowercase alphanumeric characters, a hyphen (`-`), an underscore (`_`), and a period (`.`).
* A tag value must contain only uppercase and lowercase alphanumeric characters and any of the following characters:

  + A colon (`:`)
  + A comma (`,`)
  + A curly braces (`{}`)
  + A hyphen (`-`)
  + A parentheses (`()`)
  + A percent sign (`%`)
  + A plus (`+`)
  + A pound sign (`$`)
  + A space.
  + A square braces (`[]`)
  + An ampersand (`&`)
  + An asterisk (`*`)
  + An at sign (`@`)
  + An equals sign (`=`)
  + An underscore (`_`)
  + A period (`.`)
* A tag key and value must begin and end with an alphanumeric character.
* Tag value must be one of the predefined values for the key.
* You can configure a maximum of 50 tags.
* Do not define a tag key with the same value as any of the existing tag keys that get inherited from the parent resource.

#### [4.6.2. Configuring user-defined labels and tags for Google Cloud](#installing-gcp-cluster-creation_installing-gcp-customizations) Copy linkLink copied to clipboard!

Configuring user-defined labels and tags for Google Cloud means that you can apply key-value pairs to your cloud resources for the purposes of organizing, managing, and automating your infrastructure.

**Prerequisites**

* The installation program requires that a service account includes a `TagUser` role, so that the program can create the OpenShift Container Platform cluster with defined tags at both organization and project levels.

**Procedure**

* Update the `install-config.yaml` file to define the list of required labels and tags.

  Note

  If you set labels and tags during creation of the `install-config.yaml` configuration file, you cannot create new or update existing labels and tags after creation of the cluster.

  **Sample `install-config.yaml` file**

  ```
  apiVersion: v1
  credentialsMode: Passthrough
  ```

  1

  ```
  platform:
   gcp:
     userLabels:
  ```

  2

  ```
     - key: <label_key>
  ```

  3

  ```
       value: <label_value>
  ```

  4

  ```
     userTags:
  ```

  5

  ```
     - parentID: <OrganizationID/ProjectID>
  ```

  6

  ```
       key: <tag_key_short_name>
       value: <tag_value_short_name>
  # ...
  ```

  [1](#CO2-1)
  :   In passthrough mode, the Cloud Credential Operator (CCO) passes the provided cloud credential to the components that request cloud credentials.

  [2](#CO2-2)
  :   Adds keys and values as labels to the resources created on Google Cloud.

  [3](#CO2-3)
  :   Defines the label name.

  [4](#CO2-4)
  :   Defines the label content.

  [5](#CO2-5)
  :   Adds keys and values as tags to the resources created on Google Cloud.

  [6](#CO2-6)
  :   The ID of the hierarchical resource where you defined the tags at the organization or the project level.

#### [4.6.3. Querying user-defined labels and tags for Google Cloud](#installing-gcp-querying-labels-tags-gcp_installing-gcp-customizations) Copy linkLink copied to clipboard!

After creating the OpenShift Container Platform cluster, you can access the list of the labels and tags defined for the Google Cloud resources in the `infrastructures.config.openshift.io/cluster` object as shown in the following sample `infrastructure.yaml` file.

**Sample `infrastructure.yaml` file**

```
apiVersion: config.openshift.io/v1
kind: Infrastructure
metadata:
 name: cluster
spec:
 platformSpec:
   type: GCP
status:
 infrastructureName: <cluster_id>
```

1

```
 platform: GCP
 platformStatus:
   gcp:
     resourceLabels:
     - key: <label_key>
       value: <label_value>
     resourceTags:
     - key: <tag_key_short_name>
       parentID: <OrganizationID/ProjectID>
       value: <tag_value_short_name>
   type: GCP
```

[1](#CO3-1)
:   The cluster ID that is generated during cluster installation.

Along with the user-defined labels, resources have a label defined by the OpenShift Container Platform. The format of the OpenShift Container Platform labels is `kubernetes-io-cluster-<cluster_id>:owned`.

### [4.7. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-gcp-customizations) Copy linkLink copied to clipboard!

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

### [4.8. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-gcp-customizations) Copy linkLink copied to clipboard!

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

### [4.9. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-gcp-customizations) Copy linkLink copied to clipboard!

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

### [4.10. Alternatives to storing administrator-level secrets in the kube-system project](#installing-gcp-manual-modes_installing-gcp-customizations) Copy linkLink copied to clipboard!

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives:

* To manage long-term cloud credentials manually, follow the procedure in [Manually creating long-term credentials](#manually-create-iam_installing-gcp-customizations "4.10.1. Manually creating long-term credentials").
* To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in [Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-gcp-customizations "4.10.2. Configuring a Google Cloud cluster to use short-term credentials").

#### [4.10.1. Manually creating long-term credentials](#manually-create-iam_installing-gcp-customizations) Copy linkLink copied to clipboard!

The Cloud Credential Operator (CCO) can be put into manual mode prior to installation in environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace.

**Procedure**

1. Add the following granular permissions to the Google Cloud account that the installation program uses:

   * compute.machineTypes.list
   * compute.regions.list
   * compute.zones.list
   * dns.changes.create
   * dns.changes.get
   * dns.managedZones.create
   * dns.managedZones.delete
   * dns.managedZones.get
   * dns.managedZones.list
   * dns.networks.bindPrivateDNSZone
   * dns.resourceRecordSets.create
   * dns.resourceRecordSets.delete
   * dns.resourceRecordSets.list
2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

   **Sample configuration file snippet**

   ```
   apiVersion: v1
   baseDomain: example.com
   credentialsMode: Manual
   # ...
   ```
3. If you have not previously created installation manifest files, do so by running the following command:

   ```
   $ openshift-install create manifests --dir <installation_directory>
   ```

   where `<installation_directory>` is the directory in which the installation program creates files.
4. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
5. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Specifies only the manifests that your specific cluster configuration requires.

   `<path_to_directory_with_installation_configuration>`
   :   Specifies the location of the `install-config.yaml` file.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       This command creates a YAML file for each `CredentialsRequest` object.

       **Sample `CredentialsRequest` object**

       ```
       apiVersion: cloudcredential.openshift.io/v1
       kind: CredentialsRequest
       metadata:
         name: <component_credentials_request>
         namespace: openshift-cloud-credential-operator
         ...
       spec:
         providerSpec:
           apiVersion: cloudcredential.openshift.io/v1
           kind: GCPProviderSpec
           predefinedRoles:
           - roles/storage.admin
           - roles/iam.serviceAccountUser
           skipServiceCheck: true
         ...
       ```
6. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

   **Sample `CredentialsRequest` object with secrets**

   ```
   apiVersion: cloudcredential.openshift.io/v1
   kind: CredentialsRequest
   metadata:
     name: <component_credentials_request>
     namespace: openshift-cloud-credential-operator
     ...
   spec:
     providerSpec:
       apiVersion: cloudcredential.openshift.io/v1
         ...
     secretRef:
       name: <component_secret>
       namespace: <component_namespace>
     ...
   ```

   **Sample `Secret` object**

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: <component_secret>
     namespace: <component_namespace>
   data:
     service_account.json: <base64_encoded_gcp_service_account_file>
   ```

   Important

   Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.

#### [4.10.2. Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-gcp-customizations) Copy linkLink copied to clipboard!

To install a cluster that is configured to use Google Cloud Workload Identity, you must configure the Cloud Credential Operator (CCO) utility and create the required Google Cloud resources for your cluster. Cluster Operators use the credentials created by the CCO. The installation program does not use these credentials.

##### [4.10.2.1. Configuring the Cloud Credential Operator utility](#cco-ccoctl-configuring_installing-gcp-customizations) Copy linkLink copied to clipboard!

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment.

**Prerequisites**

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the OpenShift CLI (`oc`).

* You have added one of the following authentication options to the Google Cloud account that the `ccoctl` utility uses:

  + The **IAM Workload Identity Pool Admin** role
  + The following granular permissions:

    - `compute.projects.get`
    - `iam.googleapis.com/workloadIdentityPoolProviders.create`
    - `iam.googleapis.com/workloadIdentityPoolProviders.get`
    - `iam.googleapis.com/workloadIdentityPools.create`
    - `iam.googleapis.com/workloadIdentityPools.delete`
    - `iam.googleapis.com/workloadIdentityPools.get`
    - `iam.googleapis.com/workloadIdentityPools.undelete`
    - `iam.roles.create`
    - `iam.roles.delete`
    - `iam.roles.list`
    - `iam.roles.undelete`
    - `iam.roles.update`
    - `iam.serviceAccounts.create`
    - `iam.serviceAccounts.delete`
    - `iam.serviceAccounts.getIamPolicy`
    - `iam.serviceAccounts.list`
    - `iam.serviceAccounts.setIamPolicy`
    - `iam.workloadIdentityPoolProviders.get`
    - `iam.workloadIdentityPools.delete`
    - `resourcemanager.projects.get`
    - `resourcemanager.projects.getIamPolicy`
    - `resourcemanager.projects.setIamPolicy`
    - `storage.buckets.create`
    - `storage.buckets.delete`
    - `storage.buckets.get`
    - `storage.buckets.getIamPolicy`
    - `storage.buckets.setIamPolicy`
    - `storage.objects.create`
    - `storage.objects.delete`
    - `storage.objects.list`

**Procedure**

1. Set a variable for the OpenShift Container Platform release image by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:

   ```
   $ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
   ```

   Note

   Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
3. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:

   ```
   $ oc image extract $CCO_IMAGE \
     --file="/usr/bin/ccoctl.<rhel_version>" \
     -a ~/.pull-secret
   ```

   For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid:

   * `rhel8`: Specify this value for hosts that use RHEL 8.
   * `rhel9`: Specify this value for hosts that use RHEL 9.

   Note

   The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
4. Change the permissions to make `ccoctl` executable by running the following command:

   ```
   $ chmod 775 ccoctl
   ```

**Verification**

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:

  ```
  $ ./ccoctl
  ```

  **Example output**

  ```
  OpenShift credentials provisioning tool

  Usage:
    ccoctl [command]

  Available Commands:
    aws          Manage credentials objects for AWS cloud
    azure        Manage credentials objects for Azure
    gcp          Manage credentials objects for Google cloud
    help         Help about any command
    ibmcloud     Manage credentials objects for IBM Cloud
    nutanix      Manage credentials objects for Nutanix

  Flags:
    -h, --help   help for ccoctl

  Use "ccoctl [command] --help" for more information about a command.
  ```

##### [4.10.2.2. Creating Google Cloud resources with the Cloud Credential Operator utility](#cco-ccoctl-creating-at-once_installing-gcp-customizations) Copy linkLink copied to clipboard!

You can use the `ccoctl gcp create-all` command to automate the creation of Google Cloud resources.

Note

By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.

**Prerequisites**

You must have:

* Extracted and prepared the `ccoctl` binary.

**Procedure**

1. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Specifies to include only the manifests that your specific cluster configuration requires.

   `<path_to_directory_with_installation_configuration>`
   :   Specifies the location of the `install-config.yaml` file.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       Note

       This command might take a few moments to run.
3. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:

   ```
   $ ccoctl gcp create-all \
     --name=<name> \
     --region=<gcp_region> \
     --project=<gcp_project_id> \
     --credentials-requests-dir=<path_to_credentials_requests_directory> \
     --key-storage-method=<key_storage_method>
   ```

   where:

   `<name>`
   :   Specifies the user-defined name for all created Google Cloud resources used for tracking. If you plan to install the Google Cloud Filestore Container Storage Interface (CSI) Driver Operator, retain this value.

   `<gcp_region>`
   :   Specifies the Google Cloud region in which cloud resources will be created.

   `<gcp_project_id>`
   :   Specifies the Google Cloud project ID in which cloud resources will be created.

   `<path_to_credentials_requests_directory>`
   :   Specifies the directory containing the files of `CredentialsRequest` manifests to create Google Cloud service accounts.

   `<key_storage_method>`
   :   Specifies the method for storing OIDC JWK files. Accepted values are `public-bucket` and `pool-jwk-file`. The default value `public-bucket` creates a public GCS bucket to host the OIDC configuration and JWK files. The `pool-jwk-file` value attaches the JWK directly to the workload identity pool provider without creating a public bucket. This parameter is optional.

       Note

       If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.

**Verification**

* To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory:

  ```
  $ ls <path_to_ccoctl_output_dir>/manifests
  ```

  **Example output**

  ```
  cluster-authentication-02-config.yaml
  openshift-cloud-controller-manager-gcp-ccm-cloud-credentials-credentials.yaml
  openshift-cloud-credential-operator-cloud-credential-operator-gcp-ro-creds-credentials.yaml
  openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
  openshift-cluster-api-capg-manager-bootstrap-credentials-credentials.yaml
  openshift-cluster-csi-drivers-gcp-pd-cloud-credentials-credentials.yaml
  openshift-image-registry-installer-cloud-credentials-credentials.yaml
  openshift-ingress-operator-cloud-credentials-credentials.yaml
  openshift-machine-api-gcp-cloud-credentials-credentials.yaml
  ```

  You can verify that the IAM service accounts are created by querying Google Cloud. For more information, refer to Google Cloud documentation on listing IAM service accounts.

##### [4.10.2.3. Restricting service account impersonation to the compute nodes service account](#restricting-sa-impersonation-compute-sa-gcp_installing-gcp-customizations) Copy linkLink copied to clipboard!

After the Cloud Credential Operator utility (`ccoctl`) creates the resources for the cluster, you can restrict the Google Cloud `iam.serviceAccounts.actAs` permission that the `ccoctl` utility granted to the Machine API controller service account to the compute nodes service account.

Note

Restricting service account impersonation to the compute nodes service account is optional. If your organization does not require this change, you can continue to "Incorporating the Cloud Credential Operator utility manifests".

When the `ccoctl` utility assigns custom and Google Cloud predefined roles to OpenShift Container Platform components service accounts, it grants the `iam.serviceAccounts.actAs` permission to the Machine API controller service account at the Google Cloud project level. To reduce the scope of the `iam.serviceAccounts.actAs` permission, you identify the custom role of the Machine API controller service account and replace it with a role that has a more restricted set of permissions. To allow this component to work, you then grant the Machine API controller service account the Service Account User role on the service account of the compute nodes instead.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have used the `ccoctl` utility to create the cloud provider resources for your cluster.
* You have access to your `install-config.yaml` file.
* You have logged in to the Google Cloud CLI (`gcloud`) as a user with permissions to manage service accounts and roles.

**Procedure**

1. Obtain the following values from your `install-config.yaml` file:

   * The Google Cloud project name. In the YAML file, this is the value of the `platform.gcp.projectID` parameter.
   * The cluster name. In the YAML file, this is the value of the `metadata.name` parameter.
   * The service account for the compute nodes. In the YAML file, this is the value of the `compute[0].platform.gcp.serviceAccount` parameter.
2. Obtain the service account for the Machine API controller that the `ccoctl` utility created by running the following command:

   ```
   $ gcloud iam service-accounts list \
     --filter="displayName=<cluster_name>-openshift-machine-api-gcp" \
     --format='value(email)'
   ```

   where `<cluster_name>` is the value specified for the `metadata.name` parameter in your `install-config.yaml` file.
3. Obtain the role ID of the custom role for the Machine API controller service account by running the following command:

   ```
   $ gcloud projects get-iam-policy <project_name> \
     --flatten='bindings[].members' \
     --format='table(bindings.role)' \
     --filter="bindings.members:<machine_api_controller_service_account>"
   ```

   where `<machine_api_controller_service_account>` is the Machine API controller service account.
4. List the custom role permissions for the Machine API controller service account by running the following command:

   ```
   $ gcloud iam roles describe <machine_api_role> \
     --project <project_name>
   ```

   where `<machine_api_role>` is the role ID of the custom role for the Machine API controller service account.

   **Example output**

   ```
   etag: <etag_value>
   includedPermissions:
   - compute.acceleratorTypes.get
   - compute.acceleratorTypes.list
   - compute.disks.create
   - compute.disks.createTagBinding
   ...
   - compute.zones.get
   - compute.zones.list
   - iam.serviceAccounts.actAs
   - iam.serviceAccounts.get
   - iam.serviceAccounts.list
   - resourcemanager.tagValues.get
   - resourcemanager.tagValues.list
   - serviceusage.quotas.get
   - serviceusage.services.get
   - serviceusage.services.list
   name: projects/<project_name>/roles/<machine_api_role>
   stage: GA
   title: <project_name>-openshift-machine-api-gcp
   ```

   where `<project_name>` is the Google Cloud project name specified in the `install-config.yaml` file.

   Note

   This truncated example output might not match the permissions list for your cluster.
5. Create a custom role that includes all of the permissions from your output except for the `iam.serviceAccounts.actAs` permission by running a command similar to the following:

   ```
   $ gcloud iam roles create <machine_api_role>_without_actas \
   --project=<project_name> \
   --title=<machine_api_role>_without_actas \
   --description="Required permissions for the Machine API controller without the iam.serviceAccounts.actAs permission" \
   --permissions=compute.acceleratorTypes.get,\
   compute.acceleratorTypes.list,\
   compute.disks.create,\
   compute.disks.createTagBinding,\
   ...
   compute.zones.get,\
   compute.zones.list,\
   iam.serviceAccounts.get,\
   iam.serviceAccounts.list,\
   resourcemanager.tagValues.get,\
   resourcemanager.tagValues.list,\
   serviceusage.quotas.get,\
   serviceusage.services.get,\
   serviceusage.services.list
   ```

   In this example, the new role name is the original custom role name, `<machine_api_role>`, with a `_without_actas` string added to the end.

   Important

   This truncated example command might not match the permissions list for your cluster. You must use the list of permissions from the output of the `gcloud iam roles describe <machine_api_role> --project <project_name>` command on your cluster.
6. Remove the custom role that includes the `iam.serviceAccounts.actAs` permission from the Machine API controller service account by running the following command:

   ```
   $ gcloud projects remove-iam-policy-binding <project_name> \
     --member "serviceAccount:<machine_api_controller_service_account>" \
     --role "projects/<project_name>/roles/<machine_api_role>"
   ```

   where `<machine_api_role>` is the original custom role.
7. Grant the custom role that excludes the `iam.serviceAccounts.actAs` permission to the Machine API controller service account by running the following command:

   ```
   $ gcloud projects add-iam-policy-binding <project_name> \
     --member "serviceAccount:<machine_api_controller_service_account>" \
     --role "projects/<project_name>/roles/<machine_api_role>_without_actas
   ```

   where `<machine_api_role>_without_actas` is the new custom role.
8. Optional: To verify that the Machine API controller service account has the correct role, check the attached role ID by running the following command:

   ```
   $ gcloud projects get-iam-policy <project_name> \
     --flatten='bindings[].members' \
     --format='table(bindings.role)' \
     --filter="bindings.members:<machine_api_controller_service_account>"
   ```

   **Example output**

   ```
   ROLE
   projects/<project_name>/roles/<machine_api_role>_without_actas
   ```
9. Grant the Machine API controller service account the Service Account User role on the service account of the compute nodes by running the following command:

   ```
   $ gcloud iam service-accounts add-iam-policy-binding <compute_nodes_service_account> \
     --member="serviceAccount:<machine_api_controller_service_account>" \
     --role=roles/iam.serviceAccountUser
   ```

   where `<compute_nodes_service_account>` is the service account for your compute nodes. This value is the `compute[0].platform.gcp.serviceAccount` parameter in your `install-config.yaml` file.

##### [4.10.2.4. Incorporating the Cloud Credential Operator utility manifests](#cco-ccoctl-install-creating-manifests_installing-gcp-customizations) Copy linkLink copied to clipboard!

To implement short-term security credentials managed outside the cluster for individual components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have configured the Cloud Credential Operator utility (`ccoctl`).
* You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility.

**Procedure**

1. Add the following granular permissions to the Google Cloud account that the installation program uses:

   * compute.machineTypes.list
   * compute.regions.list
   * compute.zones.list
   * dns.changes.create
   * dns.changes.get
   * dns.managedZones.create
   * dns.managedZones.delete
   * dns.managedZones.get
   * dns.managedZones.list
   * dns.networks.bindPrivateDNSZone
   * dns.resourceRecordSets.create
   * dns.resourceRecordSets.delete
   * dns.resourceRecordSets.list
2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

   **Sample configuration file snippet**

   ```
   apiVersion: v1
   baseDomain: example.com
   credentialsMode: Manual
   # ...
   ```
3. If you have not previously created installation manifest files, do so by running the following command:

   ```
   $ openshift-install create manifests --dir <installation_directory>
   ```

   where `<installation_directory>` is the directory in which the installation program creates files.
4. Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command:

   ```
   $ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
   ```
5. Copy the `tls` directory that contains the private key to the installation directory:

   ```
   $ cp -a /<path_to_ccoctl_output_dir>/tls .
   ```

### [4.11. Using the Google Cloud Marketplace offering](#installation-gcp-marketplace_installing-gcp-customizations) Copy linkLink copied to clipboard!

Using the Google Cloud Marketplace offering lets you deploy an OpenShift Container Platform cluster, which is billed on pay-per-use basis (hourly, per core) through Google Cloud, while still being supported directly by Red Hat.

By default, the installation program downloads and installs the Red Hat Enterprise Linux CoreOS (RHCOS) image that is used to deploy compute machines. To deploy an OpenShift Container Platform cluster using an RHCOS image from the Google Cloud Marketplace, override the default behavior by modifying the `install-config.yaml` file to reference the location of Google Cloud Marketplace offer.

Note

You should only modify the RHCOS image for compute machines to use a Google Cloud Marketplace image. Control plane machines and infrastructure nodes do not require an OpenShift Container Platform subscription and use the public RHCOS default image by default, which does not incur subscription costs on your Google Cloud bill. Therefore, you should not modify the cluster default boot image or the control plane boot images. Applying the Google Cloud Marketplace image to them will incur additional licensing costs that cannot be recovered.

**Prerequisites**

* You have an existing `install-config.yaml` file.

**Procedure**

1. Edit the `compute.platform.gcp.osImage` parameters to specify the location of the Google Cloud Marketplace image:

   * Set the `project` parameter to `redhat-marketplace-public`
   * Set the `name` parameter to one of the following offers:

     OpenShift Container Platform
     :   `redhat-coreos-ocp-413-x86-64-202305021736`

     OpenShift Platform Plus
     :   `redhat-coreos-opp-413-x86-64-202305021736`

     OpenShift Kubernetes Engine
     :   `redhat-coreos-oke-413-x86-64-202305021736`
2. Save the file and reference it when deploying the cluster.

**Sample `install-config.yaml` file that specifies a Google Cloud Marketplace image for compute machines**

```
apiVersion: v1
baseDomain: example.com
controlPlane:
# ...
compute:
  platform:
    gcp:
      osImage:
        project: redhat-marketplace-public
        name: redhat-coreos-ocp-413-x86-64-202305021736
# ...
```

### [4.12. Network configuration phases](#nw-network-config_installing-gcp-customizations) Copy linkLink copied to clipboard!

There are two phases prior to OpenShift Container Platform installation where you can customize the network configuration. Customize settings in the `install-config.yaml` file and in the Cluster Network Operator manifest across two configuration phases.

Phase 1
:   You can customize the following network-related fields in the `install-config.yaml` file before you create the manifest files:

    * `networking.networkType`
    * `networking.clusterNetwork`
    * `networking.serviceNetwork`
    * `networking.machineNetwork`
    * `nodeNetworking`

      For more information, see "Installation configuration parameters".

      Note

      Set the `networking.machineNetwork` to match the Classless Inter-Domain Routing (CIDR) where the preferred subnet is located.

      Important

      The CIDR range `172.17.0.0/16` is reserved by `libVirt`. You cannot use any other CIDR range that overlaps with the `172.17.0.0/16` CIDR range for networks in your cluster.

Phase 2
:   After creating the manifest files by running `openshift-install create manifests`, you can define a customized Cluster Network Operator manifest with only the fields you want to modify. You can use the manifest to specify an advanced network configuration.

During phase 2, you cannot override the values that you specified in phase 1 in the `install-config.yaml` file. However, you can customize the network plugin during phase 2.

### [4.13. Specifying advanced network configuration](#modifying-nwoperator-config-startup_installing-gcp-customizations) Copy linkLink copied to clipboard!

To integrate your OpenShift Container Platform cluster with your existing network environment, you can specify advanced network configuration in a manifest before you install the cluster. Advanced network configuration can be configured only during cluster installation.

Important

Customizing your network configuration by modifying the OpenShift Container Platform manifest files created by the installation program is not supported. Applying a manifest file that you create, as in the following procedure, is supported.

**Prerequisites**

* You have created the `install-config.yaml` file and completed any modifications to it.

**Procedure**

1. Change to the directory that contains the installation program and create the manifests:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```

   The `<installation_directory>` specifies the name of the directory that contains the `install-config.yaml` file for your cluster.
2. Create a stub manifest file for the advanced network configuration that is named `cluster-network-03-config.yml` in the `<installation_directory>/manifests/` directory:

   ```
   apiVersion: operator.openshift.io/v1
   kind: Network
   metadata:
     name: cluster
   spec:
   ```
3. Specify the advanced network configuration for your cluster in the `cluster-network-03-config.yml` file, such as in the following example:

   **Enable IPsec for the OVN-Kubernetes network provider**

   ```
   apiVersion: operator.openshift.io/v1
   kind: Network
   metadata:
     name: cluster
   spec:
     defaultNetwork:
       ovnKubernetesConfig:
         ipsecConfig:
           mode: Full
   ```
4. Optional: Back up the `manifests/cluster-network-03-config.yml` file. The installation program consumes the `manifests/` directory when you create the Ignition config files.
5. Remove the Kubernetes manifest files that define the control plane machines and compute `MachineSets`:

   ```
   $ rm -f openshift/99_openshift-cluster-api_master-machines-*.yaml openshift/99_openshift-cluster-api_worker-machineset-*.yaml
   ```

   Because you create and manage these resources yourself, you do not have to initialize them.

   * You can preserve the `MachineSet` files to create compute machines by using the machine API, but you must update references to them to match your environment.

### [4.14. Cluster Network Operator configuration](#nw-operator-cr_installing-gcp-customizations) Copy linkLink copied to clipboard!

To manage cluster networking, configure the Cluster Network Operator (CNO) `Network` custom resource (CR) named `cluster` so the cluster uses the correct IP ranges and network plugin settings for reliable pod and service connectivity. Some settings and fields are inherited at the time of install or by the `default.Network.type` plugin, OVN-Kubernetes.

The CNO configuration inherits the following fields during cluster installation from the `Network` API in the `Network.config.openshift.io` API group:

`clusterNetwork`
:   IP address pools from which pod IP addresses are allocated.

`serviceNetwork`
:   IP address pool for services.

`defaultNetwork.type`
:   Cluster network plugin. `OVNKubernetes` is the only supported plugin during installation.

You can specify the cluster network plugin configuration for your cluster by setting the fields for the `defaultNetwork` object in the CNO object named `cluster`.

#### [4.14.1. Cluster Network Operator configuration object](#nw-operator-cr-cno-object_installing-gcp-customizations) Copy linkLink copied to clipboard!

The fields for the Cluster Network Operator (CNO) are described in the following table:

Expand

Table 4.2. Cluster Network Operator configuration object

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

#### [4.14.2. defaultNetwork object configuration](#nw-operator-cr-defaultnetwork_installing-gcp-customizations) Copy linkLink copied to clipboard!

The values for the `defaultNetwork` object are defined in the following table:

Expand

Table 4.3. defaultNetwork object

| Field | Type | Description |
| --- | --- | --- |
| `type` | `string` | `OVNKubernetes`. The Red Hat OpenShift Networking network plugin is selected during installation. This value cannot be changed after cluster installation.  Note  OpenShift Container Platform uses the OVN-Kubernetes network plugin by default. |
| `ovnKubernetesConfig` | `object` | This object is only valid for the OVN-Kubernetes network plugin. |

Show more

#### [4.14.3. Configuration for the OVN-Kubernetes network plugin](#nw-operator-configuration-parameters-for-ovn-sdn_installing-gcp-customizations) Copy linkLink copied to clipboard!

The following table describes the configuration fields for the OVN-Kubernetes network plugin:

Expand

Table 4.4. ovnKubernetesConfig object

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

Table 4.5. ovnKubernetesConfig.ipv4 object

| Field | Type | Description |
| --- | --- | --- |
| `internalTransitSwitchSubnet` | string | If your existing network infrastructure overlaps with the `100.88.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.  The default value is `100.88.0.0/16`. |
| `internalJoinSubnet` | string | If your existing network infrastructure overlaps with the `100.64.0.0/16` IPv4 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster. For example, if the `clusterNetwork.cidr` value is `10.128.0.0/14` and the `clusterNetwork.hostPrefix` value is `/23`, then the maximum number of nodes is `2^(23-14)=512`.  The default value is `100.64.0.0/16`. |

Show more

Expand

Table 4.6. ovnKubernetesConfig.ipv6 object

| Field | Type | Description |
| --- | --- | --- |
| `internalTransitSwitchSubnet` | string | If your existing network infrastructure overlaps with the `fd97::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. The subnet for the distributed transit switch that enables east-west traffic. This subnet cannot overlap with any other subnets used by OVN-Kubernetes or on the host itself. It must be large enough to accommodate one IP address per node in your cluster.  The default value is `fd97::/64`. |
| `internalJoinSubnet` | string | If your existing network infrastructure overlaps with the `fd98::/64` IPv6 subnet, you can specify a different IP address range for internal use by OVN-Kubernetes. You must ensure that the IP address range does not overlap with any other subnet used by your OpenShift Container Platform installation. The IP address range must be larger than the maximum number of nodes that can be added to the cluster.  The default value is `fd98::/64`. |

Show more

Expand

Table 4.7. policyAuditConfig object

| Field | Type | Description |
| --- | --- | --- |
| `rateLimit` | integer | The maximum number of messages to generate every second per node. The default value is `20` messages per second. |
| `maxFileSize` | integer | The maximum size for the audit log in bytes. The default value is `50000000` or 50 MB. |
| `maxLogFiles` | integer | The maximum number of log files that are retained. |
| `destination` | string | One of the following additional audit log targets:  `libc`  The libc `syslog()` function of the journald process on the host.  `udp:<host>:<port>`  A syslog server. Replace `<host>:<port>` with the host and port of the syslog server.  `unix:<file>`  A Unix Domain Socket file specified by `<file>`.  `null`  Do not send the audit logs to any additional target. |
| `syslogFacility` | string | The syslog facility, such as `kern`, as defined by RFC5424. The default value is `local0`. |

Show more

Expand

Table 4.8. gatewayConfig object

| Field | Type | Description |
| --- | --- | --- |
| `routingViaHost` | `boolean` | Set this field to `true` to send egress traffic from pods to the host networking stack. For highly-specialized installations and applications that rely on manually configured routes in the kernel routing table, you might want to route egress traffic to the host networking stack. By default, egress traffic is processed in OVN to exit the cluster and is not affected by specialized routes in the kernel routing table. The default value is `false`.  This field has an interaction with the Open vSwitch hardware offloading feature. If you set this field to `true`, you do not receive the performance benefits of the offloading because egress traffic is processed by the host networking stack. |
| `ipForwarding` | `object` | You can control IP forwarding for all traffic on OVN-Kubernetes managed interfaces by using the `ipForwarding` specification in the `Network` resource. Specify `Restricted` to only allow IP forwarding for Kubernetes related traffic. Specify `Global` to allow forwarding of all IP traffic. For new installations, the default is `Restricted`. For updates to OpenShift Container Platform 4.14 or later, the default is `Global`.  Note  The default value of `Restricted` sets the IP forwarding to drop. |
| `ipv4` | `object` | Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv4 addresses. |
| `ipv6` | `object` | Optional: Specify an object to configure the internal OVN-Kubernetes masquerade address for host to service traffic for IPv6 addresses. |

Show more

Expand

Table 4.9. gatewayConfig.ipv4 object

| Field | Type | Description |
| --- | --- | --- |
| `internalMasqueradeSubnet` | `string` | The masquerade IPv4 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `169.254.169.0/29`.  Important  For OpenShift Container Platform 4.17 and later versions, clusters use `169.254.0.0/17` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet. |

Show more

Expand

Table 4.10. gatewayConfig.ipv6 object

| Field | Type | Description |
| --- | --- | --- |
| `internalMasqueradeSubnet` | `string` | The masquerade IPv6 addresses that are used internally to enable host to service traffic. The host is configured with these IP addresses as well as the shared gateway bridge interface. The default value is `fd69::/125`.  Important  For OpenShift Container Platform 4.17 and later versions, clusters use `fd69::/112` as the default masquerade subnet. For upgraded clusters, there is no change to the default masquerade subnet. |

Show more

Expand

Table 4.11. ipsecConfig object

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

### [4.15. Deploying the cluster](#installation-launching-installer_installing-gcp-customizations) Copy linkLink copied to clipboard!

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

Important

You can run the `create cluster` command of the installation program only once, during initial installation.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

**Procedure**

1. Remove any existing Google Cloud credentials that do not use the service account key for the Google Cloud account that you configured for your cluster and that are stored in the following locations:

   * The `GOOGLE_CREDENTIALS`, `GOOGLE_CLOUD_KEYFILE_JSON`, or `GCLOUD_KEYFILE_JSON` environment variables
   * The `~/.gcp/osServiceAccount.json` file
   * The `gcloud cli` default credentials
2. In the directory that contains the installation program, initialize the cluster deployment by running the following command:

   ```
   $ ./openshift-install create cluster --dir <installation_directory> \
       --log-level=info
   ```

   * For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.
   * To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.
3. Optional: You can reduce the number of permissions for the service account that you used to install the cluster.

   * If you assigned the `Owner` role to your service account, you can remove that role and replace it with the `Viewer` role.
   * If you included the `Service Account Key Admin` role, you can remove it.

**Verification**

When the cluster deployment completes successfully:

* The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.
* Credential information also outputs to `<installation_directory>/.openshift_install.log`.

  Important

  Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.

  **Example output**

  ```
  ...
  INFO Install complete!
  INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
  INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
  INFO Login to the console with user: "kubeadmin", and password: "password"
  INFO Time elapsed: 36m22s
  ```

  Important

  + The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
  + It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

### [4.16. Provisioning your own DNS records](#installation-gcp-provisioning-own-dns-records_installing-gcp-customizations) Copy linkLink copied to clipboard!

Use the IP address of the API server to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. Use the IP address of the Ingress service to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

Important

Before you use this feature, you must add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS".

**Prerequisites**

* You installed your cluster.
* You installed the `gcloud` CLI tool.

**Procedure**

1. Determine the infrastructure ID of your cluster by running the following command:

   ```
   $ infra_id=$(jq -r .infraID <installation_directory>/metadata.json)
   ```

   where:

   `<installation_directory>`
   :   Specifies the directory where you ran the installation program.
2. Find the IP address of the API server:

   1. If you installed a private cluster, determine the IP address of the API server by running the following command:

      ```
      $ gcloud compute forwarding-rules describe "${infra_id}-api-internal" --project=<project_name> --region <region_name> --format json | jq -r .IPAddress
      ```

      where:

      `<project_name>`
      :   Specifies the name of your Google Cloud project.

      `<region_name>`
      :   Specifies the region where you installed your cluster.
   2. If you installed a public cluster, determine the IP address of the API server by running the following command:

      ```
      $ gcloud compute forwarding-rules describe --global "${infra_id}-apiserver" --format json | jq -r .IPAddress
      ```
3. Use the IP address to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.
4. Find the IP address of the Ingress service:

   1. If you installed a private cluster, find the IP address of the Ingress service by running the following command:

      ```
      $ gcloud compute forwarding-rules list --project=<project_name> --filter="subnetwork:(projects/<project_name>/regions/<region_name>/subnetworks/<compute_subnet_name>)" --format="json" | jq -r '.[].IPAddress'
      ```

      where:

      `<project_name>`
      :   Specifies the name of your Google Cloud project.

      `<region_name>`
      :   Specifies the region where you installed your cluster.

      `<compute_subnet_name>`
      :   Specifies the name of the subnet that contains your compute nodes.
   2. If you installed a public cluster, find the IP address by using the forwarding rule:

      1. Find the forwarding rule for the Ingress service by running the following command:

         ```
         $ ingress_forwarding_rule=$(gcloud compute target-pools list --format=json --filter="instances[]~${infra_id}" | jq -r .[].name)
         ```
      2. Use the forwarding rule value to find the IP address of the Ingress service by running the following command:

         ```
         $ gcloud compute forwarding-rules describe --region "<region_name>" "${ingress_forwarding_rule}" --format json | jq -r .IPAddress
         ```

         where:

         `<region_name>`
         :   Specifies the region where you installed your cluster.
5. Use the IP address to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

### [4.17. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-gcp-customizations) Copy linkLink copied to clipboard!

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

### [4.18. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-gcp-customizations) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

### [4.19. Next steps](#next-steps-3) Copy linkLink copied to clipboard!

* [Customize your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations).
* If necessary, you can [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting).

## [Chapter 5. Installing a cluster on Google Cloud in a disconnected environment](#installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you can install a cluster on Google Cloud in a restricted network by creating an internal mirror of the installation release content on an existing Google Virtual Private Cloud (VPC).

Important

You can install an OpenShift Container Platform cluster by using mirrored installation release content, but your cluster will require internet access to use the Google Cloud APIs.

### [5.1. Prerequisites](#prerequisites_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

* You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes.
* You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing).
* You [configured a Google Cloud project](#installing-gcp-account "Chapter 2. Configuring a Google Cloud project") to host the cluster.
* You [mirrored the images for a disconnected installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installation-about-mirror-registry_installing-mirroring-installation-images) to your registry and obtained the `imageContentSources` data for your version of OpenShift Container Platform.

  Important

  Because the installation media is on the mirror host, you can use that computer to complete all installation steps.
* You have an existing VPC in Google Cloud. While installing a cluster in a restricted network that uses installer-provisioned infrastructure, you cannot use the installer-provisioned VPC. You must use a user-provisioned VPC that satisfies one of the following requirements:

  + Contains the mirror registry
  + Has firewall rules or a peering connection to access the mirror registry hosted elsewhere
* If you use a firewall, you [configured it to allow the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires access to. While you might need to grant access to more sites, you must grant access to `*.googleapis.com` and `accounts.google.com`.
* If you are installing using a [Private Service Connect (PSC) endpoint](https://cloud.google.com/vpc/docs/private-service-connect), you must configure the endpoint in the same Virtual Private Cloud (VPC) where you install the cluster, specified in the `install-config.yaml` file, as described in [Installing a cluster on Google Cloud into an existing VPC](#installing-gcp-vpc "Chapter 6. Installing a cluster on Google Cloud into an existing VPC").

### [5.2. About installations in restricted networks](#installation-about-restricted-networks_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

You can install OpenShift Container Platform 4.22 in a restricted network without an active internet connection to obtain software components. Restricted network installations can use installer-provisioned or user-provisioned infrastructure, depending on the cloud platform to which you are installing the cluster.

If you perform a restricted network installation on a cloud platform, you still require access to its cloud APIs. Some cloud functions, such as Amazon Web Service’s Route 53 DNS and IAM services, require internet access. Depending on your network, you might require less internet access for an installation on bare-metal hardware, Nutanix, or on VMware vSphere.

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and has the installation media. You can create this registry on a mirror host, which can access both the internet and your closed network, or by using other methods that meet your restrictions.

#### [5.2.1. Additional limits](#installation-restricted-network-limits_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

Clusters in restricted networks have the following additional limitations and restrictions:

* The `ClusterVersion` status includes an `Unable to retrieve available updates` error.
* By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags.

### [5.3. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to obtain the images that are necessary to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

### [5.4. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

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

### [5.5. Creating the installation configuration file](#installation-initializing_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

You can customize the OpenShift Container Platform cluster you install on Google Cloud.

**Prerequisites**

* You have the OpenShift Container Platform installation program and the pull secret for your cluster. For a restricted network installation, these files are on your mirror host.
* You have the `imageContentSources` values that were generated during mirror registry creation.
* You have obtained the contents of the certificate for your mirror registry.
* Configure a Google Cloud account.

**Procedure**

1. Create the `install-config.yaml` file.

   1. Change to the directory that contains the installation program and run the following command:

      ```
      $ ./openshift-install create install-config --dir <installation_directory>
      ```

      * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

        When specifying the directory:
      * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
      * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
   2. At the prompts, provide the configuration details for your cloud:

      1. Optional: Select an SSH key to use to access your cluster machines.

         Note

         For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
      2. Select **gcp** as the platform to target.
      3. If you have not configured the service account key for your Google Cloud account on your computer, you must obtain it from Google Cloud and paste the contents of the file or enter the absolute path to the file.
      4. Select the project ID to provision the cluster in. The default value is specified by the service account that you configured.
      5. Select the region to deploy the cluster to.
      6. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.
      7. Enter a descriptive name for your cluster.
2. Edit the `install-config.yaml` file to give the additional information that is required for an installation in a restricted network.

   1. Update the `pullSecret` value to contain the authentication information for your registry:

      ```
      pullSecret: '{"auths":{"<mirror_host_name>:5000": {"auth": "<credentials>","email": "you@example.com"}}}'
      ```

      For `<mirror_host_name>`, specify the registry domain name that you specified in the certificate for your mirror registry, and for `<credentials>`, specify the base64-encoded user name and password for your mirror registry.
   2. Add the `additionalTrustBundle` parameter and value.

      ```
      additionalTrustBundle: |
        -----BEGIN CERTIFICATE-----
        ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
        -----END CERTIFICATE-----
      ```

      The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority, or the self-signed certificate that you generated for the mirror registry.
   3. Define the network and subnets for the VPC to install the cluster in under the parent `platform.gcp` field:

      ```
      platform:
        gcp:
          network: <existing_vpc>
          controlPlaneSubnet: <control_plane_subnet>
          computeSubnet: <compute_subnet>
      ```

      For `platform.gcp.network`, specify the name for the existing Google VPC. For `platform.gcp.controlPlaneSubnet` and `platform.gcp.computeSubnet`, specify the existing subnets to deploy the control plane machines and compute machines, respectively.
   4. Add the image content resources, which resemble the following YAML excerpt:

      ```
      imageContentSources:
      - mirrors:
        - <mirror_host_name>:5000/<repo_name>/release
        source: quay.io/openshift-release-dev/ocp-release
      - mirrors:
        - <mirror_host_name>:5000/<repo_name>/release
        source: registry.redhat.io/ocp/release
      ```

      For these values, use the `imageContentSources` that you recorded during mirror registry creation.
   5. Optionally, set the publishing strategy to `Internal`:

      ```
      publish: Internal
      ```

      By setting this option, you create an internal Ingress Controller and a private load balancer.
3. Make any other modifications to the `install-config.yaml` file that you require.

   For more information about the parameters, see "Installation configuration parameters".
4. Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

   Important

   The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

#### [5.5.1. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 5.1. Minimum resource requirements

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Show more

* One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
* OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance.
* As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines.

Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* ppc64le architecture requires IBM® Power9 ISA
* s390x architecture requires IBM® z14 ISA

For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

#### [5.5.2. Tested instance types for Google Cloud](#installation-gcp-tested-machine-types_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

The following Google Cloud instance types have been tested with OpenShift Container Platform.

Note

Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) (Google documentation).

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see [machine series support for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in *Storage*.

See the following machine series:

* `A2`
* `A3`
* `C2`
* `C2D`
* `C3`
* `C3D`
* `C4`
* `E2`
* `M1`
* `N1`
* `N2`
* `N2D`
* `N4`
* `Tau T2D`

#### [5.5.3. Tested instance types for Google Cloud on 64-bit ARM infrastructures](#installation-gcp-tested-machine-types-arm_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

The following Google Cloud 64-bit ARM instance types have been tested with OpenShift Container Platform.

See the following machine series for 64-bit ARM machines:

* `C4A`
* `N4A`
* `Tau T2A`

#### [5.5.4. Using custom machine types](#installation-custom-machine-types_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

Using a custom machine type to install a OpenShift Container Platform cluster is supported.

Consider the following when using a custom machine type:

* Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation".
* The name of the custom machine type must adhere to the following syntax:

  `custom-<number_of_cpus>-<amount_of_memory_in_mb>`

  For example, `custom-6-20480`.

As part of the installation process, you specify the custom machine type in the `install-config.yaml` file.

**Sample `install-config.yaml` file with a custom machine type**

```
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  platform:
    gcp:
      type: custom-6-20480
  replicas: 2
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    gcp:
      type: custom-6-20480
  replicas: 3
```

#### [5.5.5. Enabling Shielded VMs](#installation-gcp-enabling-shielded-vms_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).

Note

Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use shielded VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            secureBoot: Enabled
     ```
  2. To use shielded VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            secureBoot: Enabled
     ```
  3. To use shielded VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            secureBoot: Enabled
     ```

#### [5.5.6. Enabling Confidential VMs](#installation-gcp-enabling-confidential-vms_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google’s documentation on [Confidential Computing](https://cloud.google.com/confidential-computing). You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

Note

Confidential VMs are currently not supported on 64-bit ARM architectures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use confidential VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
     ```

     1

     ```
            type: n2d-standard-8
     ```

     2

     ```
            onHostMaintenance: Terminate
     ```

     3

     [1](#CO4-1)
     :   Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional Google Cloud configuration parameters".

     [2](#CO4-2)
     :   Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see [Supported operating systems and machine types](https://cloud.google.com/compute/confidential-vm/docs/os-and-machine-type#machine-type).

     [3](#CO4-3)
     :   Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.
  2. To use confidential VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```
  3. To use confidential VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```

#### [5.5.7. Enabling a user-managed DNS](#installation-gcp-enabling-user-managed-DNS_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

You can install a cluster with a domain name server (DNS) solution that you manage instead of the default cluster-provisioned DNS solution. As a result, you can manage the API and Ingress DNS records in your own system rather than adding the records to the DNS of the cloud.

For example, your organization’s security policies might not allow the use of public DNS services such as Google Cloud DNS. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services.

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation.

**Prerequisites**

* You installed the `jq` package.

**Procedure**

* Before you deploy your cluster, use a text editor to open the `install-config.yaml` file and add the following stanza:

  + To enable user-managed DNS:

    ```
    platform:
      gcp:
        userProvisionedDNS: Enabled
    ```

    where:

    `Enabled`
    :   Enables user-provisioned DNS management.

For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records".

#### [5.5.8. Sample customized install-config.yaml file for Google Cloud](#installation-gcp-config-yaml_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

To specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters, you can customize the `install-config.yaml` file.

Important

This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.

```
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
controlPlane:
  name: master
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
compute:
- name: worker
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  gcp:
    projectID: sample-project
    region: us-east1
```

where:

`controlPlane`
:   Specifies parameters that apply to control plane machines.

`compute`
:   Specifies parameters that apply to compute machines.

`networking`
:   Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.

`platform`
:   Specifies parameters that apply to the infrastructure platform that hosts the cluster.

#### [5.5.9. Create an Ingress Controller with global access on Google Cloud](#nw-gcp-global-access-configuration_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

You can create an Ingress Controller that has global access to a Google Cloud cluster. Global access is only available to Ingress Controllers using internal load balancers.

**Prerequisites**

* You created the `install-config.yaml` and complete any modifications to it.

**Procedure**

Create an Ingress Controller with global access on a new Google Cloud cluster.

1. Change to the directory that contains the installation program and create a manifest file:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```

   1

   [1](#CO5-1)
   :   For `<installation_directory>`, specify the name of the directory that contains the `install-config.yaml` file for your cluster.
2. Create a file that is named `cluster-ingress-default-ingresscontroller.yaml` in the `<installation_directory>/manifests/` directory:

   ```
   $ touch <installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml
   ```

   1

   [1](#CO6-1)
   :   For `<installation_directory>`, specify the directory name that contains the `manifests/` directory for your cluster.

   After creating the file, several network configuration files are in the `manifests/` directory, as shown:

   ```
   $ ls <installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml
   ```

   **Example output**

   ```
   cluster-ingress-default-ingresscontroller.yaml
   ```
3. Open the `cluster-ingress-default-ingresscontroller.yaml` file in an editor and enter a custom resource (CR) that describes the Operator configuration you want:

   **Sample `clientAccess` configuration to `Global`**

   ```
     apiVersion: operator.openshift.io/v1
     kind: IngressController
     metadata:
       name: default
       namespace: openshift-ingress-operator
     spec:
       endpointPublishingStrategy:
         loadBalancer:
           providerParameters:
             gcp:
               clientAccess: Global
   ```

   1

   ```
             type: GCP
           scope: Internal
   ```

   2

   ```
         type: LoadBalancerService
   ```

   [1](#CO7-1)
   :   Set `gcp.clientAccess` to `Global`.

   [2](#CO7-2)
   :   Global access is only available to Ingress Controllers using internal load balancers.

#### [5.5.10. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

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

### [5.6. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

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

### [5.7. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

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

### [5.8. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

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

### [5.9. Alternatives to storing administrator-level secrets in the kube-system project](#installing-gcp-manual-modes_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives:

* To manage long-term cloud credentials manually, follow the procedure in [Manually creating long-term credentials](#manually-create-iam_installing-restricted-networks-gcp-installer-provisioned "5.9.1. Manually creating long-term credentials").
* To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in [Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-restricted-networks-gcp-installer-provisioned "5.9.2. Configuring a Google Cloud cluster to use short-term credentials").

#### [5.9.1. Manually creating long-term credentials](#manually-create-iam_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

The Cloud Credential Operator (CCO) can be put into manual mode prior to installation in environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace.

**Procedure**

1. Add the following granular permissions to the Google Cloud account that the installation program uses:

   * compute.machineTypes.list
   * compute.regions.list
   * compute.zones.list
   * dns.changes.create
   * dns.changes.get
   * dns.managedZones.create
   * dns.managedZones.delete
   * dns.managedZones.get
   * dns.managedZones.list
   * dns.networks.bindPrivateDNSZone
   * dns.resourceRecordSets.create
   * dns.resourceRecordSets.delete
   * dns.resourceRecordSets.list
2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

   **Sample configuration file snippet**

   ```
   apiVersion: v1
   baseDomain: example.com
   credentialsMode: Manual
   # ...
   ```
3. If you have not previously created installation manifest files, do so by running the following command:

   ```
   $ openshift-install create manifests --dir <installation_directory>
   ```

   where `<installation_directory>` is the directory in which the installation program creates files.
4. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
5. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Specifies only the manifests that your specific cluster configuration requires.

   `<path_to_directory_with_installation_configuration>`
   :   Specifies the location of the `install-config.yaml` file.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       This command creates a YAML file for each `CredentialsRequest` object.

       **Sample `CredentialsRequest` object**

       ```
       apiVersion: cloudcredential.openshift.io/v1
       kind: CredentialsRequest
       metadata:
         name: <component_credentials_request>
         namespace: openshift-cloud-credential-operator
         ...
       spec:
         providerSpec:
           apiVersion: cloudcredential.openshift.io/v1
           kind: GCPProviderSpec
           predefinedRoles:
           - roles/storage.admin
           - roles/iam.serviceAccountUser
           skipServiceCheck: true
         ...
       ```
6. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

   **Sample `CredentialsRequest` object with secrets**

   ```
   apiVersion: cloudcredential.openshift.io/v1
   kind: CredentialsRequest
   metadata:
     name: <component_credentials_request>
     namespace: openshift-cloud-credential-operator
     ...
   spec:
     providerSpec:
       apiVersion: cloudcredential.openshift.io/v1
         ...
     secretRef:
       name: <component_secret>
       namespace: <component_namespace>
     ...
   ```

   **Sample `Secret` object**

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: <component_secret>
     namespace: <component_namespace>
   data:
     service_account.json: <base64_encoded_gcp_service_account_file>
   ```

   Important

   Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.

#### [5.9.2. Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

To install a cluster that is configured to use Google Cloud Workload Identity, you must configure the CCO utility and create the required Google Cloud resources for your cluster.

##### [5.9.2.1. Configuring the Cloud Credential Operator utility](#cco-ccoctl-configuring_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment.

**Prerequisites**

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the OpenShift CLI (`oc`).

* You have added one of the following authentication options to the Google Cloud account that the `ccoctl` utility uses:

  + The **IAM Workload Identity Pool Admin** role
  + The following granular permissions:

    - `compute.projects.get`
    - `iam.googleapis.com/workloadIdentityPoolProviders.create`
    - `iam.googleapis.com/workloadIdentityPoolProviders.get`
    - `iam.googleapis.com/workloadIdentityPools.create`
    - `iam.googleapis.com/workloadIdentityPools.delete`
    - `iam.googleapis.com/workloadIdentityPools.get`
    - `iam.googleapis.com/workloadIdentityPools.undelete`
    - `iam.roles.create`
    - `iam.roles.delete`
    - `iam.roles.list`
    - `iam.roles.undelete`
    - `iam.roles.update`
    - `iam.serviceAccounts.create`
    - `iam.serviceAccounts.delete`
    - `iam.serviceAccounts.getIamPolicy`
    - `iam.serviceAccounts.list`
    - `iam.serviceAccounts.setIamPolicy`
    - `iam.workloadIdentityPoolProviders.get`
    - `iam.workloadIdentityPools.delete`
    - `resourcemanager.projects.get`
    - `resourcemanager.projects.getIamPolicy`
    - `resourcemanager.projects.setIamPolicy`
    - `storage.buckets.create`
    - `storage.buckets.delete`
    - `storage.buckets.get`
    - `storage.buckets.getIamPolicy`
    - `storage.buckets.setIamPolicy`
    - `storage.objects.create`
    - `storage.objects.delete`
    - `storage.objects.list`

**Procedure**

1. Set a variable for the OpenShift Container Platform release image by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:

   ```
   $ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
   ```

   Note

   Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
3. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:

   ```
   $ oc image extract $CCO_IMAGE \
     --file="/usr/bin/ccoctl.<rhel_version>" \
     -a ~/.pull-secret
   ```

   For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid:

   * `rhel8`: Specify this value for hosts that use RHEL 8.
   * `rhel9`: Specify this value for hosts that use RHEL 9.

   Note

   The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
4. Change the permissions to make `ccoctl` executable by running the following command:

   ```
   $ chmod 775 ccoctl
   ```

**Verification**

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:

  ```
  $ ./ccoctl
  ```

  **Example output**

  ```
  OpenShift credentials provisioning tool

  Usage:
    ccoctl [command]

  Available Commands:
    aws          Manage credentials objects for AWS cloud
    azure        Manage credentials objects for Azure
    gcp          Manage credentials objects for Google cloud
    help         Help about any command
    ibmcloud     Manage credentials objects for IBM Cloud
    nutanix      Manage credentials objects for Nutanix

  Flags:
    -h, --help   help for ccoctl

  Use "ccoctl [command] --help" for more information about a command.
  ```

##### [5.9.2.2. Creating Google Cloud resources with the Cloud Credential Operator utility](#cco-ccoctl-creating-at-once_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

You can use the `ccoctl gcp create-all` command to automate the creation of Google Cloud resources.

Note

By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.

**Prerequisites**

You must have:

* Extracted and prepared the `ccoctl` binary.

**Procedure**

1. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Specifies to include only the manifests that your specific cluster configuration requires.

   `<path_to_directory_with_installation_configuration>`
   :   Specifies the location of the `install-config.yaml` file.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       Note

       This command might take a few moments to run.
3. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:

   ```
   $ ccoctl gcp create-all \
     --name=<name> \
     --region=<gcp_region> \
     --project=<gcp_project_id> \
     --credentials-requests-dir=<path_to_credentials_requests_directory> \
     --key-storage-method=<key_storage_method>
   ```

   where:

   `<name>`
   :   Specifies the user-defined name for all created Google Cloud resources used for tracking. If you plan to install the Google Cloud Filestore Container Storage Interface (CSI) Driver Operator, retain this value.

   `<gcp_region>`
   :   Specifies the Google Cloud region in which cloud resources will be created.

   `<gcp_project_id>`
   :   Specifies the Google Cloud project ID in which cloud resources will be created.

   `<path_to_credentials_requests_directory>`
   :   Specifies the directory containing the files of `CredentialsRequest` manifests to create Google Cloud service accounts.

   `<key_storage_method>`
   :   Specifies the method for storing OIDC JWK files. Accepted values are `public-bucket` and `pool-jwk-file`. The default value `public-bucket` creates a public GCS bucket to host the OIDC configuration and JWK files. The `pool-jwk-file` value attaches the JWK directly to the workload identity pool provider without creating a public bucket. This parameter is optional.

       Note

       If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.

**Verification**

* To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory:

  ```
  $ ls <path_to_ccoctl_output_dir>/manifests
  ```

  **Example output**

  ```
  cluster-authentication-02-config.yaml
  openshift-cloud-controller-manager-gcp-ccm-cloud-credentials-credentials.yaml
  openshift-cloud-credential-operator-cloud-credential-operator-gcp-ro-creds-credentials.yaml
  openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
  openshift-cluster-api-capg-manager-bootstrap-credentials-credentials.yaml
  openshift-cluster-csi-drivers-gcp-pd-cloud-credentials-credentials.yaml
  openshift-image-registry-installer-cloud-credentials-credentials.yaml
  openshift-ingress-operator-cloud-credentials-credentials.yaml
  openshift-machine-api-gcp-cloud-credentials-credentials.yaml
  ```

  You can verify that the IAM service accounts are created by querying Google Cloud. For more information, refer to Google Cloud documentation on listing IAM service accounts.

##### [5.9.2.3. Restricting service account impersonation to the compute nodes service account](#restricting-sa-impersonation-compute-sa-gcp_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

After the Cloud Credential Operator utility (`ccoctl`) creates the resources for the cluster, you can restrict the Google Cloud `iam.serviceAccounts.actAs` permission that the `ccoctl` utility granted to the Machine API controller service account to the compute nodes service account.

Note

Restricting service account impersonation to the compute nodes service account is optional. If your organization does not require this change, you can continue to "Incorporating the Cloud Credential Operator utility manifests".

When the `ccoctl` utility assigns custom and Google Cloud predefined roles to OpenShift Container Platform components service accounts, it grants the `iam.serviceAccounts.actAs` permission to the Machine API controller service account at the Google Cloud project level. To reduce the scope of the `iam.serviceAccounts.actAs` permission, you identify the custom role of the Machine API controller service account and replace it with a role that has a more restricted set of permissions. To allow this component to work, you then grant the Machine API controller service account the Service Account User role on the service account of the compute nodes instead.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have used the `ccoctl` utility to create the cloud provider resources for your cluster.
* You have access to your `install-config.yaml` file.
* You have logged in to the Google Cloud CLI (`gcloud`) as a user with permissions to manage service accounts and roles.

**Procedure**

1. Obtain the following values from your `install-config.yaml` file:

   * The Google Cloud project name. In the YAML file, this is the value of the `platform.gcp.projectID` parameter.
   * The cluster name. In the YAML file, this is the value of the `metadata.name` parameter.
   * The service account for the compute nodes. In the YAML file, this is the value of the `compute[0].platform.gcp.serviceAccount` parameter.
2. Obtain the service account for the Machine API controller that the `ccoctl` utility created by running the following command:

   ```
   $ gcloud iam service-accounts list \
     --filter="displayName=<cluster_name>-openshift-machine-api-gcp" \
     --format='value(email)'
   ```

   where `<cluster_name>` is the value specified for the `metadata.name` parameter in your `install-config.yaml` file.
3. Obtain the role ID of the custom role for the Machine API controller service account by running the following command:

   ```
   $ gcloud projects get-iam-policy <project_name> \
     --flatten='bindings[].members' \
     --format='table(bindings.role)' \
     --filter="bindings.members:<machine_api_controller_service_account>"
   ```

   where `<machine_api_controller_service_account>` is the Machine API controller service account.
4. List the custom role permissions for the Machine API controller service account by running the following command:

   ```
   $ gcloud iam roles describe <machine_api_role> \
     --project <project_name>
   ```

   where `<machine_api_role>` is the role ID of the custom role for the Machine API controller service account.

   **Example output**

   ```
   etag: <etag_value>
   includedPermissions:
   - compute.acceleratorTypes.get
   - compute.acceleratorTypes.list
   - compute.disks.create
   - compute.disks.createTagBinding
   ...
   - compute.zones.get
   - compute.zones.list
   - iam.serviceAccounts.actAs
   - iam.serviceAccounts.get
   - iam.serviceAccounts.list
   - resourcemanager.tagValues.get
   - resourcemanager.tagValues.list
   - serviceusage.quotas.get
   - serviceusage.services.get
   - serviceusage.services.list
   name: projects/<project_name>/roles/<machine_api_role>
   stage: GA
   title: <project_name>-openshift-machine-api-gcp
   ```

   where `<project_name>` is the Google Cloud project name specified in the `install-config.yaml` file.

   Note

   This truncated example output might not match the permissions list for your cluster.
5. Create a custom role that includes all of the permissions from your output except for the `iam.serviceAccounts.actAs` permission by running a command similar to the following:

   ```
   $ gcloud iam roles create <machine_api_role>_without_actas \
   --project=<project_name> \
   --title=<machine_api_role>_without_actas \
   --description="Required permissions for the Machine API controller without the iam.serviceAccounts.actAs permission" \
   --permissions=compute.acceleratorTypes.get,\
   compute.acceleratorTypes.list,\
   compute.disks.create,\
   compute.disks.createTagBinding,\
   ...
   compute.zones.get,\
   compute.zones.list,\
   iam.serviceAccounts.get,\
   iam.serviceAccounts.list,\
   resourcemanager.tagValues.get,\
   resourcemanager.tagValues.list,\
   serviceusage.quotas.get,\
   serviceusage.services.get,\
   serviceusage.services.list
   ```

   In this example, the new role name is the original custom role name, `<machine_api_role>`, with a `_without_actas` string added to the end.

   Important

   This truncated example command might not match the permissions list for your cluster. You must use the list of permissions from the output of the `gcloud iam roles describe <machine_api_role> --project <project_name>` command on your cluster.
6. Remove the custom role that includes the `iam.serviceAccounts.actAs` permission from the Machine API controller service account by running the following command:

   ```
   $ gcloud projects remove-iam-policy-binding <project_name> \
     --member "serviceAccount:<machine_api_controller_service_account>" \
     --role "projects/<project_name>/roles/<machine_api_role>"
   ```

   where `<machine_api_role>` is the original custom role.
7. Grant the custom role that excludes the `iam.serviceAccounts.actAs` permission to the Machine API controller service account by running the following command:

   ```
   $ gcloud projects add-iam-policy-binding <project_name> \
     --member "serviceAccount:<machine_api_controller_service_account>" \
     --role "projects/<project_name>/roles/<machine_api_role>_without_actas
   ```

   where `<machine_api_role>_without_actas` is the new custom role.
8. Optional: To verify that the Machine API controller service account has the correct role, check the attached role ID by running the following command:

   ```
   $ gcloud projects get-iam-policy <project_name> \
     --flatten='bindings[].members' \
     --format='table(bindings.role)' \
     --filter="bindings.members:<machine_api_controller_service_account>"
   ```

   **Example output**

   ```
   ROLE
   projects/<project_name>/roles/<machine_api_role>_without_actas
   ```
9. Grant the Machine API controller service account the Service Account User role on the service account of the compute nodes by running the following command:

   ```
   $ gcloud iam service-accounts add-iam-policy-binding <compute_nodes_service_account> \
     --member="serviceAccount:<machine_api_controller_service_account>" \
     --role=roles/iam.serviceAccountUser
   ```

   where `<compute_nodes_service_account>` is the service account for your compute nodes. This value is the `compute[0].platform.gcp.serviceAccount` parameter in your `install-config.yaml` file.

##### [5.9.2.4. Incorporating the Cloud Credential Operator utility manifests](#cco-ccoctl-install-creating-manifests_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

To implement short-term security credentials managed outside the cluster for individual components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have configured the Cloud Credential Operator utility (`ccoctl`).
* You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility.

**Procedure**

1. Add the following granular permissions to the Google Cloud account that the installation program uses:

   * compute.machineTypes.list
   * compute.regions.list
   * compute.zones.list
   * dns.changes.create
   * dns.changes.get
   * dns.managedZones.create
   * dns.managedZones.delete
   * dns.managedZones.get
   * dns.managedZones.list
   * dns.networks.bindPrivateDNSZone
   * dns.resourceRecordSets.create
   * dns.resourceRecordSets.delete
   * dns.resourceRecordSets.list
2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

   **Sample configuration file snippet**

   ```
   apiVersion: v1
   baseDomain: example.com
   credentialsMode: Manual
   # ...
   ```
3. If you have not previously created installation manifest files, do so by running the following command:

   ```
   $ openshift-install create manifests --dir <installation_directory>
   ```

   where `<installation_directory>` is the directory in which the installation program creates files.
4. Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command:

   ```
   $ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
   ```
5. Copy the `tls` directory that contains the private key to the installation directory:

   ```
   $ cp -a /<path_to_ccoctl_output_dir>/tls .
   ```

### [5.10. Deploying the cluster](#installation-launching-installer_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

Important

You can run the `create cluster` command of the installation program only once, during initial installation.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

**Procedure**

1. Remove any existing Google Cloud credentials that do not use the service account key for the Google Cloud account that you configured for your cluster and that are stored in the following locations:

   * The `GOOGLE_CREDENTIALS`, `GOOGLE_CLOUD_KEYFILE_JSON`, or `GCLOUD_KEYFILE_JSON` environment variables
   * The `~/.gcp/osServiceAccount.json` file
   * The `gcloud cli` default credentials
2. In the directory that contains the installation program, initialize the cluster deployment by running the following command:

   ```
   $ ./openshift-install create cluster --dir <installation_directory> \
       --log-level=info
   ```

   * For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.
   * To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.
3. Optional: You can reduce the number of permissions for the service account that you used to install the cluster.

   * If you assigned the `Owner` role to your service account, you can remove that role and replace it with the `Viewer` role.
   * If you included the `Service Account Key Admin` role, you can remove it.

**Verification**

When the cluster deployment completes successfully:

* The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.
* Credential information also outputs to `<installation_directory>/.openshift_install.log`.

  Important

  Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.

  **Example output**

  ```
  ...
  INFO Install complete!
  INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
  INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
  INFO Login to the console with user: "kubeadmin", and password: "password"
  INFO Time elapsed: 36m22s
  ```

  Important

  + The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
  + It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

### [5.11. Provisioning your own DNS records](#installation-gcp-provisioning-own-dns-records_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

Use the IP address of the API server to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. Use the IP address of the Ingress service to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

Important

Before you use this feature, you must add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS".

**Prerequisites**

* You installed your cluster.
* You installed the `gcloud` CLI tool.

**Procedure**

1. Determine the infrastructure ID of your cluster by running the following command:

   ```
   $ infra_id=$(jq -r .infraID <installation_directory>/metadata.json)
   ```

   where:

   `<installation_directory>`
   :   Specifies the directory where you ran the installation program.
2. Find the IP address of the API server:

   1. If you installed a private cluster, determine the IP address of the API server by running the following command:

      ```
      $ gcloud compute forwarding-rules describe "${infra_id}-api-internal" --project=<project_name> --region <region_name> --format json | jq -r .IPAddress
      ```

      where:

      `<project_name>`
      :   Specifies the name of your Google Cloud project.

      `<region_name>`
      :   Specifies the region where you installed your cluster.
   2. If you installed a public cluster, determine the IP address of the API server by running the following command:

      ```
      $ gcloud compute forwarding-rules describe --global "${infra_id}-apiserver" --format json | jq -r .IPAddress
      ```
3. Use the IP address to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.
4. Find the IP address of the Ingress service:

   1. If you installed a private cluster, find the IP address of the Ingress service by running the following command:

      ```
      $ gcloud compute forwarding-rules list --project=<project_name> --filter="subnetwork:(projects/<project_name>/regions/<region_name>/subnetworks/<compute_subnet_name>)" --format="json" | jq -r '.[].IPAddress'
      ```

      where:

      `<project_name>`
      :   Specifies the name of your Google Cloud project.

      `<region_name>`
      :   Specifies the region where you installed your cluster.

      `<compute_subnet_name>`
      :   Specifies the name of the subnet that contains your compute nodes.
   2. If you installed a public cluster, find the IP address by using the forwarding rule:

      1. Find the forwarding rule for the Ingress service by running the following command:

         ```
         $ ingress_forwarding_rule=$(gcloud compute target-pools list --format=json --filter="instances[]~${infra_id}" | jq -r .[].name)
         ```
      2. Use the forwarding rule value to find the IP address of the Ingress service by running the following command:

         ```
         $ gcloud compute forwarding-rules describe --region "<region_name>" "${ingress_forwarding_rule}" --format json | jq -r .IPAddress
         ```

         where:

         `<region_name>`
         :   Specifies the region where you installed your cluster.
5. Use the IP address to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

### [5.12. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

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

### [5.13. Disabling the default software catalog sources](#olm-restricted-networks-operatorhub_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

To use only trusted or locally available Operator catalogs, disable the default software catalog sources that OpenShift Container Platform configures during installation. In a restricted network environment, you must disable the default catalogs as a cluster administrator.

**Procedure**

* Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object:

  ```
  $ oc patch OperatorHub cluster --type json \
      -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
  ```

  Tip

  Or, you can use the web console to manage catalog sources. From the **Administration** → **Cluster Settings** → **Configuration** → **OperatorHub** page, click the **Sources** tab, where you can create, update, delete, disable, and enable individual sources.

### [5.14. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

### [5.15. Next steps](#next-steps_installing-restricted-networks-gcp-installer-provisioned) Copy linkLink copied to clipboard!

* [Validate an installation](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/validation_and_troubleshooting/#validating-an-installation).
* [Customize your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations).
* [Configure image streams](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#post-install-must-gather-disconnected) for the Cluster Samples Operator and the `must-gather` tool.
* Learn how to [use Operator Lifecycle Manager in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#olm-restricted-networks).
* If the mirror registry that you used to install your cluster has a trusted CA, add it to the cluster by [configuring additional trust stores](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#images-configuration-cas_image-configuration).
* If necessary, you can [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting).
* If necessary, see [Registering your disconnected cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#insights-operator-register-disconnected-cluster_remote-health-reporting)

## [Chapter 6. Installing a cluster on Google Cloud into an existing VPC](#installing-gcp-vpc) Copy linkLink copied to clipboard!

In OpenShift Container Platform version 4.22, you can install a cluster into an existing Virtual Private Cloud (VPC) on Google Cloud. The installation program provisions the rest of the required infrastructure, which you can further customize. To customize the installation, you modify parameters in the `install-config.yaml` file before you install the cluster.

### [6.1. Prerequisites](#prerequisites-3) Copy linkLink copied to clipboard!

* You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes.
* You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing).
* You [configured a Google Cloud project](#installing-gcp-account "Chapter 2. Configuring a Google Cloud project") to host the cluster.
* If you use a firewall, you [configured it to allow the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires access to.
* If you manage your Google Cloud firewall rules, you [configured the required firewall rules](#installation-gcp-user-managed-firewall-rules_installing-gcp-account "2.6. Managing your own firewall rules").

### [6.2. About using a custom VPC](#installation-custom-gcp-vpc_installing-gcp-vpc) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you can deploy a cluster into existing subnets in an existing Virtual Private Cloud (VPC) in Google Cloud. By deploying OpenShift Container Platform into an existing Google Cloud VPC, you might be able to avoid limit constraints in new accounts or more easily abide by the operational constraints that your company’s guidelines set. If you cannot obtain the infrastructure creation permissions that are required to create the VPC yourself, use this installation option. You must configure networking for the subnets.

#### [6.2.1. Requirements for using your VPC](#installation-custom-gcp-vpc-requirements_installing-gcp-vpc) Copy linkLink copied to clipboard!

The union of the VPC CIDR block and the machine network CIDR must be non-empty. The subnets must be within the machine network.

The installation program does not create the following components:

* NAT gateways
* Subnets
* Route tables
* VPC network

Note

The installation program requires that you use the cloud-provided DNS server. Using a custom DNS server is not supported and causes the installation to fail.

#### [6.2.2. VPC validation](#installation-custom-gcp-vpc-validation_installing-gcp-vpc) Copy linkLink copied to clipboard!

To ensure that the subnets that you provide are suitable, the installation program confirms the following data:

* All the subnets that you specify exist.
* You provide one subnet for control-plane machines and one subnet for compute machines.
* The subnet’s CIDRs belong to the machine CIDR that you specified.

#### [6.2.3. Division of permissions](#installation-about-custom-gcp-permissions_installing-gcp-vpc) Copy linkLink copied to clipboard!

Some individuals can create different resource in your clouds than others. For example, you might be able to create application-specific items, like instances, buckets, and load balancers, but not networking-related components such as VPCs, subnets, or ingress rules.

#### [6.2.4. Isolation between clusters](#installation-custom-gcp-vpc-isolation_installing-gcp-vpc) Copy linkLink copied to clipboard!

If you deploy OpenShift Container Platform to an existing network, the isolation of cluster services is reduced in the following ways:

* You can install multiple OpenShift Container Platform clusters in the same VPC.
* ICMP ingress is allowed to the entire network.
* TCP 22 ingress (SSH) is allowed to the entire network.
* Control plane TCP 6443 ingress (Kubernetes API) is allowed to the entire network.
* Control plane TCP 22623 ingress (MCS) is allowed to the entire network.

### [6.3. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-gcp-vpc) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [6.4. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-gcp-vpc) Copy linkLink copied to clipboard!

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

### [6.5. Obtaining the installation program](#installation-obtaining-installer_installing-gcp-vpc) Copy linkLink copied to clipboard!

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

### [6.6. Creating the installation configuration file](#installation-initializing_installing-gcp-vpc) Copy linkLink copied to clipboard!

You can customize the OpenShift Container Platform cluster you install on Google Cloud.

**Prerequisites**

* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* Configure a Google Cloud account.

**Procedure**

1. Create the `install-config.yaml` file.

   1. Change to the directory that contains the installation program and run the following command:

      ```
      $ ./openshift-install create install-config --dir <installation_directory>
      ```

      * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

        When specifying the directory:
      * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
      * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
   2. At the prompts, provide the configuration details for your cloud:

      1. Optional: Select an SSH key to use to access your cluster machines.

         Note

         For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
      2. Select **gcp** as the platform to target.
      3. If you have not configured the service account key for your Google Cloud account on your computer, you must obtain it from Google Cloud and paste the contents of the file or enter the absolute path to the file.
      4. Select the project ID to provision the cluster in. The default value is specified by the service account that you configured.
      5. Select the region to deploy the cluster to.
      6. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.
      7. Enter a descriptive name for your cluster.
2. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.

   1. Define the network and subnets for the VPC to install the cluster in under the parent `platform.gcp` field:

      ```
      platform:
        gcp:
          network: <existing_vpc>
          controlPlaneSubnet: <control_plane_subnet>
          computeSubnet: <compute_subnet>
      ```

      For the `platform.gcp.network` parameter, specify the name for the existing Google VPC. For the `platform.gcp.controlPlaneSubnet` and `platform.gcp.computeSubnet` parameters, specify the existing subnets to deploy the control plane machines and compute machines, respectively.
3. Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

   Important

   The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

#### [6.6.1. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-gcp-vpc) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 6.1. Minimum resource requirements

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Show more

* One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
* OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance.
* As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines.

Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* ppc64le architecture requires IBM® Power9 ISA
* s390x architecture requires IBM® z14 ISA

For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

#### [6.6.2. Tested instance types for Google Cloud](#installation-gcp-tested-machine-types_installing-gcp-vpc) Copy linkLink copied to clipboard!

The following Google Cloud instance types have been tested with OpenShift Container Platform.

Note

Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) (Google documentation).

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see [machine series support for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in *Storage*.

See the following machine series:

* `A2`
* `A3`
* `C2`
* `C2D`
* `C3`
* `C3D`
* `C4`
* `E2`
* `M1`
* `N1`
* `N2`
* `N2D`
* `N4`
* `Tau T2D`

#### [6.6.3. Tested instance types for Google Cloud on 64-bit ARM infrastructures](#installation-gcp-tested-machine-types-arm_installing-gcp-vpc) Copy linkLink copied to clipboard!

The following Google Cloud 64-bit ARM instance types have been tested with OpenShift Container Platform.

See the following machine series for 64-bit ARM machines:

* `C4A`
* `N4A`
* `Tau T2A`

#### [6.6.4. Using custom machine types](#installation-custom-machine-types_installing-gcp-vpc) Copy linkLink copied to clipboard!

Using a custom machine type to install a OpenShift Container Platform cluster is supported.

Consider the following when using a custom machine type:

* Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation".
* The name of the custom machine type must adhere to the following syntax:

  `custom-<number_of_cpus>-<amount_of_memory_in_mb>`

  For example, `custom-6-20480`.

As part of the installation process, you specify the custom machine type in the `install-config.yaml` file.

**Sample `install-config.yaml` file with a custom machine type**

```
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  platform:
    gcp:
      type: custom-6-20480
  replicas: 2
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    gcp:
      type: custom-6-20480
  replicas: 3
```

#### [6.6.5. Enabling Shielded VMs](#installation-gcp-enabling-shielded-vms_installing-gcp-vpc) Copy linkLink copied to clipboard!

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).

Note

Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use shielded VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            secureBoot: Enabled
     ```
  2. To use shielded VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            secureBoot: Enabled
     ```
  3. To use shielded VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            secureBoot: Enabled
     ```

#### [6.6.6. Enabling Confidential VMs](#installation-gcp-enabling-confidential-vms_installing-gcp-vpc) Copy linkLink copied to clipboard!

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google’s documentation on [Confidential Computing](https://cloud.google.com/confidential-computing). You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

Note

Confidential VMs are currently not supported on 64-bit ARM architectures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use confidential VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
     ```

     1

     ```
            type: n2d-standard-8
     ```

     2

     ```
            onHostMaintenance: Terminate
     ```

     3

     [1](#CO8-1)
     :   Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional Google Cloud configuration parameters".

     [2](#CO8-2)
     :   Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see [Supported operating systems and machine types](https://cloud.google.com/compute/confidential-vm/docs/os-and-machine-type#machine-type).

     [3](#CO8-3)
     :   Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.
  2. To use confidential VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```
  3. To use confidential VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```

#### [6.6.7. Enabling a user-managed DNS](#installation-gcp-enabling-user-managed-DNS_installing-gcp-vpc) Copy linkLink copied to clipboard!

You can install a cluster with a domain name server (DNS) solution that you manage instead of the default cluster-provisioned DNS solution. As a result, you can manage the API and Ingress DNS records in your own system rather than adding the records to the DNS of the cloud.

For example, your organization’s security policies might not allow the use of public DNS services such as Google Cloud DNS. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services.

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation.

**Prerequisites**

* You installed the `jq` package.

**Procedure**

* Before you deploy your cluster, use a text editor to open the `install-config.yaml` file and add the following stanza:

  + To enable user-managed DNS:

    ```
    platform:
      gcp:
        userProvisionedDNS: Enabled
    ```

    where:

    `Enabled`
    :   Enables user-provisioned DNS management.

For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records".

#### [6.6.8. Sample customized install-config.yaml file for Google Cloud](#installation-gcp-config-yaml_installing-gcp-vpc) Copy linkLink copied to clipboard!

To specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters, you can customize the `install-config.yaml` file.

Important

This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.

```
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
controlPlane:
  name: master
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
compute:
- name: worker
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  gcp:
    projectID: sample-project
    region: us-east1
```

where:

`controlPlane`
:   Specifies parameters that apply to control plane machines.

`compute`
:   Specifies parameters that apply to compute machines.

`networking`
:   Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.

`platform`
:   Specifies parameters that apply to the infrastructure platform that hosts the cluster.

#### [6.6.9. Create an Ingress Controller with global access on Google Cloud](#nw-gcp-global-access-configuration_installing-gcp-vpc) Copy linkLink copied to clipboard!

You can create an Ingress Controller that has global access to a Google Cloud cluster. Global access is only available to Ingress Controllers using internal load balancers.

**Prerequisites**

* You created the `install-config.yaml` and complete any modifications to it.

**Procedure**

Create an Ingress Controller with global access on a new Google Cloud cluster.

1. Change to the directory that contains the installation program and create a manifest file:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```

   1

   [1](#CO9-1)
   :   For `<installation_directory>`, specify the name of the directory that contains the `install-config.yaml` file for your cluster.
2. Create a file that is named `cluster-ingress-default-ingresscontroller.yaml` in the `<installation_directory>/manifests/` directory:

   ```
   $ touch <installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml
   ```

   1

   [1](#CO10-1)
   :   For `<installation_directory>`, specify the directory name that contains the `manifests/` directory for your cluster.

   After creating the file, several network configuration files are in the `manifests/` directory, as shown:

   ```
   $ ls <installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml
   ```

   **Example output**

   ```
   cluster-ingress-default-ingresscontroller.yaml
   ```
3. Open the `cluster-ingress-default-ingresscontroller.yaml` file in an editor and enter a custom resource (CR) that describes the Operator configuration you want:

   **Sample `clientAccess` configuration to `Global`**

   ```
     apiVersion: operator.openshift.io/v1
     kind: IngressController
     metadata:
       name: default
       namespace: openshift-ingress-operator
     spec:
       endpointPublishingStrategy:
         loadBalancer:
           providerParameters:
             gcp:
               clientAccess: Global
   ```

   1

   ```
             type: GCP
           scope: Internal
   ```

   2

   ```
         type: LoadBalancerService
   ```

   [1](#CO11-1)
   :   Set `gcp.clientAccess` to `Global`.

   [2](#CO11-2)
   :   Global access is only available to Ingress Controllers using internal load balancers.

#### [6.6.10. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-gcp-vpc) Copy linkLink copied to clipboard!

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

### [6.7. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-gcp-vpc) Copy linkLink copied to clipboard!

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

### [6.8. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-gcp-vpc) Copy linkLink copied to clipboard!

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

### [6.9. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-gcp-vpc) Copy linkLink copied to clipboard!

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

### [6.10. Alternatives to storing administrator-level secrets in the kube-system project](#installing-gcp-manual-modes_installing-gcp-vpc) Copy linkLink copied to clipboard!

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives:

* To manage long-term cloud credentials manually, follow the procedure in [Manually creating long-term credentials](#manually-create-iam_installing-gcp-vpc "6.10.1. Manually creating long-term credentials").
* To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in [Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-gcp-vpc "6.10.2. Configuring a Google Cloud cluster to use short-term credentials").

#### [6.10.1. Manually creating long-term credentials](#manually-create-iam_installing-gcp-vpc) Copy linkLink copied to clipboard!

The Cloud Credential Operator (CCO) can be put into manual mode prior to installation in environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace.

**Procedure**

1. Add the following granular permissions to the Google Cloud account that the installation program uses:

   * compute.machineTypes.list
   * compute.regions.list
   * compute.zones.list
   * dns.changes.create
   * dns.changes.get
   * dns.managedZones.create
   * dns.managedZones.delete
   * dns.managedZones.get
   * dns.managedZones.list
   * dns.networks.bindPrivateDNSZone
   * dns.resourceRecordSets.create
   * dns.resourceRecordSets.delete
   * dns.resourceRecordSets.list
2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

   **Sample configuration file snippet**

   ```
   apiVersion: v1
   baseDomain: example.com
   credentialsMode: Manual
   # ...
   ```
3. If you have not previously created installation manifest files, do so by running the following command:

   ```
   $ openshift-install create manifests --dir <installation_directory>
   ```

   where `<installation_directory>` is the directory in which the installation program creates files.
4. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
5. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Specifies only the manifests that your specific cluster configuration requires.

   `<path_to_directory_with_installation_configuration>`
   :   Specifies the location of the `install-config.yaml` file.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       This command creates a YAML file for each `CredentialsRequest` object.

       **Sample `CredentialsRequest` object**

       ```
       apiVersion: cloudcredential.openshift.io/v1
       kind: CredentialsRequest
       metadata:
         name: <component_credentials_request>
         namespace: openshift-cloud-credential-operator
         ...
       spec:
         providerSpec:
           apiVersion: cloudcredential.openshift.io/v1
           kind: GCPProviderSpec
           predefinedRoles:
           - roles/storage.admin
           - roles/iam.serviceAccountUser
           skipServiceCheck: true
         ...
       ```
6. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

   **Sample `CredentialsRequest` object with secrets**

   ```
   apiVersion: cloudcredential.openshift.io/v1
   kind: CredentialsRequest
   metadata:
     name: <component_credentials_request>
     namespace: openshift-cloud-credential-operator
     ...
   spec:
     providerSpec:
       apiVersion: cloudcredential.openshift.io/v1
         ...
     secretRef:
       name: <component_secret>
       namespace: <component_namespace>
     ...
   ```

   **Sample `Secret` object**

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: <component_secret>
     namespace: <component_namespace>
   data:
     service_account.json: <base64_encoded_gcp_service_account_file>
   ```

   Important

   Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.

#### [6.10.2. Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-gcp-vpc) Copy linkLink copied to clipboard!

To install a cluster that is configured to use Google Cloud Workload Identity, you must configure the CCO utility and create the required Google Cloud resources for your cluster.

##### [6.10.2.1. Configuring the Cloud Credential Operator utility](#cco-ccoctl-configuring_installing-gcp-vpc) Copy linkLink copied to clipboard!

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment.

**Prerequisites**

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the OpenShift CLI (`oc`).

* You have added one of the following authentication options to the Google Cloud account that the `ccoctl` utility uses:

  + The **IAM Workload Identity Pool Admin** role
  + The following granular permissions:

    - `compute.projects.get`
    - `iam.googleapis.com/workloadIdentityPoolProviders.create`
    - `iam.googleapis.com/workloadIdentityPoolProviders.get`
    - `iam.googleapis.com/workloadIdentityPools.create`
    - `iam.googleapis.com/workloadIdentityPools.delete`
    - `iam.googleapis.com/workloadIdentityPools.get`
    - `iam.googleapis.com/workloadIdentityPools.undelete`
    - `iam.roles.create`
    - `iam.roles.delete`
    - `iam.roles.list`
    - `iam.roles.undelete`
    - `iam.roles.update`
    - `iam.serviceAccounts.create`
    - `iam.serviceAccounts.delete`
    - `iam.serviceAccounts.getIamPolicy`
    - `iam.serviceAccounts.list`
    - `iam.serviceAccounts.setIamPolicy`
    - `iam.workloadIdentityPoolProviders.get`
    - `iam.workloadIdentityPools.delete`
    - `resourcemanager.projects.get`
    - `resourcemanager.projects.getIamPolicy`
    - `resourcemanager.projects.setIamPolicy`
    - `storage.buckets.create`
    - `storage.buckets.delete`
    - `storage.buckets.get`
    - `storage.buckets.getIamPolicy`
    - `storage.buckets.setIamPolicy`
    - `storage.objects.create`
    - `storage.objects.delete`
    - `storage.objects.list`

**Procedure**

1. Set a variable for the OpenShift Container Platform release image by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:

   ```
   $ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
   ```

   Note

   Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
3. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:

   ```
   $ oc image extract $CCO_IMAGE \
     --file="/usr/bin/ccoctl.<rhel_version>" \
     -a ~/.pull-secret
   ```

   For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid:

   * `rhel8`: Specify this value for hosts that use RHEL 8.
   * `rhel9`: Specify this value for hosts that use RHEL 9.

   Note

   The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
4. Change the permissions to make `ccoctl` executable by running the following command:

   ```
   $ chmod 775 ccoctl
   ```

**Verification**

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:

  ```
  $ ./ccoctl
  ```

  **Example output**

  ```
  OpenShift credentials provisioning tool

  Usage:
    ccoctl [command]

  Available Commands:
    aws          Manage credentials objects for AWS cloud
    azure        Manage credentials objects for Azure
    gcp          Manage credentials objects for Google cloud
    help         Help about any command
    ibmcloud     Manage credentials objects for IBM Cloud
    nutanix      Manage credentials objects for Nutanix

  Flags:
    -h, --help   help for ccoctl

  Use "ccoctl [command] --help" for more information about a command.
  ```

##### [6.10.2.2. Creating Google Cloud resources with the Cloud Credential Operator utility](#cco-ccoctl-creating-at-once_installing-gcp-vpc) Copy linkLink copied to clipboard!

You can use the `ccoctl gcp create-all` command to automate the creation of Google Cloud resources.

Note

By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.

**Prerequisites**

You must have:

* Extracted and prepared the `ccoctl` binary.

**Procedure**

1. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Specifies to include only the manifests that your specific cluster configuration requires.

   `<path_to_directory_with_installation_configuration>`
   :   Specifies the location of the `install-config.yaml` file.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       Note

       This command might take a few moments to run.
3. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:

   ```
   $ ccoctl gcp create-all \
     --name=<name> \
     --region=<gcp_region> \
     --project=<gcp_project_id> \
     --credentials-requests-dir=<path_to_credentials_requests_directory> \
     --key-storage-method=<key_storage_method>
   ```

   where:

   `<name>`
   :   Specifies the user-defined name for all created Google Cloud resources used for tracking. If you plan to install the Google Cloud Filestore Container Storage Interface (CSI) Driver Operator, retain this value.

   `<gcp_region>`
   :   Specifies the Google Cloud region in which cloud resources will be created.

   `<gcp_project_id>`
   :   Specifies the Google Cloud project ID in which cloud resources will be created.

   `<path_to_credentials_requests_directory>`
   :   Specifies the directory containing the files of `CredentialsRequest` manifests to create Google Cloud service accounts.

   `<key_storage_method>`
   :   Specifies the method for storing OIDC JWK files. Accepted values are `public-bucket` and `pool-jwk-file`. The default value `public-bucket` creates a public GCS bucket to host the OIDC configuration and JWK files. The `pool-jwk-file` value attaches the JWK directly to the workload identity pool provider without creating a public bucket. This parameter is optional.

       Note

       If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.

**Verification**

* To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory:

  ```
  $ ls <path_to_ccoctl_output_dir>/manifests
  ```

  **Example output**

  ```
  cluster-authentication-02-config.yaml
  openshift-cloud-controller-manager-gcp-ccm-cloud-credentials-credentials.yaml
  openshift-cloud-credential-operator-cloud-credential-operator-gcp-ro-creds-credentials.yaml
  openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
  openshift-cluster-api-capg-manager-bootstrap-credentials-credentials.yaml
  openshift-cluster-csi-drivers-gcp-pd-cloud-credentials-credentials.yaml
  openshift-image-registry-installer-cloud-credentials-credentials.yaml
  openshift-ingress-operator-cloud-credentials-credentials.yaml
  openshift-machine-api-gcp-cloud-credentials-credentials.yaml
  ```

  You can verify that the IAM service accounts are created by querying Google Cloud. For more information, refer to Google Cloud documentation on listing IAM service accounts.

##### [6.10.2.3. Restricting service account impersonation to the compute nodes service account](#restricting-sa-impersonation-compute-sa-gcp_installing-gcp-vpc) Copy linkLink copied to clipboard!

After the Cloud Credential Operator utility (`ccoctl`) creates the resources for the cluster, you can restrict the Google Cloud `iam.serviceAccounts.actAs` permission that the `ccoctl` utility granted to the Machine API controller service account to the compute nodes service account.

Note

Restricting service account impersonation to the compute nodes service account is optional. If your organization does not require this change, you can continue to "Incorporating the Cloud Credential Operator utility manifests".

When the `ccoctl` utility assigns custom and Google Cloud predefined roles to OpenShift Container Platform components service accounts, it grants the `iam.serviceAccounts.actAs` permission to the Machine API controller service account at the Google Cloud project level. To reduce the scope of the `iam.serviceAccounts.actAs` permission, you identify the custom role of the Machine API controller service account and replace it with a role that has a more restricted set of permissions. To allow this component to work, you then grant the Machine API controller service account the Service Account User role on the service account of the compute nodes instead.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have used the `ccoctl` utility to create the cloud provider resources for your cluster.
* You have access to your `install-config.yaml` file.
* You have logged in to the Google Cloud CLI (`gcloud`) as a user with permissions to manage service accounts and roles.

**Procedure**

1. Obtain the following values from your `install-config.yaml` file:

   * The Google Cloud project name. In the YAML file, this is the value of the `platform.gcp.projectID` parameter.
   * The cluster name. In the YAML file, this is the value of the `metadata.name` parameter.
   * The service account for the compute nodes. In the YAML file, this is the value of the `compute[0].platform.gcp.serviceAccount` parameter.
2. Obtain the service account for the Machine API controller that the `ccoctl` utility created by running the following command:

   ```
   $ gcloud iam service-accounts list \
     --filter="displayName=<cluster_name>-openshift-machine-api-gcp" \
     --format='value(email)'
   ```

   where `<cluster_name>` is the value specified for the `metadata.name` parameter in your `install-config.yaml` file.
3. Obtain the role ID of the custom role for the Machine API controller service account by running the following command:

   ```
   $ gcloud projects get-iam-policy <project_name> \
     --flatten='bindings[].members' \
     --format='table(bindings.role)' \
     --filter="bindings.members:<machine_api_controller_service_account>"
   ```

   where `<machine_api_controller_service_account>` is the Machine API controller service account.
4. List the custom role permissions for the Machine API controller service account by running the following command:

   ```
   $ gcloud iam roles describe <machine_api_role> \
     --project <project_name>
   ```

   where `<machine_api_role>` is the role ID of the custom role for the Machine API controller service account.

   **Example output**

   ```
   etag: <etag_value>
   includedPermissions:
   - compute.acceleratorTypes.get
   - compute.acceleratorTypes.list
   - compute.disks.create
   - compute.disks.createTagBinding
   ...
   - compute.zones.get
   - compute.zones.list
   - iam.serviceAccounts.actAs
   - iam.serviceAccounts.get
   - iam.serviceAccounts.list
   - resourcemanager.tagValues.get
   - resourcemanager.tagValues.list
   - serviceusage.quotas.get
   - serviceusage.services.get
   - serviceusage.services.list
   name: projects/<project_name>/roles/<machine_api_role>
   stage: GA
   title: <project_name>-openshift-machine-api-gcp
   ```

   where `<project_name>` is the Google Cloud project name specified in the `install-config.yaml` file.

   Note

   This truncated example output might not match the permissions list for your cluster.
5. Create a custom role that includes all of the permissions from your output except for the `iam.serviceAccounts.actAs` permission by running a command similar to the following:

   ```
   $ gcloud iam roles create <machine_api_role>_without_actas \
   --project=<project_name> \
   --title=<machine_api_role>_without_actas \
   --description="Required permissions for the Machine API controller without the iam.serviceAccounts.actAs permission" \
   --permissions=compute.acceleratorTypes.get,\
   compute.acceleratorTypes.list,\
   compute.disks.create,\
   compute.disks.createTagBinding,\
   ...
   compute.zones.get,\
   compute.zones.list,\
   iam.serviceAccounts.get,\
   iam.serviceAccounts.list,\
   resourcemanager.tagValues.get,\
   resourcemanager.tagValues.list,\
   serviceusage.quotas.get,\
   serviceusage.services.get,\
   serviceusage.services.list
   ```

   In this example, the new role name is the original custom role name, `<machine_api_role>`, with a `_without_actas` string added to the end.

   Important

   This truncated example command might not match the permissions list for your cluster. You must use the list of permissions from the output of the `gcloud iam roles describe <machine_api_role> --project <project_name>` command on your cluster.
6. Remove the custom role that includes the `iam.serviceAccounts.actAs` permission from the Machine API controller service account by running the following command:

   ```
   $ gcloud projects remove-iam-policy-binding <project_name> \
     --member "serviceAccount:<machine_api_controller_service_account>" \
     --role "projects/<project_name>/roles/<machine_api_role>"
   ```

   where `<machine_api_role>` is the original custom role.
7. Grant the custom role that excludes the `iam.serviceAccounts.actAs` permission to the Machine API controller service account by running the following command:

   ```
   $ gcloud projects add-iam-policy-binding <project_name> \
     --member "serviceAccount:<machine_api_controller_service_account>" \
     --role "projects/<project_name>/roles/<machine_api_role>_without_actas
   ```

   where `<machine_api_role>_without_actas` is the new custom role.
8. Optional: To verify that the Machine API controller service account has the correct role, check the attached role ID by running the following command:

   ```
   $ gcloud projects get-iam-policy <project_name> \
     --flatten='bindings[].members' \
     --format='table(bindings.role)' \
     --filter="bindings.members:<machine_api_controller_service_account>"
   ```

   **Example output**

   ```
   ROLE
   projects/<project_name>/roles/<machine_api_role>_without_actas
   ```
9. Grant the Machine API controller service account the Service Account User role on the service account of the compute nodes by running the following command:

   ```
   $ gcloud iam service-accounts add-iam-policy-binding <compute_nodes_service_account> \
     --member="serviceAccount:<machine_api_controller_service_account>" \
     --role=roles/iam.serviceAccountUser
   ```

   where `<compute_nodes_service_account>` is the service account for your compute nodes. This value is the `compute[0].platform.gcp.serviceAccount` parameter in your `install-config.yaml` file.

##### [6.10.2.4. Incorporating the Cloud Credential Operator utility manifests](#cco-ccoctl-install-creating-manifests_installing-gcp-vpc) Copy linkLink copied to clipboard!

To implement short-term security credentials managed outside the cluster for individual components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have configured the Cloud Credential Operator utility (`ccoctl`).
* You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility.

**Procedure**

1. Add the following granular permissions to the Google Cloud account that the installation program uses:

   * compute.machineTypes.list
   * compute.regions.list
   * compute.zones.list
   * dns.changes.create
   * dns.changes.get
   * dns.managedZones.create
   * dns.managedZones.delete
   * dns.managedZones.get
   * dns.managedZones.list
   * dns.networks.bindPrivateDNSZone
   * dns.resourceRecordSets.create
   * dns.resourceRecordSets.delete
   * dns.resourceRecordSets.list
2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

   **Sample configuration file snippet**

   ```
   apiVersion: v1
   baseDomain: example.com
   credentialsMode: Manual
   # ...
   ```
3. If you have not previously created installation manifest files, do so by running the following command:

   ```
   $ openshift-install create manifests --dir <installation_directory>
   ```

   where `<installation_directory>` is the directory in which the installation program creates files.
4. Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command:

   ```
   $ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
   ```
5. Copy the `tls` directory that contains the private key to the installation directory:

   ```
   $ cp -a /<path_to_ccoctl_output_dir>/tls .
   ```

### [6.11. Deploying the cluster](#installation-launching-installer_installing-gcp-vpc) Copy linkLink copied to clipboard!

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

Important

You can run the `create cluster` command of the installation program only once, during initial installation.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

**Procedure**

1. Remove any existing Google Cloud credentials that do not use the service account key for the Google Cloud account that you configured for your cluster and that are stored in the following locations:

   * The `GOOGLE_CREDENTIALS`, `GOOGLE_CLOUD_KEYFILE_JSON`, or `GCLOUD_KEYFILE_JSON` environment variables
   * The `~/.gcp/osServiceAccount.json` file
   * The `gcloud cli` default credentials
2. In the directory that contains the installation program, initialize the cluster deployment by running the following command:

   ```
   $ ./openshift-install create cluster --dir <installation_directory> \
       --log-level=info
   ```

   * For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.
   * To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.
3. Optional: You can reduce the number of permissions for the service account that you used to install the cluster.

   * If you assigned the `Owner` role to your service account, you can remove that role and replace it with the `Viewer` role.
   * If you included the `Service Account Key Admin` role, you can remove it.

**Verification**

When the cluster deployment completes successfully:

* The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.
* Credential information also outputs to `<installation_directory>/.openshift_install.log`.

  Important

  Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.

  **Example output**

  ```
  ...
  INFO Install complete!
  INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
  INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
  INFO Login to the console with user: "kubeadmin", and password: "password"
  INFO Time elapsed: 36m22s
  ```

  Important

  + The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
  + It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

### [6.12. Provisioning your own DNS records](#installation-gcp-provisioning-own-dns-records_installing-gcp-vpc) Copy linkLink copied to clipboard!

Use the IP address of the API server to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. Use the IP address of the Ingress service to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

Important

Before you use this feature, you must add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS".

**Prerequisites**

* You installed your cluster.
* You installed the `gcloud` CLI tool.

**Procedure**

1. Determine the infrastructure ID of your cluster by running the following command:

   ```
   $ infra_id=$(jq -r .infraID <installation_directory>/metadata.json)
   ```

   where:

   `<installation_directory>`
   :   Specifies the directory where you ran the installation program.
2. Find the IP address of the API server:

   1. If you installed a private cluster, determine the IP address of the API server by running the following command:

      ```
      $ gcloud compute forwarding-rules describe "${infra_id}-api-internal" --project=<project_name> --region <region_name> --format json | jq -r .IPAddress
      ```

      where:

      `<project_name>`
      :   Specifies the name of your Google Cloud project.

      `<region_name>`
      :   Specifies the region where you installed your cluster.
   2. If you installed a public cluster, determine the IP address of the API server by running the following command:

      ```
      $ gcloud compute forwarding-rules describe --global "${infra_id}-apiserver" --format json | jq -r .IPAddress
      ```
3. Use the IP address to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.
4. Find the IP address of the Ingress service:

   1. If you installed a private cluster, find the IP address of the Ingress service by running the following command:

      ```
      $ gcloud compute forwarding-rules list --project=<project_name> --filter="subnetwork:(projects/<project_name>/regions/<region_name>/subnetworks/<compute_subnet_name>)" --format="json" | jq -r '.[].IPAddress'
      ```

      where:

      `<project_name>`
      :   Specifies the name of your Google Cloud project.

      `<region_name>`
      :   Specifies the region where you installed your cluster.

      `<compute_subnet_name>`
      :   Specifies the name of the subnet that contains your compute nodes.
   2. If you installed a public cluster, find the IP address by using the forwarding rule:

      1. Find the forwarding rule for the Ingress service by running the following command:

         ```
         $ ingress_forwarding_rule=$(gcloud compute target-pools list --format=json --filter="instances[]~${infra_id}" | jq -r .[].name)
         ```
      2. Use the forwarding rule value to find the IP address of the Ingress service by running the following command:

         ```
         $ gcloud compute forwarding-rules describe --region "<region_name>" "${ingress_forwarding_rule}" --format json | jq -r .IPAddress
         ```

         where:

         `<region_name>`
         :   Specifies the region where you installed your cluster.
5. Use the IP address to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

### [6.13. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-gcp-vpc) Copy linkLink copied to clipboard!

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

### [6.14. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-gcp-vpc) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

### [6.15. Next steps](#next-steps-4) Copy linkLink copied to clipboard!

* [Customize your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations).
* If necessary, you can [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting).

## [Chapter 7. Installing a cluster on Google Cloud into a shared VPC](#installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

In OpenShift Container Platform version 4.22, you can install a cluster into a shared Virtual Private Cloud (VPC) on Google Cloud. In this installation method, the cluster is configured to use a VPC from a different Google Cloud project. A shared VPC enables an organization to connect resources from multiple projects to a common VPC network. You can communicate within the organization securely and efficiently by using internal IP addresses from that network. For more information about shared VPC, see [Shared VPC overview in the Google Cloud documentation](https://cloud.google.com/vpc/docs/shared-vpc).

The installation program provisions the rest of the required infrastructure, which you can further customize. To customize the installation, change parameters in the `install-config.yaml` file before you install the cluster.

### [7.1. Prerequisites](#installation-gcp-shared-vpc-prerequisites_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

* You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes.
* You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing).
* If you use a firewall, you [configured it to allow the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires access to.
* You [configured a Google Cloud project](#installing-gcp-account "Chapter 2. Configuring a Google Cloud project") to host the cluster. This project, known as the service project, must be attached to the host project. For more information, see [Attaching service projects in the Google Cloud documentation](https://cloud.google.com/vpc/docs/provisioning-shared-vpc#create-shared).
* You have a Google Cloud host project that contains a shared VPC network and that has a configured Cloud Router and Cloud NAT gateway, to ensure that internet access from the VPC is available. For more information, see [Cloud Router overview](https://cloud.google.com/network-connectivity/docs/router/concepts/overview) and [Cloud NAT overview](https://cloud.google.com/nat/docs/overview) (Google documentation).
* You have a Google Cloud service account that has the [required Google Cloud permissions](#minimum-required-permissions-ipi-gcp-xpn_installing-gcp-account "2.5.3. Required Google Cloud permissions for shared VPC installations") in both the host and service projects.
* If you want to provide your own private hosted zone, you must have created one in the service project with the DNS pattern `cluster-name.baseDomain.`, for example `testCluster.example.com.`. The private hosted zone must be bound to the VPC in the host project. For more information about cross-project binding, see [Create a zone with cross-project binding](https://cloud.google.com/dns/docs/zones/cross-project-binding) (Google documentation). If you do not provide a private hosted zone, the installation program will provision one automatically.
* If you manage your Google Cloud firewall rules, you [configured the required firewall rules](#installation-gcp-user-managed-firewall-rules_installing-gcp-account "2.6. Managing your own firewall rules").

### [7.2. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [7.3. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

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

### [7.4. Obtaining the installation program](#installation-obtaining-installer_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

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

### [7.5. Creating the installation files for Google Cloud](#installation-user-infra-generate_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on Google Cloud into a shared VPC, you must generate the `install-config.yaml` file and modify it so that the cluster uses the correct VPC networks, DNS zones, and project names.

#### [7.5.1. Manually creating the installation configuration file](#installation-initializing-manual_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

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
2. Edit the `install-config.yaml` file to set the parameters necessary for installation into a shared VPC.

   1. Define the network, subnets, and project names for the shared VPC:

      ```
      # ...
      platform:
        gcp:
          computeSubnet: <shared_vpc_compute_subnet>
          controlPlaneSubnet: <shared_vpc_control_plane_subnet>
          network: <shared_vpc_name>
          networkProjectID: <host_project_name>
          projectID: <service_project_name>
      ```

      where:

      `<shared_vpc_compute_subnet>`
      :   Specifies the name of the subnet in the shared VPC for compute machines to use.

      `<shared_vpc_control_plane_subnet>`
      :   Specifies the name of the subnet in the shared VPC for control plane machines to use.

      `<shared_vpc_name>`
      :   Specifies the name of the shared VPC.

      `<host_project_name>`
      :   Specifies the name of the host project where the shared VPC exists.

      `<service_project_name>`
      :   Specifies the name of the project where you want to install the cluster.
3. Customize the provided sample `install-config.yaml` file template and save the file in the `<installation_directory>`.

   Note

   You must name this configuration file `install-config.yaml`.
4. Back up the `install-config.yaml` file so that you can use it to install many clusters.

   Important

   Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.

#### [7.5.2. Enabling Shielded VMs](#installation-gcp-enabling-shielded-vms_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).

Note

Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use shielded VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            secureBoot: Enabled
     ```
  2. To use shielded VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            secureBoot: Enabled
     ```
  3. To use shielded VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            secureBoot: Enabled
     ```

#### [7.5.3. Enabling Confidential VMs](#installation-gcp-enabling-confidential-vms_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google’s documentation on [Confidential Computing](https://cloud.google.com/confidential-computing). You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

Note

Confidential VMs are currently not supported on 64-bit ARM architectures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use confidential VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
     ```

     1

     ```
            type: n2d-standard-8
     ```

     2

     ```
            onHostMaintenance: Terminate
     ```

     3

     [1](#CO12-1)
     :   Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional Google Cloud configuration parameters".

     [2](#CO12-2)
     :   Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see [Supported operating systems and machine types](https://cloud.google.com/compute/confidential-vm/docs/os-and-machine-type#machine-type).

     [3](#CO12-3)
     :   Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.
  2. To use confidential VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```
  3. To use confidential VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```

#### [7.5.4. Enabling a user-managed DNS](#installation-gcp-enabling-user-managed-DNS_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

You can install a cluster with a domain name server (DNS) solution that you manage instead of the default cluster-provisioned DNS solution. As a result, you can manage the API and Ingress DNS records in your own system rather than adding the records to the DNS of the cloud.

For example, your organization’s security policies might not allow the use of public DNS services such as Google Cloud DNS. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services.

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation.

**Prerequisites**

* You installed the `jq` package.

**Procedure**

* Before you deploy your cluster, use a text editor to open the `install-config.yaml` file and add the following stanza:

  + To enable user-managed DNS:

    ```
    platform:
      gcp:
        userProvisionedDNS: Enabled
    ```

    where:

    `Enabled`
    :   Enables user-provisioned DNS management.

For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records".

#### [7.5.5. Sample customized install-config.yaml file for Google Cloud](#installation-gcp-config-yaml_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

To specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters, you can customize the `install-config.yaml` file.

Important

This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.

```
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
controlPlane:
  name: master
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
compute:
- name: worker
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  gcp:
    projectID: sample-project
    region: us-east1
```

where:

`controlPlane`
:   Specifies parameters that apply to control plane machines.

`compute`
:   Specifies parameters that apply to compute machines.

`networking`
:   Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.

`platform`
:   Specifies parameters that apply to the infrastructure platform that hosts the cluster.

#### [7.5.6. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

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

### [7.6. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

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

### [7.7. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

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

### [7.8. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

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

### [7.9. Alternatives to storing administrator-level secrets in the kube-system project](#installing-gcp-manual-modes_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives:

* To manage long-term cloud credentials manually, follow the procedure in [Manually creating long-term credentials](#manually-create-iam_installing-gcp-shared-vpc "7.9.1. Manually creating long-term credentials").
* To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in [Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-gcp-shared-vpc "7.9.2. Configuring a Google Cloud cluster to use short-term credentials").

#### [7.9.1. Manually creating long-term credentials](#manually-create-iam_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

The Cloud Credential Operator (CCO) can be put into manual mode prior to installation in environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace.

**Procedure**

1. Add the following granular permissions to the Google Cloud account that the installation program uses:

   * compute.machineTypes.list
   * compute.regions.list
   * compute.zones.list
   * dns.changes.create
   * dns.changes.get
   * dns.managedZones.create
   * dns.managedZones.delete
   * dns.managedZones.get
   * dns.managedZones.list
   * dns.networks.bindPrivateDNSZone
   * dns.resourceRecordSets.create
   * dns.resourceRecordSets.delete
   * dns.resourceRecordSets.list
2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

   **Sample configuration file snippet**

   ```
   apiVersion: v1
   baseDomain: example.com
   credentialsMode: Manual
   # ...
   ```
3. If you have not previously created installation manifest files, do so by running the following command:

   ```
   $ openshift-install create manifests --dir <installation_directory>
   ```

   where `<installation_directory>` is the directory in which the installation program creates files.
4. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
5. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Specifies only the manifests that your specific cluster configuration requires.

   `<path_to_directory_with_installation_configuration>`
   :   Specifies the location of the `install-config.yaml` file.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       This command creates a YAML file for each `CredentialsRequest` object.

       **Sample `CredentialsRequest` object**

       ```
       apiVersion: cloudcredential.openshift.io/v1
       kind: CredentialsRequest
       metadata:
         name: <component_credentials_request>
         namespace: openshift-cloud-credential-operator
         ...
       spec:
         providerSpec:
           apiVersion: cloudcredential.openshift.io/v1
           kind: GCPProviderSpec
           predefinedRoles:
           - roles/storage.admin
           - roles/iam.serviceAccountUser
           skipServiceCheck: true
         ...
       ```
6. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

   **Sample `CredentialsRequest` object with secrets**

   ```
   apiVersion: cloudcredential.openshift.io/v1
   kind: CredentialsRequest
   metadata:
     name: <component_credentials_request>
     namespace: openshift-cloud-credential-operator
     ...
   spec:
     providerSpec:
       apiVersion: cloudcredential.openshift.io/v1
         ...
     secretRef:
       name: <component_secret>
       namespace: <component_namespace>
     ...
   ```

   **Sample `Secret` object**

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: <component_secret>
     namespace: <component_namespace>
   data:
     service_account.json: <base64_encoded_gcp_service_account_file>
   ```

   Important

   Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.

#### [7.9.2. Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

To install a cluster that is configured to use Google Cloud Workload Identity, you must configure the Cloud Credential Operator (CCO) utility and create the required Google Cloud resources for your cluster.

Important

When installing a cluster on a shared Virtual Private Cloud (VPC) by using short-lived credentials, you must grant the `compute.subnetworks.use` permission in the host project to Day 2 Operator service accounts.

After using the `ccoctl` utility to generate the Google Cloud credentials, manually grant this permission to the Cluster CAPI Operator and Machine API Operator service accounts.

##### [7.9.2.1. Configuring the Cloud Credential Operator utility](#cco-ccoctl-configuring_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment.

**Prerequisites**

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the OpenShift CLI (`oc`).

* You have added one of the following authentication options to the Google Cloud account that the `ccoctl` utility uses:

  + The **IAM Workload Identity Pool Admin** role
  + The following granular permissions:

    - `compute.projects.get`
    - `iam.googleapis.com/workloadIdentityPoolProviders.create`
    - `iam.googleapis.com/workloadIdentityPoolProviders.get`
    - `iam.googleapis.com/workloadIdentityPools.create`
    - `iam.googleapis.com/workloadIdentityPools.delete`
    - `iam.googleapis.com/workloadIdentityPools.get`
    - `iam.googleapis.com/workloadIdentityPools.undelete`
    - `iam.roles.create`
    - `iam.roles.delete`
    - `iam.roles.list`
    - `iam.roles.undelete`
    - `iam.roles.update`
    - `iam.serviceAccounts.create`
    - `iam.serviceAccounts.delete`
    - `iam.serviceAccounts.getIamPolicy`
    - `iam.serviceAccounts.list`
    - `iam.serviceAccounts.setIamPolicy`
    - `iam.workloadIdentityPoolProviders.get`
    - `iam.workloadIdentityPools.delete`
    - `resourcemanager.projects.get`
    - `resourcemanager.projects.getIamPolicy`
    - `resourcemanager.projects.setIamPolicy`
    - `storage.buckets.create`
    - `storage.buckets.delete`
    - `storage.buckets.get`
    - `storage.buckets.getIamPolicy`
    - `storage.buckets.setIamPolicy`
    - `storage.objects.create`
    - `storage.objects.delete`
    - `storage.objects.list`

**Procedure**

1. Set a variable for the OpenShift Container Platform release image by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:

   ```
   $ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
   ```

   Note

   Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
3. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:

   ```
   $ oc image extract $CCO_IMAGE \
     --file="/usr/bin/ccoctl.<rhel_version>" \
     -a ~/.pull-secret
   ```

   For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid:

   * `rhel8`: Specify this value for hosts that use RHEL 8.
   * `rhel9`: Specify this value for hosts that use RHEL 9.

   Note

   The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
4. Change the permissions to make `ccoctl` executable by running the following command:

   ```
   $ chmod 775 ccoctl
   ```

**Verification**

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:

  ```
  $ ./ccoctl
  ```

  **Example output**

  ```
  OpenShift credentials provisioning tool

  Usage:
    ccoctl [command]

  Available Commands:
    aws          Manage credentials objects for AWS cloud
    azure        Manage credentials objects for Azure
    gcp          Manage credentials objects for Google cloud
    help         Help about any command
    ibmcloud     Manage credentials objects for IBM Cloud
    nutanix      Manage credentials objects for Nutanix

  Flags:
    -h, --help   help for ccoctl

  Use "ccoctl [command] --help" for more information about a command.
  ```

##### [7.9.2.2. Creating Google Cloud resources with the Cloud Credential Operator utility](#cco-ccoctl-creating-at-once_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

You can use the `ccoctl gcp create-all` command to automate the creation of Google Cloud resources.

Note

By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.

**Prerequisites**

You must have:

* Extracted and prepared the `ccoctl` binary.

**Procedure**

1. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Specifies to include only the manifests that your specific cluster configuration requires.

   `<path_to_directory_with_installation_configuration>`
   :   Specifies the location of the `install-config.yaml` file.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       Note

       This command might take a few moments to run.
3. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:

   ```
   $ ccoctl gcp create-all \
     --name=<name> \
     --region=<gcp_region> \
     --project=<gcp_project_id> \
     --credentials-requests-dir=<path_to_credentials_requests_directory> \
     --key-storage-method=<key_storage_method>
   ```

   where:

   `<name>`
   :   Specifies the user-defined name for all created Google Cloud resources used for tracking. If you plan to install the Google Cloud Filestore Container Storage Interface (CSI) Driver Operator, retain this value.

   `<gcp_region>`
   :   Specifies the Google Cloud region in which cloud resources will be created.

   `<gcp_project_id>`
   :   Specifies the Google Cloud project ID in which cloud resources will be created.

   `<path_to_credentials_requests_directory>`
   :   Specifies the directory containing the files of `CredentialsRequest` manifests to create Google Cloud service accounts.

   `<key_storage_method>`
   :   Specifies the method for storing OIDC JWK files. Accepted values are `public-bucket` and `pool-jwk-file`. The default value `public-bucket` creates a public GCS bucket to host the OIDC configuration and JWK files. The `pool-jwk-file` value attaches the JWK directly to the workload identity pool provider without creating a public bucket. This parameter is optional.

       Note

       If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.

**Verification**

* To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory:

  ```
  $ ls <path_to_ccoctl_output_dir>/manifests
  ```

  **Example output**

  ```
  cluster-authentication-02-config.yaml
  openshift-cloud-controller-manager-gcp-ccm-cloud-credentials-credentials.yaml
  openshift-cloud-credential-operator-cloud-credential-operator-gcp-ro-creds-credentials.yaml
  openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
  openshift-cluster-api-capg-manager-bootstrap-credentials-credentials.yaml
  openshift-cluster-csi-drivers-gcp-pd-cloud-credentials-credentials.yaml
  openshift-image-registry-installer-cloud-credentials-credentials.yaml
  openshift-ingress-operator-cloud-credentials-credentials.yaml
  openshift-machine-api-gcp-cloud-credentials-credentials.yaml
  ```

  You can verify that the IAM service accounts are created by querying Google Cloud. For more information, refer to Google Cloud documentation on listing IAM service accounts.

##### [7.9.2.3. Restricting service account impersonation to the compute nodes service account](#restricting-sa-impersonation-compute-sa-gcp_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

After the Cloud Credential Operator utility (`ccoctl`) creates the resources for the cluster, you can restrict the Google Cloud `iam.serviceAccounts.actAs` permission that the `ccoctl` utility granted to the Machine API controller service account to the compute nodes service account.

Note

Restricting service account impersonation to the compute nodes service account is optional. If your organization does not require this change, you can continue to "Incorporating the Cloud Credential Operator utility manifests".

When the `ccoctl` utility assigns custom and Google Cloud predefined roles to OpenShift Container Platform components service accounts, it grants the `iam.serviceAccounts.actAs` permission to the Machine API controller service account at the Google Cloud project level. To reduce the scope of the `iam.serviceAccounts.actAs` permission, you identify the custom role of the Machine API controller service account and replace it with a role that has a more restricted set of permissions. To allow this component to work, you then grant the Machine API controller service account the Service Account User role on the service account of the compute nodes instead.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have used the `ccoctl` utility to create the cloud provider resources for your cluster.
* You have access to your `install-config.yaml` file.
* You have logged in to the Google Cloud CLI (`gcloud`) as a user with permissions to manage service accounts and roles.

**Procedure**

1. Obtain the following values from your `install-config.yaml` file:

   * The Google Cloud project name. In the YAML file, this is the value of the `platform.gcp.projectID` parameter.
   * The cluster name. In the YAML file, this is the value of the `metadata.name` parameter.
   * The service account for the compute nodes. In the YAML file, this is the value of the `compute[0].platform.gcp.serviceAccount` parameter.
2. Obtain the service account for the Machine API controller that the `ccoctl` utility created by running the following command:

   ```
   $ gcloud iam service-accounts list \
     --filter="displayName=<cluster_name>-openshift-machine-api-gcp" \
     --format='value(email)'
   ```

   where `<cluster_name>` is the value specified for the `metadata.name` parameter in your `install-config.yaml` file.
3. Obtain the role ID of the custom role for the Machine API controller service account by running the following command:

   ```
   $ gcloud projects get-iam-policy <project_name> \
     --flatten='bindings[].members' \
     --format='table(bindings.role)' \
     --filter="bindings.members:<machine_api_controller_service_account>"
   ```

   where `<machine_api_controller_service_account>` is the Machine API controller service account.
4. List the custom role permissions for the Machine API controller service account by running the following command:

   ```
   $ gcloud iam roles describe <machine_api_role> \
     --project <project_name>
   ```

   where `<machine_api_role>` is the role ID of the custom role for the Machine API controller service account.

   **Example output**

   ```
   etag: <etag_value>
   includedPermissions:
   - compute.acceleratorTypes.get
   - compute.acceleratorTypes.list
   - compute.disks.create
   - compute.disks.createTagBinding
   ...
   - compute.zones.get
   - compute.zones.list
   - iam.serviceAccounts.actAs
   - iam.serviceAccounts.get
   - iam.serviceAccounts.list
   - resourcemanager.tagValues.get
   - resourcemanager.tagValues.list
   - serviceusage.quotas.get
   - serviceusage.services.get
   - serviceusage.services.list
   name: projects/<project_name>/roles/<machine_api_role>
   stage: GA
   title: <project_name>-openshift-machine-api-gcp
   ```

   where `<project_name>` is the Google Cloud project name specified in the `install-config.yaml` file.

   Note

   This truncated example output might not match the permissions list for your cluster.
5. Create a custom role that includes all of the permissions from your output except for the `iam.serviceAccounts.actAs` permission by running a command similar to the following:

   ```
   $ gcloud iam roles create <machine_api_role>_without_actas \
   --project=<project_name> \
   --title=<machine_api_role>_without_actas \
   --description="Required permissions for the Machine API controller without the iam.serviceAccounts.actAs permission" \
   --permissions=compute.acceleratorTypes.get,\
   compute.acceleratorTypes.list,\
   compute.disks.create,\
   compute.disks.createTagBinding,\
   ...
   compute.zones.get,\
   compute.zones.list,\
   iam.serviceAccounts.get,\
   iam.serviceAccounts.list,\
   resourcemanager.tagValues.get,\
   resourcemanager.tagValues.list,\
   serviceusage.quotas.get,\
   serviceusage.services.get,\
   serviceusage.services.list
   ```

   In this example, the new role name is the original custom role name, `<machine_api_role>`, with a `_without_actas` string added to the end.

   Important

   This truncated example command might not match the permissions list for your cluster. You must use the list of permissions from the output of the `gcloud iam roles describe <machine_api_role> --project <project_name>` command on your cluster.
6. Remove the custom role that includes the `iam.serviceAccounts.actAs` permission from the Machine API controller service account by running the following command:

   ```
   $ gcloud projects remove-iam-policy-binding <project_name> \
     --member "serviceAccount:<machine_api_controller_service_account>" \
     --role "projects/<project_name>/roles/<machine_api_role>"
   ```

   where `<machine_api_role>` is the original custom role.
7. Grant the custom role that excludes the `iam.serviceAccounts.actAs` permission to the Machine API controller service account by running the following command:

   ```
   $ gcloud projects add-iam-policy-binding <project_name> \
     --member "serviceAccount:<machine_api_controller_service_account>" \
     --role "projects/<project_name>/roles/<machine_api_role>_without_actas
   ```

   where `<machine_api_role>_without_actas` is the new custom role.
8. Optional: To verify that the Machine API controller service account has the correct role, check the attached role ID by running the following command:

   ```
   $ gcloud projects get-iam-policy <project_name> \
     --flatten='bindings[].members' \
     --format='table(bindings.role)' \
     --filter="bindings.members:<machine_api_controller_service_account>"
   ```

   **Example output**

   ```
   ROLE
   projects/<project_name>/roles/<machine_api_role>_without_actas
   ```
9. Grant the Machine API controller service account the Service Account User role on the service account of the compute nodes by running the following command:

   ```
   $ gcloud iam service-accounts add-iam-policy-binding <compute_nodes_service_account> \
     --member="serviceAccount:<machine_api_controller_service_account>" \
     --role=roles/iam.serviceAccountUser
   ```

   where `<compute_nodes_service_account>` is the service account for your compute nodes. This value is the `compute[0].platform.gcp.serviceAccount` parameter in your `install-config.yaml` file.

##### [7.9.2.4. Incorporating the Cloud Credential Operator utility manifests](#cco-ccoctl-install-creating-manifests_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

To implement short-term security credentials managed outside the cluster for individual components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have configured the Cloud Credential Operator utility (`ccoctl`).
* You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility.

**Procedure**

1. Add the following granular permissions to the Google Cloud account that the installation program uses:

   * compute.machineTypes.list
   * compute.regions.list
   * compute.zones.list
   * dns.changes.create
   * dns.changes.get
   * dns.managedZones.create
   * dns.managedZones.delete
   * dns.managedZones.get
   * dns.managedZones.list
   * dns.networks.bindPrivateDNSZone
   * dns.resourceRecordSets.create
   * dns.resourceRecordSets.delete
   * dns.resourceRecordSets.list
2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

   **Sample configuration file snippet**

   ```
   apiVersion: v1
   baseDomain: example.com
   credentialsMode: Manual
   # ...
   ```
3. If you have not previously created installation manifest files, do so by running the following command:

   ```
   $ openshift-install create manifests --dir <installation_directory>
   ```

   where `<installation_directory>` is the directory in which the installation program creates files.
4. Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command:

   ```
   $ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
   ```
5. Copy the `tls` directory that contains the private key to the installation directory:

   ```
   $ cp -a /<path_to_ccoctl_output_dir>/tls .
   ```

### [7.10. Deploying the cluster](#installation-launching-installer_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

Important

You can run the `create cluster` command of the installation program only once, during initial installation.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

**Procedure**

1. Remove any existing Google Cloud credentials that do not use the service account key for the Google Cloud account that you configured for your cluster and that are stored in the following locations:

   * The `GOOGLE_CREDENTIALS`, `GOOGLE_CLOUD_KEYFILE_JSON`, or `GCLOUD_KEYFILE_JSON` environment variables
   * The `~/.gcp/osServiceAccount.json` file
   * The `gcloud cli` default credentials
2. In the directory that contains the installation program, initialize the cluster deployment by running the following command:

   ```
   $ ./openshift-install create cluster --dir <installation_directory> \
       --log-level=info
   ```

   * For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.
   * To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.
3. Optional: You can reduce the number of permissions for the service account that you used to install the cluster.

   * If you assigned the `Owner` role to your service account, you can remove that role and replace it with the `Viewer` role.
   * If you included the `Service Account Key Admin` role, you can remove it.

**Verification**

When the cluster deployment completes successfully:

* The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.
* Credential information also outputs to `<installation_directory>/.openshift_install.log`.

  Important

  Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.

  **Example output**

  ```
  ...
  INFO Install complete!
  INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
  INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
  INFO Login to the console with user: "kubeadmin", and password: "password"
  INFO Time elapsed: 36m22s
  ```

  Important

  + The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
  + It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

### [7.11. Provisioning your own DNS records](#installation-gcp-provisioning-own-dns-records_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

Use the IP address of the API server to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. Use the IP address of the Ingress service to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

Important

Before you use this feature, you must add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS".

**Prerequisites**

* You installed your cluster.
* You installed the `gcloud` CLI tool.

**Procedure**

1. Determine the infrastructure ID of your cluster by running the following command:

   ```
   $ infra_id=$(jq -r .infraID <installation_directory>/metadata.json)
   ```

   where:

   `<installation_directory>`
   :   Specifies the directory where you ran the installation program.
2. Find the IP address of the API server:

   1. If you installed a private cluster, determine the IP address of the API server by running the following command:

      ```
      $ gcloud compute forwarding-rules describe "${infra_id}-api-internal" --project=<project_name> --region <region_name> --format json | jq -r .IPAddress
      ```

      where:

      `<project_name>`
      :   Specifies the name of your Google Cloud project.

      `<region_name>`
      :   Specifies the region where you installed your cluster.
   2. If you installed a public cluster, determine the IP address of the API server by running the following command:

      ```
      $ gcloud compute forwarding-rules describe --global "${infra_id}-apiserver" --format json | jq -r .IPAddress
      ```
3. Use the IP address to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.
4. Find the IP address of the Ingress service:

   1. If you installed a private cluster, find the IP address of the Ingress service by running the following command:

      ```
      $ gcloud compute forwarding-rules list --project=<project_name> --filter="subnetwork:(projects/<project_name>/regions/<region_name>/subnetworks/<compute_subnet_name>)" --format="json" | jq -r '.[].IPAddress'
      ```

      where:

      `<project_name>`
      :   Specifies the name of your Google Cloud project.

      `<region_name>`
      :   Specifies the region where you installed your cluster.

      `<compute_subnet_name>`
      :   Specifies the name of the subnet that contains your compute nodes.
   2. If you installed a public cluster, find the IP address by using the forwarding rule:

      1. Find the forwarding rule for the Ingress service by running the following command:

         ```
         $ ingress_forwarding_rule=$(gcloud compute target-pools list --format=json --filter="instances[]~${infra_id}" | jq -r .[].name)
         ```
      2. Use the forwarding rule value to find the IP address of the Ingress service by running the following command:

         ```
         $ gcloud compute forwarding-rules describe --region "<region_name>" "${ingress_forwarding_rule}" --format json | jq -r .IPAddress
         ```

         where:

         `<region_name>`
         :   Specifies the region where you installed your cluster.
5. Use the IP address to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

### [7.12. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

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

### [7.13. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

### [7.14. Next steps](#installation-gcp-shared-vpc-next-steps_installing-gcp-shared-vpc) Copy linkLink copied to clipboard!

* [Customize your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations).
* If necessary, you can [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting).

## [Chapter 8. Installing a private cluster on Google Cloud](#installing-gcp-private) Copy linkLink copied to clipboard!

In OpenShift Container Platform version 4.22, you can install a private cluster into an existing VPC on Google Cloud. The installation program provisions the rest of the required infrastructure, which you can further customize. To customize the installation, you modify parameters in the `install-config.yaml` file before you install the cluster.

### [8.1. Prerequisites](#prerequisites-4) Copy linkLink copied to clipboard!

* You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes.
* You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing).
* You [configured a Google Cloud project](#installing-gcp-account "Chapter 2. Configuring a Google Cloud project") to host the cluster.
* If you use a firewall, you [configured it to allow the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires access to.

### [8.2. Private clusters](#private-clusters-default_installing-gcp-private) Copy linkLink copied to clipboard!

You can deploy a private OpenShift Container Platform cluster that does not expose external endpoints. Private clusters are accessible from only an internal network and are not visible to the internet.

By default, OpenShift Container Platform is provisioned to use publicly-accessible DNS and endpoints. A private cluster sets the DNS, Ingress Controller, and API server to private when you deploy your cluster. This means that the cluster resources are only accessible from your internal network and are not visible to the internet.

Important

If the cluster has any public subnets, load balancer services created by administrators might be publicly accessible. To ensure cluster security, verify that these services are explicitly annotated as private.

To deploy a private cluster, you must:

* Use existing networking that meets your requirements. Your cluster resources might be shared between other clusters on the network.
* Deploy from a machine that has access to:

  + The API services for the cloud to which you provision.
  + The hosts on the network that you provision.
  + The internet to obtain installation media.

#### [8.2.1. Private clusters in Google Cloud](#private-clusters-about-gcp_installing-gcp-private) Copy linkLink copied to clipboard!

To create a private cluster on Google Cloud, you must provide an existing VPC network and subnets to host the cluster, and you must specify `publish: Internal` in your `install-config.yaml` file. The installation program must also be able to resolve the DNS records that the cluster requires. The installation program configures the Ingress Operator and API server for only internal traffic.

The cluster still requires access to internet to access the Google Cloud APIs.

The following items are not required or created when you install a private cluster:

* Public subnets
* Public network load balancers, which support public ingress
* A public DNS zone that matches the `baseDomain` for the cluster

The installation program does use the `baseDomain` that you specify to create a private DNS zone and the required records for the cluster. The cluster is configured so that the Operators do not create public records for the cluster and all cluster machines are placed in the private subnets that you specify.

Because it is not possible to limit access to external load balancers based on source tags, the private cluster uses only internal load balancers to allow access to internal instances.

The internal load balancer relies on instance groups rather than the target pools that the network load balancers use. The installation program creates instance groups for each zone, even if there is no instance in that group.

* The cluster IP address is internal only.
* One forwarding rule manages both the Kubernetes API and machine config server ports.
* The backend service is comprised of each zone’s instance group and, while it exists, the bootstrap instance group.
* The firewall uses a single rule that is based on only internal source ranges.

##### [8.2.1.1. Limitations](#private-clusters-limitations-gcp_installing-gcp-private) Copy linkLink copied to clipboard!

No health check for the Machine config server, `/healthz`, runs because of a difference in load balancer functionality. Two internal load balancers cannot share a single IP address, but two network load balancers can share a single external IP address. Instead, the health of an instance is determined entirely by the `/readyz` check on port 6443.

### [8.3. About using a custom VPC](#installation-about-custom-gcp-vpc_installing-gcp-private) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you can deploy a cluster into an existing VPC in Google Cloud. If you do, you must also use existing subnets within the VPC and routing rules.

By deploying OpenShift Container Platform into an existing Google Cloud VPC, you might be able to avoid limit constraints in new accounts or more easily abide by the operational constraints that your company’s guidelines set. This is a good option to use if you cannot obtain the infrastructure creation permissions that are required to create the VPC yourself.

#### [8.3.1. Requirements for using your VPC](#installation-about-custom-gcp-vpcs-requirements_installing-gcp-private) Copy linkLink copied to clipboard!

The installation program will no longer create the following components:

* VPC
* Subnets
* Cloud router
* Cloud NAT
* NAT IP addresses

If you use a custom VPC, you must correctly configure it and its subnets for the installation program and the cluster to use. The installation program cannot subdivide network ranges for the cluster to use, set route tables for the subnets, or set VPC options like DHCP, so you must do so before you install the cluster.

Your VPC and subnets must meet the following characteristics:

* The VPC must be in the same Google Cloud project that you deploy the OpenShift Container Platform cluster to.
* To allow access to the internet from the control plane and compute machines, you must configure cloud NAT on the subnets to allow egress to it. These machines do not have a public address. Even if you do not require access to the internet, you must allow egress to the VPC network to obtain the installation program and images. Because multiple cloud NATs cannot be configured on the shared subnets, the installation program cannot configure it.

To ensure that the subnets that you provide are suitable, the installation program confirms the following data:

* All the subnets that you specify exist and belong to the VPC that you specified.
* The subnet CIDRs belong to the machine CIDR.
* You must provide a subnet to deploy the cluster control plane and compute machines to. You can use the same subnet for both machine types.

If you destroy a cluster that uses an existing VPC, the VPC is not deleted.

#### [8.3.2. Division of permissions](#installation-about-custom-gcp-permissions_installing-gcp-private) Copy linkLink copied to clipboard!

Starting with OpenShift Container Platform 4.3, you do not need all of the permissions that are required for an installation program-provisioned infrastructure cluster to deploy a cluster. This change mimics the division of permissions that you might have at your company: some individuals can create different resources in your clouds than others. For example, you might be able to create application-specific items, like instances, buckets, and load balancers, but not networking-related components such as VPCs, subnets, or Ingress rules.

The Google Cloud credentials that you use when you create your cluster do not need the networking permissions that are required to make VPCs and core networking components within the VPC, such as subnets, routing tables, internet gateways, NAT, and VPN. You still need permission to make the application resources that the machines within the cluster require, such as load balancers, security groups, storage, and nodes.

#### [8.3.3. Isolation between clusters](#installation-about-custom-gcp-vpcs-isolation_installing-gcp-private) Copy linkLink copied to clipboard!

If you deploy OpenShift Container Platform to an existing network, the isolation of cluster services is preserved by firewall rules that reference the machines in your cluster by the cluster’s infrastructure ID. Only traffic within the cluster is allowed.

If you deploy multiple clusters to the same VPC, the following components might share access between clusters:

* The API, which is globally available with an external publishing strategy or available throughout the network in an internal publishing strategy
* Debugging tools, such as ports on VM instances that are open to the machine CIDR for SSH and ICMP access

### [8.4. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-gcp-private) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [8.5. Generating a key pair for cluster node SSH access](#ssh-agent-using_installing-gcp-private) Copy linkLink copied to clipboard!

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

### [8.6. Obtaining the installation program](#installation-obtaining-installer_installing-gcp-private) Copy linkLink copied to clipboard!

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

### [8.7. Manually creating the installation configuration file](#installation-initializing-manual_installing-gcp-private) Copy linkLink copied to clipboard!

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
2. Edit the `install-config.yaml` file to set the `publish: Internal` parameter.
3. Edit the `install-config.yaml` file to set the parameters necessary for installation into an existing VPC.

   1. Define the network and subnets for the VPC to install the cluster in under the parent `platform.gcp` field:

      ```
      platform:
        gcp:
          network: <existing_vpc>
          controlPlaneSubnet: <control_plane_subnet>
          computeSubnet: <compute_subnet>
      ```

      For the `platform.gcp.network` parameter, specify the name for the existing Google VPC. For the `platform.gcp.controlPlaneSubnet` and `platform.gcp.computeSubnet` parameters, specify the existing subnets to deploy the control plane machines and compute machines, respectively.
4. Customize the provided sample `install-config.yaml` file template and save the file in the `<installation_directory>`.

   Note

   You must name this configuration file `install-config.yaml`.
5. Back up the `install-config.yaml` file so that you can use it to install many clusters.

   Important

   Back up the `install-config.yaml` file now, because the installation process consumes the file in the next step.

#### [8.7.1. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-gcp-private) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 8.1. Minimum resource requirements

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Show more

* One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
* OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance.
* As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines.

Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* ppc64le architecture requires IBM® Power9 ISA
* s390x architecture requires IBM® z14 ISA

For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

#### [8.7.2. Tested instance types for Google Cloud](#installation-gcp-tested-machine-types_installing-gcp-private) Copy linkLink copied to clipboard!

The following Google Cloud instance types have been tested with OpenShift Container Platform.

Note

Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) (Google documentation).

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see [machine series support for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in *Storage*.

See the following machine series:

* `A2`
* `A3`
* `C2`
* `C2D`
* `C3`
* `C3D`
* `C4`
* `E2`
* `M1`
* `N1`
* `N2`
* `N2D`
* `N4`
* `Tau T2D`

#### [8.7.3. Tested instance types for Google Cloud on 64-bit ARM infrastructures](#installation-gcp-tested-machine-types-arm_installing-gcp-private) Copy linkLink copied to clipboard!

The following Google Cloud 64-bit ARM instance types have been tested with OpenShift Container Platform.

See the following machine series for 64-bit ARM machines:

* `C4A`
* `N4A`
* `Tau T2A`

#### [8.7.4. Using custom machine types](#installation-custom-machine-types_installing-gcp-private) Copy linkLink copied to clipboard!

Using a custom machine type to install a OpenShift Container Platform cluster is supported.

Consider the following when using a custom machine type:

* Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation".
* The name of the custom machine type must adhere to the following syntax:

  `custom-<number_of_cpus>-<amount_of_memory_in_mb>`

  For example, `custom-6-20480`.

As part of the installation process, you specify the custom machine type in the `install-config.yaml` file.

**Sample `install-config.yaml` file with a custom machine type**

```
compute:
- architecture: amd64
  hyperthreading: Enabled
  name: worker
  platform:
    gcp:
      type: custom-6-20480
  replicas: 2
controlPlane:
  architecture: amd64
  hyperthreading: Enabled
  name: master
  platform:
    gcp:
      type: custom-6-20480
  replicas: 3
```

#### [8.7.5. Enabling Shielded VMs](#installation-gcp-enabling-shielded-vms_installing-gcp-private) Copy linkLink copied to clipboard!

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).

Note

Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use shielded VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            secureBoot: Enabled
     ```
  2. To use shielded VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            secureBoot: Enabled
     ```
  3. To use shielded VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            secureBoot: Enabled
     ```

#### [8.7.6. Enabling Confidential VMs](#installation-gcp-enabling-confidential-vms_installing-gcp-private) Copy linkLink copied to clipboard!

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google’s documentation on [Confidential Computing](https://cloud.google.com/confidential-computing). You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

Note

Confidential VMs are currently not supported on 64-bit ARM architectures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use confidential VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
     ```

     1

     ```
            type: n2d-standard-8
     ```

     2

     ```
            onHostMaintenance: Terminate
     ```

     3

     [1](#CO13-1)
     :   Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional Google Cloud configuration parameters".

     [2](#CO13-2)
     :   Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see [Supported operating systems and machine types](https://cloud.google.com/compute/confidential-vm/docs/os-and-machine-type#machine-type).

     [3](#CO13-3)
     :   Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.
  2. To use confidential VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```
  3. To use confidential VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```

#### [8.7.7. Enabling a user-managed DNS](#installation-gcp-enabling-user-managed-DNS_installing-gcp-private) Copy linkLink copied to clipboard!

You can install a cluster with a domain name server (DNS) solution that you manage instead of the default cluster-provisioned DNS solution. As a result, you can manage the API and Ingress DNS records in your own system rather than adding the records to the DNS of the cloud.

For example, your organization’s security policies might not allow the use of public DNS services such as Google Cloud DNS. In such scenarios, you can use your own DNS service to bypass the public DNS service and manage your own DNS for the IP addresses of the API and Ingress services.

If you enable user-managed DNS during installation, the installation program provisions DNS records for the API and Ingress services only within the cluster. To ensure access from outside the cluster, you must provision the DNS records in an external DNS service of your choice for the API and Ingress services after installation.

**Prerequisites**

* You installed the `jq` package.

**Procedure**

* Before you deploy your cluster, use a text editor to open the `install-config.yaml` file and add the following stanza:

  + To enable user-managed DNS:

    ```
    platform:
      gcp:
        userProvisionedDNS: Enabled
    ```

    where:

    `Enabled`
    :   Enables user-provisioned DNS management.

For information about provisioning your DNS records for the API server and the Ingress services, see "Provisioning your own DNS records".

#### [8.7.8. Sample customized install-config.yaml file for Google Cloud](#installation-gcp-config-yaml_installing-gcp-private) Copy linkLink copied to clipboard!

To specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters, you can customize the `install-config.yaml` file.

Important

This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.

```
apiVersion: v1
baseDomain: example.com
pullSecret: '{"auths": ...}'
controlPlane:
  name: master
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
compute:
- name: worker
  replicas: 3
  platform:
    gcp:
      type: n2-standard-4
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
platform:
  gcp:
    projectID: sample-project
    region: us-east1
```

where:

`controlPlane`
:   Specifies parameters that apply to control plane machines.

`compute`
:   Specifies parameters that apply to compute machines.

`networking`
:   Specifies parameters that apply to the cluster networking configuration. If you do not provide networking values, the installation program provides default values.

`platform`
:   Specifies parameters that apply to the infrastructure platform that hosts the cluster.

#### [8.7.9. Create an Ingress Controller with global access on Google Cloud](#nw-gcp-global-access-configuration_installing-gcp-private) Copy linkLink copied to clipboard!

You can create an Ingress Controller that has global access to a Google Cloud cluster. Global access is only available to Ingress Controllers using internal load balancers.

**Prerequisites**

* You created the `install-config.yaml` and complete any modifications to it.

**Procedure**

Create an Ingress Controller with global access on a new Google Cloud cluster.

1. Change to the directory that contains the installation program and create a manifest file:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```

   1

   [1](#CO14-1)
   :   For `<installation_directory>`, specify the name of the directory that contains the `install-config.yaml` file for your cluster.
2. Create a file that is named `cluster-ingress-default-ingresscontroller.yaml` in the `<installation_directory>/manifests/` directory:

   ```
   $ touch <installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml
   ```

   1

   [1](#CO15-1)
   :   For `<installation_directory>`, specify the directory name that contains the `manifests/` directory for your cluster.

   After creating the file, several network configuration files are in the `manifests/` directory, as shown:

   ```
   $ ls <installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml
   ```

   **Example output**

   ```
   cluster-ingress-default-ingresscontroller.yaml
   ```
3. Open the `cluster-ingress-default-ingresscontroller.yaml` file in an editor and enter a custom resource (CR) that describes the Operator configuration you want:

   **Sample `clientAccess` configuration to `Global`**

   ```
     apiVersion: operator.openshift.io/v1
     kind: IngressController
     metadata:
       name: default
       namespace: openshift-ingress-operator
     spec:
       endpointPublishingStrategy:
         loadBalancer:
           providerParameters:
             gcp:
               clientAccess: Global
   ```

   1

   ```
             type: GCP
           scope: Internal
   ```

   2

   ```
         type: LoadBalancerService
   ```

   [1](#CO16-1)
   :   Set `gcp.clientAccess` to `Global`.

   [2](#CO16-2)
   :   Global access is only available to Ingress Controllers using internal load balancers.

#### [8.7.10. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-gcp-private) Copy linkLink copied to clipboard!

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

### [8.8. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-gcp-private) Copy linkLink copied to clipboard!

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

### [8.9. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-gcp-private) Copy linkLink copied to clipboard!

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

### [8.10. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-gcp-private) Copy linkLink copied to clipboard!

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

### [8.11. Alternatives to storing administrator-level secrets in the kube-system project](#installing-gcp-manual-modes_installing-gcp-private) Copy linkLink copied to clipboard!

By default, administrator secrets are stored in the `kube-system` project. If you configured the `credentialsMode` parameter in the `install-config.yaml` file to `Manual`, you must use one of the following alternatives:

* To manage long-term cloud credentials manually, follow the procedure in [Manually creating long-term credentials](#manually-create-iam_installing-gcp-private "8.11.1. Manually creating long-term credentials").
* To implement short-term credentials that are managed outside the cluster for individual components, follow the procedures in [Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-gcp-private "8.11.2. Configuring a Google Cloud cluster to use short-term credentials").

#### [8.11.1. Manually creating long-term credentials](#manually-create-iam_installing-gcp-private) Copy linkLink copied to clipboard!

The Cloud Credential Operator (CCO) can be put into manual mode prior to installation in environments where the cloud identity and access management (IAM) APIs are not reachable, or the administrator prefers not to store an administrator-level credential secret in the cluster `kube-system` namespace.

**Procedure**

1. Add the following granular permissions to the Google Cloud account that the installation program uses:

   * compute.machineTypes.list
   * compute.regions.list
   * compute.zones.list
   * dns.changes.create
   * dns.changes.get
   * dns.managedZones.create
   * dns.managedZones.delete
   * dns.managedZones.get
   * dns.managedZones.list
   * dns.networks.bindPrivateDNSZone
   * dns.resourceRecordSets.create
   * dns.resourceRecordSets.delete
   * dns.resourceRecordSets.list
2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

   **Sample configuration file snippet**

   ```
   apiVersion: v1
   baseDomain: example.com
   credentialsMode: Manual
   # ...
   ```
3. If you have not previously created installation manifest files, do so by running the following command:

   ```
   $ openshift-install create manifests --dir <installation_directory>
   ```

   where `<installation_directory>` is the directory in which the installation program creates files.
4. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
5. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Specifies only the manifests that your specific cluster configuration requires.

   `<path_to_directory_with_installation_configuration>`
   :   Specifies the location of the `install-config.yaml` file.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       This command creates a YAML file for each `CredentialsRequest` object.

       **Sample `CredentialsRequest` object**

       ```
       apiVersion: cloudcredential.openshift.io/v1
       kind: CredentialsRequest
       metadata:
         name: <component_credentials_request>
         namespace: openshift-cloud-credential-operator
         ...
       spec:
         providerSpec:
           apiVersion: cloudcredential.openshift.io/v1
           kind: GCPProviderSpec
           predefinedRoles:
           - roles/storage.admin
           - roles/iam.serviceAccountUser
           skipServiceCheck: true
         ...
       ```
6. Create YAML files for secrets in the `openshift-install` manifests directory that you generated previously. The secrets must be stored using the namespace and secret name defined in the `spec.secretRef` for each `CredentialsRequest` object.

   **Sample `CredentialsRequest` object with secrets**

   ```
   apiVersion: cloudcredential.openshift.io/v1
   kind: CredentialsRequest
   metadata:
     name: <component_credentials_request>
     namespace: openshift-cloud-credential-operator
     ...
   spec:
     providerSpec:
       apiVersion: cloudcredential.openshift.io/v1
         ...
     secretRef:
       name: <component_secret>
       namespace: <component_namespace>
     ...
   ```

   **Sample `Secret` object**

   ```
   apiVersion: v1
   kind: Secret
   metadata:
     name: <component_secret>
     namespace: <component_namespace>
   data:
     service_account.json: <base64_encoded_gcp_service_account_file>
   ```

   Important

   Before upgrading a cluster that uses manually maintained credentials, you must ensure that the CCO is in an upgradeable state.

#### [8.11.2. Configuring a Google Cloud cluster to use short-term credentials](#installing-gcp-with-short-term-creds_installing-gcp-private) Copy linkLink copied to clipboard!

To install a cluster that is configured to use Google Cloud Workload Identity, you must configure the CCO utility and create the required Google Cloud resources for your cluster.

##### [8.11.2.1. Configuring the Cloud Credential Operator utility](#cco-ccoctl-configuring_installing-gcp-private) Copy linkLink copied to clipboard!

To create and manage cloud credentials from outside of the cluster when the Cloud Credential Operator (CCO) is operating in manual mode, extract and prepare the CCO utility (`ccoctl`) binary.

Note

The `ccoctl` utility is a Linux binary that must run in a Linux environment.

**Prerequisites**

* You have access to an OpenShift Container Platform account with cluster administrator access.
* You have installed the OpenShift CLI (`oc`).

* You have added one of the following authentication options to the Google Cloud account that the `ccoctl` utility uses:

  + The **IAM Workload Identity Pool Admin** role
  + The following granular permissions:

    - `compute.projects.get`
    - `iam.googleapis.com/workloadIdentityPoolProviders.create`
    - `iam.googleapis.com/workloadIdentityPoolProviders.get`
    - `iam.googleapis.com/workloadIdentityPools.create`
    - `iam.googleapis.com/workloadIdentityPools.delete`
    - `iam.googleapis.com/workloadIdentityPools.get`
    - `iam.googleapis.com/workloadIdentityPools.undelete`
    - `iam.roles.create`
    - `iam.roles.delete`
    - `iam.roles.list`
    - `iam.roles.undelete`
    - `iam.roles.update`
    - `iam.serviceAccounts.create`
    - `iam.serviceAccounts.delete`
    - `iam.serviceAccounts.getIamPolicy`
    - `iam.serviceAccounts.list`
    - `iam.serviceAccounts.setIamPolicy`
    - `iam.workloadIdentityPoolProviders.get`
    - `iam.workloadIdentityPools.delete`
    - `resourcemanager.projects.get`
    - `resourcemanager.projects.getIamPolicy`
    - `resourcemanager.projects.setIamPolicy`
    - `storage.buckets.create`
    - `storage.buckets.delete`
    - `storage.buckets.get`
    - `storage.buckets.getIamPolicy`
    - `storage.buckets.setIamPolicy`
    - `storage.objects.create`
    - `storage.objects.delete`
    - `storage.objects.list`

**Procedure**

1. Set a variable for the OpenShift Container Platform release image by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Obtain the CCO container image from the OpenShift Container Platform release image by running the following command:

   ```
   $ CCO_IMAGE=$(oc adm release info --image-for='cloud-credential-operator' $RELEASE_IMAGE -a ~/.pull-secret)
   ```

   Note

   Ensure that the architecture of the `$RELEASE_IMAGE` matches the architecture of the environment in which you will use the `ccoctl` tool.
3. Extract the `ccoctl` binary from the CCO container image within the OpenShift Container Platform release image by running the following command:

   ```
   $ oc image extract $CCO_IMAGE \
     --file="/usr/bin/ccoctl.<rhel_version>" \
     -a ~/.pull-secret
   ```

   For `<rhel_version>`, specify the value that corresponds to the version of Red Hat Enterprise Linux (RHEL) that the host uses. If no value is specified, `ccoctl.rhel8` is used by default. The following values are valid:

   * `rhel8`: Specify this value for hosts that use RHEL 8.
   * `rhel9`: Specify this value for hosts that use RHEL 9.

   Note

   The `ccoctl` binary is created in the directory from where you executed the command and not in `/usr/bin/`. You must rename the directory or move the `ccoctl.<rhel_version>` binary to `ccoctl`.
4. Change the permissions to make `ccoctl` executable by running the following command:

   ```
   $ chmod 775 ccoctl
   ```

**Verification**

* To verify that `ccoctl` is ready to use, display the help file. Use a relative file name when you run the command, for example:

  ```
  $ ./ccoctl
  ```

  **Example output**

  ```
  OpenShift credentials provisioning tool

  Usage:
    ccoctl [command]

  Available Commands:
    aws          Manage credentials objects for AWS cloud
    azure        Manage credentials objects for Azure
    gcp          Manage credentials objects for Google cloud
    help         Help about any command
    ibmcloud     Manage credentials objects for IBM Cloud
    nutanix      Manage credentials objects for Nutanix

  Flags:
    -h, --help   help for ccoctl

  Use "ccoctl [command] --help" for more information about a command.
  ```

##### [8.11.2.2. Creating Google Cloud resources with the Cloud Credential Operator utility](#cco-ccoctl-creating-at-once_installing-gcp-private) Copy linkLink copied to clipboard!

You can use the `ccoctl gcp create-all` command to automate the creation of Google Cloud resources.

Note

By default, `ccoctl` creates objects in the directory in which the commands are run. To create the objects in a different directory, use the `--output-dir` flag. This procedure uses `<path_to_ccoctl_output_dir>` to refer to this directory.

**Prerequisites**

You must have:

* Extracted and prepared the `ccoctl` binary.

**Procedure**

1. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Extract the list of `CredentialsRequest` objects from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --install-config=<path_to_directory_with_installation_configuration>/install-config.yaml \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   Specifies to include only the manifests that your specific cluster configuration requires.

   `<path_to_directory_with_installation_configuration>`
   :   Specifies the location of the `install-config.yaml` file.

   `<path_to_directory_for_credentials_requests>`
   :   Specifies the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.

       Note

       This command might take a few moments to run.
3. Use the `ccoctl` tool to process all `CredentialsRequest` objects by running the following command:

   ```
   $ ccoctl gcp create-all \
     --name=<name> \
     --region=<gcp_region> \
     --project=<gcp_project_id> \
     --credentials-requests-dir=<path_to_credentials_requests_directory> \
     --key-storage-method=<key_storage_method>
   ```

   where:

   `<name>`
   :   Specifies the user-defined name for all created Google Cloud resources used for tracking. If you plan to install the Google Cloud Filestore Container Storage Interface (CSI) Driver Operator, retain this value.

   `<gcp_region>`
   :   Specifies the Google Cloud region in which cloud resources will be created.

   `<gcp_project_id>`
   :   Specifies the Google Cloud project ID in which cloud resources will be created.

   `<path_to_credentials_requests_directory>`
   :   Specifies the directory containing the files of `CredentialsRequest` manifests to create Google Cloud service accounts.

   `<key_storage_method>`
   :   Specifies the method for storing OIDC JWK files. Accepted values are `public-bucket` and `pool-jwk-file`. The default value `public-bucket` creates a public GCS bucket to host the OIDC configuration and JWK files. The `pool-jwk-file` value attaches the JWK directly to the workload identity pool provider without creating a public bucket. This parameter is optional.

       Note

       If your cluster uses Technology Preview features that are enabled by the `TechPreviewNoUpgrade` feature set, you must include the `--enable-tech-preview` parameter.

**Verification**

* To verify that the OpenShift Container Platform secrets are created, list the files in the `<path_to_ccoctl_output_dir>/manifests` directory:

  ```
  $ ls <path_to_ccoctl_output_dir>/manifests
  ```

  **Example output**

  ```
  cluster-authentication-02-config.yaml
  openshift-cloud-controller-manager-gcp-ccm-cloud-credentials-credentials.yaml
  openshift-cloud-credential-operator-cloud-credential-operator-gcp-ro-creds-credentials.yaml
  openshift-cloud-network-config-controller-cloud-credentials-credentials.yaml
  openshift-cluster-api-capg-manager-bootstrap-credentials-credentials.yaml
  openshift-cluster-csi-drivers-gcp-pd-cloud-credentials-credentials.yaml
  openshift-image-registry-installer-cloud-credentials-credentials.yaml
  openshift-ingress-operator-cloud-credentials-credentials.yaml
  openshift-machine-api-gcp-cloud-credentials-credentials.yaml
  ```

  You can verify that the IAM service accounts are created by querying Google Cloud. For more information, refer to Google Cloud documentation on listing IAM service accounts.

##### [8.11.2.3. Restricting service account impersonation to the compute nodes service account](#restricting-sa-impersonation-compute-sa-gcp_installing-gcp-private) Copy linkLink copied to clipboard!

After the Cloud Credential Operator utility (`ccoctl`) creates the resources for the cluster, you can restrict the Google Cloud `iam.serviceAccounts.actAs` permission that the `ccoctl` utility granted to the Machine API controller service account to the compute nodes service account.

Note

Restricting service account impersonation to the compute nodes service account is optional. If your organization does not require this change, you can continue to "Incorporating the Cloud Credential Operator utility manifests".

When the `ccoctl` utility assigns custom and Google Cloud predefined roles to OpenShift Container Platform components service accounts, it grants the `iam.serviceAccounts.actAs` permission to the Machine API controller service account at the Google Cloud project level. To reduce the scope of the `iam.serviceAccounts.actAs` permission, you identify the custom role of the Machine API controller service account and replace it with a role that has a more restricted set of permissions. To allow this component to work, you then grant the Machine API controller service account the Service Account User role on the service account of the compute nodes instead.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have used the `ccoctl` utility to create the cloud provider resources for your cluster.
* You have access to your `install-config.yaml` file.
* You have logged in to the Google Cloud CLI (`gcloud`) as a user with permissions to manage service accounts and roles.

**Procedure**

1. Obtain the following values from your `install-config.yaml` file:

   * The Google Cloud project name. In the YAML file, this is the value of the `platform.gcp.projectID` parameter.
   * The cluster name. In the YAML file, this is the value of the `metadata.name` parameter.
   * The service account for the compute nodes. In the YAML file, this is the value of the `compute[0].platform.gcp.serviceAccount` parameter.
2. Obtain the service account for the Machine API controller that the `ccoctl` utility created by running the following command:

   ```
   $ gcloud iam service-accounts list \
     --filter="displayName=<cluster_name>-openshift-machine-api-gcp" \
     --format='value(email)'
   ```

   where `<cluster_name>` is the value specified for the `metadata.name` parameter in your `install-config.yaml` file.
3. Obtain the role ID of the custom role for the Machine API controller service account by running the following command:

   ```
   $ gcloud projects get-iam-policy <project_name> \
     --flatten='bindings[].members' \
     --format='table(bindings.role)' \
     --filter="bindings.members:<machine_api_controller_service_account>"
   ```

   where `<machine_api_controller_service_account>` is the Machine API controller service account.
4. List the custom role permissions for the Machine API controller service account by running the following command:

   ```
   $ gcloud iam roles describe <machine_api_role> \
     --project <project_name>
   ```

   where `<machine_api_role>` is the role ID of the custom role for the Machine API controller service account.

   **Example output**

   ```
   etag: <etag_value>
   includedPermissions:
   - compute.acceleratorTypes.get
   - compute.acceleratorTypes.list
   - compute.disks.create
   - compute.disks.createTagBinding
   ...
   - compute.zones.get
   - compute.zones.list
   - iam.serviceAccounts.actAs
   - iam.serviceAccounts.get
   - iam.serviceAccounts.list
   - resourcemanager.tagValues.get
   - resourcemanager.tagValues.list
   - serviceusage.quotas.get
   - serviceusage.services.get
   - serviceusage.services.list
   name: projects/<project_name>/roles/<machine_api_role>
   stage: GA
   title: <project_name>-openshift-machine-api-gcp
   ```

   where `<project_name>` is the Google Cloud project name specified in the `install-config.yaml` file.

   Note

   This truncated example output might not match the permissions list for your cluster.
5. Create a custom role that includes all of the permissions from your output except for the `iam.serviceAccounts.actAs` permission by running a command similar to the following:

   ```
   $ gcloud iam roles create <machine_api_role>_without_actas \
   --project=<project_name> \
   --title=<machine_api_role>_without_actas \
   --description="Required permissions for the Machine API controller without the iam.serviceAccounts.actAs permission" \
   --permissions=compute.acceleratorTypes.get,\
   compute.acceleratorTypes.list,\
   compute.disks.create,\
   compute.disks.createTagBinding,\
   ...
   compute.zones.get,\
   compute.zones.list,\
   iam.serviceAccounts.get,\
   iam.serviceAccounts.list,\
   resourcemanager.tagValues.get,\
   resourcemanager.tagValues.list,\
   serviceusage.quotas.get,\
   serviceusage.services.get,\
   serviceusage.services.list
   ```

   In this example, the new role name is the original custom role name, `<machine_api_role>`, with a `_without_actas` string added to the end.

   Important

   This truncated example command might not match the permissions list for your cluster. You must use the list of permissions from the output of the `gcloud iam roles describe <machine_api_role> --project <project_name>` command on your cluster.
6. Remove the custom role that includes the `iam.serviceAccounts.actAs` permission from the Machine API controller service account by running the following command:

   ```
   $ gcloud projects remove-iam-policy-binding <project_name> \
     --member "serviceAccount:<machine_api_controller_service_account>" \
     --role "projects/<project_name>/roles/<machine_api_role>"
   ```

   where `<machine_api_role>` is the original custom role.
7. Grant the custom role that excludes the `iam.serviceAccounts.actAs` permission to the Machine API controller service account by running the following command:

   ```
   $ gcloud projects add-iam-policy-binding <project_name> \
     --member "serviceAccount:<machine_api_controller_service_account>" \
     --role "projects/<project_name>/roles/<machine_api_role>_without_actas
   ```

   where `<machine_api_role>_without_actas` is the new custom role.
8. Optional: To verify that the Machine API controller service account has the correct role, check the attached role ID by running the following command:

   ```
   $ gcloud projects get-iam-policy <project_name> \
     --flatten='bindings[].members' \
     --format='table(bindings.role)' \
     --filter="bindings.members:<machine_api_controller_service_account>"
   ```

   **Example output**

   ```
   ROLE
   projects/<project_name>/roles/<machine_api_role>_without_actas
   ```
9. Grant the Machine API controller service account the Service Account User role on the service account of the compute nodes by running the following command:

   ```
   $ gcloud iam service-accounts add-iam-policy-binding <compute_nodes_service_account> \
     --member="serviceAccount:<machine_api_controller_service_account>" \
     --role=roles/iam.serviceAccountUser
   ```

   where `<compute_nodes_service_account>` is the service account for your compute nodes. This value is the `compute[0].platform.gcp.serviceAccount` parameter in your `install-config.yaml` file.

##### [8.11.2.4. Incorporating the Cloud Credential Operator utility manifests](#cco-ccoctl-install-creating-manifests_installing-gcp-private) Copy linkLink copied to clipboard!

To implement short-term security credentials managed outside the cluster for individual components, you must move the manifest files that the Cloud Credential Operator utility (`ccoctl`) created to the correct directories for the installation program.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have configured the Cloud Credential Operator utility (`ccoctl`).
* You have created the cloud provider resources that are required for your cluster with the `ccoctl` utility.

**Procedure**

1. Add the following granular permissions to the Google Cloud account that the installation program uses:

   * compute.machineTypes.list
   * compute.regions.list
   * compute.zones.list
   * dns.changes.create
   * dns.changes.get
   * dns.managedZones.create
   * dns.managedZones.delete
   * dns.managedZones.get
   * dns.managedZones.list
   * dns.networks.bindPrivateDNSZone
   * dns.resourceRecordSets.create
   * dns.resourceRecordSets.delete
   * dns.resourceRecordSets.list
2. If you did not set the `credentialsMode` parameter in the `install-config.yaml` configuration file to `Manual`, modify the value as shown:

   **Sample configuration file snippet**

   ```
   apiVersion: v1
   baseDomain: example.com
   credentialsMode: Manual
   # ...
   ```
3. If you have not previously created installation manifest files, do so by running the following command:

   ```
   $ openshift-install create manifests --dir <installation_directory>
   ```

   where `<installation_directory>` is the directory in which the installation program creates files.
4. Copy the manifests that the `ccoctl` utility generated to the `manifests` directory that the installation program created by running the following command:

   ```
   $ cp /<path_to_ccoctl_output_dir>/manifests/* ./manifests/
   ```
5. Copy the `tls` directory that contains the private key to the installation directory:

   ```
   $ cp -a /<path_to_ccoctl_output_dir>/tls .
   ```

### [8.12. Deploying the cluster](#installation-launching-installer_installing-gcp-private) Copy linkLink copied to clipboard!

To deploy your OpenShift Container Platform cluster, you can initialize installation by running the `openshift-install create cluster` command from the directory that contains the installation program. The installation program provisions infrastructure and completes cluster setup.

Important

You can run the `create cluster` command of the installation program only once, during initial installation.

**Prerequisites**

* You have configured an account with the cloud platform that hosts your cluster.
* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* You have verified that the cloud provider account on your host has the correct permissions to deploy the cluster. An account with incorrect permissions causes the installation process to fail with an error message that displays the missing permissions.

**Procedure**

1. Remove any existing Google Cloud credentials that do not use the service account key for the Google Cloud account that you configured for your cluster and that are stored in the following locations:

   * The `GOOGLE_CREDENTIALS`, `GOOGLE_CLOUD_KEYFILE_JSON`, or `GCLOUD_KEYFILE_JSON` environment variables
   * The `~/.gcp/osServiceAccount.json` file
   * The `gcloud cli` default credentials
2. In the directory that contains the installation program, initialize the cluster deployment by running the following command:

   ```
   $ ./openshift-install create cluster --dir <installation_directory> \
       --log-level=info
   ```

   * For `<installation_directory>`, specify the location of your customized `./install-config.yaml` file.
   * To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.
3. Optional: You can reduce the number of permissions for the service account that you used to install the cluster.

   * If you assigned the `Owner` role to your service account, you can remove that role and replace it with the `Viewer` role.
   * If you included the `Service Account Key Admin` role, you can remove it.

**Verification**

When the cluster deployment completes successfully:

* The terminal displays directions for accessing your cluster, including a link to the web console and credentials for the `kubeadmin` user.
* Credential information also outputs to `<installation_directory>/.openshift_install.log`.

  Important

  Do not delete the installation program or the files that the installation program creates. Both are required to delete the cluster.

  **Example output**

  ```
  ...
  INFO Install complete!
  INFO To access the cluster as the system:admin user when using 'oc', run 'export KUBECONFIG=/home/myuser/install_dir/auth/kubeconfig'
  INFO Access the OpenShift web-console here: https://console-openshift-console.apps.mycluster.example.com
  INFO Login to the console with user: "kubeadmin", and password: "password"
  INFO Time elapsed: 36m22s
  ```

  Important

  + The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
  + It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

### [8.13. Provisioning your own DNS records](#installation-gcp-provisioning-own-dns-records_installing-gcp-private) Copy linkLink copied to clipboard!

Use the IP address of the API server to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain. Use the IP address of the Ingress service to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

Important

Before you use this feature, you must add the `userProvisionedDNS` parameter to the `install-config.yaml` file and enable the parameter. For more information, see "Enabling a user-managed DNS".

**Prerequisites**

* You installed your cluster.
* You installed the `gcloud` CLI tool.

**Procedure**

1. Determine the infrastructure ID of your cluster by running the following command:

   ```
   $ infra_id=$(jq -r .infraID <installation_directory>/metadata.json)
   ```

   where:

   `<installation_directory>`
   :   Specifies the directory where you ran the installation program.
2. Find the IP address of the API server:

   1. If you installed a private cluster, determine the IP address of the API server by running the following command:

      ```
      $ gcloud compute forwarding-rules describe "${infra_id}-api-internal" --project=<project_name> --region <region_name> --format json | jq -r .IPAddress
      ```

      where:

      `<project_name>`
      :   Specifies the name of your Google Cloud project.

      `<region_name>`
      :   Specifies the region where you installed your cluster.
   2. If you installed a public cluster, determine the IP address of the API server by running the following command:

      ```
      $ gcloud compute forwarding-rules describe --global "${infra_id}-apiserver" --format json | jq -r .IPAddress
      ```
3. Use the IP address to provision your own DNS record with the `api.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.
4. Find the IP address of the Ingress service:

   1. If you installed a private cluster, find the IP address of the Ingress service by running the following command:

      ```
      $ gcloud compute forwarding-rules list --project=<project_name> --filter="subnetwork:(projects/<project_name>/regions/<region_name>/subnetworks/<compute_subnet_name>)" --format="json" | jq -r '.[].IPAddress'
      ```

      where:

      `<project_name>`
      :   Specifies the name of your Google Cloud project.

      `<region_name>`
      :   Specifies the region where you installed your cluster.

      `<compute_subnet_name>`
      :   Specifies the name of the subnet that contains your compute nodes.
   2. If you installed a public cluster, find the IP address by using the forwarding rule:

      1. Find the forwarding rule for the Ingress service by running the following command:

         ```
         $ ingress_forwarding_rule=$(gcloud compute target-pools list --format=json --filter="instances[]~${infra_id}" | jq -r .[].name)
         ```
      2. Use the forwarding rule value to find the IP address of the Ingress service by running the following command:

         ```
         $ gcloud compute forwarding-rules describe --region "<region_name>" "${ingress_forwarding_rule}" --format json | jq -r .IPAddress
         ```

         where:

         `<region_name>`
         :   Specifies the region where you installed your cluster.
5. Use the IP address to provision your own DNS record with the `*.apps.<cluster_name>.<base_domain>.` hostname by using your cluster name and base cluster domain.

### [8.14. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-gcp-private) Copy linkLink copied to clipboard!

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

### [8.15. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-gcp-private) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

### [8.16. Next steps](#next-steps-5) Copy linkLink copied to clipboard!

* [Customize your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations).
* If necessary, you can [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting).

## [Chapter 9. Installing a cluster on user-provisioned infrastructure in Google Cloud by using Infrastructure Manager templates](#installing-gcp-user-infra) Copy linkLink copied to clipboard!

In OpenShift Container Platform version 4.22, you can install a cluster on Google Cloud that uses infrastructure that you provide.

The steps for performing a user-provided infrastructure install are outlined here. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods.

Important

The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.

### [9.1. Prerequisites](#prerequisites-5) Copy linkLink copied to clipboard!

* You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes.
* You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing).
* If you use a firewall and plan to use the Telemetry service, you [configured the firewall to allow the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires access to.
* If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, you can [manually create and maintain long-term credentials](#manually-create-iam_installing-gcp-customizations "4.10.1. Manually creating long-term credentials").

  Note

  Be sure to also review this site list if you are configuring a proxy.

### [9.2. Certificate signing requests management](#csr-management_installing-gcp-user-infra) Copy linkLink copied to clipboard!

On user-provisioned infrastructure, you must implement a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that kubelet credentials request because it cannot confirm that the correct machine issued the request. You must find and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

### [9.3. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-gcp-user-infra) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [9.4. Configuring your Google Cloud project](#installation-gcp-user-infra-config-project) Copy linkLink copied to clipboard!

Before you can install OpenShift Container Platform, you must configure a Google Cloud project to host it.

#### [9.4.1. Creating a Google Cloud project](#installation-gcp-project_installing-gcp-user-infra) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, you must create a project in your Google Cloud account to host the cluster.

**Procedure**

* Create a project to host your OpenShift Container Platform cluster. See [Creating and Managing Projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in the Google Cloud documentation.

  Important

  Your Google Cloud project must use the Premium Network Service Tier if you are using installer-provisioned infrastructure. The Standard Network Service Tier is not supported for clusters installed using the installation program. The installation program configures internal load balancing for the `api-int.<cluster_name>.<base_domain>` URL; the Premium Tier is required for internal load balancing.

#### [9.4.2. Enabling API services in Google Cloud](#installation-gcp-enabling-api-services_installing-gcp-user-infra) Copy linkLink copied to clipboard!

Your Google Cloud project requires access to several API services to complete OpenShift Container Platform installation.

**Prerequisites**

* You created a project to host your cluster.

**Procedure**

* Enable the following required API services in the project that hosts your cluster. You may also enable optional API services which are not required for installation. See [Enabling services](https://cloud.google.com/service-usage/docs/enable-disable#enabling) in the Google Cloud documentation.

  Expand

  Table 9.1. Required API services

  | API service | Console service name |
  | --- | --- |
  | Compute Engine API | `compute.googleapis.com` |
  | Cloud Resource Manager API | `cloudresourcemanager.googleapis.com` |
  | Cloud DNS API | `dns.googleapis.com` |
  | IAM Service Account Credentials API | `iamcredentials.googleapis.com` |
  | Identity and Access Management (IAM) API | `iam.googleapis.com` |
  | Service Usage API | `serviceusage.googleapis.com` |

  Show more

  Expand

  Table 9.2. Optional API services

  | API service | Console service name |
  | --- | --- |
  | Cloud Deployment Manager V2 API | `deploymentmanager.googleapis.com` |
  | Google Cloud APIs | `cloudapis.googleapis.com` |
  | Service Management API | `servicemanagement.googleapis.com` |
  | Google Cloud Storage JSON API | `storage-api.googleapis.com` |
  | Cloud Storage | `storage-component.googleapis.com` |

  Show more

#### [9.4.3. Configuring DNS for Google Cloud](#installation-gcp-dns_installing-gcp-user-infra) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, the Google Cloud account you use must have a dedicated public hosted zone in the same project that you host the OpenShift Container Platform cluster. This zone must be authoritative for the domain. The DNS service provides cluster DNS resolution and name lookup for external connections to the cluster.

**Procedure**

1. Identify your domain, or subdomain, and registrar. You can transfer an existing domain and registrar or obtain a new one through Google Cloud or another source.

   Note

   If you purchase a new domain, it can take time for the relevant DNS changes to propagate. For more information about purchasing domains through Google, see [Google Domains](https://domains.google/).
2. Create a public hosted zone for your domain or subdomain in your Google Cloud project. See [Creating public zones](https://cloud.google.com/dns/zones/#creating_public_zones) in the Google Cloud documentation.

   Use an appropriate root domain, such as `openshiftcorp.com`, or subdomain, such as `clusters.openshiftcorp.com`.
3. Extract the new authoritative name servers from the hosted zone records. See [Look up your Cloud DNS name servers](https://cloud.google.com/dns/docs/update-name-servers#look_up_your_name_servers) in the Google Cloud documentation.

   You typically have four name servers.
4. Update the registrar records for the name servers that your domain uses. For example, if you registered your domain to Google Domains, see the following topic in the Google Domains Help: [How to switch to custom name servers](https://support.google.com/domains/answer/3290309?hl=en).
5. If you migrated your root domain to Google Cloud DNS, migrate your DNS records. See [Migrating to Cloud DNS](https://cloud.google.com/dns/docs/migrating) in the Google Cloud documentation.
6. If you use a subdomain, follow your company’s procedures to add its delegation records to the parent domain. This process might include a request to your company’s IT department or the division that controls the root domain and DNS services for your company.

#### [9.4.4. Google Cloud account limits](#installation-gcp-limits_installing-gcp-user-infra) Copy linkLink copied to clipboard!

The OpenShift Container Platform cluster uses a number of Google Cloud components, but the default [Quotas](https://cloud.google.com/docs/quota) do not affect your ability to install a default OpenShift Container Platform cluster.

A default cluster, which contains three compute and three control plane machines, uses the following resources. Note that some resources are required only during the bootstrap process and are removed after the cluster deploys.

Expand

Table 9.3. Google Cloud resources used in a default cluster

| Service | Component | Location | Total resources required | Resources removed after bootstrap |
| --- | --- | --- | --- | --- |
| Service account | IAM | Global | 6 | 1 |
| Firewall rules | Networking | Global | 11 | 1 |
| Forwarding rules | Compute | Global | 2 | 0 |
| Health checks | Compute | Global | 2 | 0 |
| Images | Compute | Global | 1 | 0 |
| Networks | Networking | Global | 1 | 0 |
| Routers | Networking | Global | 1 | 0 |
| Routes | Networking | Global | 2 | 0 |
| Subnetworks | Compute | Global | 2 | 0 |
| Target pools | Networking | Global | 2 | 0 |

Show more

Note

If any of the quotas are insufficient during installation, the installation program displays an error that states both which quota was exceeded and the region.

Be sure to consider your actual cluster size, planned cluster growth, and any usage from other clusters that are associated with your account. The CPU, static IP addresses, and persistent disk SSD (storage) quotas are the ones that are most likely to be insufficient.

If you plan to deploy your cluster in one of the following regions, you will exceed the maximum storage quota and are likely to exceed the CPU quota limit:

* `asia-east2`
* `asia-northeast2`
* `asia-south1`
* `australia-southeast1`
* `europe-north1`
* `europe-west2`
* `europe-west3`
* `europe-west6`
* `northamerica-northeast1`
* `southamerica-east1`
* `us-west2`

You can increase resource quotas from the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas), but you might need to file a support ticket. Be sure to plan your cluster size early so that you can allow time to resolve the support ticket before you install your OpenShift Container Platform cluster.

#### [9.4.5. Creating a service account in Google Cloud](#installation-gcp-service-account_installing-gcp-user-infra) Copy linkLink copied to clipboard!

OpenShift Container Platform requires a Google Cloud service account that provides authentication and authorization to access data in the Google APIs. If you do not have an existing IAM service account that contains the required roles in your project, you must create one.

Note

To reduce the scope of permissions granted to the main service account in your Google Cloud project while still being able to use the Google Cloud Container Storage Interface (CSI) Driver Operator, you can transfer the control of permissions from the project-wide service account to the control plane and compute node service accounts instead, thus reducing the scope of the permission. For more information, see Section *Reducing permissions while using the Google Cloud CSI Driver Operator*.

**Prerequisites**

* You created a project to host your cluster.

**Procedure**

1. Create a service account in the project that you use to host your OpenShift Container Platform cluster. See [Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account) in the Google Cloud documentation.
2. Grant the service account the appropriate permissions. You can either grant the individual permissions that follow or assign the `Owner` role to it. See [Granting roles to a service account for specific resources](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource).

   Note

   While making the service account an owner of the project is the easiest way to gain the required permissions, it means that service account has complete control over the project. You must determine if the risk that comes from offering that power is acceptable.
3. You can create the service account key in JSON format, or attach the service account to a Google Cloud virtual machine. See [Creating service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and [Creating and enabling service accounts for instances](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances) in the Google Cloud documentation.

   Note

   If you use a virtual machine with an attached service account to create your cluster, you must set `credentialsMode: Manual` in the `install-config.yaml` file before installation.

#### [9.4.6. Required Google Cloud roles](#installation-gcp-permissions_installing-gcp-user-infra) Copy linkLink copied to clipboard!

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform. If your organization’s security policies require a more restrictive set of permissions, you can create a service account with the following permissions. If you deploy your cluster into an existing virtual private cloud (VPC), the service account does not require certain networking permissions, which are noted in the following lists:

**Required roles for the installation program**

* Compute Admin
* Role Administrator
* Security Admin
* Service Account Admin
* Service Account Key Admin
* Service Account User
* Storage Admin

**Required roles for creating network resources during installation**

* DNS Administrator

**Required roles for using the Cloud Credential Operator in passthrough mode**

* Compute Load Balancer Admin
* Tag User

**Required roles for user-provisioned Google Cloud infrastructure**

* Cloud Infrastructure Manager Admin

The following roles are applied to the service accounts that the control plane and compute machines use:

Expand

Table 9.4. Google Cloud service account roles

| Account | Roles |
| --- | --- |
| Control Plane | `roles/compute.instanceAdmin` |
| `roles/compute.networkAdmin` |
| `roles/compute.securityAdmin` |
| `roles/storage.admin` |
| `roles/iam.serviceAccountUser` |
| Compute | `roles/compute.viewer` |
| `roles/storage.admin` |
| `roles/artifactregistry.reader` |

Show more

#### [9.4.7. Required Google Cloud permissions for user-provisioned infrastructure](#minimum-required-permissions-upi-gcp_installing-gcp-user-infra) Copy linkLink copied to clipboard!

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform.

If your organization’s security policies require a more restrictive set of permissions, you can create [custom roles](https://cloud.google.com/iam/docs/creating-custom-roles) with the necessary permissions. The following permissions are required for the user-provisioned infrastructure for creating and deleting the OpenShift Container Platform cluster.

**Example 9.1. Required permissions for creating network resources**

* `compute.addresses.create`
* `compute.addresses.createInternal`
* `compute.addresses.delete`
* `compute.addresses.get`
* `compute.addresses.list`
* `compute.addresses.use`
* `compute.addresses.useInternal`
* `compute.firewalls.create`
* `compute.firewalls.delete`
* `compute.firewalls.get`
* `compute.firewalls.list`
* `compute.forwardingRules.create`
* `compute.forwardingRules.get`
* `compute.forwardingRules.list`
* `compute.forwardingRules.setLabels`
* `compute.globalAddresses.create`
* `compute.globalAddresses.get`
* `compute.globalAddresses.use`
* `compute.globalForwardingRules.create`
* `compute.globalForwardingRules.get`
* `compute.globalForwardingRules.setLabels`
* `compute.networks.create`
* `compute.networks.get`
* `compute.networks.list`
* `compute.networks.updatePolicy`
* `compute.networks.use`
* `compute.routers.create`
* `compute.routers.get`
* `compute.routers.list`
* `compute.routers.update`
* `compute.routes.list`
* `compute.subnetworks.create`
* `compute.subnetworks.get`
* `compute.subnetworks.list`
* `compute.subnetworks.use`
* `compute.subnetworks.useExternalIp`

**Example 9.2. Required permissions for creating load balancer resources**

* `compute.backendServices.create`
* `compute.backendServices.get`
* `compute.backendServices.list`
* `compute.backendServices.update`
* `compute.backendServices.use`
* `compute.regionBackendServices.create`
* `compute.regionBackendServices.get`
* `compute.regionBackendServices.list`
* `compute.regionBackendServices.update`
* `compute.regionBackendServices.use`
* `compute.targetPools.addInstance`
* `compute.targetPools.create`
* `compute.targetPools.get`
* `compute.targetPools.list`
* `compute.targetPools.removeInstance`
* `compute.targetPools.use`
* `compute.targetTcpProxies.create`
* `compute.targetTcpProxies.get`
* `compute.targetTcpProxies.use`

**Example 9.3. Required permissions for creating DNS resources**

* `dns.changes.create`
* `dns.changes.get`
* `dns.managedZones.create`
* `dns.managedZones.get`
* `dns.managedZones.list`
* `dns.networks.bindPrivateDNSZone`
* `dns.resourceRecordSets.create`
* `dns.resourceRecordSets.list`
* `dns.resourceRecordSets.update`

**Example 9.4. Required permissions for creating Service Account resources**

* `iam.serviceAccountKeys.create`
* `iam.serviceAccountKeys.delete`
* `iam.serviceAccountKeys.get`
* `iam.serviceAccountKeys.list`
* `iam.serviceAccounts.actAs`
* `iam.serviceAccounts.create`
* `iam.serviceAccounts.delete`
* `iam.serviceAccounts.get`
* `iam.serviceAccounts.list`
* `resourcemanager.projects.get`
* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`

**Example 9.5. Required permissions for creating compute resources**

* `compute.disks.create`
* `compute.disks.get`
* `compute.disks.list`
* `compute.instanceGroups.create`
* `compute.instanceGroups.delete`
* `compute.instanceGroups.get`
* `compute.instanceGroups.list`
* `compute.instanceGroups.update`
* `compute.instanceGroups.use`
* `compute.instances.create`
* `compute.instances.delete`
* `compute.instances.get`
* `compute.instances.list`
* `compute.instances.setLabels`
* `compute.instances.setMetadata`
* `compute.instances.setServiceAccount`
* `compute.instances.setTags`
* `compute.instances.use`
* `compute.machineTypes.get`
* `compute.machineTypes.list`

**Example 9.6. Required for creating storage resources**

* `storage.buckets.create`
* `storage.buckets.delete`
* `storage.buckets.get`
* `storage.buckets.list`
* `storage.objects.create`
* `storage.objects.delete`
* `storage.objects.get`
* `storage.objects.list`

**Example 9.7. Required permissions for creating health check resources**

* `compute.healthChecks.create`
* `compute.healthChecks.get`
* `compute.healthChecks.list`
* `compute.healthChecks.useReadOnly`
* `compute.httpHealthChecks.create`
* `compute.httpHealthChecks.get`
* `compute.httpHealthChecks.list`
* `compute.httpHealthChecks.useReadOnly`
* `compute.regionHealthChecks.create`
* `compute.regionHealthChecks.get`
* `compute.regionHealthChecks.useReadOnly`

**Example 9.8. Required permissions to get Google Cloud zone and region related information**

* `compute.globalOperations.get`
* `compute.regionOperations.get`
* `compute.regions.get`
* `compute.regions.list`
* `compute.zoneOperations.get`
* `compute.zones.get`
* `compute.zones.list`

**Example 9.9. Required permissions for checking services and quotas**

* `monitoring.timeSeries.list`
* `serviceusage.quotas.get`
* `serviceusage.services.list`

**Example 9.10. Required IAM permissions for installation**

* `iam.roles.get`

**Example 9.11. Required permissions when authenticating without a service account key**

* `iam.serviceAccounts.signBlob`

**Example 9.12. Required permissions when providing Key Management Service (KMS) key rings**

* `cloudkms.keyRings.list`

**Example 9.13. Required Images permissions for installation**

* `compute.images.create`
* `compute.images.delete`
* `compute.images.get`
* `compute.images.list`

**Example 9.14. Optional permission for running gather bootstrap**

* `compute.instances.getSerialPortOutput`

**Example 9.15. Required permissions for deleting network resources**

* `compute.addresses.delete`
* `compute.addresses.deleteInternal`
* `compute.addresses.list`
* `compute.addresses.setLabels`
* `compute.firewalls.delete`
* `compute.firewalls.list`
* `compute.forwardingRules.delete`
* `compute.forwardingRules.list`
* `compute.globalAddresses.delete`
* `compute.globalAddresses.list`
* `compute.globalForwardingRules.delete`
* `compute.globalForwardingRules.list`
* `compute.networks.delete`
* `compute.networks.list`
* `compute.networks.updatePolicy`
* `compute.routers.delete`
* `compute.routers.list`
* `compute.routes.list`
* `compute.subnetworks.delete`
* `compute.subnetworks.list`

**Example 9.16. Required permissions for deleting load balancer resources**

* `compute.backendServices.delete`
* `compute.backendServices.list`
* `compute.regionBackendServices.delete`
* `compute.regionBackendServices.list`
* `compute.targetPools.delete`
* `compute.targetPools.list`
* `compute.targetTcpProxies.delete`
* `compute.targetTcpProxies.list`

**Example 9.17. Required permissions for deleting DNS resources**

* `dns.changes.create`
* `dns.managedZones.delete`
* `dns.managedZones.get`
* `dns.managedZones.list`
* `dns.resourceRecordSets.delete`
* `dns.resourceRecordSets.list`

**Example 9.18. Required permissions for deleting Service Account resources**

* `iam.serviceAccounts.delete`
* `iam.serviceAccounts.get`
* `iam.serviceAccounts.list`
* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`

**Example 9.19. Required permissions for deleting compute resources**

* `compute.disks.delete`
* `compute.disks.list`
* `compute.instanceGroups.delete`
* `compute.instanceGroups.list`
* `compute.instances.delete`
* `compute.instances.list`
* `compute.instances.stop`
* `compute.machineTypes.list`

**Example 9.20. Required for deleting storage resources**

* `storage.buckets.delete`
* `storage.buckets.getIamPolicy`
* `storage.buckets.list`
* `storage.objects.delete`
* `storage.objects.list`

**Example 9.21. Required permissions for deleting health check resources**

* `compute.healthChecks.delete`
* `compute.healthChecks.list`
* `compute.httpHealthChecks.delete`
* `compute.httpHealthChecks.list`
* `compute.regionHealthChecks.delete`
* `compute.regionHealthChecks.list`

**Example 9.22. Required Images permissions for deletion**

* `compute.images.delete`
* `compute.images.list`

**Example 9.23. Required permissions to get Region related information**

* `compute.regions.get`

**Example 9.24. Required Deployment Manager permissions**

* config.deployments.create
* config.deployments.delete
* config.deployments.get
* config.deployments.list
* config.operations.get
* config.resources.list
* cloudbuild.builds.create
* cloudbuild.builds.get

#### [9.4.8. Supported Google Cloud regions](#installation-gcp-regions_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can deploy an OpenShift Container Platform cluster to the following Google Cloud regions:

* `africa-south1` (Johannesburg, South Africa)
* `asia-east1` (Changhua County, Taiwan)
* `asia-east2` (Hong Kong)
* `asia-northeast1` (Tokyo, Japan)
* `asia-northeast2` (Osaka, Japan)
* `asia-northeast3` (Seoul, South Korea)
* `asia-south1` (Mumbai, India)
* `asia-south2` (Delhi, India)
* `asia-southeast1` (Jurong West, Singapore)
* `asia-southeast2` (Jakarta, Indonesia)
* `australia-southeast1` (Sydney, Australia)
* `australia-southeast2` (Melbourne, Australia)
* `europe-central2` (Warsaw, Poland)
* `europe-north1` (Hamina, Finland)
* `europe-southwest1` (Madrid, Spain)
* `europe-west1` (St. Ghislain, Belgium)
* `europe-west2` (London, England, UK)
* `europe-west3` (Frankfurt, Germany)
* `europe-west4` (Eemshaven, Netherlands)
* `europe-west6` (Zürich, Switzerland)
* `europe-west8` (Milan, Italy)
* `europe-west9` (Paris, France)
* `europe-west12` (Turin, Italy)
* `me-central1` (Doha, Qatar, Middle East)
* `me-central2` (Dammam, Saudi Arabia, Middle East)
* `me-west1` (Tel Aviv, Israel)
* `northamerica-northeast1` (Montréal, Québec, Canada)
* `northamerica-northeast2` (Toronto, Ontario, Canada)
* `southamerica-east1` (São Paulo, Brazil)
* `southamerica-west1` (Santiago, Chile)
* `us-central1` (Council Bluffs, Iowa, USA)
* `us-east1` (Moncks Corner, South Carolina, USA)
* `us-east4` (Ashburn, Northern Virginia, USA)
* `us-east5` (Columbus, Ohio)
* `us-south1` (Dallas, Texas)
* `us-west1` (The Dalles, Oregon, USA)
* `us-west2` (Los Angeles, California, USA)
* `us-west3` (Salt Lake City, Utah, USA)
* `us-west4` (Las Vegas, Nevada, USA)

Note

To determine which machine type instances are available by region and zone, see the Google [documentation](https://cloud.google.com/compute/docs/regions-zones#available).

#### [9.4.9. Installing and configuring CLI tools for Google Cloud](#installation-gcp-install-cli_installing-gcp-user-infra) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on Google Cloud using user-provisioned infrastructure, you must install and configure the CLI tools for Google Cloud.

**Prerequisites**

* You created a project to host your cluster.
* You created a service account and granted it the required permissions.

**Procedure**

1. Install the following binaries in `$PATH`:

   * `gcloud`
   * `gsutil`

   See [Install the latest Cloud SDK version](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version) in the Google Cloud documentation.
2. Authenticate using the `gcloud` tool with your configured service account.

   See [Authorizing with a service account](https://cloud.google.com/sdk/docs/authorizing#authorizing_with_a_service_account) in the Google Cloud documentation.

### [9.5. Requirements for a cluster with user-provisioned infrastructure](#installation-requirements-user-infra_installing-gcp-user-infra) Copy linkLink copied to clipboard!

For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

This section describes the requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

#### [9.5.1. Required machines for cluster installation](#installation-machine-requirements_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

Important

For a cluster that has user-provisioned infrastructure, you must deploy all of the required machines.

Expand

Table 9.5. Minimum required hosts

| Hosts | Description |
| --- | --- |
| One temporary bootstrap machine | The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster. |
| Three control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| At least two compute machines, which are also known as worker machines. | The workloads requested by OpenShift Container Platform users run on the compute machines. |

Show more

Important

To keep high availability of your cluster, use separate physical hosts for these cluster machines.

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. However, the compute machines can use Red Hat Enterprise Linux CoreOS (RHCOS), Red Hat Enterprise Linux (RHEL) 8.6 and later.

RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.8 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits).

#### [9.5.2. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-gcp-user-infra) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 9.6. Minimum resource requirements

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Show more

* One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
* OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance.
* As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines.

Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* ppc64le architecture requires IBM® Power9 ISA
* s390x architecture requires IBM® z14 ISA

For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

#### [9.5.3. Tested instance types for Google Cloud](#installation-gcp-tested-machine-types_installing-gcp-user-infra) Copy linkLink copied to clipboard!

The following Google Cloud instance types have been tested with OpenShift Container Platform.

Note

Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) (Google documentation).

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see [machine series support for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in *Storage*.

See the following machine series:

* `A2`
* `A3`
* `C2`
* `C2D`
* `C3`
* `C3D`
* `C4`
* `E2`
* `M1`
* `N1`
* `N2`
* `N2D`
* `N4`
* `Tau T2D`

#### [9.5.4. Tested instance types for Google Cloud on 64-bit ARM infrastructures](#installation-gcp-tested-machine-types-arm_installing-gcp-user-infra) Copy linkLink copied to clipboard!

The following Google Cloud 64-bit ARM instance types have been tested with OpenShift Container Platform.

See the following machine series for 64-bit ARM machines:

* `C4A`
* `N4A`
* `Tau T2A`

#### [9.5.5. Using custom machine types](#installation-custom-machine-types_installing-gcp-user-infra) Copy linkLink copied to clipboard!

Using a custom machine type to install a OpenShift Container Platform cluster is supported.

Consider the following when using a custom machine type:

* Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation".
* The name of the custom machine type must adhere to the following syntax:

  `custom-<number_of_cpus>-<amount_of_memory_in_mb>`

  For example, `custom-6-20480`.

### [9.6. Creating the installation files for Google Cloud](#installation-user-infra-generate_installing-gcp-user-infra) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on Google Cloud by using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use.

You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.

#### [9.6.1. Optional: Creating a separate /var partition](#installation-disk-partitioning-upi-templates_installing-gcp-user-infra) Copy linkLink copied to clipboard!

To isolate growing storage for containers, etcd, or logs, you can optionally create a separate `/var` partition on worker nodes before you generate Ignition configs.

It is recommended that disk partitioning for OpenShift Container Platform be left to the installation program. However, there are cases where you might want to create separate partitions in a part of the filesystem that you expect to grow.

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` partition or a subdirectory of `/var`. For example:

* `/var/lib/containers`: Holds container-related content that can grow as more images and containers are added to a system.
* `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage.
* `/var`: Holds data that you might want to keep separate for purposes such as auditing.

Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date and keep that data intact. With this method, you will not have to pull all your containers again, nor will you have to copy massive log files when you update systems.

Because `/var` must be in place before a fresh installation of Red Hat Enterprise Linux CoreOS (RHCOS), the following procedure sets up the separate `/var` partition by creating a machine config manifest that is inserted during the `openshift-install` preparation phases of an OpenShift Container Platform installation.

Important

If you follow the steps to create a separate `/var` partition in this procedure, it is not necessary to create the Kubernetes manifest and Ignition config files again as described later in this section.

**Procedure**

1. Create a directory to hold the OpenShift Container Platform installation files:

   ```
   $ mkdir $HOME/clusterconfig
   ```
2. Run `openshift-install` to create a set of files in the `manifest` and `openshift` subdirectories. Answer the system questions as you are prompted:

   ```
   $ openshift-install create manifests --dir $HOME/clusterconfig
   ```

   **Example output**

   ```
   ? SSH Public Key ...
   INFO Credentials loaded from the "myprofile" profile in file "/home/myuser/.aws/credentials"
   INFO Consuming Install Config from target directory
   INFO Manifests created in: $HOME/clusterconfig/manifests and $HOME/clusterconfig/openshift
   ```
3. Optional: Confirm that the installation program created manifests in the `clusterconfig/openshift` directory:

   ```
   $ ls $HOME/clusterconfig/openshift/
   ```

   **Example output**

   ```
   99_kubeadmin-password-secret.yaml
   99_openshift-cluster-api_master-machines-0.yaml
   99_openshift-cluster-api_master-machines-1.yaml
   99_openshift-cluster-api_master-machines-2.yaml
   ...
   ```
4. Create a Butane config that configures the additional partition. For example, name the file `$HOME/clusterconfig/98-var-partition.bu`, change the disk device name to the name of the storage device on the `worker` systems, and set the storage size as appropriate. This example places the `/var` directory on a separate partition:

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
   :   Specifies the `start_mib` parameter. When adding a data partition to the boot disk, a minimum value of 25000 MiB (Mebibytes) is recommended. The root file system is automatically resized to fill all available space up to the specified offset. If no value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of RHCOS might overwrite the beginning of the data partition.

   `<partition_size>`
   :   Specifies the size of the data partition in mebibytes.

   `storage.filesystems.mount_options`
   :   The `prjquota` mount option must be enabled for filesystems used for container storage.

       Note

       When creating a separate `/var` partition, you cannot use different instance types for worker nodes, if the different instance types do not have the same device name.
5. Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command:

   ```
   $ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
   ```
6. Run `openshift-install` again to create Ignition configs from a set of files in the `manifest` and `openshift` subdirectories:

   ```
   $ openshift-install create ignition-configs --dir $HOME/clusterconfig
   ```

   ```
   $ ls $HOME/clusterconfig/
   auth  bootstrap.ign  master.ign  metadata.json  worker.ign
   ```

   You can now use the Ignition config files as input to the installation procedures to install Red Hat Enterprise Linux CoreOS (RHCOS) systems.

#### [9.6.2. Creating the installation configuration file](#installation-initializing_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can customize the OpenShift Container Platform cluster you install on Google Cloud.

**Prerequisites**

* You have the OpenShift Container Platform installation program and the pull secret for your cluster.
* Configure a Google Cloud account.

**Procedure**

1. Create the `install-config.yaml` file.

   1. Change to the directory that contains the installation program and run the following command:

      ```
      $ ./openshift-install create install-config --dir <installation_directory>
      ```

      * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

        When specifying the directory:
      * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
      * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
   2. At the prompts, provide the configuration details for your cloud:

      1. Optional: Select an SSH key to use to access your cluster machines.

         Note

         For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
      2. Select **gcp** as the platform to target.
      3. If you have not configured the service account key for your Google Cloud account on your computer, you must obtain it from Google Cloud and paste the contents of the file or enter the absolute path to the file.
      4. Select the project ID to provision the cluster in. The default value is specified by the service account that you configured.
      5. Select the region to deploy the cluster to.
      6. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.
      7. Enter a descriptive name for your cluster.
2. Modify the `install-config.yaml` file. You can find more information about the available parameters in the "Installation configuration parameters" section.

   Note

   If you are installing a three-node cluster, be sure to set the `compute.replicas` parameter to `0`. This ensures that the cluster’s control planes are schedulable. For more information, see "Installing a three-node cluster on Google Cloud".
3. Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

   Important

   The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

#### [9.6.3. Enabling Shielded VMs](#installation-gcp-enabling-shielded-vms_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).

Note

Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use shielded VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            secureBoot: Enabled
     ```
  2. To use shielded VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            secureBoot: Enabled
     ```
  3. To use shielded VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            secureBoot: Enabled
     ```

#### [9.6.4. Enabling Confidential VMs](#installation-gcp-enabling-confidential-vms_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google’s documentation on [Confidential Computing](https://cloud.google.com/confidential-computing). You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

Note

Confidential VMs are currently not supported on 64-bit ARM architectures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use confidential VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
     ```

     1

     ```
            type: n2d-standard-8
     ```

     2

     ```
            onHostMaintenance: Terminate
     ```

     3

     [1](#CO17-1)
     :   Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional Google Cloud configuration parameters".

     [2](#CO17-2)
     :   Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see [Supported operating systems and machine types](https://cloud.google.com/compute/confidential-vm/docs/os-and-machine-type#machine-type).

     [3](#CO17-3)
     :   Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.
  2. To use confidential VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```
  3. To use confidential VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```

#### [9.6.5. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-gcp-user-infra) Copy linkLink copied to clipboard!

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

**Prerequisites**

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

#### [9.6.6. Creating the Kubernetes manifest and Ignition config files](#installation-user-infra-generate-k8s-manifest-ignition_installing-gcp-user-infra) Copy linkLink copied to clipboard!

Because you manually provision infrastructure, you must generate the Kubernetes manifest and Ignition config files that the cluster requires.

The installation program converts the installation configuration into Kubernetes manifests and then wraps them into Ignition configuration files. You use these Ignition files to configure the cluster machines.

Important

* The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which the system then renews. If you shut down the cluster before the system renews the certificates and you later restart the cluster after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
* Use Ignition config files within 12 hours after you generate them, because the 24-hour certificate rotates from 16 to 22 hours after you install the cluster. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

**Procedure**

1. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```

   where:

   `<installation_directory>`
   :   Specifies the installation directory that contains the `install-config.yaml` file you created.
2. Remove the Kubernetes manifest files that define the control plane machines:

   ```
   $ rm -f <installation_directory>/openshift/99_openshift-cluster-api_master-machines-*.yaml
   ```

   By removing these files, you prevent the cluster from automatically generating control plane machines.
3. Remove the Kubernetes manifest files that define the control plane machine set:

   ```
   $ rm -f <installation_directory>/openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
   ```
4. Optional: If you do not want the cluster to provision compute machines, remove the Kubernetes manifest files that define the worker machines:

   ```
   $ rm -f <installation_directory>/openshift/99_openshift-cluster-api_worker-machineset-*.yaml
   ```

   Important

   If you disabled the `MachineAPI` capability when installing a cluster on user-provisioned infrastructure, you must remove the Kubernetes manifest files that define the worker machines. Otherwise, your cluster fails to install.

   Because you create and manage the worker machines yourself, you do not need to initialize these machines.

   Warning

   If you are installing a three-node cluster, skip the following step to allow the control plane nodes to be schedulable.

   Important

   When you configure control plane nodes from the default unschedulable to schedulable, you require additional subscriptions because control plane nodes then become compute nodes.
5. Verify that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:

   1. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.
   2. Locate the `mastersSchedulable` parameter and verify that it is set to `false`.
   3. Save and exit the file.
6. Optional: If you do not want [the Ingress Operator](https://github.com/openshift/cluster-ingress-operator) to create DNS records on your behalf, remove the `privateZone` and `publicZone` sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file:

   ```
   apiVersion: config.openshift.io/v1
   kind: DNS
   metadata:
     creationTimestamp: null
     name: cluster
   spec:
     baseDomain: example.openshift.com
     privateZone:
       id: mycluster-100419-private-zone
     publicZone:
       id: example.openshift.com
   status: {}
   ```

   `spec.privateZone`: Remove this section completely.

   If you do so, you must add ingress DNS records manually in a later step.
7. To create the Ignition configuration files, run the following command from the directory that contains the installation program:

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

### [9.7. Exporting common variables](#installation-gcp-user-infra-exporting-common-variables) Copy linkLink copied to clipboard!

#### [9.7.1. Extracting the infrastructure name](#installation-extracting-infraid_installing-gcp-user-infra) Copy linkLink copied to clipboard!

To identify your cluster resources in Google Cloud, extract the unique infrastructure name from the Ignition config files.

The infrastructure name is also used to locate the appropriate Google Cloud resources during an OpenShift Container Platform installation. The provided Infrastructure Manager templates contain references to this infrastructure name, so you must extract it.

Warning

Do not run the `openshift-install create manifests` command again after creating any Google Cloud resources. Running the command again generates a new cluster identifier, which will cause errors in existing resources. If you need to regenerate the manifests because you modified the `install-config.yaml` file, delete any Google Cloud resources you created and recreate them with the new cluster identifier.

**Prerequisites**

* You installed the `jq` package.

**Procedure**

* To extract and view the infrastructure name from the Ignition config file metadata, run the following command:

  ```
  $ jq -r .infraID <installation_directory>/metadata.json
  ```

  where `<installation_directory>` is the path to the directory that you stored the installation files in.

  **Example output**

  ```
  openshift-vw9j6
  ```

  The output of this command is your cluster name and a random string.

#### [9.7.2. Exporting common variables for Infrastructure Manager templates](#installation-user-infra-exporting-common-variables_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must export a common set of variables that are used with the provided Infrastructure Manager templates used to assist in installing a cluster with user-provisioned infrastructure on Google Cloud.

Note

Specific Infrastructure Manager templates can also require additional exported variables, which are detailed in their related procedures.

**Procedure**

* Export the following common variables to be used by the provided Infrastructure Manager templates. For any command with `<installation_directory>`, specify the path to the directory that you stored the installation files in.

  + Export the `BASE_DOMAIN` variable by running the following command:

    ```
    $ export BASE_DOMAIN='<base_domain>'
    ```

    `<base_domain>`
    :   If you are installing a cluster into a shared VPC, specify the value for the host project.
  + Export the `BASE_DOMAIN_ZONE_NAME` variable by running the following command:

    ```
    $ export BASE_DOMAIN_ZONE_NAME='<base_domain_zone_name>'
    ```

    `<base_domain_zone_name>`
    :   Specifies the base domain zone name.
  + Export the `NETWORK_CIDR` variable by running the following command:

    ```
    $ export NETWORK_CIDR='<network_cidr>'
    ```

    `<network_cidr>`
    :   Specifies the network CIDR your cluster uses. For example, `10.0.0.0/16`.
  + Export the `MASTER_SUBNET_CIDR` variable by running the following command:

    ```
    $ export MASTER_SUBNET_CIDR='<master_subnet_cidr>'
    ```

    `<master_subnet_cidr>`
    :   Specifies the network CIDR that your cluster’s control plane uses. For example, `10.0.0.0/17`.
  + Export the `WORKER_SUBNET_CIDR` variable by running the following command:

    ```
    $ export WORKER_SUBNET_CIDR='<worker_subnet_cidr>'
    ```

    `<worker_subnet_cidr>`
    :   Specifies the network CIDR that your cluster’s compute machines use. For example, `10.0.128.0/17`.
  + Export the `KUBECONFIG` variable by running the following command:

    ```
    $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
    ```
  + Export the `CLUSTER_NAME` variable by running the following command:

    ```
    $ export CLUSTER_NAME=`jq -r .clusterName <installation_directory>/metadata.json`
    ```
  + Export the `INFRA_ID` variable by running the following command:

    ```
    $ export INFRA_ID=`jq -r .infraID <installation_directory>/metadata.json`
    ```
  + Export the `PROJECT_NAME` variable by running the following command:

    ```
    $ export PROJECT_NAME=`jq -r .gcp.projectID <installation_directory>/metadata.json`
    ```
  + If you are installing a cluster into a shared VPC, export the `HOST_PROJECT` variable by running the following command:

    ```
    $ export HOST_PROJECT=<host_project_name>
    ```

    `<host_project_name>` specifies the name of the host project that contains the shared VPC.
  + If you are installing a cluster into a shared VPC, export the `HOST_PROJECT_ACCOUNT` variable by running the following command:

    ```
    $ export HOST_PROJECT_ACCOUNT=<host_project_account>
    ```

    `<host_project_account>` specifies the name of an account that can access the host project that contains the shared VPC.
  + Export the `REGION` variable by running the following command:

    ```
    $ export REGION=`jq -r .gcp.region <installation_directory>/metadata.json`
    ```
  + Export the `ZONE_0` variable by running the following command:

    ```
    $ export ZONE_0=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[0]' | cut -d "/" -f9)
    ```
  + Export the `ZONE_1` variable by running the following command:

    ```
    $ export ZONE_1=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[1]' | cut -d "/" -f9)
    ```
  + Export the `ZONE_2` variable by running the following command:

    ```
    $ export ZONE_2=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[2]' | cut -d "/" -f9)
    ```
  + Export the `SERVICE_ACCOUNT_EMAIL` variable by running the following command:

    ```
    $ export SERVICE_ACCOUNT_EMAIL="<service_account_email>"
    ```

    `<service_account_email>`
    :   Specifies the email address of the service account you used for the installation.
  + Export the `INSTALL_SERVICE_ACCOUNT` variable by running the following command:

    ```
    $ export INSTALL_SERVICE_ACCOUNT="projects/${PROJECT_NAME}/serviceAccounts/${SERVICE_ACCOUNT_EMAIL}"
    ```
  + Export the `CLUSTER_DOMAIN` variable by running the following command:

    ```
    $ export CLUSTER_DOMAIN="${CLUSTER_NAME}.${BASE_DOMAIN}"
    ```

### [9.8. Creating a VPC in Google Cloud](#installation-creating-gcp-vpc_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must create a VPC in Google Cloud for your OpenShift Container Platform cluster to use. You can customize the VPC to meet your requirements. One way to create the VPC is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided Infrastructure Manager template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* You have defined the variables in the *Exporting common variables* section.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for the VPC** section of this topic and save it as `01_vpc.tf` in a directory called `01_vpc` on your computer. This template describes the VPC that your cluster requires.
2. Create a VPC by running the following command:

   ```
   $ gcloud infra-manager deployments apply <vpc_deployment_name> \
     --location=${REGION} \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},master_subnet_cidr=${MASTER_SUBNET_CIDR},worker_subnet_cidr=${WORKER_SUBNET_CIDR} \
     --project=${PROJECT_NAME} \
     --local-source=./01_vpc \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<vpc_deployment_name>` specifies the name of the VPC deployment you create.
3. Configure environment variables that will be used to create other cluster infrastructure.

   1. Configure the `CLUSTER_NETWORK` environment variable by running the following command:

      ```
      $ export CLUSTER_NETWORK=$(gcloud compute networks describe ${INFRA_ID}-network --format json | jq -r .selfLink)
      ```
   2. Configure the `CONTROL_SUBNET` environment variable by running the following command:

      ```
      $ export CONTROL_SUBNET=$(gcloud compute networks subnets describe ${INFRA_ID}-master-subnet --region=${REGION} --format json | jq -r .selfLink)
      ```
   3. Configure the `COMPUTE_SUBNET` environment variable by running the following command:

      ```
      $ export COMPUTE_SUBNET=$(gcloud compute networks subnets describe ${INFRA_ID}-worker-subnet --region=${REGION} --format json | jq -r .selfLink)
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [9.8.1. Infrastructure Manager template for the VPC](#installation-infrastructure-manager-vpc_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the VPC that you need for your OpenShift Container Platform cluster:

**Example 9.25. `01_vpc.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "master_subnet_cidr" {
  type        = string
  description = "CIDR for the control plane subnet."
}

variable "worker_subnet_cidr" {
  type        = string
  description = "CIDR for the compute subnet."
}

resource "google_compute_network" "cluster_network" {
  provider = google-beta

  name = "${var.infra_id}-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "master_subnet" {
  provider = google-beta

  name = "${var.infra_id}-master-subnet"
  ip_cidr_range = "${var.master_subnet_cidr}"
  region = "${var.region}"
  network = google_compute_network.cluster_network.self_link
}

resource "google_compute_subnetwork" "worker_subnet" {
  provider = google-beta

  name = "${var.infra_id}-worker-subnet"
  ip_cidr_range = "${var.worker_subnet_cidr}"
  region = "${var.region}"
  network = google_compute_network.cluster_network.self_link
}

#tfimport-terraform import google_compute_router._router  __project__//-router
resource "google_compute_router" "router" {
  provider = google-beta

  name = "${var.infra_id}-router"
  network = google_compute_network.cluster_network.self_link
  region = "${var.region}"
}
resource "google_compute_router_nat" "master_nat" {
  provider = google-beta

  name = "${var.infra_id}-nat-master"
  source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"
  nat_ip_allocate_option = "AUTO_ONLY"
  min_ports_per_vm = 7168
  subnetwork {
    name = google_compute_subnetwork.master_subnet.self_link
    source_ip_ranges_to_nat = ["ALL_IP_RANGES"]
  }

  router = google_compute_router.router.name
  region = "${var.region}"

  depends_on = [
    google_compute_router.router
  ]
}
resource "google_compute_router_nat" "worker_nat" {
  provider = google-beta

  name = "${var.infra_id}-nat-worker"
  source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"
  nat_ip_allocate_option = "AUTO_ONLY"
  min_ports_per_vm = 512
  subnetwork {
    name = google_compute_subnetwork.worker_subnet.self_link
    source_ip_ranges_to_nat = ["ALL_IP_RANGES"]
  }

  router = google_compute_router.router.name
  region = "${var.region}"

  depends_on = [
    google_compute_router.router
  ]
}
```

### [9.9. Networking requirements for user-provisioned infrastructure](#installation-network-user-infra_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files.

#### [9.9.1. Setting the cluster node hostnames through DHCP](#installation-host-names-dhcp-user-infra_installing-gcp-user-infra) Copy linkLink copied to clipboard!

On Red Hat Enterprise Linux CoreOS (RHCOS) machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start prior to this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node.

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation.

#### [9.9.2. Network connectivity requirements](#installation-network-connectivity-user-infra_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster.

This section provides details about the ports that are required.

Important

In connected OpenShift Container Platform environments, all nodes are required to have internet access to pull images for platform containers and provide telemetry data to Red Hat.

Expand

Table 9.7. Ports used for all-machine to all-machine communications

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

Table 9.8. Ports used for all-machine to control plane communications

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | `6443` | Kubernetes API |

Show more

Expand

Table 9.9. Ports used for control plane machine to control plane machine communications

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | `2379`-`2380` | etcd server and peer ports |

Show more

### [9.10. Creating load balancers in Google Cloud](#installation-creating-gcp-lb_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must configure load balancers in Google Cloud for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* You have defined the variables in the *Exporting common variables* section.
* If you are not installing a cluster into a shared VPC, you have defined the variables in the *Creating a VPC in Google Cloud* section.

**Procedure**

1. If you are installing a cluster into a shared VPC, set environment variables for the cluster network and control plane subnet.

   1. Determine the shared VPC network name by running the following command:

      ```
      $ gcloud compute networks list
      ```
   2. Set the `CLUSTER_NETWORK` variable by running the following command:

      ```
      $ export CLUSTER_NETWORK=$(gcloud compute networks describe <network_name> --format json | jq -r .selfLink)
      ```

      `<network_name>` specifies the name of the network you determined.
   3. List the available network subnets by running the following command:

      ```
      $ gcloud compute networks subnets list --network=<network_name>
      ```

      `<network_name>` specifies the name of the network you determined.
   4. Select a subnet from the list, and set the `CONTROL_SUBNET` variable by running the following command:

      ```
      $ export CONTROL_SUBNET=<control_subnet>
      ```

      `<control_subnet>` specifies the name of the subnet you selected from the list of subnets.
2. Copy the template from the **Infrastructure Manager template for the internal load balancer** section of this topic and save it as `02_lb_int.tf` in a directory called `02_lb_int` on your computer. This template describes the internal load balancing objects that your cluster requires.

   1. Create an internal load balancer by running the following command:

      ```
      $ gcloud infra-manager deployments apply <internal_lb_deployment_name> \
        --location=${REGION} \
        --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_network=${CLUSTER_NETWORK},control_subnet=${CONTROL_SUBNET},zone_0=${ZONE_0},zone_1=${ZONE_1},zone_2=${ZONE_2} \
        --project=${PROJECT_NAME} \
        --local-source=./02_lb_int \
        --service-account=${INSTALL_SERVICE_ACCOUNT}
      ```

      `<internal_lb_deployment_name>` specifies the name of the internal load balancer deployment you create.
   2. Export the `CLUSTER_IP` variable by running the following command:

      ```
      $ export CLUSTER_IP=$(gcloud compute addresses describe ${INFRA_ID}-cluster-ip --region=${REGION} --format json | jq -r .address)
      ```
3. Optional: For a public or externally available cluster, copy the template from the **Infrastructure Manager template for the external load balancer** section of this topic and save it as `02_lb_ext.tf` in a directory called `02_lb_ext` on your computer. This template describes the external load balancing objects that your cluster requires.

   1. Create an external load balancer by running the following command:

      ```
      $ gcloud infra-manager deployments apply <external_lb_deployment_name> \
        --location=${REGION} \
        --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION} \
        --project=${PROJECT_NAME} \
        --local-source=./02_lb_ext \
        --service-account=${INSTALL_SERVICE_ACCOUNT}
      ```

      `<external_lb_deployment_name>` specifies the name of the external load balancer deployment you create.
   2. Export the `CLUSTER_PUBLIC_IP` variable by running the following command:

      ```
      $ export CLUSTER_PUBLIC_IP=$(gcloud compute addresses describe ${INFRA_ID}-cluster-public-ip --region=${REGION} --format json | jq -r .address)
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [9.10.1. Infrastructure Manager template for the external load balancer](#installation-infrastructure-manager-ext-lb_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the external load balancer that you need for your OpenShift Container Platform cluster:

**Example 9.26. `02_lb_ext.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}
variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}
variable "project" {
  type        = string
  description = "Project ID"
}
variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

resource "google_compute_address" "cluster_public_ip" {
  provider = google-beta

  name = "${var.infra_id}-cluster-public-ip"
  region = "${var.region}"
}

resource "google_compute_http_health_check" "api_http_health_check" {
  provider = google-beta

  name = "${var.infra_id}-api-http-health-check"
  port = 6080
  request_path = "/readyz"
}

resource "google_compute_target_pool" "api_target_pool" {
  provider = google-beta

  name = "${var.infra_id}-api-target-pool"
  region = "${var.region}"
  health_checks = [
    google_compute_http_health_check.api_http_health_check.id
  ]
}

resource "google_compute_forwarding_rule" "api_forwarding_rule" {
  provider = google-beta

  name = "${var.infra_id}-api-forwarding-rule"
  ip_address = google_compute_address.cluster_public_ip.address
  port_range = "6443"
  region = "${var.region}"
  target = google_compute_target_pool.api_target_pool.id
}
```

#### [9.10.2. Infrastructure Manager template for the internal load balancer](#installation-infrastructure-manager-int-lb_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the internal load balancer that you need for your OpenShift Container Platform cluster:

**Example 9.27. `02_lb_int.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}
variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}
variable "project" {
  type        = string
  description = "Project ID"
}
variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}
variable "control_subnet" {
  type        = string
  description = "Subnet for the control plane instances."
}
variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

# Terraform handles lists but the infra-manager --input-values only
# supports scalar types.
# If you require more or less zones, you must manually add them below
# as a single variable for each. You must add the zones to the
# locals `zones` list below.
variable "zone_0" {
  type        = string
  description = "Zone 1 for the instance types."
}

variable "zone_1" {
  type        = string
  description = "Zone 2 for the instance types."
}

variable "zone_2" {
  type        = string
  description = "Zone 3 for the instance types."
}

locals {
  zones = ["${var.zone_0}", "${var.zone_1}", "${var.zone_2}"]
}

resource "google_compute_address" "cluster_ip" {
  provider = google-beta

  name = "${var.infra_id}-cluster-ip"
  address_type = "INTERNAL"
  region = "${var.region}"
  subnetwork = "${var.control_subnet}"
}

resource "google_compute_health_check" "api_internal_health_check" {
  provider = google-beta

  name = "${var.infra_id}-api-internal-health-check"
  https_health_check {
    port = 6443
  }
}

resource "google_compute_region_backend_service" "api_internal" {
  provider = google-beta

  name = "${var.infra_id}-api-internal"
  timeout_sec = 120
  protocol = "TCP"
  region = "${var.region}"
  load_balancing_scheme = "INTERNAL"
  health_checks = [
    google_compute_health_check.api_internal_health_check.id
  ]

  dynamic "backend" {
    for_each = google_compute_instance_group.master_ig

    content {
      balancing_mode = "CONNECTION"
      group = backend.value.self_link
    }
  }
}

resource "google_compute_forwarding_rule" "api_internal_forwarding_rule" {
  provider = google-beta

  name = "${var.infra_id}-api-internal-forwarding-rule"
  ip_address = google_compute_address.cluster_ip.address
  backend_service = google_compute_region_backend_service.api_internal.id
  load_balancing_scheme = "INTERNAL"
  ports = [
    "6443",
    "22623"
  ]
  region = "${var.region}"
  subnetwork = "${var.control_subnet}"
}

resource "google_compute_instance_group" "master_ig" {
  provider = google-beta

  for_each = toset(local.zones)

  name = "${var.infra_id}-master-${each.key}-ig"
  network = "${var.cluster_network}"
  zone = "${each.key}"
  named_port {
    name = "ignition"
    port = 22623
  }
  named_port {
    name = "https"
    port = 6443
  }
}
```

### [9.11. Creating a private DNS zone in Google Cloud](#installation-creating-gcp-private-dns_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must configure a private DNS zone in Google Cloud for your OpenShift Container Platform cluster to use. One way to create this component is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for the private DNS** section of this topic and save it as `02_dns.tf` in a folder called `02_dns` on your computer. This template describes the private DNS objects that your cluster requires.
2. If you are installing a cluster into a shared VPC, and the host project already has a private DNS zone, skip this step. Create the DNS zone by running the following command:

   ```
   $ gcloud infra-manager deployments apply <dns_zone_deployment_name> \
     --location=${REGION} \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_domain=${CLUSTER_DOMAIN},cluster_network=${CLUSTER_NETWORK} \
     --project=${PROJECT_NAME} \
     --local-source=./02_dns \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<dns_zone_deployment_name>` specifies the name of the DNS zone deployment you create.
3. The templates do not create DNS entries due to limitations of Infrastructure Manager, so you must create them manually:

   1. Add the internal DNS entries by running the following commands:

      ```
      $ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
      ```

      ```
      $ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone
      ```

      ```
      $ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone
      ```

      ```
      $ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api-int.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone
      ```

      ```
      $ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone
      ```
   2. For an external cluster, also add the external DNS entries by running the following commands:

      ```
      $ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
      ```

      ```
      $ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
      ```

      ```
      $ gcloud dns record-sets transaction add ${CLUSTER_PUBLIC_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
      ```

      ```
      $ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [9.11.1. Infrastructure Manager template for the private DNS](#installation-infrastructure-manager-private-dns_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the private DNS that you need for your OpenShift Container Platform cluster:

**Example 9.28. `02_dns.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "cluster_domain" {
  type        = string
  description = "ClusterName.BaseDomain"
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

resource "google_dns_managed_zone" "private_zone" {
  provider = google-beta

  name = "${var.infra_id}-private-zone"
  dns_name = "${var.cluster_domain}."
  description = "OpenShift Installer UPI create private DNS zone."
  visibility = "private"
  private_visibility_config {
    networks {
      network_url = "${var.cluster_network}"
    }
  }

  force_destroy = false
}
```

### [9.12. Creating firewall rules and IAM roles in Google Cloud](#installation-creating-gcp-firewall-rules-vpc_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must create firewall rules and IAM roles in Google Cloud for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Infrastructure Manager template. If you are installing a cluster into a shared VPC and the host project already has the necessary firewall rules and IAM roles, you can skip creating these resources.

Note

If you do not use the provided Infrastructure Manager template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for firewall rules and IAM roles** section of this topic and save it as `03_security.tf` in a folder called `03_security` on your computer. This template describes the security groups that your cluster requires.
2. Create the firewall rules and IAM roles by running the following command:

   ```
   $ gcloud infra-manager deployments apply <security_deployment_name> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./03_security \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_network=${CLUSTER_NETWORK},network_cidr=${NETWORK_CIDR} \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<security_deployment_name>` specifies the name of the deployment of firewall rules and IAM roles.
3. Configure service account variables based on the roles you created by running the following commands:

   ```
   $ export MASTER_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter "email~^${INFRA_ID}-m@${PROJECT_NAME}." --format json | jq -r '.[0].email')
   ```

   ```
   $ export WORKER_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter "email~^${INFRA_ID}-w@${PROJECT_NAME}." --format json | jq -r '.[0].email')
   ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [9.12.1. Infrastructure Manager template for firewall rules and IAM roles](#installation-infrastructure-manager-firewall-rules_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the firewall rules and IAM roles that you need for your OpenShift Container Platform cluster:

**Example 9.29. `03_security.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

variable "network_cidr" {
  type        = string
  description = "CIDR for network of the cluster."
}

variable "allowed_external_cidr" {
  type        = string
  description = "Allowed external CIDR for firewall rule."
  default     = "0.0.0.0/0"
}

resource "google_compute_firewall" "bootstrap_in_ssh" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap-in-ssh"
  source_ranges = [
    "${var.allowed_external_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-bootstrap"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["22"]
  }
}

resource "google_compute_firewall" "api" {
  provider = google-beta

  name = "${var.infra_id}-api"
  source_ranges = [
   "${var.allowed_external_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["6443"]
  }
}

resource "google_compute_firewall" "health_checks" {
  provider = google-beta

  name = "${var.infra_id}-health-checks"
  source_ranges = [
    "35.191.0.0/16",
    "130.211.0.0/22",
    "209.85.152.0/22",
    "209.85.204.0/22"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["6080", "6443", "22624"]
  }
}

resource "google_compute_firewall" "etcd" {
  provider = google-beta

  name = "${var.infra_id}-etcd"
  source_tags = [
    "${var.infra_id}-master"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["2379-2380"]
  }
}

resource "google_compute_firewall" "control_plane" {
  provider = google-beta

  name = "${var.infra_id}-control-plane"
  source_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["10257"]
  }
  allow {
    protocol = "tcp"
    ports = ["10259"]
  }
  allow {
    protocol = "tcp"
    ports = ["22623"]
  }
}

resource "google_compute_firewall" "internal_network" {
  provider = google-beta

  name = "${var.infra_id}-internal-network"
  source_ranges = [
    "${var.network_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "icmp"
  }
  allow {
    protocol = "tcp"
    ports = ["22"]
  }
}

resource "google_compute_firewall" "internal_cluster" {
  provider = google-beta

  name = "${var.infra_id}-internal-cluster"
  source_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  target_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "udp"
    ports = ["4789", "6081"]
  }
  allow {
    protocol = "udp"
    ports = ["500", "4500"]
  }
  allow {
    protocol = "esp"
  }
  allow {
    protocol = "tcp"
    ports = ["9000-9999"]
  }
  allow {
    protocol = "udp"
    ports = ["9000-9999"]
  }
  allow {
    protocol = "tcp"
    ports = ["10250"]
  }
  allow {
    protocol = "tcp"
    ports = ["30000-32767"]
  }
  allow {
    protocol = "udp"
    ports = ["30000-32767"]
  }
}

resource "google_service_account" "master_node_sa" {
  provider = google-beta

  account_id = "${var.infra_id}-m"
  display_name = "${var.infra_id}-master-node"
}

resource "google_service_account" "worker_node_sa" {
  provider = google-beta

  account_id = "${var.infra_id}-w"
  display_name = "${var.infra_id}-worker-node"
}
```

### [9.13. Creating IAM policy bindings in Google Cloud](#installation-creating-gcp-iam-shared-vpc_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must create IAM policy bindings in Google Cloud for your OpenShift Container Platform cluster to use.

**Prerequisites**

* You have defined the variables in the *Exporting common variables* section.

**Procedure**

1. Export the variable for the subnet that hosts the compute machines by running the following command:

   ```
   $ export COMPUTE_SUBNET=(`gcloud compute networks subnets describe ${INFRA_ID}-worker-subnet --region=${REGION} --format json | jq -r .selfLink`)
   ```
2. The templates do not create the policy bindings due to limitations of Infrastructure Manager, so you must create them manually by running the following commands:

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.instanceAdmin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkAdmin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.securityAdmin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/iam.serviceAccountUser"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/storage.admin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/compute.viewer"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/storage.admin"
   ```
3. Create a service account key and store it locally for later use by running the following command:

   ```
   $ gcloud iam service-accounts keys create service-account-key.json --iam-account=${MASTER_SERVICE_ACCOUNT}
   ```

### [9.14. Creating the RHCOS cluster image for the Google Cloud infrastructure](#installation-gcp-user-infra-rhcos_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must use a valid Red Hat Enterprise Linux CoreOS (RHCOS) image for Google Cloud for your OpenShift Container Platform nodes.

**Prerequisites**

* You have downloaded the `openshift-install` binary.

**Procedure**

1. Obtain the image name by running the following command:

   ```
   $ source_image=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.gcp.name')
   ```
2. Obtain the project name by running the following command:

   ```
   $ source_project=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.gcp.project')
   ```
3. Create the image by running the following command:

   ```
   $ gcloud compute images create "${INFRA_ID}-rhcos-image" \
       --source-image="${source_image}" --source-image-project="${source_project}"
   ```

### [9.15. Creating the bootstrap machine in Google Cloud](#installation-creating-gcp-bootstrap_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must create the bootstrap machine in Google Cloud to use during OpenShift Container Platform cluster initialization. One way to create this machine is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided Infrastructure Manager template to create your bootstrap machine, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

If you need to redeploy the bootstrap machine for any reason, delete the existing bootstrap VM first. If you redeploy the bootstrap machine without deleting the existing VM, Infrastructure Manager will update the metadata and appear to succeed, but the Ignition file will not be executed again. This will result in the VM still being based on the old Ignition data.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for the bootstrap machine** section of this topic and save it as `04_bootstrap.tf` in a folder called `04_bootstrap` on your computer. This template describes the bootstrap machine that your cluster requires.

   * You can edit the `04_bootstrap.tf` file to add additional tags to the bootstrap machine, by modifying the existing `tags` stanza as follows:

     ```
     resource "google_compute_instance" "bootstrap" {
     # ...
       tags = [
         "${var.infra_id}-master",
         "${var.infra_id}-bootstrap",
         "custom-tag-example"
       ]
     # ...
     }
     ```
2. Export the location of the Red Hat Enterprise Linux CoreOS (RHCOS) image that the installation program requires by running the following command:

   ```
   $ export CLUSTER_IMAGE=(`gcloud compute images describe ${INFRA_ID}-rhcos-image --format json | jq -r .selfLink`)
   ```
3. Create a bucket by running the following command:

   ```
   $ gcloud storage buckets create "gs://${INFRA_ID}-bootstrap-ignition"
   ```
4. Upload the `bootstrap.ign` file by running the following command:

   ```
   $ gcloud storage cp bootstrap.ign "gs://${INFRA_ID}-bootstrap-ignition/"
   ```
5. Create a signed URL for the bootstrap instance and export the URL from the output as a variable by running the following command:

   ```
   $ export BOOTSTRAP_IGN="$(gcloud storage sign-url --duration=2h --private-key-file=service-account-key.json "gs://${INFRA_ID}-bootstrap-ignition/bootstrap.ign" | grep "^signed_url:" | awk '{print $2}')"
   ```
6. Create the bootstrap deployment by running the following command:

   ```
   $ gcloud infra-manager deployments apply <bootstrap_deployment_name> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./04_bootstrap \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone=${ZONE_0},cluster_network=${CLUSTER_NETWORK},subnet=${CONTROL_SUBNET},image=${CLUSTER_IMAGE},bootstrap_ign="${BOOTSTRAP_IGN}",is_public_cluster=<public_cluster_status> \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   where:

   `<bootstrap_deployment_name>`
   :   Specifies the name of the bootstrap deployment.

   `<public_cluster_status>`
   :   Specifies whether the cluster is public or private. If it is a public cluster, specify `true`. If it is a private cluster, specify `false`.
7. The templates do not manage load balancer membership due to limitations of Infrastructure Manager, so you must add the bootstrap machine manually.

   1. Add the bootstrap instance to the internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances \
          ${INFRA_ID}-bootstrap-ig --zone=${ZONE_0} --instances=${INFRA_ID}-bootstrap
      ```
   2. Add the bootstrap instance group to the internal load balancer backend service by running the following command:

      ```
      $ gcloud compute backend-services add-backend \
          ${INFRA_ID}-api-internal --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [9.15.1. Infrastructure Manager template for the bootstrap machine](#installation-infrastructure-manager-bootstrap_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the bootstrap machine that you need for your OpenShift Container Platform cluster:

**Example 9.30. `04_bootstrap.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "zone" {
  type        = string
  description = "Zone inside of the region where the bootstrap node is created."
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

variable "subnet" {
  type        = string
  description = "Control plane subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the bootstrap machine."
  default     = "n1-standard-4"
}

variable "root_volume_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "bootstrap_ign" {
  type        = string
  description = "Bootstrap ignition data."
}

variable "is_public_cluster" {
  type        = bool
  default     = true
  description = "Whether the publish policy is the default External"
}

resource "google_compute_address" "bootstrap_public_ip" {
  provider = google-beta
  count = var.is_public_cluster ? 1 : 0

  name = "${var.infra_id}-bootstrap-public-ip"
  region = "${var.region}"
}

resource "google_compute_instance" "bootstrap" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap"
  zone = "${var.zone}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-bootstrap"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.root_volume_size}"
      image = "${var.image}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"

    # Dynamic block to conditionally create access_config
    dynamic "access_config" {
      for_each = var.is_public_cluster ? [1] : []
      content {
        nat_ip = google_compute_address.bootstrap_public_ip[0].address
      }
    }
  }
  metadata = {
    user-data = "{\"ignition\":{\"config\":{\"replace\":{\"source\":\"${var.bootstrap_ign}\"}},\"version\":\"3.2.0\"}}"
  }
}

resource "google_compute_instance_group" "bootstrap_ig" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap-ig"
  network = "${var.cluster_network}"
  zone = "${var.zone}"
  named_port {
    name = "ignition"
    port = 22623
  }
  named_port {
    name = "https"
    port = 6443
  }
}
```

### [9.16. Creating the control plane machines in Google Cloud](#installation-creating-gcp-control-plane_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You must create the control plane machines in Google Cloud for your cluster to use. One way to create these machines is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided template to create your control plane machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* You defined the variables in the *Exporting common variables*, *Creating load balancers in Google Cloud*, *Creating IAM roles in Google Cloud*, and *Creating the bootstrap machine in Google Cloud* sections.
* You created the bootstrap machine.
* You created the Ignition configuration files.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for control plane machines** section of this topic and save it as `05_control_plane.tf` in a folder called `05_control_plane` on your computer. This template describes the control plane machines that your cluster requires.

   * You can edit the `05_control_plane.tf` file to add additional tags to the control plane machines, by modifying the existing `tags` stanza. The following example adds a custom tag to the first control plane machine, which is named `master_0`:

     ```
     resource "google_compute_instance" "master_0" {
     # ...
       tags = [
         "${var.infra_id}-master",
         "custom_tag_example"
       ]
     # ...
     }
     ```
2. Copy the `master.ign` file from your installation directory into the `05_control_plane` folder by running the following command:

   ```
   $ cp <installation_directory>/master.ign 05_control_plane/master.ign
   ```

   `<installation_directory>` specifies the directory where you created the Ignition configuration files.
3. Create the control plane deployment by running the following command:

   ```
   $ gcloud infra-manager deployments apply <control_plane_deployment> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./05_control_plane \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone_0=${ZONE_0},zone_1=${ZONE_1},zone_2=${ZONE_2},subnet=${CONTROL_SUBNET},image=${CLUSTER_IMAGE},service_account_email=${MASTER_SERVICE_ACCOUNT} \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<control_plane_deployment>` specifies the name of the control plane deployment.
4. Delete the temporary ignition file from the `05_control_plane` folder by running the following command:

   ```
   $ rm 05_control_plane/master.ign
   ```
5. The templates do not manage load balancer membership due to limitations of Infrastructure Manager, so you must add the control plane machines manually.

   1. Add the first control plane machine to an internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_0}-ig --zone=${ZONE_0} --instances=${INFRA_ID}-master-0
      ```
   2. Add the second control plane machine to an internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_1}-ig --zone=${ZONE_1} --instances=${INFRA_ID}-master-1
      ```
   3. Add the third control plane machine to an internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_2}-ig --zone=${ZONE_2} --instances=${INFRA_ID}-master-2
      ```
6. For an external cluster, you must also add the control plane machines to external load balancer target pools.

   1. Add the first control plane machine to an external load balancer pool by running the following command:

      ```
      $ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_0}" --instances=${INFRA_ID}-master-0
      ```
   2. Add the second control plane machine to an external load balancer pool by running the following command:

      ```
      $ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_1}" --instances=${INFRA_ID}-master-1
      ```
   3. Add the third control plane machine to an external load balancer pool by running the following command:

      ```
      $ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_2}" --instances=${INFRA_ID}-master-2
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [9.16.1. Infrastructure Manager template for control plane machines](#installation-infrastructure-manager-control-plane_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the control plane machines that you need for your OpenShift Container Platform cluster:

**Example 9.31. `05_control_plane.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
    local = {
        source = "hashicorp/local",
        version = ">= 2.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

# Terraform handles lists but the infra-manager --input-values only
# supports scalar types.
# If you require more or less zones, you must manually add them below
# as a single variable for each. You must add the zones to the
# locals `zones` list below.
variable "zone_0" {
  type        = string
  description = "Zone 1 for the instance types."
}

variable "zone_1" {
  type        = string
  description = "Zone 2 for the instance types."
}

variable "zone_2" {
  type        = string
  description = "Zone 3 for the instance types."
}

variable "subnet" {
  type        = string
  description = "Control plane subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the control plane machine."
  default     = "n1-standard-4"
}

variable "disk_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "disk_type" {
  type        = string
  description = "Type of storage disk for the vm."
  default     = "pd-ssd"
}

variable "service_account_email" {
  type        = string
  description = "Email for the service account attached to the control planes."
}

data "local_file" "ignition_file" {
  filename = "${path.module}/master.ign"
}

resource "google_compute_instance" "master_0" {
  provider = google-beta

  name = "${var.infra_id}-master-0"
  zone = "${var.zone_0}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

resource "google_compute_instance" "master_1" {
  provider = google-beta

  name = "${var.infra_id}-master-1"
  zone = "${var.zone_1}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

resource "google_compute_instance" "master_2" {
  provider = google-beta

  name = "${var.infra_id}-master-2"
  zone = "${var.zone_2}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}
```

### [9.17. Creating additional worker machines in Google Cloud](#installation-creating-gcp-worker_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can create worker machines in Google Cloud for your cluster by using the Infrastructure Manager template. You can adjust the number of machines by modifying the number of `google_compute_instance` resources in the provided template.

Note

If you do not use the provided Infrastructure Manager template to create your compute machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

If you are installing a three-node cluster, skip this step. A three-node cluster consists of three control plane machines, which also act as compute machines.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables*, *Creating load balancers in Google Cloud*, and *Creating the bootstrap machine in Google Cloud* sections.
* Create the bootstrap machine.
* Create the control plane machines.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for worker machines** section of this topic and save it as `06_worker.tf` in a folder called `06_worker` on your computer. This template describes the worker machines that your cluster requires.

   * You can edit the `06_worker.tf` file to add additional tags to the compute machines, by modifying the existing `tags` stanza as follows:

     ```
     resource "google_compute_instance" "worker_0" {
     # ...
       tags = [
         "${var.infra_id}-worker-0",
         "custom-tag-example"
       ]
     # ...
     }
     ```
2. Copy the `worker.ign` file from your installation directory into the `06_worker` folder by running the following command:

   ```
   $ cp <installation_directory>/worker.ign 06_worker/worker.ign
   ```

   `<installation_directory>` specifies the directory where you created the Ignition configuration files.
3. Create the deployment by running the following command:

   ```
   $ gcloud infra-manager deployments apply <worker_deployment_name> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./06_worker \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone_0=${ZONE_0},zone_1=${ZONE_1},subnet=${COMPUTE_SUBNET},image=${CLUSTER_IMAGE},service_account_email=${WORKER_SERVICE_ACCOUNT} \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<worker_deployment_name>` specifies the name of the deployment.
4. Remove the `worker.ign` file by running the following command:

   ```
   $ rm 06_worker/worker.ign
   ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [9.17.1. Infrastructure Manager template for worker machines](#installation-infrastructure-manager-worker_installing-gcp-user-infra) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the worker machines that you need for your OpenShift Container Platform cluster:

**Example 9.32. `06_worker.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

# Terraform handles lists but the infra-manager --input-values only
# supports scalar types.
# If you require more or less zones, you must manually add them below
# as a single variable for each. You must add the zones to the
# locals `zones` list below.
variable "zone_0" {
  type        = string
  description = "Zone 1 for the instance types."
}

variable "zone_1" {
  type        = string
  description = "Zone 2 for the instance types."
}

variable "subnet" {
  type        = string
  description = "Compute subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the compute machine."
  default     = "n1-standard-4"
}

variable "disk_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "disk_type" {
  type        = string
  description = "Type of storage disk for the vm."
  default     = "pd-ssd"
}

variable "service_account_email" {
  type        = string
  description = "Email for the service account attached to the compute nodes."
}

data "local_file" "ignition_file" {
  filename = "${path.module}/worker.ign"
}

resource "google_compute_instance" "worker_0" {
  provider = google-beta

  name = "${var.infra_id}-worker-0"
  zone = "${var.zone_0}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-worker"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

resource "google_compute_instance" "worker_1" {
  provider = google-beta

  name = "${var.infra_id}-worker-1"
  zone = "${var.zone_1}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-worker"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}
```

### [9.18. Removing bootstrap resources in Google Cloud](#installation-gcp-user-infra-wait-for-bootstrap_installing-gcp-user-infra) Copy linkLink copied to clipboard!

After you create all of the required infrastructure in Google Cloud, wait for the bootstrap process to complete on the machines that you provisioned by using the Ignition config files. The installation program created the Ignition config files.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.
* Create the bootstrap machine.
* Create the control plane machines.

**Procedure**

1. Change to the directory that includes the installation program and run the following command:

   ```
   $ ./openshift-install wait-for bootstrap-complete --dir <installation_directory> \
   ```

   1

   ```
       --log-level info
   ```

   2

   [1](#CO18-1)
   :   For `<installation_directory>`, specify the path to the directory where you stored the installation files.

   [2](#CO18-2)
   :   To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

   If the command exits without a `FATAL` warning, your production control plane has initialized.
2. To remove the bootstrap instance group from the backend services' backends, run the following commands:

   ```
   $ gcloud compute backend-services remove-backend ${INFRA_ID}-api-internal --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
   ```

   ```
   $ ingress_backendservice=$(gcloud compute backend-services list --filter="backends.group~${INFRA_ID}" --format='value(name)' | grep -v "${INFRA_ID}")
   ```

   1. If `ingress_backendservice` is not empty, run the following `describe` command for the bootstrap group:

      ```
      $ gcloud compute backend-services describe ${ingress_backendservice} --region=${REGION}
      ```
   2. If the `describe` command displays that the bootstrap group is one of its backends, run the following `remove-backend` command to remove the bootstrap group from the backends:

      ```
      $ gcloud compute backend-services remove-backend ${ingress_backendservice} --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
      ```
   3. To remove the bucket and the deployment, run the following commands:

      ```
      $ gcloud storage rm "gs://${INFRA_ID}-bootstrap-ignition/bootstrap.ign"
      ```

      ```
      $ gcloud storage rm --recursive "gs://${INFRA_ID}-bootstrap-ignition/"
      ```

      ```
      $ gcloud infra-manager deployments delete <bootstrap_deployment_name> \
          --project=${PROJECT_NAME} --location=${REGION} --quiet
      ```

      Specify the name of the bootstrap deployment you created for `<bootstrap_deployment_name>`.

### [9.19. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-gcp-user-infra) Copy linkLink copied to clipboard!

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

### [9.20. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-gcp-user-infra) Copy linkLink copied to clipboard!

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

### [9.21. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-gcp-user-infra) Copy linkLink copied to clipboard!

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

### [9.22. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-gcp-user-infra) Copy linkLink copied to clipboard!

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and OpenShift Container Platform generates it during installation.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* Ensure the bootstrap process completed successfully.

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

### [9.23. Approving the certificate signing requests for your machines](#installation-approve-csrs_installing-gcp-user-infra) Copy linkLink copied to clipboard!

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

### [9.24. Optional: Adding the ingress DNS records](#installation-gcp-user-infra-adding-ingress_installing-gcp-user-infra) Copy linkLink copied to clipboard!

If you removed the DNS zone configuration when creating Kubernetes manifests and generating Ignition configs, you must manually create DNS records that point at the ingress load balancer. You can create either a wildcard `*.apps.{baseDomain}.` or specific records. You can use A, CNAME, and other records per your requirements.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* section.
* Remove the DNS Zone configuration when creating Kubernetes manifests and generating Ignition configs.
* Ensure the bootstrap process completed successfully.

**Procedure**

1. Wait for the Ingress router to create a load balancer and populate the `EXTERNAL-IP` field:

   ```
   $ oc -n openshift-ingress get service router-default
   ```

   **Example output**

   ```
   NAME             TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)                      AGE
   router-default   LoadBalancer   172.30.18.154   35.233.157.184   80:32288/TCP,443:31215/TCP   98
   ```
2. Add the A record to your zones:

   * To use A records:

     1. Export the variable for the router IP address:

        ```
        $ export ROUTER_IP=`oc -n openshift-ingress get service router-default --no-headers | awk '{print $4}'`
        ```
     2. Add the A record to the private zones:

        ```
        $ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
        ```

        ```
        $ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone
        ```

        ```
        $ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${INFRA_ID}-private-zone
        ```

        ```
        $ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone
        ```
     3. For an external cluster, also add the A record to the public zones:

        ```
        $ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
        ```

        ```
        $ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
        ```

        ```
        $ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
        ```

        ```
        $ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
        ```
   * To add explicit domains instead of using a wildcard, create entries for each of the cluster’s current routes:

     ```
     $ oc get --all-namespaces -o jsonpath='{range .items[*]}{range .status.ingress[*]}{.host}{"\n"}{end}{end}' routes
     ```

     **Example output**

     ```
     oauth-openshift.apps.your.cluster.domain.example.com
     console-openshift-console.apps.your.cluster.domain.example.com
     downloads-openshift-console.apps.your.cluster.domain.example.com
     alertmanager-main-openshift-monitoring.apps.your.cluster.domain.example.com
     prometheus-k8s-openshift-monitoring.apps.your.cluster.domain.example.com
     ```

### [9.25. Completing a Google Cloud installation on user-provisioned infrastructure](#installation-gcp-user-infra-installation_installing-gcp-user-infra) Copy linkLink copied to clipboard!

After you start the OpenShift Container Platform installation on Google Cloud user-provisioned infrastructure, you can monitor the cluster events until the cluster is ready.

**Prerequisites**

* Ensure the bootstrap process completed successfully.

**Procedure**

1. Complete the cluster installation:

   ```
   $ ./openshift-install --dir <installation_directory> wait-for install-complete
   ```

   1

   **Example output**

   ```
   INFO Waiting up to 30m0s for the cluster to initialize...
   ```

   [1](#CO19-1)
   :   For `<installation_directory>`, specify the path to the directory that you stored the installation files in.

   Important

   * The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
   * It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
2. Observe the running state of your cluster.

   1. Run the following command to view the current cluster version and status:

      ```
      $ oc get clusterversion
      ```

      **Example output**

      ```
      NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
      version             False       True          24m     Working towards 4.5.4: 99% complete
      ```
   2. Run the following command to view the Operators managed on the control plane by the Cluster Version Operator (CVO):

      ```
      $ oc get clusteroperators
      ```

      **Example output**

      ```
      NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
      authentication                             4.5.4     True        False         False      7m56s
      cloud-credential                           4.5.4     True        False         False      31m
      cluster-autoscaler                         4.5.4     True        False         False      16m
      console                                    4.5.4     True        False         False      10m
      csi-snapshot-controller                    4.5.4     True        False         False      16m
      dns                                        4.5.4     True        False         False      22m
      etcd                                       4.5.4     False       False         False      25s
      image-registry                             4.5.4     True        False         False      16m
      ingress                                    4.5.4     True        False         False      16m
      insights                                   4.5.4     True        False         False      17m
      kube-apiserver                             4.5.4     True        False         False      19m
      kube-controller-manager                    4.5.4     True        False         False      20m
      kube-scheduler                             4.5.4     True        False         False      20m
      kube-storage-version-migrator              4.5.4     True        False         False      16m
      machine-api                                4.5.4     True        False         False      22m
      machine-config                             4.5.4     True        False         False      22m
      marketplace                                4.5.4     True        False         False      16m
      monitoring                                 4.5.4     True        False         False      10m
      network                                    4.5.4     True        False         False      23m
      node-tuning                                4.5.4     True        False         False      23m
      openshift-apiserver                        4.5.4     True        False         False      17m
      openshift-controller-manager               4.5.4     True        False         False      15m
      openshift-samples                          4.5.4     True        False         False      16m
      operator-lifecycle-manager                 4.5.4     True        False         False      22m
      operator-lifecycle-manager-catalog         4.5.4     True        False         False      22m
      operator-lifecycle-manager-packageserver   4.5.4     True        False         False      18m
      service-ca                                 4.5.4     True        False         False      23m
      service-catalog-apiserver                  4.5.4     True        False         False      23m
      service-catalog-controller-manager         4.5.4     True        False         False      23m
      storage                                    4.5.4     True        False         False      17m
      ```
   3. Run the following command to view your cluster pods:

      ```
      $ oc get pods --all-namespaces
      ```

      **Example output**

      ```
      NAMESPACE                                               NAME                                                                READY     STATUS      RESTARTS   AGE
      kube-system                                             etcd-member-ip-10-0-3-111.us-east-2.compute.internal                1/1       Running     0          35m
      kube-system                                             etcd-member-ip-10-0-3-239.us-east-2.compute.internal                1/1       Running     0          37m
      kube-system                                             etcd-member-ip-10-0-3-24.us-east-2.compute.internal                 1/1       Running     0          35m
      openshift-apiserver-operator                            openshift-apiserver-operator-6d6674f4f4-h7t2t                       1/1       Running     1          37m
      openshift-apiserver                                     apiserver-fm48r                                                     1/1       Running     0          30m
      openshift-apiserver                                     apiserver-fxkvv                                                     1/1       Running     0          29m
      openshift-apiserver                                     apiserver-q85nm                                                     1/1       Running     0          29m
      ...
      openshift-service-ca-operator                           openshift-service-ca-operator-66ff6dc6cd-9r257                      1/1       Running     0          37m
      openshift-service-ca                                    apiservice-cabundle-injector-695b6bcbc-cl5hm                        1/1       Running     0          35m
      openshift-service-ca                                    configmap-cabundle-injector-8498544d7-25qn6                         1/1       Running     0          35m
      openshift-service-ca                                    service-serving-cert-signer-6445fc9c6-wqdqn                         1/1       Running     0          35m
      openshift-service-catalog-apiserver-operator            openshift-service-catalog-apiserver-operator-549f44668b-b5q2w       1/1       Running     0          32m
      openshift-service-catalog-controller-manager-operator   openshift-service-catalog-controller-manager-operator-b78cr2lnm     1/1       Running     0          31m
      ```

      When the current cluster version is `AVAILABLE`, the installation is complete.

### [9.26. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-gcp-user-infra) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

### [9.27. Next steps](#next-steps-6) Copy linkLink copied to clipboard!

* [Customize your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations)
* If necessary, you can [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting)
* [Configuring Global Access for an Ingress Controller on Google Cloud](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/networking_operators/#nw-ingress-controller-configuration-gcp-global-access_configuring-ingress)

## [Chapter 10. Installing a cluster into a shared VPC on Google Cloud using Infrastructure Manager templates](#installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

In OpenShift Container Platform version 4.22, you can install a cluster into a shared Virtual Private Cloud (VPC) on Google Cloud that uses infrastructure that you provide. In this context, a cluster installed into a shared VPC is a cluster that is configured to use a VPC from a project different from where the cluster is being deployed.

A shared VPC enables an organization to connect resources from multiple projects to a common VPC network. You can communicate within the organization securely and efficiently by using internal IPs from that network. For more information about shared VPC, see [Shared VPC overview](https://cloud.google.com/vpc/docs/shared-vpc) in the Google Cloud documentation.

The steps for performing a user-provided infrastructure installation into a shared VPC are outlined here. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods.

Important

The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.

### [10.1. Prerequisites](#prerequisites-6) Copy linkLink copied to clipboard!

* You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes.
* You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing).
* If you use a firewall and plan to use the Telemetry service, you [configured the firewall to allow the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires access to.
* If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, you can [manually create and maintain long-term credentials](#manually-create-iam_installing-gcp-customizations "4.10.1. Manually creating long-term credentials").
* If you want to provide your own private hosted zone, you must have created one in the service project with the DNS pattern `cluster-name.baseDomain.`, for example `testCluster.example.com.`. The private hosted zone must be bound to the VPC in the host project. For more information about cross-project binding, see [Create a zone with cross-project binding](https://cloud.google.com/dns/docs/zones/cross-project-binding) (Google documentation). If you do not provide a private hosted zone, the installation program will provision one automatically.

  Note

  Be sure to also review this site list if you are configuring a proxy.

### [10.2. Certificate signing requests management](#csr-management_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

On user-provisioned infrastructure, you must implement a mechanism for approving cluster certificate signing requests (CSRs) after installation when your cluster has limited access to automatic machine management.

The `kube-controller-manager` only approves the kubelet client CSRs. The `machine-approver` cannot guarantee the validity of a serving certificate that kubelet credentials request because it cannot confirm that the correct machine issued the request. You must find and implement a method of verifying the validity of the kubelet serving certificate requests and approving them.

### [10.3. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

Important

If your cluster cannot have direct internet access, you can perform a restricted network installation on some types of infrastructure that you provision. During that process, you download the required content and use it to populate a mirror registry with the installation packages. With some installation types, the environment that you install your cluster in will not require internet access. Before you update the cluster, you update the content of the mirror registry.

### [10.4. Configuring the Google Cloud project that hosts your cluster](#installation-gcp-user-infra-config-project-vpc) Copy linkLink copied to clipboard!

Before you can install OpenShift Container Platform, you must configure a Google Cloud project to host it.

#### [10.4.1. Creating a Google Cloud project](#installation-gcp-project_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, you must create a project in your Google Cloud account to host the cluster.

**Procedure**

* Create a project to host your OpenShift Container Platform cluster. See [Creating and Managing Projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in the Google Cloud documentation.

  Important

  Your Google Cloud project must use the Premium Network Service Tier if you are using installer-provisioned infrastructure. The Standard Network Service Tier is not supported for clusters installed using the installation program. The installation program configures internal load balancing for the `api-int.<cluster_name>.<base_domain>` URL; the Premium Tier is required for internal load balancing.

#### [10.4.2. Enabling API services in Google Cloud](#installation-gcp-enabling-api-services_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

Your Google Cloud project requires access to several API services to complete OpenShift Container Platform installation.

**Prerequisites**

* You created a project to host your cluster.

**Procedure**

* Enable the following required API services in the project that hosts your cluster. You may also enable optional API services which are not required for installation. See [Enabling services](https://cloud.google.com/service-usage/docs/enable-disable#enabling) in the Google Cloud documentation.

  Expand

  Table 10.1. Required API services

  | API service | Console service name |
  | --- | --- |
  | Compute Engine API | `compute.googleapis.com` |
  | Cloud Resource Manager API | `cloudresourcemanager.googleapis.com` |
  | Cloud DNS API | `dns.googleapis.com` |
  | IAM Service Account Credentials API | `iamcredentials.googleapis.com` |
  | Identity and Access Management (IAM) API | `iam.googleapis.com` |
  | Service Usage API | `serviceusage.googleapis.com` |

  Show more

  Expand

  Table 10.2. Optional API services

  | API service | Console service name |
  | --- | --- |
  | Cloud Deployment Manager V2 API | `deploymentmanager.googleapis.com` |
  | Google Cloud APIs | `cloudapis.googleapis.com` |
  | Service Management API | `servicemanagement.googleapis.com` |
  | Google Cloud Storage JSON API | `storage-api.googleapis.com` |
  | Cloud Storage | `storage-component.googleapis.com` |

  Show more

#### [10.4.3. Google Cloud account limits](#installation-gcp-limits_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

The OpenShift Container Platform cluster uses a number of Google Cloud components, but the default [Quotas](https://cloud.google.com/docs/quota) do not affect your ability to install a default OpenShift Container Platform cluster.

A default cluster, which contains three compute and three control plane machines, uses the following resources. Note that some resources are required only during the bootstrap process and are removed after the cluster deploys.

Expand

Table 10.3. Google Cloud resources used in a default cluster

| Service | Component | Location | Total resources required | Resources removed after bootstrap |
| --- | --- | --- | --- | --- |
| Service account | IAM | Global | 6 | 1 |
| Firewall rules | Networking | Global | 11 | 1 |
| Forwarding rules | Compute | Global | 2 | 0 |
| Health checks | Compute | Global | 2 | 0 |
| Images | Compute | Global | 1 | 0 |
| Networks | Networking | Global | 1 | 0 |
| Routers | Networking | Global | 1 | 0 |
| Routes | Networking | Global | 2 | 0 |
| Subnetworks | Compute | Global | 2 | 0 |
| Target pools | Networking | Global | 2 | 0 |

Show more

Note

If any of the quotas are insufficient during installation, the installation program displays an error that states both which quota was exceeded and the region.

Be sure to consider your actual cluster size, planned cluster growth, and any usage from other clusters that are associated with your account. The CPU, static IP addresses, and persistent disk SSD (storage) quotas are the ones that are most likely to be insufficient.

If you plan to deploy your cluster in one of the following regions, you will exceed the maximum storage quota and are likely to exceed the CPU quota limit:

* `asia-east2`
* `asia-northeast2`
* `asia-south1`
* `australia-southeast1`
* `europe-north1`
* `europe-west2`
* `europe-west3`
* `europe-west6`
* `northamerica-northeast1`
* `southamerica-east1`
* `us-west2`

You can increase resource quotas from the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas), but you might need to file a support ticket. Be sure to plan your cluster size early so that you can allow time to resolve the support ticket before you install your OpenShift Container Platform cluster.

#### [10.4.4. Creating a service account in Google Cloud](#installation-gcp-service-account_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

OpenShift Container Platform requires a Google Cloud service account that provides authentication and authorization to access data in the Google APIs. If you do not have an existing IAM service account that contains the required roles in your project, you must create one.

Note

To reduce the scope of permissions granted to the main service account in your Google Cloud project while still being able to use the Google Cloud Container Storage Interface (CSI) Driver Operator, you can transfer the control of permissions from the project-wide service account to the control plane and compute node service accounts instead, thus reducing the scope of the permission. For more information, see Section *Reducing permissions while using the Google Cloud CSI Driver Operator*.

**Prerequisites**

* You created a project to host your cluster.

**Procedure**

1. Create a service account in the project that you use to host your OpenShift Container Platform cluster. See [Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account) in the Google Cloud documentation.
2. Grant the service account the appropriate permissions. You can either grant the individual permissions that follow or assign the `Owner` role to it. See [Granting roles to a service account for specific resources](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource).

   Note

   While making the service account an owner of the project is the easiest way to gain the required permissions, it means that service account has complete control over the project. You must determine if the risk that comes from offering that power is acceptable.
3. You can create the service account key in JSON format, or attach the service account to a Google Cloud virtual machine. See [Creating service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and [Creating and enabling service accounts for instances](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances) in the Google Cloud documentation.

   Note

   If you use a virtual machine with an attached service account to create your cluster, you must set `credentialsMode: Manual` in the `install-config.yaml` file before installation.

##### [10.4.4.1. Required Google Cloud roles](#installation-gcp-permissions_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform. If your organization’s security policies require a more restrictive set of permissions, you can create a service account with the following permissions. If you deploy your cluster into an existing virtual private cloud (VPC), the service account does not require certain networking permissions, which are noted in the following lists:

**Required roles for the installation program**

* Compute Admin
* Role Administrator
* Security Admin
* Service Account Admin
* Service Account Key Admin
* Service Account User
* Storage Admin

**Required roles for creating network resources during installation**

* DNS Administrator

**Required roles for using the Cloud Credential Operator in passthrough mode**

* Compute Load Balancer Admin
* Tag User

**Required roles for user-provisioned Google Cloud infrastructure**

* Cloud Infrastructure Manager Admin

The following roles are applied to the service accounts that the control plane and compute machines use:

Expand

Table 10.4. Google Cloud service account roles

| Account | Roles |
| --- | --- |
| Control Plane | `roles/compute.instanceAdmin` |
| `roles/compute.networkAdmin` |
| `roles/compute.securityAdmin` |
| `roles/storage.admin` |
| `roles/iam.serviceAccountUser` |
| Compute | `roles/compute.viewer` |
| `roles/storage.admin` |
| `roles/artifactregistry.reader` |

Show more

#### [10.4.5. Supported Google Cloud regions](#installation-gcp-regions_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can deploy an OpenShift Container Platform cluster to the following Google Cloud regions:

* `africa-south1` (Johannesburg, South Africa)
* `asia-east1` (Changhua County, Taiwan)
* `asia-east2` (Hong Kong)
* `asia-northeast1` (Tokyo, Japan)
* `asia-northeast2` (Osaka, Japan)
* `asia-northeast3` (Seoul, South Korea)
* `asia-south1` (Mumbai, India)
* `asia-south2` (Delhi, India)
* `asia-southeast1` (Jurong West, Singapore)
* `asia-southeast2` (Jakarta, Indonesia)
* `australia-southeast1` (Sydney, Australia)
* `australia-southeast2` (Melbourne, Australia)
* `europe-central2` (Warsaw, Poland)
* `europe-north1` (Hamina, Finland)
* `europe-southwest1` (Madrid, Spain)
* `europe-west1` (St. Ghislain, Belgium)
* `europe-west2` (London, England, UK)
* `europe-west3` (Frankfurt, Germany)
* `europe-west4` (Eemshaven, Netherlands)
* `europe-west6` (Zürich, Switzerland)
* `europe-west8` (Milan, Italy)
* `europe-west9` (Paris, France)
* `europe-west12` (Turin, Italy)
* `me-central1` (Doha, Qatar, Middle East)
* `me-central2` (Dammam, Saudi Arabia, Middle East)
* `me-west1` (Tel Aviv, Israel)
* `northamerica-northeast1` (Montréal, Québec, Canada)
* `northamerica-northeast2` (Toronto, Ontario, Canada)
* `southamerica-east1` (São Paulo, Brazil)
* `southamerica-west1` (Santiago, Chile)
* `us-central1` (Council Bluffs, Iowa, USA)
* `us-east1` (Moncks Corner, South Carolina, USA)
* `us-east4` (Ashburn, Northern Virginia, USA)
* `us-east5` (Columbus, Ohio)
* `us-south1` (Dallas, Texas)
* `us-west1` (The Dalles, Oregon, USA)
* `us-west2` (Los Angeles, California, USA)
* `us-west3` (Salt Lake City, Utah, USA)
* `us-west4` (Las Vegas, Nevada, USA)

Note

To determine which machine type instances are available by region and zone, see the Google [documentation](https://cloud.google.com/compute/docs/regions-zones#available).

#### [10.4.6. Installing and configuring CLI tools for Google Cloud](#installation-gcp-install-cli_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on Google Cloud using user-provisioned infrastructure, you must install and configure the CLI tools for Google Cloud.

**Prerequisites**

* You created a project to host your cluster.
* You created a service account and granted it the required permissions.

**Procedure**

1. Install the following binaries in `$PATH`:

   * `gcloud`
   * `gsutil`

   See [Install the latest Cloud SDK version](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version) in the Google Cloud documentation.
2. Authenticate using the `gcloud` tool with your configured service account.

   See [Authorizing with a service account](https://cloud.google.com/sdk/docs/authorizing#authorizing_with_a_service_account) in the Google Cloud documentation.

### [10.5. Requirements for a cluster with user-provisioned infrastructure](#installation-requirements-user-infra_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

This section describes the requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

#### [10.5.1. Required machines for cluster installation](#installation-machine-requirements_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

Important

For a cluster that has user-provisioned infrastructure, you must deploy all of the required machines.

Expand

Table 10.5. Minimum required hosts

| Hosts | Description |
| --- | --- |
| One temporary bootstrap machine | The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster. |
| Three control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| At least two compute machines, which are also known as worker machines. | The workloads requested by OpenShift Container Platform users run on the compute machines. |

Show more

Important

To keep high availability of your cluster, use separate physical hosts for these cluster machines.

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. However, the compute machines can use Red Hat Enterprise Linux CoreOS (RHCOS), Red Hat Enterprise Linux (RHEL) 8.6 and later.

RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.8 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits).

#### [10.5.2. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 10.6. Minimum resource requirements

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Show more

* One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
* OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance.
* As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines.

Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* ppc64le architecture requires IBM® Power9 ISA
* s390x architecture requires IBM® z14 ISA

For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

#### [10.5.3. Tested instance types for Google Cloud](#installation-gcp-tested-machine-types_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

The following Google Cloud instance types have been tested with OpenShift Container Platform.

Note

Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) (Google documentation).

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see [machine series support for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in *Storage*.

See the following machine series:

* `A2`
* `A3`
* `C2`
* `C2D`
* `C3`
* `C3D`
* `C4`
* `E2`
* `M1`
* `N1`
* `N2`
* `N2D`
* `N4`
* `Tau T2D`

#### [10.5.4. Using custom machine types](#installation-custom-machine-types_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

Using a custom machine type to install a OpenShift Container Platform cluster is supported.

Consider the following when using a custom machine type:

* Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation".
* The name of the custom machine type must adhere to the following syntax:

  `custom-<number_of_cpus>-<amount_of_memory_in_mb>`

  For example, `custom-6-20480`.

### [10.6. Configuring the Google Cloud project that hosts your shared VPC network](#installation-gcp-user-infra-config-host-project-vpc_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

If you use a shared Virtual Private Cloud (VPC) to host your OpenShift Container Platform cluster in Google Cloud, you must configure the project that hosts it.

Note

If you already have a project that hosts the shared VPC network, review this section to ensure that the project meets all of the requirements to install an OpenShift Container Platform cluster.

**Procedure**

1. Create a project to host the shared VPC for your OpenShift Container Platform cluster. See [Creating and Managing Projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in the Google Cloud documentation.
2. Create a service account in the project that hosts your shared VPC. See [Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account) in the Google Cloud documentation.
3. Grant the service account the appropriate permissions. You can either grant the individual permissions that follow or assign the `Owner` role to it. See [Granting roles to a service account for specific resources](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource).

   Note

   While making the service account an owner of the project is the easiest way to gain the required permissions, it means that service account has complete control over the project. You must determine if the risk that comes from offering that power is acceptable.

   The service account for the project that hosts the shared VPC network requires the following roles:

   * Compute Network User
   * Compute Security Admin
   * Cloud Infrastructure Manager Admin
   * DNS Administrator
   * Security Admin
   * Network Management Admin

#### [10.6.1. Configuring DNS for Google Cloud](#installation-gcp-dns_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, the Google Cloud account you use must have a dedicated public hosted zone in the project that hosts the shared VPC that you install the cluster into. This zone must be authoritative for the domain. The DNS service provides cluster DNS resolution and name lookup for external connections to the cluster.

**Procedure**

1. Identify your domain, or subdomain, and registrar. You can transfer an existing domain and registrar or obtain a new one through Google Cloud or another source.

   Note

   If you purchase a new domain, it can take time for the relevant DNS changes to propagate. For more information about purchasing domains through Google, see [Google Domains](https://domains.google/).
2. Create a public hosted zone for your domain or subdomain in your Google Cloud project. See [Creating public zones](https://cloud.google.com/dns/zones/#creating_public_zones) in the Google Cloud documentation.

   Use an appropriate root domain, such as `openshiftcorp.com`, or subdomain, such as `clusters.openshiftcorp.com`.
3. Extract the new authoritative name servers from the hosted zone records. See [Look up your Cloud DNS name servers](https://cloud.google.com/dns/docs/update-name-servers#look_up_your_name_servers) in the Google Cloud documentation.

   You typically have four name servers.
4. Update the registrar records for the name servers that your domain uses. For example, if you registered your domain to Google Domains, see the following topic in the Google Domains Help: [How to switch to custom name servers](https://support.google.com/domains/answer/3290309?hl=en).
5. If you migrated your root domain to Google Cloud DNS, migrate your DNS records. See [Migrating to Cloud DNS](https://cloud.google.com/dns/docs/migrating) in the Google Cloud documentation.
6. If you use a subdomain, follow your company’s procedures to add its delegation records to the parent domain. This process might include a request to your company’s IT department or the division that controls the root domain and DNS services for your company.

### [10.7. Creating the installation files for Google Cloud](#installation-user-infra-generate_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on Google Cloud by using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use.

You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.

#### [10.7.1. Manually creating the installation configuration file](#installation-initializing-manual_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

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

#### [10.7.2. Enabling Shielded VMs](#installation-gcp-enabling-shielded-vms_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).

Note

Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use shielded VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            secureBoot: Enabled
     ```
  2. To use shielded VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            secureBoot: Enabled
     ```
  3. To use shielded VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            secureBoot: Enabled
     ```

#### [10.7.3. Enabling Confidential VMs](#installation-gcp-enabling-confidential-vms_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google’s documentation on [Confidential Computing](https://cloud.google.com/confidential-computing). You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

Note

Confidential VMs are currently not supported on 64-bit ARM architectures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use confidential VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
     ```

     1

     ```
            type: n2d-standard-8
     ```

     2

     ```
            onHostMaintenance: Terminate
     ```

     3

     [1](#CO20-1)
     :   Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional Google Cloud configuration parameters".

     [2](#CO20-2)
     :   Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see [Supported operating systems and machine types](https://cloud.google.com/compute/confidential-vm/docs/os-and-machine-type#machine-type).

     [3](#CO20-3)
     :   Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.
  2. To use confidential VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```
  3. To use confidential VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```

#### [10.7.4. Sample customized install-config.yaml file for Google Cloud](#installation-gcp-user-infra-shared-vpc-config-yaml_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can customize the `install-config.yaml` file to specify more details about your OpenShift Container Platform cluster’s platform or modify the values of the required parameters.

Important

This sample YAML file is provided for reference only. You must obtain your `install-config.yaml` file by using the installation program and modify it.

```
apiVersion: v1
baseDomain: example.com
```

1

```
controlPlane:
```

2

```
  hyperthreading: Enabled
```

3

```

```

4

```
  name: master
  platform:
    gcp:
      type: n2-standard-4
      zones:
      - us-central1-a
      - us-central1-c
      tags:
```

5

```
      - control-plane-tag1
      - control-plane-tag2
  replicas: 3
compute:
```

6

```
- hyperthreading: Enabled
```

7

```
  name: worker
  platform:
    gcp:
      type: n2-standard-4
      zones:
      - us-central1-a
      - us-central1-c
      tags:
```

8

```
      - compute-tag1
      - compute-tag2
  replicas: 0
metadata:
  name: test-cluster
networking:
  clusterNetwork:
  - cidr: 10.128.0.0/14
    hostPrefix: 23
  machineNetwork:
  - cidr: 10.0.0.0/16
  networkType: OVNKubernetes
```

9

```
  serviceNetwork:
  - 172.30.0.0/16
platform:
  gcp:
    defaultMachinePlatform:
      tags:
```

10

```
      - global-tag1
      - global-tag2
    projectID: openshift-production
```

11

```
    region: us-central1
```

12

```
pullSecret: '{"auths": ...}'
fips: false
```

13

```
sshKey: ssh-ed25519 AAAA...
```

14

```
publish: Internal
```

15

[1](#CO21-1)
:   Specify the public DNS on the host project.

[2](#CO21-2) [6](#CO21-6)
:   If you do not provide these parameters and values, the installation program provides the default value.

[3](#CO21-3) [7](#CO21-7)
:   The `controlPlane` section is a single mapping, but the compute section is a sequence of mappings. To meet the requirements of the different data structures, the first line of the `compute` section must begin with a hyphen, `-`, and the first line of the `controlPlane` section must not. Although both sections currently define a single machine pool, it is possible that future versions of OpenShift Container Platform will support defining multiple compute pools during installation. Only one control plane pool is used.

[4](#CO21-4)
:   Whether to enable or disable simultaneous multithreading, or `hyperthreading`. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores. You can disable it by setting the parameter value to `Disabled`. If you disable simultaneous multithreading in some cluster machines, you must disable it in all cluster machines.

    Important

    If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance. Use larger machine types, such as `n1-standard-8`, for your machines if you disable simultaneous multithreading.

[5](#CO21-5) [8](#CO21-8) [10](#CO21-10)
:   Optional: A set of network tags to apply to the control plane or compute machine sets. The `platform.gcp.defaultMachinePlatform.tags` parameter applies to both control plane and compute machines. If the `compute.platform.gcp.tags` or `controlPlane.platform.gcp.tags` parameters are set, they override the `platform.gcp.defaultMachinePlatform.tags` parameter.

[9](#CO21-9)
:   The cluster network plugin to install. The default value `OVNKubernetes` is the only supported value.

[11](#CO21-11)
:   Specify the main project where the VM instances reside.

[12](#CO21-12)
:   Specify the region that your VPC network is in.

[13](#CO21-13)
:   Whether to enable or disable FIPS mode. By default, FIPS mode is not enabled. If FIPS mode is enabled, the Red Hat Enterprise Linux CoreOS (RHCOS) machines that OpenShift Container Platform runs on bypass the default Kubernetes cryptography suite and use the cryptography modules that are provided with RHCOS instead.

    Important

    To enable FIPS mode for your cluster, you must run the installation program from a Red Hat Enterprise Linux (RHEL) computer configured to operate in FIPS mode. For more information about configuring FIPS mode on RHEL, see [Switching RHEL to FIPS mode](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/9/html/security_hardening/switching-rhel-to-fips-mode_security-hardening).

    When running Red Hat Enterprise Linux (RHEL) or Red Hat Enterprise Linux CoreOS (RHCOS) booted in FIPS mode, OpenShift Container Platform core components use the RHEL cryptographic libraries that have been submitted to NIST for FIPS 140-2/140-3 Validation on only the x86\_64, ppc64le, and s390x architectures.

[14](#CO21-14)
:   You can optionally provide the `sshKey` value that you use to access the machines in your cluster.

    Note

    For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.

[15](#CO21-15)
:   How to publish the user-facing endpoints of your cluster. Set `publish` to `Internal` to deploy a private cluster, which cannot be accessed from the internet. The default value is `External`. To use a shared VPC in a cluster that uses infrastructure that you provision, you must set `publish` to `Internal`. The installation program will no longer be able to access the public DNS zone for the base domain in the host project.

#### [10.7.5. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

**Prerequisites**

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

#### [10.7.6. Creating the Kubernetes manifest and Ignition config files](#installation-user-infra-generate-k8s-manifest-ignition_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

Because you manually provision infrastructure, you must generate the Kubernetes manifest and Ignition config files that the cluster requires.

The installation program converts the installation configuration into Kubernetes manifests and then wraps them into Ignition configuration files. You use these Ignition files to configure the cluster machines.

Important

* The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which the system then renews. If you shut down the cluster before the system renews the certificates and you later restart the cluster after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
* Use Ignition config files within 12 hours after you generate them, because the 24-hour certificate rotates from 16 to 22 hours after you install the cluster. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

**Procedure**

1. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```

   where:

   `<installation_directory>`
   :   Specifies the installation directory that contains the `install-config.yaml` file you created.
2. Remove the Kubernetes manifest files that define the control plane machines:

   ```
   $ rm -f <installation_directory>/openshift/99_openshift-cluster-api_master-machines-*.yaml
   ```

   By removing these files, you prevent the cluster from automatically generating control plane machines.
3. Remove the Kubernetes manifest files that define the control plane machine set:

   ```
   $ rm -f <installation_directory>/openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
   ```
4. Remove the Kubernetes manifest files that define the worker machines:

   ```
   $ rm -f <installation_directory>/openshift/99_openshift-cluster-api_worker-machineset-*.yaml
   ```

   Because you create and manage the worker machines yourself, you do not need to initialize these machines.
5. Verify that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:

   1. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.
   2. Locate the `mastersSchedulable` parameter and verify that it is set to `false`.
   3. Save and exit the file.
6. Remove the `privateZone` sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file:

   ```
   apiVersion: config.openshift.io/v1
   kind: DNS
   metadata:
     creationTimestamp: null
     name: cluster
   spec:
     baseDomain: example.openshift.com
     privateZone:
       id: mycluster-100419-private-zone
   status: {}
   ```

   `spec.privateZone`: Remove this section completely.
7. Configure the cloud provider for your VPC.

   1. Open the `<installation_directory>/manifests/cloud-provider-config.yaml` file.
   2. Add the `network-project-id` parameter and set its value to the ID of project that hosts the shared VPC network.
   3. Add the `network-name` parameter and set its value to the name of the shared VPC network that hosts the OpenShift Container Platform cluster.
   4. Replace the value of the `subnetwork-name` parameter with the value of the shared VPC subnet that hosts your compute machines.

      The contents of the `<installation_directory>/manifests/cloud-provider-config.yaml` resemble the following example:

      ```
      config: |+
        [global]
        project-id      = example-project
        regional        = true
        multizone       = true
        node-tags       = opensh-ptzzx-master
        node-tags       = opensh-ptzzx-worker
        node-instance-prefix = opensh-ptzzx
        external-instance-groups-prefix = opensh-ptzzx
        network-project-id = example-shared-vpc
        network-name    = example-network
        subnetwork-name = example-worker-subnet
      ```
8. If you deploy a cluster that is not on a private network, open the `<installation_directory>/manifests/cluster-ingress-default-ingresscontroller.yaml` file and replace the value of the `scope` parameter with `External`. The contents of the file resemble the following example:

   ```
   apiVersion: operator.openshift.io/v1
   kind: IngressController
   metadata:
     creationTimestamp: null
     name: default
     namespace: openshift-ingress-operator
   spec:
     endpointPublishingStrategy:
       loadBalancer:
         scope: External
       type: LoadBalancerService
   status:
     availableReplicas: 0
     domain: ''
     selector: ''
   ```
9. To create the Ignition configuration files, run the following command from the directory that contains the installation program:

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

### [10.8. Exporting common variables](#installation-gcp-user-infra-exporting-common-variables-vpc) Copy linkLink copied to clipboard!

#### [10.8.1. Extracting the infrastructure name](#installation-extracting-infraid_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

To identify your cluster resources in Google Cloud, extract the unique infrastructure name from the Ignition config files.

The infrastructure name is also used to locate the appropriate Google Cloud resources during an OpenShift Container Platform installation. The provided Infrastructure Manager templates contain references to this infrastructure name, so you must extract it.

Warning

Do not run the `openshift-install create manifests` command again after creating any Google Cloud resources. Running the command again generates a new cluster identifier, which will cause errors in existing resources. If you need to regenerate the manifests because you modified the `install-config.yaml` file, delete any Google Cloud resources you created and recreate them with the new cluster identifier.

**Prerequisites**

* You installed the `jq` package.

**Procedure**

* To extract and view the infrastructure name from the Ignition config file metadata, run the following command:

  ```
  $ jq -r .infraID <installation_directory>/metadata.json
  ```

  where `<installation_directory>` is the path to the directory that you stored the installation files in.

  **Example output**

  ```
  openshift-vw9j6
  ```

  The output of this command is your cluster name and a random string.

#### [10.8.2. Exporting common variables for Infrastructure Manager templates](#installation-user-infra-exporting-common-variables_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must export a common set of variables that are used with the provided Infrastructure Manager templates used to assist in installing a cluster with user-provisioned infrastructure on Google Cloud.

Note

Specific Infrastructure Manager templates can also require additional exported variables, which are detailed in their related procedures.

**Procedure**

* Export the following common variables to be used by the provided Infrastructure Manager templates. For any command with `<installation_directory>`, specify the path to the directory that you stored the installation files in.

  + Export the `BASE_DOMAIN` variable by running the following command:

    ```
    $ export BASE_DOMAIN='<base_domain>'
    ```

    `<base_domain>`
    :   If you are installing a cluster into a shared VPC, specify the value for the host project.
  + Export the `BASE_DOMAIN_ZONE_NAME` variable by running the following command:

    ```
    $ export BASE_DOMAIN_ZONE_NAME='<base_domain_zone_name>'
    ```

    `<base_domain_zone_name>`
    :   Specifies the base domain zone name.
  + Export the `NETWORK_CIDR` variable by running the following command:

    ```
    $ export NETWORK_CIDR='<network_cidr>'
    ```

    `<network_cidr>`
    :   Specifies the network CIDR your cluster uses. For example, `10.0.0.0/16`.
  + Export the `MASTER_SUBNET_CIDR` variable by running the following command:

    ```
    $ export MASTER_SUBNET_CIDR='<master_subnet_cidr>'
    ```

    `<master_subnet_cidr>`
    :   Specifies the network CIDR that your cluster’s control plane uses. For example, `10.0.0.0/17`.
  + Export the `WORKER_SUBNET_CIDR` variable by running the following command:

    ```
    $ export WORKER_SUBNET_CIDR='<worker_subnet_cidr>'
    ```

    `<worker_subnet_cidr>`
    :   Specifies the network CIDR that your cluster’s compute machines use. For example, `10.0.128.0/17`.
  + Export the `KUBECONFIG` variable by running the following command:

    ```
    $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
    ```
  + Export the `CLUSTER_NAME` variable by running the following command:

    ```
    $ export CLUSTER_NAME=`jq -r .clusterName <installation_directory>/metadata.json`
    ```
  + Export the `INFRA_ID` variable by running the following command:

    ```
    $ export INFRA_ID=`jq -r .infraID <installation_directory>/metadata.json`
    ```
  + Export the `PROJECT_NAME` variable by running the following command:

    ```
    $ export PROJECT_NAME=`jq -r .gcp.projectID <installation_directory>/metadata.json`
    ```
  + If you are installing a cluster into a shared VPC, export the `HOST_PROJECT` variable by running the following command:

    ```
    $ export HOST_PROJECT=<host_project_name>
    ```

    `<host_project_name>` specifies the name of the host project that contains the shared VPC.
  + If you are installing a cluster into a shared VPC, export the `HOST_PROJECT_ACCOUNT` variable by running the following command:

    ```
    $ export HOST_PROJECT_ACCOUNT=<host_project_account>
    ```

    `<host_project_account>` specifies the name of an account that can access the host project that contains the shared VPC.
  + Export the `REGION` variable by running the following command:

    ```
    $ export REGION=`jq -r .gcp.region <installation_directory>/metadata.json`
    ```
  + Export the `ZONE_0` variable by running the following command:

    ```
    $ export ZONE_0=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[0]' | cut -d "/" -f9)
    ```
  + Export the `ZONE_1` variable by running the following command:

    ```
    $ export ZONE_1=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[1]' | cut -d "/" -f9)
    ```
  + Export the `ZONE_2` variable by running the following command:

    ```
    $ export ZONE_2=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[2]' | cut -d "/" -f9)
    ```
  + Export the `SERVICE_ACCOUNT_EMAIL` variable by running the following command:

    ```
    $ export SERVICE_ACCOUNT_EMAIL="<service_account_email>"
    ```

    `<service_account_email>`
    :   Specifies the email address of the service account you used for the installation.
  + Export the `INSTALL_SERVICE_ACCOUNT` variable by running the following command:

    ```
    $ export INSTALL_SERVICE_ACCOUNT="projects/${PROJECT_NAME}/serviceAccounts/${SERVICE_ACCOUNT_EMAIL}"
    ```
  + Export the `CLUSTER_DOMAIN` variable by running the following command:

    ```
    $ export CLUSTER_DOMAIN="${CLUSTER_NAME}.${BASE_DOMAIN}"
    ```

### [10.9. Networking requirements for user-provisioned infrastructure](#installation-network-user-infra_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files.

#### [10.9.1. Setting the cluster node hostnames through DHCP](#installation-host-names-dhcp-user-infra_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

On Red Hat Enterprise Linux CoreOS (RHCOS) machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start prior to this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node.

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation.

#### [10.9.2. Network connectivity requirements](#installation-network-connectivity-user-infra_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster.

This section provides details about the ports that are required.

Important

In connected OpenShift Container Platform environments, all nodes are required to have internet access to pull images for platform containers and provide telemetry data to Red Hat.

Expand

Table 10.7. Ports used for all-machine to all-machine communications

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

Table 10.8. Ports used for all-machine to control plane communications

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | `6443` | Kubernetes API |

Show more

Expand

Table 10.9. Ports used for control plane machine to control plane machine communications

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | `2379`-`2380` | etcd server and peer ports |

Show more

### [10.10. Creating load balancers in Google Cloud](#installation-creating-gcp-lb_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must configure load balancers in Google Cloud for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* You have defined the variables in the *Exporting common variables* section.
* If you are not installing a cluster into a shared VPC, you have defined the variables in the *Creating a VPC in Google Cloud* section.

**Procedure**

1. If you are installing a cluster into a shared VPC, set environment variables for the cluster network and control plane subnet.

   1. Determine the shared VPC network name by running the following command:

      ```
      $ gcloud compute networks list
      ```
   2. Set the `CLUSTER_NETWORK` variable by running the following command:

      ```
      $ export CLUSTER_NETWORK=$(gcloud compute networks describe <network_name> --format json | jq -r .selfLink)
      ```

      `<network_name>` specifies the name of the network you determined.
   3. List the available network subnets by running the following command:

      ```
      $ gcloud compute networks subnets list --network=<network_name>
      ```

      `<network_name>` specifies the name of the network you determined.
   4. Select a subnet from the list, and set the `CONTROL_SUBNET` variable by running the following command:

      ```
      $ export CONTROL_SUBNET=<control_subnet>
      ```

      `<control_subnet>` specifies the name of the subnet you selected from the list of subnets.
2. Copy the template from the **Infrastructure Manager template for the internal load balancer** section of this topic and save it as `02_lb_int.tf` in a directory called `02_lb_int` on your computer. This template describes the internal load balancing objects that your cluster requires.

   1. Create an internal load balancer by running the following command:

      ```
      $ gcloud infra-manager deployments apply <internal_lb_deployment_name> \
        --location=${REGION} \
        --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_network=${CLUSTER_NETWORK},control_subnet=${CONTROL_SUBNET},zone_0=${ZONE_0},zone_1=${ZONE_1},zone_2=${ZONE_2} \
        --project=${PROJECT_NAME} \
        --local-source=./02_lb_int \
        --service-account=${INSTALL_SERVICE_ACCOUNT}
      ```

      `<internal_lb_deployment_name>` specifies the name of the internal load balancer deployment you create.
   2. Export the `CLUSTER_IP` variable by running the following command:

      ```
      $ export CLUSTER_IP=$(gcloud compute addresses describe ${INFRA_ID}-cluster-ip --region=${REGION} --format json | jq -r .address)
      ```
3. Optional: For a public or externally available cluster, copy the template from the **Infrastructure Manager template for the external load balancer** section of this topic and save it as `02_lb_ext.tf` in a directory called `02_lb_ext` on your computer. This template describes the external load balancing objects that your cluster requires.

   1. Create an external load balancer by running the following command:

      ```
      $ gcloud infra-manager deployments apply <external_lb_deployment_name> \
        --location=${REGION} \
        --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION} \
        --project=${PROJECT_NAME} \
        --local-source=./02_lb_ext \
        --service-account=${INSTALL_SERVICE_ACCOUNT}
      ```

      `<external_lb_deployment_name>` specifies the name of the external load balancer deployment you create.
   2. Export the `CLUSTER_PUBLIC_IP` variable by running the following command:

      ```
      $ export CLUSTER_PUBLIC_IP=$(gcloud compute addresses describe ${INFRA_ID}-cluster-public-ip --region=${REGION} --format json | jq -r .address)
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [10.10.1. Infrastructure Manager template for the external load balancer](#installation-infrastructure-manager-ext-lb_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the external load balancer that you need for your OpenShift Container Platform cluster:

**Example 10.1. `02_lb_ext.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}
variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}
variable "project" {
  type        = string
  description = "Project ID"
}
variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

resource "google_compute_address" "cluster_public_ip" {
  provider = google-beta

  name = "${var.infra_id}-cluster-public-ip"
  region = "${var.region}"
}

resource "google_compute_http_health_check" "api_http_health_check" {
  provider = google-beta

  name = "${var.infra_id}-api-http-health-check"
  port = 6080
  request_path = "/readyz"
}

resource "google_compute_target_pool" "api_target_pool" {
  provider = google-beta

  name = "${var.infra_id}-api-target-pool"
  region = "${var.region}"
  health_checks = [
    google_compute_http_health_check.api_http_health_check.id
  ]
}

resource "google_compute_forwarding_rule" "api_forwarding_rule" {
  provider = google-beta

  name = "${var.infra_id}-api-forwarding-rule"
  ip_address = google_compute_address.cluster_public_ip.address
  port_range = "6443"
  region = "${var.region}"
  target = google_compute_target_pool.api_target_pool.id
}
```

#### [10.10.2. Infrastructure Manager template for the internal load balancer](#installation-infrastructure-manager-int-lb_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the internal load balancer that you need for your OpenShift Container Platform cluster:

**Example 10.2. `02_lb_int.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}
variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}
variable "project" {
  type        = string
  description = "Project ID"
}
variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}
variable "control_subnet" {
  type        = string
  description = "Subnet for the control plane instances."
}
variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

# Terraform handles lists but the infra-manager --input-values only
# supports scalar types.
# If you require more or less zones, you must manually add them below
# as a single variable for each. You must add the zones to the
# locals `zones` list below.
variable "zone_0" {
  type        = string
  description = "Zone 1 for the instance types."
}

variable "zone_1" {
  type        = string
  description = "Zone 2 for the instance types."
}

variable "zone_2" {
  type        = string
  description = "Zone 3 for the instance types."
}

locals {
  zones = ["${var.zone_0}", "${var.zone_1}", "${var.zone_2}"]
}

resource "google_compute_address" "cluster_ip" {
  provider = google-beta

  name = "${var.infra_id}-cluster-ip"
  address_type = "INTERNAL"
  region = "${var.region}"
  subnetwork = "${var.control_subnet}"
}

resource "google_compute_health_check" "api_internal_health_check" {
  provider = google-beta

  name = "${var.infra_id}-api-internal-health-check"
  https_health_check {
    port = 6443
  }
}

resource "google_compute_region_backend_service" "api_internal" {
  provider = google-beta

  name = "${var.infra_id}-api-internal"
  timeout_sec = 120
  protocol = "TCP"
  region = "${var.region}"
  load_balancing_scheme = "INTERNAL"
  health_checks = [
    google_compute_health_check.api_internal_health_check.id
  ]

  dynamic "backend" {
    for_each = google_compute_instance_group.master_ig

    content {
      balancing_mode = "CONNECTION"
      group = backend.value.self_link
    }
  }
}

resource "google_compute_forwarding_rule" "api_internal_forwarding_rule" {
  provider = google-beta

  name = "${var.infra_id}-api-internal-forwarding-rule"
  ip_address = google_compute_address.cluster_ip.address
  backend_service = google_compute_region_backend_service.api_internal.id
  load_balancing_scheme = "INTERNAL"
  ports = [
    "6443",
    "22623"
  ]
  region = "${var.region}"
  subnetwork = "${var.control_subnet}"
}

resource "google_compute_instance_group" "master_ig" {
  provider = google-beta

  for_each = toset(local.zones)

  name = "${var.infra_id}-master-${each.key}-ig"
  network = "${var.cluster_network}"
  zone = "${each.key}"
  named_port {
    name = "ignition"
    port = 22623
  }
  named_port {
    name = "https"
    port = 6443
  }
}
```

### [10.11. Creating a private DNS zone in Google Cloud](#installation-creating-gcp-private-dns_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must configure a private DNS zone in Google Cloud for your OpenShift Container Platform cluster to use. One way to create this component is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for the private DNS** section of this topic and save it as `02_dns.tf` in a folder called `02_dns` on your computer. This template describes the private DNS objects that your cluster requires.
2. If you are installing a cluster into a shared VPC, and the host project already has a private DNS zone, skip this step. Create the DNS zone by running the following command:

   ```
   $ gcloud infra-manager deployments apply <dns_zone_deployment_name> \
     --location=${REGION} \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_domain=${CLUSTER_DOMAIN},cluster_network=${CLUSTER_NETWORK} \
     --project=${PROJECT_NAME} \
     --local-source=./02_dns \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<dns_zone_deployment_name>` specifies the name of the DNS zone deployment you create.
3. The templates do not create DNS entries due to limitations of Infrastructure Manager, so you must create them manually:

   1. Add the internal DNS entries by running the following commands:

      ```
      $ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
      ```

      ```
      $ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
      ```

      ```
      $ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
      ```

      ```
      $ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api-int.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
      ```

      ```
      $ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
      ```
   2. For an external cluster, also add the external DNS entries by running the following commands:

      ```
      $ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
      ```

      ```
      $ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
      ```

      ```
      $ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} dns record-sets transaction add ${CLUSTER_PUBLIC_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
      ```

      ```
      $ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [10.11.1. Infrastructure Manager template for the private DNS](#installation-infrastructure-manager-private-dns_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the private DNS that you need for your OpenShift Container Platform cluster:

**Example 10.3. `02_dns.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "cluster_domain" {
  type        = string
  description = "ClusterName.BaseDomain"
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

resource "google_dns_managed_zone" "private_zone" {
  provider = google-beta

  name = "${var.infra_id}-private-zone"
  dns_name = "${var.cluster_domain}."
  description = "OpenShift Installer UPI create private DNS zone."
  visibility = "private"
  private_visibility_config {
    networks {
      network_url = "${var.cluster_network}"
    }
  }

  force_destroy = false
}
```

### [10.12. Creating firewall rules and IAM roles in Google Cloud](#installation-creating-gcp-firewall-rules-vpc_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must create firewall rules and IAM roles in Google Cloud for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Infrastructure Manager template. If you are installing a cluster into a shared VPC and the host project already has the necessary firewall rules and IAM roles, you can skip creating these resources.

Note

If you do not use the provided Infrastructure Manager template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for firewall rules and IAM roles** section of this topic and save it as `03_security.tf` in a folder called `03_security` on your computer. This template describes the security groups that your cluster requires.
2. Create the firewall rules and IAM roles by running the following command:

   ```
   $ gcloud infra-manager deployments apply <security_deployment_name> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./03_security \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_network=${CLUSTER_NETWORK},network_cidr=${NETWORK_CIDR} \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<security_deployment_name>` specifies the name of the deployment of firewall rules and IAM roles.
3. Configure service account variables based on the roles you created by running the following commands:

   ```
   $ export MASTER_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter "email~^${INFRA_ID}-m@${PROJECT_NAME}." --format json | jq -r '.[0].email')
   ```

   ```
   $ export WORKER_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter "email~^${INFRA_ID}-w@${PROJECT_NAME}." --format json | jq -r '.[0].email')
   ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [10.12.1. Infrastructure Manager template for firewall rules and IAM roles](#installation-infrastructure-manager-firewall-rules_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the firewall rules and IAM roles that you need for your OpenShift Container Platform cluster:

**Example 10.4. `03_security.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

variable "network_cidr" {
  type        = string
  description = "CIDR for network of the cluster."
}

variable "allowed_external_cidr" {
  type        = string
  description = "Allowed external CIDR for firewall rule."
  default     = "0.0.0.0/0"
}

resource "google_compute_firewall" "bootstrap_in_ssh" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap-in-ssh"
  source_ranges = [
    "${var.allowed_external_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-bootstrap"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["22"]
  }
}

resource "google_compute_firewall" "api" {
  provider = google-beta

  name = "${var.infra_id}-api"
  source_ranges = [
   "${var.allowed_external_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["6443"]
  }
}

resource "google_compute_firewall" "health_checks" {
  provider = google-beta

  name = "${var.infra_id}-health-checks"
  source_ranges = [
    "35.191.0.0/16",
    "130.211.0.0/22",
    "209.85.152.0/22",
    "209.85.204.0/22"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["6080", "6443", "22624"]
  }
}

resource "google_compute_firewall" "etcd" {
  provider = google-beta

  name = "${var.infra_id}-etcd"
  source_tags = [
    "${var.infra_id}-master"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["2379-2380"]
  }
}

resource "google_compute_firewall" "control_plane" {
  provider = google-beta

  name = "${var.infra_id}-control-plane"
  source_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["10257"]
  }
  allow {
    protocol = "tcp"
    ports = ["10259"]
  }
  allow {
    protocol = "tcp"
    ports = ["22623"]
  }
}

resource "google_compute_firewall" "internal_network" {
  provider = google-beta

  name = "${var.infra_id}-internal-network"
  source_ranges = [
    "${var.network_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "icmp"
  }
  allow {
    protocol = "tcp"
    ports = ["22"]
  }
}

resource "google_compute_firewall" "internal_cluster" {
  provider = google-beta

  name = "${var.infra_id}-internal-cluster"
  source_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  target_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "udp"
    ports = ["4789", "6081"]
  }
  allow {
    protocol = "udp"
    ports = ["500", "4500"]
  }
  allow {
    protocol = "esp"
  }
  allow {
    protocol = "tcp"
    ports = ["9000-9999"]
  }
  allow {
    protocol = "udp"
    ports = ["9000-9999"]
  }
  allow {
    protocol = "tcp"
    ports = ["10250"]
  }
  allow {
    protocol = "tcp"
    ports = ["30000-32767"]
  }
  allow {
    protocol = "udp"
    ports = ["30000-32767"]
  }
}

resource "google_service_account" "master_node_sa" {
  provider = google-beta

  account_id = "${var.infra_id}-m"
  display_name = "${var.infra_id}-master-node"
}

resource "google_service_account" "worker_node_sa" {
  provider = google-beta

  account_id = "${var.infra_id}-w"
  display_name = "${var.infra_id}-worker-node"
}
```

### [10.13. Creating IAM policy bindings in Google Cloud](#installation-creating-gcp-iam-shared-vpc_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must create IAM policy bindings in Google Cloud for your OpenShift Container Platform cluster to use.

**Prerequisites**

* You have defined the variables in the *Exporting common variables* section.

**Procedure**

1. Assign the permissions that the installation program requires to the service accounts for the subnets that host the control plane and compute subnets:

   1. Grant the `networkViewer` role of the project that hosts your shared VPC to the master service account by running the following command:

      ```
      $ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} projects add-iam-policy-binding ${HOST_PROJECT} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkViewer"
      ```
   2. Grant the `networkUser` role to the master service account for the control plane subnet by running the following command:

      ```
      $ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} compute networks subnets add-iam-policy-binding "${HOST_PROJECT_CONTROL_SUBNET}" --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkUser" --region ${REGION}
      ```
   3. Grant the `networkUser` role to the worker service account for the control plane subnet by running the following command:

      ```
      $ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} compute networks subnets add-iam-policy-binding "${HOST_PROJECT_CONTROL_SUBNET}" --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/compute.networkUser" --region ${REGION}
      ```
   4. Grant the `networkUser` role to the master service account for the compute subnet by running the following command:

      ```
      $ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} compute networks subnets add-iam-policy-binding "${HOST_PROJECT_COMPUTE_SUBNET}" --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkUser" --region ${REGION}
      ```
   5. Grant the `networkUser` role to the worker service account for the compute subnet by running the following command:

      ```
      $ gcloud --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT} compute networks subnets add-iam-policy-binding "${HOST_PROJECT_COMPUTE_SUBNET}" --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/compute.networkUser" --region ${REGION}
      ```
2. The templates do not create the policy bindings due to limitations of Infrastructure Manager, so you must create them manually by running the following commands:

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.instanceAdmin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkAdmin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.securityAdmin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/iam.serviceAccountUser"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/storage.admin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/compute.viewer"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/storage.admin"
   ```
3. Create a service account key and store it locally for later use by running the following command:

   ```
   $ gcloud iam service-accounts keys create service-account-key.json --iam-account=${MASTER_SERVICE_ACCOUNT}
   ```

### [10.14. Creating the RHCOS cluster image for the Google Cloud infrastructure](#installation-gcp-user-infra-rhcos_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must use a valid Red Hat Enterprise Linux CoreOS (RHCOS) image for Google Cloud for your OpenShift Container Platform nodes.

**Prerequisites**

* You have downloaded the `openshift-install` binary.

**Procedure**

1. Obtain the image name by running the following command:

   ```
   $ source_image=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.gcp.name')
   ```
2. Obtain the project name by running the following command:

   ```
   $ source_project=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.gcp.project')
   ```
3. Create the image by running the following command:

   ```
   $ gcloud compute images create "${INFRA_ID}-rhcos-image" \
       --source-image="${source_image}" --source-image-project="${source_project}"
   ```

### [10.15. Creating the bootstrap machine in Google Cloud](#installation-creating-gcp-bootstrap_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must create the bootstrap machine in Google Cloud to use during OpenShift Container Platform cluster initialization. One way to create this machine is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided Infrastructure Manager template to create your bootstrap machine, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

If you need to redeploy the bootstrap machine for any reason, delete the existing bootstrap VM first. If you redeploy the bootstrap machine without deleting the existing VM, Infrastructure Manager will update the metadata and appear to succeed, but the Ignition file will not be executed again. This will result in the VM still being based on the old Ignition data.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for the bootstrap machine** section of this topic and save it as `04_bootstrap.tf` in a folder called `04_bootstrap` on your computer. This template describes the bootstrap machine that your cluster requires.

   * You can edit the `04_bootstrap.tf` file to add additional tags to the bootstrap machine, by modifying the existing `tags` stanza as follows:

     ```
     resource "google_compute_instance" "bootstrap" {
     # ...
       tags = [
         "${var.infra_id}-master",
         "${var.infra_id}-bootstrap",
         "custom-tag-example"
       ]
     # ...
     }
     ```
2. Export the location of the Red Hat Enterprise Linux CoreOS (RHCOS) image that the installation program requires by running the following command:

   ```
   $ export CLUSTER_IMAGE=(`gcloud compute images describe ${INFRA_ID}-rhcos-image --format json | jq -r .selfLink`)
   ```
3. Create a bucket by running the following command:

   ```
   $ gcloud storage buckets create "gs://${INFRA_ID}-bootstrap-ignition"
   ```
4. Upload the `bootstrap.ign` file by running the following command:

   ```
   $ gcloud storage cp bootstrap.ign "gs://${INFRA_ID}-bootstrap-ignition/"
   ```
5. Create a signed URL for the bootstrap instance and export the URL from the output as a variable by running the following command:

   ```
   $ export BOOTSTRAP_IGN="$(gcloud storage sign-url --duration=2h --private-key-file=service-account-key.json "gs://${INFRA_ID}-bootstrap-ignition/bootstrap.ign" | grep "^signed_url:" | awk '{print $2}')"
   ```
6. Create the bootstrap deployment by running the following command:

   ```
   $ gcloud infra-manager deployments apply <bootstrap_deployment_name> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./04_bootstrap \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone=${ZONE_0},cluster_network=${CLUSTER_NETWORK},subnet=${CONTROL_SUBNET},image=${CLUSTER_IMAGE},bootstrap_ign="${BOOTSTRAP_IGN}",is_public_cluster=<public_cluster_status> \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   where:

   `<bootstrap_deployment_name>`
   :   Specifies the name of the bootstrap deployment.

   `<public_cluster_status>`
   :   Specifies whether the cluster is public or private. If it is a public cluster, specify `true`. If it is a private cluster, specify `false`.
7. The templates do not manage load balancer membership due to limitations of Infrastructure Manager, so you must add the bootstrap machine manually.

   1. Add the bootstrap instance to the internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances \
          ${INFRA_ID}-bootstrap-ig --zone=${ZONE_0} --instances=${INFRA_ID}-bootstrap
      ```
   2. Add the bootstrap instance group to the internal load balancer backend service by running the following command:

      ```
      $ gcloud compute backend-services add-backend \
          ${INFRA_ID}-api-internal --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [10.15.1. Infrastructure Manager template for the bootstrap machine](#installation-infrastructure-manager-bootstrap_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the bootstrap machine that you need for your OpenShift Container Platform cluster:

**Example 10.5. `04_bootstrap.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "zone" {
  type        = string
  description = "Zone inside of the region where the bootstrap node is created."
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

variable "subnet" {
  type        = string
  description = "Control plane subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the bootstrap machine."
  default     = "n1-standard-4"
}

variable "root_volume_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "bootstrap_ign" {
  type        = string
  description = "Bootstrap ignition data."
}

variable "is_public_cluster" {
  type        = bool
  default     = true
  description = "Whether the publish policy is the default External"
}

resource "google_compute_address" "bootstrap_public_ip" {
  provider = google-beta
  count = var.is_public_cluster ? 1 : 0

  name = "${var.infra_id}-bootstrap-public-ip"
  region = "${var.region}"
}

resource "google_compute_instance" "bootstrap" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap"
  zone = "${var.zone}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-bootstrap"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.root_volume_size}"
      image = "${var.image}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"

    # Dynamic block to conditionally create access_config
    dynamic "access_config" {
      for_each = var.is_public_cluster ? [1] : []
      content {
        nat_ip = google_compute_address.bootstrap_public_ip[0].address
      }
    }
  }
  metadata = {
    user-data = "{\"ignition\":{\"config\":{\"replace\":{\"source\":\"${var.bootstrap_ign}\"}},\"version\":\"3.2.0\"}}"
  }
}

resource "google_compute_instance_group" "bootstrap_ig" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap-ig"
  network = "${var.cluster_network}"
  zone = "${var.zone}"
  named_port {
    name = "ignition"
    port = 22623
  }
  named_port {
    name = "https"
    port = 6443
  }
}
```

### [10.16. Creating the control plane machines in Google Cloud](#installation-creating-gcp-control-plane_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You must create the control plane machines in Google Cloud for your cluster to use. One way to create these machines is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided template to create your control plane machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* You defined the variables in the *Exporting common variables*, *Creating load balancers in Google Cloud*, *Creating IAM roles in Google Cloud*, and *Creating the bootstrap machine in Google Cloud* sections.
* You created the bootstrap machine.
* You created the Ignition configuration files.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for control plane machines** section of this topic and save it as `05_control_plane.tf` in a folder called `05_control_plane` on your computer. This template describes the control plane machines that your cluster requires.

   * You can edit the `05_control_plane.tf` file to add additional tags to the control plane machines, by modifying the existing `tags` stanza. The following example adds a custom tag to the first control plane machine, which is named `master_0`:

     ```
     resource "google_compute_instance" "master_0" {
     # ...
       tags = [
         "${var.infra_id}-master",
         "custom_tag_example"
       ]
     # ...
     }
     ```
2. Copy the `master.ign` file from your installation directory into the `05_control_plane` folder by running the following command:

   ```
   $ cp <installation_directory>/master.ign 05_control_plane/master.ign
   ```

   `<installation_directory>` specifies the directory where you created the Ignition configuration files.
3. Create the control plane deployment by running the following command:

   ```
   $ gcloud infra-manager deployments apply <control_plane_deployment> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./05_control_plane \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone_0=${ZONE_0},zone_1=${ZONE_1},zone_2=${ZONE_2},subnet=${CONTROL_SUBNET},image=${CLUSTER_IMAGE},service_account_email=${MASTER_SERVICE_ACCOUNT} \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<control_plane_deployment>` specifies the name of the control plane deployment.
4. Delete the temporary ignition file from the `05_control_plane` folder by running the following command:

   ```
   $ rm 05_control_plane/master.ign
   ```
5. The templates do not manage load balancer membership due to limitations of Infrastructure Manager, so you must add the control plane machines manually.

   1. Add the first control plane machine to an internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_0}-ig --zone=${ZONE_0} --instances=${INFRA_ID}-master-0
      ```
   2. Add the second control plane machine to an internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_1}-ig --zone=${ZONE_1} --instances=${INFRA_ID}-master-1
      ```
   3. Add the third control plane machine to an internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_2}-ig --zone=${ZONE_2} --instances=${INFRA_ID}-master-2
      ```
6. For an external cluster, you must also add the control plane machines to external load balancer target pools.

   1. Add the first control plane machine to an external load balancer pool by running the following command:

      ```
      $ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_0}" --instances=${INFRA_ID}-master-0
      ```
   2. Add the second control plane machine to an external load balancer pool by running the following command:

      ```
      $ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_1}" --instances=${INFRA_ID}-master-1
      ```
   3. Add the third control plane machine to an external load balancer pool by running the following command:

      ```
      $ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_2}" --instances=${INFRA_ID}-master-2
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [10.16.1. Infrastructure Manager template for control plane machines](#installation-infrastructure-manager-control-plane_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the control plane machines that you need for your OpenShift Container Platform cluster:

**Example 10.6. `05_control_plane.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
    local = {
        source = "hashicorp/local",
        version = ">= 2.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

# Terraform handles lists but the infra-manager --input-values only
# supports scalar types.
# If you require more or less zones, you must manually add them below
# as a single variable for each. You must add the zones to the
# locals `zones` list below.
variable "zone_0" {
  type        = string
  description = "Zone 1 for the instance types."
}

variable "zone_1" {
  type        = string
  description = "Zone 2 for the instance types."
}

variable "zone_2" {
  type        = string
  description = "Zone 3 for the instance types."
}

variable "subnet" {
  type        = string
  description = "Control plane subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the control plane machine."
  default     = "n1-standard-4"
}

variable "disk_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "disk_type" {
  type        = string
  description = "Type of storage disk for the vm."
  default     = "pd-ssd"
}

variable "service_account_email" {
  type        = string
  description = "Email for the service account attached to the control planes."
}

data "local_file" "ignition_file" {
  filename = "${path.module}/master.ign"
}

resource "google_compute_instance" "master_0" {
  provider = google-beta

  name = "${var.infra_id}-master-0"
  zone = "${var.zone_0}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

resource "google_compute_instance" "master_1" {
  provider = google-beta

  name = "${var.infra_id}-master-1"
  zone = "${var.zone_1}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

resource "google_compute_instance" "master_2" {
  provider = google-beta

  name = "${var.infra_id}-master-2"
  zone = "${var.zone_2}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}
```

### [10.17. Creating additional worker machines in Google Cloud](#installation-creating-gcp-worker_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can create worker machines in Google Cloud for your cluster by using the Infrastructure Manager template. You can adjust the number of machines by modifying the number of `google_compute_instance` resources in the provided template.

Note

If you do not use the provided Infrastructure Manager template to create your compute machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

If you are installing a three-node cluster, skip this step. A three-node cluster consists of three control plane machines, which also act as compute machines.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables*, *Creating load balancers in Google Cloud*, and *Creating the bootstrap machine in Google Cloud* sections.
* Create the bootstrap machine.
* Create the control plane machines.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for worker machines** section of this topic and save it as `06_worker.tf` in a folder called `06_worker` on your computer. This template describes the worker machines that your cluster requires.

   * You can edit the `06_worker.tf` file to add additional tags to the compute machines, by modifying the existing `tags` stanza as follows:

     ```
     resource "google_compute_instance" "worker_0" {
     # ...
       tags = [
         "${var.infra_id}-worker-0",
         "custom-tag-example"
       ]
     # ...
     }
     ```
2. Copy the `worker.ign` file from your installation directory into the `06_worker` folder by running the following command:

   ```
   $ cp <installation_directory>/worker.ign 06_worker/worker.ign
   ```

   `<installation_directory>` specifies the directory where you created the Ignition configuration files.
3. Create the deployment by running the following command:

   ```
   $ gcloud infra-manager deployments apply <worker_deployment_name> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./06_worker \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone_0=${ZONE_0},zone_1=${ZONE_1},subnet=${COMPUTE_SUBNET},image=${CLUSTER_IMAGE},service_account_email=${WORKER_SERVICE_ACCOUNT} \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<worker_deployment_name>` specifies the name of the deployment.
4. Remove the `worker.ign` file by running the following command:

   ```
   $ rm 06_worker/worker.ign
   ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [10.17.1. Infrastructure Manager template for worker machines](#installation-infrastructure-manager-worker_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the worker machines that you need for your OpenShift Container Platform cluster:

**Example 10.7. `06_worker.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

# Terraform handles lists but the infra-manager --input-values only
# supports scalar types.
# If you require more or less zones, you must manually add them below
# as a single variable for each. You must add the zones to the
# locals `zones` list below.
variable "zone_0" {
  type        = string
  description = "Zone 1 for the instance types."
}

variable "zone_1" {
  type        = string
  description = "Zone 2 for the instance types."
}

variable "subnet" {
  type        = string
  description = "Compute subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the compute machine."
  default     = "n1-standard-4"
}

variable "disk_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "disk_type" {
  type        = string
  description = "Type of storage disk for the vm."
  default     = "pd-ssd"
}

variable "service_account_email" {
  type        = string
  description = "Email for the service account attached to the compute nodes."
}

data "local_file" "ignition_file" {
  filename = "${path.module}/worker.ign"
}

resource "google_compute_instance" "worker_0" {
  provider = google-beta

  name = "${var.infra_id}-worker-0"
  zone = "${var.zone_0}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-worker"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

resource "google_compute_instance" "worker_1" {
  provider = google-beta

  name = "${var.infra_id}-worker-1"
  zone = "${var.zone_1}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-worker"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}
```

### [10.18. Removing bootstrap resources in Google Cloud](#installation-gcp-user-infra-wait-for-bootstrap_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

After you create all of the required infrastructure in Google Cloud, wait for the bootstrap process to complete on the machines that you provisioned by using the Ignition config files. The installation program created the Ignition config files.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.
* Create the bootstrap machine.
* Create the control plane machines.

**Procedure**

1. Change to the directory that includes the installation program and run the following command:

   ```
   $ ./openshift-install wait-for bootstrap-complete --dir <installation_directory> \
   ```

   1

   ```
       --log-level info
   ```

   2

   [1](#CO22-1)
   :   For `<installation_directory>`, specify the path to the directory where you stored the installation files.

   [2](#CO22-2)
   :   To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

   If the command exits without a `FATAL` warning, your production control plane has initialized.
2. To remove the bootstrap instance group from the backend services' backends, run the following commands:

   ```
   $ gcloud compute backend-services remove-backend ${INFRA_ID}-api-internal --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
   ```

   ```
   $ ingress_backendservice=$(gcloud compute backend-services list --filter="backends.group~${INFRA_ID}" --format='value(name)' | grep -v "${INFRA_ID}")
   ```

   1. If `ingress_backendservice` is not empty, run the following `describe` command for the bootstrap group:

      ```
      $ gcloud compute backend-services describe ${ingress_backendservice} --region=${REGION}
      ```
   2. If the `describe` command displays that the bootstrap group is one of its backends, run the following `remove-backend` command to remove the bootstrap group from the backends:

      ```
      $ gcloud compute backend-services remove-backend ${ingress_backendservice} --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
      ```
   3. To remove the bucket and the deployment, run the following commands:

      ```
      $ gcloud storage rm "gs://${INFRA_ID}-bootstrap-ignition/bootstrap.ign"
      ```

      ```
      $ gcloud storage rm --recursive "gs://${INFRA_ID}-bootstrap-ignition/"
      ```

      ```
      $ gcloud infra-manager deployments delete <bootstrap_deployment_name> \
          --project=${PROJECT_NAME} --location=${REGION} --quiet
      ```

      Specify the name of the bootstrap deployment you created for `<bootstrap_deployment_name>`.

### [10.19. Installing the OpenShift CLI on Linux](#cli-installing-cli-linux_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

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

### [10.20. Installing the OpenShift CLI on Windows](#cli-installing-cli-windows_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

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

### [10.21. Installing the OpenShift CLI on macOS](#cli-installing-cli-macos_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

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

### [10.22. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and OpenShift Container Platform generates it during installation.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* Ensure the bootstrap process completed successfully.

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

### [10.23. Approving the certificate signing requests for your machines](#installation-approve-csrs_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

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

### [10.24. Adding the ingress DNS records](#installation-gcp-user-infra-adding-ingress_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

DNS zone configuration is removed when creating Kubernetes manifests and generating Ignition configs. You must manually create DNS records that point at the ingress load balancer. You can create either a wildcard `*.apps.{baseDomain}.` or specific records. You can use A, CNAME, and other records per your requirements.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* section.
* Remove the DNS Zone configuration when creating Kubernetes manifests and generating Ignition configs.
* Ensure the bootstrap process completed successfully.

**Procedure**

1. Wait for the Ingress router to create a load balancer and populate the `EXTERNAL-IP` field:

   ```
   $ oc -n openshift-ingress get service router-default
   ```

   **Example output**

   ```
   NAME             TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)                      AGE
   router-default   LoadBalancer   172.30.18.154   35.233.157.184   80:32288/TCP,443:31215/TCP   98
   ```
2. Add the A record to your zones:

   * To use A records:

     1. Export the variable for the router IP address:

        ```
        $ export ROUTER_IP=`oc -n openshift-ingress get service router-default --no-headers | awk '{print $4}'`
        ```
     2. Add the A record to the private zones:

        +

```
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
```

+

```
$ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
```

+

```
$ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
```

+

```
$ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
```

1. For an external cluster, also add the A record to the public zones:

   +

```
$ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
```

+

```
$ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME} --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
```

+

```
$ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${BASE_DOMAIN_ZONE_NAME} --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
```

+

```
$ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME} --project ${HOST_PROJECT} --account ${HOST_PROJECT_ACCOUNT}
```

* To add explicit domains instead of using a wildcard, create entries for each of the cluster’s current routes:

  ```
  $ oc get --all-namespaces -o jsonpath='{range .items[*]}{range .status.ingress[*]}{.host}{"\n"}{end}{end}' routes
  ```

  **Example output**

  ```
  oauth-openshift.apps.your.cluster.domain.example.com
  console-openshift-console.apps.your.cluster.domain.example.com
  downloads-openshift-console.apps.your.cluster.domain.example.com
  alertmanager-main-openshift-monitoring.apps.your.cluster.domain.example.com
  prometheus-k8s-openshift-monitoring.apps.your.cluster.domain.example.com
  ```

### [10.25. Adding ingress firewall rules](#installation-gcp-user-infra-vpc-adding-firewall-rules) Copy linkLink copied to clipboard!

The cluster requires several firewall rules. If you do not use a shared VPC, these rules are created by the Ingress Controller via the Google Cloud cloud provider. When you use a shared VPC, you can either create cluster-wide firewall rules for all services now or create each rule based on events, when the cluster requests access. By creating each rule when the cluster requests access, you know exactly which firewall rules are required. By creating cluster-wide firewall rules, you can apply the same rule set across multiple clusters.

If you choose to create each rule based on events, you must create firewall rules after you provision the cluster and during the life of the cluster when the console notifies you that rules are missing. Events that are similar to the following event are displayed, and you must add the firewall rules that are required:

```
$ oc get events -n openshift-ingress --field-selector="reason=LoadBalancerManualChange"
```

**Example output**

```
Firewall change required by security admin: `gcloud compute firewall-rules create k8s-fw-a26e631036a3f46cba28f8df67266d55 --network example-network --description "{\"kubernetes.io/service-name\":\"openshift-ingress/router-default\", \"kubernetes.io/service-ip\":\"35.237.236.234\"}\" --allow tcp:443,tcp:80 --source-ranges 0.0.0.0/0 --target-tags exampl-fqzq7-master,exampl-fqzq7-worker --project example-project`
```

If you encounter issues when creating these rule-based events, you can configure the cluster-wide firewall rules while your cluster is running.

#### [10.25.1. Creating cluster-wide firewall rules for a shared VPC in Google Cloud](#installation-creating-gcp-shared-vpc-cluster-wide-firewall-rules_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

You can create cluster-wide firewall rules to allow the access that the OpenShift Container Platform cluster requires.

Warning

If you do not choose to create firewall rules based on cluster events, you must create cluster-wide firewall rules.

**Prerequisites**

* You exported the variables that the Infrastructure Manager templates require to deploy your cluster.
* You created the networking and load balancing components in Google Cloud that your cluster requires.

**Procedure**

1. Add a single firewall rule to allow the Google Cloud Engine health checks to access all of the services. This rule enables the ingress load balancers to determine the health status of their instances.

   ```
   $ gcloud compute firewall-rules create --allow='tcp:30000-32767,udp:30000-32767' --network="${CLUSTER_NETWORK}" --source-ranges='130.211.0.0/22,35.191.0.0/16,209.85.152.0/22,209.85.204.0/22' --target-tags="${INFRA_ID}-master,${INFRA_ID}-worker" ${INFRA_ID}-ingress-hc --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT}
   ```
2. Add a single firewall rule to allow access to all cluster services:

   * For an external cluster:

     ```
     $ gcloud compute firewall-rules create --allow='tcp:80,tcp:443' --network="${CLUSTER_NETWORK}" --source-ranges="0.0.0.0/0" --target-tags="${INFRA_ID}-master,${INFRA_ID}-worker" ${INFRA_ID}-ingress --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT}
     ```
   * For a private cluster:

     ```
     $ gcloud compute firewall-rules create --allow='tcp:80,tcp:443' --network="${CLUSTER_NETWORK}" --source-ranges=${NETWORK_CIDR} --target-tags="${INFRA_ID}-master,${INFRA_ID}-worker" ${INFRA_ID}-ingress --account=${HOST_PROJECT_ACCOUNT} --project=${HOST_PROJECT}
     ```

   Because this rule only allows traffic on TCP ports `80` and `443`, ensure that you add all the ports that your services use.

### [10.26. Completing a Google Cloud installation on user-provisioned infrastructure](#installation-gcp-user-infra-installation_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

After you start the OpenShift Container Platform installation on Google Cloud user-provisioned infrastructure, you can monitor the cluster events until the cluster is ready.

**Prerequisites**

* Ensure the bootstrap process completed successfully.

**Procedure**

1. Complete the cluster installation:

   ```
   $ ./openshift-install --dir <installation_directory> wait-for install-complete
   ```

   1

   **Example output**

   ```
   INFO Waiting up to 30m0s for the cluster to initialize...
   ```

   [1](#CO23-1)
   :   For `<installation_directory>`, specify the path to the directory that you stored the installation files in.

   Important

   * The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
   * It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
2. Observe the running state of your cluster.

   1. Run the following command to view the current cluster version and status:

      ```
      $ oc get clusterversion
      ```

      **Example output**

      ```
      NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
      version             False       True          24m     Working towards 4.5.4: 99% complete
      ```
   2. Run the following command to view the Operators managed on the control plane by the Cluster Version Operator (CVO):

      ```
      $ oc get clusteroperators
      ```

      **Example output**

      ```
      NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
      authentication                             4.5.4     True        False         False      7m56s
      cloud-credential                           4.5.4     True        False         False      31m
      cluster-autoscaler                         4.5.4     True        False         False      16m
      console                                    4.5.4     True        False         False      10m
      csi-snapshot-controller                    4.5.4     True        False         False      16m
      dns                                        4.5.4     True        False         False      22m
      etcd                                       4.5.4     False       False         False      25s
      image-registry                             4.5.4     True        False         False      16m
      ingress                                    4.5.4     True        False         False      16m
      insights                                   4.5.4     True        False         False      17m
      kube-apiserver                             4.5.4     True        False         False      19m
      kube-controller-manager                    4.5.4     True        False         False      20m
      kube-scheduler                             4.5.4     True        False         False      20m
      kube-storage-version-migrator              4.5.4     True        False         False      16m
      machine-api                                4.5.4     True        False         False      22m
      machine-config                             4.5.4     True        False         False      22m
      marketplace                                4.5.4     True        False         False      16m
      monitoring                                 4.5.4     True        False         False      10m
      network                                    4.5.4     True        False         False      23m
      node-tuning                                4.5.4     True        False         False      23m
      openshift-apiserver                        4.5.4     True        False         False      17m
      openshift-controller-manager               4.5.4     True        False         False      15m
      openshift-samples                          4.5.4     True        False         False      16m
      operator-lifecycle-manager                 4.5.4     True        False         False      22m
      operator-lifecycle-manager-catalog         4.5.4     True        False         False      22m
      operator-lifecycle-manager-packageserver   4.5.4     True        False         False      18m
      service-ca                                 4.5.4     True        False         False      23m
      service-catalog-apiserver                  4.5.4     True        False         False      23m
      service-catalog-controller-manager         4.5.4     True        False         False      23m
      storage                                    4.5.4     True        False         False      17m
      ```
   3. Run the following command to view your cluster pods:

      ```
      $ oc get pods --all-namespaces
      ```

      **Example output**

      ```
      NAMESPACE                                               NAME                                                                READY     STATUS      RESTARTS   AGE
      kube-system                                             etcd-member-ip-10-0-3-111.us-east-2.compute.internal                1/1       Running     0          35m
      kube-system                                             etcd-member-ip-10-0-3-239.us-east-2.compute.internal                1/1       Running     0          37m
      kube-system                                             etcd-member-ip-10-0-3-24.us-east-2.compute.internal                 1/1       Running     0          35m
      openshift-apiserver-operator                            openshift-apiserver-operator-6d6674f4f4-h7t2t                       1/1       Running     1          37m
      openshift-apiserver                                     apiserver-fm48r                                                     1/1       Running     0          30m
      openshift-apiserver                                     apiserver-fxkvv                                                     1/1       Running     0          29m
      openshift-apiserver                                     apiserver-q85nm                                                     1/1       Running     0          29m
      ...
      openshift-service-ca-operator                           openshift-service-ca-operator-66ff6dc6cd-9r257                      1/1       Running     0          37m
      openshift-service-ca                                    apiservice-cabundle-injector-695b6bcbc-cl5hm                        1/1       Running     0          35m
      openshift-service-ca                                    configmap-cabundle-injector-8498544d7-25qn6                         1/1       Running     0          35m
      openshift-service-ca                                    service-serving-cert-signer-6445fc9c6-wqdqn                         1/1       Running     0          35m
      openshift-service-catalog-apiserver-operator            openshift-service-catalog-apiserver-operator-549f44668b-b5q2w       1/1       Running     0          32m
      openshift-service-catalog-controller-manager-operator   openshift-service-catalog-controller-manager-operator-b78cr2lnm     1/1       Running     0          31m
      ```

      When the current cluster version is `AVAILABLE`, the installation is complete.

### [10.27. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-gcp-user-infra-vpc) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

### [10.28. Next steps](#next-steps-7) Copy linkLink copied to clipboard!

* [Customize your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations).
* If necessary, you can [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting).

## [Chapter 11. Installing a cluster on Google Cloud in a disconnected environment with user-provisioned infrastructure](#installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

In OpenShift Container Platform version 4.22, you can install a cluster on Google Cloud that uses infrastructure that you provide and an internal mirror of the installation release content.

Important

While you can install an OpenShift Container Platform cluster by using mirrored installation release content, your cluster still requires internet access to use the Google Cloud APIs.

The steps for performing a user-provided infrastructure install are outlined here. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods.

Important

The steps for performing a user-provisioned infrastructure installation are provided as an example only. Installing a cluster with infrastructure you provide requires knowledge of the cloud provider and the installation process of OpenShift Container Platform. Several Infrastructure Manager templates are provided to assist in completing these steps or to help model your own. You are also free to create the required resources through other methods; the templates are just an example.

### [11.1. Prerequisites](#prerequisites-7) Copy linkLink copied to clipboard!

* You reviewed details about the [OpenShift Container Platform installation and update](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/architecture/#architecture-installation) processes.
* You read the documentation on [selecting a cluster installation method and preparing it for users](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_overview/#installing-preparing).
* You [created a registry on your mirror host](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#installing-mirroring-installation-images) and obtained the `imageContentSources` data for your version of OpenShift Container Platform.

  Important

  Because the installation media is on the mirror host, you can use that computer to complete all installation steps.
* If you use a firewall, you [configured it to allow the sites](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/installation_configuration/#configuring-firewall-module_configuring-firewall) that your cluster requires access to. While you might need to grant access to more sites, you must grant access to `*.googleapis.com` and `accounts.google.com`.
* If the cloud identity and access management (IAM) APIs are not accessible in your environment, or if you do not want to store an administrator-level credential secret in the `kube-system` namespace, you can [manually create and maintain long-term credentials](#manually-create-iam_installing-gcp-customizations "4.10.1. Manually creating long-term credentials").

### [11.2. About installations in restricted networks](#installation-about-restricted-networks_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can install OpenShift Container Platform 4.22 in a restricted network without an active internet connection to obtain software components. Restricted network installations can use installer-provisioned or user-provisioned infrastructure, depending on the cloud platform to which you are installing the cluster.

If you perform a restricted network installation on a cloud platform, you still require access to its cloud APIs. Some cloud functions, such as Amazon Web Service’s Route 53 DNS and IAM services, require internet access. Depending on your network, you might require less internet access for an installation on bare-metal hardware, Nutanix, or on VMware vSphere.

To complete a restricted network installation, you must create a registry that mirrors the contents of the OpenShift image registry and has the installation media. You can create this registry on a mirror host, which can access both the internet and your closed network, or by using other methods that meet your restrictions.

Important

Because of the complexity of the configuration for user-provisioned installations, consider completing a standard user-provisioned infrastructure installation before you try a restricted network installation using user-provisioned infrastructure. Completing this test installation might make it easier to isolate and troubleshoot any issues that might arise during your installation in a restricted network.

#### [11.2.1. Additional limits](#installation-restricted-network-limits_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

Clusters in restricted networks have the following additional limitations and restrictions:

* The `ClusterVersion` status includes an `Unable to retrieve available updates` error.
* By default, you cannot use the contents of the Developer Catalog because you cannot access the required image stream tags.

### [11.3. Internet access for OpenShift Container Platform](#cluster-entitlements_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

In OpenShift Container Platform 4.22, you require access to the internet to obtain the images that are necessary to install your cluster.

You must have internet access to perform the following actions:

* Access Red Hat Hybrid Cloud Console to download the installation program and perform subscription management. If the cluster has internet access and you do not disable Telemetry, that service automatically entitles your cluster.
* Access Quay.io to obtain the packages that are required to install your cluster.
* Obtain the packages that are required to perform cluster updates.

### [11.4. Configuring your Google Cloud project](#installation-restricted-networks-gcp-user-infra-config-project) Copy linkLink copied to clipboard!

Before you can install OpenShift Container Platform, you must configure a Google Cloud project to host it.

#### [11.4.1. Creating a Google Cloud project](#installation-gcp-project_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, you must create a project in your Google Cloud account to host the cluster.

**Procedure**

* Create a project to host your OpenShift Container Platform cluster. See [Creating and Managing Projects](https://cloud.google.com/resource-manager/docs/creating-managing-projects) in the Google Cloud documentation.

  Important

  Your Google Cloud project must use the Premium Network Service Tier if you are using installer-provisioned infrastructure. The Standard Network Service Tier is not supported for clusters installed using the installation program. The installation program configures internal load balancing for the `api-int.<cluster_name>.<base_domain>` URL; the Premium Tier is required for internal load balancing.

#### [11.4.2. Enabling API services in Google Cloud](#installation-gcp-enabling-api-services_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

Your Google Cloud project requires access to several API services to complete OpenShift Container Platform installation.

**Prerequisites**

* You created a project to host your cluster.

**Procedure**

* Enable the following required API services in the project that hosts your cluster. You may also enable optional API services which are not required for installation. See [Enabling services](https://cloud.google.com/service-usage/docs/enable-disable#enabling) in the Google Cloud documentation.

  Expand

  Table 11.1. Required API services

  | API service | Console service name |
  | --- | --- |
  | Compute Engine API | `compute.googleapis.com` |
  | Cloud Resource Manager API | `cloudresourcemanager.googleapis.com` |
  | Cloud DNS API | `dns.googleapis.com` |
  | IAM Service Account Credentials API | `iamcredentials.googleapis.com` |
  | Identity and Access Management (IAM) API | `iam.googleapis.com` |
  | Service Usage API | `serviceusage.googleapis.com` |

  Show more

  Expand

  Table 11.2. Optional API services

  | API service | Console service name |
  | --- | --- |
  | Google Cloud APIs | `cloudapis.googleapis.com` |
  | Service Management API | `servicemanagement.googleapis.com` |
  | Google Cloud Storage JSON API | `storage-api.googleapis.com` |
  | Cloud Storage | `storage-component.googleapis.com` |

  Show more

#### [11.4.3. Configuring DNS for Google Cloud](#installation-gcp-dns_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

To install OpenShift Container Platform, the Google Cloud account you use must have a dedicated public hosted zone in the same project that you host the OpenShift Container Platform cluster. This zone must be authoritative for the domain. The DNS service provides cluster DNS resolution and name lookup for external connections to the cluster.

**Procedure**

1. Identify your domain, or subdomain, and registrar. You can transfer an existing domain and registrar or obtain a new one through Google Cloud or another source.

   Note

   If you purchase a new domain, it can take time for the relevant DNS changes to propagate. For more information about purchasing domains through Google, see [Google Domains](https://domains.google/).
2. Create a public hosted zone for your domain or subdomain in your Google Cloud project. See [Creating public zones](https://cloud.google.com/dns/zones/#creating_public_zones) in the Google Cloud documentation.

   Use an appropriate root domain, such as `openshiftcorp.com`, or subdomain, such as `clusters.openshiftcorp.com`.
3. Extract the new authoritative name servers from the hosted zone records. See [Look up your Cloud DNS name servers](https://cloud.google.com/dns/docs/update-name-servers#look_up_your_name_servers) in the Google Cloud documentation.

   You typically have four name servers.
4. Update the registrar records for the name servers that your domain uses. For example, if you registered your domain to Google Domains, see the following topic in the Google Domains Help: [How to switch to custom name servers](https://support.google.com/domains/answer/3290309?hl=en).
5. If you migrated your root domain to Google Cloud DNS, migrate your DNS records. See [Migrating to Cloud DNS](https://cloud.google.com/dns/docs/migrating) in the Google Cloud documentation.
6. If you use a subdomain, follow your company’s procedures to add its delegation records to the parent domain. This process might include a request to your company’s IT department or the division that controls the root domain and DNS services for your company.

#### [11.4.4. Google Cloud account limits](#installation-gcp-limits_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

The OpenShift Container Platform cluster uses a number of Google Cloud components, but the default [Quotas](https://cloud.google.com/docs/quota) do not affect your ability to install a default OpenShift Container Platform cluster.

A default cluster, which contains three compute and three control plane machines, uses the following resources. Note that some resources are required only during the bootstrap process and are removed after the cluster deploys.

Expand

Table 11.3. Google Cloud resources used in a default cluster

| Service | Component | Location | Total resources required | Resources removed after bootstrap |
| --- | --- | --- | --- | --- |
| Service account | IAM | Global | 6 | 1 |
| Firewall rules | Networking | Global | 11 | 1 |
| Forwarding rules | Compute | Global | 2 | 0 |
| Health checks | Compute | Global | 2 | 0 |
| Images | Compute | Global | 1 | 0 |
| Networks | Networking | Global | 1 | 0 |
| Routers | Networking | Global | 1 | 0 |
| Routes | Networking | Global | 2 | 0 |
| Subnetworks | Compute | Global | 2 | 0 |
| Target pools | Networking | Global | 2 | 0 |

Show more

Note

If any of the quotas are insufficient during installation, the installation program displays an error that states both which quota was exceeded and the region.

Be sure to consider your actual cluster size, planned cluster growth, and any usage from other clusters that are associated with your account. The CPU, static IP addresses, and persistent disk SSD (storage) quotas are the ones that are most likely to be insufficient.

If you plan to deploy your cluster in one of the following regions, you will exceed the maximum storage quota and are likely to exceed the CPU quota limit:

* `asia-east2`
* `asia-northeast2`
* `asia-south1`
* `australia-southeast1`
* `europe-north1`
* `europe-west2`
* `europe-west3`
* `europe-west6`
* `northamerica-northeast1`
* `southamerica-east1`
* `us-west2`

You can increase resource quotas from the [Google Cloud console](https://console.cloud.google.com/iam-admin/quotas), but you might need to file a support ticket. Be sure to plan your cluster size early so that you can allow time to resolve the support ticket before you install your OpenShift Container Platform cluster.

#### [11.4.5. Creating a service account in Google Cloud](#installation-gcp-service-account_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

OpenShift Container Platform requires a Google Cloud service account that provides authentication and authorization to access data in the Google APIs. If you do not have an existing IAM service account that contains the required roles in your project, you must create one.

Note

To reduce the scope of permissions granted to the main service account in your Google Cloud project while still being able to use the Google Cloud Container Storage Interface (CSI) Driver Operator, you can transfer the control of permissions from the project-wide service account to the control plane and compute node service accounts instead, thus reducing the scope of the permission. For more information, see Section *Reducing permissions while using the Google Cloud CSI Driver Operator*.

**Prerequisites**

* You created a project to host your cluster.

**Procedure**

1. Create a service account in the project that you use to host your OpenShift Container Platform cluster. See [Creating a service account](https://cloud.google.com/iam/docs/creating-managing-service-accounts#creating_a_service_account) in the Google Cloud documentation.
2. Grant the service account the appropriate permissions. You can either grant the individual permissions that follow or assign the `Owner` role to it. See [Granting roles to a service account for specific resources](https://cloud.google.com/iam/docs/granting-roles-to-service-accounts#granting_access_to_a_service_account_for_a_resource).

   Note

   While making the service account an owner of the project is the easiest way to gain the required permissions, it means that service account has complete control over the project. You must determine if the risk that comes from offering that power is acceptable.
3. You can create the service account key in JSON format, or attach the service account to a Google Cloud virtual machine. See [Creating service account keys](https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys) and [Creating and enabling service accounts for instances](https://cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances) in the Google Cloud documentation.

   Note

   If you use a virtual machine with an attached service account to create your cluster, you must set `credentialsMode: Manual` in the `install-config.yaml` file before installation.

#### [11.4.6. Required Google Cloud roles](#installation-gcp-permissions_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform. If your organization’s security policies require a more restrictive set of permissions, you can create a service account with the following permissions. If you deploy your cluster into an existing virtual private cloud (VPC), the service account does not require certain networking permissions, which are noted in the following lists:

**Required roles for the installation program**

* Compute Admin
* Role Administrator
* Security Admin
* Service Account Admin
* Service Account Key Admin
* Service Account User
* Storage Admin

**Required roles for creating network resources during installation**

* DNS Administrator

**Required roles for using the Cloud Credential Operator in passthrough mode**

* Compute Load Balancer Admin
* Tag User

**Required roles for user-provisioned Google Cloud infrastructure**

* Cloud Infrastructure Manager Admin

The following roles are applied to the service accounts that the control plane and compute machines use:

Expand

Table 11.4. Google Cloud service account roles

| Account | Roles |
| --- | --- |
| Control Plane | `roles/compute.instanceAdmin` |
| `roles/compute.networkAdmin` |
| `roles/compute.securityAdmin` |
| `roles/storage.admin` |
| `roles/iam.serviceAccountUser` |
| Compute | `roles/compute.viewer` |
| `roles/storage.admin` |
| `roles/artifactregistry.reader` |

Show more

#### [11.4.7. Required Google Cloud permissions for user-provisioned infrastructure](#minimum-required-permissions-upi-gcp_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

When you attach the `Owner` role to the service account that you create, you grant that service account all permissions, including those that are required to install OpenShift Container Platform.

If your organization’s security policies require a more restrictive set of permissions, you can create [custom roles](https://cloud.google.com/iam/docs/creating-custom-roles) with the necessary permissions. The following permissions are required for the user-provisioned infrastructure for creating and deleting the OpenShift Container Platform cluster.

**Example 11.1. Required permissions for creating network resources**

* `compute.addresses.create`
* `compute.addresses.createInternal`
* `compute.addresses.delete`
* `compute.addresses.get`
* `compute.addresses.list`
* `compute.addresses.use`
* `compute.addresses.useInternal`
* `compute.firewalls.create`
* `compute.firewalls.delete`
* `compute.firewalls.get`
* `compute.firewalls.list`
* `compute.forwardingRules.create`
* `compute.forwardingRules.get`
* `compute.forwardingRules.list`
* `compute.forwardingRules.setLabels`
* `compute.globalAddresses.create`
* `compute.globalAddresses.get`
* `compute.globalAddresses.use`
* `compute.globalForwardingRules.create`
* `compute.globalForwardingRules.get`
* `compute.globalForwardingRules.setLabels`
* `compute.networks.create`
* `compute.networks.get`
* `compute.networks.list`
* `compute.networks.updatePolicy`
* `compute.networks.use`
* `compute.routers.create`
* `compute.routers.get`
* `compute.routers.list`
* `compute.routers.update`
* `compute.routes.list`
* `compute.subnetworks.create`
* `compute.subnetworks.get`
* `compute.subnetworks.list`
* `compute.subnetworks.use`
* `compute.subnetworks.useExternalIp`

**Example 11.2. Required permissions for creating load balancer resources**

* `compute.backendServices.create`
* `compute.backendServices.get`
* `compute.backendServices.list`
* `compute.backendServices.update`
* `compute.backendServices.use`
* `compute.regionBackendServices.create`
* `compute.regionBackendServices.get`
* `compute.regionBackendServices.list`
* `compute.regionBackendServices.update`
* `compute.regionBackendServices.use`
* `compute.targetPools.addInstance`
* `compute.targetPools.create`
* `compute.targetPools.get`
* `compute.targetPools.list`
* `compute.targetPools.removeInstance`
* `compute.targetPools.use`
* `compute.targetTcpProxies.create`
* `compute.targetTcpProxies.get`
* `compute.targetTcpProxies.use`

**Example 11.3. Required permissions for creating DNS resources**

* `dns.changes.create`
* `dns.changes.get`
* `dns.managedZones.create`
* `dns.managedZones.get`
* `dns.managedZones.list`
* `dns.networks.bindPrivateDNSZone`
* `dns.resourceRecordSets.create`
* `dns.resourceRecordSets.list`
* `dns.resourceRecordSets.update`

**Example 11.4. Required permissions for creating Service Account resources**

* `iam.serviceAccountKeys.create`
* `iam.serviceAccountKeys.delete`
* `iam.serviceAccountKeys.get`
* `iam.serviceAccountKeys.list`
* `iam.serviceAccounts.actAs`
* `iam.serviceAccounts.create`
* `iam.serviceAccounts.delete`
* `iam.serviceAccounts.get`
* `iam.serviceAccounts.list`
* `resourcemanager.projects.get`
* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`

**Example 11.5. Required permissions for creating compute resources**

* `compute.disks.create`
* `compute.disks.get`
* `compute.disks.list`
* `compute.instanceGroups.create`
* `compute.instanceGroups.delete`
* `compute.instanceGroups.get`
* `compute.instanceGroups.list`
* `compute.instanceGroups.update`
* `compute.instanceGroups.use`
* `compute.instances.create`
* `compute.instances.delete`
* `compute.instances.get`
* `compute.instances.list`
* `compute.instances.setLabels`
* `compute.instances.setMetadata`
* `compute.instances.setServiceAccount`
* `compute.instances.setTags`
* `compute.instances.use`
* `compute.machineTypes.get`
* `compute.machineTypes.list`

**Example 11.6. Required for creating storage resources**

* `storage.buckets.create`
* `storage.buckets.delete`
* `storage.buckets.get`
* `storage.buckets.list`
* `storage.objects.create`
* `storage.objects.delete`
* `storage.objects.get`
* `storage.objects.list`

**Example 11.7. Required permissions for creating health check resources**

* `compute.healthChecks.create`
* `compute.healthChecks.get`
* `compute.healthChecks.list`
* `compute.healthChecks.useReadOnly`
* `compute.httpHealthChecks.create`
* `compute.httpHealthChecks.get`
* `compute.httpHealthChecks.list`
* `compute.httpHealthChecks.useReadOnly`
* `compute.regionHealthChecks.create`
* `compute.regionHealthChecks.get`
* `compute.regionHealthChecks.useReadOnly`

**Example 11.8. Required permissions to get Google Cloud zone and region related information**

* `compute.globalOperations.get`
* `compute.regionOperations.get`
* `compute.regions.get`
* `compute.regions.list`
* `compute.zoneOperations.get`
* `compute.zones.get`
* `compute.zones.list`

**Example 11.9. Required permissions for checking services and quotas**

* `monitoring.timeSeries.list`
* `serviceusage.quotas.get`
* `serviceusage.services.list`

**Example 11.10. Required IAM permissions for installation**

* `iam.roles.get`

**Example 11.11. Required permissions when authenticating without a service account key**

* `iam.serviceAccounts.signBlob`

**Example 11.12. Required permissions when providing Key Management Service (KMS) key rings**

* `cloudkms.keyRings.list`

**Example 11.13. Required Images permissions for installation**

* `compute.images.create`
* `compute.images.delete`
* `compute.images.get`
* `compute.images.list`

**Example 11.14. Optional permission for running gather bootstrap**

* `compute.instances.getSerialPortOutput`

**Example 11.15. Required permissions for deleting network resources**

* `compute.addresses.delete`
* `compute.addresses.deleteInternal`
* `compute.addresses.list`
* `compute.addresses.setLabels`
* `compute.firewalls.delete`
* `compute.firewalls.list`
* `compute.forwardingRules.delete`
* `compute.forwardingRules.list`
* `compute.globalAddresses.delete`
* `compute.globalAddresses.list`
* `compute.globalForwardingRules.delete`
* `compute.globalForwardingRules.list`
* `compute.networks.delete`
* `compute.networks.list`
* `compute.networks.updatePolicy`
* `compute.routers.delete`
* `compute.routers.list`
* `compute.routes.list`
* `compute.subnetworks.delete`
* `compute.subnetworks.list`

**Example 11.16. Required permissions for deleting load balancer resources**

* `compute.backendServices.delete`
* `compute.backendServices.list`
* `compute.regionBackendServices.delete`
* `compute.regionBackendServices.list`
* `compute.targetPools.delete`
* `compute.targetPools.list`
* `compute.targetTcpProxies.delete`
* `compute.targetTcpProxies.list`

**Example 11.17. Required permissions for deleting DNS resources**

* `dns.changes.create`
* `dns.managedZones.delete`
* `dns.managedZones.get`
* `dns.managedZones.list`
* `dns.resourceRecordSets.delete`
* `dns.resourceRecordSets.list`

**Example 11.18. Required permissions for deleting Service Account resources**

* `iam.serviceAccounts.delete`
* `iam.serviceAccounts.get`
* `iam.serviceAccounts.list`
* `resourcemanager.projects.getIamPolicy`
* `resourcemanager.projects.setIamPolicy`

**Example 11.19. Required permissions for deleting compute resources**

* `compute.disks.delete`
* `compute.disks.list`
* `compute.instanceGroups.delete`
* `compute.instanceGroups.list`
* `compute.instances.delete`
* `compute.instances.list`
* `compute.instances.stop`
* `compute.machineTypes.list`

**Example 11.20. Required for deleting storage resources**

* `storage.buckets.delete`
* `storage.buckets.getIamPolicy`
* `storage.buckets.list`
* `storage.objects.delete`
* `storage.objects.list`

**Example 11.21. Required permissions for deleting health check resources**

* `compute.healthChecks.delete`
* `compute.healthChecks.list`
* `compute.httpHealthChecks.delete`
* `compute.httpHealthChecks.list`
* `compute.regionHealthChecks.delete`
* `compute.regionHealthChecks.list`

**Example 11.22. Required Images permissions for deletion**

* `compute.images.delete`
* `compute.images.list`

**Example 11.23. Required permissions to get Region related information**

* `compute.regions.get`

**Example 11.24. Required Deployment Manager permissions**

* config.deployments.create
* config.deployments.delete
* config.deployments.get
* config.deployments.list
* config.operations.get
* config.resources.list
* cloudbuild.builds.create
* cloudbuild.builds.get

#### [11.4.8. Supported Google Cloud regions](#installation-gcp-regions_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can deploy an OpenShift Container Platform cluster to the following Google Cloud regions:

* `africa-south1` (Johannesburg, South Africa)
* `asia-east1` (Changhua County, Taiwan)
* `asia-east2` (Hong Kong)
* `asia-northeast1` (Tokyo, Japan)
* `asia-northeast2` (Osaka, Japan)
* `asia-northeast3` (Seoul, South Korea)
* `asia-south1` (Mumbai, India)
* `asia-south2` (Delhi, India)
* `asia-southeast1` (Jurong West, Singapore)
* `asia-southeast2` (Jakarta, Indonesia)
* `australia-southeast1` (Sydney, Australia)
* `australia-southeast2` (Melbourne, Australia)
* `europe-central2` (Warsaw, Poland)
* `europe-north1` (Hamina, Finland)
* `europe-southwest1` (Madrid, Spain)
* `europe-west1` (St. Ghislain, Belgium)
* `europe-west2` (London, England, UK)
* `europe-west3` (Frankfurt, Germany)
* `europe-west4` (Eemshaven, Netherlands)
* `europe-west6` (Zürich, Switzerland)
* `europe-west8` (Milan, Italy)
* `europe-west9` (Paris, France)
* `europe-west12` (Turin, Italy)
* `me-central1` (Doha, Qatar, Middle East)
* `me-central2` (Dammam, Saudi Arabia, Middle East)
* `me-west1` (Tel Aviv, Israel)
* `northamerica-northeast1` (Montréal, Québec, Canada)
* `northamerica-northeast2` (Toronto, Ontario, Canada)
* `southamerica-east1` (São Paulo, Brazil)
* `southamerica-west1` (Santiago, Chile)
* `us-central1` (Council Bluffs, Iowa, USA)
* `us-east1` (Moncks Corner, South Carolina, USA)
* `us-east4` (Ashburn, Northern Virginia, USA)
* `us-east5` (Columbus, Ohio)
* `us-south1` (Dallas, Texas)
* `us-west1` (The Dalles, Oregon, USA)
* `us-west2` (Los Angeles, California, USA)
* `us-west3` (Salt Lake City, Utah, USA)
* `us-west4` (Las Vegas, Nevada, USA)

Note

To determine which machine type instances are available by region and zone, see the Google [documentation](https://cloud.google.com/compute/docs/regions-zones#available).

#### [11.4.9. Installing and configuring CLI tools for Google Cloud](#installation-gcp-install-cli_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on Google Cloud using user-provisioned infrastructure, you must install and configure the CLI tools for Google Cloud.

**Prerequisites**

* You created a project to host your cluster.
* You created a service account and granted it the required permissions.

**Procedure**

1. Install the following binaries in `$PATH`:

   * `gcloud`
   * `gsutil`

   See [Install the latest Cloud SDK version](https://cloud.google.com/sdk/docs/#install_the_latest_cloud_tools_version_cloudsdk_current_version) in the Google Cloud documentation.
2. Authenticate using the `gcloud` tool with your configured service account.

   See [Authorizing with a service account](https://cloud.google.com/sdk/docs/authorizing#authorizing_with_a_service_account) in the Google Cloud documentation.

### [11.5. Requirements for a cluster with user-provisioned infrastructure](#installation-requirements-user-infra_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

For a cluster that contains user-provisioned infrastructure, you must deploy all of the required machines.

This section describes the requirements for deploying OpenShift Container Platform on user-provisioned infrastructure.

#### [11.5.1. Required machines for cluster installation](#installation-machine-requirements_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must specify the minimum required machines or hosts for your cluster so that your cluster remains stable if a node fails.

The smallest OpenShift Container Platform clusters require the following hosts:

Important

For a cluster that has user-provisioned infrastructure, you must deploy all of the required machines.

Expand

Table 11.5. Minimum required hosts

| Hosts | Description |
| --- | --- |
| One temporary bootstrap machine | The cluster requires the bootstrap machine to deploy the OpenShift Container Platform cluster on the three control plane machines. You can remove the bootstrap machine after you install the cluster. |
| Three control plane machines | The control plane machines run the Kubernetes and OpenShift Container Platform services that form the control plane. |
| At least two compute machines, which are also known as worker machines. | The workloads requested by OpenShift Container Platform users run on the compute machines. |

Show more

Important

To keep high availability of your cluster, use separate physical hosts for these cluster machines.

The bootstrap and control plane machines must use Red Hat Enterprise Linux CoreOS (RHCOS) as the operating system. However, the compute machines can use Red Hat Enterprise Linux CoreOS (RHCOS), Red Hat Enterprise Linux (RHEL) 8.6 and later.

RHCOS is based on Red Hat Enterprise Linux (RHEL) 9.8 and inherits all of its hardware certifications and requirements. See [Red Hat Enterprise Linux technology capabilities and limits](https://access.redhat.com/articles/rhel-limits).

#### [11.5.2. Minimum resource requirements for cluster installation](#installation-minimum-resource-requirements_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

To ensure that your OpenShift Container Platform cluster runs as expected, each cluster machine must meet minimum CPU, memory, and storage requirements.

Expand

Table 11.6. Minimum resource requirements

| Machine | Operating system | vCPU | Virtual RAM | Storage | Input/Output Per Second (IOPS) |
| --- | --- | --- | --- | --- | --- |
| Bootstrap | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Control plane | RHCOS | 4 | 16 GB | 100 GB | 300 |
| Compute | RHCOS | 2 | 8 GB | 100 GB | 300 |

Show more

* One vCPU is equal to one physical core when simultaneous multithreading (SMT), or Hyper-Threading, is not enabled. When enabled, use the following formula to calculate the corresponding ratio: (threads per core × cores) × sockets = vCPUs.
* OpenShift Container Platform and Kubernetes are sensitive to disk performance, and Red Hat recommends faster storage, particularly for etcd on the control plane nodes which require a 10 ms p99 fsync duration. On many cloud platforms, storage size and IOPS scale together, so you might need to provision more storage to get enough performance.
* As with all user-provisioned installations, if you choose to use RHEL compute machines in your cluster, you take responsibility for all operating system life cycle management and maintenance, including performing system updates, applying patches, and completing all other required tasks. OpenShift Container Platform 4.10 and later do not support RHEL 7 compute machines.

Note

In OpenShift Container Platform version 4.22, RHCOS uses RHEL version 9.8, which updates the micro-architecture requirements. Each architecture requires the following minimum instruction set architectures (ISA):

* x86-64 architecture requires x86-64-v2 ISA
* ARM64 architecture requires ARMv8.0-A ISA
* ppc64le architecture requires IBM® Power9 ISA
* s390x architecture requires IBM® z14 ISA

For more information, see [Architectures](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/9/html-single/9.8_release_notes/index#architectures) in the RHEL documentation.

If an instance type for your platform meets the minimum requirements for cluster machines, it is supported to use in OpenShift Container Platform.

#### [11.5.3. Tested instance types for Google Cloud](#installation-gcp-tested-machine-types_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

The following Google Cloud instance types have been tested with OpenShift Container Platform.

Note

Not all instance types are available in all regions and zones. For a detailed breakdown of which instance types are available in which zones, see [regions and zones](https://cloud.google.com/compute/docs/regions-zones#available) (Google documentation).

Some instance types require the use of Hyperdisk storage. If you use an instance type that requires Hyperdisk storage, all of the nodes in your cluster must support Hyperdisk storage, and you must change the default storage class to use Hyperdisk storage. For more information, see [machine series support for Hyperdisk](https://cloud.google.com/compute/docs/disks/hyperdisks#machine-type-support) (Google documentation). For instructions on modifying storage classes, see the "GCE PersistentDisk (gcePD) object definition" section in the Dynamic Provisioning page in *Storage*.

See the following machine series:

* `A2`
* `A3`
* `C2`
* `C2D`
* `C3`
* `C3D`
* `C4`
* `E2`
* `M1`
* `N1`
* `N2`
* `N2D`
* `N4`
* `Tau T2D`

#### [11.5.4. Using custom machine types](#installation-custom-machine-types_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

Using a custom machine type to install a OpenShift Container Platform cluster is supported.

Consider the following when using a custom machine type:

* Similar to predefined instance types, custom machine types must meet the minimum resource requirements for control plane and compute machines. For more information, see "Minimum resource requirements for cluster installation".
* The name of the custom machine type must adhere to the following syntax:

  `custom-<number_of_cpus>-<amount_of_memory_in_mb>`

  For example, `custom-6-20480`.

### [11.6. Creating the installation files for Google Cloud](#installation-user-infra-generate_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

To install OpenShift Container Platform on Google Cloud by using user-provisioned infrastructure, you must generate the files that the installation program needs to deploy your cluster and modify them so that the cluster creates only the machines that it will use.

You generate and customize the `install-config.yaml` file, Kubernetes manifests, and Ignition config files. You also have the option to first set up a separate `var` partition during the preparation phases of installation.

#### [11.6.1. Optional: Creating a separate /var partition](#installation-disk-partitioning-upi-templates_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

To isolate growing storage for containers, etcd, or logs, you can optionally create a separate `/var` partition on worker nodes before you generate Ignition configs.

It is recommended that disk partitioning for OpenShift Container Platform be left to the installation program. However, there are cases where you might want to create separate partitions in a part of the filesystem that you expect to grow.

OpenShift Container Platform supports the addition of a single partition to attach storage to either the `/var` partition or a subdirectory of `/var`. For example:

* `/var/lib/containers`: Holds container-related content that can grow as more images and containers are added to a system.
* `/var/lib/etcd`: Holds data that you might want to keep separate for purposes such as performance optimization of etcd storage.
* `/var`: Holds data that you might want to keep separate for purposes such as auditing.

Storing the contents of a `/var` directory separately makes it easier to grow storage for those areas as needed and reinstall OpenShift Container Platform at a later date and keep that data intact. With this method, you will not have to pull all your containers again, nor will you have to copy massive log files when you update systems.

Because `/var` must be in place before a fresh installation of Red Hat Enterprise Linux CoreOS (RHCOS), the following procedure sets up the separate `/var` partition by creating a machine config manifest that is inserted during the `openshift-install` preparation phases of an OpenShift Container Platform installation.

Important

If you follow the steps to create a separate `/var` partition in this procedure, it is not necessary to create the Kubernetes manifest and Ignition config files again as described later in this section.

**Procedure**

1. Create a directory to hold the OpenShift Container Platform installation files:

   ```
   $ mkdir $HOME/clusterconfig
   ```
2. Run `openshift-install` to create a set of files in the `manifest` and `openshift` subdirectories. Answer the system questions as you are prompted:

   ```
   $ openshift-install create manifests --dir $HOME/clusterconfig
   ```

   **Example output**

   ```
   ? SSH Public Key ...
   INFO Credentials loaded from the "myprofile" profile in file "/home/myuser/.aws/credentials"
   INFO Consuming Install Config from target directory
   INFO Manifests created in: $HOME/clusterconfig/manifests and $HOME/clusterconfig/openshift
   ```
3. Optional: Confirm that the installation program created manifests in the `clusterconfig/openshift` directory:

   ```
   $ ls $HOME/clusterconfig/openshift/
   ```

   **Example output**

   ```
   99_kubeadmin-password-secret.yaml
   99_openshift-cluster-api_master-machines-0.yaml
   99_openshift-cluster-api_master-machines-1.yaml
   99_openshift-cluster-api_master-machines-2.yaml
   ...
   ```
4. Create a Butane config that configures the additional partition. For example, name the file `$HOME/clusterconfig/98-var-partition.bu`, change the disk device name to the name of the storage device on the `worker` systems, and set the storage size as appropriate. This example places the `/var` directory on a separate partition:

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
   :   Specifies the `start_mib` parameter. When adding a data partition to the boot disk, a minimum value of 25000 MiB (Mebibytes) is recommended. The root file system is automatically resized to fill all available space up to the specified offset. If no value is specified, or if the specified value is smaller than the recommended minimum, the resulting root file system will be too small, and future reinstalls of RHCOS might overwrite the beginning of the data partition.

   `<partition_size>`
   :   Specifies the size of the data partition in mebibytes.

   `storage.filesystems.mount_options`
   :   The `prjquota` mount option must be enabled for filesystems used for container storage.

       Note

       When creating a separate `/var` partition, you cannot use different instance types for worker nodes, if the different instance types do not have the same device name.
5. Create a manifest from the Butane config and save it to the `clusterconfig/openshift` directory. For example, run the following command:

   ```
   $ butane $HOME/clusterconfig/98-var-partition.bu -o $HOME/clusterconfig/openshift/98-var-partition.yaml
   ```
6. Run `openshift-install` again to create Ignition configs from a set of files in the `manifest` and `openshift` subdirectories:

   ```
   $ openshift-install create ignition-configs --dir $HOME/clusterconfig
   ```

   ```
   $ ls $HOME/clusterconfig/
   auth  bootstrap.ign  master.ign  metadata.json  worker.ign
   ```

   You can now use the Ignition config files as input to the installation procedures to install Red Hat Enterprise Linux CoreOS (RHCOS) systems.

#### [11.6.2. Creating the installation configuration file](#installation-initializing_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can customize the OpenShift Container Platform cluster you install on Google Cloud.

**Prerequisites**

* You have the OpenShift Container Platform installation program and the pull secret for your cluster. For a restricted network installation, these files are on your mirror host.
* You have the `imageContentSources` values that were generated during mirror registry creation.
* You have obtained the contents of the certificate for your mirror registry.
* Configure a Google Cloud account.

**Procedure**

1. Create the `install-config.yaml` file.

   1. Change to the directory that contains the installation program and run the following command:

      ```
      $ ./openshift-install create install-config --dir <installation_directory>
      ```

      * `<installation_directory>`: For `<installation_directory>`, specify the directory name to store the files that the installation program creates.

        When specifying the directory:
      * Verify that the directory has the `execute` permission. This permission is required to run Terraform binaries under the installation directory.
      * Use an empty directory. Some installation assets, such as bootstrap X.509 certificates, have short expiration intervals, therefore you must not reuse an installation directory. If you want to reuse individual files from another cluster installation, you can copy them into your directory. However, the file names for the installation assets might change between releases. Use caution when copying installation files from an earlier OpenShift Container Platform version.
   2. At the prompts, provide the configuration details for your cloud:

      1. Optional: Select an SSH key to use to access your cluster machines.

         Note

         For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.
      2. Select **gcp** as the platform to target.
      3. If you have not configured the service account key for your Google Cloud account on your computer, you must obtain it from Google Cloud and paste the contents of the file or enter the absolute path to the file.
      4. Select the project ID to provision the cluster in. The default value is specified by the service account that you configured.
      5. Select the region to deploy the cluster to.
      6. Select the base domain to deploy the cluster to. The base domain corresponds to the public DNS zone that you created for your cluster.
      7. Enter a descriptive name for your cluster.
2. Edit the `install-config.yaml` file to give the additional information that is required for an installation in a restricted network.

   1. Update the `pullSecret` value to contain the authentication information for your registry:

      ```
      pullSecret: '{"auths":{"<mirror_host_name>:5000": {"auth": "<credentials>","email": "you@example.com"}}}'
      ```

      For `<mirror_host_name>`, specify the registry domain name that you specified in the certificate for your mirror registry, and for `<credentials>`, specify the base64-encoded user name and password for your mirror registry.
   2. Add the `additionalTrustBundle` parameter and value.

      ```
      additionalTrustBundle: |
        -----BEGIN CERTIFICATE-----
        ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
        -----END CERTIFICATE-----
      ```

      The value must be the contents of the certificate file that you used for your mirror registry. The certificate file can be an existing, trusted certificate authority, or the self-signed certificate that you generated for the mirror registry.
   3. Add the image content resources, which resemble the following YAML excerpt:

      ```
      imageContentSources:
      - mirrors:
        - <mirror_host_name>:5000/<repo_name>/release
        source: quay.io/openshift-release-dev/ocp-release
      - mirrors:
        - <mirror_host_name>:5000/<repo_name>/release
        source: registry.redhat.io/ocp/release
      ```

      For these values, use the `imageContentSources` that you recorded during mirror registry creation.
   4. Optionally, set the publishing strategy to `Internal`:

      ```
      publish: Internal
      ```

      By setting this option, you create an internal Ingress Controller and a private load balancer.
3. Make any other modifications to the `install-config.yaml` file that you require.

   For more information about the parameters, see "Installation configuration parameters".
4. Back up the `install-config.yaml` file so that you can use it to install multiple clusters.

   Important

   The `install-config.yaml` file is consumed during the installation process. If you want to reuse the file, you must back it up now.

#### [11.6.3. Enabling Shielded VMs](#installation-gcp-enabling-shielded-vms_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can use Shielded VMs when installing your cluster. Shielded VMs have extra security features including secure boot, firmware and integrity monitoring, and rootkit detection. For more information, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).

Note

Shielded VMs are currently not supported on clusters with 64-bit ARM infrastructures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use shielded VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            secureBoot: Enabled
     ```
  2. To use shielded VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            secureBoot: Enabled
     ```
  3. To use shielded VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            secureBoot: Enabled
     ```

#### [11.6.4. Enabling Confidential VMs](#installation-gcp-enabling-confidential-vms_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can use Confidential VMs when installing your cluster. Confidential VMs encrypt data while it is being processed. For more information, see Google’s documentation on [Confidential Computing](https://cloud.google.com/confidential-computing). You can enable Confidential VMs and Shielded VMs at the same time, although they are not dependent on each other.

Note

Confidential VMs are currently not supported on 64-bit ARM architectures.

**Procedure**

* Use a text editor to edit the `install-config.yaml` file prior to deploying your cluster and add one of the following stanzas:

  1. To use confidential VMs for only control plane machines:

     ```
     controlPlane:
       platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
     ```

     1

     ```
            type: n2d-standard-8
     ```

     2

     ```
            onHostMaintenance: Terminate
     ```

     3

     [1](#CO24-1)
     :   Enable confidential VMs with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP). For more information about available options, see "Additional Google Cloud configuration parameters".

     [2](#CO24-2)
     :   Specify a machine type that supports Confidential VMs. Confidential VMs require the N2D, C2D, C3D, or C3 series of machine types. For more information on supported machine types, see [Supported operating systems and machine types](https://cloud.google.com/compute/confidential-vm/docs/os-and-machine-type#machine-type).

     [3](#CO24-3)
     :   Specify the behavior of the VM during a host maintenance event, such as a hardware or software update. For a machine that uses Confidential VM, this value must be set to `Terminate`, which stops the VM. Confidential VMs do not support live VM migration.
  2. To use confidential VMs for only compute machines:

     ```
     compute:
     - platform:
         gcp:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```
  3. To use confidential VMs for all machines:

     ```
     platform:
       gcp:
         defaultMachinePlatform:
            confidentialCompute: AMDEncryptedVirtualizationNestedPaging
            type: n2d-standard-8
            onHostMaintenance: Terminate
     ```

#### [11.6.5. Configuring the cluster-wide proxy during installation](#installation-configure-proxy_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

Production environments can deny direct access to the internet and instead have an HTTP or HTTPS proxy available. You can configure a new OpenShift Container Platform cluster to use a proxy by configuring the proxy settings in the `install-config.yaml` file.

**Prerequisites**

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

#### [11.6.6. Creating the Kubernetes manifest and Ignition config files](#installation-user-infra-generate-k8s-manifest-ignition_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

Because you manually provision infrastructure, you must generate the Kubernetes manifest and Ignition config files that the cluster requires.

The installation program converts the installation configuration into Kubernetes manifests and then wraps them into Ignition configuration files. You use these Ignition files to configure the cluster machines.

Important

* The Ignition config files that the OpenShift Container Platform installation program generates contain certificates that expire after 24 hours, which the system then renews. If you shut down the cluster before the system renews the certificates and you later restart the cluster after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
* Use Ignition config files within 12 hours after you generate them, because the 24-hour certificate rotates from 16 to 22 hours after you install the cluster. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.

**Procedure**

1. Change to the directory that contains the OpenShift Container Platform installation program and generate the Kubernetes manifests for the cluster:

   ```
   $ ./openshift-install create manifests --dir <installation_directory>
   ```

   where:

   `<installation_directory>`
   :   Specifies the installation directory that contains the `install-config.yaml` file you created.
2. Remove the Kubernetes manifest files that define the control plane machines:

   ```
   $ rm -f <installation_directory>/openshift/99_openshift-cluster-api_master-machines-*.yaml
   ```

   By removing these files, you prevent the cluster from automatically generating control plane machines.
3. Remove the Kubernetes manifest files that define the control plane machine set:

   ```
   $ rm -f <installation_directory>/openshift/99_openshift-machine-api_master-control-plane-machine-set.yaml
   ```
4. Optional: If you do not want the cluster to provision compute machines, remove the Kubernetes manifest files that define the worker machines:

   ```
   $ rm -f <installation_directory>/openshift/99_openshift-cluster-api_worker-machineset-*.yaml
   ```

   Important

   If you disabled the `MachineAPI` capability when installing a cluster on user-provisioned infrastructure, you must remove the Kubernetes manifest files that define the worker machines. Otherwise, your cluster fails to install.

   Because you create and manage the worker machines yourself, you do not need to initialize these machines.
5. Verify that the `mastersSchedulable` parameter in the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` Kubernetes manifest file is set to `false`. This setting prevents pods from being scheduled on the control plane machines:

   1. Open the `<installation_directory>/manifests/cluster-scheduler-02-config.yml` file.
   2. Locate the `mastersSchedulable` parameter and verify that it is set to `false`.
   3. Save and exit the file.
6. Optional: If you do not want [the Ingress Operator](https://github.com/openshift/cluster-ingress-operator) to create DNS records on your behalf, remove the `privateZone` and `publicZone` sections from the `<installation_directory>/manifests/cluster-dns-02-config.yml` DNS configuration file:

   ```
   apiVersion: config.openshift.io/v1
   kind: DNS
   metadata:
     creationTimestamp: null
     name: cluster
   spec:
     baseDomain: example.openshift.com
     privateZone:
       id: mycluster-100419-private-zone
     publicZone:
       id: example.openshift.com
   status: {}
   ```

   `spec.privateZone`: Remove this section completely.

   If you do so, you must add ingress DNS records manually in a later step.
7. To create the Ignition configuration files, run the following command from the directory that contains the installation program:

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

### [11.7. Exporting common variables](#installation-restricted-networks-gcp-user-infra-exporting-common-variables) Copy linkLink copied to clipboard!

#### [11.7.1. Extracting the infrastructure name](#installation-extracting-infraid_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

To identify your cluster resources in Google Cloud, extract the unique infrastructure name from the Ignition config files.

The infrastructure name is also used to locate the appropriate Google Cloud resources during an OpenShift Container Platform installation. The provided Infrastructure Manager templates contain references to this infrastructure name, so you must extract it.

Warning

Do not run the `openshift-install create manifests` command again after creating any Google Cloud resources. Running the command again generates a new cluster identifier, which will cause errors in existing resources. If you need to regenerate the manifests because you modified the `install-config.yaml` file, delete any Google Cloud resources you created and recreate them with the new cluster identifier.

**Prerequisites**

* You installed the `jq` package.

**Procedure**

* To extract and view the infrastructure name from the Ignition config file metadata, run the following command:

  ```
  $ jq -r .infraID <installation_directory>/metadata.json
  ```

  where `<installation_directory>` is the path to the directory that you stored the installation files in.

  **Example output**

  ```
  openshift-vw9j6
  ```

  The output of this command is your cluster name and a random string.

#### [11.7.2. Exporting common variables for Infrastructure Manager templates](#installation-user-infra-exporting-common-variables_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must export a common set of variables that are used with the provided Infrastructure Manager templates used to assist in installing a cluster with user-provisioned infrastructure on Google Cloud.

Note

Specific Infrastructure Manager templates can also require additional exported variables, which are detailed in their related procedures.

**Procedure**

* Export the following common variables to be used by the provided Infrastructure Manager templates. For any command with `<installation_directory>`, specify the path to the directory that you stored the installation files in.

  + Export the `BASE_DOMAIN` variable by running the following command:

    ```
    $ export BASE_DOMAIN='<base_domain>'
    ```

    `<base_domain>`
    :   If you are installing a cluster into a shared VPC, specify the value for the host project.
  + Export the `BASE_DOMAIN_ZONE_NAME` variable by running the following command:

    ```
    $ export BASE_DOMAIN_ZONE_NAME='<base_domain_zone_name>'
    ```

    `<base_domain_zone_name>`
    :   Specifies the base domain zone name.
  + Export the `NETWORK_CIDR` variable by running the following command:

    ```
    $ export NETWORK_CIDR='<network_cidr>'
    ```

    `<network_cidr>`
    :   Specifies the network CIDR your cluster uses. For example, `10.0.0.0/16`.
  + Export the `MASTER_SUBNET_CIDR` variable by running the following command:

    ```
    $ export MASTER_SUBNET_CIDR='<master_subnet_cidr>'
    ```

    `<master_subnet_cidr>`
    :   Specifies the network CIDR that your cluster’s control plane uses. For example, `10.0.0.0/17`.
  + Export the `WORKER_SUBNET_CIDR` variable by running the following command:

    ```
    $ export WORKER_SUBNET_CIDR='<worker_subnet_cidr>'
    ```

    `<worker_subnet_cidr>`
    :   Specifies the network CIDR that your cluster’s compute machines use. For example, `10.0.128.0/17`.
  + Export the `KUBECONFIG` variable by running the following command:

    ```
    $ export KUBECONFIG=<installation_directory>/auth/kubeconfig
    ```
  + Export the `CLUSTER_NAME` variable by running the following command:

    ```
    $ export CLUSTER_NAME=`jq -r .clusterName <installation_directory>/metadata.json`
    ```
  + Export the `INFRA_ID` variable by running the following command:

    ```
    $ export INFRA_ID=`jq -r .infraID <installation_directory>/metadata.json`
    ```
  + Export the `PROJECT_NAME` variable by running the following command:

    ```
    $ export PROJECT_NAME=`jq -r .gcp.projectID <installation_directory>/metadata.json`
    ```
  + If you are installing a cluster into a shared VPC, export the `HOST_PROJECT` variable by running the following command:

    ```
    $ export HOST_PROJECT=<host_project_name>
    ```

    `<host_project_name>` specifies the name of the host project that contains the shared VPC.
  + If you are installing a cluster into a shared VPC, export the `HOST_PROJECT_ACCOUNT` variable by running the following command:

    ```
    $ export HOST_PROJECT_ACCOUNT=<host_project_account>
    ```

    `<host_project_account>` specifies the name of an account that can access the host project that contains the shared VPC.
  + Export the `REGION` variable by running the following command:

    ```
    $ export REGION=`jq -r .gcp.region <installation_directory>/metadata.json`
    ```
  + Export the `ZONE_0` variable by running the following command:

    ```
    $ export ZONE_0=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[0]' | cut -d "/" -f9)
    ```
  + Export the `ZONE_1` variable by running the following command:

    ```
    $ export ZONE_1=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[1]' | cut -d "/" -f9)
    ```
  + Export the `ZONE_2` variable by running the following command:

    ```
    $ export ZONE_2=$(gcloud compute regions describe ${REGION} --format=json | jq -r '.zones[2]' | cut -d "/" -f9)
    ```
  + Export the `SERVICE_ACCOUNT_EMAIL` variable by running the following command:

    ```
    $ export SERVICE_ACCOUNT_EMAIL="<service_account_email>"
    ```

    `<service_account_email>`
    :   Specifies the email address of the service account you used for the installation.
  + Export the `INSTALL_SERVICE_ACCOUNT` variable by running the following command:

    ```
    $ export INSTALL_SERVICE_ACCOUNT="projects/${PROJECT_NAME}/serviceAccounts/${SERVICE_ACCOUNT_EMAIL}"
    ```
  + Export the `CLUSTER_DOMAIN` variable by running the following command:

    ```
    $ export CLUSTER_DOMAIN="${CLUSTER_NAME}.${BASE_DOMAIN}"
    ```

### [11.8. Creating a VPC in Google Cloud](#installation-creating-gcp-vpc_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must create a VPC in Google Cloud for your OpenShift Container Platform cluster to use. You can customize the VPC to meet your requirements. One way to create the VPC is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided Infrastructure Manager template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* You have defined the variables in the *Exporting common variables* section.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for the VPC** section of this topic and save it as `01_vpc.tf` in a directory called `01_vpc` on your computer. This template describes the VPC that your cluster requires.
2. Create a VPC by running the following command:

   ```
   $ gcloud infra-manager deployments apply <vpc_deployment_name> \
     --location=${REGION} \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},master_subnet_cidr=${MASTER_SUBNET_CIDR},worker_subnet_cidr=${WORKER_SUBNET_CIDR} \
     --project=${PROJECT_NAME} \
     --local-source=./01_vpc \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<vpc_deployment_name>` specifies the name of the VPC deployment you create.
3. Configure environment variables that will be used to create other cluster infrastructure.

   1. Configure the `CLUSTER_NETWORK` environment variable by running the following command:

      ```
      $ export CLUSTER_NETWORK=$(gcloud compute networks describe ${INFRA_ID}-network --format json | jq -r .selfLink)
      ```
   2. Configure the `CONTROL_SUBNET` environment variable by running the following command:

      ```
      $ export CONTROL_SUBNET=$(gcloud compute networks subnets describe ${INFRA_ID}-master-subnet --region=${REGION} --format json | jq -r .selfLink)
      ```
   3. Configure the `COMPUTE_SUBNET` environment variable by running the following command:

      ```
      $ export COMPUTE_SUBNET=$(gcloud compute networks subnets describe ${INFRA_ID}-worker-subnet --region=${REGION} --format json | jq -r .selfLink)
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [11.8.1. Infrastructure Manager template for the VPC](#installation-infrastructure-manager-vpc_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the VPC that you need for your OpenShift Container Platform cluster:

**Example 11.25. `01_vpc.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "master_subnet_cidr" {
  type        = string
  description = "CIDR for the control plane subnet."
}

variable "worker_subnet_cidr" {
  type        = string
  description = "CIDR for the compute subnet."
}

resource "google_compute_network" "cluster_network" {
  provider = google-beta

  name = "${var.infra_id}-network"
  auto_create_subnetworks = false
}

resource "google_compute_subnetwork" "master_subnet" {
  provider = google-beta

  name = "${var.infra_id}-master-subnet"
  ip_cidr_range = "${var.master_subnet_cidr}"
  region = "${var.region}"
  network = google_compute_network.cluster_network.self_link
}

resource "google_compute_subnetwork" "worker_subnet" {
  provider = google-beta

  name = "${var.infra_id}-worker-subnet"
  ip_cidr_range = "${var.worker_subnet_cidr}"
  region = "${var.region}"
  network = google_compute_network.cluster_network.self_link
}

#tfimport-terraform import google_compute_router._router  __project__//-router
resource "google_compute_router" "router" {
  provider = google-beta

  name = "${var.infra_id}-router"
  network = google_compute_network.cluster_network.self_link
  region = "${var.region}"
}
resource "google_compute_router_nat" "master_nat" {
  provider = google-beta

  name = "${var.infra_id}-nat-master"
  source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"
  nat_ip_allocate_option = "AUTO_ONLY"
  min_ports_per_vm = 7168
  subnetwork {
    name = google_compute_subnetwork.master_subnet.self_link
    source_ip_ranges_to_nat = ["ALL_IP_RANGES"]
  }

  router = google_compute_router.router.name
  region = "${var.region}"

  depends_on = [
    google_compute_router.router
  ]
}
resource "google_compute_router_nat" "worker_nat" {
  provider = google-beta

  name = "${var.infra_id}-nat-worker"
  source_subnetwork_ip_ranges_to_nat = "LIST_OF_SUBNETWORKS"
  nat_ip_allocate_option = "AUTO_ONLY"
  min_ports_per_vm = 512
  subnetwork {
    name = google_compute_subnetwork.worker_subnet.self_link
    source_ip_ranges_to_nat = ["ALL_IP_RANGES"]
  }

  router = google_compute_router.router.name
  region = "${var.region}"

  depends_on = [
    google_compute_router.router
  ]
}
```

### [11.9. Networking requirements for user-provisioned infrastructure](#installation-network-user-infra_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must configure networking for all the Red Hat Enterprise Linux CoreOS (RHCOS) machines in `initramfs` during boot, so that they can fetch their Ignition config files.

#### [11.9.1. Setting the cluster node hostnames through DHCP](#installation-host-names-dhcp-user-infra_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

On Red Hat Enterprise Linux CoreOS (RHCOS) machines, the hostname is set through NetworkManager. By default, the machines obtain their hostname through DHCP. If the hostname is not provided by DHCP, set statically through kernel arguments, or another method, it is obtained through a reverse DNS lookup. Reverse DNS lookup occurs after the network has been initialized on a node and can take time to resolve. Other system services can start prior to this and detect the hostname as `localhost` or similar. You can avoid this by using DHCP to provide the hostname for each cluster node.

Additionally, setting the hostnames through DHCP can bypass any manual DNS record name configuration errors in environments that have a DNS split-horizon implementation.

#### [11.9.2. Network connectivity requirements](#installation-network-connectivity-user-infra_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must configure the network connectivity between machines to allow OpenShift Container Platform cluster components to communicate. Each machine must be able to resolve the hostnames of all other machines in the cluster.

This section provides details about the ports that are required.

Expand

Table 11.7. Ports used for all-machine to all-machine communications

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

Table 11.8. Ports used for all-machine to control plane communications

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | `6443` | Kubernetes API |

Show more

Expand

Table 11.9. Ports used for control plane machine to control plane machine communications

| Protocol | Port | Description |
| --- | --- | --- |
| TCP | `2379`-`2380` | etcd server and peer ports |

Show more

### [11.10. Creating load balancers in Google Cloud](#installation-creating-gcp-lb_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must configure load balancers in Google Cloud for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* You have defined the variables in the *Exporting common variables* section.
* If you are not installing a cluster into a shared VPC, you have defined the variables in the *Creating a VPC in Google Cloud* section.

**Procedure**

1. If you are installing a cluster into a shared VPC, set environment variables for the cluster network and control plane subnet.

   1. Determine the shared VPC network name by running the following command:

      ```
      $ gcloud compute networks list
      ```
   2. Set the `CLUSTER_NETWORK` variable by running the following command:

      ```
      $ export CLUSTER_NETWORK=$(gcloud compute networks describe <network_name> --format json | jq -r .selfLink)
      ```

      `<network_name>` specifies the name of the network you determined.
   3. List the available network subnets by running the following command:

      ```
      $ gcloud compute networks subnets list --network=<network_name>
      ```

      `<network_name>` specifies the name of the network you determined.
   4. Select a subnet from the list, and set the `CONTROL_SUBNET` variable by running the following command:

      ```
      $ export CONTROL_SUBNET=<control_subnet>
      ```

      `<control_subnet>` specifies the name of the subnet you selected from the list of subnets.
2. Copy the template from the **Infrastructure Manager template for the internal load balancer** section of this topic and save it as `02_lb_int.tf` in a directory called `02_lb_int` on your computer. This template describes the internal load balancing objects that your cluster requires.

   1. Create an internal load balancer by running the following command:

      ```
      $ gcloud infra-manager deployments apply <internal_lb_deployment_name> \
        --location=${REGION} \
        --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_network=${CLUSTER_NETWORK},control_subnet=${CONTROL_SUBNET},zone_0=${ZONE_0},zone_1=${ZONE_1},zone_2=${ZONE_2} \
        --project=${PROJECT_NAME} \
        --local-source=./02_lb_int \
        --service-account=${INSTALL_SERVICE_ACCOUNT}
      ```

      `<internal_lb_deployment_name>` specifies the name of the internal load balancer deployment you create.
   2. Export the `CLUSTER_IP` variable by running the following command:

      ```
      $ export CLUSTER_IP=$(gcloud compute addresses describe ${INFRA_ID}-cluster-ip --region=${REGION} --format json | jq -r .address)
      ```
3. Optional: For a public or externally available cluster, copy the template from the **Infrastructure Manager template for the external load balancer** section of this topic and save it as `02_lb_ext.tf` in a directory called `02_lb_ext` on your computer. This template describes the external load balancing objects that your cluster requires.

   1. Create an external load balancer by running the following command:

      ```
      $ gcloud infra-manager deployments apply <external_lb_deployment_name> \
        --location=${REGION} \
        --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION} \
        --project=${PROJECT_NAME} \
        --local-source=./02_lb_ext \
        --service-account=${INSTALL_SERVICE_ACCOUNT}
      ```

      `<external_lb_deployment_name>` specifies the name of the external load balancer deployment you create.
   2. Export the `CLUSTER_PUBLIC_IP` variable by running the following command:

      ```
      $ export CLUSTER_PUBLIC_IP=$(gcloud compute addresses describe ${INFRA_ID}-cluster-public-ip --region=${REGION} --format json | jq -r .address)
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [11.10.1. Infrastructure Manager template for the external load balancer](#installation-infrastructure-manager-ext-lb_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the external load balancer that you need for your OpenShift Container Platform cluster:

**Example 11.26. `02_lb_ext.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}
variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}
variable "project" {
  type        = string
  description = "Project ID"
}
variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

resource "google_compute_address" "cluster_public_ip" {
  provider = google-beta

  name = "${var.infra_id}-cluster-public-ip"
  region = "${var.region}"
}

resource "google_compute_http_health_check" "api_http_health_check" {
  provider = google-beta

  name = "${var.infra_id}-api-http-health-check"
  port = 6080
  request_path = "/readyz"
}

resource "google_compute_target_pool" "api_target_pool" {
  provider = google-beta

  name = "${var.infra_id}-api-target-pool"
  region = "${var.region}"
  health_checks = [
    google_compute_http_health_check.api_http_health_check.id
  ]
}

resource "google_compute_forwarding_rule" "api_forwarding_rule" {
  provider = google-beta

  name = "${var.infra_id}-api-forwarding-rule"
  ip_address = google_compute_address.cluster_public_ip.address
  port_range = "6443"
  region = "${var.region}"
  target = google_compute_target_pool.api_target_pool.id
}
```

#### [11.10.2. Infrastructure Manager template for the internal load balancer](#installation-infrastructure-manager-int-lb_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the internal load balancer that you need for your OpenShift Container Platform cluster:

**Example 11.27. `02_lb_int.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}
variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}
variable "project" {
  type        = string
  description = "Project ID"
}
variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}
variable "control_subnet" {
  type        = string
  description = "Subnet for the control plane instances."
}
variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

# Terraform handles lists but the infra-manager --input-values only
# supports scalar types.
# If you require more or less zones, you must manually add them below
# as a single variable for each. You must add the zones to the
# locals `zones` list below.
variable "zone_0" {
  type        = string
  description = "Zone 1 for the instance types."
}

variable "zone_1" {
  type        = string
  description = "Zone 2 for the instance types."
}

variable "zone_2" {
  type        = string
  description = "Zone 3 for the instance types."
}

locals {
  zones = ["${var.zone_0}", "${var.zone_1}", "${var.zone_2}"]
}

resource "google_compute_address" "cluster_ip" {
  provider = google-beta

  name = "${var.infra_id}-cluster-ip"
  address_type = "INTERNAL"
  region = "${var.region}"
  subnetwork = "${var.control_subnet}"
}

resource "google_compute_health_check" "api_internal_health_check" {
  provider = google-beta

  name = "${var.infra_id}-api-internal-health-check"
  https_health_check {
    port = 6443
  }
}

resource "google_compute_region_backend_service" "api_internal" {
  provider = google-beta

  name = "${var.infra_id}-api-internal"
  timeout_sec = 120
  protocol = "TCP"
  region = "${var.region}"
  load_balancing_scheme = "INTERNAL"
  health_checks = [
    google_compute_health_check.api_internal_health_check.id
  ]

  dynamic "backend" {
    for_each = google_compute_instance_group.master_ig

    content {
      balancing_mode = "CONNECTION"
      group = backend.value.self_link
    }
  }
}

resource "google_compute_forwarding_rule" "api_internal_forwarding_rule" {
  provider = google-beta

  name = "${var.infra_id}-api-internal-forwarding-rule"
  ip_address = google_compute_address.cluster_ip.address
  backend_service = google_compute_region_backend_service.api_internal.id
  load_balancing_scheme = "INTERNAL"
  ports = [
    "6443",
    "22623"
  ]
  region = "${var.region}"
  subnetwork = "${var.control_subnet}"
}

resource "google_compute_instance_group" "master_ig" {
  provider = google-beta

  for_each = toset(local.zones)

  name = "${var.infra_id}-master-${each.key}-ig"
  network = "${var.cluster_network}"
  zone = "${each.key}"
  named_port {
    name = "ignition"
    port = 22623
  }
  named_port {
    name = "https"
    port = 6443
  }
}
```

### [11.11. Creating a private DNS zone in Google Cloud](#installation-creating-gcp-private-dns_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must configure a private DNS zone in Google Cloud for your OpenShift Container Platform cluster to use. One way to create this component is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for the private DNS** section of this topic and save it as `02_dns.tf` in a folder called `02_dns` on your computer. This template describes the private DNS objects that your cluster requires.
2. If you are installing a cluster into a shared VPC, and the host project already has a private DNS zone, skip this step. Create the DNS zone by running the following command:

   ```
   $ gcloud infra-manager deployments apply <dns_zone_deployment_name> \
     --location=${REGION} \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_domain=${CLUSTER_DOMAIN},cluster_network=${CLUSTER_NETWORK} \
     --project=${PROJECT_NAME} \
     --local-source=./02_dns \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<dns_zone_deployment_name>` specifies the name of the DNS zone deployment you create.
3. The templates do not create DNS entries due to limitations of Infrastructure Manager, so you must create them manually:

   1. Add the internal DNS entries by running the following commands:

      ```
      $ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
      ```

      ```
      $ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone
      ```

      ```
      $ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone
      ```

      ```
      $ gcloud dns record-sets transaction add ${CLUSTER_IP} --name api-int.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${INFRA_ID}-private-zone
      ```

      ```
      $ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone
      ```
   2. For an external cluster, also add the external DNS entries by running the following commands:

      ```
      $ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
      ```

      ```
      $ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
      ```

      ```
      $ gcloud dns record-sets transaction add ${CLUSTER_PUBLIC_IP} --name api.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 60 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
      ```

      ```
      $ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [11.11.1. Infrastructure Manager template for the private DNS](#installation-infrastructure-manager-private-dns_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the private DNS that you need for your OpenShift Container Platform cluster:

**Example 11.28. `02_dns.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "cluster_domain" {
  type        = string
  description = "ClusterName.BaseDomain"
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

resource "google_dns_managed_zone" "private_zone" {
  provider = google-beta

  name = "${var.infra_id}-private-zone"
  dns_name = "${var.cluster_domain}."
  description = "OpenShift Installer UPI create private DNS zone."
  visibility = "private"
  private_visibility_config {
    networks {
      network_url = "${var.cluster_network}"
    }
  }

  force_destroy = false
}
```

### [11.12. Creating firewall rules and IAM roles in Google Cloud](#installation-creating-gcp-firewall-rules-vpc_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must create firewall rules and IAM roles in Google Cloud for your OpenShift Container Platform cluster to use. One way to create these components is to modify the provided Infrastructure Manager template. If you are installing a cluster into a shared VPC and the host project already has the necessary firewall rules and IAM roles, you can skip creating these resources.

Note

If you do not use the provided Infrastructure Manager template to create your Google Cloud infrastructure, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for firewall rules and IAM roles** section of this topic and save it as `03_security.tf` in a folder called `03_security` on your computer. This template describes the security groups that your cluster requires.
2. Create the firewall rules and IAM roles by running the following command:

   ```
   $ gcloud infra-manager deployments apply <security_deployment_name> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./03_security \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},cluster_network=${CLUSTER_NETWORK},network_cidr=${NETWORK_CIDR} \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<security_deployment_name>` specifies the name of the deployment of firewall rules and IAM roles.
3. Configure service account variables based on the roles you created by running the following commands:

   ```
   $ export MASTER_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter "email~^${INFRA_ID}-m@${PROJECT_NAME}." --format json | jq -r '.[0].email')
   ```

   ```
   $ export WORKER_SERVICE_ACCOUNT=$(gcloud iam service-accounts list --filter "email~^${INFRA_ID}-w@${PROJECT_NAME}." --format json | jq -r '.[0].email')
   ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [11.12.1. Infrastructure Manager template for firewall rules and IAM roles](#installation-infrastructure-manager-firewall-rules_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the firewall rules and IAM roles that you need for your OpenShift Container Platform cluster:

**Example 11.29. `03_security.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

variable "network_cidr" {
  type        = string
  description = "CIDR for network of the cluster."
}

variable "allowed_external_cidr" {
  type        = string
  description = "Allowed external CIDR for firewall rule."
  default     = "0.0.0.0/0"
}

resource "google_compute_firewall" "bootstrap_in_ssh" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap-in-ssh"
  source_ranges = [
    "${var.allowed_external_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-bootstrap"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["22"]
  }
}

resource "google_compute_firewall" "api" {
  provider = google-beta

  name = "${var.infra_id}-api"
  source_ranges = [
   "${var.allowed_external_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["6443"]
  }
}

resource "google_compute_firewall" "health_checks" {
  provider = google-beta

  name = "${var.infra_id}-health-checks"
  source_ranges = [
    "35.191.0.0/16",
    "130.211.0.0/22",
    "209.85.152.0/22",
    "209.85.204.0/22"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["6080", "6443", "22624"]
  }
}

resource "google_compute_firewall" "etcd" {
  provider = google-beta

  name = "${var.infra_id}-etcd"
  source_tags = [
    "${var.infra_id}-master"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["2379-2380"]
  }
}

resource "google_compute_firewall" "control_plane" {
  provider = google-beta

  name = "${var.infra_id}-control-plane"
  source_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  target_tags = [
    "${var.infra_id}-master"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "tcp"
    ports = ["10257"]
  }
  allow {
    protocol = "tcp"
    ports = ["10259"]
  }
  allow {
    protocol = "tcp"
    ports = ["22623"]
  }
}

resource "google_compute_firewall" "internal_network" {
  provider = google-beta

  name = "${var.infra_id}-internal-network"
  source_ranges = [
    "${var.network_cidr}"
  ]
  target_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "icmp"
  }
  allow {
    protocol = "tcp"
    ports = ["22"]
  }
}

resource "google_compute_firewall" "internal_cluster" {
  provider = google-beta

  name = "${var.infra_id}-internal-cluster"
  source_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  target_tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-worker"
  ]
  network = "${var.cluster_network}"
  allow {
    protocol = "udp"
    ports = ["4789", "6081"]
  }
  allow {
    protocol = "udp"
    ports = ["500", "4500"]
  }
  allow {
    protocol = "esp"
  }
  allow {
    protocol = "tcp"
    ports = ["9000-9999"]
  }
  allow {
    protocol = "udp"
    ports = ["9000-9999"]
  }
  allow {
    protocol = "tcp"
    ports = ["10250"]
  }
  allow {
    protocol = "tcp"
    ports = ["30000-32767"]
  }
  allow {
    protocol = "udp"
    ports = ["30000-32767"]
  }
}

resource "google_service_account" "master_node_sa" {
  provider = google-beta

  account_id = "${var.infra_id}-m"
  display_name = "${var.infra_id}-master-node"
}

resource "google_service_account" "worker_node_sa" {
  provider = google-beta

  account_id = "${var.infra_id}-w"
  display_name = "${var.infra_id}-worker-node"
}
```

### [11.13. Creating IAM policy bindings in Google Cloud](#installation-creating-gcp-iam-shared-vpc_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must create IAM policy bindings in Google Cloud for your OpenShift Container Platform cluster to use.

**Prerequisites**

* You have defined the variables in the *Exporting common variables* section.

**Procedure**

1. Export the variable for the subnet that hosts the compute machines by running the following command:

   ```
   $ export COMPUTE_SUBNET=(`gcloud compute networks subnets describe ${INFRA_ID}-worker-subnet --region=${REGION} --format json | jq -r .selfLink`)
   ```
2. The templates do not create the policy bindings due to limitations of Infrastructure Manager, so you must create them manually by running the following commands:

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.instanceAdmin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.networkAdmin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/compute.securityAdmin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/iam.serviceAccountUser"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${MASTER_SERVICE_ACCOUNT}" --role "roles/storage.admin"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/compute.viewer"
   ```

   ```
   $ gcloud projects add-iam-policy-binding ${PROJECT_NAME} --member "serviceAccount:${WORKER_SERVICE_ACCOUNT}" --role "roles/storage.admin"
   ```
3. Create a service account key and store it locally for later use by running the following command:

   ```
   $ gcloud iam service-accounts keys create service-account-key.json --iam-account=${MASTER_SERVICE_ACCOUNT}
   ```

### [11.14. Creating the RHCOS cluster image for the Google Cloud infrastructure](#installation-gcp-user-infra-rhcos_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must use a valid Red Hat Enterprise Linux CoreOS (RHCOS) image for Google Cloud for your OpenShift Container Platform nodes.

**Prerequisites**

* You have downloaded the `openshift-install` binary.

**Procedure**

1. Obtain the image name by running the following command:

   ```
   $ source_image=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.gcp.name')
   ```
2. Obtain the project name by running the following command:

   ```
   $ source_project=$(openshift-install coreos print-stream-json | jq -r '.architectures.x86_64.images.gcp.project')
   ```
3. Create the image by running the following command:

   ```
   $ gcloud compute images create "${INFRA_ID}-rhcos-image" \
       --source-image="${source_image}" --source-image-project="${source_project}"
   ```

### [11.15. Creating the bootstrap machine in Google Cloud](#installation-creating-gcp-bootstrap_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must create the bootstrap machine in Google Cloud to use during OpenShift Container Platform cluster initialization. One way to create this machine is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided Infrastructure Manager template to create your bootstrap machine, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

If you need to redeploy the bootstrap machine for any reason, delete the existing bootstrap VM first. If you redeploy the bootstrap machine without deleting the existing VM, Infrastructure Manager will update the metadata and appear to succeed, but the Ignition file will not be executed again. This will result in the VM still being based on the old Ignition data.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for the bootstrap machine** section of this topic and save it as `04_bootstrap.tf` in a folder called `04_bootstrap` on your computer. This template describes the bootstrap machine that your cluster requires.

   * You can edit the `04_bootstrap.tf` file to add additional tags to the bootstrap machine, by modifying the existing `tags` stanza as follows:

     ```
     resource "google_compute_instance" "bootstrap" {
     # ...
       tags = [
         "${var.infra_id}-master",
         "${var.infra_id}-bootstrap",
         "custom-tag-example"
       ]
     # ...
     }
     ```
2. Export the location of the Red Hat Enterprise Linux CoreOS (RHCOS) image that the installation program requires by running the following command:

   ```
   $ export CLUSTER_IMAGE=(`gcloud compute images describe ${INFRA_ID}-rhcos-image --format json | jq -r .selfLink`)
   ```
3. Create a bucket by running the following command:

   ```
   $ gcloud storage buckets create "gs://${INFRA_ID}-bootstrap-ignition"
   ```
4. Upload the `bootstrap.ign` file by running the following command:

   ```
   $ gcloud storage cp bootstrap.ign "gs://${INFRA_ID}-bootstrap-ignition/"
   ```
5. Create a signed URL for the bootstrap instance and export the URL from the output as a variable by running the following command:

   ```
   $ export BOOTSTRAP_IGN="$(gcloud storage sign-url --duration=2h --private-key-file=service-account-key.json "gs://${INFRA_ID}-bootstrap-ignition/bootstrap.ign" | grep "^signed_url:" | awk '{print $2}')"
   ```
6. Create the bootstrap deployment by running the following command:

   ```
   $ gcloud infra-manager deployments apply <bootstrap_deployment_name> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./04_bootstrap \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone=${ZONE_0},cluster_network=${CLUSTER_NETWORK},subnet=${CONTROL_SUBNET},image=${CLUSTER_IMAGE},bootstrap_ign="${BOOTSTRAP_IGN}",is_public_cluster=<public_cluster_status> \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   where:

   `<bootstrap_deployment_name>`
   :   Specifies the name of the bootstrap deployment.

   `<public_cluster_status>`
   :   Specifies whether the cluster is public or private. If it is a public cluster, specify `true`. If it is a private cluster, specify `false`.
7. The templates do not manage load balancer membership due to limitations of Infrastructure Manager, so you must add the bootstrap machine manually.

   1. Add the bootstrap instance to the internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances \
          ${INFRA_ID}-bootstrap-ig --zone=${ZONE_0} --instances=${INFRA_ID}-bootstrap
      ```
   2. Add the bootstrap instance group to the internal load balancer backend service by running the following command:

      ```
      $ gcloud compute backend-services add-backend \
          ${INFRA_ID}-api-internal --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [11.15.1. Infrastructure Manager template for the bootstrap machine](#installation-infrastructure-manager-bootstrap_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the bootstrap machine that you need for your OpenShift Container Platform cluster:

**Example 11.30. `04_bootstrap.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

variable "zone" {
  type        = string
  description = "Zone inside of the region where the bootstrap node is created."
}

variable "cluster_network" {
  type        = string
  description = "Full link to the cluster network."
}

variable "subnet" {
  type        = string
  description = "Control plane subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the bootstrap machine."
  default     = "n1-standard-4"
}

variable "root_volume_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "bootstrap_ign" {
  type        = string
  description = "Bootstrap ignition data."
}

variable "is_public_cluster" {
  type        = bool
  default     = true
  description = "Whether the publish policy is the default External"
}

resource "google_compute_address" "bootstrap_public_ip" {
  provider = google-beta
  count = var.is_public_cluster ? 1 : 0

  name = "${var.infra_id}-bootstrap-public-ip"
  region = "${var.region}"
}

resource "google_compute_instance" "bootstrap" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap"
  zone = "${var.zone}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master",
    "${var.infra_id}-bootstrap"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.root_volume_size}"
      image = "${var.image}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"

    # Dynamic block to conditionally create access_config
    dynamic "access_config" {
      for_each = var.is_public_cluster ? [1] : []
      content {
        nat_ip = google_compute_address.bootstrap_public_ip[0].address
      }
    }
  }
  metadata = {
    user-data = "{\"ignition\":{\"config\":{\"replace\":{\"source\":\"${var.bootstrap_ign}\"}},\"version\":\"3.2.0\"}}"
  }
}

resource "google_compute_instance_group" "bootstrap_ig" {
  provider = google-beta

  name = "${var.infra_id}-bootstrap-ig"
  network = "${var.cluster_network}"
  zone = "${var.zone}"
  named_port {
    name = "ignition"
    port = 22623
  }
  named_port {
    name = "https"
    port = 6443
  }
}
```

### [11.16. Creating the control plane machines in Google Cloud](#installation-creating-gcp-control-plane_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You must create the control plane machines in Google Cloud for your cluster to use. One way to create these machines is to modify the provided Infrastructure Manager template.

Note

If you do not use the provided template to create your control plane machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

**Prerequisites**

* You defined the variables in the *Exporting common variables*, *Creating load balancers in Google Cloud*, *Creating IAM roles in Google Cloud*, and *Creating the bootstrap machine in Google Cloud* sections.
* You created the bootstrap machine.
* You created the Ignition configuration files.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for control plane machines** section of this topic and save it as `05_control_plane.tf` in a folder called `05_control_plane` on your computer. This template describes the control plane machines that your cluster requires.

   * You can edit the `05_control_plane.tf` file to add additional tags to the control plane machines, by modifying the existing `tags` stanza. The following example adds a custom tag to the first control plane machine, which is named `master_0`:

     ```
     resource "google_compute_instance" "master_0" {
     # ...
       tags = [
         "${var.infra_id}-master",
         "custom_tag_example"
       ]
     # ...
     }
     ```
2. Copy the `master.ign` file from your installation directory into the `05_control_plane` folder by running the following command:

   ```
   $ cp <installation_directory>/master.ign 05_control_plane/master.ign
   ```

   `<installation_directory>` specifies the directory where you created the Ignition configuration files.
3. Create the control plane deployment by running the following command:

   ```
   $ gcloud infra-manager deployments apply <control_plane_deployment> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./05_control_plane \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone_0=${ZONE_0},zone_1=${ZONE_1},zone_2=${ZONE_2},subnet=${CONTROL_SUBNET},image=${CLUSTER_IMAGE},service_account_email=${MASTER_SERVICE_ACCOUNT} \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<control_plane_deployment>` specifies the name of the control plane deployment.
4. Delete the temporary ignition file from the `05_control_plane` folder by running the following command:

   ```
   $ rm 05_control_plane/master.ign
   ```
5. The templates do not manage load balancer membership due to limitations of Infrastructure Manager, so you must add the control plane machines manually.

   1. Add the first control plane machine to an internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_0}-ig --zone=${ZONE_0} --instances=${INFRA_ID}-master-0
      ```
   2. Add the second control plane machine to an internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_1}-ig --zone=${ZONE_1} --instances=${INFRA_ID}-master-1
      ```
   3. Add the third control plane machine to an internal load balancer instance group by running the following command:

      ```
      $ gcloud compute instance-groups unmanaged add-instances ${INFRA_ID}-master-${ZONE_2}-ig --zone=${ZONE_2} --instances=${INFRA_ID}-master-2
      ```
6. For an external cluster, you must also add the control plane machines to external load balancer target pools.

   1. Add the first control plane machine to an external load balancer pool by running the following command:

      ```
      $ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_0}" --instances=${INFRA_ID}-master-0
      ```
   2. Add the second control plane machine to an external load balancer pool by running the following command:

      ```
      $ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_1}" --instances=${INFRA_ID}-master-1
      ```
   3. Add the third control plane machine to an external load balancer pool by running the following command:

      ```
      $ gcloud compute target-pools add-instances ${INFRA_ID}-api-target-pool --instances-zone="${ZONE_2}" --instances=${INFRA_ID}-master-2
      ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [11.16.1. Infrastructure Manager template for control plane machines](#installation-infrastructure-manager-control-plane_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the control plane machines that you need for your OpenShift Container Platform cluster:

**Example 11.31. `05_control_plane.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
    google-beta = {
        source = "hashicorp/google-beta",
        version = ">= 4.0.0"
    }
    local = {
        source = "hashicorp/local",
        version = ">= 2.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

# Terraform handles lists but the infra-manager --input-values only
# supports scalar types.
# If you require more or less zones, you must manually add them below
# as a single variable for each. You must add the zones to the
# locals `zones` list below.
variable "zone_0" {
  type        = string
  description = "Zone 1 for the instance types."
}

variable "zone_1" {
  type        = string
  description = "Zone 2 for the instance types."
}

variable "zone_2" {
  type        = string
  description = "Zone 3 for the instance types."
}

variable "subnet" {
  type        = string
  description = "Control plane subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the control plane machine."
  default     = "n1-standard-4"
}

variable "disk_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "disk_type" {
  type        = string
  description = "Type of storage disk for the vm."
  default     = "pd-ssd"
}

variable "service_account_email" {
  type        = string
  description = "Email for the service account attached to the control planes."
}

data "local_file" "ignition_file" {
  filename = "${path.module}/master.ign"
}

resource "google_compute_instance" "master_0" {
  provider = google-beta

  name = "${var.infra_id}-master-0"
  zone = "${var.zone_0}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

resource "google_compute_instance" "master_1" {
  provider = google-beta

  name = "${var.infra_id}-master-1"
  zone = "${var.zone_1}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

resource "google_compute_instance" "master_2" {
  provider = google-beta

  name = "${var.infra_id}-master-2"
  zone = "${var.zone_2}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-master"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}
```

### [11.17. Creating additional worker machines in Google Cloud](#installation-creating-gcp-worker_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can create worker machines in Google Cloud for your cluster by using the Infrastructure Manager template. You can adjust the number of machines by modifying the number of `google_compute_instance` resources in the provided template.

Note

If you do not use the provided Infrastructure Manager template to create your compute machines, you must review the provided information and manually create the infrastructure. If your cluster does not initialize correctly, you might have to contact Red Hat support with your installation logs.

If you are installing a three-node cluster, skip this step. A three-node cluster consists of three control plane machines, which also act as compute machines.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables*, *Creating load balancers in Google Cloud*, and *Creating the bootstrap machine in Google Cloud* sections.
* Create the bootstrap machine.
* Create the control plane machines.

**Procedure**

1. Copy the template from the **Infrastructure Manager template for worker machines** section of this topic and save it as `06_worker.tf` in a folder called `06_worker` on your computer. This template describes the worker machines that your cluster requires.

   * You can edit the `06_worker.tf` file to add additional tags to the compute machines, by modifying the existing `tags` stanza as follows:

     ```
     resource "google_compute_instance" "worker_0" {
     # ...
       tags = [
         "${var.infra_id}-worker-0",
         "custom-tag-example"
       ]
     # ...
     }
     ```
2. Copy the `worker.ign` file from your installation directory into the `06_worker` folder by running the following command:

   ```
   $ cp <installation_directory>/worker.ign 06_worker/worker.ign
   ```

   `<installation_directory>` specifies the directory where you created the Ignition configuration files.
3. Create the deployment by running the following command:

   ```
   $ gcloud infra-manager deployments apply <worker_deployment_name> \
     --location=${REGION} \
     --project=${PROJECT_NAME} \
     --local-source=./06_worker \
     --input-values=infra_id=${INFRA_ID},project=${PROJECT_NAME},region=${REGION},zone_0=${ZONE_0},zone_1=${ZONE_1},subnet=${COMPUTE_SUBNET},image=${CLUSTER_IMAGE},service_account_email=${WORKER_SERVICE_ACCOUNT} \
     --service-account=${INSTALL_SERVICE_ACCOUNT}
   ```

   `<worker_deployment_name>` specifies the name of the deployment.
4. Remove the `worker.ign` file by running the following command:

   ```
   $ rm 06_worker/worker.ign
   ```

**Verification**

1. Verify the deployment is active by running the following command:

   ```
   $ gcloud infra-manager deployments describe <deployment_name> --format='value(state)'
   ```

   Replace `<deployment_name>` with the name of the deployment you created.

   **Example output**

   ```
   ACTIVE
   ```

#### [11.17.1. Infrastructure Manager template for worker machines](#installation-infrastructure-manager-worker_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

You can use the following Infrastructure Manager template to deploy the worker machines that you need for your OpenShift Container Platform cluster:

**Example 11.32. `06_worker.tf` Infrastructure Manager template**

```
terraform {
  # Infra manager supports specific Terraform versions; ensure compatibility
  required_version = ">=1.2.3"
  required_providers {
    google = {
      source = "hashicorp/google"
      version = ">= 4.0.0"
    }
  }
}

provider "google-beta" {
  project = "${var.project}"
  region = "${var.region}"
}

variable "infra_id" {
  type        = string
  description = "OpenShift Installer Infrastructure ID"
}

variable "project" {
  type        = string
  description = "Project ID"
}

variable "region" {
  type        = string
  description = "GCP Region where the resources will be created."
  default     = "us-central1"
}

# Terraform handles lists but the infra-manager --input-values only
# supports scalar types.
# If you require more or less zones, you must manually add them below
# as a single variable for each. You must add the zones to the
# locals `zones` list below.
variable "zone_0" {
  type        = string
  description = "Zone 1 for the instance types."
}

variable "zone_1" {
  type        = string
  description = "Zone 2 for the instance types."
}

variable "subnet" {
  type        = string
  description = "Compute subnet."
}

variable "image" {
  type        = string
  description = "Cluster Image."
}

variable "machine_type" {
  type        = string
  description = "Machine type for the compute machine."
  default     = "n1-standard-4"
}

variable "disk_size" {
  type        = string
  description = "Size in GB for the root volume."
  default     = "128"
}

variable "disk_type" {
  type        = string
  description = "Type of storage disk for the vm."
  default     = "pd-ssd"
}

variable "service_account_email" {
  type        = string
  description = "Email for the service account attached to the compute nodes."
}

data "local_file" "ignition_file" {
  filename = "${path.module}/worker.ign"
}

resource "google_compute_instance" "worker_0" {
  provider = google-beta

  name = "${var.infra_id}-worker-0"
  zone = "${var.zone_0}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-worker"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}

resource "google_compute_instance" "worker_1" {
  provider = google-beta

  name = "${var.infra_id}-worker-1"
  zone = "${var.zone_1}"
  machine_type = "${var.machine_type}"
  tags = [
    "${var.infra_id}-worker"
  ]
  boot_disk {
    auto_delete = true
    initialize_params {
      size = "${var.disk_size}"
      image = "${var.image}"
      type = "${var.disk_type}"
    }
  }
  network_interface {
    subnetwork = "${var.subnet}"
  }
  metadata = {
    user-data = data.local_file.ignition_file.content
  }
  service_account {
    email = "${var.service_account_email}"
    scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
}
```

### [11.18. Removing bootstrap resources in Google Cloud](#installation-gcp-user-infra-wait-for-bootstrap_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

After you create all of the required infrastructure in Google Cloud, wait for the bootstrap process to complete on the machines that you provisioned by using the Ignition config files. The installation program created the Ignition config files.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* and *Creating load balancers in Google Cloud* sections.
* Create the bootstrap machine.
* Create the control plane machines.

**Procedure**

1. Change to the directory that includes the installation program and run the following command:

   ```
   $ ./openshift-install wait-for bootstrap-complete --dir <installation_directory> \
   ```

   1

   ```
       --log-level info
   ```

   2

   [1](#CO25-1)
   :   For `<installation_directory>`, specify the path to the directory where you stored the installation files.

   [2](#CO25-2)
   :   To view different installation details, specify `warn`, `debug`, or `error` instead of `info`.

   If the command exits without a `FATAL` warning, your production control plane has initialized.
2. To remove the bootstrap instance group from the backend services' backends, run the following commands:

   ```
   $ gcloud compute backend-services remove-backend ${INFRA_ID}-api-internal --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
   ```

   ```
   $ ingress_backendservice=$(gcloud compute backend-services list --filter="backends.group~${INFRA_ID}" --format='value(name)' | grep -v "${INFRA_ID}")
   ```

   1. If `ingress_backendservice` is not empty, run the following `describe` command for the bootstrap group:

      ```
      $ gcloud compute backend-services describe ${ingress_backendservice} --region=${REGION}
      ```
   2. If the `describe` command displays that the bootstrap group is one of its backends, run the following `remove-backend` command to remove the bootstrap group from the backends:

      ```
      $ gcloud compute backend-services remove-backend ${ingress_backendservice} --region=${REGION} --instance-group=${INFRA_ID}-bootstrap-ig --instance-group-zone=${ZONE_0}
      ```
   3. To remove the bucket and the deployment, run the following commands:

      ```
      $ gcloud storage rm "gs://${INFRA_ID}-bootstrap-ignition/bootstrap.ign"
      ```

      ```
      $ gcloud storage rm --recursive "gs://${INFRA_ID}-bootstrap-ignition/"
      ```

      ```
      $ gcloud infra-manager deployments delete <bootstrap_deployment_name> \
          --project=${PROJECT_NAME} --location=${REGION} --quiet
      ```

      Specify the name of the bootstrap deployment you created for `<bootstrap_deployment_name>`.

### [11.19. Logging in to the cluster by using the CLI](#cli-logging-in-kubeadmin_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

To log in to your cluster as the default system user, export the `kubeconfig` file. This configuration enables the CLI to authenticate and connect to the specific API server created during OpenShift Container Platform installation.

The `kubeconfig` file is specific to a cluster and OpenShift Container Platform generates it during installation.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* Ensure the bootstrap process completed successfully.

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

### [11.20. Disabling the default software catalog sources](#olm-restricted-networks-operatorhub_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

To use only trusted or locally available Operator catalogs, disable the default software catalog sources that OpenShift Container Platform configures during installation. In a restricted network environment, you must disable the default catalogs as a cluster administrator.

**Procedure**

* Disable the sources for the default catalogs by adding `disableAllDefaultSources: true` to the `OperatorHub` object:

  ```
  $ oc patch OperatorHub cluster --type json \
      -p '[{"op": "add", "path": "/spec/disableAllDefaultSources", "value": true}]'
  ```

  Tip

  Or, you can use the web console to manage catalog sources. From the **Administration** → **Cluster Settings** → **Configuration** → **OperatorHub** page, click the **Sources** tab, where you can create, update, delete, disable, and enable individual sources.

### [11.21. Approving the certificate signing requests for your machines](#installation-approve-csrs_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

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

### [11.22. Optional: Adding the ingress DNS records](#installation-gcp-user-infra-adding-ingress_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

If you removed the DNS zone configuration when creating Kubernetes manifests and generating Ignition configs, you must manually create DNS records that point at the ingress load balancer. You can create either a wildcard `*.apps.{baseDomain}.` or specific records. You can use A, CNAME, and other records per your requirements.

**Prerequisites**

* Ensure you defined the variables in the *Exporting common variables* section.
* Remove the DNS Zone configuration when creating Kubernetes manifests and generating Ignition configs.
* Ensure the bootstrap process completed successfully.

**Procedure**

1. Wait for the Ingress router to create a load balancer and populate the `EXTERNAL-IP` field:

   ```
   $ oc -n openshift-ingress get service router-default
   ```

   **Example output**

   ```
   NAME             TYPE           CLUSTER-IP      EXTERNAL-IP      PORT(S)                      AGE
   router-default   LoadBalancer   172.30.18.154   35.233.157.184   80:32288/TCP,443:31215/TCP   98
   ```
2. Add the A record to your zones:

   * To use A records:

     1. Export the variable for the router IP address:

        ```
        $ export ROUTER_IP=`oc -n openshift-ingress get service router-default --no-headers | awk '{print $4}'`
        ```
     2. Add the A record to the private zones:

        ```
        $ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
        ```

        ```
        $ gcloud dns record-sets transaction start --zone ${INFRA_ID}-private-zone
        ```

        ```
        $ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${INFRA_ID}-private-zone
        ```

        ```
        $ gcloud dns record-sets transaction execute --zone ${INFRA_ID}-private-zone
        ```
     3. For an external cluster, also add the A record to the public zones:

        ```
        $ if [ -f transaction.yaml ]; then rm transaction.yaml; fi
        ```

        ```
        $ gcloud dns record-sets transaction start --zone ${BASE_DOMAIN_ZONE_NAME}
        ```

        ```
        $ gcloud dns record-sets transaction add ${ROUTER_IP} --name \*.apps.${CLUSTER_NAME}.${BASE_DOMAIN}. --ttl 300 --type A --zone ${BASE_DOMAIN_ZONE_NAME}
        ```

        ```
        $ gcloud dns record-sets transaction execute --zone ${BASE_DOMAIN_ZONE_NAME}
        ```
   * To add explicit domains instead of using a wildcard, create entries for each of the cluster’s current routes:

     ```
     $ oc get --all-namespaces -o jsonpath='{range .items[*]}{range .status.ingress[*]}{.host}{"\n"}{end}{end}' routes
     ```

     **Example output**

     ```
     oauth-openshift.apps.your.cluster.domain.example.com
     console-openshift-console.apps.your.cluster.domain.example.com
     downloads-openshift-console.apps.your.cluster.domain.example.com
     alertmanager-main-openshift-monitoring.apps.your.cluster.domain.example.com
     prometheus-k8s-openshift-monitoring.apps.your.cluster.domain.example.com
     ```

### [11.23. Completing a Google Cloud installation on user-provisioned infrastructure](#installation-gcp-user-infra-installation_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

After you start the OpenShift Container Platform installation on Google Cloud user-provisioned infrastructure, you can monitor the cluster events until the cluster is ready.

**Prerequisites**

* Ensure the bootstrap process completed successfully.

**Procedure**

1. Complete the cluster installation:

   ```
   $ ./openshift-install --dir <installation_directory> wait-for install-complete
   ```

   1

   **Example output**

   ```
   INFO Waiting up to 30m0s for the cluster to initialize...
   ```

   [1](#CO26-1)
   :   For `<installation_directory>`, specify the path to the directory that you stored the installation files in.

   Important

   * The Ignition config files that the installation program generates contain certificates that expire after 24 hours, which are then renewed at that time. If the cluster is shut down before renewing the certificates and the cluster is later restarted after the 24 hours have elapsed, the cluster automatically recovers the expired certificates. The exception is that you must manually approve the pending `node-bootstrapper` certificate signing requests (CSRs) to recover kubelet certificates. See the documentation for *Recovering from expired control plane certificates* for more information.
   * It is recommended that you use Ignition config files within 12 hours after they are generated because the 24-hour certificate rotates from 16 to 22 hours after the cluster is installed. By using the Ignition config files within 12 hours, you can avoid installation failure if the certificate update runs during installation.
2. Observe the running state of your cluster.

   1. Run the following command to view the current cluster version and status:

      ```
      $ oc get clusterversion
      ```

      **Example output**

      ```
      NAME      VERSION   AVAILABLE   PROGRESSING   SINCE   STATUS
      version             False       True          24m     Working towards 4.5.4: 99% complete
      ```
   2. Run the following command to view the Operators managed on the control plane by the Cluster Version Operator (CVO):

      ```
      $ oc get clusteroperators
      ```

      **Example output**

      ```
      NAME                                       VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE
      authentication                             4.5.4     True        False         False      7m56s
      cloud-credential                           4.5.4     True        False         False      31m
      cluster-autoscaler                         4.5.4     True        False         False      16m
      console                                    4.5.4     True        False         False      10m
      csi-snapshot-controller                    4.5.4     True        False         False      16m
      dns                                        4.5.4     True        False         False      22m
      etcd                                       4.5.4     False       False         False      25s
      image-registry                             4.5.4     True        False         False      16m
      ingress                                    4.5.4     True        False         False      16m
      insights                                   4.5.4     True        False         False      17m
      kube-apiserver                             4.5.4     True        False         False      19m
      kube-controller-manager                    4.5.4     True        False         False      20m
      kube-scheduler                             4.5.4     True        False         False      20m
      kube-storage-version-migrator              4.5.4     True        False         False      16m
      machine-api                                4.5.4     True        False         False      22m
      machine-config                             4.5.4     True        False         False      22m
      marketplace                                4.5.4     True        False         False      16m
      monitoring                                 4.5.4     True        False         False      10m
      network                                    4.5.4     True        False         False      23m
      node-tuning                                4.5.4     True        False         False      23m
      openshift-apiserver                        4.5.4     True        False         False      17m
      openshift-controller-manager               4.5.4     True        False         False      15m
      openshift-samples                          4.5.4     True        False         False      16m
      operator-lifecycle-manager                 4.5.4     True        False         False      22m
      operator-lifecycle-manager-catalog         4.5.4     True        False         False      22m
      operator-lifecycle-manager-packageserver   4.5.4     True        False         False      18m
      service-ca                                 4.5.4     True        False         False      23m
      service-catalog-apiserver                  4.5.4     True        False         False      23m
      service-catalog-controller-manager         4.5.4     True        False         False      23m
      storage                                    4.5.4     True        False         False      17m
      ```
   3. Run the following command to view your cluster pods:

      ```
      $ oc get pods --all-namespaces
      ```

      **Example output**

      ```
      NAMESPACE                                               NAME                                                                READY     STATUS      RESTARTS   AGE
      kube-system                                             etcd-member-ip-10-0-3-111.us-east-2.compute.internal                1/1       Running     0          35m
      kube-system                                             etcd-member-ip-10-0-3-239.us-east-2.compute.internal                1/1       Running     0          37m
      kube-system                                             etcd-member-ip-10-0-3-24.us-east-2.compute.internal                 1/1       Running     0          35m
      openshift-apiserver-operator                            openshift-apiserver-operator-6d6674f4f4-h7t2t                       1/1       Running     1          37m
      openshift-apiserver                                     apiserver-fm48r                                                     1/1       Running     0          30m
      openshift-apiserver                                     apiserver-fxkvv                                                     1/1       Running     0          29m
      openshift-apiserver                                     apiserver-q85nm                                                     1/1       Running     0          29m
      ...
      openshift-service-ca-operator                           openshift-service-ca-operator-66ff6dc6cd-9r257                      1/1       Running     0          37m
      openshift-service-ca                                    apiservice-cabundle-injector-695b6bcbc-cl5hm                        1/1       Running     0          35m
      openshift-service-ca                                    configmap-cabundle-injector-8498544d7-25qn6                         1/1       Running     0          35m
      openshift-service-ca                                    service-serving-cert-signer-6445fc9c6-wqdqn                         1/1       Running     0          35m
      openshift-service-catalog-apiserver-operator            openshift-service-catalog-apiserver-operator-549f44668b-b5q2w       1/1       Running     0          32m
      openshift-service-catalog-controller-manager-operator   openshift-service-catalog-controller-manager-operator-b78cr2lnm     1/1       Running     0          31m
      ```

      When the current cluster version is `AVAILABLE`, the installation is complete.

### [11.24. Telemetry access for OpenShift Container Platform](#cluster-telemetry_installing-restricted-networks-gcp) Copy linkLink copied to clipboard!

To provide metrics about cluster health and the success of updates, the Telemetry service requires internet access. When connected, this service runs automatically by default and registers your cluster to [OpenShift Cluster Manager](https://console.redhat.com/openshift).

After you confirm that your [OpenShift Cluster Manager](https://console.redhat.com/openshift) inventory is correct, either maintained automatically by Telemetry or manually by using OpenShift Cluster Manager,use subscription watch to track your OpenShift Container Platform subscriptions at the account or multi-cluster level. For more information about subscription watch, see "Data Gathered and Used by Red Hat’s subscription services" in the *Additional resources* section.

### [11.25. Next steps](#next-steps-8) Copy linkLink copied to clipboard!

* [Customize your cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#available_cluster_customizations).
* [Configure image streams](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/postinstallation_configuration/#post-install-must-gather-disconnected) for the Cluster Samples Operator and the `must-gather` tool.
* Learn how to [Use Operator Lifecycle Manager in disconnected environments](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/disconnected_environments/#olm-restricted-networks).
* If the mirror registry that you used to install your cluster has a trusted CA, add it to the cluster by [configuring additional trust stores](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/images/#images-configuration-cas_image-configuration).
* If necessary, you can [Remote health reporting](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#remote-health-reporting).
* If necessary, see [Registering your disconnected cluster](https://docs.redhat.com/en/documentation/openshift_container_platform/4.22/html-single/support/#insights-operator-register-disconnected-cluster_remote-health-reporting)

## [Chapter 12. Installing a three-node cluster on Google Cloud](#installing-gcp-three-node) Copy linkLink copied to clipboard!

In OpenShift Container Platform version 4.22, you can install a three-node cluster on Google Cloud. A three-node cluster consists of three control plane machines, which also act as compute machines. This type of cluster provides a smaller, more resource efficient cluster, for cluster administrators and developers to use for testing, development, and production.

You can install a three-node cluster by using either installer-provisioned or user-provisioned infrastructure.

### [12.1. Configuring a three-node cluster](#installation-three-node-cluster_installing-gcp-three-node) Copy linkLink copied to clipboard!

To configure a three-node cluster, set the number of worker nodes to `0` in the `install-config.yaml` file before you deploy the cluster.

Setting the number of worker nodes to `0` ensures that the control plane machines are schedulable. This allows application workloads to be scheduled to run from the control plane nodes.

Note

Because application workloads run from control plane nodes, additional subscriptions are required, as the control plane nodes are considered to be compute nodes.

**Prerequisites**

* You have an existing `install-config.yaml` file.

**Procedure**

1. Set the number of compute replicas to `0` in your `install-config.yaml` file, as shown in the following `compute` stanza:

   **Example `install-config.yaml` file for a three-node cluster**

   ```
   apiVersion: v1
   baseDomain: example.com
   compute:
   - name: worker
     platform: {}
     replicas: 0
   # ...
   ```
2. If you are deploying a cluster with user-provisioned infrastructure:

   * After you create the Kubernetes manifest files, make sure that the `spec.mastersSchedulable` parameter is set to `true` in `cluster-scheduler-02-config.yml` file. You can locate this file in `<installation_directory>/manifests`. For more information, see "Creating the Kubernetes manifest and Ignition config files" in "Installing a cluster on user-provisioned infrastructure in Google Cloud by using Infrastructure Manager templates".
   * Do not create additional worker nodes.

   **Example `cluster-scheduler-02-config.yml` file for a three-node cluster**

   ```
   apiVersion: config.openshift.io/v1
   kind: Scheduler
   metadata:
     creationTimestamp: null
     name: cluster
   spec:
     mastersSchedulable: true
     policy:
       name: ""
   status: {}
   ```

## [Chapter 13. Installation configuration parameters for Google Cloud](#installation-config-parameters-gcp) Copy linkLink copied to clipboard!

Before you deploy an OpenShift Container Platform cluster on Google Cloud, you create the `install-config.yaml` file and provide parameters to customize your cluster and the platform that hosts it. You can then modify the `install-config.yaml` file to customize your cluster further.

### [13.1. Available installation configuration parameters for Google Cloud](#installation-configuration-parameters_installation-config-parameters-gcp) Copy linkLink copied to clipboard!

To customize your cluster installation, you can use configuration parameters in the `install-config.yaml` file.

The following tables specify the required, optional, and Google Cloud-specific installation configuration parameters that you can set as part of the installation process.

Important

After installation, you cannot change these parameters in the `install-config.yaml` file.

#### [13.1.1. Required configuration parameters](#installation-configuration-parameters-required_installation-config-parameters-gcp) Copy linkLink copied to clipboard!

Required installation configuration parameters are described in the following table:

Expand

Table 13.1. Required parameters

| Parameter | Description |
| --- | --- |
| ``` apiVersion: ``` | The API version for the `install-config.yaml` content. The current version is `v1`. The installation program might also support older API versions.  **Value:** String |
| ``` baseDomain: ``` | The base domain of your cloud provider. The base domain is used to create routes to your OpenShift Container Platform cluster components. The full DNS name for your cluster is a combination of the `baseDomain` and `metadata.name` parameter values that uses the `<metadata.name>.<baseDomain>` format.  **Value:** A fully-qualified domain or subdomain name, such as `example.com`. |
| ``` metadata: ``` | Kubernetes resource `ObjectMeta`, from which only the `name` parameter is consumed.  **Value:** Object |
| ``` metadata:   name: ``` | The name of the cluster. DNS records for the cluster are all subdomains of `{{.metadata.name}}.{{.baseDomain}}`.  **Value:** String of lowercase letters, hyphens (`-`), and periods (`.`), such as `dev`. |
| ``` platform: ``` | The configuration for the specific platform upon which to perform the installation: `aws`, `baremetal`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}`. For additional information about `platform.<platform>` parameters, consult the table for your specific platform that follows.  **Value:** Object |
| ``` pullSecret: ``` | Get a [pull secret from Red Hat OpenShift Cluster Manager](https://console.redhat.com/openshift/install/pull-secret) to authenticate downloading container images for OpenShift Container Platform components from services such as Quay.io.  **Value:**  ``` {    "auths":{       "cloud.openshift.com":{          "auth":"b3Blb=",          "email":"you@example.com"       },       "quay.io":{          "auth":"b3Blb=",          "email":"you@example.com"       }    } } ``` |

Show more

#### [13.1.2. Network configuration parameters](#installation-configuration-parameters-network_installation-config-parameters-gcp) Copy linkLink copied to clipboard!

You can customize your installation configuration based on the requirements of your existing network infrastructure. For example, you can expand the IP address block for the cluster network or configure different IP address blocks than the defaults.

Only IPv4 addresses are supported.

Expand

Table 13.2. Network parameters

| Parameter | Description |
| --- | --- |
| ``` networking: ``` | The configuration for the cluster network.  **Value:** Object  Note  You cannot change parameters specified by the `networking` object after installation. |
| ``` networking:   networkType: ``` | The Red Hat OpenShift Networking network plugin to install.  **Value:**`OVNKubernetes`. `OVNKubernetes` is a Container Network Interface (CNI) plugin for Linux networks and hybrid networks that contain both Linux and Windows servers. The default value is `OVNKubernetes`. |
| ``` networking:   clusterNetwork: ``` | The IP address blocks for pods.  The default value is `10.128.0.0/14` with a host prefix of `/23`.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  ``` networking:   clusterNetwork:   - cidr: 10.128.0.0/14     hostPrefix: 23 ``` |
| ``` networking:   clusterNetwork:     cidr: ``` | Required if you use `networking.clusterNetwork`. An IP address block.  An IPv4 network. |
| ``` networking:   clusterNetwork:     hostPrefix: ``` | The subnet prefix length to assign to each individual node. For example, if `hostPrefix` is set to `23` then each node is assigned a `/23` subnet out of the given `cidr`. A `hostPrefix` value of `23` provides 510 (2^(32 - 23) - 2) pod IP addresses.  **Value:** A subnet prefix.  The default value is `23`. |
| ``` networking:   serviceNetwork: ``` | The IP address block for services. The default value is `172.30.0.0/16`.  **Value:** An array with an IP address block in CIDR format. For example:  ``` networking:   serviceNetwork:    - 172.30.0.0/16 ``` |
| ``` networking:   machineNetwork: ``` | The IP address blocks for machines.  If you specify multiple IP address blocks, the blocks must not overlap.  **Value:** An array of objects. For example:  ``` networking:   machineNetwork:   - cidr: 10.0.0.0/16 ``` |
| ``` networking:   machineNetwork:     cidr: ``` | Required if you use `networking.machineNetwork`. An IP address block. The default value is `10.0.0.0/16` for all platforms other than libvirt and IBM Power® Virtual Server. For libvirt, the default value is `192.168.126.0/24`. For IBM Power® Virtual Server, the default value is `192.168.0.0/24`.  **Value:** An IP network block in CIDR notation.  For example, `10.0.0.0/16`.  Note  Set the `networking.machineNetwork` to match the CIDR of the preferred NIC.  If you are installing a cluster on AWS with dual-stack networking, consider the following distinction:  * If the installation program creates the VPC, do not specify an IPv6 entry in `networking.machineNetwork`. The installation program will assign an IPv6 address to the VPC. * If you provide existing dual-stack subnets using the `platform.aws.vpc.subnets` parameter, you must specify IPv6 entries corresponding to either the VPC CIDR or the CIDR of the subnets. * In both cases, you must provide an IPv4 CIDR entry. |
| ``` networking:   ovnKubernetesConfig:     ipv4:       internalJoinSubnet: ``` | Configures the IPv4 join subnet that is used internally by `ovn-kubernetes`. This subnet must not overlap with any other subnet that OpenShift Container Platform is using, including the node network. The size of the subnet must be larger than the number of nodes. You cannot change the value after installation.  **Value:** An IP network block in CIDR notation. The default value is `100.64.0.0/16`. |

Show more

#### [13.1.3. Optional configuration parameters](#installation-configuration-parameters-optional_installation-config-parameters-gcp) Copy linkLink copied to clipboard!

Optional installation configuration parameters are described in the following table:

Expand

Table 13.3. Optional parameters

| Parameter | Description |
| --- | --- |
| ``` additionalTrustBundle: ``` | A PEM-encoded X.509 certificate bundle that is added to the nodes' trusted certificate store. This trust bundle might also be used when a proxy has been configured.  **Value:** String |
| ``` capabilities: ``` | Controls the installation of optional core cluster components. You can reduce the footprint of your OpenShift Container Platform cluster by disabling optional components. For more information, see the "Cluster capabilities" page in *Installing*.  **Value:** String array |
| ``` capabilities:   baselineCapabilitySet: ``` | Selects an initial set of optional capabilities to enable. Valid values are `None`, `v4.11`, `v4.12` and `vCurrent`. The default value is `vCurrent`.  **Value:** String |
| ``` capabilities:   additionalEnabledCapabilities: ``` | Extends the set of optional capabilities beyond what you specify in `baselineCapabilitySet`. You can specify multiple capabilities in this parameter.  **Value:** String array |
| ``` cpuPartitioningMode: ``` | Enables workload partitioning, which isolates OpenShift Container Platform services, cluster management workloads, and infrastructure pods to run on a reserved set of CPUs. You can only enable workload partitioning during installation. You cannot disable it after installation. While this field enables workload partitioning, it does not configure workloads to use specific CPUs. For more information, see the *Workload partitioning* page in the *Scalability and Performance* section.  **Value:** `None` or `AllNodes`. `None` is the default value. |
| ``` compute: ``` | The configuration for the machines that comprise the compute nodes.  **Value:** Array of `MachinePool` objects. |
| ``` compute:   architecture: ``` | Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are `amd64` and `arm64`.  **Value:** String |
| ``` compute:   hyperthreading: ``` | Whether to enable or disable simultaneous multithreading, or `hyperthreading`, on compute machines. By default, simultaneous multithreading is enabled to increase the performance of your machines' cores.  Important  If you disable simultaneous multithreading, ensure that your capacity planning accounts for the dramatically decreased machine performance.  **Value:** `Enabled` or `Disabled` |
| ``` compute:   name: ``` | Required if you use `compute`. The name of the machine pool.  **Value:** `worker` |
| ``` compute:   platform: ``` | Required if you use `compute`. Use this parameter to specify the cloud provider to host the worker machines. This parameter value must match the `controlPlane.platform` parameter value.  **Value:**`aws`, `azure`, `gcp`, `ibmcloud`, `nutanix`, `openstack`, `powervs`, `vsphere`, or `{}` |
| ``` compute:   replicas: ``` | The number of compute machines, which are also known as worker machines, to provision.  **Value:** A positive integer greater than or equal to `2`. The default value is `3`. |
| ``` featureSet: ``` | Enables the cluster for a feature set. A feature set is a collection of OpenShift Container Platform features that are not enabled by default. For more information about enabling a feature set during installation, see "Enabling features using feature gates".  **Value:** String. The name of the feature set to enable, such as `TechPreviewNoUpgrade`. |
| ``` controlPlane: ``` | The configuration for the machines that form the control plane.  **Value:** Array of `MachinePool` objects. |
| ``` controlPlane:   architecture: ``` | Determines the instruction set architecture of the machines in the pool. Currently, clusters with varied architectures are not supported. All pools must specify the same architecture. Valid values are `amd64` and `arm64`.  **Value:** String |
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
| ``` publish: ``` | How to publish or expose the user-facing endpoints of your cluster, such as the Kubernetes API, OpenShift routes.  **Value:**`Internal` or `External`. To deploy a private cluster that cannot be accessed from the internet, set the `publish` parameter to `Internal`. The default value is `External`. |
| ``` sshKey: ``` | The SSH key to authenticate access to your cluster machines.  Note  For production OpenShift Container Platform clusters on which you want to perform installation debugging or disaster recovery, specify an SSH key that your `ssh-agent` process uses.  **Value:** For example, `sshKey: ssh-ed25519 AAAA..`. |

Show more

Note

If you are installing on Google Cloud into a shared virtual private cloud (VPC), `credentialsMode` must be set to `Passthrough` or `Manual`.

Important

Setting this parameter to `Manual` enables alternatives to storing administrator-level secrets in the `kube-system` project, which require additional configuration steps. For more information, see "Alternatives to storing administrator-level secrets in the kube-system project".

#### [13.1.4. Additional Google Cloud configuration parameters](#installation-configuration-parameters-additional-gcp_installation-config-parameters-gcp) Copy linkLink copied to clipboard!

Additional Google Cloud configuration parameters are described in the following table:

Expand

Table 13.4. Additional Google Cloud parameters

| Parameter | Description |
| --- | --- |
| ``` controlPlane:   platform:     gcp:       osImage:         project: ``` | Optional. By default, the installation program downloads and installs the Red Hat Enterprise Linux CoreOS (RHCOS) image that is used to boot control plane machines. You can override the default behavior by specifying the location of a custom RHCOS image that the installation program is to use for control plane machines only. Control plane machines do not contribute to licensing costs when using the default image. But, if you apply a Google Cloud Marketplace image for a control plane machine, usage costs do apply.  **Value:** String. The name of Google Cloud project where the image is located. |
| ``` controlPlane:   platform:     gcp:       osImage:         name: ``` | The name of the custom RHCOS image that the installation program is to use to boot control plane machines. If you use `controlPlane.platform.gcp.osImage.project`, this field is required.  **Value:** String. The name of the RHCOS image. |
| ``` compute:   platform:     gcp:       osImage:         project: ``` | Optional. By default, the installation program downloads and installs the RHCOS image that is used to boot compute machines. You can override the default behavior by specifying the location of a custom RHCOS image that the installation program is to use for compute machines only.  **Value:** String. The name of Google Cloud project where the image is located. |
| ``` compute:   platform:     gcp:       osImage:         name: ``` | The name of the custom RHCOS image that the installation program is to use to boot compute machines. If you use `compute.platform.gcp.osImage.project`, this field is required.  **Value:** String. The name of the RHCOS image. |
| ``` compute:   platform:     gcp:       serviceAccount: ``` | Specifies the email address of a Google Cloud service account to be used during installations. This service account is used to provision compute machines.  **Value:** String. The email address of the service account. |
| ``` platform:   gcp:     firewallRulesManagement: ``` | Specifies the firewall management policy for the cluster. `Managed` indicates that the firewall rules will be created and destroyed by the cluster. `Unmanaged` indicates that the user should create and destroy the firewall rules. For shared VPC installation, if the credential you provided the installation program doesn’t have firewall rules management permissions, the `firewallRulesManagement` parameter can be absent or set to `Unmanaged`. For non-shared VPC installation, if the credential you provided the installation program doesn’t have firewall rules management permissions, the `firewallRulesManagement` parameter must be set to `Unmanaged`. If you manage your own firewall rules, you must pre-configure the VPC network and the firewall rules before the installation.  **Value:** String. `Managed` or `Unmanaged`. The default value is `Managed`. |
| ``` platform:   gcp:     network: ``` | The name of the existing Virtual Private Cloud (VPC) where you want to deploy your cluster. If you want to deploy your cluster into a shared VPC, you must set `platform.gcp.networkProjectID` with the name of the Google Cloud project that contains the shared VPC.  **Value:** String. |
| ``` platform:   gcp:     networkProjectID: ``` | Optional. The name of the Google Cloud project that contains the shared VPC where you want to deploy your cluster.  **Value:** String. |
| ``` platform:   gcp:     projectID: ``` | The name of the Google Cloud project where the installation program installs the cluster.  **Value:** String. |
| ``` platform:   gcp:     dns:       privateZone:         name: ``` | The name of the private DNS zone. This parameter is only used during shared VPC installations. You can use a private DNS zone in a service project that is distinct from the projects specified by the `projectID` or `networkProjectID` parameters.  **Value:** String. |
| ``` platform:   gcp:     dns:       privateZone:         projectID: ``` | The ID of the project that contains the private zone from the `privateZone.name` parameter.  **Value:** String. |
| ``` platform:   gcp:     userProvisionedDNS: ``` | Enables user-provisioned DNS instead of the default cluster-provisioned DNS solution. If you use this feature, you must provide your own DNS solution that includes records for `api.<cluster_name>.<base_domain>.` and `*.apps.<cluster_name>.<base_domain>.`.  **Value:** `Enabled` or `Disabled`. The default value is `Disabled`. |
| ``` platform:   gcp:     region: ``` | The name of the Google Cloud region that hosts your cluster.  **Value:** Any valid region name, such as `us-central1`. |
| ``` platform:   gcp:     controlPlaneSubnet: ``` | The name of the existing subnet where you want to deploy your control plane machines.  **Value:** The subnet name. |
| ``` platform:   gcp:     computeSubnet: ``` | The name of the existing subnet where you want to deploy your compute machines.  **Value:** The subnet name. |
| ``` platform:   gcp:     defaultMachinePlatform:       zones: ``` | The availability zones where the installation program creates machines.  **Value:** A list of valid [Google Cloud availability zones](https://cloud.google.com/compute/docs/regions-zones#available), such as `us-central1-a`, in a [YAML sequence](https://yaml.org/spec/1.2/spec.html#sequence//).  Important  When running your cluster on Google Cloud 64-bit ARM infrastructures, ensure that you use a zone where Ampere Altra Arm CPU’s are available. You can find which zones are compatible with 64-bit ARM processors in the "Google Cloud availability zones" link. |
| ``` platform:   gcp:     defaultMachinePlatform:       osDisk:         diskSizeGB: ``` | The size of the disk in gigabytes (GB).  **Value:** Any size between 16 GB and 65536 GB. |
| ``` platform:   gcp:     defaultMachinePlatform:       osDisk:         diskType: ``` | The [Google Cloud disk type](https://cloud.google.com/compute/docs/disks#disk-types).  **Value:** The default disk type for all machines. Valid values are `pd-balanced`, `pd-ssd`, `pd-standard`, or `hyperdisk-balanced`. The default value is `pd-ssd`. Control plane machines cannot use the `pd-standard` disk type, so if you specify `pd-standard` as the default machine platform disk type, you must specify a different disk type using the `controlPlane.platform.gcp.osDisk.diskType` parameter. |
| ``` platform:   gcp:     defaultMachinePlatform:       osImage:         project: ``` | Optional. By default, the installation program downloads and installs the RHCOS image that is used to boot control plane and compute machines. You can override the default behavior by specifying the location of a custom RHCOS image that the installation program is to use for both types of machines.  **Value:** String. The name of Google Cloud project where the image is located. |
| ``` platform:   gcp:     defaultMachinePlatform:       osImage:         name: ``` | The name of the custom RHCOS image that the installation program is to use to boot control plane and compute machines. If you use `platform.gcp.defaultMachinePlatform.osImage.project`, this field is required.  **Value:** String. The name of the RHCOS image. |
| ``` platform:   gcp:     defaultMachinePlatform:       tags: ``` | Optional. Additional network tags to add to the control plane and compute machines.  **Value:** One or more strings, for example `network-tag1`. |
| ``` platform:   gcp:     defaultMachinePlatform:       type: ``` | The [Google Cloud machine type](https://cloud.google.com/compute/docs/machine-types) for control plane and compute machines.  **Value:** The Google Cloud machine type, for example `n1-standard-4`. |
| ``` platform:   gcp:     defaultMachinePlatform:       osDisk:         encryptionKey:           kmsKey:             name: ``` | The name of the customer managed encryption key to be used for machine disk encryption.  **Value:** The encryption key name. |
| ``` platform:   gcp:     defaultMachinePlatform:       osDisk:         encryptionKey:           kmsKey:             keyRing: ``` | The name of the Key Management Service (KMS) key ring to which the KMS key belongs.  **Value:** The KMS key ring name. |
| ``` platform:   gcp:     defaultMachinePlatform:       osDisk:         encryptionKey:           kmsKey:             location: ``` | The [Google Cloud location](https://cloud.google.com/kms/docs/locations) in which the KMS key ring exists.  **Value:** The Google Cloud location. |
| ``` platform:   gcp:     defaultMachinePlatform:       osDisk:         encryptionKey:           kmsKey:             projectID: ``` | The ID of the project in which the KMS key ring exists. This value defaults to the value of the `platform.gcp.projectID` parameter if it is not set.  **Value:** The Google Cloud project ID. |
| ``` platform:   gcp:     defaultMachinePlatform:       osDisk:         encryptionKey:           kmsKeyServiceAccount: ``` | The Google Cloud service account used for the encryption request for control plane and compute machines. If absent, the Compute Engine default service account is used. For more information about Google Cloud service accounts, see Google’s documentation on [service accounts](https://cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account).  **Value:** The Google Cloud service account email, for example `<service_account_name>@<project_id>.iam.gserviceaccount.com`. |
| ``` platform:   gcp:     defaultMachinePlatform:       secureBoot: ``` | Whether to enable Shielded VM secure boot for all machines in the cluster. Shielded VMs have additional security protocols such as secure boot, firmware and integrity monitoring, and rootkit protection. For more information on Shielded VMs, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).  **Value:** `Enabled` or `Disabled`. The default value is `Disabled`. |
| ``` platform:   gcp:     defaultMachinePlatform:       confidentialCompute: ``` | Whether to use Confidential VMs for all machines in the cluster. Confidential VMs provide encryption for data during processing. For more information on Confidential computing, see Google’s documentation about [Confidential Computing](https://cloud.google.com/confidential-computing).  Supported values are:  * `Enabled`, which automatically selects a Confidential Computing platform  Important  The `Enabled` value selects Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV), which is deprecated. * `Disabled`, which disables Confidential Computing * `AMDEncryptedVirtualizationNestedPaging`, which enables Confidential Computing with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP) * `AMDEncryptedVirtualization`, which enables Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV)  Important  The use of Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV) has been deprecated and will be removed in a future release. * `IntelTrustedDomainExtensions`, which enables Confidential Computing with Intel Trusted Domain Extensions (Intel TDX)  If you specify any value other than `Disabled`, you must set `platform.gcp.defaultMachinePlatform.onHostMaintenance` to `Terminate`, and you must specify a region and machine type that support Confidential Computing. For more information, see Google’s documentation about [Supported configurations](https://cloud.google.com/confidential-computing/confidential-vm/docs/supported-configurations#machine-type-cpu-zone).  **Value:** String. |
| ``` platform:   gcp:     defaultMachinePlatform:       onHostMaintenance: ``` | Specifies the behavior of all VMs during a host maintenance event, such as a software or hardware update. For Confidential VMs, this parameter must be set to `Terminate`. Confidential VMs do not support live VM migration.  **Value:** `Terminate` or `Migrate`. The default value is `Migrate`. |
| ``` controlPlane:   platform:     gcp:       osDisk:         encryptionKey:           kmsKey:             name: ``` | The name of the customer managed encryption key to be used for control plane machine disk encryption.  **Value:** The encryption key name. |
| ``` controlPlane:   platform:     gcp:       osDisk:         encryptionKey:           kmsKey:             keyRing: ``` | For control plane machines, the name of the KMS key ring to which the KMS key belongs.  **Value:** The KMS key ring name. |
| ``` controlPlane:   platform:     gcp:       osDisk:         encryptionKey:           kmsKey:             location: ``` | For control plane machines, the Google Cloud location in which the key ring exists. For more information about KMS locations, see Google’s documentation on [Cloud KMS locations](https://cloud.google.com/kms/docs/locations).  **Value:** The Google Cloud location for the key ring. |
| ``` controlPlane:   platform:     gcp:       osDisk:         encryptionKey:           kmsKey:             projectID: ``` | For control plane machines, the ID of the project in which the KMS key ring exists. This value defaults to the VM project ID if not set.  **Value:** The Google Cloud project ID. |
| ``` controlPlane:   platform:     gcp:       osDisk:         encryptionKey:           kmsKeyServiceAccount: ``` | The Google Cloud service account used for the encryption request for control plane machines. If absent, the Compute Engine default service account is used. For more information about Google Cloud service accounts, see Google’s documentation on [service accounts](https://cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account).  **Value:** The Google Cloud service account email, for example `<service_account_name>@<project_id>.iam.gserviceaccount.com`. |
| ``` controlPlane:   platform:     gcp:       osDisk:         diskSizeGB: ``` | The size of the disk in gigabytes (GB). This value applies to control plane machines.  **Value:** Any integer between 16 and 65536. |
| ``` controlPlane:   platform:     gcp:       osDisk:         diskType: ``` | The [Google Cloud disk type](https://cloud.google.com/compute/docs/disks#disk-types) for control plane machines.  **Value:** Valid values are `pd-balanced`, `pd-ssd`, or `hyperdisk-balanced`. The default value is `pd-ssd`. |
| ``` controlPlane:   platform:     gcp:       tags: ``` | Optional. Additional network tags to add to the control plane machines. If set, this parameter overrides the `platform.gcp.defaultMachinePlatform.tags` parameter for control plane machines.  **Value:** One or more strings, for example `control-plane-tag1`. |
| ``` controlPlane:   platform:     gcp:       type: ``` | The [Google Cloud machine type](https://cloud.google.com/compute/docs/machine-types) for control plane machines. If set, this parameter overrides the `platform.gcp.defaultMachinePlatform.type` parameter.  **Value:** The Google Cloud machine type, for example `n1-standard-4`. |
| ``` controlPlane:   platform:     gcp:       zones: ``` | The availability zones where the installation program creates control plane machines.  **Value:** A list of valid [Google Cloud availability zones](https://cloud.google.com/compute/docs/regions-zones#available), such as `us-central1-a`, in a [YAML sequence](https://yaml.org/spec/1.2/spec.html#sequence//).  Important  When running your cluster on Google Cloud 64-bit ARM infrastructures, ensure that you use a zone where Ampere Altra Arm CPU’s are available. You can find which zones are compatible with 64-bit ARM processors in the "Google Cloud availability zones" link. |
| ``` controlPlane:   platform:     gcp:       secureBoot: ``` | Whether to enable Shielded VM secure boot for control plane machines. Shielded VMs have additional security protocols such as secure boot, firmware and integrity monitoring, and rootkit protection. For more information on Shielded VMs, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).  **Value:** `Enabled` or `Disabled`. The default value is `Disabled`. |
| ``` controlPlane:   platform:     gcp:       confidentialCompute: ``` | Whether to use Confidential VMs for control plane machines. Confidential VMs provide encryption for data during processing. For more information on Confidential computing, see Google’s documentation about [Confidential Computing](https://cloud.google.com/confidential-computing).  Supported values are:  * `Enabled`, which automatically selects a Confidential Computing platform  Important  The `Enabled` value selects Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV), which is deprecated. * `Disabled`, which disables Confidential Computing * `AMDEncryptedVirtualizationNestedPaging`, which enables Confidential Computing with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP) * `AMDEncryptedVirtualization`, which enables Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV)  Important  The use of Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV) has been deprecated and will be removed in a future release. * `IntelTrustedDomainExtensions`, which enables Confidential Computing with Intel Trusted Domain Extensions (Intel TDX)  If you specify any value other than `Disabled`, you must set `controlPlane.platform.gcp.defaultMachinePlatform.onHostMaintenance` to `Terminate`.  **Value:** String. |
| ``` controlPlane:   platform:     gcp:       onHostMaintenance: ``` | Specifies the behavior of control plane VMs during a host maintenance event, such as a software or hardware update. For Confidential VMs, this parameter must be set to `Terminate`. Confidential VMs do not support live VM migration.  **Value:** `Terminate` or `Migrate`. The default value is `Migrate`. |
| ``` controlPlane:   platform:     gcp:       serviceAccount: ``` | Specifies the email address of a Google Cloud service account to be used during installations. This service account is used to provision control plane machines.  Important  In the case of shared VPC installations, when the service account is not provided, the installation program service account must have the `resourcemanager.projects.getIamPolicy` and `resourcemanager.projects.setIamPolicy` permissions in the host project.  **Value:** String. The email address of the service account. |
| ``` compute:   platform:     gcp:       osDisk:         encryptionKey:           kmsKey:             name: ``` | The name of the customer managed encryption key to be used for compute machine disk encryption.  **Value:** The encryption key name. |
| ``` compute:   platform:     gcp:       osDisk:         encryptionKey:           kmsKey:             keyRing: ``` | For compute machines, the name of the KMS key ring to which the KMS key belongs.  **Value:** The KMS key ring name. |
| ``` compute:   platform:     gcp:       osDisk:         encryptionKey:           kmsKey:             location: ``` | For compute machines, the Google Cloud location in which the key ring exists. For more information about KMS locations, see Google’s documentation on [Cloud KMS locations](https://cloud.google.com/kms/docs/locations).  **Value:** The Google Cloud location for the key ring. |
| ``` compute:   platform:     gcp:       osDisk:         encryptionKey:           kmsKey:             projectID: ``` | For compute machines, the ID of the project in which the KMS key ring exists. This value defaults to the VM project ID if not set.  **Value:** The Google Cloud project ID. |
| ``` compute:   platform:     gcp:       osDisk:         encryptionKey:           kmsKeyServiceAccount: ``` | The Google Cloud service account used for the encryption request for compute machines. If this value is not set, the Compute Engine default service account is used. For more information about Google Cloud service accounts, see Google’s documentation on [service accounts](https://cloud.google.com/compute/docs/access/service-accounts#compute_engine_service_account).  **Value:** The Google Cloud service account email, for example `<service_account_name>@<project_id>.iam.gserviceaccount.com`. |
| ``` compute:   platform:     gcp:       osDisk:         diskSizeGB: ``` | The size of the disk in gigabytes (GB). This value applies to compute machines.  **Value:** Any integer between 16 and 65536. |
| ``` compute:   platform:     gcp:       osDisk:         diskType: ``` | The [Google Cloud disk type](https://cloud.google.com/compute/docs/disks#disk-types) for compute machines.  **Value:** Valid values are `pd-balanced`, `pd-ssd`, `pd-standard`, or `hyperdisk-balanced`. The default value is `pd-ssd`. |
| ``` compute:   platform:     gcp:       tags: ``` | Optional. Additional network tags to add to the compute machines. If set, this parameter overrides the `platform.gcp.defaultMachinePlatform.tags` parameter for compute machines.  **Value:** One or more strings, for example `compute-network-tag1`. |
| ``` compute:   platform:     gcp:       type: ``` | The [Google Cloud machine type](https://cloud.google.com/compute/docs/machine-types) for compute machines. If set, this parameter overrides the `platform.gcp.defaultMachinePlatform.type` parameter.  **Value:** The Google Cloud machine type, for example `n1-standard-4`. |
| ``` compute:   platform:     gcp:       zones: ``` | The availability zones where the installation program creates compute machines.  **Value:** A list of valid [Google Cloud availability zones](https://cloud.google.com/compute/docs/regions-zones#available), such as `us-central1-a`, in a [YAML sequence](https://yaml.org/spec/1.2/spec.html#sequence//).  Important  When running your cluster on Google Cloud 64-bit ARM infrastructures, ensure that you use a zone where Ampere Altra Arm CPU’s are available. You can find which zones are compatible with 64-bit ARM processors in the "Google Cloud availability zones" link. |
| ``` compute:   platform:     gcp:       secureBoot: ``` | Whether to enable Shielded VM secure boot for compute machines. Shielded VMs have additional security protocols such as secure boot, firmware and integrity monitoring, and rootkit protection. For more information on Shielded VMs, see Google’s documentation on [Shielded VMs](https://cloud.google.com/shielded-vm).  **Value:** `Enabled` or `Disabled`. The default value is `Disabled`. |
| ``` compute:   platform:     gcp:       confidentialCompute: ``` | Whether to use Confidential VMs for compute machines. Confidential VMs provide encryption for data during processing. For more information on Confidential computing, see Google’s documentation on [Confidential computing](https://cloud.google.com/confidential-computing).  Supported values are:  * `Enabled`, which automatically selects a Confidential Computing platform  Important  The `Enabled` value selects Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV), which is deprecated. * `Disabled`, which disables Confidential Computing * `AMDEncryptedVirtualizationNestedPaging`, which enables Confidential Computing with AMD Secure Encrypted Virtualization Secure Nested Paging (AMD SEV-SNP) * `AMDEncryptedVirtualization`, which enables Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV)  Important  The use of Confidential Computing with AMD Secure Encrypted Virtualization (AMD SEV) has been deprecated and will be removed in a future release. * `IntelTrustedDomainExtensions`, which enables Confidential Computing with Intel Trusted Domain Extensions (Intel TDX)  If you specify any value other than `Disabled`, you must set `compute.platform.gcp.onHostMaintenance` to `Terminate`.  **Value:** String. |
| ``` compute:   platform:     gcp:       onHostMaintenance: ``` | Specifies the behavior of compute VMs during a host maintenance event, such as a software or hardware update. For Confidential VMs, this parameter must be set to `Terminate`. Confidential VMs do not support live VM migration.  **Value:** `Terminate` or `Migrate`. The default value is `Migrate`. |

Show more

## [Chapter 14. Uninstalling a cluster on Google Cloud](#uninstalling-cluster-gcp) Copy linkLink copied to clipboard!

You can remove a cluster that you deployed to Google Cloud and delete the associated cloud provider resources when you no longer need the cluster, to free up cloud resources and stop incurring costs.

### [14.1. Removing a cluster that uses installer-provisioned infrastructure](#installation-uninstall-clouds_uninstalling-cluster-gcp) Copy linkLink copied to clipboard!

To remove an OpenShift Container Platform cluster that uses installer-provisioned infrastructure, you can use the installation program and the installation files from your original deployment to uninstall the cluster from your cloud platform.

Note

After uninstallation, check your cloud provider for any resources that were not removed properly, especially with user-provisioned infrastructure clusters. Some resources might exist because either the installation program did not create the resource or could not access the resource. For example, some Google Cloud resources require [IAM permissions](https://cloud.google.com/iam/docs/overview#concepts_related_to_access_management) in shared VPC host projects, or there might be unused [health checks that must be deleted](https://cloud.google.com/sdk/gcloud/reference/compute/health-checks/delete).

**Prerequisites**

* You have a copy of the installation program that you used to deploy the cluster.
* You have the files that the installation program generated when you created your cluster.

**Procedure**

1. From the directory that has the installation program on the computer that you used to install the cluster, run the following command:

   ```
   $ ./openshift-install destroy cluster \
   --dir <installation_directory> --log-level info
   ```

   where:

   `<installation_directory>`
   :   Specify the path to the directory that you stored the installation files in.

   `--log-level info`
   :   To view different details, specify `warn`, `debug`, or `error` instead of `info`.

       Note

       You must specify the directory that includes the cluster definition files for your cluster. The installation program requires the `metadata.json` file in this directory to delete the cluster.
2. Optional: Delete the `<installation_directory>` directory and the OpenShift Container Platform installation program.

### [14.2. Deleting Google Cloud resources with the Cloud Credential Operator utility](#cco-ccoctl-deleting-sts-resources_uninstalling-cluster-gcp) Copy linkLink copied to clipboard!

After uninstalling an OpenShift Container Platform cluster that uses short-term credentials managed outside the cluster, you can use the Cloud Credential Operator (CCO) utility (`ccoctl`) to remove the Google Cloud resources that `ccoctl` created during installation.

**Prerequisites**

* Extract and prepare the `ccoctl` binary.
* Uninstall an OpenShift Container Platform cluster on Google Cloud that uses short-term credentials.

**Procedure**

1. Set a `$RELEASE_IMAGE` variable with the release image from your installation file by running the following command:

   ```
   $ RELEASE_IMAGE=$(./openshift-install version | awk '/release image/ {print $3}')
   ```
2. Extract the list of `CredentialsRequest` custom resources (CRs) from the OpenShift Container Platform release image by running the following command:

   ```
   $ oc adm release extract \
     --from=$RELEASE_IMAGE \
     --credentials-requests \
     --included \
     --to=<path_to_directory_for_credentials_requests>
   ```

   where:

   `--included`
   :   The parameter includes only the manifests that your specific cluster configuration requires.

   `<path_to_directory_for_credentials_requests>`
   :   Specify the path to the directory where you want to store the `CredentialsRequest` objects. If the specified directory does not exist, this command creates it.
3. Delete the Google Cloud resources that `ccoctl` created by running the following command:

   ```
   $ ccoctl gcp delete \
     --name=<name> \
     --project=<gcp_project_id> \
     --credentials-requests-dir=<path_to_credentials_requests_directory> \
     --force-delete-custom-roles
   ```

   where:

   `<name>`
   :   Matches the name that was originally used to create and tag the cloud resources.

   `<gcp_project_id>`
   :   The Google Cloud project ID in which to delete cloud resources.

   `force-delete-custom-roles`
   :   Optional: This parameter deletes the custom roles that the `ccoctl` utility creates during installation. Google Cloud does not permanently delete custom roles immediately. For more information, see Google Cloud documentation about [deleting a custom role](https://cloud.google.com/iam/docs/creating-custom-roles#deleting-custom-role).

**Verification**

* To verify that the resources are deleted, query Google Cloud. For more information, refer to Google Cloud documentation.

## [Chapter 15. Installing a cluster with the support for configuring multi-architecture compute machines](#installing-gcp-multiarch-support) Copy linkLink copied to clipboard!

You can install an OpenShift Container Platform cluster on Google Cloud with multi-architecture support to run workloads on compute machines with different CPU architectures.

Note

When you have nodes with different architectures in your cluster, the architecture of your image must be consistent with the architecture of the node. You must verify that the pod is assigned to the node with the appropriate architecture and that it matches the image architecture. For more information about assigning pods to nodes, see "Scheduling workloads on clusters with multi-architecture compute machines".

You can install a Google Cloud cluster with the support for configuring multi-architecture compute machines. After installing the Google Cloud cluster, you can add multi-architecture compute machines to the cluster in the following ways:

* Adding 64-bit x86 compute machines to a cluster that uses 64-bit ARM control plane machines and already includes 64-bit ARM compute machines. In this case, 64-bit x86 is considered the secondary architecture.
* Adding 64-bit ARM compute machines to a cluster that uses 64-bit x86 control plane machines and already includes 64-bit x86 compute machines. In this case, 64-bit ARM is considered the secondary architecture.

Note

Before adding a secondary architecture node to your cluster, it is recommended to install the Multiarch Tuning Operator, and deploy a `ClusterPodPlacementConfig` custom resource. For more information, see "Managing workloads on multi-architecture clusters by using the Multiarch Tuning Operator".

### [15.1. Installing a cluster with multi-architecture support](#installing-a-cluster-with-multiarch-support_installing-gcp-multiarch-support) Copy linkLink copied to clipboard!

You can install a cluster with multi-architecture support to use compute machines with different Central Processing Unit (CPU) architectures. Modifying your configuration file helps ensure your control plane and worker nodes deploy with the correct architecture.

**Prerequisites**

* You installed the OpenShift CLI (`oc`).
* You have the OpenShift Container Platform installation program.
* You downloaded the pull secret for your cluster.

**Procedure**

1. Check that the `openshift-install` binary is using the `multi` payload by running the following command:

   ```
   $ ./openshift-install version
   ```

   **Example output**

   ```
   ./openshift-install 4.22.0
   built from commit abc123etc
   release image quay.io/openshift-release-dev/ocp-release@sha256:abc123wxyzetc
   release architecture multi
   default architecture amd64
   ```

   The output must contain `release architecture multi` to indicate that the `openshift-install` binary is using the `multi` payload.
2. Update the `install-config.yaml` file to configure the architecture for the nodes.

   **Sample `install-config.yaml` file with multi-architecture configuration**

   ```
   apiVersion: v1
   baseDomain: example.openshift.com
   compute:
   - architecture: amd64
     hyperthreading: Enabled
     name: worker
     platform: {}
     replicas: 3
   controlPlane:
     architecture: arm64
     name: master
     platform: {}
     replicas: 3
   # ...
   ```

   where:

   `compute.architecture`
   :   Specifies the architecture of the worker node. You can set this field to either `arm64` or `amd64`.

   `controlPlane.architecture`
   :   Specifies the control plane node architecture. You can set this field to either `arm64` or `amd64`.

## [Legal Notice](#idm140613129376576) Copy linkLink copied to clipboard!

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
